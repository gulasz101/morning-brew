"""GUL-1468: empty transcripts must be retried, and a miss must say why.

The resume gate used to test `txf.stat().st_size > 0`. A failed transcription
still writes the header, so the file was never zero bytes and the video was
never retried. These tests pin the body-based rule and the chunking that stops
long audio from dying in parakeet-cli's Metal allocation.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

os.environ.setdefault("KARAKEEP_API_KEY", "test-key")
os.environ.setdefault("KARAKEEP_SERVER_ADDR", "http://127.0.0.1:9")

PLUMBING = Path(__file__).resolve().parent.parent / "plumbing"
if str(PLUMBING) not in sys.path:
    sys.path.insert(0, str(PLUMBING))

import kk  # noqa: E402

BID = "q1lv4mzawywkttk96s3q57jl"
URL = "https://www.youtube.com/watch?v=4BnLL7tUGmI"


def bookmark():
    return {
        "id": BID,
        "createdAt": "2026-11-12T07:00:00.000Z",
        "content": {"type": "link", "url": URL, "title": "Don't buy Anthropic stock"},
        "tags": [],
    }


def transcript_file(txdir: Path, body: str) -> Path:
    tx = txdir / f"{kk.slug_for(BID)}.md"
    tx.write_text(
        f"# Don't buy Anthropic stock\n\n- Source: {URL}\n- Karakeep doc: `{BID}`\n"
        f"- Transcribed: 2026-11-12 (Parakeet)\n\n---\n\n## Raw transcript\n\n{body}\n"
    )
    return tx


def stub_transcribe(monkeypatch, text: str, reason: str = ""):
    calls = {"download": 0, "transcribe": 0, "chunks": []}

    def fake_download(url, out_base):
        calls["download"] += 1
        return f"{out_base}.wav"

    def fake_transcribe(wav, out_json):
        calls["transcribe"] += 1
        return text, reason

    monkeypatch.setattr(kk, "download_audio", fake_download)
    monkeypatch.setattr(kk, "transcribe", fake_transcribe)
    return calls


def test_empty_body_is_retried(tmp_path, monkeypatch):
    tx = transcript_file(tmp_path, "")
    assert tx.stat().st_size > 0, "the old size test is exactly what broke resume"

    calls = stub_transcribe(monkeypatch, "everyone is telling you that AI")
    entry, resumed = kk.build_entry(bookmark(), "2026-11-12", tmp_path)

    assert calls["transcribe"] == 1, "an empty body must be re-transcribed"
    assert resumed is False
    assert kk.transcript_body(tx) == "everyone is telling you that AI"
    assert "empty_transcript" not in entry


def test_real_body_is_reused(tmp_path, monkeypatch):
    tx = transcript_file(tmp_path, "already transcribed words")
    calls = stub_transcribe(monkeypatch, "should never be used")

    entry, resumed = kk.build_entry(bookmark(), "2026-11-12", tmp_path)

    assert resumed is True
    assert calls["download"] == 0 and calls["transcribe"] == 0
    assert kk.transcript_body(tx) == "already transcribed words"
    assert entry["resumed"] is True


def test_failed_attempt_records_reason(tmp_path, monkeypatch):
    stub_transcribe(
        monkeypatch,
        "",
        "chunk 2/2 empty: ggml_metal_synchronize: command buffer 0 failed with status 5",
    )

    entry, resumed = kk.build_entry(bookmark(), "2026-11-12", tmp_path)

    assert entry["empty_transcript"] is True
    assert "Insufficient" in entry["empty_reason"] or "command buffer" in entry["empty_reason"]
    assert resumed is False


def test_split_wav_returns_original_when_short(tmp_path, monkeypatch):
    wav = tmp_path / "short.wav"
    wav.write_bytes(b"RIFF")
    monkeypatch.setattr(kk, "wav_duration", lambda p: 120.0)

    assert kk.split_wav(str(wav)) == [str(wav)]


def test_split_wav_chunks_long_audio(tmp_path, monkeypatch):
    """The 570 s file that used to fail now goes through two 300 s chunks."""
    wav = tmp_path / "long.wav"
    wav.write_bytes(b"RIFF")
    monkeypatch.setattr(kk, "wav_duration", lambda p: 570.0)

    class R:
        returncode = 0
        stdout = ""
        stderr = ""

    def fake_sh(cmd, **kw):
        Path(cmd[-1]).write_bytes(b"RIFF")
        return R()

    monkeypatch.setattr(kk, "sh", fake_sh)
    parts = kk.split_wav(str(wav))

    assert parts == [
        str(tmp_path / "long.part00.wav"),
        str(tmp_path / "long.part01.wav"),
    ]


def native_mode(monkeypatch, tmp_path, volumes, texts):
    """Force the native branch: no docker, parts = one per entry in [volumes]."""
    model = tmp_path / "model.bin"
    model.write_bytes(b"x")
    monkeypatch.setattr(kk, "NATIVE_MODEL", model)
    monkeypatch.setattr(kk.shutil, "which", lambda name: None if name == "docker" else "/usr/bin/" + name)
    monkeypatch.setattr(kk, "split_wav", lambda w: [f"{w}.part{i:02d}" for i in range(len(volumes))])
    calls = {"transcribe": 0}

    def fake_volumes(part):
        return volumes[int(part.split(".part")[1])]

    def fake_native(part, base):
        calls["transcribe"] += 1
        return texts[int(part.split(".part")[1])], "parakeet_print_timings: compute = 3.20 ms"

    monkeypatch.setattr(kk, "wav_mean_volume", fake_volumes)
    monkeypatch.setattr(kk, "_native_transcribe", fake_native)
    return calls


def test_silent_chunk_is_skipped_not_retried(tmp_path, monkeypatch):
    """Dead air at the start of a livestream must not burn two GPU passes."""
    calls = native_mode(monkeypatch, tmp_path, volumes=[-91.0, -24.0], texts=["", "spoken words"])

    text, reason = kk.transcribe(str(tmp_path / "a.wav"), str(tmp_path / "a.json"))

    assert text == "spoken words"
    assert reason == ""
    assert calls["transcribe"] == 1, "only the audible chunk may reach parakeet-cli"


def test_all_silent_says_why_instead_of_failing(tmp_path, monkeypatch):
    native_mode(monkeypatch, tmp_path, volumes=[-91.0, -90.0], texts=["", ""])

    text, reason = kk.transcribe(str(tmp_path / "b.wav"), str(tmp_path / "b.json"))

    assert text == ""
    assert "silent audio" in reason
    assert "dB" in reason
