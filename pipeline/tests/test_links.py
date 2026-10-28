"""Link candidates: only real URLs, numbered, noise dropped, never model text."""

from __future__ import annotations

from lib.links import candidates, format_candidates, is_roundup_title

ARTICLE = """
<p>See <a href="https://github.com/morluto/rea">REA</a> and
<a href="https://x.com/someone/status/1">a tweet</a>. Docs at
https://rea.example.dev and a long read at https://example.com/2026/10/some-article-here.
Mirror: https://gitlab.com/foo/bar. Sponsor: https://ko-fi.com/nerd.</p>
"""


def test_candidates_are_numbered_and_deduped():
    rows = candidates({}, ARTICLE)
    urls = [r["url"] for r in rows]
    assert "https://github.com/morluto/rea" in urls
    assert "https://gitlab.com/foo/bar" in urls
    assert len(urls) == len(set(urls))
    listing = format_candidates(rows)
    assert listing.startswith("[1] ")


def test_noise_hosts_are_dropped():
    urls = [r["url"] for r in candidates({}, ARTICLE)]
    assert not any("x.com" in u or "ko-fi.com" in u for u in urls)


def test_article_paths_are_not_project_homepages():
    """A news article is not a project link, a short path is."""
    urls = [r["url"] for r in candidates({}, ARTICLE)]
    assert "https://rea.example.dev" in urls
    assert not any("/2026/10/" in u for u in urls)


def test_enriched_repo_and_roundup_rows_are_added():
    item = {"repo": "gulasz101/homelab-2nd", "gh_meta": {"full_name": "gulasz101/morning-brew"}}
    rows = candidates(item, "", extra=[{"name": "Kitty", "url": "https://github.com/kovidgoyal/kitty"}])
    urls = [r["url"] for r in rows]
    assert "https://github.com/gulasz101/homelab-2nd" in urls
    assert "https://github.com/gulasz101/morning-brew" in urls
    assert "https://github.com/kovidgoyal/kitty" in urls
    assert [r["where"] for r in rows].count("roundup") == 1


def test_roundup_titles():
    assert is_roundup_title("7 Best Free and Open Source Terminal Emulators")
    assert is_roundup_title("Open-source alternatives to Synology apps")
    assert not is_roundup_title("Zed 1.5.2 Released")
    assert not is_roundup_title("MOSS Image with control and references")
