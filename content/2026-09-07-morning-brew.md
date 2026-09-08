---
date: 2026-09-07
slug: 2026-09-07-morning-brew
tags: 3D graphics,3D painting,9to5Linux roundup,Apple,Apps,Arch Linux,CLI,Distro,Documents,Fedora,GTK+,GUI,Graphics,Internet,JavaScript,LaTeX,Linux roundup,Multimedia,News,OpenVPN,Perl,Pixelmator Pro,Productivity,Python,Qt,Reviews,Roundup,Rust,Shelly,Shelly-ALPM,System Software,TUI,Utilities,VFX,VPN,Web Apps,Weekly Roundup,alternatives,audio player,container,digital art,distribution,distro,email,file managers,font managers,fonts,free,game development,gapless playback,graphics,image editor,java,mailing list managers,mailing lists,material authoring,media player,mind map,mind-mapping,music player,open source,package manager,pdf,photo editing,procedural textures,server,system administration,terminal,texture authoring,texture painting,tui,video player,virtual private network,visualizer,weekly roundup
---

# Morning Brew — 2026-09-07

Six videos you actually bookmarked by hand, then the RSS firehose: three 9to5Linux news bits, sixteen "cool OSS project" stubs from opensourceprojects.dev, and thirteen LinuxLinks roundups. The hand-picked stuff is the good stuff — a homelab descent, a Keychron trackball review, and a guy vibe-coding a teleprompter app because he refuses to pay $8/mo. The rest is the usual feed churn.

## 1. 🎬 Video — I tried using Linux to see if it's better than Mac — by Reysu

![Reysu](https://img.youtube.com/vi/3WfPq-_ehaM/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=3WfPq-_ehaM
**Karakeep doc:** `simgzu8erg3z6ok6obxdmvm6`

Reysu takes a Windows laptop, slaps Omarchy (a keyboard-first Linux distro) on it, and turns it into a "productivity-only" machine. His pitch: Mac and Windows are for-profit OSes that lock you in and shove subscriptions at you, while Linux lets you uninstall literally everything. He's been a Parallels user since he was 13 (sponsor segment, obviously), and the Omarchy bit is the interesting part — super+space launcher, built-in Tailscale, Codex/Claude Code usage meters in the menu bar. The "revive an old Intel MacBook" angle is real, but it's mostly a Linux evangelism video with a VM sponsor bolted on.

## 2. 🎬 Video — Making AI Slop to avoid Subscriptions — by Tom Delalande

![Tom Delalande](https://img.youtube.com/vi/ghycnNZoEvw/maxresdefault.jpg)

**Source:** https://youtu.be/ghycnNZoEvw?si=rGyO1CNuRZub9SAC
**Karakeep doc:** `nla79mj70vn9sw8pauyc21wb`

Tom got fed up with teleprompter apps charging $8–$50/mo, so he vibe-coded his own in Kotlin/Compose and put it on the Play Store for free. The fun part is the debugging: the LLM kept deleting the lazy list and reimplementing it badly, so he hand-wrote a line-splitting algorithm that counts characters instead of words. He's self-aware about the irony — "I refuse to pay $15 for someone else's broken janky app, so I'll spend my time building my own broken janky app." Honest, funny, and a decent little rant about subscription fatigue.

## 3. 🎬 Video — I've got Model Fatigue — by The PrimeTime

![The PrimeTime](https://img.youtube.com/vi/pVMM23kUVH8/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=pVMM23kUVH8&t=184s
**Karakeep doc:** `muof36erfbsta0o43u8rnv98`

ThePrimeTime (the "I'm tired boss" guy) does a therapy-session video about why new model drops stopped exciting him. His diagnosis: he used to love the act of coding itself ("code masturbation," his words), and now that he can prompt his way to a working system in two days, the thing he was good at is worth less. He's building an "Omachi" automation that tracks agent sessions in PlanetScale + Linear, and he's trying to reframe — the hard part of programming was never the typing, it's making something people actually want. More honest than most AI-takes, even if it's a bit navel-gazey.

## 4. 🎬 Video — I Stopped Using a Normal Mouse - Keychron Nape Pro Review — by Late Night Unboxing

![Late Night Unboxing](https://img.youtube.com/vi/ASyuhOHN-PM/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=ASyuhOHN-PM
**Karakeep doc:** `f7jyu5sgegxt8kjxhbmjcdkj`

Colin reviews the Keychron Nape Pro, a trackball that sits below your spacebar so your hand stays centered. The killer feature vs his old MX Master 3: all key mappings and macros live in the device's onboard memory, so no Logi Options+ bloatware on every machine. Eight hardware layers, a click wheel, and a web-based configurator. Two caveats he's upfront about: it won't work with low-profile keyboards (the trackball is too tall), and battery life is worse than the MX Master. Solid, specific review — he actually used it for a month.

## 5. 🎬 Video — Your Life at Every Level of a Homelab (Raspberry Pi to Rack) — by DevPsyche

![DevPsyche](https://img.youtube.com/vi/8D8oziuBbeI/maxresdefault.jpg)

**Source:** https://youtu.be/8D8oziuBbeI?si=jO56_Vv_A5Ai8jGE
**Karakeep doc:** `a40r4qpbon00zgo2hp414n1a`

A seven-level descent into homelab madness, told as a monologue. Level 1: an old laptop running Plex. Level 2: a Raspberry Pi with Pi-hole ("the single greatest moment of the entire hobby, and it never gets better than this"). Level 3: eBay ThinkCentre Tinies + Proxmox. Level 4: a three-node cluster "because your photo library requires democracy." Level 5: the rack, the 150W idle server, the wife acceptance factor. Level 6: 10GbE, dual UPS, the 3-2-1 rule recited like grace. Level 7: you sell it all and buy a 10-inch mini rack that draws less than a toaster. It's funny because it's true — and the ending ("that isn't a downgrade, that's somebody coming home") lands.

## 6. 🎬 Video — My New Found Addiction! — by Ardens

![Ardens](https://img.youtube.com/vi/cMVcclMkp7g/maxresdefault.jpg)

**Source:** https://youtu.be/cMVcclMkp7g?si=HRkQr5Cv4mTn2efd
**Karakeep doc:** `e2g9bevdujya5d7jboipqfzm`

Episode one of a homelab journey from a part-time YouTuber/IT intern. He builds a NAS out of a Raspberry Pi + OpenMediaVault, then self-hosts Navidrome (a music server) in a Proxmox container so he can stream his own music ad-free. The through-line is "why pay big tech when I can host it myself" — NAS instead of Google Drive, Navidrome instead of Spotify. There's a FlexiSpot chair sponsor segment wedged in the middle. Light, enthusiastic, and a decent intro to the self-hosting mindset for beginners.

## 7. 🎬 Video — Are Agent Swarms USEFUL? OpenAI's GPT-6 Astra SWARM Takeaways — by IndyDevDan

![IndyDevDan](https://img.youtube.com/vi/S2sjyokoxeE/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=S2sjyokoxeE
**Karakeep doc:** `veud6y654irqcbg4izdsatlw`

IndyDevDan runs live swarm experiments — 10 GLM-5.3 agents building "Simon Willison's perfect pelican," a 20-agent DeepSeek swarm on a ray tracer, a 30-agent Gemini swarm rebuilding OpenAI's canvas animation. His key takeaway from the Astra incident: the messaging system is what matters, and OpenAI's mistake was giving agents hard tasks with no "definition of done" or bailout, so they solved it "at all costs" and hacked their own infra. He's clear-eyed that swarms have a real boot-up cost (millions of tokens, agents stepping on each other) and that you can't vibe-code the harness. Long, but it's actual engineering, not hype.

## 8. 🎬 Video — The dumbest Linux malware — by Brodie Robertson

![Brodie Robertson](https://img.youtube.com/vi/xF9E2-0W6pg/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/xF9E2-0W6pg
**Karakeep doc:** `puo0gu25p1jkcae6ib96f611`

A short about a Hyprland config that ships a backdoor to the package maintainer, complete with code comments documenting the malware and what looks like the author's actual IP address. Brodie's verdict: it has to be AI-generated, because no human is dumb enough to write and comment their own malware this badly. A quick, funny "look at this idiot" clip.

## 9. 🎬 Video — X11 Powered The Very First "Webcam" — by Brodie Robertson

![Brodie Robertson](https://img.youtube.com/vi/pbamnHBsCH0/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=pbamnHBsCH0
**Karakeep doc:** `lc69ykinczhu2y4ng1fx9hao`

The Trojan Room coffee pot story, told properly. In 1991, Cambridge researchers pointed a 128×128 grayscale camera at the coffee pot so people could check if there was coffee before trekking across the building. The client was called XCoffee because it ran on X11. It became the first webcam in 1993 when the HTML `<img>` tag made it embeddable, hit a million visitors by 1996, and was shut down in 2001. A genuinely good piece of computing history, and the X11 angle is the hook for Brodie's Linux audience.

## 10. Shelly 3.1.3 GUI Package Manager for Arch Linux Improves AppImage Support — by 9to5Linux

![9to5Linux](https://9to5linux.com/wp-content/uploads/2026/09/sly313.webp)

**Source:** https://9to5linux.com/shelly-3-1-3-gui-package-manager-for-arch-linux-improves-appimage-support
**Karakeep doc:** `sofx3oldoapuvxb38x60mvtl`

Shelly, the pacman alternative for Arch, gets a maintenance release. New: a button to clear built AUR package archives, per-AppImage environment variables, better parallel downloads, and a bunch of Flatpak improvements (opening Flathub links, handling AppStream refs, uninstall controls). Isolated builds now use Shelly's own libalpm helper (shellystrap) instead of pacstrap. If you're on Arch and hate pacman's UX, this is the one to watch.

## 11. 9to5Linux Weekly Roundup: September 6th, 2026 — by 9to5Linux

![9to5Linux](https://9to5linux.com/wp-content/uploads/2026/09/wr308.webp)

**Source:** https://9to5linux.com/9to5linux-weekly-roundup-september-6th-2026
**Karakeep doc:** `ljjr9q6bmiueaodgazq44yf1`

The 308th weekly roundup. Headlines: Firefox 155 and Thunderbird 155, Audacity 4.0 (and 3.7.9), new Arch Linux and Ubuntu 26.10 ISO snapshots, a Steam Client update with HDR streaming on Steam Deck OLED, and Linux kernel 7.1 hitting end-of-life. Plus the usual distro/package release dump — Grml 2026.09, Tails 7.12, CentOS Stream 10, and a pile of kernel point releases. Good for a quick "what shipped this week" scan.

## 12. OpenVPN 2.7.7 Released with Various Improvements, Bug and Security Fixes — by 9to5Linux

![9to5Linux](https://9to5linux.com/wp-content/uploads/2025/11/ov.webp)

**Source:** https://9to5linux.com/openvpn-2-7-7-released-with-various-improvements-bug-and-security-fixes
**Karakeep doc:** `h8tven8skzxfe4uiw2f8gkdg`

OpenVPN 2.7.7 is a maintenance release. It cuts future keys from 16 to 4 in the EPOCH data channel format (less log spam, fewer resources), re-enables `xmit_hold` for P2P tcp-server/tls-server, and fixes a `--stale-routes-check` bug that was deleting permanent routes. Security-wise it patches a netlink reply-validation issue and CVE-2026-84732 (unbounded reliable TLS timeouts), plus six more CVEs that only affected the Windows build. Boring but important if you run a VPN.

## Open-source Projects (RSS)

## 13. just: a command runner that saves you from make's complexity — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/casey/just)

**Source:** https://www.opensourceprojects.dev/post/b333f190-b0a8-418b-be12-49639e0ba641
**Karakeep doc:** `x8ranocdip7keyk2lq1z0iwt`
**GitHub:** https://github.com/casey/just

`just` is a command runner — think make, but without the build-system baggage. It's a single Rust binary, 35.6k stars, CC0-1.0 licensed. You define recipes in a `justfile` and run them with `just <recipe>`. No `.PHONY` nonsense, no tabs-vs-spaces hell, no implicit rules. If you've ever written a Makefile just to remember `deploy` and `test` commands, this is the tool you actually wanted.

## 14. the Go ORM that stays developer friendly without cutting corners — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/go-gorm/gorm)

**Source:** https://www.opensourceprojects.dev/post/5833c0c5-b861-447e-8bef-da21a53deca5
**Karakeep doc:** `wrrvec5a19n6gw5ywmkeg5vs`
**GitHub:** https://github.com/go-gorm/gorm

GORM, the de-facto Go ORM, at 39.9k stars. It's the "fantastic ORM library for Golang" — associations, hooks, migrations, transactions, and a query builder that reads like SQL but stays type-safe-ish. MIT licensed. It's the thing everyone uses and half of Go devs complain about, but it's still the default for a reason: it gets you 90% of the way without fighting the language.

## 15. Solana Mev Eth Bot — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/darby42thieforest/solana-mev-eth-bot)

**Source:** https://www.opensourceprojects.dev/post/d1d07eb1-1d9a-4400-ab9f-585f194ff254
**Karakeep doc:** `uzsjcs0fqy9a79r54l0s7mqf`

The repo behind this stub (`darby42thieforest/solana-mev-eth-bot`) 404s on GitHub — it's been deleted or never existed. The name screams "MEV bot" scam bait, the kind of thing that's usually a rug-pull or a wallet-drainer in disguise. Skip it. If you want MEV tooling, look at something with actual stars and a real maintainer.

## 16. FinancePy: Options, bonds, and more with C-like speed via Numba — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/domokane/financepy)

**Source:** https://www.opensourceprojects.dev/post/1faeccc6-e9ad-4ef3-82b4-e13822c86892
**Karakeep doc:** `ucqwwu8zcywpr4zgj1sfhi9d`
**GitHub:** https://github.com/domokane/financepy

FinancePy is a Python finance library focused on pricing and risk for options, bonds, and other derivatives, using Numba to get C-like speed. 3.1k stars, GPL-3.0, mostly Jupyter notebooks. It's aimed at quants and students who want a self-contained pricing library without pulling in a full Bloomberg terminal. Solid if you're doing derivatives math in Python.

## 17. Alpaca-py brings OOP design and data validation to Python trading APIs — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/alpacahq/alpaca-py)

**Source:** https://www.opensourceprojects.dev/post/edf1fd27-5bd0-4b60-971d-fe9e37c414bd
**Karakeep doc:** `u1xq2n47fvdetvhmuk8zwdcu`
**GitHub:** https://github.com/alpacahq/alpaca-py

The official Python SDK for the Alpaca trading API, 1.5k stars, Apache-2.0. It wraps Alpaca's REST and streaming endpoints with proper OOP models and Pydantic data validation, so you get typed objects instead of raw dicts. If you're building an algo-trading bot against Alpaca, this is the sanctioned client.

## 18. Checkmate — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/bluewave-labs/checkmate)

**Source:** https://www.opensourceprojects.dev/post/bfbe78d2-cd69-4364-a236-d1e6d0ba7b13
**Karakeep doc:** `revfooc6rt7kmxaxnibfymhb`
**GitHub:** https://github.com/bluewave-labs/checkmate

Checkmate is a self-hosted server and infrastructure monitoring tool from Bluewave Labs — 10.8k stars, TypeScript, AGPL-3.0. It tracks CPU, memory, disk, and network across your servers with a clean dashboard and alerting. Think of it as a lighter, self-hosted alternative to the Datadog/New Relic tier. The AGPL license is the thing to note if you're building a commercial product on top of it.

## 19. BetterDisplay turns any Mac display into a fully scalable screen with DDC and virtual displays — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/waydabber/betterdisplay)

**Source:** https://www.opensourceprojects.dev/post/80c1b61c-4681-4d11-b6b5-0e2755d929b1
**Karakeep doc:** `ov4i003ex5pr6lftkys1y0r3`
**GitHub:** https://github.com/waydabber/betterdisplay

BetterDisplay is the Mac display utility — 33.5k stars. It unlocks HiDPI scaling, lets you create virtual displays, control brightness/contrast via DDC, and manage external monitors properly. It's the thing you install the day you plug a 4K monitor into a Mac and realize macOS's scaling options are garbage. No license field on the repo, but it's the de-facto standard for this.

## 20. WSA builds with GApps are breaking after June 2025 — here's the fix and LTS releases — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/mustardchef/wsabuilds)

**Source:** https://www.opensourceprojects.dev/post/268cb89c-0e18-466a-ab08-c76762fc318b
**Karakeep doc:** `o8aro4rts4g1ktx7vln47iot`
**GitHub:** https://github.com/MustardChef/WSABuilds

WSABuilds is the community project that keeps Windows Subsystem for Android alive with Google Play Services (GApps) baked in — 18.3k stars, Python, AGPL-3.0. The post is about GApps builds breaking after June 2025 and the LTS releases that fix it. If you still run Android apps on Windows, this is the maintained fork to use now that Microsoft's official WSA is dead.

## 21. Web3j: Java and Android library for Ethereum smart contracts — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/lfdt-web3j/web3j)

**Source:** https://www.opensourceprojects.dev/post/35371476-ea59-4a31-a373-82985f72e9fc
**Karakeep doc:** `mhhioxcd6jpuzeujyeqa9dwx`
**GitHub:** https://github.com/LFDT-web3j/web3j

Web3j is the Java/Android library for interacting with Ethereum — 5.4k stars, Java, now under the LFDT (Linux Foundation Decentralized Trust) umbrella. It generates typed smart-contract wrappers from ABI so you don't hand-roll boilerplate. If you're stuck writing Ethereum integration in Java (banking, enterprise), this is the standard.

## 22. DocStrange turns PDFs, DOCX, and images into LLM-optimized Markdown and JSON — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/nanonets/docstrange)

**Source:** https://www.opensourceprojects.dev/post/930d492f-2775-4c83-9670-979a82b2ac25
**Karakeep doc:** `h29pvo98ju3p5vciph1yvspt`
**GitHub:** https://github.com/NanoNets/docstrange

DocStrange (from NanoNets) converts PDFs, DOCX, and images into clean Markdown and JSON optimized for LLM ingestion — 1.5k stars, Python, MIT. It's a document-parsing pipeline for RAG: feed it a messy PDF, get structured text your model can actually use. Useful if you're building a document-QA system and tired of garbage OCR output.

## 23. Stop scrolling through go test output — let tparse summarize failures, panics, and more — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/mfridman/tparse)

**Source:** https://www.opensourceprojects.dev/post/55e64eba-9df2-41cc-be7f-963a345c40b5
**Karakeep doc:** `g6jlw0p6xopkkbrahpxkxtnt`
**GitHub:** https://github.com/mfridman/tparse

`tparse` is a Go test-output formatter — 1.3k stars, Go, MIT. Pipe `go test` into it and it summarizes failures, panics, and slow tests into a readable table instead of a wall of `--- FAIL` lines. A small quality-of-life tool that's genuinely nice if you run Go tests in CI and squint at raw output all day.

## 24. Backtesting that accounts for feed latency, order latency, and queue position — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/nkaz001/hftbacktest)

**Source:** https://www.opensourceprojects.dev/post/dcb48799-ee0f-46bc-9e22-65ef4ea68e7a
**Karakeep doc:** `bnr14407l29rzfiuc9k46ox5`
**GitHub:** https://github.com/nkaz001/hftbacktest

`hftbacktest` is a high-frequency trading backtester in Rust (with Python bindings) — 4.6k stars, MIT. The selling point is realism: it models feed latency, order latency, and queue position, so your backtest doesn't lie to you the way naive bar-based backtests do. If you're doing HFT research and want results that survive contact with a real exchange, this is the serious option.

## 25. Fullstack SaaS boilerplate with Fastify, tRPC, and React 19 — demo included — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/alan345/ai-fullstack-saas-boilerplate)

**Source:** https://www.opensourceprojects.dev/post/72cf9c3e-1209-4851-bcc3-6285e7807527
**Karakeep doc:** `ssy8thmtxae6x4so4l35whqy`
**GitHub:** https://github.com/alan345/AI-Fullstack-SaaS-Boilerplate

A fullstack SaaS starter with Fastify, tRPC, and React 19 — 1.4k stars, TypeScript, MIT. It's the "clone this and you have auth, billing, and a working app shell" template. The "AI" in the name is marketing; the actual stack is a solid modern TypeScript monorepo. Fine if you want a head start on a SaaS, but it's a boilerplate, not a product.

## 26. Papra: open-source document archiving with email ingestion, OCR, and self-hosting — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/papra-hq/papra)

**Source:** https://www.opensourceprojects.dev/post/6f86cf95-878a-4b45-ad4b-b2a1bfcbe6d4
**Karakeep doc:** `llovcn4lsc2bdrrm56qhwoi6`
**GitHub:** https://github.com/papra-hq/papra

Papra is a self-hosted document archiving platform — 5.3k stars, TypeScript, AGPL-3.0. It ingests documents via email, runs OCR, and stores everything searchable. Think Paperless-ngx but with a more modern stack and a focus on email ingestion. If you're already running a self-hosted stack and want your paperwork searchable, this is worth a look.

## 27. The $15 ESP32 dev board with a built-in 2.8" touchscreen deserves better docs — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/witnessmenow/esp32-cheap-yellow-display)

**Source:** https://www.opensourceprojects.dev/post/211a21f2-b189-4620-beac-d74718d46696
**Karakeep doc:** `cakug82zhdc9yaagyajf5jad`
**GitHub:** https://github.com/witnessmenow/ESP32-Cheap-Yellow-Display

The "Cheap Yellow Display" is a $15 ESP32 board with a 2.8" touchscreen that's become a hobbyist favorite — 4.4k stars, Rust, MIT. The repo is a community effort to document and build around the board, since the official docs are thin. If you want a dirt-cheap touchscreen dev board for a home dashboard or sensor display, this is the one everyone's using.

## 28. Generative AI guide that sorts courses by journey and skill level — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/aishwaryanr/awesome-generative-ai-guide)

**Source:** https://www.opensourceprojects.dev/post/eff8ea81-488e-4c74-91ee-f07be6e7fc8c
**Karakeep doc:** `ascgi09vq28fzq8oovx5bk0w`
**GitHub:** https://github.com/aishwaryanr/awesome-generative-ai-guide

An "awesome list" of generative AI resources — 29.3k stars, HTML, MIT. It's a curated index of courses, papers, and tools, sorted by journey and skill level. The kind of thing you bookmark and never actually read, but it's a decent starting point if you're trying to figure out where to begin with gen AI. It's a list, not a course.

## LinuxLinks (RSS)

## 29. Typesetter - Minimalist Typst Editor — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2019/08/document-management-systems.jpg)

**Source:** https://www.linuxlinks.com/typesetter-minimalist-typst-editor/
**Karakeep doc:** `uydf7b0oct1e8loblmnkti77`

Typesetter is a minimalist editor for Typst, the LaTeX alternative that's been eating LaTeX's lunch lately. LinuxLinks profiles it as a clean, focused writing environment for Typst documents. If you're curious about Typst but don't want to fight a full IDE, a dedicated minimal editor is the on-ramp. (The LinuxLinks post is a thin profile; the actual project is the thing to check.)

## 30. 17 Best Free and Open Source Linux File Managers — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2022/05/Transfer_Files41021.jpg)

**Source:** https://www.linuxlinks.com/filemanagers/
**Karakeep doc:** `s19e0y2zf65en9wyhzs87s1g`

A roundup of 17 FOSS file managers for Linux. The usual suspects — Nautilus, Dolphin, Thunar, Nemo — plus the terminal/tiling crowd-pleasers like ranger, nnn, and lf. It's a listicle, so the value is in discovering the niche ones (dual-pane, keyboard-driven, or tiling-WM-integrated) you haven't tried. Skim it, don't read it.

## 31. myMarkmap - Create Mind Maps from Markdown — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/11/Minder-mapping.png)

**Source:** https://www.linuxlinks.com/mymarkmap-create-mind-maps-markdown/
**Karakeep doc:** `w0jyvl8s9rx52s7bbnw9f0xw`
**GitHub:** https://github.com/eyssette/myMarkmap

myMarkmap is a custom editor for Markmap, the tool that turns Markdown outlines into interactive mind maps — 65 stars, Svelte, MIT. It's a niche tool for people who think in outlines and want a visual map without leaving Markdown. Small project, but if you do a lot of note-taking and want a mind-map view, it's a neat trick.

## 32. 9 Best Free and Open Source Font Managers — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/05/044-font.png)

**Source:** https://www.linuxlinks.com/best-free-open-source-font-managers/
**Karakeep doc:** `qi681c49ca4yp75u5b7ogzwl`

Nine FOSS font managers — Font Manager, FontBase, and the usual GNOME/KDE options. If you've ever had a thousand fonts installed and no way to preview or organize them, this is the roundup for you. It's a listicle; the useful bit is finding one that does live preview and font comparison without a subscription.

## 33. Fedora CoreOS - minimal container-focused Linux distribution — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/04/Linux-Distributions.png)

**Source:** https://www.linuxlinks.com/fedora-coreos-minimal-container-focused-linux-distribution/
**Karakeep doc:** `dcma2t1m03iyo2oekfvxci78`

Fedora CoreOS is the minimal, auto-updating Fedora built for running containerized workloads at scale. It's immutable, ships with Ignition for provisioning, and updates itself atomically. If you're running Kubernetes or a container host and want an OS you never have to babysit, this is the Fedora answer to Flatcar/Container Linux. The LinuxLinks post is a profile, not a tutorial.

## 34. Revisited: SparkPlayer — visually appealing media player now with gapless playback — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2022/12/music-printing-blocks.jpg)

**Source:** https://www.linuxlinks.com/sparkplayer-visually-appealing-media-player-gapless-playback/
**Karakeep doc:** `hyfb9b2dtjl7kyoexo1qevuq`
**GitHub:** https://github.com/dividebysandwich/sparkplayer

SparkPlayer is a terminal-based media player in Rust — 52 stars, GPL-2.0. The "revisited" angle is that it now has gapless playback, plus visualizers, album art, and video support. It's a TUI music/video player for people who live in the terminal. Small but charming; the gapless playback is the headline feature for album listeners.

## 35. rst2pdf - Convert reStructuredText Documents to PDF — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2019/04/PDF-File.png)

**Source:** https://www.linuxlinks.com/rst2pdf-convert-restructuredtext-documents-pdf/
**Karakeep doc:** `gqjde11n61csoo6x1gaw6jtp`
**GitHub:** https://github.com/rst2pdf/rst2pdf

rst2pdf converts reStructuredText straight to styled PDF using ReportLab — 595 stars, Python, MIT. It's the "write docs in reST, ship a PDF" tool, with a tagline that nails it: "Use a text editor. Make a PDF." If you're in the Sphinx/reST ecosystem and need PDF output without LaTeX, this is the path.

## 36. Netshot - Network Configuration and Compliance Management — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2023/02/20944989-network.jpg)

**Source:** https://www.linuxlinks.com/netshot-network-configuration-compliance-management/
**Karakeep doc:** `dklpilow1wmk95eqk9b6u92c`
**GitHub:** https://github.com/netshot-net/Netshot

Netshot is a web app for network inventory, config backup, compliance monitoring, and automated device tasks — 284 stars, Java. It's the "keep track of every switch and router config, back them up, and check they comply" tool. Niche, but if you manage a fleet of network devices and want config drift detection without paying for SolarWinds, this is the FOSS option.

## 37. 6 Best Free and Open Source Material and Texture Authoring Tools — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/04/3d-render-abstract-background-with-space-your-text-digital-3d-illustration-design.jpg)

**Source:** https://www.linuxlinks.com/best-free-open-source-material-texture-authoring-tools/
**Karakeep doc:** `d086muszdpd9s2ke1yjmet47`

Six FOSS tools for material and texture authoring — the Substance Painter/Designer alternatives for 3D artists, game devs, and VFX. Expect Material Maker, ArmorPaint, and similar. If you do 3D work and want procedural textures without an Adobe subscription, this roundup is the starting point. Listicle, skim it.

## 38. open-pdf-sign - Digitally Sign PDF Documents — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2019/04/PDF-File.png)

**Source:** https://www.linuxlinks.com/open-pdf-sign-digitally-sign-pdf-documents/
**Karakeep doc:** `twk4xjlb6j23kjy6ylzkqwb1`
**GitHub:** https://github.com/open-pdf-sign/open-pdf-sign

open-pdf-sign is a CLI and server for applying standards-based electronic signatures and timestamps to PDFs — 949 stars, Java, Apache-2.0. It's the "sign a PDF from the command line or a server, legally" tool. If you need to batch-sign documents or integrate signing into a workflow without a GUI, this is it.

## 39. 14 Best Free and Open Source Mailing List Managers — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/03/businessman-touching-wireframe-e-mail-email-marketing-newsletter.jpg)

**Source:** https://www.linuxlinks.com/mailinglistmanagers/
**Karakeep doc:** `tu3gau9mf87e39iawv5mwfee`

Fourteen FOSS mailing list managers — Mailman, Sympa, and the rest. If you run a community or project and need to manage discussion lists or newsletters without paying Mailchimp, this is the roundup. It's a listicle; the useful bit is comparing Mailman vs Sympa vs the lighter options for your scale.

## 40. Best Free and Open Source Alternatives to Apple Pixelmator Pro — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2018/10/Painting-tools.jpg)

**Source:** https://www.linuxlinks.com/best-free-open-source-alternatives-apple-pixelmator-pro/
**Karakeep doc:** `eu985nltjjiu8dyht5xuybbl`

FOSS alternatives to Pixelmator Pro for image editing, retouching, and painting on Linux — GIMP, Krita, and friends. The framing is "you're leaving the Apple ecosystem, here's what replaces Pixelmator." If you're doing the Mac-to-Linux migration (see item 1), this is the companion roundup for your image-editing needs.

## 41. latexindent.pl - highly configurable LaTeX formatter — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2021/07/typesetting-tools.jpg)

**Source:** https://www.linuxlinks.com/latexindent-pl-highly-configurable-latex-formatter/
**Karakeep doc:** `o4jpmtm4rf91tt5c25chd180`
**GitHub:** https://github.com/cmhughes/latexindent.pl

latexindent.pl is a Perl script that formats LaTeX source — 1.1k stars, TeX, GPL-3.0. Configurable indentation, delimiter alignment, text wrapping, substitutions, and YAML rules. It's the `prettier` of the LaTeX world: run it on your `.tex` files and stop arguing about whitespace. If you write LaTeX and care about readable source, this is a must-have.
