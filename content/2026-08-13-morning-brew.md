---
date: 2026-08-13
slug: 2026-08-13-morning-brew
tags: digest,karakeep,AI
---
# Morning Brew — 2026-08-13

Hoarded 2 bookmarks on 2026-08-13: both articles. Theme of the day: **AI tooling for humans who actually ship** — a 146k-star repo of drop-in AI agent "personas" for your coding workflow, and Intel's OpenVINO AI effects landing natively in Audacity. One is genuinely useful, the other is a nice-to-have for audio nerds.

---

## 1. agency-agents — a complete AI agency at your fingertips — by github.com

![github.com](https://opengraph.githubassets.com/e445031faa255fb3c5a57b16d590ea096e160df98363c21fd7b8c4b57b962d6f/msitarzewski/agency-agents)
- **Source:** https://github.com/msitarzewski/agency-agents
- **Karakeep doc:** `ybnzhz49gn7bqw2lkuiknssb`

This one's a monster and it earns it. **146k stars, 23.6k forks** — and it actually has substance behind the hype. It's a community-built collection of **230+ specialized AI agent personalities**, each with a real voice, process, and "proven deliverables" rather than the usual generic prompt-template slop. Born from a Reddit thread and months of iteration.

The roster is organized into divisions covering practically everything: engineering, marketing, sales, finance, product, design, strategy, security, testing, project management, paid media, healthcare, GIS, game development, spatial computing, even academic and specialized. So when you need "a reality checker" or a "whimsy injector" mid-project, there's a pre-baked persona for it.

**How you actually use it:** copy the agent files into `~/.claude/agents/` for Claude Code, or (newer) grab the **Agency Agents native app** for macOS/Linux/Windows that browses the whole roster and one-click installs it into Claude Code, Cursor, Codex, Gemini, Osaurus, and more — no clone, no scripts, auto-updates. MIT licensed, so free for commercial use too.

**Verdict:** The star count alone tells you it's not vaporware. If you do any serious agentic coding, this is worth a poke — the "personality-driven specialists" approach beats wrangling one generic agent to do everything.

---

## 2. Audacity AI Plugins (OpenVINO) — by audacityteam.org

![audacityteam.org](/apple-touch-icon.png)
- **Source:** https://www.audacityteam.org/download/openvino/
- **Karakeep doc:** `uwpt4q2bhuquumc9sg395gnj`

Intel's OpenVINO AI plugins are now bundled into Audacity, and it's a surprisingly useful set of on-device effects. Here's what you get:

- **Music separation** — split a mono/stereo track into stems (Drums, Bass, Vocals, Other).
- **Noise suppression** — clean background noise, works best on spoken word.
- **Music generation & continuation** — uses the **MusicGen LLM** to generate snippets or continue an existing one.
- **Whisper transcription** — full audio-to-text via OpenAI's Whisper, exportable as a subtitle file.
- **Audio super resolution** — upsamples the sampling rate; aimed at old 8kHz telephone recordings.

The key angle: **everything runs locally via OpenVINO** — no cloud round-trips, no uploading your audio somewhere. That's a genuinely good privacy feature for audio work.

**Verdict:** The free, local, no-cloud-required angle is the whole story. Stem separation + Whisper transcription + MusicGen on-device for free is a genuinely nice upgrade for anyone doing podcast or audio production on a budget.

---

*Digest generated 2026-08-19 by Hermes nightly karakeep processor (backfilled 2026-08-13).*
