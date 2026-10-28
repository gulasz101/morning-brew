"""Template render: the fixed shape, no dashes, no invented URLs."""

from __future__ import annotations

import re

from lib.item import render

META = {
    "title": "MOSS Image with control, references and editing in ComfyUI",
    "source": "Nerdy Rodent",
    "url": "https://youtu.be/hTCjWfbyCjU",
    "id": "zw1ob3khs3nh247xflmip9h4",
    "image": "https://i.ytimg.com/vi/hTCjWfbyCjU/maxresdefault.jpg",
}


def test_exact_shape(items, links):
    entry = items[1]
    out = render(3, entry["reply"], META, links)
    lines = out.splitlines()
    assert lines[0] == "## 3. MOSS Image with control, references and editing in ComfyUI, by Nerdy Rodent"
    assert lines[1] == "![](https://i.ytimg.com/vi/hTCjWfbyCjU/maxresdefault.jpg)"
    assert lines[2].startswith("**Project:** [rea](https://github.com/morluto/rea)")
    assert lines[3] == "**Source:** https://youtu.be/hTCjWfbyCjU · **Karakeep:** `zw1ob3khs3nh247xflmip9h4`"
    assert "**In short:** " in out
    assert "**Key points:**" in out
    assert out.count("- ") >= 3
    assert "**Details:** " in out
    assert "**For my projects:**\n- ideogram4-local: " in out


def test_nothing_for_my_projects_line(items, links):
    entry = items[0]
    out = render(1, entry["reply"], META, links)
    assert "**For my projects:** Nothing for my projects." in out


def test_no_project_line_when_no_links_picked(items, links):
    reply = dict(items[2]["reply"], project_links=[])
    out = render(1, reply, META, links)
    assert "**Project:**" not in out


def test_roundup_projects_block_at_the_end(items, links):
    resolved = [
        {"name": "Alacritty", "url": "https://github.com/alacritty/alacritty", "what": "GPU terminal"},
        {"name": "Kitty", "url": "https://github.com/kovidgoyal/kitty", "what": "GPU terminal"},
    ]
    out = render(4, items[2]["reply"], META, links, resolved)
    assert out.rstrip().endswith("- [Kitty](https://github.com/kovidgoyal/kitty): GPU terminal")
    assert out.count("**Projects:**") == 1


def test_no_dashes_anywhere_in_the_template(items, links):
    for entry in items:
        out = render(1, entry["reply"], META, links)
        assert "\u2014" not in out and "\u2013" not in out


def test_urls_come_only_from_the_candidate_list(items, links):
    out = render(1, items[1]["reply"], META, links)
    found = set(re.findall(r"https?://[^\s\)]+", out))
    allowed = {r["url"] for r in links} | {META["url"], META["image"]}
    assert found <= allowed
