# Morning Brew pipeline

One script, one right answer per step. The writer model fills a fixed JSON form for **one
item per call**; the script validates it, retries once with the error list, lints it and
renders the markdown. No URL ever comes from the model.

```bash
uv run pipeline/brew.py --date 2026-10-27 --dry-run    # build + check into a temp dir
uv run pipeline/brew.py                                # yesterday, Europe/Warsaw
uv run pipeline/brew.py --date 2026-10-27 --resume     # redo only missing/failed items
uv run pipeline/brew.py --model some-other-model
uv run --with pytest pytest pipeline/tests
uv run pipeline/gate.py 2026-10-27 --pre-push
```

## Environment (no key is ever in this repo)

| Variable | What it is | Where to get it |
|---|---|---|
| `BREW_LLM_API_KEY` | key for `https://llm.voitech.dev/v1` (the writer) | Bill's profile `.env` (`~/.hermes/.env`, the default Hermes profile) stores it as `LM_API_KEY`; Hermes' own config wires `llm.voitech.dev` to `${LM_API_KEY}`. Export it as `export BREW_LLM_API_KEY="$LM_API_KEY"` after sourcing that file. |
| `KARAKEEP_API_KEY` | Karakeep API key for the fetch and enrichment stages | same file, `KARAKEEP_API_KEY` |
| `KARAKEEP_SERVER_ADDR` | Karakeep server, e.g. `https://keep.voitech.dev` | same file, or set it by hand |

Nothing else is needed: the ported scripts raise a clear error and exit when a variable
is missing, and they have no literal fallbacks.

## Shape

- `brew.py` — orchestrator: fetch, enrich, writer fan-out (4 in parallel, 1 retry),
  roundup project links, render, gate, git push, live check, `report.json`.
- `lib/` — `model.py` (writer client), `item.py` (validator, lint, template),
  `links.py` (article text + numbered candidate links), `publish.py` (assembly, git, live),
  `config.py`.
- `plumbing/` — ported from the Hermes skill: `kk.py` (Karakeep fetch + transcription),
  `enrich.py`, `roundup_links.py`, `validate_links.py`, `tags.py`, `extract_repos.py`.
- `prompts/` — `voice-card.md`, `digest-rules.md`, `projects.md`, `banned.txt`.
- `gate.py` — the ported deliverable gate with a size guard on the Hermes skill.
- `report.json` — written into the run dir and updated as items finish.

## The writer model, and the 100 s wall in front of it

`[writer].model` in `config.toml` is the only writer switch; `--model` overrides it for one run.
Measurements from the 3-day x 3-model replay (GUL-520, all `--dry-run`) are in the GUL-527 and
GUL-528 threads. Two facts outlive that replay:

- **A reasoning model's empty reply is a drop, not a blank page.** When the model spends its whole
  `max_tokens` on thinking, the provider answers `finish_reason: "length"` with `content: null`.
  `lib/model.py` now raises `ModelError` for that (and for any `finish_reason: "length"` reply), and
  `brew.py` wraps every worker so a crashed item still lands in `report.json` as a `dropped` row.
  Before that, the item vanished from `items` and `dropped` both, and the gate still said PASS.
- **The edge cuts a request at 100 s.** Cloudflare in front of `llm.voitech.dev` answers `HTTP 524`
  at 100 s, long before `Writer`'s own `timeout=240`. The mitigation is the input budget
  (`limits.article_chars` / `limits.transcript_chars`), not a bigger timeout: raising the timeout
  cannot move someone else's edge limit. A model that still 524s a normal day is not a writer
  candidate — that is how `qwen3.8-flash-go` was rejected (13 of 29 items on 2026-10-16, 883 s for
  the day). A 524 now shows up as a `dropped` row carrying `HTTP 524 from the writer model`, so a
  slow model is visible in the report instead of silently shrinking the edition.
