#!/usr/bin/env python3
"""Morning Brew builder: one script, one right answer per step.

  fetch (Karakeep) -> enrich -> one writer call per item -> validate -> lint
  -> render -> gate -> publish -> live check

Usage:
  uv run pipeline/brew.py                          # yesterday, Europe/Warsaw
  uv run pipeline/brew.py --date 2026-10-27
  uv run pipeline/brew.py --date 2026-10-27 --dry-run
  uv run pipeline/brew.py --date 2026-10-27 --resume
  uv run pipeline/brew.py --model deepseek-v4.1-flash-ollama

Every credential comes from the environment (see pipeline/README.md). Nothing in this
file, the config or the repo holds a key.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import os
import subprocess
import sys
import tempfile
import threading
import time
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from lib import item as itemlib  # noqa: E402
from lib import links as linklib  # noqa: E402
from lib import publish  # noqa: E402
from lib.config import ConfigError, expand, load_config, require_env  # noqa: E402
from lib.model import ModelError, Writer, extract_json  # noqa: E402

PROMPTS = HERE / "prompts"
TZ = ZoneInfo("Europe/Warsaw")

SCHEMA = """{
  "in_short": "1-2 sentences: what it is and my verdict",
  "key_points": ["3-6 bullets, hard facts: numbers, versions, prices, licence, who is behind it"],
  "details": "1-3 short paragraphs, 80-200 words (videos up to 300)",
  "ideas": [{"project": "riffradar|homelab-2nd|ideogram4-local", "idea": "one concrete idea"}],
  "project_links": [1, 4]
}"""

PROJECT_LINK_RULE = {
    "riffradar": "riffradar",
    "homelab-2nd": "homelab-2nd",
    "ideogram4-local": "ideogram4-local",
}


def log(msg: str) -> None:
    print(f"[{datetime.now(TZ):%H:%M:%S}] {msg}", flush=True)


def yesterday() -> str:
    return (datetime.now(TZ).date() - timedelta(days=1)).isoformat()


class Reporter:
    """report.json, rewritten after every item so a poller can watch it."""

    def __init__(self, path: Path, meta: dict):
        self.path = path
        self.lock = threading.Lock()
        self.data = dict(meta, started=datetime.now(TZ).isoformat(), items=[], counts={})

    def update(self, **kw) -> None:
        with self.lock:
            self.data.update(kw)
            self._write()

    def add_item(self, row: dict) -> None:
        with self.lock:
            kept = [r for r in self.data["items"] if r.get("id") != row.get("id")]
            self.data["items"] = kept + [row]
            self._write()

    def _write(self) -> None:
        tmp = self.path.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(self.data, indent=2, ensure_ascii=False))
        tmp.replace(self.path)


def read_prompt(name: str) -> str:
    return (PROMPTS / name).read_text().strip()


# ------------------------------------------------------------------ inputs
def ensure_inputs(day: str, cfg: dict, rundir: Path, resume: bool) -> tuple[dict, dict]:
    """Manifest + enrichment. Reuses existing files; runs the ported stages when missing."""
    vault = expand(cfg["paths"]["vault_root"])
    daydir = vault / "karakeep" / day
    manifest_p = daydir / "manifest.json"
    enriched_p = daydir / "enriched.json"
    if not manifest_p.exists() or (resume and not manifest_p.exists()):
        log("fetch: running the ported Karakeep processor")
        env = dict(os.environ)
        out = subprocess.run(
            [sys.executable, str(HERE / "plumbing" / "kk.py"), "--date", day],
            capture_output=True, text=True, env=env,
        )
        log(f"fetch: exit {out.returncode} {(out.stderr or '').strip()[:300]}")
    if not enriched_p.exists():
        log("enrich: running the ported enrichment stage")
        out = subprocess.run(
            [sys.executable, str(HERE / "plumbing" / "enrich.py"), "--date", day],
            capture_output=True, text=True, env=dict(os.environ),
        )
        log(f"enrich: exit {out.returncode} {(out.stderr or '').strip()[:300]}")
    if not manifest_p.exists():
        raise ConfigError(f"no manifest for {day}: {manifest_p} does not exist")
    manifest = json.loads(manifest_p.read_text())
    enriched = json.loads(enriched_p.read_text()) if enriched_p.exists() else {"bookmarks": []}
    return manifest, enriched


def merge_items(manifest: dict, enriched: dict) -> list[dict]:
    """Enrichment wins for display fields; the manifest wins for the item set and order."""
    by_id = {b.get("id"): b for b in enriched.get("bookmarks", [])}
    out = []
    for b in manifest.get("bookmarks", []):
        merged = dict(by_id.get(b["id"], {}))
        merged.update({k: v for k, v in b.items() if v not in (None, "", [])})
        out.append(merged)
    return out


# ------------------------------------------------------------------ writer
def build_prompt(day: str, n: int, total: int, it: dict, text: str, cands: list[dict],
                 projects: str, roundup: bool) -> str:
    label = it.get("channel") or it.get("publisher") or "unknown"
    bits = [
        f"DAY: {day}",
        f"ITEM {n} of {total}",
        f"TITLE: {it.get('real_title') or it.get('title') or ''}",
        f"SOURCE: {label}",
        f"URL: {it.get('url') or ''}",
        f"KARAKEEP ID: {it.get('id') or ''}",
        f"TYPE: {'video' if it.get('video_id') else 'article'}",
        f"ROUNDUP: {'yes' if roundup else 'no'}",
        "",
        "MY PROJECTS (use these to decide the ideas, nothing else):",
        projects,
        "",
        "CANDIDATE LINKS (answer with these numbers only, never a URL):",
        linklib.format_candidates(cands) or "(none)",
        "",
        "SOURCE TEXT:",
        text or "(no text could be fetched: write what the title and the candidate links support, and say plainly that the body was not available)",
        "",
        "Reply with JSON only, exactly this shape:",
        SCHEMA,
    ]
    if roundup:
        bits.append(
            '\nThis is a roundup. Add "projects": ["Name", "Name", ...] with every project '
            "the source text actually names (2 to 14 names). Do not invent names."
        )
    return "\n".join(bits)


def write_item(writer: Writer, system: str, prompt: str, cands: list[dict],
               allowed: list[str], is_video: bool, roundup: bool,
               banned: list[str], max_tokens: int = 2000) -> tuple[dict | None, list[str], int]:
    """One writer call, one retry with the errors attached. Returns (item, errors, tries)."""
    errors: list[str] = []
    reply = ""
    for attempt in range(2):
        ask = prompt if attempt == 0 else (
            prompt
            + "\n\nYour previous answer was rejected. Fix exactly these problems and reply "
              "with the corrected JSON only:\n- " + "\n- ".join(errors)
        )
        reply = writer.call(system, ask, max_tokens=max_tokens)
        try:
            data = extract_json(reply)
        except ModelError as exc:
            errors = [f"the reply was not valid JSON: {exc}"]
            continue
        errors = itemlib.validate(data, len(cands), allowed, is_video, roundup)
        if not errors:
            rendered = itemlib.render_probe(data, allowed)
            lint = itemlib.lint(rendered, banned)
            if lint:
                errors = lint
                continue
            return data, [], attempt + 1
    return None, errors or ["unknown failure"], 2


def resolve_roundup(day: str, n: int, it: dict, names: list[str],
                    rundir: Path) -> list[dict]:
    """Project links for a roundup: resolved and probed by the ported resolver."""
    payload = [{"n": n, "names": names, "source": it.get("url") or ""}]
    inp = rundir / f"roundup_{n}.in.json"
    outp = rundir / f"roundup_{n}.links.json"
    md = rundir / f"roundup_{n}.blocks.md"
    inp.write_text(json.dumps(payload, indent=2))
    cmd = [sys.executable, str(HERE / "plumbing" / "roundup_links.py"), str(inp),
           "--out", str(outp), "--md", str(md)]
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
        log(f"roundup {n}: resolver exit {out.returncode} ({(out.stdout or '').strip()[-160:]})")
    except subprocess.TimeoutExpired:
        log(f"roundup {n}: resolver timed out, shipping without project links")
        return []
    rows: list[dict] = []
    if outp.exists():
        try:
            data = json.loads(outp.read_text())
        except json.JSONDecodeError:
            data = {}
        if isinstance(data, dict):
            data = data.get("roundups") or data.get("items") or []
        for entry in data if isinstance(data, list) else []:
            for row in entry.get("projects", entry.get("links", [])) if isinstance(entry, dict) else []:
                if isinstance(row, dict) and row.get("url"):
                    rows.append({"name": row.get("name") or row.get("project") or "",
                                 "url": row["url"], "what": row.get("what") or row.get("blurb") or ""})
    return rows


# ------------------------------------------------------------------ budget and safety
def model_limits(cfg: dict, model: str) -> dict:
    """The writer budget for this model: input window and answer ceiling.

    `[writer.limits.default]` first, then an optional `[writer.limits."<model>"]`
    override. The window exists because Cloudflare cuts a call at 100 s: a model that
    thinks for a minute before it writes cannot also chew a 26k-character transcript
    (see README, "The 100 s edge").
    """
    writer_cfg = cfg.get("writer") or {}
    limits = writer_cfg.get("limits") or {}
    out = {
        "max_tokens": int(writer_cfg.get("max_tokens", 2000)),
        "article_chars": int(cfg["limits"]["article_chars"]),
        "transcript_chars": int(cfg["limits"]["transcript_chars"]),
    }
    out.update(limits.get("default") or {})
    out.update(limits.get(model) or {})
    return {k: int(v) for k, v in out.items()}


def clip(text: str, limit: int) -> str:
    """Head plus tail: the intro and the conclusion of a long transcript both matter."""
    if limit <= 0 or len(text) <= limit:
        return text
    head = int(limit * 0.7)
    tail = limit - head
    return f"{text[:head]}\n[... middle of the source omitted ...]\n{text[-tail:]}"


def guard_item(it: dict, process, record) -> None:
    """Run one item's writer pass; any exception becomes a visible dropped row.

    A worker that raised used to kill its thread and take its item with it: the item
    landed in neither `report.json.items` nor `report.json.dropped`, so the counts, the
    drop ratio and the intro line all undercounted. Nothing leaves this function
    unrecorded.
    """
    row: dict = {"id": it.get("id"), "title": (it.get("title") or "")[:90]}
    try:
        row.update(process())
    except Exception as exc:  # noqa: BLE001 - one item must never take the run down
        row.update(status="dropped",
                   errors=[f"worker crashed: {type(exc).__name__}: {exc}"])
    try:
        record(row)
    except Exception as exc:  # noqa: BLE001 - the report write itself is the last resort
        log(f"REPORT FAILED for {row.get('id')}: {type(exc).__name__}: {exc}")


# ------------------------------------------------------------------ main
def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Morning Brew builder")
    ap.add_argument("--date", default=None, help="YYYY-MM-DD (default: yesterday, Europe/Warsaw)")
    ap.add_argument("--resume", action="store_true", help="only redo missing or failed items")
    ap.add_argument("--dry-run", action="store_true",
                    help="build and check into a temp dir: no vault write, no commit, no push")
    ap.add_argument("--model", default=None, help="override the writer model from config.toml")
    ap.add_argument("--limit", type=int, default=0, help="only the first N items (smoke tests)")
    args = ap.parse_args(argv)

    started = time.time()
    cfg = load_config()
    day = args.date or yesterday()
    try:
        datetime.strptime(day, "%Y-%m-%d")
    except ValueError:
        log(f"--date must be YYYY-MM-DD, got {day!r}")
        return 2

    try:
        api_key = require_env(cfg["writer"]["api_key_env"],
                              "It is the key for llm.voitech.dev.")
        kk_key = require_env(cfg["karakeep"]["api_key_env"],
                             "It is the Karakeep API key the fetch stage needs.")
        kk_server = require_env(cfg["karakeep"]["server_env"],
                                "It is the Karakeep server address, https://keep.voitech.dev.")
    except ConfigError as exc:
        log(f"config: {exc}")
        return 2

    vault = expand(cfg["paths"]["vault_root"])
    blog = expand(cfg["paths"]["blog_repo"])
    rundir = Path(tempfile.mkdtemp(prefix=f"brew-{day}-")) if args.dry_run else (
        Path(os.environ.get("TMPDIR", "/tmp")) / f"brew-{day}")
    rundir.mkdir(parents=True, exist_ok=True)
    model = args.model or cfg["writer"]["model"]

    reporter = Reporter(rundir / "report.json", {
        "date": day, "model": model, "dry_run": args.dry_run, "run_dir": str(rundir),
    })

    log(f"Morning Brew {day}: model {model}, run dir {rundir}")
    manifest, enriched = ensure_inputs(day, cfg, rundir, args.resume)
    items = merge_items(manifest, enriched)
    if args.limit:
        items = items[: args.limit]
    total = len(items)
    log(f"{total} items to write")

    system = "\n\n".join([read_prompt("voice-card.md"), read_prompt("digest-rules.md")])
    projects = read_prompt("projects.md")
    banned = itemlib.load_banned()
    allowed = list(cfg["projects"]["allowed"])
    limits = model_limits(cfg, model)
    writer = Writer(model, cfg["writer"]["base_url"], api_key,
                    timeout=int(cfg["writer"].get("timeout_sec", 0)) or None)

    a_chars = limits["article_chars"]
    t_chars = limits["transcript_chars"]
    done: dict[int, dict] = {}
    dropped: list[dict] = []
    n_ok = n_retried = 0
    lock = threading.Lock()

    def record(row: dict) -> None:
        nonlocal n_ok, n_retried
        with lock:
            if row.get("status") == "dropped":
                dropped.append(row)
            elif int(row.get("tries", 1)) > 1:
                n_retried += 1
            else:
                n_ok += 1
            reporter.add_item(row)
        if row.get("status") == "dropped":
            log(f"DROP {row.get('title')}: {'; '.join(row.get('errors') or [])[:200]}")

    def work(idx: int, it: dict) -> None:
        def process() -> dict:
            is_video = bool(it.get("video_id"))
            roundup = linklib.is_roundup_title(it.get("real_title") or it.get("title") or "")
            text = linklib.transcript_text(it, vault) if is_video else ""
            src = "transcript"
            if not text:
                text, src = linklib.article_text(it, cfg, kk_key, kk_server)
            text = clip(text, t_chars if is_video else a_chars)
            cands = linklib.candidates(it, text)
            prompt = build_prompt(day, idx + 1, total, it, text, cands, projects, roundup)
            row = {"id": it.get("id"), "title": (it.get("title") or "")[:90],
                   "text_source": src, "candidates": len(cands)}
            try:
                data, errors, tries = write_item(writer, system, prompt, cands, allowed,
                                                 is_video, roundup, banned,
                                                 limits["max_tokens"])
            except ModelError as exc:
                data, errors, tries = None, [str(exc)], 1
            if data is None:
                row.update(status="dropped", errors=errors)
                return row
            row.update(status="retried" if tries > 1 else "ok", errors=[], tries=tries)
            done[idx] = {"item": data, "meta": it, "links": cands, "roundup": roundup}
            return row

        guard_item(it, process, record)

    workers = max(1, int(cfg["writer"]["parallel"]))
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(work, i, it) for i, it in enumerate(items)]
        for f in concurrent.futures.as_completed(futures):
            exc = f.exception()
            if exc:  # guard_item swallows the item-level ones; this is the last line
                log(f"worker crashed outside guard_item: {exc}")

    if not done:
        log("nothing came back from the writer, stopping")
        reporter.update(finished=datetime.now(TZ).isoformat(), counts={
            "ok": 0, "retried": 0, "dropped": len(dropped)})
        return 1

    # Roundup project links: resolved by the script, never by the model.
    for idx in sorted(done):
        entry = done[idx]
        if not entry["roundup"]:
            continue
        names = entry["item"].get("projects") or []
        entry["resolved"] = resolve_roundup(day, idx + 1, entry["meta"], names, rundir)

    groups: dict[str, list[str]] = {"Hand-bookmarked": [], "RSS": []}
    number = 0
    for idx in sorted(done):
        entry = done[idx]
        number += 1
        meta = {
            "title": entry["meta"].get("real_title") or entry["meta"].get("title") or "Untitled",
            "source": entry["meta"].get("channel") or entry["meta"].get("publisher") or "unknown",
            "url": entry["meta"].get("url") or "",
            "id": entry["meta"].get("id") or "",
            "image": entry["meta"].get("imageUrl") or entry["meta"].get("thumbnail") or "",
        }
        block = itemlib.render(number, entry["item"], meta, entry["links"],
                               entry.get("resolved"))
        src = (entry["meta"].get("source") or "").lower()
        key = "Hand-bookmarked" if src in ("hoard", "manual", "web") else "RSS"
        groups[key].append(block)

    body_parts: list[str] = []
    body = ""
    for name, blocks in groups.items():
        if not blocks:
            continue
        body_parts.append(f"### {name}\n")
        body_parts.extend(blocks)
    body = "\n".join(body_parts)
    if not body.strip():
        log("no items rendered, nothing to publish")
        return 1

    tags = []
    raw_tags = [t for it in items for t in (it.get("tags") or [])]
    for t in raw_tags:
        if t not in tags:
            tags.append(t)
    tags = tags[:14]

    intro_items = len(done)
    intro = (
        f"Morning Brew for {day}: {intro_items} items written from {total} hoarded bookmarks "
        f"and feeds, {len(dropped)} dropped after a failed retry."
    )
    post = publish.build_post(day, intro, body, tags)
    vnote = publish.build_vault_note(day, intro, body)

    if args.dry_run:
        out_post = rundir / f"{day}-morning-brew.md"
        out_note = rundir / f"{day}.md"
    else:
        out_post = blog / "content" / f"{day}-morning-brew.md"
        out_note = vault / "karakeep" / day / f"{day}.md"
    publish.write(out_post, post)
    publish.write(out_note, vnote)
    log(f"wrote {out_post}")

    gate_cmd = [sys.executable, str(HERE / "gate.py"), day,
                "--post", str(out_post), "--note", str(out_note)]
    gate_cmd.append("--dry-run" if args.dry_run else "--pre-push")
    gate = subprocess.run(gate_cmd, capture_output=True, text=True,
                          env={**os.environ, "MB_VAULT_ROOT": str(vault),
                               "MB_BLOG_REPO": str(blog)})
    log(gate.stdout.strip() or gate.stderr.strip()[:400])

    pushed, push_detail = publish.git_publish(
        blog, f"content/{day}-morning-brew.md",
        f"Morning Brew {day}: {intro_items} items, {len(dropped)} dropped", args.dry_run)
    live_url = f"{cfg['live']['base'].rstrip('/')}/{day}-morning-brew.html"
    live = None
    if pushed and not args.dry_run:
        ok, detail = publish.live_check(live_url)
        live = detail
        log(f"live check: {detail}")

    wall = round(time.time() - started, 1)
    counts = {"ok": n_ok, "retried": n_retried, "dropped": len(dropped), "items": intro_items}
    reporter.update(finished=datetime.now(TZ).isoformat(), wall_sec=wall, counts=counts,
                    dropped=dropped, post=str(out_post), live_url=live_url, live=live,
                    pushed=pushed, push_detail=push_detail)

    ratio = len(dropped) / max(1, total)
    ok = gate.returncode == 0 and pushed and ratio <= float(cfg["limits"]["max_drop_ratio"])
    log(f"done in {wall}s: {counts} gate={'pass' if gate.returncode == 0 else 'fail'} "
        f"dropped={ratio:.1%}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
