#!/usr/bin/env python3
"""Canonical tag-vocabulary policy for the Morning Brew blog.

THE PROBLEM (measured 2026-09-27, marmite 0.4.2)
  The digest unioned every bookmark's tags into each post's frontmatter. After
  61 posts that was 2,030 unique tags / 4,299 tag-post pairs, and 1,400 of them
  (69%) appeared on exactly ONE post. Marmite emits one HTML page AND one RSS
  feed per tag, so the blog exploded to 5,931 generated files / 1.3 GB -- and it
  regenerates ALL of it on every push. Local build: 409s. CI: killed at 7.5-9min
  ("The operation was canceled") -> the day's brew never publishes.

THE POLICY
  1. a tag must be used by >= MIN_GLOBAL posts corpus-wide to earn a page;
  2. a post carries at most MAX_TAGS tags, in the manifest's original order.
  Measured on the real corpus: unique tags 2,030 -> 258, generated files
  5,931 -> 870, site 1.3 GB -> 74 MB, build 409s -> 2.8s. Deploy went from
  FAILING at 7m34s to SUCCESS in 28s (run 36304855988, 2026-09-27).

WHY THIS SHAPE
  Filtering by corpus frequency makes the vocabulary SELF-LIMITING: a brand-new
  one-off tag earns no page, so the site cannot regrow the way it did. The
  per-post cap bounds the worst case. Post BODIES are never touched -- only the
  `tags:` line of the frontmatter. (A tag page for a single post is dead weight:
  69% of them pointed at exactly one post.)

USAGE
  python3 tag_vocabulary.py --audit                 # report only, no writes
  python3 tag_vocabulary.py --apply                 # cap every post
  python3 tag_vocabulary.py --apply --limit 21      # only newest 21 by date
  python3 tag_vocabulary.py --apply --content DIR   # other checkout

SAFETY
  * audit (no writes) unless --apply is passed
  * originals tarred to /tmp/kkrec/tagcap-backups-<ts>.tar.gz before writing
  * post bodies are never modified; `git -C <repo> diff --stat` proves it
"""
import argparse
import collections
import datetime
import json
import os
import re
import tarfile

MAX_TAGS = 14
MIN_GLOBAL = 2
DEFAULT_CONTENT = os.path.expanduser("~/Projects/morning-brew/content")


# ---------------------------------------------------------------- parsing ----
def parse_tags(text):
    """Return the tag list from a leading --- frontmatter block, or None."""
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return None
    tm = re.search(r"^tags:[ \t]*(.*)$", m.group(1), re.M)
    if tm is None:
        return None
    raw = tm.group(1).strip()
    if not raw:
        return []
    return [x.strip().strip("\"'") for x in raw.split(",") if x.strip()]


def corpus_freq(content_dir, exclude=None):
    """(Counter of tag -> number of posts using it, number of posts read).

    `exclude` skips one filename (used when generating a day's own frontmatter,
    so that day's tags don't inflate their own corpus count).
    """
    freq = collections.Counter()
    n = 0
    for f in sorted(os.listdir(content_dir)):
        if not f.endswith(".md") or f == exclude:
            continue
        try:
            text = open(os.path.join(content_dir, f), encoding="utf-8").read()
        except OSError:
            continue
        tags = parse_tags(text)
        if tags is None:
            continue
        freq.update(tags)
        n += 1
    return freq, n


def cap_tags(tags, freq, max_tags=MAX_TAGS, min_global=MIN_GLOBAL):
    """The policy. Corpus-frequency filter, then order-preserving truncation."""
    return [t for t in tags if freq[t] >= min_global][:max_tags]


# ------------------------------------------------------------------- main ----
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--content", default=DEFAULT_CONTENT)
    ap.add_argument("--apply", action="store_true", help="write changes")
    ap.add_argument("--audit", action="store_true", help="report only (default)")
    ap.add_argument("--limit", type=int, default=0,
                    help="only rewrite the newest N posts by date (0 = all)")
    ap.add_argument("--max-tags", type=int, default=MAX_TAGS)
    ap.add_argument("--min-global", type=int, default=MIN_GLOBAL)
    ap.add_argument(
        "--cap-list",
        metavar="TAG,TAG,...",
        help="cap a comma-separated tag list against the corpus vocabulary and print "
             "the survivors as a comma-separated line (for the cron's STEP 4 frontmatter). "
             "Use instead of pasting a raw union.",
    )
    a = ap.parse_args()

    content = os.path.abspath(os.path.expanduser(a.content))
    if not os.path.isdir(content):
        raise SystemExit(f"no such content dir: {content}")

    if a.cap_list is not None:
        freq, _ = corpus_freq(content)
        raw = [t.strip() for t in a.cap_list.split(",") if t.strip()]
        print(",".join(cap_tags(raw, freq, a.max_tags, a.min_global)))
        return

    files = sorted(f for f in os.listdir(content) if f.endswith(".md"))
    freq, n_posts = corpus_freq(content)

    per, texts = {}, {}
    for f in files:
        t = open(os.path.join(content, f), encoding="utf-8").read()
        tags = parse_tags(t)
        if tags is None:
            continue
        texts[f] = t
        per[f] = tags

    targets = set(files)
    if a.limit:
        targets = set(sorted(per, reverse=True)[: a.limit])  # filenames are dated

    plan, kept = {}, collections.Counter()
    for f, tags in per.items():
        if f in targets:
            new = cap_tags(tags, freq, a.max_tags, a.min_global)
        else:
            new = [t for t in tags if freq[t] >= a.min_global]
        kept.update(new)
        plan[f] = {"before": tags, "after": new}

    ts = datetime.datetime.now().strftime("%Y%m%dT%H%M%S")
    changed = [f for f in plan if plan[f]["before"] != plan[f]["after"]]
    report = {
        "content_dir": content,
        "posts_read": n_posts,
        "policy": {"min_global": a.min_global, "max_tags": a.max_tags,
                   "limit": a.limit or "all"},
        "unique_tags": {"before": len(freq), "after": len(kept)},
        "tag_pairs": {"before": sum(freq.values()), "after": sum(kept.values())},
        "files_to_change": len(changed),
    }
    print(json.dumps(report, indent=2))

    if not a.apply:
        print("\nAUDIT ONLY (no writes). Re-run with --apply to rewrite.")
        return

    # Backups -> /tmp so the repo stays clean (git history is the real undo).
    bdir = f"/tmp/kkrec/tagcap-backups-{ts}"
    os.makedirs(bdir, exist_ok=True)
    tarpath = f"{bdir}.tar.gz"
    with tarfile.open(tarpath, "w:gz") as tar:
        for f in changed:
            tar.add(os.path.join(content, f), arcname=f)

    written = 0
    for f in changed:
        path = os.path.join(content, f)
        t = texts[f]
        new = plan[f]["after"]
        if new:
            line = "tags: " + ", ".join(new)
            t2 = re.sub(r"^tags:[ \t]*.*$", line, t, count=1, flags=re.M)
        else:
            t2 = re.sub(r"^tags:[ \t]*.*\n?", "", t, count=1, flags=re.M)
        if t2 == t:
            continue
        # post body must survive byte-for-byte
        assert t2.split("\n---", 1)[-1] == t.split("\n---", 1)[-1], f"body drift {f}"
        open(path, "w", encoding="utf-8").write(t2)
        written += 1

    print(f"\nAPPLIED. files changed: {written}")
    print(f"unique tags : {len(freq)} -> {len(kept)}")
    print(f"tag pairs   : {sum(freq.values())} -> {sum(kept.values())}")
    print(f"backup      : {tarpath}")


if __name__ == "__main__":
    main()
