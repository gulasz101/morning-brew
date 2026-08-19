---
date: 2026-08-11
slug: 2026-08-11-morning-brew
tags: digest,karakeep,Web Scraping
---

# Morning Brew — 2026-08-11
Backfill of 4 bookmarks from my hoard: a scraper library pitching itself as the free AI replacement, an offline Whisper transcription app, and two videos now transcribed (a bankrupt-price Lucid and a Tame Impala cheat code).

## 1. Scrapling — "AI is too expensive for scraping, use my regex instead"

Scrapling (by D4Vinci) is a Python scraping library selling itself as the budget answer to the AI-scraping trend. The pitch: companies lean on AI/LLMs to scrape because sites break static selectors, throw anti-bot walls, and generic scraping of unknown sites is a nightmare — but feeding whole page DOMs into an LLM to pull fields is a token furnace that burns cash by the hour. So Scrapling promises you skip the AI and stay cheap. The toolkit: an `adaptive` selector that stores every unique property of an element and re-finds it by similarity score when the site's DOM shifts (no more dying on a stale XPath); three non-selector selection methods (`find_by_text`, regex matching, similar-element + filter-based) for the junk sites with random/no class names; and two fetchers — `DynamicFetcher` (stealth browser automation) and `StealthyFetcher`, the hardmode browser that claims to auto-bypass Cloudflare Turnstile/interstitial walls. For broad scraping it leans on regex pattern-matching (docs walk through `find_by_regex(r'£[\d\.,]+')` for price extraction); pagination is still DIY, a built-in paginator is "coming." Cost table is the kicker: free/low-cost vs Browse AI from $19/mo and Oxylabs from $49/mo — though the no-code AI tools win on setup ease for non-technical folks. Verdict: a solid argument that most scraping headaches don't need an LLM — just boring pattern-matching and a browser that doesn't trip the wall.

- 🔗 https://scrapling.readthedocs.io/en/latest/tutorials/replacing_ai.html
- karakeep id: `qd20crwa3yen0a7o87qv111h`

## 2. Buzz — Whisper transcription that runs offline on your laptop

Buzz (chidiwilliams/buzz, ~21k stars, MIT) is a GUI desktop app that transcribes and translates audio fully offline on your personal computer, powered by OpenAI's Whisper. No cloud, no API keys, your audio never leaves the box. Import audio/video files, live microphone recording with transcription, and subtitle/transcript export. Includes speaker diarization (whisper-diarization) and forced alignment (ctc-forced-aligner) for word-level timing, plus multilingual punctuation restoration. Ships as Windows/macOS/Linux desktop builds (Flatpak/Snap/AppImage) and a PyPI package (`pip install buzz-captions`, Python 3.12, ffmpeg required) with CUDA/GPU support via matching torch builds. It's the standard recommendation for "local Whisper without fighting the command line" — a real GUI, drag-drop files, pick a model, hit go. Python-heavy and GPU setup is a small ordeal, but for anyone who wants speech-to-text without renting an API or trusting Google, it does the job quietly and privately.

- 🔗 https://github.com/chidiwilliams/buzz
- karakeep id: `ti354v9mkpd9dhfozmprzguu`

## 🎬 Video 3. I Bought a $140,000 Lucid for $4,100 Because Everyone Thought Lucid Was Going Bankrupt

🔗 https://www.youtube.com/watch?v=0YVws9s7IGA

Hell of a lead-in: a $140,000 Lucid Air for four grand, because a bankruptcy rumor plus a struggling stock sent the used EV market into a feeding frenzy. A 2024 Lucid Air, run and drive, 6,000 miles, sold at auction for eight thousand dollars — a six-figure luxury EV trading for Nissan Altima money. So he buys a dead one for $4,100, and the real pain begins: a five-thousand-pound paperweight with all four wheels locked, a screen that boots once and dies, and a battery that refuses to charge. What follows is a weekend of dragging it off the transporter with Crisco-greased pizza trays, baby oil, and a winch rope one ounce from becoming a whip. Lucid hid the tow hook so well he has to crawl through the dead car to reach it. On inspection: clamshell hood, every panel damaged, all four wheels curbed, rear bumper in a body bag, literal blood on the steering wheel — yet the airbags didn't blow, the highest honor a dead car can earn. Underneath, the battery pack is clean — no forklift punctures, just a coolant leak and a popped ball joint. Verdict: worth a shot, if he can unlock the wheels and get the software to boot. Spoiler: that is exactly what a man says before a year of pain. Caps off with him clowning around an Xpeng launch in Germany.

- karakeep id: `hk72kwwarv23s2dvxryzee8u`

## 🎬 Video 4. Tame Impala Made a Music Cheat Code

🔗 https://www.youtube.com/watch?v=epAECLliJLA

Kevin Parker of Tame Impala and friends at Telepathic Instruments built the ORK — an "ideas machine" for musicians — and the product design team (Tom and Joseph, who know music production) unbox and road-test it. Transparent, nice notebook, designed as "a space to help you get your ideas out of your head and into the world." Price stings at ~£600. They jam: dual LED bass sequences, an LED-matrix display that squishes text instead of scrolling, and an overdub button that gets the kick hard. But it's opinionated to a fault — one dial nukes all your parameters and drags you into a different vibe, and the sounds are bright and brash rather than nuanced. Still, respect: it's genuinely new in a homogenized world, the way we make opinionated tools for a few people who love them hard. And the killer last note is about AI: an LLM writing you a "top ten pop song" chord sequence would be awful, and even if it weren't, the creative process is precious and fragile — they want real tools to facilitate it, not a chatbot in the loop. An expensive little cheat code for ideas, and thank God someone made something new instead of a fifteenth reissue of the same synth.

- karakeep id: `krzhrep5o60l89gjmkg8zl0i`

---

*Morning Brew digest — 2026-08-11. Tags: web scraping, AI, Whisper, transcription, EVs, music.*
