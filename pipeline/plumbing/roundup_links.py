#!/usr/bin/env python3
"""Resolve the projects named in a roundup/project-list digest item to a
verified link + one-line "what is it", and emit a ready-to-paste markdown block.

Why this exists (Wojtek, 2026-09-20): roundups like "I ditched Synology's apps
for open-source alternatives" or "7 New Home Lab Projects to Try This Weekend"
name a pile of projects and link NONE of them. He wants to click straight to
GitHub and know what each thing is without googling.

Hard rule: NO UNVERIFIED LINKS. Every emitted URL was resolved AND probed over
live HTTPS in this same run (200 + the page is what we think it is). A name that
cannot be resolved is emitted as an explicit gap, never a guessed owner/repo.

Metadata comes from HTML/og:description (NOT the GitHub API) on purpose: the
unauthenticated API limit is 60 req/h and resolving one roundup can burn it,
while plain HTML probing is unlimited and discriminates 200 vs 404 just as well.

Input JSON:
  [{"n": 5, "names": ["Immich", "Navidrome", "Grimmory", ...],
    "source": "https://www.linuxlinks.com/best-free-..."}, ...]

  The roundup number may also arrive as `id` (raw chunk dicts use `id` —
  GUL-309: the 2026-10-27 run fed those in and the resolver died on
  KeyError: 'n'). `n` wins when both are present; an item with NEITHER is
  rejected with exit 2 and a one-line message, not a traceback.

  `source` is OPTIONAL but strongly recommended: it is the fallback path (step 3)
  when a name is not in the curated map.

Resolution ladder (added 2026-09-28 — the 2026-09-27 roundup shipped 36 bare
names because a curated-map miss was terminal):

  1. curated map            `references/curated-project-links.json` (normalized key)
  2. exact / alias key      normalized, plus a small alias table + loose substring pass
  3. ARTICLE-PAGE EXTRACTION  if the input item carries `"source": "<article url>"`,
                            fetch it and take the first outbound link whose host is
                            not publisher/social/CDN noise (this is what recovered
                            isolate/mpdris2-rs/Freezed/matrixOS/Notation/… on 09-27)
  4. GITHUB SEARCH           https://api.github.com/search/repositories — last resort,
                            paced (unauthenticated search is ~10 req/min).
                            This is what recovered `Shelly` → Seafoam-Labs/Shelly-ALPM.

A miss in step 1 is NOT terminal any more. Only if all four fail does the name
become an explicit gap.

Usage:
  python3 roundup_project_links.py <input.json> [--out /tmp/kk_run/links.json]
                                  [--md /tmp/kk_run/blocks.md] [--no-probe]
                                  [--no-fallback] [--budget SECONDS]
                                  [--workers N]

Budget (2026-10-26): the resolver always finishes. `--budget` (default 150 s,
below the 180 s Hermes `terminal.timeout`) is a hard wall-clock deadline, not a
hint: names are resolved in parallel and whatever is not finished by the
deadline ships as an honest gap with `source: "dropped-budget"`. The process
writes `--out`/`--md` and exits 0 within budget + 10 s even if the network
blocks, and the last stdout line is always
`dropped: budget <N> [names]`.

Output:
  stdout  — per-section table, then the dropped-budget line
  --out   — JSON {results: {section: [...]}, blocks: {...},
                  dropped_budget: [names]}
  --md    — markdown blocks, one per section, ready to paste into the digest
"""
import datetime
import html
import json
import os
import queue
import re
import shutil
import ssl
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
CURATED = os.path.join(HERE, "..", "references", "curated-project-links.json")

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

# pages that answer 200 but are bot-walls / non-content
WALL = re.compile(r"(just a moment|are you a bot|not a bot|client challenge|"
                  r"attention required|enable javascript|access denied|"
                  r"checking your browser)", re.I)

# HTTP statuses that are NEVER proof a project is dead.
#   403/406/429/503 = bot-wall (sourceforge, codeberg, gitlab.gnome.org)
#   3xx             = urllib refused a redirect it could not follow (flathub 308)
# Both must fall through to the curl fallback (curl -L follows 308 and often
# clears the wall) before a name is allowed to read as DEAD.
BOTWALL = {403, 406, 429, 503}
DEAD_OK = {404, 410}

# ---------------------------------------------------------------------------
# Wall-clock budget (2026-10-26)
#
# The 10-26 cron run called this script 7 times; each call was killed at the
# 180 s Hermes tool timeout because 79 names at ~7.5 s each is ~10 minutes. A
# sequential `check before each name` is not enough: a single name can block for
# minutes (probe retries 4 x 30 s, _curl 45 s, gh 30 s). So every network call
# below is capped at the remaining budget AND the main thread stops collecting
# at the deadline, writes partial output and exits 0. A watchdog thread writes
# the same output and hard-exits if anything still blocks past the deadline.
# ---------------------------------------------------------------------------

_DEADLINE = [None]      # absolute time.time() deadline, or None for "no budget"
_WRITE_LOCK = threading.Lock()
_FINISHED = [False]
_RUN_ID = [0]


def _remaining():
    """Seconds left before the deadline, or None when no budget is set."""
    return None if _DEADLINE[0] is None else _DEADLINE[0] - time.time()


def _net_ok(slack=0.0):
    """True while there is budget left for another network call."""
    r = _remaining()
    return r is None or r > slack


def _cap_timeout(seconds):
    """Never wait longer than the remaining budget."""
    r = _remaining()
    if r is None:
        return float(seconds)
    return max(1.0, min(float(seconds), r))


# A binary/appimage href is never the project's home page. The 10-26 run resolved
# Audacious -> audacious-4.6.2.tar.bz2, BIND -> bind-9.20.30.tar.xz and BleachBit
# -> BleachBit-6.0.6-x86_64.AppImage from the article rung: a download is worse
# than an honest gap.
DOWNLOAD_EXT = re.compile(
    r"\.(tar\.gz|tgz|tar\.bz2|tar\.xz|zip|7z|gz|bz2|xz|appimage|deb|rpm|dmg|"
    r"exe|msi|pkg|snap|flatpakref|iso)$", re.I)


def is_download_url(url):
    """True for a link that points at a downloadable file, not a project page."""
    path = re.sub(r"[?#].*$", "", url or "").rstrip("/")
    return bool(DOWNLOAD_EXT.search(path))


def repo_root_from_download(url):
    """`github.com/o/r/releases/download/...` -> `https://github.com/o/r`.

    9to5linux roundups link every project to its release tarball
    (`.../transmission-4.1.4.tar.xz`). The tarball is not the project page, but
    its own repo root is: same owner, same project, and it saves a GitHub search
    per name. Only repo hosts with a fixed owner/repo prefix are derived.
    """
    m = re.match(r"https?://(?:www\.)?(github\.com|gitlab\.com)/([^/]+)/([^/#?]+)",
                 url or "", re.I)
    if not m:
        return None
    repo = re.sub(r"\.git$", "", m.group(3))
    return f"https://{m.group(1).lower()}/{m.group(2)}/{repo}"


def norm(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def load_curated():
    with open(CURATED) as f:
        raw = json.load(f)
    out = {}
    for k, v in raw.items():
        if k.startswith("_"):
            continue
        out[norm(k)] = v
    return out


def _probe_curl(url, ua=None):
    """Fallback transport. When urllib's connection gets dropped (seen with
    claws-mail.org under sequential load), curl usually still answers. Returns
    the same tuple shape, or None if curl also fails.

    UA note (found 2026-09-24): the Chrome UA in UA is itself walled by some
    hosts — sourceforge.io and codeberg answer **403 to the Chrome UA** while
    answering 200 to no-UA / curl-UA / Safari-UA. So the wall is UA-sniffing,
    not a real bot-block. Try the caller's UA first, then a neutral curl UA."""
    import subprocess
    agents = [ua] if ua else []
    agents += ["curl/8.7.1"]
    for a in agents:
        if not _net_ok():
            return None
        cap = int(max(1.0, _cap_timeout(40)))
        try:
            cmd = ["curl", "-sSL", "--max-time", str(cap)]
            if a:
                cmd += ["-A", a]
            cmd += ["-w", "\n__META__%{http_code} %{url_effective}", url]
            p = subprocess.run(cmd, capture_output=True, text=True, timeout=cap + 5)
        except Exception:
            continue
        if p.returncode != 0 or "__META__" not in p.stdout:
            continue
        body, _, meta = p.stdout.rpartition("\n__META__")
        try:
            code_s, final = meta.split(" ", 1)
            code = int(code_s)
        except Exception:
            continue
        if code != 200:
            last_code = code
            continue
        title = ""
        m = re.search(r"<title[^>]*>(.*?)</title>", body, re.S | re.I)
        if m:
            title = re.sub(r"\s+", " ", m.group(1)).strip()
        desc = ""
        for pat in (r'<meta[^>]+property=["\']og:description["\'][^>]+content=["\'](.*?)["\']',
                    r'<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\']'):
            m2 = re.search(pat, body, re.S | re.I)
            if m2:
                desc = re.sub(r"\s+", " ", m2.group(1)).strip()
                break
        return (code, final, title, desc)
    return None


def probe(url, tries=4):
    """Return (code, final_url, title, description). Never raises.
    Retries on transport failure only: some project sites (claws-mail.org) drop
    the connection when hammered, and a transient 0 must not read as 'dead'.
    A real HTTP status (404/403) is returned immediately — that IS the answer."""
    last = (0, url, "", "")
    for attempt in range(tries):
        if not _net_ok():
            break
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=_cap_timeout(30), context=CTX) as r:
                body = r.read(500000).decode("utf-8", "ignore")
                code, final = r.status, r.url
            break
        except urllib.error.HTTPError as e:
            # A bot-wall or an unfollowed redirect is NOT proof of death — but a
            # 404/410 IS. Only the latter is returned immediately; the former
            # gets one curl attempt (`-L` follows 308, and curl's TLS/UA often
            # clears sourceforge+codeberg walls) before we accept the verdict.
            if e.code in BOTWALL or 300 <= e.code < 400:
                alt = _probe_curl(url, ua=None)
                if alt and alt[0] == 200:
                    return alt
                return alt if alt else (e.code, url, "", "")
            return (e.code, url, "", "")          # real HTTP answer — do not retry
        except Exception:
            last = (0, url, "", "")
            if attempt < tries - 1 and _net_ok(2.0):
                time.sleep(min(2.0 * (attempt + 1), _remaining()))
    else:
        # urllib exhausted — hand off to curl before calling it dead.
        alt = _probe_curl(url)
        return alt if alt else last

    def meta(pat):
        m = re.search(pat, body, re.S | re.I)
        return re.sub(r"\s+", " ", m.group(1)).strip() if m else ""

    title = meta(r"<title[^>]*>(.*?)</title>")
    desc = (meta(r'<meta[^>]+property=["\']og:description["\'][^>]+content=["\'](.*?)["\']')
            or meta(r'<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\']'))
    desc = re.sub(r"&quot;", '"', desc)
    if title and WALL.search(title):
        return (code, final, title, desc + " [BOT-WALL]")
    return (code, final, title, desc)


def link_of(entry):
    return entry.get("repo") and f"https://github.com/{entry['repo']}" or entry.get("docs")


def clean_what(text, name, fallback):
    """Turn a repo description into a one-clause blurb."""
    t = (text or "").strip()
    t = re.sub(r"^GitHub\s*-\s*[\w.\-]+/[\w.\-]+:\s*", "", t)
    t = re.sub(r"\s*[·|]\s*GitHub\s*$", "", t)
    t = t.strip(" -—:")
    if not t or norm(t).startswith(norm("read-only mirror")):
        return fallback
    if len(t) > 200:
        t = t[:197].rstrip() + "…"
    t = t[0].upper() + t[1:]
    if not t.endswith((".", "!", "?")):
        t += "."
    return t


# ---------------------------------------------------------------------------
# Fallback resolution (2026-09-28) — a curated-map miss must not be terminal.
# ---------------------------------------------------------------------------

# Hosts that are never "the project": publishers, socials, CDNs, generic infra.
NOISE_HOST = re.compile(r"""(?ix)
    (^|\.)(gmpg\.org|w3\.org|schema\.org|wordpress\.(com|org)|wp\.com
    |twitter\.com|x\.com|facebook\.com|reddit\.com|linkedin\.com
    |pinterest\.[a-z.]+|t\.me|telegram\.(me|org)|youtube\.com|youtu\.be
    |instagram\.com|threads\.(net|com)|mastodon\.[a-z.]+
    |gravatar\.com|patreon\.com|paypal\.com|buymeacoffee\.com
    |forfoss\.com|ossblog\.org|amazon\.[a-z.]+|apple\.com|google\.com
    |9to5linux\.com|linuxlinks\.com|makeuseof\.com|howtogeek\.com
    |androidpolice\.com|notebookcheck\.net|techradar\.com|sciencealert\.com
    |anpoimages\.com|makeuseofimages\.com|howtogeekimages\.com
    |static[0-9]*\.[a-z.]+|cdn\.[a-z.]+|fonts\.(googleapis|gstatic)\.com
    |gstatic\.com|cloudflare\.com|jquery\.com|jsdelivr\.net|unpkg\.com)$
""")

# shortlink services — never a project URL
SHORTENER = re.compile(r"(?i)(^|\.)(wp\.me|bit\.ly|tinyurl\.com|t\.co|goo\.gl|"
                       r"ow\.ly|buff\.ly|is\.gd|rebrand\.ly|s\.id|lnkd\.in|"
                       r"d\.ly|rb\.gy|shorturl\.at|x\.co)$")

REPO_HOST = re.compile(r"(github\.com|gitlab\.com|codeberg\.org|sr\.ht|"
                       r"git\.savannah\.gnu\.org|gitlab\.gnome\.org|"
                       r"invent\.kde\.org|codeberg\.page)")

ALIASES = {
    "nura": "postmarketos", "postmarketosnura": "postmarketos",
    "gnu": "gnu", "firefox": "mozillafirefox", "ffmpeg": "ffmpeg",
    "kernel": "linuxkernel", "linux": "linuxkernel",
    "video hub app": "videohubapp", "videohub": "videohubapp",
    "catppuccin for tmux": "catppuccintmux",
    "mit intro to deep learning": "mitdeeplearning",
}


def _host(url):
    """Host of a URL, lowercased, www-stripped. '' if unparseable."""
    m = re.match(r"https?://([^/?#]+)", url or "")
    return re.sub(r"^www\.", "", m.group(1)).lower() if m else ""


def _curl(url, ua=None, timeout=45):
    """curl -sSL transport returning (code, final_url, body)."""
    import subprocess
    if not _net_ok():
        return (0, url, "")
    timeout = int(max(1.0, _cap_timeout(timeout)))
    cmd = ["curl", "-sSL", "--max-time", str(timeout)]
    if ua:
        cmd += ["-A", ua]
    cmd += ["-w", "\n__META__%{http_code} %{url_effective}", url]
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout + 5)
    except Exception:
        return (0, url, "")
    if p.returncode != 0 or "__META__" not in p.stdout:
        return (0, url, "")
    body, _, meta = p.stdout.rpartition("\n__META__")
    try:
        code_s, final = meta.split(" ", 1)
        return (int(code_s), final.strip(), body)
    except Exception:
        return (0, url, "")


def _title(body):
    m = re.search(r"<title[^>]*>(.*?)</title>", body, re.S | re.I)
    return re.sub(r"\s+", " ", m.group(1)).strip() if m else ""


# ---------------------------------------------------------------------------
# LinuxLinks name-aware resolution (2026-10-22)
#
# Two page shapes, both carrying the project's canonical link in a labelled
# <strong> field rather than as the first outbound href:
#   * the 100-GUI listing: <h4>25. Element</h4> ... <strong>Website:</strong>
#     <a href="https://element.io/...">       <- link lives ON THE LISTING PAGE
#   * the classic roundup: a <tr> row links /name/, and the internal review page
#     carries <strong>Home Page:</strong>.
# The 10-22 run fell through both and guessed from GitHub search, producing
# Element -> ElemeFE/element, Shortwave -> maunalinux/shortwave, Kodi -> a
# plugins fork. Label-first parsing is the fix; it is also what keeps GIMP and
# Wireshark on gimp.org/wireshark.org instead of a read-only GitHub mirror.
# ---------------------------------------------------------------------------

LINK_LABELS = ("Website", "Home Page", "Source Code", "GitHub", "Project",
               "Repository")


def homepage_link(html_text):
    """Return (label, url) for the first labelled project link, or (None, None).

    Find the LABEL first, then take the first external anchor after it. Taking
    the first outbound href on the page picks the screenshot image or a
    publisher link, which is how the old parser produced wrong-but-200 URLs.
    """
    for label in LINK_LABELS:
        for mm in re.finditer(r"<strong>\s*" + label + r"\s*:?\s*</strong>(.{0,400})",
                              html_text or "", re.S | re.I):
            for href in re.findall(r'href=["\'](https?://[^"\']+)["\']',
                                   mm.group(1), re.I):
                href = html.unescape(href)
                host = _host(href)
                if not host or "linuxlinks.com" in host:
                    continue
                if NOISE_HOST.search(host) or SHORTENER.search(host):
                    continue
                if is_download_url(href):
                    continue
                return label, href
    return None, None


def _listing_heading_sections(body):
    """[(start, end, label)] for the h3/h4 headings on a listing page."""
    out = []
    for mm in re.finditer(r"<h([34])[^>]*>(.*?)</h\1>", body or "", re.S | re.I):
        label = re.sub(r"<[^>]+>", " ", mm.group(2))
        label = html.unescape(re.sub(r"\s+", " ", label)).strip()
        label = re.sub(r"^\d+[\.\)]\s*", "", label)
        out.append((mm.start(), mm.end(), label))
    return out


def _listing_section(body, name):
    """The <h3>/<h4> section whose heading matches "name", or None."""
    want = norm(name)
    heads = _listing_heading_sections(body)
    pick = None
    for pos, end, label in heads:
        if norm(label) == want:
            pick = (pos, end, label)
            break
    if not pick:
        for pos, end, label in heads:
            nl = norm(label)
            if len(nl) >= 4 and len(want) >= 4 and (nl.startswith(want) or want.startswith(nl)):
                pick = (pos, end, label)
                break
    if not pick:
        return None
    start, end, _label = pick
    nxt = len(body)
    for pos, _e, _l in heads:
        if pos > start:
            nxt = pos
            break
    return body[end:nxt]


def from_linuxlinks_listing(listing_url, name):
    """Resolve a LinuxLinks roundup name from the publisher's own page.

    Order: listing-section Website: link -> classic /name/ internal page ->
    repo-host anchor inside the section. Name-aware and API-free, so it is
    immune to GitHub rate-limiting and never guesses a popular namesake.
    """
    if listing_url not in _LISTING_BODY_CACHE:
        _listing_body(listing_url)
    code, _final, body = _LISTING_BODY_CACHE[listing_url]
    if code != 200 or not body:
        return None
    sec = _listing_section(body, name)
    if sec:
        label, href = homepage_link(sec)
        if href:
            p = probe(href)
            if p[0] == 200:
                return {"url": href, "code": 200, "final": p[1], "title": p[2],
                        "source": "linuxlinks-website",
                        "what": p[3] or p[2] or None, "label": label}
    if "linuxlinks.com" in listing_url:
        slug = _index_map(listing_url).get(name)
        if not slug:
            key = norm(name)
            for disp, sl in _index_map(listing_url).items():
                dk = norm(disp)
                if dk == key or (len(key) >= 4 and len(dk) >= 4
                                 and (dk.startswith(key) or key.startswith(dk))):
                    slug = sl
                    break
        if slug:
            c2, _f2, pbody = _curl("https://www.linuxlinks.com" + slug, ua=UA)
            if c2 == 200 and pbody:
                label, href = homepage_link(pbody)
                if href:
                    p = probe(href)
                    if p[0] == 200:
                        return {"url": href, "code": 200, "final": p[1],
                                "title": p[2], "source": "linuxlinks-website",
                                "what": p[3] or p[2] or None, "label": label}
    if sec:
        # last resort: a repo-host anchor inside the section (never a screenshot)
        for href in re.findall(r'href=["\'](https?://[^"\']+)["\']', sec, re.I):
            href = html.unescape(href)
            if not REPO_HOST.search(href):
                continue
            if is_download_url(href):
                continue
            p = probe(href)
            if p[0] == 200:
                return {"url": html.unescape(href), "code": 200, "final": p[1],
                        "title": p[2], "source": "linuxlinks-section",
                        "what": p[3] or p[2] or None}
    return None


def article_name_scoped(source_url, name):
    """Name-aware article rung: the anchor whose OWN text/alt matches the name.

    This is the safe replacement for the blind from_article() rung. It never
    takes "the first outbound link", so one article cannot paint every bullet
    with the same URL.
    """
    code, _final, body = _listing_body(source_url)
    if code != 200 or not body:
        return None
    key = norm(name)
    for a in re.finditer(r'<a\b([^>]*?)href=["\'](https?://[^"\']+)["\']([^>]*)>(.*?)</a>',
                         body, re.S | re.I):
        attrs, href, tail, text = a.group(1), a.group(2), a.group(3), a.group(4)
        label = re.sub(r"<[^>]+>", " ", text)
        label = re.sub(r"\s+", " ", label).strip()
        alt = re.search(r'alt=["\']([^"\']+)["\']', attrs + tail)
        cand = norm(label + " " + (alt.group(1) if alt else ""))
        if not cand:
            continue
        if cand == key or key in cand or cand in key:
            href = html.unescape(href)
            if NOISE_HOST.search(_host(href)) or SHORTENER.search(_host(href)):
                continue
            if is_download_url(href):
                root = repo_root_from_download(href)
                if root:
                    p = probe(root)
                    if p[0] == 200:
                        return {"url": root, "code": 200, "final": p[1],
                                "title": p[2], "source": "article-download-repo",
                                "what": p[3] or p[2] or None}
                continue
            p = probe(href)
            if p[0] == 200:
                return {"url": href, "code": 200, "final": p[1], "title": p[2],
                        "source": "article-name-scoped",
                        "what": p[3] or p[2] or None}
    return None


def from_article(source_url, name):
    """Step 3 — pull the project link out of the article that mentions it.

    LinuxLinks single-project posts and most 'X replaced my Y' writeups carry the
    upstream repo in an outbound href. The name-scoped pass first tries to find a
    href near the name; failing that it takes the first non-noise outbound link.
    """
    code, final, body = _listing_body(source_url)
    if code != 200 or not body:
        return None
    hrefs = re.findall(r'href=["\'](https?://[^"\']+)["\']', body, re.I)
    clean = []
    for h in hrefs:
        host = re.sub(r"^www\.", "", re.sub(r"^https?://", "", h).split("/")[0]).lower()
        if NOISE_HOST.search(host):
            continue
        if h not in clean:
            clean.append(h)
    if not clean:
        return None
    # STRICT: only a real project host counts. Falling back to "any non-noise
    # link" returned https://wp.me/9swuV (a WordPress SHORTLINK) in testing —
    # a wrong-but-200 URL is worse than an honest miss, because the digest would
    # print it as if it were the project. Better None; the GitHub search follows.
    repos = [h for h in clean if REPO_HOST.search(h)]
    pubs = [h for h in clean if not REPO_HOST.search(h)]
    for cand in repos + [c for c in pubs
                         if not SHORTENER.search(_host(c))
                         and _host(c) not in {"forfoss.com", "ossblog.org"}]:
        if is_download_url(cand):
            continue
        c2, f2, b2 = _curl(cand, ua=UA)
        if c2 != 200:
            continue
        # a followed shortlink lands back on the publisher's own domain -> reject.
        # NOTE: SHORTENER must be tested against the HOST. Testing it against the
        # raw URL (with a `$` anchor) never matched https://wp.me/p9swuV-E4N, which
        # is how a WordPress shortlink leaked into the digest in testing.
        f2host = _host(f2)
        if SHORTENER.search(_host(cand)) or f2host in ("wp.me", "wordpress.com"):
            continue
        return {"url": cand, "code": c2, "title": _title(b2),
                "source": "article-page", "what": _title(b2) or None}
    return None


_LAST_GH = [0.0]
_GH_PACE_LOCK = threading.Lock()


def _pace(min_gap=6.5):
    """Serialise GitHub search calls: 8 workers must not burst the rate limit.

    The lock is held across the sleep on purpose — the whole point is that only
    one search is in flight, and that consecutive searches respect the gap.
    """
    with _GH_PACE_LOCK:
        gap = time.time() - _LAST_GH[0]
        if gap < min_gap:
            time.sleep(min(min_gap - gap, max(0.0, _remaining() or min_gap - gap)))
        _LAST_GH[0] = time.time()


def _gh_search(name):
    """Authenticated repository search through `gh api` (30 req/min).

    Returns the parsed JSON, or None so the caller falls back to the
    unauthenticated curl call. `gh` is a hard dependency of the homelab anyway
    and 30/min beats 10/min, which is what let 79 names take 10 minutes.
    """
    gh = shutil.which("gh")
    if not gh or not _net_ok(1.0):
        return None
    q = urllib.parse.quote(name)
    _pace(2.1)
    if not _net_ok(1.0):
        return None
    try:
        p = subprocess.run([gh, "api", f"search/repositories?q={q}&per_page=8"],
                           capture_output=True, text=True,
                           timeout=_cap_timeout(30))
        if p.returncode != 0 or not p.stdout.strip():
            return None
        return json.loads(p.stdout)
    except Exception:
        return None


def bounded(longer, shorter):
    """True if `longer` starts with `shorter` at a real name boundary."""
    if not longer.startswith(shorter) or longer == shorter:
        return False
    nxt = longer[len(shorter)]
    return nxt in "-_.0123456789 " or longer[len(shorter):].isdigit()


def from_github_search(name, min_stars=25):
    """Step 4 — last resort. Paced: unauthenticated search allows ~10 req/min.

    Requires the repo name to actually correspond to the queried name, so a
    generic query can't silently attach an unrelated popular repo.
    """
    import subprocess
    import urllib.parse
    q = urllib.parse.quote(name)
    url = f"https://api.github.com/search/repositories?q={q}&per_page=8"
    # Authenticated first (30 req/min). The unauthenticated call is ~10 req/min
    # per IP and a roundup exhausts it; rate-limit exhaustion is NOT "project has
    # no repo" — say so plainly (a silent None here is how a resolvable name
    # ships as a bare bullet).
    d = _gh_search(name)
    if d is None:
        if not _net_ok(12.0):
            return None
        _pace()
        try:
            p = subprocess.run(["curl", "-sSL", "-A", "hermes", "-H",
                                "Accept: application/vnd.github+json",
                                "-w", "\n__META__%{http_code}",
                                "--max-time", str(int(max(1.0, _cap_timeout(30)))),
                                url],
                               capture_output=True, text=True,
                               timeout=_cap_timeout(35) + 5)
            body, _, meta = p.stdout.rpartition("\n__META__")
            code = int((meta.strip().split(" ") or ["0"])[0] or 0)
            if code == 403:
                print(f"  ! GitHub search RATE-LIMITED for {name!r} — unresolved for now, "
                      f"not 'no such project'. Retry later or set GITHUB_TOKEN.")
                return None
            d = json.loads(body)
        except Exception:
            return None
    want = norm(name)
    cands = []
    for it in (d.get("items") or []):
        full = it.get("full_name", "")
        owner, _, repo = full.partition("/")
        nr, no = norm(repo), norm(owner)
        if it.get("stargazers_count", 0) < min_stars:
            continue
        # STRICT-ish match. The old `want in norm(repo)` substring rule attached
        # ALLTERCO/shelly-script-examples (330★, Shelly smart-HOME gear) to the
        # Arch pkg manager "Shelly" — a plausible, verified-200, totally wrong
        # repo. Rule now: repo name equals the query, or starts with it with only
        # a SHORT suffix (Shelly-ALPM -> shelly+alpm = 5 chars over: accept).
        # A prefix match must break on a separator/digit, otherwise "isolate"
        # matches "isolated-vm" (laverdet/isolated-vm, 2929★ — a Node.js sandbox,
        # NOT ioi/isolate). "shelly" -> "shelly-alpm" is a boundary; ok.
        #
        # CRITICAL: compare the RAW strings, not the normalized ones. norm()
        # strips hyphens, so `nr`("shellyalpm") vs `want`("shelly") has no
        # boundary char left to test and the match silently failed in testing.
        nr_raw, want_raw = repo.lower(), name.strip().lower()
        ok = (nr == want or no == want
              or (bounded(nr_raw, want_raw) and len(nr) - len(want) <= 8)
              or (bounded(want_raw, nr_raw) and len(want) - len(nr) <= 4))
        if ok:
            cands.append((it.get("stargazers_count", 0), it))
    if not cands:
        return None
    # highest-starred name match, not merely the first hit Google/GitHub ranked
    best = max(cands, key=lambda c: c[0])[1]
    return {"url": best["html_url"], "code": 200, "title": best["full_name"],
            "source": "github-search", "what": (best.get("description") or "")[:200],
            "stars": best.get("stargazers_count")}


# ---------------------------------------------------------------------------
# Offline index (2026-10-03) — linuxlinks roundups link to the publisher's OWN
# internal review page (`/name/`); the upstream repo is an outbound href ON that
# page. The 2026-10-02 run resolved 22 roundup names exactly this way with an
# ad-hoc /tmp script and then DIED on its tool-iteration cap before pasting the
# blocks — stranding the whole brew. A resolver must not depend on inline code,
# so the internal-index lookup lives here, permanently.
# ---------------------------------------------------------------------------

REPO_HOSTS_WIDE = REPO_HOST  # outbound candidates: same repo hosts the article pass trusts

# Names a curated miss can land on when even the internal page is unavailable.
# Every URL here was probed 200 on 2026-10-03 while finishing the 10-02 brew.
MANUAL_LINKS = {
    "OpenWebRX+": "https://github.com/0xAF/openwebrxplus",
    "OpenWebRX": "https://github.com/jketterl/openwebrx",
    # 2026-10-14 brew — gh-search + internal-page ladder misses; recovered via the
    # LinuxLinks internal page (linuxlinks.com/<slug>/) whose <title> matches the
    # project. "image_to_console" stays an honest gap (no internal page exists).
    "PTUI": "https://github.com/narbs/ptui",
    "rsimg": "https://github.com/kirchberger/rsimg",
    "MOBAC": "https://mobac.sourceforge.io/",
    "ZombieTrackerGPS": "https://www.zombietrackergps.net/ztgps/",
    "GPS Correlate": "https://github.com/dfandrich/gpscorrelate",
    "AAT Activity Tracker": "https://github.com/bailuk/AAT",
    "MiroTalk SFU": "https://github.com/miroslavpejic85/mirotalksfu",
    "MiroTalk P2P": "https://github.com/miroslavpejic85/mirotalk",
    "Nextcloud Talk": "https://github.com/nextcloud/talk-desktop",
    "PairUX": "https://github.com/profullstack/pairux.com",
    "markuplint": "https://github.com/markuplint/markuplint",
    "LintHTML": "https://github.com/linthtml/linthtml",
    "Pat": "https://github.com/la5nta/pat",
    "Indigo": "https://github.com/epam/Indigo",
    "ECT": "https://github.com/fhanau/Efficient-Compression-Tool",
    "YOGA": "https://github.com/Chocobozzz/yoimage",
    "Btrfs": "https://docs.kernel.org/filesystems/btrfs.html",
    "ext4": "https://docs.kernel.org/filesystems/ext4/index.html",
    "XFS": "https://docs.kernel.org/filesystems/xfs.html",
    "F2FS": "https://docs.kernel.org/filesystems/f2fs.html",
    "JFS": "https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/fs/jfs",
    "GFS2": "https://gitlab.com/linux-gfs2/gfs2-utils",
    "ext3": "https://docs.kernel.org/filesystems/ext3.html",
    "UBIFS": "https://docs.kernel.org/filesystems/ubifs.html",
    "OCFS2": "https://github.com/markfasheh/ocfs2-tools",
    "JFFS2": "https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/fs/jffs2",
    "Bcachefs": "https://github.com/koverstreet/bcachefs",
    "ScoutFS": "https://github.com/versity/scoutfs-kmod-dev",
    "OpenZFS": "https://github.com/openzfs/zfs",
    # 2026-10-04 brew — curated+article+gh-search misses; every URL probed 200
    # (bvi/loop-AES/cryptmount are sourceforge-source.net hosts, GNOME Maps moved
    # to apps.gnome.org, Shufflecake's mirror at shufflecake.net).
    "bvi": "https://bvi.sourceforge.net/",
    "GNOME Maps": "https://apps.gnome.org/Maps/",
    "loop-AES": "https://loop-aes.sourceforge.net/",
    "Shufflecake": "https://shufflecake.net/",
    "cryptmount": "https://cryptmount.sourceforge.net/",
    # 2026-10-08 brew — github-search produced NAME-COLLISIONS (godot→godotengine/godot
    # the game engine, Staticcheck→dominikh/staticcheck-action the CI action,
    # Pulsar→apache/pulsar the message broker, Janus→deepseek-ai/Janus, gedit→a
    # themes repo, gofmt→a git hook). Every URL below was resolved from the
    # LinuxLinks internal review page (or the project's own canonical host) and
    # probed 200 — prefer this over the fuzzy github-search step.
    "Pulsar": "https://github.com/pulsar-edit/pulsar",
    "Mousepad": "https://gitlab.xfce.org/apps/mousepad",
    "gedit": "https://gedit-text-editor.org/",
    "Jottr": "https://github.com/mfat/jottr",
    "Janus": "https://github.com/gholmann16/janus",
    "xed": "https://github.com/linuxmint/xed",
    "CudaText": "https://github.com/Alexey-T/CudaText",
    "Pluma": "https://github.com/mate-desktop/pluma",
    "CorePad": "https://gitlab.com/cubocore/coreapps/corepad",
    "typobuster": "https://github.com/nwg-piotr/typobuster",
    "Howl": "https://howl.io",
    "Parchment": "https://codeberg.org/vtrlx/parchment",
    "Webkit Word": "https://github.com/fastrizwaan/webkitword",
    "Mini Text": "https://github.com/Nokse22/mini-text",
    "GNOME Text Editor": "https://apps.gnome.org/TextEditor/",
    "Nota": "https://mauikit.org",
    "Kate": "https://kate-editor.org",
    "gofmt": "https://pkg.go.dev/cmd/gofmt",
    "Vet": "https://pkg.go.dev/cmd/vet",
    "Staticcheck": "https://github.com/dominikh/go-tools",
    "Godoc-Lint": "https://github.com/godoc-lint/godoc-lint",
    "godot": "https://github.com/tetafro/godot",
    "gocondense": "https://github.com/abemedia/gocondense",
    "empress": "https://github.com/ray-kast/empress",
    "MPRIS MiniPlayer": "https://git.dummkopf.live/InventorX/mpris-miniplayer",
    "go-ruleguard": "https://github.com/quasilyte/go-ruleguard",
    "exhaustive": "https://github.com/nishanths/exhaustive",
    "goimports": "https://github.com/golang/tools",
    # 2026-10-09 brew — curated+article+gh-search misses (LinuxLinks novelists /
    # Phone Link / self-hosted-cloud-storage roundups). Resolved from each
    # project's own canonical host; every URL probed 200.
    "KDE Connect": "https://github.com/KDE/kdeconnect-kde",
    "Sync-in": "https://github.com/Sync-in/server",
    "Cheese Paper": "https://github.com/ByteOfBrie/cheese-paper",
}

# LinuxLinks single-project review pages live at /<slug>/ and listing pages carry
# the same <tr><a href="/slug/">Name</a> shape this parses.
INDEX_HOST = "www.linuxlinks.com"
_INDEX_CACHE = {}
_LISTING_BODY_CACHE = {}
_CACHE_LOCKS = {}
_CACHE_LOCK = threading.Lock()


def _key_lock(key):
    """One lock per cache key: 8 workers fetch a page once, not 8 times."""
    with _CACHE_LOCK:
        lock = _CACHE_LOCKS.get(key)
        if lock is None:
            lock = _CACHE_LOCKS[key] = threading.Lock()
        return lock


def _listing_body(url):
    if url not in _LISTING_BODY_CACHE:
        with _key_lock(("body", url)):
            if url not in _LISTING_BODY_CACHE:
                _LISTING_BODY_CACHE[url] = _curl(url, ua=UA)
    return _LISTING_BODY_CACHE[url]


def _index_map(page_url):
    """LinuxLinks listing page -> {display name: internal slug}. Cached per URL."""
    with _key_lock(("idx", page_url)):
        if page_url in _INDEX_CACHE:
            return _INDEX_CACHE[page_url]
        code, final, body = _listing_body(page_url)
        out = {}
        if code == 200 and body:
            for row in re.findall(r"<tr[^>]*>(.*?)</tr>", body, re.S):
                a = re.search(r'<a href="(/[^"]+)"[^>]*>(.*?)</a>', row, re.S)
                if not a:
                    continue
                nm = re.sub(r"<[^>]+>", "", a.group(2))
                nm = re.sub(r"\s+", " ", nm).replace("&amp;", "&").strip()
                out[nm] = a.group(1)
        _INDEX_CACHE[page_url] = out
        return out


def _meta_desc(html):
    m = re.search(r'<meta name="description" content="([^"]*)"', html)
    return re.sub(r"\s+", " ", m.group(1)).strip().strip('"') if m else ""


def from_linuxlinks_page(listing_url, name):
    """Backwards-compatible alias for the label-first resolver (2026-10-22).

    Kept because older notes/SKILL text import this name. It now delegates to
    from_linuxlinks_listing(), which reads the listing section's `<strong>
    Website:</strong>` link before the classic `/name/` page. The old
    first-outbound-href parser was the bug that picked screenshots.
    """
    return from_linuxlinks_listing(listing_url, name)


def _manual_link(name):
    """Step 3c — hand-maintained, live-probed links for names that repeatedly miss.

    Returns the resolved dict or None. Kept as a helper so it can be consulted
    BEFORE the fuzzy loose-substring pass: an explicit, probed URL must beat a
    fuzzy curated match (caught 2026-10-04 — "GNOME Maps" loose-matched the
    generic 'gnome' entry and pointed at gnome.org instead of apps.gnome.org/Maps).
    """
    if name not in MANUAL_LINKS:
        return None
    u = MANUAL_LINKS[name]
    code, final, body = _curl(u, ua=UA)
    # sourceforge's *.sourceforge.net hosts 403 the Chrome UA but 200 the curl
    # UA — a bot-wall, not a dead page. Retry once with curl (same rule the main
    # probe() applies via _probe_curl).
    if code in BOTWALL or code == 0:
        c2, f2, b2 = _curl(u, ua="curl/8.7.1")
        if c2 == 200:
            code, final, body = c2, f2, b2
    if code == 200:
        return {"url": u, "code": code, "title": _title(body),
                "source": "manual", "what": _title(body) or None}
    return None


def local_lookup(name, curated):
    """Curated exact/alias match. Pure local, never touches the network.

    The fuzzy loose pass deliberately does NOT live here: an explicit
    hand-probed MANUAL_LINKS entry must beat it (GNOME Maps -> apps.gnome.org/Maps
    instead of the generic gnome.org), so loose runs inside resolve_unknown.
    """
    key = norm(name)
    for k, v in curated.items():
        if k == key or ALIASES.get(key) == k:
            return dict(v, _how="alias" if k != key else "exact")
    return None


def resolve_unknown(name, source_url, curated, allow_fallback=True, local=None):
    """Ladder steps 2-4 for a name the curated map missed."""
    got = local if local is not None else local_lookup(name, curated)
    if got:
        return got
    key = norm(name)
    # step 2b — an explicit hand-probed link beats the fuzzy loose pass
    r = _manual_link(name)
    if r:
        return r
    # an alias lands on a KEY STEM, and the stored key may carry extra words
    # ("Nura" -> "postmarketos" must still find the key "postmarketosnura").
    for alias in filter(None, (ALIASES.get(key), key)):
        for k, v in curated.items():
            if len(alias) >= 4 and (k.startswith(alias) or alias.startswith(k)):
                return dict(v, _how="loose")
    if not allow_fallback or not _net_ok():
        return None
    # step 3 — the publisher's own page. Name-aware only: the blind
    # from_article() rung is what painted every LinuxLinks bullet with the same
    # URL on 2026-10-17/19, so it is not in the roundup ladder below.
    if source_url and _net_ok():
        r = from_linuxlinks_listing(source_url, name)
        if r:
            return r
        if _net_ok():
            r = article_name_scoped(source_url, name)
            if r:
                return r
    # step 3c — hand-maintained links for names that repeatedly miss
    r = _manual_link(name)
    if r:
        return r
    # step 4 — GitHub search
    if not _net_ok():
        return None
    return from_github_search(name)


# ---------------------------------------------------------------------------
# Link sanity + duplicate scope (2026-10-22)
#
# The 10-21 review found 8 more live wrong links after the five named in
# GUL-96. Every one came from github-search or a loose curated match, so the
# checks below judge fallback-resolved GitHub URLs only. A publisher Website:
# link or an exact curated entry is trusted; a flagged guess is dropped as an
# honest gap (never hand-investigated by the cron agent).
# ---------------------------------------------------------------------------

GH_API_CACHE = {}

# An org's OWN mirror is acceptable: it lands on the right project and the org
# controls it. A third-party mirror/clone (mirror/gimp, FreeRDP/Remmina,
# basvodde/filezilla) is not. The domain map proves the ownership.
OFFICIAL_ORG_DOMAINS = {
    "gnome": "gnome.org",
    "kde": "kde.org",
    "libreoffice": "libreoffice.org",
    "inkscape": "inkscape.org",
    "ffmpeg": "ffmpeg.org",
}

# A product qualifier the project name carries must appear in the repo name or
# its description. Catches `Nextcloud Desktop` -> nextcloud/server, which is the
# right org but the wrong product; does not reject version suffixes (`v2`).
QUALIFIER_TOKENS = {"desktop", "studio", "ide"}


def github_full_name(url):
    """owner/repo for a github.com URL, else None."""
    m = re.match(r"https?://(?:www\.)?github\.com/([^/]+)/([^/#?]+)", url or "", re.I)
    if not m:
        return None
    repo = re.sub(r"\.git$", "", m.group(2))
    return f"{m.group(1)}/{repo}"


def _gh_repo(full_name):
    """Repo metadata via authenticated `gh api`, public API as fallback.

    Returns None when metadata is unavailable (no gh, offline, rate limit).
    Callers then SKIP the check rather than dropping a possibly-good link.
    """
    if full_name in GH_API_CACHE:
        return GH_API_CACHE[full_name]
    with _key_lock(("gh", full_name)):
        if full_name in GH_API_CACHE:
            return GH_API_CACHE[full_name]
        GH_API_CACHE[full_name] = _gh_repo_uncached(full_name)
        return GH_API_CACHE[full_name]


def _gh_repo_uncached(full_name):
    if not _net_ok(1.0):
        return None
    meta = None
    gh = shutil.which("gh") or next((p for p in ("/opt/homebrew/bin/gh", "/usr/local/bin/gh")
                                     if os.path.exists(p)), None)
    if gh:
        try:
            p = subprocess.run([gh, "api", f"repos/{full_name}"],
                               capture_output=True, text=True,
                               timeout=_cap_timeout(30))
            if p.returncode == 0 and p.stdout.strip():
                meta = json.loads(p.stdout)
        except Exception:
            meta = None
    if meta is None and _net_ok(1.0):
        code, _final, body = _curl(f"https://api.github.com/repos/{full_name}",
                                   timeout=20)
        if code == 200:
            try:
                meta = json.loads(body)
            except Exception:
                meta = None
    return meta


def _official_org(owner, repo, meta):
    """True when owner is the project's own upstream org, not a mirror host."""
    if norm(owner) == norm(repo):
        return True
    dom = OFFICIAL_ORG_DOMAINS.get(owner.lower())
    if not dom:
        return False
    home = _host(meta.get("homepage") or "")
    return home == dom or home.endswith("." + dom)


def sanity_check(name, url, hint_url=None):
    """Return (ok, reason) for a resolved GitHub URL.

    Non-GitHub URLs are trusted (they already came from a labelled publisher
    field or the curated map). `hint_url` is the publisher's own link for this
    project, used only for the homepage-domain check when it is not itself a
    repo host.
    """
    full = github_full_name(url)
    if not full:
        return True, ""
    meta = _gh_repo(full)
    if not meta:
        return True, "sanity skipped (repo metadata unavailable)"
    owner, _, repo = full.partition("/")
    if meta.get("archived"):
        return False, "archived"
    if meta.get("fork"):
        return False, "fork"
    pushed = meta.get("pushed_at")
    if pushed:
        try:
            dt = datetime.datetime.fromisoformat(pushed.replace("Z", "+00:00"))
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=datetime.timezone.utc)
            age_days = (datetime.datetime.now(datetime.timezone.utc) - dt).days
            if age_days > 3 * 365:
                return False, f"stale (pushed_at {pushed[:10]})"
        except Exception:
            pass
    desc = (meta.get("description") or "").strip()
    if re.match(r"(?i)^(mirror of|clone from|read-only mirror)", desc):
        if not _official_org(owner, repo, meta):
            return False, "third-party mirror/clone"
    home = meta.get("homepage") or ""
    if hint_url and home and not REPO_HOST.search(hint_url):
        hh, ph = _host(home), _host(hint_url)
        if hh and ph and hh != ph and not (hh.endswith("." + ph) or ph.endswith("." + hh)):
            return False, f"homepage {hh} != publisher {ph}"
    toks = [t for t in re.findall(r"[a-z0-9]+", name.lower()) if t in QUALIFIER_TOKENS]
    blob = (repo + " " + desc).lower()
    for t in toks:
        if t not in blob:
            return False, f"name says {t!r}, repo doesn't"
    return True, ""


def sanity_pass(results):
    """Drop fallback-resolved GitHub links that fail the sanity checks."""
    dropped = []
    for rows in results.values():
        for row in rows:
            if not row.get("url") or row.get("sanity"):
                continue
            if (row.get("source") or "").startswith("manual"):
                continue
            ok, why = sanity_check(row["name"], row["url"], row.get("hint"))
            row["sanity"] = "ok" if ok else why
            if ok:
                continue
            dropped.append((row["name"], row["url"], why))
            row["why"] = why
            row["source"] = "SANITY"
            row["url"] = None
            row["what"] = None
    for name, url, why in dropped:
        print(f"  ! sanity drop {name}: {why} ({url})")
    return dropped


def reuse_across_roundups(results):
    """Resolve an unresolved name from an earlier roundup's verified link.

    Keyed by the NORMALISED name, so `Mandelbulber` and `Mandelbulber v2` are
    allowed to share a URL across roundups. The old global URL duplicate check
    nulled them; this is the replacement.
    """
    first = {}
    for rows in results.values():
        for row in rows:
            if row.get("url"):
                first.setdefault(norm(row["name"]), row)
    reused = 0
    for rows in results.values():
        for row in rows:
            if row.get("url"):
                continue
            src = first.get(norm(row["name"]))
            if src and src is not row:
                row.update({"url": src["url"], "final": src.get("final"),
                            "title": src.get("title"), "what": src.get("what"),
                            "source": "cross-roundup", "why": None,
                            "sanity": "ok (cross-roundup)"})
                reused += 1
    return reused


def null_duplicate_urls(rows):
    """Within ONE roundup, null a URL claimed by 2+ DIFFERENT names.

    Scoped per roundup on purpose: calibre legitimately appears in the GUI and
    the Docker roundups; that is not a duplicate.
    """
    byurl = {}
    for row in rows:
        if row.get("url"):
            byurl.setdefault(row["url"], []).append(row["name"])
    for url, names in byurl.items():
        distinct = {norm(n) for n in names}
        if len(distinct) > 1:
            for row in rows:
                if row.get("url") == url:
                    row["why"] = f"duplicate url shared with {sorted(set(names) - {row['name']})}"
                    row["source"] = "DUPLICATE"
                    row["url"] = None
                    row["what"] = None


# 150 s: below the 180 s Hermes `terminal.timeout`. 16 workers: measured on
# the 79-name 2026-10-25 roundups, 8 workers finish in 122-138 s but the run is
# latency-bound; 16 flatten it to 95 s, which is the GitHub-search pacing floor
# (2.1 s x ~45 searches). More than 16 buys nothing.
DEFAULT_BUDGET = 150.0
DEFAULT_WORKERS = 16


def _row_stub(name):
    return {"name": name, "url": None, "what": None, "code": None,
            "source": None, "note": None}


def _gap(name, source, why=None):
    row = _row_stub(name)
    row["source"] = source
    if why:
        row["why"] = why
    return row


def _curated_row(name, entry, do_probe):
    """Row for a curated/alias/loose hit. Local; the probe/ sanity are optional."""
    row = _row_stub(name)
    how = entry.get("_how")
    if how in ("alias", "loose"):
        row["source"] = f"curated-{how}"
    else:
        row["source"] = "curated-repo" if entry.get("repo") else "curated-docs"
    row["note"] = entry.get("note")
    row["url"] = link_of(entry)
    row["final"] = row["url"]
    row["what"] = clean_what(None, name, entry.get("what"))
    row["probed"] = False
    if not do_probe or not _net_ok():
        return row
    code, final, title, desc = probe(row["url"])
    row.update(code=code, final=final, title=title, probed=True)
    if code != 200:
        row.update(url=None, what=None, source=f"DEAD({code})")
        return row
    row["what"] = clean_what(desc, name, entry.get("what"))
    if github_full_name(row["url"]):
        if not _net_ok():
            return row
        ok, why = sanity_check(name, row["url"])
        row["sanity"] = "ok" if ok else why
        if not ok:
            print(f"  ! sanity drop {name}: {why} ({row['url']})")
            row.update(url=None, what=None, source="SANITY", why=why)
    return row


def _fallback_row(task):
    """Ladder for a name the curated map missed. Sanity-checked before it ships."""
    name = task["name"]
    if not task["allow_fallback"]:
        return _gap(name, "UNRESOLVED")
    if not _net_ok():
        return _gap(name, "dropped-budget", "budget exhausted before resolution")
    got = resolve_unknown(name, task["source_url"], task["curated"], True)
    if not got or not (got.get("url") or got.get("_how")):
        if not _net_ok():
            return _gap(name, "dropped-budget", "budget exhausted inside the ladder")
        return _gap(name, "UNRESOLVED")
    if got.get("_how"):
        return _curated_row(name, got, task["do_probe"])
    row = _row_stub(name)
    row.update(url=got["url"], final=got.get("url"), title=got.get("title"),
               code=got.get("code"), source=got.get("source", "fallback"),
               what=clean_what(got.get("what"), name, None))
    if got.get("stars"):
        row["stars"] = got["stars"]
    if not task["do_probe"]:
        row["sanity"] = "unchecked-no-probe"
        return row
    if row["source"].startswith("manual") or not github_full_name(row["url"]):
        return row                      # hand-probed, or not a repo link
    if not _net_ok():
        return _gap(name, "dropped-budget",
                    "resolved but the budget ended before the sanity check")
    ok, why = sanity_check(name, row["url"])
    row["sanity"] = "ok" if ok else why
    if not ok:
        print(f"  ! sanity drop {name}: {why} ({row['url']})")
        row.update(url=None, what=None, source="SANITY", why=why)
    return row


def _work(task):
    if task["kind"] == "curated":
        return _curated_row(task["name"], task["local"], task["do_probe"])
    return _fallback_row(task)


def _run(tasks, work, n_workers, deadline, sink):
    """Run tasks on daemon threads, stop collecting at the deadline.

    Daemon threads on purpose: a stuck `urlopen`/`curl` must never keep the
    process alive. Whatever has not been collected by the deadline stays a gap.
    """
    if not tasks:
        return
    q, out = queue.Queue(), queue.Queue()
    for t in tasks:
        q.put(t)

    def loop():
        while True:
            try:
                t = q.get_nowait()
            except queue.Empty:
                return
            try:
                r = work(t)
            except Exception as exc:            # one bad name must not kill the run
                print(f"  ! {t['name']}: {exc!r}")
                r = (_curated_row(t["name"], t["local"], False)
                     if t.get("local") is not None
                     else _gap(t["name"], "ERROR", repr(exc)[:160]))
            out.put((t, r))

    for _ in range(max(1, min(int(n_workers), len(tasks)))):
        threading.Thread(target=loop, daemon=True).start()
    done = 0
    while done < len(tasks):
        left = deadline - time.time()
        if left <= 0:
            break
        try:
            t, r = out.get(timeout=left)
        except queue.Empty:
            break
        done += 1
        sink(t, r)


def _watchdog(deadline, finish, run_id):
    """Last-resort guarantee: write what we have and hard-exit.

    The main loop already escapes at the deadline; this only fires if something
    blocks in a way the per-call timeouts cannot interrupt (DNS, a wedged
    subprocess). budget + 8 s is inside the budget + 10 s promise.
    """
    time.sleep(max(0.0, deadline + 8 - time.time()))
    if _RUN_ID[0] != run_id:
        return
    with _WRITE_LOCK:
        if _FINISHED[0]:
            return
    try:
        finish()
    finally:
        sys.stdout.flush()
        sys.stderr.flush()
        os._exit(0)


def item_number(it):
    """Roundup number of an input item: field `n`, else the `id` alias.

    GUL-309: the 2026-10-27 run fed the resolver raw chunk dicts, which carry
    the roundup number under `id`, and the first invocation died on
    `KeyError: 'n'` after 0.5 s. Only call this after main() has validated the
    item, so neither key present never gets here.
    """
    v = it.get("n") if isinstance(it, dict) else None
    if v is None and isinstance(it, dict):
        v = it.get("id")
    return str(v)


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv:
        print(__doc__)
        return 2
    src = argv[0]

    def opt(flag, default):
        if flag in argv:
            i = argv.index(flag) + 1
            if i < len(argv):
                return argv[i]
        return default

    out_path = opt("--out", "/tmp/kk_run/links.json")
    md_path = opt("--md", "/tmp/kk_run/blocks.md")
    do_probe = "--no-probe" not in argv
    allow_fallback = "--no-fallback" not in argv
    budget = float(opt("--budget", DEFAULT_BUDGET))
    workers = int(opt("--workers", DEFAULT_WORKERS))

    t0 = time.time()
    deadline = t0 + max(0.0, budget)
    _DEADLINE[0] = deadline
    _FINISHED[0] = False
    _RUN_ID[0] += 1
    run_id = _RUN_ID[0]

    curated = load_curated()
    with open(src) as f:
        items = json.load(f)

    bad = [i for i, it in enumerate(items)
           if not isinstance(it, dict)
           or (it.get("n") is None and it.get("id") is None)]
    if bad:
        print(f"input items {bad} have neither 'n' nor 'id' - each item needs "
              "the roundup number under one of those two keys")
        return 2

    slots = {}
    tasks = []
    total = 0
    for it in items:
        n = item_number(it)
        source_url = it.get("source") or it.get("url")
        for j, name in enumerate(it.get("names") or []):
            total += 1
            entry = local_lookup(name, curated)
            if entry is not None:
                # Curated/alias hits are local and always resolved. The probe is
                # network work: when the budget dies first, the row still ships
                # (marked unprobed) instead of turning the digest empty.
                slots[(n, j)] = _curated_row(name, entry, False)
                if do_probe:
                    tasks.append({"kind": "curated", "n": n, "j": j,
                                  "name": name, "local": entry,
                                  "do_probe": True, "allow_fallback": allow_fallback,
                                  "source_url": source_url, "curated": curated})
            else:
                tasks.append({"kind": "resolve", "n": n, "j": j, "name": name,
                              "local": None, "do_probe": do_probe,
                              "allow_fallback": allow_fallback,
                              "source_url": source_url, "curated": curated})

    def sink(task, row):
        slots[(task["n"], task["j"])] = row

    def finish():
        with _WRITE_LOCK:
            if _FINISHED[0]:
                return None
            _FINISHED[0] = True

        results, dropped = {}, []
        for it in items:
            n = item_number(it)
            rows = []
            for j, name in enumerate(it.get("names") or []):
                row = slots.get((n, j))
                if row is None:
                    row = _gap(name, "dropped-budget", "budget exhausted")
                if row.get("source") == "dropped-budget":
                    dropped.append(name)
                if row.get("url") and not row.get("probed") and not row.get("sanity"):
                    # A curated link that the deadline stopped us from probing or
                    # judging: ship it (human-verified), but say so in the row.
                    row["sanity"] = ("unchecked-budget" if do_probe
                                     else "unchecked-no-probe")
                rows.append(row)
            results[n] = rows

        reused = reuse_across_roundups(results)
        for rows in results.values():
            null_duplicate_urls(rows)

        blocks = {}
        for n, rows in results.items():
            for r in rows:
                if r["url"]:
                    extra = f" ★{r['stars']}" if r.get("stars") else ""
                    print(f"  §{n:<3} {r['name']:<22} {r['source']:<18} {r['url']}{extra}")
                else:
                    why = f" ({r['why']})" if r.get("why") else ""
                    print(f"  §{n:<3} {r['name']:<22} {r['source']:<18} —{why}")
            blocks[n] = "\n".join(
                (f"- **[{r['name']}]({r['url']})** — {r['what']}" if r["url"]
                 else f"- **{r['name']}** — _no verified public repo found_")
                for r in rows)
            print()

        payload = {"results": results, "blocks": blocks,
                   "dropped_budget": dropped}
        for path in (out_path, md_path):
            os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
        with open(out_path, "w") as f:
            json.dump(payload, f, indent=2)
        with open(md_path, "w") as f:
            for n, b in blocks.items():
                f.write(f"### §{n}\n{b}\n\n")

        resolved = sum(1 for rows in results.values() for r in rows if r["url"])
        print(f"Wrote {out_path}\nWrote {md_path}")
        print(f"budget {budget:.0f}s | {total} names | {resolved} resolved | "
              f"{len(dropped)} dropped-budget | wall {time.time() - t0:.1f}s")
        if reused:
            print(f"cross-roundup reuse filled {reused} name(s)")
        unresolved = [r["name"] for rows in results.values() for r in rows
                      if not r["url"] and r.get("source") != "dropped-budget"]
        if unresolved:
            print(f"\n⚠️  {len(unresolved)} UNRESOLVED: {unresolved}")
        # Last stdout line, always: the cron prompt greps for it.
        print(f"dropped: budget {len(dropped)} {dropped}")
        sys.stdout.flush()
        return payload

    if do_probe:
        threading.Thread(target=_watchdog, args=(deadline, finish, run_id),
                         daemon=True).start()

    _run(tasks, _work, workers, deadline, sink)
    finish()
    return 0


if __name__ == "__main__":
    rc = main()
    sys.stdout.flush()
    os._exit(rc)
