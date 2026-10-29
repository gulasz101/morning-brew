"""The writer client: a null or truncated reply is a ModelError, never a silent None."""

from __future__ import annotations

import io
import json
import urllib.request

import pytest

from lib.model import EDGE_TIMEOUT_SEC, ModelError, Writer, extract_json


class FakeResponse:
    """Just enough of an http.client response for json.load()."""

    def __init__(self, payload: dict):
        self._buf = io.BytesIO(json.dumps(payload).encode())

    def read(self, *args):
        return self._buf.read(*args)

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


def reply(content, finish: str = "stop") -> dict:
    return {
        "choices": [{"message": {"role": "assistant", "content": content},
                     "finish_reason": finish}],
        "usage": {"prompt_tokens": 1556, "completion_tokens": 7091, "total_tokens": 8647,
                  "completion_tokens_details": {"reasoning_tokens": 6775}},
    }


def fake_writer(monkeypatch, payload: dict, **kw) -> Writer:
    monkeypatch.setattr(urllib.request, "urlopen",
                        lambda req, timeout=None: FakeResponse(payload))
    return Writer("beam-free-go", "https://llm.example/v1", "not-a-real-key", **kw)


def test_null_content_is_a_model_error(monkeypatch):
    """finish_reason=stop with content=null used to reach extract_json and die there."""
    w = fake_writer(monkeypatch, reply(None))
    with pytest.raises(ModelError) as exc:
        w.call("system", "user")
    message = str(exc.value)
    assert "empty reply" in message
    assert "NoneType" in message
    assert "reasoning_tokens=6775" in message


def test_a_length_cut_is_a_model_error(monkeypatch):
    """A reply that spent the whole budget thinking answers content="" + length."""
    w = fake_writer(monkeypatch, reply("", "length"))
    with pytest.raises(ModelError) as exc:
        w.call("system", "user")
    assert "finish_reason=length" in str(exc.value)
    assert "hit the token limit" in str(exc.value)


def test_a_good_reply_comes_back_verbatim(monkeypatch):
    w = fake_writer(monkeypatch, reply('{"in_short": "fine"}'))
    assert extract_json(w.call("system", "user")) == {"in_short": "fine"}


def test_extract_json_refuses_none_instead_of_raising_attributeerror():
    with pytest.raises(ModelError):
        extract_json(None)
    with pytest.raises(ModelError):
        extract_json("   ")


def test_the_client_timeout_always_sits_below_the_edge():
    w = Writer("m", "https://llm.example/v1", "k")
    assert w.timeout < EDGE_TIMEOUT_SEC == 100
