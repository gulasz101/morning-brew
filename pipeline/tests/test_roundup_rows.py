"""Roundup links.json shapes: the resolver's real output must reach the renderer.

The nightly run on 2026-10-28 shipped three roundups with no **Projects:** block
because brew.py read links.json looking for "roundups"/"items" while the resolver
writes {"results": {"<n>": [row, ...]}}. These tests pin both shapes.
"""

from __future__ import annotations

from brew import parse_roundup_rows


def test_flat_results_rows():
    data = {"results": {"16": [
        {"name": "nnn", "url": "https://github.com/jarun/nnn", "what": "file manager", "code": 200},
    ]}}
    assert parse_roundup_rows(data, 16) == [
        {"name": "nnn", "url": "https://github.com/jarun/nnn", "what": "file manager"},
    ]


def test_nested_projects_rows():
    data = [{"n": 16, "projects": [{"name": "x", "url": "https://x.example"}]}]
    assert parse_roundup_rows(data, 16) == [
        {"name": "x", "url": "https://x.example", "what": ""},
    ]


def test_missing_number_is_empty():
    assert parse_roundup_rows({"results": {"1": [{"name": "a", "url": "https://a.example"}]}}, 16) == []


def test_falls_back_to_final_url():
    data = {"results": {"41": [{"name": "GnuPG", "final": "https://gnupg.org/"}]}}
    assert parse_roundup_rows(data, 41) == [{"name": "GnuPG", "url": "https://gnupg.org/", "what": ""}]
