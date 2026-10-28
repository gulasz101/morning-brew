"""A reasoning model's empty reply must become a visible drop, not a vanished item.

GUL-527: beam-free-go spent its whole max_tokens on thinking, answered
`finish_reason: length` with `content: null`, `extract_json` called `.strip()` on None,
the worker thread died and the item was in neither `items` nor `dropped` in report.json.
"""

from __future__ import annotations

import io
import json
import sys
from pathlib import Path

import pytest

PIPELINE = Path(__file__).resolve().parent.parent
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

import brew  # noqa: E402
from lib import model as modelmod  # noqa: E402
from lib.model import ModelError, Writer  # noqa: E402


def reply(content, finish="stop") -> dict:
    return {"choices": [{"message": {"content": content}, "finish_reason": finish}]}


def serve(monkeypatch, payload: dict) -> None:
    class Response(io.BytesIO):
        def __enter__(self):
            return self

        def __exit__(self, *exc):
            return False

    data = json.dumps(payload).encode()
    monkeypatch.setattr(modelmod.urllib.request, "urlopen",
                        lambda *args, **kwargs: Response(data))


def test_null_content_is_a_model_error(monkeypatch):
    serve(monkeypatch, reply(None, "length"))
    with pytest.raises(ModelError) as exc:
        Writer("beam-free-go", "https://example.invalid/v1", "k").call("system", "user")
    assert "empty reply" in str(exc.value)
    assert "length" in str(exc.value)


def test_truncated_reply_is_a_model_error(monkeypatch):
    serve(monkeypatch, reply('{"title": "cut off mid', "length"))
    with pytest.raises(ModelError) as exc:
        Writer("beam-free-go", "https://example.invalid/v1", "k").call("system", "user")
    assert "truncated" in str(exc.value)


def test_a_real_reply_is_returned(monkeypatch):
    serve(monkeypatch, reply('{"title": "fine"}'))
    out = Writer("beam-free-go", "https://example.invalid/v1", "k").call("system", "user")
    assert out == '{"title": "fine"}'


def test_crash_row_is_a_dropped_row():
    row = brew.crash_row(
        {"id": "abc123", "title": "Tried Banning AI And It Ends Badly"},
        AttributeError("'NoneType' object has no attribute 'strip'"),
    )
    assert row["id"] == "abc123"
    assert row["status"] == "dropped"
    assert row["errors"][0].startswith("AttributeError:")
    assert "strip" in row["errors"][0]


def test_a_crashed_item_stays_in_the_report(tmp_path):
    path = tmp_path / "report.json"
    reporter = brew.Reporter(path, {"date": "2026-10-27"})
    reporter.add_item(brew.crash_row({"id": "abc123", "title": "x"}, RuntimeError("boom")))
    reporter.update(finished="2026-10-27T06:10:00+02:00",
                    counts={"ok": 0, "retried": 0, "dropped": 1, "items": 0})
    data = json.loads(path.read_text())
    assert data["items"][0]["id"] == "abc123"
    assert data["items"][0]["status"] == "dropped"
    assert data["counts"]["dropped"] == 1
