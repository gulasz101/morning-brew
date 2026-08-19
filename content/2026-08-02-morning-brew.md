---
date: 2026-08-02
slug: 2026-08-02-morning-brew
tags: digest,karakeep,Photography,Film Simulation,Developer Tools,AI Agents
---
# Morning Brew — 2026-08-02

Hoarded 2 bookmarks on 2026-08-02, both links (no videos). Theme of the day: **free stuff for your photo toolchain and a pitch that your AI agents should be git-native.** One is a messy-but-valuable dump of film-simulation presets for RawTherapee/Darktable; the other is a startup trying to turn every agent session into a commit checkpoint.

---

## 1. The Largest Collection of Presets/Profiles brought together
- **Source:** https://marcrphoto.wordpress.com/the-largest-collection-of-film-simulation-presets-profiles-brought-together/
- **Karakeep doc:** `w451ri5jmv03cq466alnq8hd`

A perpetual work-in-progress index page (last updated May 2025) aggregating open-source film-simulation presets for **RawTherapee** and **Darktable** — the "just want my photos to look like a Fuji without owning a Fuji" corner of the photography world.

RawTherapee side, you get `.pp3` profiles you drop into your `Profiles` folder and pick from a dropdown:
- **pixls.us / RawTherapee-Presets** (Sébastien Guyader + Pat David, CC0-1.0): Acros (Ilford-ish mono), Classic Chrome, and Fuji sims (Portra/Provia/Velvia) with tone-curve files.
- **GLTR87's Fuji-inspired presets**: Velvia punch, Pro400H pastels, Classic Chrome muted, plus Astia/Soft and Eterna flat/low-contrast — all non-destructive `.pp3` files.
- **Stefan Chirila's customCHROME**: six packs — Basics for JPEG, The Classics, Tribute400H (a Fuji 400H homage), his personal portrait/wedding favorites, Carpathica (from a 2016 Romania trip), and a Holiday pack that tames mixed indoor lighting.

Darktable side:
- **Mark G. Adams' 14 styles** for the modern "Scene Referred" workflow — autumnal tones, crimson boost, plus lens-correction/horizon/exposure guidance.
- **João Pedro Almeida's t3mujinpack** (Portra presets available on his blog).
- **Fuji LUTs converted to DT Styles** (Gauche & Costanza) — all 15 official Fuji sims from the X-Trans III sensor days, ZIP download.
- **Stefano Ferro's MEL365** guide + free style pack.

**Caveats:** This is an *index*, not a curated set — links rot, and the author openly notes **DTStyle.net crashed and the owner had no backup, so that whole dataset is gone forever** (and won't be rebuilt). It's a WIP; some entries are thin. Also the download tip to use Firefox over Chrome for Chirila's site is a trust-smell — proceed with healthy paranoia.

**Verdict:** Worth a bookmark if you're into film emulation without buying a Fuji. It's a scavenger hunt — a bunch of small indie projects lumped together — not a turnkey solution. Grab the CC0 pixlsus set and t3mujinpack and you'll be fine.

---

## 2. Entire — a new developer platform is coming
- **Source:** https://entire.io/
- **Karakeep doc:** `hcmy1djk93atzoushfollbny`

A dev-tool startup pitching the idea that **coding-agent sessions should live in your git history.** The pitch: every agent session, prompt, tool call, and decision gets stored *with* your commits — a "checkpoint" per commit, so you can answer "why did we write it this way" without the agent starting from zero every time.

Core mechanics:
- An **MIT-licensed CLI** (`entire enable`) that hooks into whatever agent you run — works with Claude Code, Codex, Gemini, Cursor.
- **Checkpoints stored in your repo** ("no hosted service, no external database") — the code change + the full agent session that produced it.
- **Private by design**: claims sensitive data never leaves your machine — it detects and redacts secrets before storing.
- A **Distributed Git Network** / geo-mirroring: keep the repo on GitHub, clone from regional mirrors to avoid rate limits. Branded as "distributed everywhere: SOON".
- Throughput numbers (self-reported): 570K clones/h, 1.7M operations/h, 2.1M pushes/h from simulated workloads.

**Caveats:** It's a landing page — heavy on the "Join the rebellion" marketing and light on verifiable specifics. The throughput benchmarks are their own simulated numbers, not independent tests. "Private by design" while syncing a mirror around the world is a slightly self-cancelling claim you'd want to poke at. And the whole model assumes you actually want your whole agent-session history in the same repo that your CI and your colleagues see.

**Verdict:** Conceptually interesting — "context attached, not archived" is a legitimately good framing for why agents repeat mistakes (they cold-start each session). Whether this becomes a real dev platform or a startup that evaporates is very much TBD. Worth watching, not wiring your repo to yet.

---

*Digest generated 2026-08-02 by Hermes nightly karakeep processor.*
