"""Every project the validator allows must have a paragraph, and every paragraph a name.

The writer only knows the projects in `prompts/projects.md`, and it may only answer with the
names in `[projects].allowed`. When those two lists drift apart one of two things happens
quietly: a project with no paragraph gets "Nothing for my projects" forever, or the writer
picks a name the validator then rejects until the retry is spent.
"""

from __future__ import annotations

import re
from pathlib import Path

from lib.config import load_config

PROJECTS_MD = Path(__file__).resolve().parent.parent / "prompts" / "projects.md"


def documented() -> dict[str, str]:
    """`## name` headings and the paragraph under each, in file order."""
    out: dict[str, str] = {}
    name = None
    body: list[str] = []
    for line in PROJECTS_MD.read_text().splitlines():
        heading = re.match(r"^## (\S+)\s*$", line)
        if heading:
            if name:
                out[name] = " ".join(body).strip()
            name, body = heading.group(1), []
        elif name and line.strip():
            body.append(line.strip())
    if name:
        out[name] = " ".join(body).strip()
    return out


def test_allowed_projects_and_paragraphs_are_the_same_list():
    allowed = list(load_config()["projects"]["allowed"])
    assert list(documented()) == allowed


def test_every_paragraph_says_enough_to_match_on():
    for name, text in documented().items():
        assert len(text.split()) >= 25, f"{name} has {len(text.split())} words, too thin to match"
