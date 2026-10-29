"""No item may vanish: a crash or a null reply becomes a visible dropped row."""

from __future__ import annotations

import io
import json
import urllib.request

import brew
import pytest
from lib.config import load_config


class FakeResponse:
    def __init__(self, payload: dict):
        self._buf = io.BytesIO(json.dumps(payload).encode())

    def read(self, *args):
        return self._buf.read(*args)

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


NULL_REPLY = {
    "choices": [{"message": {"role": "assistant", "content": None}, "finish_reason": "stop"}],
    "usage": {"prompt_tokens": 1556, "completion_tokens": 7091, "total_tokens": 8647,
              "completion_tokens_details": {"reasoning_tokens": 6775}},
}


def run_dry(monkeypatch, tmp_path, *, urlopen=None, article=None):
    """Run one dry-run item through `brew.main` with the network and inputs faked."""
    cfg = load_config()
    cfg["writer"]["model"] = "beam-free-go"
    monkeypatch.setattr(brew, "load_config", lambda: cfg)
    monkeypatch.setattr(brew, "require_env", lambda name, why: "not-a-real-key")
    monkeypatch.setattr(brew, "ensure_inputs", lambda day, cfg, rundir, resume: (
        {"bookmarks": [{"id": "k1", "title": "Some item", "url": "https://example.com/x",
                        "source": "rss"}]},
        {"bookmarks": []},
    ))
    if article is not None:
        monkeypatch.setattr(brew.linklib, "article_text", article)
    else:
        monkeypatch.setattr(brew.linklib, "article_text",
                            lambda it, cfg, key, server: ("body text " * 40, "article"))
    if urlopen is not None:
        monkeypatch.setattr(urllib.request, "urlopen", urlopen)
    run = tmp_path / "run"
    run.mkdir()
    monkeypatch.setattr(brew.tempfile, "mkdtemp", lambda prefix="": str(run))
    rc = brew.main(["--date", "2026-10-27", "--dry-run"])
    return rc, json.loads((run / "report.json").read_text())


def test_a_null_writer_reply_lands_in_report_json_as_dropped(monkeypatch, tmp_path):
    rc, report = run_dry(monkeypatch, tmp_path,
                         urlopen=lambda req, timeout=None: FakeResponse(NULL_REPLY))
    assert rc == 1
    rows = [r for r in report["items"] if r["id"] == "k1"]
    assert len(rows) == 1, "the item must be in report.json, dropped or ok"
    assert rows[0]["status"] == "dropped"
    assert "empty reply" in rows[0]["errors"][0]
    assert report["counts"]["dropped"] == 1
    assert report["counts"]["ok"] == 0


def test_a_crashing_stage_lands_in_report_json_as_dropped(monkeypatch, tmp_path):
    def boom(it, cfg, key, server):
        raise AttributeError("'NoneType' object has no attribute 'strip'")

    rc, report = run_dry(monkeypatch, tmp_path, article=boom)
    assert rc == 1
    rows = [r for r in report["items"] if r["id"] == "k1"]
    assert len(rows) == 1
    assert rows[0]["status"] == "dropped"
    assert rows[0]["errors"][0].startswith("worker crashed: AttributeError")
    assert report["counts"]["dropped"] == 1


def test_guard_item_records_a_crash_and_a_success(tmp_path):
    rep = brew.Reporter(tmp_path / "report.json", {"date": "2026-10-27"})
    recorded: list[dict] = []

    def record(row: dict) -> None:
        recorded.append(row)
        rep.add_item(row)

    def boom() -> dict:
        raise ValueError("writer exploded")

    brew.guard_item({"id": "k1", "title": "First"}, boom, record)
    brew.guard_item({"id": "k2", "title": "Second"},
                    lambda: {"status": "ok", "errors": [], "tries": 1}, record)

    saved = json.loads((tmp_path / "report.json").read_text())["items"]
    assert [r["status"] for r in saved] == ["dropped", "ok"]
    assert "ValueError: writer exploded" in saved[0]["errors"][0]
    assert recorded[1]["id"] == "k2"


def test_model_limits_come_from_the_config():
    cfg = load_config()
    default = brew.model_limits(cfg, "deepseek-v4.1-flash-ollama")
    assert default == {"max_tokens": 2000, "article_chars": 14000, "transcript_chars": 26000}
    reasoning = brew.model_limits(cfg, "beam-free-go")
    # The exact cap is a tuning knob (GUL-528 measured 8000): assert the shape, not the number.
    assert reasoning["max_tokens"] > default["max_tokens"]
    assert reasoning["transcript_chars"] < default["transcript_chars"]
    assert reasoning["article_chars"] < default["article_chars"]


def test_clip_keeps_the_head_and_the_tail():
    text = "A" * 1000 + "B" * 1000
    out = brew.clip(text, 200)
    assert out.startswith("A")
    assert out.endswith("B")
    assert "[... middle of the source omitted ...]" in out
    assert len(out) < 300
    assert brew.clip("short", 200) == "short"
