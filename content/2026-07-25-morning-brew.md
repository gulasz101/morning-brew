---
date: 2026-07-25
slug: 2026-07-25-morning-brew
tags: digest,karakeep,open-source,osint,ai
---
# Morning Brew — 2026-07-25

One bookmark on 2026-07-25: a lone, caffeine-addled dev "vibe coded" a free open-source Palantir clone into existence. It's the whole day, and honestly the only bookmark worth a damn. Theme: **a three-AM Google AI Ultra-fueled 3D-globe OSINT playground in your browser.**

---

## 🎬 Video — I Built an Open-Source Palantir Clone | WorldWideView Devlog
- **Source:** https://youtu.be/p1iu62t8Ay4
- **Karakeep doc:** `dcehfymku0crtzaa2ggg3wqu`

A lone dev running on "three AM coffee" and a $230 Google AI Ultra subscription (his bank, per him, "looking at me like an abused child") built a free, browser-based knockoff of the control-room dashboards that cost governments billions and companies like Palantir six figures *just for a demo*. **WorldWideView** (`worldwideview.dev`, open source) is a live 3D globe in your browser pulling from maritime, military-jet, live-satellite and street-layer data sources — and he swears it runs at 60fps even on a phone.

**What it actually does:**
- **3D globe on Google's 3D Tiles** (same tiles as Google Earth) — real overhangs and light poles on buildings, not flat 2D-map slop. That's the killer feature: you can line a photo up against the scene for OSINT geo-location, a la Bellingcat.
- **Chrome-extension-style plugin system for geo-data.** 30+ in the marketplace already. Want the nearest cat to pet? Ask "Jarvis" to generate a plugin and... there's a plugin for that.
- **Live satellite tracking** — zoom out, disable noise layers, watch objects in orbit; click one and it shows the orbit path plus a cone of what it's currently looking at (he found a discarded ISS camera module drifting in LEO eyeing the Strait of Hormuz).
- **Military aircraft via ADSB** — 69 live at filming (nice); crowdsourced, no-filtering, so the transports/tankers/surveillance/fighters that disappear from mainstream trackers all show up.
- **OSM geolocation demo** — a "fictional" buddy owes lunch money, flees to Belgium, posts an Instagram selfie, and the tool triangulates tram line + fountain + convenience store within 100m to nail the exact photo spot.

**Caveats he'd rather you skim:** the OpenSky plane demo was scrapped because OpenSky was down during filming. The AI layer (surge tracking before news breaks, "Iron Man Jarvis" narrative briefings, MCP integration so agents do the finding) is roadmap, not shipped. It's a one-man operation begging for contributors because the workload is crushing him.

**Origin, told honestly:** he saw the video of a weekend-vibe-coded Palantir clone that Palantir's own CEO commented on, and with "no Claude subscription, no software development experience," decided to just build one. Worked, apparently.

**Verdict:** Audacious, sleek, and legitimately impressive for a solo weekend-origin project — the 3D-tile geolocation and the ADSB/satellite layers are the real deal, and free beats a six-figure demo. The "AI does the work for you" roadmap is currently vaporware, and "vibe coded" shows in the framerate hand-wave. Worth a poke at worldwideview.dev if you've ever wanted the big red spy screen; just don't hand over your demo money yet.
