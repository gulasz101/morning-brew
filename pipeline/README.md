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
