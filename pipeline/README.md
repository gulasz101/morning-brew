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
  roundup project links, render, gate, git push, live check, `report.json`. Every item is
  recorded: a crashing stage or a bad reply lands in `report.json.items` as `dropped`
  with the error, never in the void.
- `lib/` — `model.py` (writer client), `item.py` (validator, lint, template),
  `links.py` (article text + numbered candidate links), `publish.py` (assembly, git, live),
  `config.py`.
- `plumbing/` — ported from the Hermes skill: `kk.py` (Karakeep fetch + transcription),
  `enrich.py`, `roundup_links.py`, `validate_links.py`, `tags.py`, `extract_repos.py`.
- `prompts/` — `voice-card.md`, `digest-rules.md`, `projects.md`, `banned.txt`.
- `gate.py` — the ported deliverable gate with a size guard on the Hermes skill.
- `report.json` — written into the run dir and updated as items finish.

## The 100 s edge (do not raise the timeout, pick a model that fits)

`llm.voitech.dev` is a LiteLLM proxy published through a dedicated Cloudflare Tunnel.
Cloudflare allows the origin 100 s and then answers **HTTP 524**. That limit is at the
edge: a client timeout above it never fires, the run just sits there and gets a 524 for
its trouble. Measured 2026-10-28 with the pipeline's own prompts, one long conference
transcript:

| model | input | `max_tokens` | result | wall | completion tokens |
|---|---|---|---|---|---|
| `qwen3.8-flash-go` | 26000 chars | 2000 | HTTP 524 | 125 s | - |
| `qwen3.8-flash-go` | 8000 chars | 1200 | HTTP 524 | 125 s | - |
| `qwen3.8-flash-go` | 2000 chars | 600 | 200 | 111 s | 7091 (6775 reasoning) |
| `deepseek-v4.1-flash-ollama` | 26000 chars | 2000 | 200 | 11 s | 1265 |

Two facts fall out of that table:

- `max_tokens` is not a wall-clock ceiling. `qwen3.8-flash-go` answered a 600-token cap
  with 7091 completion tokens, because the provider bills reasoning outside the cap. A
  shorter transcript does not help either: 8k chars still timed out.
- The model is the variable, not the window. `deepseek-v4.1-flash-ollama` writes the
  full 26k-char item in 11 s.

So the pipeline does three things:

1. `[writer] timeout_sec = 95` — five seconds under the edge. A slow call becomes a
   retryable `ModelError` recorded in the item's `dropped` row with the budget named,
   instead of a 125 s hang that ends in a 524 and loses the item.
2. Per-model budget in `[writer.limits."<model>"]`: `max_tokens`, `article_chars`,
   `transcript_chars`. A model without an entry uses `[writer].max_tokens` and `[limits]`.
   Reasoning models get a shorter window and more answer room (`beam-free-go`:
   14000/10000/4000).
3. A model rule: **a writer model must answer one 26k-char item inside 95 s.** Check it
   before switching, with `uv run pipeline/brew.py --date <a long day> --limit 3 --dry-run`.
   `qwen3.8-flash-go` fails that check and is not a writer.

If a job ever genuinely needs more than 100 s, it needs a route that is not the edge.
LiteLLM is `ClusterIP` in `llm-hub` and published only through the tunnel, so that means
a LAN NodePort plus an ADR in `homelab-2nd`. Do not improvise it in this repo.

