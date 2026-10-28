#!/usr/bin/env python3
"""karakeep_enrich.py — deterministic enrichment stage for the nightly digest.

Turns the RAW karakeep bookmarks for a day into an enriched index the fan-out
subagents consume, with ZERO per-item LLM work left for the cron agent.

WHY THIS EXISTS (the 09-28 / 09-29 / 09-30 cap-deaths):
  The cron agent used to do enrichment inline — one web_extract/curl per item
  for og:image/favicon, Cloudflare real_title, GitHub repo, project_url, and
  roundup links. On a 62-bookmark day that's ~150 tool calls of mechanical
  no-LLM work, which blew the tool-iteration cap before a single summary was
  written. Telling the agent "use the scripts" did NOT fix it: the scripts
  read the RAW bookmark shape (content.imageUrl etc.), while the processor's
  manifest FLATTENS `content` away — so extract_github_repos.py got handed a
  manifest-shaped file and returned `{}`, and the agent improvised 21 scratch
  scripts instead. A prompt instruction is advisory; this script is the code.

  This stage reads the RAW bookmarks (it has the API key) and computes every
  enrichment field mechanically. The cron agent then only does: fan-out
  (summarize) -> assemble -> gate -> publish.

Usage:
    python3 karakeep_enrich.py --date 2026-09-29
    python3 karakeep_enrich.py             # defaults to yesterday

Writes <vault>/karakeep/<date>/enriched.json and prints a summary.

Stdlib only (json/re/urllib) + subprocess for yt-dlp/curl. Deterministic.
"""
import argparse
import datetime
import json
import os
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kk as kd  # data layer: all_bookmarks, bookmarks_for_day, yt_id

VAULT = Path.home() / "wojtek.second.brain.obsidian.vault" / "karakeep"
SKILL_SCRIPTS = Path(__file__).resolve().parent.parent / "references"

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
GH_UA = "hermes"

# domains / classification
YOUTUBE_HOSTS = ("youtube.com", "youtu.be")


def _curl(url, tries=2):
    """curl a URL, return decoded text or ''. Retry transient failures."""
    last = ""
    for attempt in range(tries):
        r = subprocess.run(
            ["curl", "-sL", "--max-time", "40", "-A", UA, url],
            capture_output=True, text=True,
        )
        if r.returncode == 0 and r.stdout:
            return r.stdout
        last = r.stdout or r.stderr or ""
        time.sleep(1.0 * (attempt + 1))
    return last


def _ytdlp_print(url, template, tries=2):
    """yt-dlp --print, fallback when curl can't resolve a YouTube channel."""
    for attempt in range(tries):
        r = subprocess.run(
            ["yt-dlp", "--skip-download", "--no-warnings",
             "--extractor-args", "youtube:player_client=web_embedded,android",
             "--print", template, url],
            capture_output=True, text=True, timeout=90,
        )
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout.strip().splitlines()[-1]
        time.sleep(2 * (attempt + 1))
    return ""


def favicon(url):
    d = urllib.parse.urlparse(url).netloc
    return f"https://{d}/favicon.ico" if d else None


def gh_meta(owner, repo):
    """GitHub REST metadata for owner/repo. Returns dict or None."""
    url = f"https://api.github.com/repos/{owner}/{repo}"
    req = urllib.request.Request(url, headers={"User-Agent": GH_UA,
        "Accept": "application/vnd.github+json"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            d = json.load(r)
    except Exception:
        return None
    return {
        "full_name": d.get("full_name"),
        "description": d.get("description"),
        "stars": d.get("stargazers_count"),
        "language": d.get("language"),
        "license": (d.get("license") or {}).get("spdx_id"),
        "html_url": d.get("html_url"),
        "topics": d.get("topics", [])[:8],
        "archived": d.get("archived"),
        "pushed_at": d.get("pushed_at"),
    }


# ---------------------------------------------------------------- per-kind enrich

def _yt_id(url):
    """video id from any YouTube URL shape: /shorts/, /watch?v=, /live/, youtu.be."""
    u = url or ""
    m = (re.search(r"youtube\.com/shorts/([\w-]{11})", u)
         or re.search(r"youtube\.com/live/([\w-]{11})", u)
         or re.search(r"[?&]v=([\w-]{11})", u)
         or re.search(r"youtu\.be/([\w-]{11})", u))
    return m.group(1) if m else None


def enrich_video(entry, b, url):
    """video_id, thumbnail, channel for a YouTube bookmark."""
    c = b.get("content") or {}
    vid = _yt_id(url)
    if vid:
        entry["video_id"] = vid
        entry["thumbnail"] = f"https://i.ytimg.com/vi/{vid}/maxresdefault.jpg"
        # channel: curl+grep ownerChannelName, fallback yt-dlp
        html = _curl(f"https://www.youtube.com/watch?v={vid}")
        m = re.search(r'"ownerChannelName":"([^"]*)"', html)
        if m:
            entry["channel"] = m.group(1)
        else:
            chan = _ytdlp_print(url, "%(channel)s")
            if chan:
                entry["channel"] = chan
    return entry


def enrich_article(entry, b, url):
    """og_image / favicon, Cloudflare real_title, repo/project_url, roundup."""
    c = b.get("content") or {}
    # image: content.imageUrl if real, else og:image, else favicon
    img = c.get("imageUrl") or ""
    if not img or "logo" in img.lower() or "opengraph.githubassets" in img:
        html = _curl(url)
        m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)', html) \
            or re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image', html)
        if m:
            img = m.group(1)
        elif not img:
            img = favicon(url)
    entry["imageUrl"] = img or favicon(url)

    # Cloudflare interstitial -> real_title (9to5linux)
    title = c.get("title") or ""
    if "Attention Required" in title or "Cloudflare" in title:
        html = _curl(url)
        m = re.search(r"<title>([^<]+)</title>", html)
        if m:
            entry["real_title"] = m.group(1).strip()

    return entry


def enrich_osp(entry, b, url):
    """opensourceprojects.dev: repo from content.imageUrl, + gh_meta."""
    c = b.get("content") or {}
    img = c.get("imageUrl") or ""
    m = re.search(r"opengraph\.githubassets\.com/1/([^/]+)/([^/]+)", img)
    if m:
        owner, repo = m.group(1), m.group(2)
        entry["repo"] = f"{owner}/{repo}"
        entry["project_url"] = f"https://github.com/{owner}/{repo}"
        meta = gh_meta(owner, repo)
        if meta:
            entry["gh_meta"] = meta
    return entry


def enrich_linuxlinks(entry, b, url):
    """linuxlinks single post: project_url from the internal page's 'Home Page'
    / 'Website' table row (raw HTML form), falling back to the first outbound
    non-linuxlinks non-XFN link."""
    html = _curl(url)
    # raw HTML table form: <strong>Home Page:</strong></td>...<a href="...">
    m = (re.search(r'<strong>Home Page:</strong></td>\s*<td[^>]*>\s*<strong>'
                   r'<a href="(https?://[^"]+)"', html)
         or re.search(r'<strong>Website:</strong></td>\s*<td[^>]*>\s*<strong>'
                      r'<a href="(https?://[^"]+)"', html))
    if m:
        entry["project_url"] = m.group(1).rstrip("/")
        return entry
    # fallback: first outbound link that is neither linuxlinks nor XFN noise
    for l in re.findall(r'href="(https?://[^"]+)"', html):
        if ("linuxlinks.com" in l or "wp-content" in l or "wordpress" in l
                or "gmpg.org" in l or "gravatar.com" in l):
            continue
        entry["project_url"] = l.rstrip("/")
        break
    return entry


def enrich_roundup(entry, b, url, roundup_input):
    """Attach resolved roundup project links (deferred to the resolver)."""
    # roundup_input is a dict built by the caller; if this bookmark's id is a
    # roundup key, we attach its resolved list.
    pass  # resolved in a second pass, see main()


def clean_title(rt):
    rt = re.sub(r"&amp;", "&", rt)
    rt = re.sub(r"&#0?39;", "'", rt)
    rt = re.sub(r"&#x27;", "'", rt)
    rt = re.sub(r"\s*\|\s*Open[- ]?source\s+Proj\w*$", "", rt).strip()
    return rt


def publisher_label(b):
    c = b.get("content") or {}
    p = c.get("publisher") or c.get("author") or "?"
    if p == "Cloudflare":
        return "9to5Linux"
    return p


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=None, help="YYYY-MM-DD (default: yesterday)")
    args = ap.parse_args()
    target = args.date or (datetime.date.today() - datetime.timedelta(days=1)).isoformat()

    bms = kd.bookmarks_for_day(target)
    if not bms:
        print(f"no bookmarks for {target}")
        return 1

    daydir = VAULT / target
    daydir.mkdir(parents=True, exist_ok=True)

    entries = []

    for b in bms:
        c = b.get("content") or {}
        url = c.get("url") or ""
        bid = b["id"]
        title = c.get("title") or b.get("title") or "(untitled)"
        entry = {
            "id": bid,
            "title": title,
            "url": url,
            "source": b.get("source"),
            "publisher": publisher_label(b),
            "tags": [t.get("name") if isinstance(t, dict) else str(t) for t in b.get("tags", [])],
            "created": b.get("createdAt"),
        }
        is_vid = any(h in url for h in YOUTUBE_HOSTS) or "instagram.com" in url

        if is_vid:
            entry = enrich_video(entry, b, url)
        elif "opensourceprojects.dev" in url:
            entry = enrich_article(entry, b, url)
            entry = enrich_osp(entry, b, url)
        elif "linuxlinks.com" in url:
            entry = enrich_article(entry, b, url)
            entry = enrich_linuxlinks(entry, b, url)
        else:
            entry = enrich_article(entry, b, url)

        # clean real_title if present
        if entry.get("real_title"):
            entry["real_title"] = clean_title(entry["real_title"])
            # The source <title> usually ends in the site's own name
            # ("… Updated Raspberry Pi Images - 9to5Linux"). The heading already
            # ends in "— by <Publisher>", so keeping it yields a doubled suffix:
            # "… - 9to5Linux — by 9to5Linux" (seen live 2026-10-03). Strip it.
            root = urllib.parse.urlparse(url).netloc.lower()
            root = root[4:] if root.startswith("www.") else root
            root = root.split(".")[0]
            if root:
                entry["real_title"] = re.sub(
                    r"\s*[-\u2013\u2014|]\s*" + re.escape(root) + r"\s*$", "",
                    entry["real_title"], flags=re.I).strip()

        # Guarantee the transcript PATH is on every video entry. The manifest only
        # carries it when the processor recorded it; when it is absent the fan-out
        # children have to hunt for transcriptions/<id>.md themselves (observed
        # 2026-10-03). Absent-but-existing is a deterministic fact, so set it here.
        tpath = daydir / "transcriptions" / f"{bid}.md"
        if tpath.exists():
            entry.setdefault("transcript", str(tpath))

        entries.append(entry)
        time.sleep(0.15)  # gentle pacing

    enriched = {"date": target, "bookmarks": entries}

    out_path = daydir / "enriched.json"
    out_path.write_text(json.dumps(enriched, indent=2, ensure_ascii=False))

    n_vid = sum(1 for e in entries if e.get("video_id"))
    n_repo = sum(1 for e in entries if e.get("repo"))
    n_proj = sum(1 for e in entries if e.get("project_url"))
    n_real = sum(1 for e in entries if e.get("real_title"))
    n_img = sum(1 for e in entries if e.get("imageUrl"))
    print(f"[{target}] enriched {len(entries)} bookmarks -> {out_path}")
    print(f"  videos={n_vid} repos={n_repo} project_urls={n_proj} "
          f"real_titles={n_real} imageUrls={n_img}")
    print(f"  NOTE: roundup resolution is NOT done here — that is STEP 3.6 "
          f"(roundup_project_links.py) in the cron, after the fan-out.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
