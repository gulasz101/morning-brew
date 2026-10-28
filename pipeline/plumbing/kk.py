#!/usr/bin/env python3
"""
karakeep_digest.py — nightly hoard processor for Wojtek's karakeep instance.

Downloads YT/IG videos hoarded on a given day, transcribes them with Parakeet
(native parakeet-cli, or the Docker image on hosts that have Docker), and writes raw
transcripts into the Obsidian vault. The cron agent
reads the produced manifest and writes the digest + Mattermost headline ping.

Usage:
    karakeep_digest.py --date 2026-08-16
    karakeep_digest.py                # defaults to yesterday
    karakeep_digest.py --status       # show what is already done for the day

Env:
    KARAKEEP_API_KEY, KARAKEEP_SERVER_ADDR (defaults embedded for this instance)

Output:
    <vault>/karakeep/<date>/transcriptions/<bookmark-id>.md
    <vault>/karakeep/<date>/manifest.json   <- list of bookmarks + transcript paths
    stdout: JSON manifest (for the cron agent to consume)

DATA LAYER (rewritten 2026-09-27 — this was silently losing ~50% of every day):
    The karakeep *CLI* (`bookmarks search ... --all`) is unusable for day queries:
      * it caps results at 20-40 no matter what, and
      * `--all` was a no-op — domain terms, `url:` filters and `after:`/`before:`
        qualifiers produced the SAME 20 rows.
    Measured: 2026-09-27 truly had 80 bookmarks; the CLI returned 40 (52 videos;
    CLI saw 24). 2026-08-20 truly had 50; CLI returned 20.
    Fix: paginate the REST API with its cursor (`limit` max is 100) and filter by
    `createdAt` local date here. A full walk is ~19 requests / ~5s.
    Also append `&archived=false`: archived bookmarks ARE still returned by the
    list endpoint otherwise, so archiving alone looks like it does nothing. That
    flag is what makes archive-based brew-thinning work at all (verified: 1823 ->
    1822 unique, canary excluded; a day's brew drops by construction).

RESUME (added 2026-09-27):
    Re-running is INCREMENTAL: an existing non-empty transcript file for a bookmark
    id is reused, never re-transcribed. The manifest is ALWAYS written — including
    when a video fails — so a killed run never strands the day without an index.

    This exists because a heavy day used to run the processor in the foreground,
    blow the 600s tool timeout (exit 124), then re-transcribe EVERY video from
    scratch on the re-run. Measured 2026-09-27: Parakeet does ~40x realtime
    (36-min video in 54s) and 4 parallel runs gave 0.93x (no speedup — the model
    already saturates the cores), so transcription was never the bottleneck.
    Repeated work was. Hence: resume, not parallelism.
"""

import argparse
import datetime
import json
import os
import re
import shutil
import signal
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, timedelta
from pathlib import Path

VAULT = Path.home() / "wojtek.second.brain.obsidian.vault" / "karakeep"
API_KEY = os.environ.get("KARAKEEP_API_KEY")
if not API_KEY:
    raise SystemExit(
        "KARAKEEP_API_KEY is not set. This script has no built-in key: export the "
        "Karakeep API key first (see pipeline/README.md)."
    )
SERVER = os.environ.get("KARAKEEP_SERVER_ADDR")
if not SERVER:
    raise SystemExit(
        "KARAKEEP_SERVER_ADDR is not set (for example https://keep.voitech.dev)."
    )
PARAKEET_IMG = "ghcr.io/mudler/parakeet.cpp-cli:latest"
MODEL = "/models/tdt_ctc-110m-q5_k.gguf"
MODEL_DIR = Path.home() / "wojtek.second.brain.obsidian.vault" / "floating_coleslaw" / "models"
# Native Homebrew parakeet-cli (whisper.cpp) cannot load mudler's .gguf files:
# it wants its own converted model. Installed 2026-10-22 (GUL-95), 668 MB.
NATIVE_PARAKEET = "parakeet-cli"
NATIVE_MODEL = MODEL_DIR / "ggml-parakeet-tdt-0.6b-v3-q8_0.bin"

YOUTUBE_HOSTS = ("youtube.com", "youtu.be")
# karakeep REST caps `limit` at 100 (ZodError above that)
PAGE_LIMIT = 100

LOG_PATH = Path("/tmp/kkd_processor.log")


def log(msg):
    line = f"[{time.strftime('%H:%M:%S')}] {msg}"
    print(line, flush=True)
    try:
        with open(LOG_PATH, "a") as fh:
            fh.write(line + "\n")
    except Exception:
        pass


def sh(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)


# ---------------------------------------------------------------- data layer

def _get(path, tries=3):
    last = None
    for attempt in range(tries):
        req = urllib.request.Request(
            SERVER + path,
            headers={"Authorization": f"Bearer {API_KEY}", "User-Agent": "curl/8.0"},
        )
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            last = RuntimeError(f"HTTP {e.code} on {path}: {e.read()[:200]!r}")
            if e.code < 500:
                raise last
        except Exception as e:  # transient network
            last = e
        time.sleep(1.5 * (attempt + 1))
    raise last


def all_bookmarks():
    """Walk every bookmark via the REST cursor. Returns list of bookmark dicts."""
    out, seen, cursor, pages = [], set(), None, 0
    while True:
        path = f"/api/v1/bookmarks?limit={PAGE_LIMIT}&archived=false"
        if cursor:
            path += "&cursor=" + urllib.parse.quote(cursor)
        d = _get(path)
        bms = d.get("bookmarks", [])
        for b in bms:
            if b["id"] not in seen:
                seen.add(b["id"])
                out.append(b)
        cursor = d.get("nextCursor")
        pages += 1
        if not cursor or pages > 80:
            break
    return out


def created_day(b):
    """Local calendar date the bookmark was created (the 'hoard day')."""
    ts = b.get("createdAt") or ""
    try:
        return datetime.datetime.fromisoformat(ts.replace("Z", "+00:00")).astimezone().date().isoformat()
    except Exception:
        return None


def bookmarks_for_day(target):
    """All bookmarks whose createdAt falls on `target` (local). Not a 20-row lie."""
    return [b for b in all_bookmarks() if created_day(b) == target]


def is_video(url):
    return any(h in url for h in YOUTUBE_HOSTS) or "instagram.com" in url


def slug_for(bid):
    """Stable transcript filename for a bookmark id."""
    return bid.replace(":", "").replace("/", "_")[:24]


def yt_id(url):
    m = re.search(r"[?&]v=([\w-]{11})", url or "") or re.search(r"youtu\.be/([\w-]{11})", url or "")
    return m.group(1) if m else None


# ---------------------------------------------------------------- media

def fetch_meta(url):
    """Title + author + duration when the karakeep record is thin. Best effort."""
    try:
        r = sh(["yt-dlp", "--skip-download", "--no-warnings",
                "--extractor-args", "youtube:player_client=web_embedded,android",
                "--print", "%(title)s\t%(uploader)s\t%(duration)s", url], timeout=90)
        parts = r.stdout.strip().splitlines()[-1].split("\t")
        if len(parts) >= 3:
            return {"title": parts[0], "author": parts[1],
                    "duration": int(float(parts[2])) if parts[2] not in ("NA", "") else None}
    except Exception:
        pass
    return {}


def download_audio(url, out_base):
    """yt-dlp best audio -> temp media, then ffmpeg -> <out_base>.wav (16k mono).

    yt-dlp intermittently fails with a bot-check / 403 hiccup (seen live on
    2026-09-27 for a video whose metadata fetched seconds later), so retry with
    backoff. A video that still fails is recorded with an `error` and NO
    transcript file, which means a later re-run will retry it (resume only skips
    videos that already have a transcript) — so a transient miss self-heals.
    """
    # YouTube's default `web` player client 403s on media fetch (2026-08).
    # Force web_embedded (works) with android as fallback.
    last = ""
    for attempt in range(3):
        r = sh([
            "yt-dlp",
            "--extractor-args", "youtube:player_client=web_embedded,android",
            "-f", "bestaudio/best",
            "-o", f"{out_base}.%(ext)s",
            url,
        ])
        if r.returncode == 0:
            break
        last = r.stderr[-400:]
        if attempt < 2:
            time.sleep(10 * (attempt + 1))
    else:
        raise RuntimeError(f"yt-dlp failed for {url} after 3 attempts: {last}")
    cands = sorted(Path("/tmp").glob(f"{Path(out_base).name}.*"))
    media = None
    for c in cands:
        if c.suffix in (".webm", ".m4a", ".mp4", ".opus"):
            media = c
            break
    if media is None:
        raise RuntimeError(f"no media file produced for {url}")
    wav = f"{out_base}.wav"
    ff = sh(["ffmpeg", "-y", "-loglevel", "error", "-i", str(media), "-ar", "16000", "-ac", "1", wav])
    if ff.returncode != 0 or not os.path.exists(wav):
        raise RuntimeError(f"ffmpeg failed for {media}")
    return wav


def transcribe(wav, out_json):
    """Parakeet transcription -> <out_json> + return text.

    Docker image (mudler) when Docker exists; otherwise the native Homebrew
    parakeet-cli (whisper.cpp) with its own converted model. The Air has no
    Docker since H2-327, and native parakeet-cli cannot read mudler's .gguf.
    """
    wav_abs = os.path.abspath(wav)
    out_abs = os.path.abspath(out_json)
    tmp = os.path.dirname(wav_abs)
    native_txt = None
    if shutil.which("docker"):
        r = sh([
            "docker", "run", "--rm",
            "-v", f"{tmp}:/work",
            "-v", f"{MODEL_DIR}:/models:ro",
            PARAKEET_IMG, "transcribe",
            "--model", MODEL,
            "--input", f"/work/{os.path.basename(wav_abs)}",
            "--output-json", f"/work/{os.path.basename(out_abs)}",
        ])
        text = r.stdout.strip()
    elif shutil.which(NATIVE_PARAKEET) and NATIVE_MODEL.exists():
        native_txt = os.path.splitext(out_abs)[0] + ".txt"
        r = sh([
            NATIVE_PARAKEET,
            "-m", str(NATIVE_MODEL),
            "-f", wav_abs,
            "-otxt", "-of", os.path.splitext(out_abs)[0],
            "-np",
        ])
        if r.returncode != 0:
            raise RuntimeError(
                f"parakeet-cli failed ({r.returncode}): {r.stderr[-300:]}"
            )
        text = r.stdout.strip()
    else:
        raise RuntimeError(
            "no transcriber: docker not found and "
            f"{NATIVE_PARAKEET} + {NATIVE_MODEL.name} unavailable"
        )
    if not text:
        try:
            d = json.load(open(out_abs))
            text = d.get("text", "")
        except Exception:
            text = ""
        if not text and native_txt and os.path.exists(native_txt):
            text = Path(native_txt).read_text().strip()
    if not os.path.exists(out_abs):
        with open(out_abs, "w") as fh:
            json.dump({"text": text}, fh)
    return text


# ---------------------------------------------------------------- work

def build_entry(b, target, txdir):
    """Bookmark -> manifest entry. Returns (entry, resumed_flag)."""
    c = b.get("content") or {}
    ctype = c.get("type")
    url = c.get("url") or ""
    bid = b.get("id")
    title = c.get("title") or b.get("title") or "(untitled)"
    pub = c.get("publisher") or c.get("author") or ctype or "?"
    entry = {
        "id": bid, "title": title, "publisher": pub,
        "url": url, "type": ctype,
        "source": b.get("source"),
        "created": b.get("createdAt"),
        "tags": [t.get("name") if isinstance(t, dict) else str(t) for t in b.get("tags", [])],
        "transcript": None,
    }

    if ctype != "link" or not is_video(url):
        if ctype == "link":
            entry["kind"] = "article"
        return entry, False

    slug = slug_for(bid)
    txf = txdir / f"{slug}.md"

    # --- RESUME: an existing non-empty transcript is reused, never redone ---
    if txf.exists() and txf.stat().st_size > 0:
        entry["transcript"] = str(txf)
        entry["resumed"] = True
        return entry, True

    out_base = f"/tmp/kk_{slug}"
    try:
        wav = download_audio(url, out_base)
        out_json = f"/tmp/kk_{slug}.json"
        text = transcribe(wav, out_json)
        txf.write_text(
            f"# {title}\n\n- Source: {url}\n- Karakeep doc: `{bid}`\n- Transcribed: {target} (Parakeet)\n\n---\n\n## Raw transcript\n\n{text}\n"
        )
        entry["transcript"] = str(txf)
        if not text.strip():
            entry["empty_transcript"] = True
    except Exception as e:
        entry["error"] = str(e)
        # keep the item visible + useful in the digest even though audio failed
        meta = fetch_meta(url)
        if meta.get("title"):
            entry["title"] = meta["title"]
        if meta.get("author"):
            entry["publisher"] = meta["author"]
            entry["author"] = meta["author"]
        if meta.get("duration"):
            entry["duration"] = meta["duration"]
    finally:
        for f in Path("/tmp").glob(f"kk_{slug}.*"):
            try:
                f.unlink()
            except Exception:
                pass
    return entry, False


def show_status(target):
    """Report what is already on disk for the day — cheap, no downloads."""
    bms = bookmarks_for_day(target)
    daydir = VAULT / target
    txdir = daydir / "transcriptions"
    have = {p.stem for p in txdir.glob("*.md")} if txdir.is_dir() else set()
    vids = [b for b in bms
            if (b.get("content") or {}).get("type") == "link"
            and is_video((b.get("content") or {}).get("url") or "")]
    done = [b for b in vids if slug_for(b["id"]) in have]
    todo = [b for b in vids if slug_for(b["id"]) not in have]
    print(json.dumps({
        "date": target,
        "bookmarks_total": len(bms),
        "videos": len(vids),
        "transcripts_on_disk": len(have),
        "videos_done": len(done),
        "videos_pending": len(todo),
        "pending": [{"id": b["id"], "title": (b.get("content") or {}).get("title")} for b in todo],
        "manifest_present": (daydir / "manifest.json").exists(),
    }, indent=2))
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=None, help="YYYY-MM-DD (default: yesterday)")
    ap.add_argument("--status", action="store_true", help="report progress, do no work")
    ap.add_argument("--limit-hours", type=float, default=None,
                    help="stop starting new videos after N hours (safe partial run)")
    args = ap.parse_args()
    target = args.date or (date.today() - timedelta(days=1)).isoformat()

    if args.status:
        return show_status(target)

    bms = bookmarks_for_day(target)
    daydir = VAULT / target
    txdir = daydir / "transcriptions"
    txdir.mkdir(parents=True, exist_ok=True)

    total_videos = sum(
        1 for b in bms
        if (b.get("content") or {}).get("type") == "link"
        and is_video((b.get("content") or {}).get("url") or "")
    )
    log(f"{len(bms)} bookmarks for {target}; {total_videos} are videos")

    manifest = {"date": target, "bookmarks": []}
    n_new = n_resumed = 0
    t_start = time.time()
    deadline = (t_start + args.limit_hours * 3600) if args.limit_hours else None

    def flush_manifest(partial=False):
        """Write the manifest NOW. Called after every bookmark and on SIGTERM/SIGINT
        so a killed or interrupted run still leaves a usable index (the cron
        runner interrupts hard; without this the whole index is lost and the
        digest is stranded)."""
        manifest["stats"] = {
            "transcribed_new": n_new,
            "transcripts_reused": n_resumed,
            "bookmarks": len(manifest["bookmarks"]),
            "videos_with_transcript": sum(1 for e in manifest["bookmarks"] if e.get("transcript")),
            "videos_failed": sum(1 for e in manifest["bookmarks"] if e.get("error")),
            "elapsed_sec": round(time.time() - t_start, 1),
            "partial": partial,
        }
        tmp = daydir / ".manifest.json.tmp"
        tmp.write_text(json.dumps(manifest, indent=2))
        tmp.replace(daydir / "manifest.json")  # atomic swap

    def _on_signal(signum, _frame):
        log(f"signal {signum} — flushing partial manifest and exiting")
        try:
            flush_manifest(partial=True)
        finally:
            sys.exit(128 + signum)

    for _sig in (signal.SIGTERM, signal.SIGINT):
        signal.signal(_sig, _on_signal)

    for b in bms:
        if deadline and time.time() > deadline:
            log("time budget reached — stopping; re-run to resume (nothing is redone)")
            break
        entry, resumed = build_entry(b, target, txdir)
        manifest["bookmarks"].append(entry)
        if entry.get("transcript"):
            if resumed:
                n_resumed += 1
            else:
                n_new += 1
                log(f"transcript {n_new + n_resumed}/{total_videos} "
                    f"{(entry.get('title') or '')[:65]}")
        elif entry.get("error"):
            log(f"FAILED {(entry.get('title') or '')[:60]}: {entry['error'][:90]}")
        flush_manifest()  # incremental: the index tracks progress live

    elapsed = time.time() - t_start
    flush_manifest()
    log(f"manifest written: {json.dumps(manifest['stats'])}")
    print(json.dumps(manifest, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
