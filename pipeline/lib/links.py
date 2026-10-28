"""Article text and candidate links. The model only ever picks indices into this list."""

from __future__ import annotations

import html as html_mod
import json
import re
import subprocess
import urllib.request
from pathlib import Path

UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 "
    "(KHTML, like Gecko) Version/17.0 Safari/605.1.15"
)

_URL_RE = re.compile(r"https?://[^\s<>\"'\)\]\}]+")

# Hosts that are never a project homepage in a digest item.
NOISE_HOSTS = {
    "twitter.com", "x.com", "facebook.com", "instagram.com", "linkedin.com",
    "reddit.com", "t.co", "bit.ly", "threads.net", "mastodon.social", "bsky.app",
    "youtube.com", "youtu.be", "youtube-nocookie.com", "medium.com", "substack.com",
    "patreon.com", "ko-fi.com", "buymeacoffee.com", "amazon.com", "amzn.to",
    "google.com", "doubleclick.net", "googletagmanager.com", "gstatic.com",
    "cdn.jsdelivr.net", "unpkg.com", "gravatar.com", "shields.io", "badge.fury.io",
    "paypal.com", "stripe.com", "discord.gg", "discord.com", "t.me", "telegram.me",
}
CODE_HOSTS = {"github.com", "gitlab.com", "codeberg.org", "sr.ht", "git.sr.ht"}

ROUNDUP_RE = re.compile(
    r"(?<![\d.])\d+\s+(?:best|great|top|open[- ]source|free|new|essential|awesome)"
    r"|\bbest\s+(?:free|open[- ]source)\b"
    r"|\balternatives?\s+to\b"
    r"|\broundup\b",
    re.IGNORECASE,
)


def _host(url: str) -> str:
    m = re.match(r"https?://([^/]+)", url)
    host = (m.group(1) if m else "").lower()
    return host[4:] if host.startswith("www.") else host


def strip_html(raw: str) -> str:
    raw = re.sub(r"(?is)<(script|style|noscript|svg)[^>]*>.*?</\1>", " ", raw)
    raw = re.sub(r"(?is)<br\s*/?>|</p>|</div>|</li>|</h[1-6]>", "\n", raw)
    raw = re.sub(r"(?s)<[^>]+>", " ", raw)
    text = html_mod.unescape(raw)
    text = re.sub(r"[ \t\xa0]+", " ", text)
    text = re.sub(r"\n\s*\n+", "\n\n", text)
    return text.strip()


def karakeep_asset(server: str, api_key: str, asset_id: str, timeout: int = 60) -> str:
    """Karakeep's own crawled copy of the page, served as the stored asset."""
    if not asset_id:
        return ""
    req = urllib.request.Request(
        f"{server.rstrip('/')}/api/v1/assets/{asset_id}",
        headers={"Authorization": f"Bearer {api_key}", "User-Agent": "curl/8.0"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            raw = r.read().decode("utf-8", "replace")
    except Exception:
        return ""
    if raw.lstrip().startswith("{"):
        try:
            meta = json.loads(raw)
        except json.JSONDecodeError:
            return ""
        for key in ("text", "content", "htmlContent"):
            if isinstance(meta.get(key), str):
                return strip_html(meta[key])
        return ""
    return strip_html(raw)


def fetch_plain(url: str, timeout: int = 40) -> str:
    """Second best: a plain fetch of the page."""
    try:
        out = subprocess.run(
            ["curl", "-sL", "--max-time", str(timeout), "-A", UA, url],
            capture_output=True,
            timeout=timeout + 15,
        )
        return strip_html(out.stdout.decode("utf-8", "replace"))
    except Exception:
        return ""


def transcript_text(item: dict, vault_root: Path | None = None) -> str:
    """The enrichment stage records the transcript path; older manifests inline it."""
    val = item.get("transcript")
    if not val:
        return ""
    if isinstance(val, str):
        p = Path(val)
        if not p.is_absolute() and vault_root is not None:
            p = vault_root / val
        if p.exists():
            try:
                return p.read_text(errors="replace")
            except OSError:
                return ""
        return val if len(val) > 200 else ""
    if isinstance(val, dict):
        for key in ("text", "path"):
            v = val.get(key)
            if isinstance(v, str) and v:
                if key == "path" and vault_root and Path(v).exists():
                    return Path(v).read_text(errors="replace")
                if key == "text":
                    return v
    return ""


def article_text(item: dict, cfg: dict, karakeep_key: str, karakeep_server: str) -> tuple[str, str]:
    """Karakeep's crawled copy first, a plain fetch second. Returns (text, source)."""
    raw = item.get("raw") or {}
    content = raw.get("content") or {}
    asset_id = content.get("contentAssetId") or item.get("contentAssetId") or ""
    text = karakeep_asset(karakeep_server, karakeep_key, asset_id)
    if len(text) > 400:
        return text, "karakeep"
    url = item.get("url") or content.get("url") or ""
    if url:
        text = fetch_plain(url)
        if len(text) > 400:
            return text, "fetch"
    # Last resort, still not model text: the crawler's own description + summary.
    fallback = "\n".join(
        part for part in (content.get("description") or "", raw.get("summary") or "") if part
    )
    return fallback, "karakeep-summary"


def _clean_url(url: str) -> str:
    url = url.rstrip(".,;:!?)>\"'")
    url = re.sub(r"[?&]utm_[^&]*", "", url)
    url = re.sub(r"\?$", "", url)
    return url


def candidates(item: dict, text: str, extra: list[dict] | None = None, cap: int = 24) -> list[dict]:
    """Numbered candidate links: article text, enriched repo, roundup resolver results.

    Every URL here was found somewhere real. Nothing is ever invented.
    """
    seen: dict[str, dict] = {}

    def add(url: str, label: str, where: str) -> None:
        url = _clean_url(url.strip())
        if not url.startswith("http") or url in seen:
            return
        host = _host(url)
        if not host or host in NOISE_HOSTS:
            return
        code = any(host == h or host.endswith("." + h) for h in CODE_HOSTS)
        generic = not code and where != "roundup"
        if generic and not _looks_like_homepage(url):
            return
        seen[url] = {"url": url, "label": label or host, "where": where, "code": code}

    for url in _URL_RE.findall(text or ""):
        add(url, _host(url), "article")

    raw = item.get("raw") or {}
    for key in ("repo", "project_url"):
        val = item.get(key)
        if isinstance(val, str) and val:
            if not val.startswith("http"):
                val = f"https://github.com/{val.strip('/')}"
            add(val, _host(val) + "/" + val.rstrip("/").split("/")[-1], "enriched")
    gh = item.get("gh_meta") or {}
    if isinstance(gh, dict) and gh.get("full_name"):
        add(f"https://github.com/{gh['full_name']}", gh["full_name"], "enriched")
    if raw.get("_project_url"):
        add(raw["_project_url"], _host(raw["_project_url"]), "enriched")

    for row in extra or []:
        url = row.get("url") or ""
        if url.startswith("http"):
            add(url, row.get("name") or _host(url), "roundup")

    return list(seen.values())[:cap]


def _looks_like_homepage(url: str) -> bool:
    """A project homepage, not a news article or a category page."""
    path = re.sub(r"^https?://[^/]+", "", url)
    if path in ("", "/"):
        return True
    bits = [b for b in path.split("/") if b]
    if len(bits) > 2:
        return False
    if re.search(r"/(20\d\d|blog|news|category|tag|page)/", path):
        return False
    return True


def is_roundup_title(title: str) -> bool:
    return bool(ROUNDUP_RE.search(title or ""))


def format_candidates(rows: list[dict]) -> str:
    return "\n".join(
        f"[{i}] {row['label']} | {row['url']} | found in {row['where']}"
        for i, row in enumerate(rows, start=1)
    )
