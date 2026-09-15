---
date: 2026-09-14
slug: 2026-09-14-morning-brew
tags: Open Source Software,Cybersecurity,Data Visualization,Cyber Threat Intelligence,Knowledge Graph,Machine Learning,Artificial Intelligence,Large Language Models,Distillation Attacks,C++ Programming,Signal Processing,Satellite Navigation,Software Defined Radio,Debugging,Performance Optimization,Python Programming,Profiling,Automation,Command Line Tools,Video Downloading,YouTube,Open Source,Programming,Software Development,Project Showcase,Productivity Tools,ChatGPT,Prompt Engineering,API Development,Logistics,Supply Chain Management,Fleet Management,Frontend Development,Design Systems,Web Development,UI Components,Networking,Open Source Projects,Proxy Servers,Speed Testing,Automation Tools,Python,Data Science,Pandas,Rust Programming,Developer Tools,Coding Resources,Programming Languages,Scala,Static Code Analysis,Linux,System Administration,Systemd,Graphical User Interface,Perl,Language Server Protocol,Typography,Character Maps,Unicode,Web Applications,File Sharing,Data Management,Self-Hosted,Earth Science,Geographic Information System,Geospatial Data,AI Agents,Best Practices,Documentation,Color Picker,Graphic Design,Linux Software,Code Linting,Compiler Plugins,Self-Hosted Software,Travel Planning,Trip Planner,Mapping and Navigation,Software Engineering,React Native,Mobile Development,Hardware Benchmarking,Cloudflare,Online Attacks,Web Security,Operating Systems,Linux Distributions,Language Learning,Vocabulary Building,Education Technology,Data Privacy,Google Gemini,Smartphones,Mobile Technology,Computer Science,Linux Kernel,Planned Obsolescence,Hardware Support,Media Downloader,Video Downloader,Multimedia Tools,Wireless Security,Network Security,Penetration Testing,PHP Programming,Code Formatter,Slackware,Linux Distribution,Security,Minimalism,Journaling,Elixir Programming
---

# Morning Brew — 2026-09-14

Thursday's hoard was a pure RSS flood — 34 items, zero hand-bookmarks. Five YouTube videos (now transcribed): an Anthropic-distillation deep-dive, a React Native obituary, a planned-obsolescence rant, and two Brodie shorts. Plus a Firefox 156 drop, the usual LinuxLinks / opensourceprojects firehose, and one Polish privacy piece from NieBezpiecznik.

### RSS — YouTube

## 1. DeepSeek and Kimi Secretly Sent Your Prompts to Claude — by Better Stack

![Better Stack](https://img.youtube.com/vi/hSVCYzphZjQ/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=hSVCYzphZjQ
**Karakeep doc:** `e5dktv4oxxgkli9l8lzqqw1o`

Anthropic's new threat report names seven Chinese AI labs for distilling Claude at industrial scale. Biggest offender: Alibaba's Qwen, with 151M exchanges over May–July, ~3,500 fake accounts, peak ~3M requests a day — and they weren't after the answer, they wanted the chain-of-thought. Moonshot (Kimi) and DeepSeek allegedly forwarded their own users' prompts through Claude and replayed the "thinking signature" across sessions to pull out the reasoning. DeepSeek even routed anyone using Claude Code or the Agent SDK to Opus, betting those users are the best source of agentic-coding data. Response: Anthropic now summarizes Claude's reasoning before answering and added "preserved thinking" to Fable 5.1 so scrapers get less.

## 2. Most GitHub Repos Are Doing AGENTS.md WRONG #ai #agents #bestpractices — by Better Stack

![Better Stack](https://img.youtube.com/vi/kJ4uDzFAL8k/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/kJ4uDzFAL8k
**Karakeep doc:** `c5szd72t2wwpip9pg3qdq56d`

ColdTe (Better Stack) scraped the top 1,000 GitHub repos to see what goes in an AGENTS.md. Only 27% even have one. The pattern: bigger repo, stricter file — the top 100 spend nearly double the space on "don't" rules. Vercel bans "generated with Claude Code" commit footers, Bun has an all-caps "NEVER run bun test directly". Median length is ~1,200 words, openhands runs 14k, VS Code's is 33 words. Their checklist: at least one explicit don't, spelled-out commit/PR format, and how to run tests and lint.

## 3. Did AI kill React Native? — by Theo - t3․gg

![Theo - t3․gg](https://img.youtube.com/vi/oPZLPUtmROo/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=oPZLPUtmROo
**Karakeep doc:** `ek3uivbcnqwrca3wtath7a9g`

Theo reacts to Shopify dropping React Native and going back to Swift/Kotlin. Their stated reason: AI coding agents killed the "build once, run twice" cost argument, so native's platform fidelity wins again. Theo's counterpoint is OTA updates — the one thing native can't match, and the reason half your Twitch users run a two-version-old app. He also roasts Shopify's new "Helix" migration system (checkpoint-by-checkpoint with two adversarial reviews) as codebase-worship over-engineering. Shop app went POC-to-App Store in 12 weeks via greenfield rewrite.

## 4. Slackware vs Debian — by Brodie Robertson

![Brodie Robertson](https://img.youtube.com/vi/_tNWPqT4qxI/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/_tNWPqT4qxI
**Karakeep doc:** `waz2bvdfan0brbky85r2wr0p`

Brodie Robertson, 60-second take: Slackware and Debian are a month apart in age, but couldn't be further apart in relevance. If Slackware vanished tomorrow, nobody would notice. If Debian vanished, you'd get world economic collapse — that much of the internet runs on it. His punchline: Debian is so important and so under-supported it's almost unfair.

## 5. Linux Kernel And Planned Obsolescence — by Brodie Robertson

![Brodie Robertson](https://img.youtube.com/vi/k5L47tFUgtQ/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=k5L47tFUgtQ
**Karakeep doc:** `s9g6ocg3pnhttiukdzv9lm51`

Brodie argues the kernel dropping 30-year-old CPUs is not planned obsolescence. He defines the real thing (built-to-fail, unrepairable, serial-locked parts, Apple's secret CPU throttling, printer ink counters) and points out the kernel never built that hardware, never set an EOL date, and debated each drop for years. You can downgrade the kernel, fork it, or run T2 Linux if you want the old chips back. His point: calling every support drop "planned obsolescence" waters the term down until real cases stop mattering.

### 9to5Linux (RSS)

## 6. Mozilla Firefox 156 Is Now Available for Download, Here’s What’s New — by 9to5Linux

![9to5Linux](https://9to5linux.com/favicon.ico)

**Source:** https://9to5linux.com/mozilla-firefox-156-is-now-available-for-download-heres-whats-new
**Karakeep doc:** `n7oyyne33z2xd226oib7ypo9`

Firefox 156 lands ahead of the Sept 15 unveiling. Better memory/CPU on large scaled-down JPEGs, FLAC audio in MP4, PiP subtitles, and a PDF viewer that starts up to 45% faster. Android gets prev/next media buttons, a seek timeline, and the native share sheet on 14+. macOS auto-starts the browser, Windows gets hardware H.264 decode for WebRTC on ARM64. A few new enterprise policies (FirefoxHome widgets, DisableServiceWorkers) round it out. (Note: the feed title was a Cloudflare interstitial — the real body parsed fine.)

### Open-source Projects (RSS)

## 7. A software-defined GNSS receiver that decodes GPS, Galileo, GLONASS, and BeiDou — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/gnss-sdr/gnss-sdr)

**Source:** https://www.opensourceprojects.dev/post/a8c36141-2aee-4cda-a4c1-e6e7400f6922
**Karakeep doc:** `yj7d32dkfldp1u7o9c33on48`
**GitHub:** https://github.com/gnss-sdr/gnss-sdr

GNSS-SDR — a software-defined GNSS receiver that turns raw radio samples into position fixes for GPS, Galileo, GLONASS and BeiDou. C++, GPL-3.0, ~2.2k stars. Every stage of the signal chain is inspectable, aimed at students and researchers, not plug-and-play users.

## 8. Trace Python execution with low overhead and visualize it in Perfetto — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/gaogaotiantian/viztracer)

**Source:** https://www.opensourceprojects.dev/post/48a94c7e-03a8-43db-9249-4ed43281c32b
**Karakeep doc:** `xp438lw4qcslys3c4407t3wx`
**GitHub:** https://github.com/gaogaotiantian/viztracer

VizTracer traces Python execution with low overhead and renders it as an interactive Perfetto timeline in the browser. Python, Apache-2.0, ~7.7k stars. Handles threading, multiprocessing and async. Good for finding bottlenecks or debugging concurrency without a setup song-and-dance.

## 9. A command-line program to download videos from YouTube and other sites — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/ytdl-org/youtube-dl)

**Source:** https://www.opensourceprojects.dev/post/caa0dbd1-ac6b-4f29-831a-a87404d79482
**Karakeep doc:** `wkxj8ktzzvg9imm0xnwgfpne`
**GitHub:** https://github.com/ytdl-org/youtube-dl

youtube-dl — the classic command-line video downloader, ~141k stars, Unlicense. Still the reference extractor library, even if yt-dlp is the fork everyone actually uses these days. Nothing new to say; it's youtube-dl.

## 10. Contractsforbase — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/autoglasschandler/contractsforbase)

**Source:** https://www.opensourceprojects.dev/post/6b9770be-5198-4c18-919e-247da44ff6d1
**Karakeep doc:** `swbtxexi6rvm9or2ya3c7aat`

Contractsforbase. The GitHub repo (autoglasschandler/contractsforbase) 404s and the source page is an empty stub, so there's nothing real to summarize — the feed pushed a repo name with no body. Linking it anyway in case it comes back.

## 11. A collection of GPT Store prompts, organized by category — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/b3o/gpts-prompt-collection)

**Source:** https://www.opensourceprojects.dev/post/baf2b303-eb21-416b-94d9-7efbe891d967
**Karakeep doc:** `r8z2sk18fsjioj58q4guuk2t`
**GitHub:** https://github.com/B3o/GPTS-Prompt-Collection

GPTS-Prompt-Collection (B3o) — a curated pile of GPT Store prompts organized by category, saved as plain markdown so you can read the "behind the scenes" instructions of popular GPTs. ~1.8k stars, MIT, no language. There's a "Boutique" section of hand-picked system prompts. Handy if you want to steal good prompt engineering.

## 12. Modular logistics and supply chain OS you can extend via API — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/fleetbase/fleetbase)

**Source:** https://www.opensourceprojects.dev/post/444149c9-703c-4535-964f-4f96d7b08ca9
**Karakeep doc:** `p9l9fx1g1k5szlh7vnt02oub`
**GitHub:** https://github.com/fleetbase/fleetbase

Fleetbase — a modular logistics and supply-chain OS you extend via API. JavaScript, AGPL-3.0, ~3.1k stars. Kanban order board, workflow config with logic/automation, live fleet maps. The anti-monolith for order management and last-mile delivery.

## 13. Beautifully designed components you can customize, extend, and build on — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/shadcn-ui/ui)

**Source:** https://www.opensourceprojects.dev/post/3bc418a2-317f-4d44-bc3e-8e3c315f9f9c
**Karakeep doc:** `ofypbd3lpgm4ouzyhpukckf4`
**GitHub:** https://github.com/shadcn-ui/ui

shadcn/ui — the copy-paste component library. TypeScript, MIT, ~124k stars. Instead of installing a dependency, you copy the source into your repo and own it. Still the default answer for accessible React components you can actually customize.

## 14. Crawls and filters free nodes, then lets you speed-test them locally — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/leon406/subcrawler)

**Source:** https://www.opensourceprojects.dev/post/f9fa73f4-75da-46ff-9693-d4e6b585cc60
**Karakeep doc:** `ntfl9nixiprxy9vdf8dg4ksh`
**GitHub:** https://github.com/Leon406/SubCrawler

SubCrawler crawls and filters free proxy nodes, then lets you speed-test them locally. Kotlin, GPL-3.0, ~1.6k stars. Generates base64 subscription files for v2rayN/SS/SSR. It's a proxy-node harvester with a gfw/shadowsocks flavour — useful if you know why you need it.

## 15. A Flask and React front-end for viewing and analyzing Pandas data structures — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/man-group/dtale)

**Source:** https://www.opensourceprojects.dev/post/e2085ca9-176d-4b6b-ba4c-69efd934aae5
**Karakeep doc:** `ndj9takvys1ir2qitlzw40yt`
**GitHub:** https://github.com/man-group/dtale

D-Tale — a Flask/React front end for eyeballing pandas DataFrames in the browser, straight from a notebook or terminal. TypeScript, LGPL-2.1, ~5.2k stars. 3D scatter, surface charts, network analysis. Built at Man Group for production use.

## 16. A curated list of Rust code and resources, organized by category — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/rust-unofficial/awesome-rust)

**Source:** https://www.opensourceprojects.dev/post/a68d2dce-c78f-42c5-b603-9350986c1357
**Karakeep doc:** `yd2h7s2bv5aerqb0z1loyzgw`
**GitHub:** https://github.com/rust-unofficial/awesome-rust

awesome-rust — the curated list of Rust code and resources, ~59k stars, CC0. The canonical jumping-off point when you need a Rust crate for anything. Nothing clever to say; it's the list.

### LinuxLinks (RSS)

## 17. OpenCTI Community Edition - cyber threat intelligence knowledge platform — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2022/12/cyber-security.jpg)

**Source:** https://www.linuxlinks.com/opencti-community-edition-cyber-threat-intelligence-knowledge-platform/
**Karakeep doc:** `q3b52blgo29k6mnq0edmddib`
**GitHub:** https://github.com/OpenCTI-Platform/opencti

OpenCTI Community Edition — a cyber threat-intel knowledge platform built on STIX. TypeScript, ~10k stars. Stores observables plus attribution/victimology in a connected knowledge graph, with a GraphQL API and a pile of connectors. The go-to open-source CTI store if you're doing anything threat-intel-shaped.

## 18. Scapegoat - static code analysis for Scala — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/01/013-coding.png)

**Source:** https://www.linuxlinks.com/scapegoat-static-code-analysis-scala/
**Karakeep doc:** `kn59zxfqzsm9dmp72010m89x`
**GitHub:** https://github.com/scapegoat-scala/scapegoat

Scapegoat — a Scala compiler plugin for static code analysis. Scala, Apache-2.0, ~556 stars. Catches code smells at compile time rather than in a separate linter pass. Fine for Scala shops that want linting wired into the build.

## 19. 4 Useful Free and Open Source systemd GUI Configuration Tools — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2021/11/command-schedulers.png)

**Source:** https://www.linuxlinks.com/useful-free-open-source-systemd-gui-configuration-tools/
**Karakeep doc:** `r0goo7qmd5lmxzq4uydq6twa`

A LinuxLinks roundup of 4 systemd GUI tools: SystemdGenie, SysD Manager, systemd Pilot and gnome-logs. If you'd rather click services than type systemctl, these wrap unit management and journal viewing in a GUI. Nothing groundbreaking, just a nicer front end on the same init system.

## 20. perl-lsp - language server for Perl — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/02/034-proofreading.png)

**Source:** https://www.linuxlinks.com/perl-lsp-language-server/
**Karakeep doc:** `mzs7etoa9sxswlqwjcdekbp3`
**GitHub:** https://github.com/tree-sitter-perl/perl-lsp

perl-lsp — a fast Perl language server in Rust with cross-file type inference, completion, goto-def and rename. MIT, ~25 stars, built on tree-sitter-perl and tower-lsp. Tiny but real: the first decent LSP for Perl, so Neovim/VSCode can finally treat Perl like a language that exists.

## 21. 5 Best Free and Open Source Character Map Tools — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/09/Character-Map-c.png)

**Source:** https://www.linuxlinks.com/best-free-open-source-character-map-tools/
**Karakeep doc:** `e77ad1m4qratu53yi4jdphdb`

A LinuxLinks roundup of 5 character-map tools: KCharSelect, gucharmap, Glyphana and friends. Lets you browse and copy special symbols / Unicode from a font without knowing the codepoint. Useful for devs and typography nerds.

## 22. SafeBucket - on-premises file sharing platform — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2022/05/Transfer_Files41021.jpg)

**Source:** https://www.linuxlinks.com/safebucket-on-premises-file-sharing-platform/
**Karakeep doc:** `x5vclaxlyfadsel1iqg9yaod`
**GitHub:** https://github.com/safebucket/safebucket

SafeBucket — on-premises file sharing. Go, Apache-2.0, ~960 stars, backed by Storj. Self-hosted S3-style sharing that keeps your files on your own hardware. The "simple, fast, safe" pitch for people who don't want their shares on someone else's cloud.

## 23. 11 Best Free and Open Source Linux GIS Software — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/05/009-geology.png)

**Source:** https://www.linuxlinks.com/earthscience/
**Karakeep doc:** `hlh6cbudzq137j9nrq5j5nrp`

A LinuxLinks roundup of 11 open-source GIS tools for Linux. Covers cartography, land-use analysis, infrastructure management — the usual QGIS/GDAL-adjacent crowd. If you're doing geospatial work on Linux, here's your shortlist.

## 24. Piccolo – modern GTK color picker — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/12/038-color-scheme.png)

**Source:** https://www.linuxlinks.com/piccolo-modern-gtk-color-picker/
**Karakeep doc:** `kq6jw19y248ptyo8mex75le8`
**GitHub:** https://github.com/Azakidev/Piccolo

Piccolo — a modern GTK color picker for Linux. Rust, MIT, ~20 stars, GTK4/libadwaita. Small and pleasant. Picks colors; that's the whole pitch, and it does it without being ugly.

## 25. WartRemover - flexible Scala code linter — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/02/034-proofreading.png)

**Source:** https://www.linuxlinks.com/wartremover-flexible-scala-code-linter/
**Karakeep doc:** `ftgmreb4vemaaba7q6huk5i7`
**GitHub:** https://github.com/wartremover/wartremover

WartRemover — the flexible Scala code linter. Scala, Apache-2.0, ~1.1k stars. A compiler plugin with a big set of built-in warts and the ability to write your own. The standard "keep Scala honest" tool.

## 26. TRIP - self-hosted POI map tracker and trip planner — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2022/11/istanbul-metro-train-line-platfrom-built-halic-with-beautiful-istanbul-landmarks.jpg)

**Source:** https://www.linuxlinks.com/trip-self-hosted-poi-map-tracker-trip-planner/
**Karakeep doc:** `d3wl8oa30x41ipjdznck7ayp`
**GitHub:** https://github.com/itskovacs/trip

TRIP — a minimalist, self-hosted POI map tracker and trip planner. TypeScript, MIT, ~1.9k stars. Plot points of interest, plan trips, visualize routes. Clean and self-hosted, so your travel data stays yours.

## 27. BOSGAME VTA-439 - Running LLMs on the Ryzen AI 9 HX 470 NPU — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/06/BOSGAME-VTA-439-banner.png)

**Source:** https://www.linuxlinks.com/bosgame-vta-439-running-llms-ryzen-ai-9-hx-470-npu/
**Karakeep doc:** `z43b9tny836c0vv5hoknupuo`
**GitHub:** https://github.com/ROCm/FastFlowLM

The BOSGAME VTA-439 article points at ROCm's FastFlowLM — run LLMs on the AMD Ryzen AI NPU (the 9 HX 470's 50 TOPS NPU) in minutes. C++, MIT, ~1.9k stars. Purpose-built for AMD NPUs, supports llama/deepseek. The interesting bit: a mini-PC NPU is now actually usable for local inference instead of being a marketing checkbox.

## 28. Aprelendo – learn vocabulary from real content — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2019/04/learning-foreign-languages.jpg)

**Source:** https://www.linuxlinks.com/aprelendo-learn-vocabulary/
**Karakeep doc:** `a37l4jqdm5ruckv34nktsutc`
**GitHub:** https://github.com/usemoslinux/aprelendo

Aprelendo — learn vocabulary while reading real content. PHP, GPL-3.0, ~31 stars. Flashcard-style vocab building from whatever you're already reading. Small but self-hostable, good for the language-learning tinkerer.

## 29. GDownloader – GUI for yt-dlp, gallery-dl and spotDL — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2022/07/youtube-logo-around-3d-rendering-abstract-shape-background.jpg)

**Source:** https://www.linuxlinks.com/gdownloader-gui-yt-dlp-gallery-dl-spotdl/
**Karakeep doc:** `aneh0k7jtzn76id4rit63x8p`
**GitHub:** https://github.com/hstr0100/GDownloader

GDownloader — a cross-platform GUI wrapping yt-dlp, gallery-dl and spotDL. Java, GPL-3.0, ~221 stars. Batch-download videos, playlists, galleries and music with hardware-accelerated transcoding. A friendly face on the command-line downloaders you already know.

## 30. 12 Best Free and Open Source Wireless Security Tools — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2022/03/wifi-business-button-locked-shield-security.jpg)

**Source:** https://www.linuxlinks.com/best-free-open-source-wireless-security-tools/
**Karakeep doc:** `fowq9dxerpajk6onki9vrug0`

A LinuxLinks roundup of 12 wireless-security tools: aircrack-ng, Kismet and friends. The standard audit/monitor/pen-test kit for WiFi. Nothing new if you've done a pentest before, but a tidy reference list.

## 31. pretty-php - opinionated PHP code formatter — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/Code-Formatter-banner3.png)

**Source:** https://www.linuxlinks.com/pretty-php-opinionated-php-code-formatter/
**Karakeep doc:** `xw4ed3enw0ra2srvf1e0ars9`
**GitHub:** https://github.com/lkrms/pretty-php

pretty-php — the opinionated PHP code formatter. PHP, MIT, ~151 stars, deterministic. If you want one canonical output for your PHP with zero config drama, this is it. Opinionated on purpose.

## 32. fu11m00n - hardened live Slackware-based Linux distribution — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/04/Linux-Distributions.png)

**Source:** https://www.linuxlinks.com/fu11m00n-hardened-live-slackware-based-linux-distribution/
**Karakeep doc:** `s34rbfn89zhyt4c3v5ls7n1u`

fu11m00n — a hardened live Slackware-based distro. Uses musl instead of glibc, runit instead of systemd, a minimalist hardened design with read-only "petrified" binaries, and an LXQt/Cutefish desktop. For advanced users who want minimal and secure, not beginner-friendly.

## 33. JourniPlan - travel planner and micro journaling app — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2022/11/istanbul-metro-train-line-platfrom-built-halic-with-beautiful-istanbul-landmarks.jpg)

**Source:** https://www.linuxlinks.com/journiplan-travel-planner-micro-journaling-app/
**Karakeep doc:** `da8hvoyk6ot435dz6m7dap8f`
**GitHub:** https://github.com/jarlah/JourniPlan

JourniPlan — an open-source travel planner and micro-journaling app in Elixir/Phoenix LiveView. GPL-3.0, ~11 stars. Plan the trip, track expenses, journal it, all in one place. Tiny and self-hostable.

### RSS — Other

## 34. AI w telefonie może czytać Twój ekran. Co widzi i jak to ograniczyć? — by NieBezpiecznik.pl

![NieBezpiecznik.pl](https://niebezpiecznik.pl/wp-content/uploads/2026/09/ai-proget-600x345.jpg)

**Source:** https://niebezpiecznik.pl/post/ai-w-telefonie-moze-czytac-twoj-ekran-co-widzi-i-jak-to-ograniczyc/
**Karakeep doc:** `nlc7yzcro3k5866uhnsv87cb`

NieBezpiecznik teases a live webinar (Thu Sept 17, 19:00) on what Gemini can actually read on your Android screen and when that data leaves your phone. Artur from Proget (the MDM vendor) will demo concrete settings on Android and iPhone to rein in AI access, and what even MDM can't control. The honest framing: is phone AI a real new threat, or just something we need to manage consciously?
