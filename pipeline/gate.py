#!/usr/bin/env python3
"""Gate for a Morning Brew edition. Ported from the Hermes skill's
`verify_deliverables.py`, retargeted at the pipeline item template.

Checks, in order:
  1  blog post exists and is not an empty shell
  2  vault note exists and is not an empty shell
  3  vault note body == blog post body (similarity above 0.995)
  4  blog frontmatter carries `slug: <date>-morning-brew`
  5  at least 3 numbered sections, strictly 1..N, no duplicates
  6  every Karakeep doc id in the body exists in the day's manifest
  7  tag budget: at most 14 tags on the post, at most 600 unique corpus tags
  8  every roundup item carries a `**Projects:**` block with at least 2 links
  9  every item carries `**Source:**` and `**Karakeep:**`
 10  live page answers 200 (skipped with --pre-push or --dry-run)
 11  warning only: the Hermes skill is longer than the configured line budget

Usage: uv run pipeline/gate.py <YYYY-MM-DD> [--pre-push] [--dry-run] [--json]
Exit: 0 pass (warnings allowed), 1 fail.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.config import expand, load_config  # noqa: E402
from lib.publish import body_similarity, strip_frontmatter  # noqa: E402

UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 "
    "(KHTML, like Gecko) Version/17.0 Safari/605.1.15"
)
MIN_BYTES = 2000
MIN_SECTIONS = 3
MAX_TAGS_PER_POST = 14
MAX_TAGS_CORPUS = 600


def sections(body: str) -> list[str]:
    return re.findall(r"^## \d+\. .+$", body, re.MULTILINE)


def doc_ids(body: str) -> list[str]:
    return re.findall(r"\*\*Karakeep:\*\* `([A-Za-z0-9]+)`", body)


def tag_line(text: str) -> list[str]:
    m = re.search(r"^tags:(.*)$", text, re.MULTILINE)
    if not m:
        return []
    return [t.strip() for t in m.group(1).split(",") if t.strip()]


def corpus_tags(content_dir: Path) -> set[str]:
    out: set[str] = set()
    for path in content_dir.glob("*.md"):
        try:
            out.update(tag_line(path.read_text()))
        except OSError:
            continue
    return out


def check_item_blocks(body: str) -> tuple[list[str], list[str]]:
    problems: list[str] = []
    warnings: list[str] = []
    blocks = re.split(r"(?m)^(?=## \d+\. )", body)[1:]
    for block in blocks:
        title = block.splitlines()[0]
        if "**Source:**" not in block:
            problems.append(f"{title!r}: no **Source:** line")
        if "**Karakeep:**" not in block:
            problems.append(f"{title!r}: no **Karakeep:** id")
        is_roundup = "**Projects:**" in block
        if is_roundup and len(re.findall(r"^- \[", block, re.MULTILINE)) < 2:
            problems.append(f"{title!r}: has a **Projects:** block with fewer than 2 links")
        if "**In short:**" not in block or "**Details:**" not in block:
            problems.append(f"{title!r}: missing **In short:** or **Details:**")
        if "**For my projects:**" not in block:
            problems.append(f"{title!r}: missing **For my projects:** line")
    return problems, warnings


def manifest_ids(day: str, vault_root: Path) -> set[str]:
    path = vault_root / "karakeep" / day / "manifest.json"
    if not path.exists():
        return set()
    try:
        data = json.loads(path.read_text())
    except json.JSONDecodeError:
        return set()
    return {b.get("id") for b in data.get("bookmarks", []) if b.get("id")}


def live_ok(url: str) -> tuple[bool, str]:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status == 200, f"HTTP {r.status}"
    except urllib.error.HTTPError as exc:
        return False, f"HTTP {exc.code}"
    except Exception as exc:
        return False, str(exc)[:120]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("day")
    ap.add_argument("--pre-push", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--post", default=None, help="blog post path (dry runs)")
    ap.add_argument("--note", default=None, help="vault note path (dry runs)")
    args = ap.parse_args(argv)
    cfg = load_config()
    vault = expand(cfg["paths"]["vault_root"])
    blog = expand(cfg["paths"]["blog_repo"])
    slug = f"{args.day}-morning-brew"
    vnote = Path(args.note) if args.note else vault / "karakeep" / args.day / f"{args.day}.md"
    bpost = Path(args.post) if args.post else blog / "content" / f"{slug}.md"
    url = f"{cfg['live']['base'].rstrip('/')}/{slug}.html"

    problems: list[str] = []
    warnings: list[str] = []

    for label, path in (("vault_note", vnote), ("blog_post", bpost)):
        if not path.exists():
            problems.append(f"{label} MISSING: {path}")
        elif path.stat().st_size < MIN_BYTES:
            problems.append(f"{label} is {path.stat().st_size}b, below {MIN_BYTES} (empty shell?)")

    vtext = vnote.read_text() if vnote.exists() else ""
    btext = bpost.read_text() if bpost.exists() else ""
    vbody, bbody = strip_frontmatter(vtext), strip_frontmatter(btext)

    if vtext and btext:
        sim = body_similarity(vbody.strip(), bbody.strip())
        if sim <= 0.995:
            problems.append(f"vault note and blog post have drifted (similarity {sim:.4f})")
    if btext and f"slug: {slug}" not in btext:
        problems.append(f"blog frontmatter missing 'slug: {slug}'")

    nums = [int(n) for n in re.findall(r"^## (\d+)\. ", vbody, re.MULTILINE)]
    if len(nums) < MIN_SECTIONS:
        problems.append(f"only {len(nums)} numbered sections (< {MIN_SECTIONS})")
    if nums != list(range(1, len(nums) + 1)):
        problems.append(f"section numbers are not 1..N in file order: {nums[:20]}")

    known = manifest_ids(args.day, vault)
    if known:
        bogus = sorted({i for i in doc_ids(vbody) if i not in known})
        if bogus:
            problems.append(f"Karakeep ids not in the day's manifest: {bogus}")

    tags = tag_line(btext)
    if len(tags) > MAX_TAGS_PER_POST:
        problems.append(f"{len(tags)} tags on the post, the budget is {MAX_TAGS_PER_POST}")
    vocab = corpus_tags(blog / "content")
    if len(vocab) > MAX_TAGS_CORPUS:
        problems.append(f"corpus vocabulary is {len(vocab)} tags, the budget is {MAX_TAGS_CORPUS}")

    item_problems, _ = check_item_blocks(vbody)
    problems.extend(item_problems)

    skill = expand(cfg["paths"]["skill_md"])
    budget = int(cfg["limits"]["skill_md_max_lines"])
    if skill.exists():
        n = sum(1 for _ in skill.open())
        if n > budget:
            warnings.append(f"the Hermes skill SKILL.md is {n} lines, over the {budget}-line budget")

    if not (args.pre_push or args.dry_run):
        ok, detail = live_ok(url)
        if not ok:
            problems.append(f"live page {url} is not answering: {detail}")
        else:
            warnings.append(f"live page answered 200 ({detail})")

    result = {
        "date": args.day,
        "ok": not problems,
        "problems": problems,
        "warnings": warnings,
        "url": url,
        "sections": len(nums),
        "tags": len(tags),
    }
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"gate {args.day}: {'PASS' if result['ok'] else 'FAIL'} "
              f"({result['sections']} sections, {result['tags']} tags)")
        for w in warnings:
            print(f"  warning: {w}")
        for p in problems:
            print(f"  FAIL: {p}")
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
