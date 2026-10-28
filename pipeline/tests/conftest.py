"""Shared fixtures: the three 2026-10-27 items and the candidate link list."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

PIPELINE = Path(__file__).resolve().parent.parent
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

FIXTURES = Path(__file__).parent / "fixtures"


@pytest.fixture(scope="session")
def sample() -> dict:
    return json.loads((FIXTURES / "2026-10-27-items.json").read_text())


@pytest.fixture(scope="session")
def items(sample) -> list[dict]:
    return sample["items"]


@pytest.fixture()
def links() -> list[dict]:
    return [
        {"label": "morluto/rea", "url": "https://github.com/morluto/rea", "code": True,
         "where": "article"},
        {"label": "techradar.com", "url": "https://www.techradar.com/news/example",
         "code": False, "where": "article"},
        {"label": "asmeurer/mypython", "url": "https://github.com/asmeurer/mypython",
         "code": True, "where": "enriched"},
    ]
