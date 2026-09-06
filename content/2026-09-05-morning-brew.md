---
date: 2026-09-05
slug: 2026-09-05-morning-brew
tags: C,C++,CAPTCHA,DNSSEC,Distro,Documents,Domain Name Service,GNOME,GUI,Gantt,Go,Graphics,ISO,Internet,JavaScript,KDE Plasma,Multimedia,Office,Pastebin,Programming,QML,Roundup,SMART objectives,Scientific,Software,System Software,TypeScript,Utilities,Void,Web Apps,Xfce,bookmark manager,capture,climate,data analysis,distribution,distro,earth science,encryption,flash,free,graphics,image compression,image editor,java,meteorology,network security,noise,open source,photo editing,privacy,projects,proof of work,raster graphics,runit,screen,security,self-hosted,service discovery,visualization,weather,web
---

# Morning Brew — 2026-09-05

45 bookmarks from the hoard: 39 articles and 6 YouTube videos (all transcribed). LinuxLinks dumped a pile of tool roundups, opensourceprojects.dev served up a batch of half-dead stubs, and there's a couple of Brodie Robertson rants plus a NetworkChuck Omarchy tour. Let's go.

## 1. ISO Image Writer - write ISO images to USB drives — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2021/01/FlashOS.png)

**Source:** https://www.linuxlinks.com/iso-image-writer-write-iso-images-usb-drives/
**Karakeep doc:** `rz2ur7oqszvm940tbihzc9wa`

KDE's graphical tool for slapping ISO images onto USB sticks without touching `dd` and praying you picked the right device. It verifies checksums and digital signatures before writing, and has safeguards so you don't nuke your system drive by accident. Runs on Linux and Windows, uses UDisks2 under the hood, GPL v3. Honestly, if you're still typing `dd if=... of=/dev/sdX` from memory, this is the grown-up version of that anxiety. 😅

## 2. How To Create Honeypot Token — by Open-source Projects

![Open-source Projects](https://www.opensourceprojects.dev/favicon.ico)

**Source:** https://www.opensourceprojects.dev/post/0f717496-fd1d-4d76-83b7-c77536d90e1c
**Karakeep doc:** `ztq9cbmag63a1w04sa46jtb1`

The source page is gone — it now returns a 404, so there's no body to summarize. The title alone tells you it's a tutorial for minting honeypot tokens, i.e. the ERC20/BEP20 scam coins that let the deployer rug-pull buyers who can't sell. That's the whole pitch. If you're reading this to actually build one, maybe go touch grass instead. 🚩

## 3. Starter code for a Next.js portfolio with Tailwind and Framer Motion — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/codebucks27/next.js-developer-portfolio-starter-code)

**Source:** https://www.opensourceprojects.dev/post/5ebb9dba-ef00-4d9e-be0c-2d54def4a473
**Karakeep doc:** `ydvfkjoexlm9o90l13k7ruqj`

A starter template for a dev portfolio built on Next.js, styled with Tailwind, animated with Framer Motion. It's companion code to a YouTube tutorial, but the repo works standalone — home, about, projects, and articles pages, light/dark mode, responsive layout. Dark mode is already wired up, which saves you the usual Tailwind config headache. It's not original, but it's a low-effort way to get something professional online and learn the stack while you're at it. 👍

## 4. Books Free Books — by Open-source Projects

![Open-source Projects](https://www.opensourceprojects.dev/favicon.ico)

**Source:** https://www.opensourceprojects.dev/post/c889e250-e1b4-4fa9-aed6-325a69d40972
**Karakeep doc:** `x49999vzy0hubg96kwqmnsej`

Another dead link — the page 404s, so there's nothing to read. The title suggests a repo collecting free books, and the name reads like a Chinese free-book aggregation project (免费书籍汇总). Beyond that, I'm not going to invent what's in it. If you want free programming books, the ebookfoundation/free-programming-books repo is the one everyone actually uses. 📚

## 5. 3DGS Render brings Gaussian splats into Blender's native workflow — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/kiri-innovation/3dgs-render-blender-addon)

**Source:** https://www.opensourceprojects.dev/post/fcfdb840-5a3b-45b2-ae3d-a145036b4c3f
**Karakeep doc:** `w26nb76qyj54afz06gttki51`

A free Blender add-on from KIRI Engine that pulls 3D Gaussian Splat `.ply` files straight into the native viewport, so you can edit splats with Blender's own selection, modifier, and cropping tools instead of wrestling an external format. Two modes: an editable mesh workflow and a faster render mode. Experimental extras include Eevee shadow proxies, baked rigged splat animation, and lighting bakes. It's moving to community-led maintenance, and the README is refreshingly honest that the experimental stuff may break across GPUs and Blender versions. 🎨

## 6. TiTiler: dynamic tiling with FastAPI and Rasterio/GDAL, now split into modular packages — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/developmentseed/titiler)

**Source:** https://www.opensourceprojects.dev/post/36e22f25-3b79-4863-acff-c415a8cbefe8
**Karakeep doc:** `pdf19kdmepwhiueycfurkz12`

TiTiler (pronounced "tee-tiler") is a set of Python modules for building dynamic tile servers on FastAPI + Rasterio/GDAL — point it at a Cloud Optimized GeoTIFF and it slices out only the tiles clients actually request, no pre-rendering thousands of static PNGs. Since 0.3.0 it's split into `titiler.core`, `titiler.xarray`, and `titiler.extensions` so you don't install a pile of deps you'll never use. Supports JPEG/PNG/WEBP/GeoTIFF output, WMTS and OGC Tiles API, and ships Lambda/ECS/Helm deployment examples. If you're serving raster data over the web, this beats the pre-processing grind. 🗺️

## 7. LangGraph gives you durable execution and human-in-the-loop for stateful agents. — by Open-source Projects

![Open-source Projects](https://www.opensourceprojects.dev/favicon.ico)

**Source:** https://www.opensourceprojects.dev/post/cb0fe33c-4d08-44e4-85e9-2e6317afd37c
**Karakeep doc:** `jvkcrakgufzxbhsggi568egi`

The source page 404s, so no body to work from. The title is basically LangGraph's own elevator pitch: durable execution (agents that survive failures and resume where they left off) plus human-in-the-loop (pause and inspect agent state mid-run) for stateful agents. It's LangChain's orchestration runtime, and the title is accurate as far as it goes. Nothing more to add without the actual post. 🤖

## 8. Contractsforbase — by Open-source Projects

![Open-source Projects](https://www.opensourceprojects.dev/favicon.ico)

**Source:** https://www.opensourceprojects.dev/post/ce42b83d-a25b-4390-a34d-62d4702fb081
**Karakeep doc:** `ijgvst8faavudsvk9rg5s5n8`

Dead link — 404, no body. The title suggests a collection of smart contracts for Base, Coinbase's L2. That's the entire extent of what I can honestly say about it. No GitHub link survives on the page to confirm the repo, so I'm not going to guess the owner or what the contracts actually do. 🪦

## 9. PEV2: a VueJS rewrite of the abandoned Postgres Explain Visualizer — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/dalibo/pev2)

**Source:** https://www.opensourceprojects.dev/post/889ad7f1-c0cb-45c9-9cf6-0a709386bb7f
**Karakeep doc:** `hnw669t2umv1j0qst52ov805`

PEV2 is a Vue 3 rewrite of the dead Postgres Explain Visualizer (pev), which sat abandoned for three years with open PRs rotting. Dalibo picked it up and turned `EXPLAIN` output into an interactive node-and-connection diagram instead of that wall of `cost=12.50..12.51 rows=1` gibberish. The killer feature is a single self-contained `pev2.html` you can double-click offline — no npm, no server, no CDN. It's a drop-in component (two props: `plan-source` and `plan-query`) or a hosted service at explain.dalibo.com, and it's refreshingly honest that it needs Bootstrap 5 CSS. If you've ever had to explain to a human why a query is slow, this is worth a look.

## 10. Zig has moved from GitHub to Codeberg—and it's not mirrored. — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/ziglang/zig)

**Source:** https://www.opensourceprojects.dev/post/34a39a3b-f89d-4dae-bdec-ef837c9ec7dc
**Karakeep doc:** `gc063qml1l4bi8n81ef3futx`

⚠️ Stub — the source page on opensourceprojects.dev returns a 404, so there's no body to summarize. The title alone tells the story: the Zig project has moved its primary repo off GitHub to Codeberg, and it's a clean cut, not a mirror. That's a real signal about where the language's maintainers are putting their trust. Nothing else to report — the post is gone.

## 11. Utility-first CSS for building custom interfaces without leaving your HTML — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/tailwindlabs/tailwindcss)

**Source:** https://www.opensourceprojects.dev/post/22acd280-b83e-4577-a754-76bd3e95c5c1
**Karakeep doc:** `b0i43eu046z8fa93q0huhhtz`

⚠️ Stub — the source page on opensourceprojects.dev returns a 404, so there's no body to summarize. The title is a textbook description of Tailwind CSS: utility-first classes you slap straight into your HTML instead of writing a separate stylesheet. That's the whole pitch, and it's not exactly news in 2026. Nothing else to report — the post is gone.

## 12. Read the damn docs — by Brodie Robertson

![Brodie Robertson](https://i.ytimg.com/vi/jiBb3JbQoVU/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/jiBb3JbQoVU
**Karakeep doc:** `g6flkdsvsg3l683byhban85j`

Brodie's take is clichéd but still true: read the documentation. He points out you've got zero excuse now, because AI tools can synthesize docs into tutorial form and cite exactly where each point comes from. But the docs are still the main source of truth — not the absolute one, that's the source code, since docs can go stale. Most people just never bother diving into the code anyway.

## 13. CrochetPARADE – crochet pattern renderer, analyzer and debugger - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/06/Linux-Home-Embroidery.png)

**Source:** https://www.linuxlinks.com/crochetparade-crochet-pattern-renderer-analyzer-debugger/
**Karakeep doc:** `t3nomzrvxp6hxfx7fjmpb3j2`

CrochetPARADE is a platform for creating, visualizing, and analyzing 2D and 3D crochet patterns using a purpose-built pattern language instead of ambiguous natural-language instructions. It parses and checks your pattern for structural correctness, then renders an interactive virtual model you can rotate, zoom, and animate to see how stitches connect before you waste yarn on a physical project. It flags stitches that look too loose or tight, exports SVG charts and Blender-ready 3D models, and does all the math locally on your device. Written in JavaScript (three.js + SVG.js), GPL v3, and it can chew through patterns with tens of thousands of stitches.

## 14. 17 Best Free and Open Source Web-Based Bookmark Managers - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/01/019-bookmark.png)

**Source:** https://www.linuxlinks.com/best-free-open-source-web-based-bookmark-managers/
**Karakeep doc:** `mbns6d8pgllt9y0tq5z9z7f9`

Mozilla killed Pocket last year, and since it was never open source, everyone had to migrate — so LinuxLinks rounds up 17 open source web-based bookmark managers. The usual suspects are all here: Linkwarden, Karakeep (the "bookmark-everything app with a touch of AI"), Shiori, linkding, wallabag, Shaarli, LinkAce, and a pile of others. It's a ratings-chart roundup with a portal page per tool, and it's the web-based companion to their separate CLI and GUI bookmark manager roundups. If you're still mourning Pocket, there's a self-hosted replacement for every taste here.

## 15. 16 Best Free Linux Screen Capture GUI Tools - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2022/09/screen-capture.jpg)

**Source:** https://www.linuxlinks.com/screencapture/
**Karakeep doc:** `gfrpgnx90qrb490vkjirgez1`

LinuxLinks rounds up 16 GUI screen capture tools, because GNOME and KDE's built-in screenshot utilities are competent but basic. The list runs the gamut from Spectacle and Ksnip to flameshot, Shutter, swappy, and a bunch of Wayland-native newcomers like shotman and wayscrollshot. GIMP and ImageMagick sneak in too, since they can capture screens despite being image editors first. It's a ratings-chart roundup confined to GUI tools, with a separate roundup for the CLI crowd.

## 16. Postgres Tips - Replace Your Entire Stack — by Better Stack

![Better Stack](https://i.ytimg.com/vi/0crLijqR40U/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/0crLijqR40U
**Karakeep doc:** `o4ue66nudhjql4ppinm3px0z`

Better Stack argues you can ditch Redis and Elasticsearch by leaning on Postgres features you already have. For caching, use `UNLOGGED` tables — they skip the write-ahead log for drastically faster writes and get auto-wiped on crash, which is exactly the behavior you want from a cache anyway. For full-text search, use a `TSVECTOR` column with a GIN index: Postgres splits text into searchable chunks, strips stopwords, and stems words down to roots so "jump" matches "jumping" and "jumped". The punchline: your five-user app probably doesn't need a separate cache or search cluster.

## 17. 7 Best Free and Open Source Climate, Weather and Earth-Science Data Analysis Tools — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2023/11/wooden-pier-sea-with-city-seattle-usa-beautiful-clouds.jpg)

**Source:** https://www.linuxlinks.com/climate-weather-earth-science-data-analysis-tools/
**Karakeep doc:** `cf9xwnm8o7k0hxuu1fxu37il`

LinuxLinks rounds up seven free, open-source tools for crunching climate, weather, and Earth-science data. The usual suspects are all here: GrADS for grid analysis, ncview for eyeballing NetCDF files, MetPy for weather calculations, VAPOR for 3D atmospheric viz, NCO for netCDF manipulation, Metview for meteorological workflows, and wradlib for weather radar. If you're drowning in temperature, pressure, and precipitation datasets and don't want to pay for a proprietary stack, this is your shopping list. 🛰️

## 18. Image Optimizer - fast private image optimization — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2023/10/image-compression-2914476.jpg)

**Source:** https://www.linuxlinks.com/image-optimizer-fast-private-image-optimization/
**Karakeep doc:** `kdlbdomg56rb55h80kwfruh5`

Image Optimizer is a TypeScript desktop app that compresses JPEG, PNG, GIF, and SVG locally — no cloud, no uploads, your files never leave the machine. It does batch optimization, recursive folder scanning, WebP conversion, metadata stripping, and a before/after preview so you can see what you're losing. MIT-licensed, by Anton Reshetov. If you're tired of sketchy online "compress my image" sites, this is the boring-but-correct answer. 🖼️

## 19. How OpenTelemetry Works: A Complete Guide — by freeCodeCamp.org

![freeCodeCamp.org](https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/32307170-27b3-463c-bae9-da3dbfd2a634.png)

**Source:** https://www.freecodecamp.org/news/how-opentelemetry-works/
**Karakeep doc:** `qxbtp0kj1halidn2m66za7u1`

A genuinely useful end-to-end walkthrough of OpenTelemetry, from instrumenting your app to seeing traces in a backend. It breaks the pipeline into eight steps — instrumentation, telemetry signals (traces/metrics/logs), spans, context propagation, the SDK, exporters, the Collector, and the observability backend — with actual Node.js code snippets. The key takeaway: you don't need every component, and the Collector is optional until you actually need it. Solid reference if you've been nodding along whenever someone says "Otel" without really knowing what it does. 📊

## 20. CloakBin - zero-knowledge encrypted pastebin — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/01/026-coding.png)

**Source:** https://www.linuxlinks.com/cloakbin-zero-knowledge-encrypted-pastebin/
**Karakeep doc:** `ozpippt9hxqio3650q34y24a`

CloakBin is a self-hosted pastebin that encrypts and decrypts everything in the browser, so the server only ever stores ciphertext. The decryption key lives in the URL fragment, which never gets sent to the server — that's the zero-knowledge trick. Built with SvelteKit and TypeScript, it's got AES-256-GCM, optional PBKDF2 password protection, burn-after-reading, a CLI, and an HTTP API. AGPL-3.0, by Ishan Naik. A PrivateBin alternative for people who want to share secrets without the host being able to read them. 🔐

## 21. Nvidia Wants to Turn Your Idle PCs Into a Personal Home Data Center With 'PAIR' — by PCMag UK

![PCMag UK](https://sm.pcmag.com/t/pcmag_uk/news/n/nvidia-wan/nvidia-wants-to-turn-your-idle-pcs-into-a-personal-home-data_uepa.1200.jpg)

**Source:** https://uk.pcmag.com/ai/167106/nvidia-wants-to-turn-your-idle-pcs-into-a-personal-home-data-center-with-pair
**Karakeep doc:** `mx5fap8wt00vn07g1tmxtcze`

Nvidia's PAIR — "Personal AI Router" — is a free, open-source tool announced at IFA 2026 that links your idle laptops, desktops, and Macs into a coordinated home cluster for running agentic AI locally. It's an AI router, not a VRAM pooler: it breaks a task into sub-tasks and farms them out to sub-agents across your machines in parallel, rather than splitting one model across boxes. The pitch is no subscription fees and no cloud privacy risk for your personal files. Clever, but let's see if it survives contact with a house full of half-dead Chromebooks. 🤖

## 22. LyargoOS – opinionated Void Linux-based distribution — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/04/Linux-Distributions.png)

**Source:** https://www.linuxlinks.com/lyargoos-opinionated-void-linux-based-distribution/
**Karakeep doc:** `o8gnbsoe4jyz352s1ptorvby`

LyargoOS is an opinionated Void Linux spin that ships a ready-to-use desktop so you don't have to build one from scratch. KDE Plasma is the flagship, with Xfce and GNOME as alternatives, runit as init, Calamares for graphical install, and a custom XBPS wrapper that mimics apt/pacman commands. It bundles zsh, Neovim, tmux, fzf, PipeWire, and even fcitx5 with Rime for Chinese input. For the "I want Void's rolling-release simplicity but not the DIY pain" crowd. 🐧

## 23. Noisekun - ambient sounds for relaxation and productivity — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2021/09/abstract-background-with-sound-waves-design.jpg)

**Source:** https://www.linuxlinks.com/noisekun-ambient-sounds-relaxation-productivity/
**Karakeep doc:** `ebx71i8sxmj9kqa8d1l2bjln`

Noisekun is a browser-based ambient sound mixer with 23 sounds — rain, waves, wind, birds, colored noise — that you can layer into custom soundscapes. Individual volume controls, saveable/shareable combos, seven themes, and a Pomodoro timer with persistent settings. MIT-licensed, by Mateus Felipe Gonçalves. A no-install Blanket alternative for when you need to drown out the open-plan office. 🎧

## 24. Omarchy Can Do WHAT?! 50 Features You're Missing — by NetworkChuck

![NetworkChuck](https://i.ytimg.com/vi/2IDjteRQgMQ/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=2IDjteRQgMQ
**Karakeep doc:** `xxhdlzglboj3kjsyh5ypgxlx`

NetworkChuck speedruns fifty Omarchy (Omachi) features in one five-hour recording session, from keybindings and tiling workspaces to scratchpads, web apps, and one-command package installs. The meaty bits: local AI agents (Claude, Codex, Copilot, Gemini, Grok) that can actually reconfigure your OS, a local Whisper-style transcription tool called Vox Type, LocalSend for AirDrop-style file sharing, and building a coffee-counter plugin with AI and shipping it to the marketplace. He also plugs ThreatLocker hard for locking down AI agents in the enterprise, because letting Claude roam free on your work machine is a terrible idea. ☕

## 25. Lenovo Yoga Pro 9n: RTX Spark with 128 GB Unified Memory — by igor´sLAB

![igor´sLAB](https://www.igorslab.de/wp-content/uploads/2026/09/7db89308-827f-4822-bd08-e05a2aa4931d.jpg)

**Source:** https://www.igorslab.de/en/nvidia-rtx-spark-laptop-lenovo-up-to-128-gb-unified-memory/
**Karakeep doc:** `cu6bdmw5po0m7zatkspxunf4`

NVIDIA is finally shoving its RTX Spark platform into laptops, and Lenovo's the first to bite. The Yoga Pro 9n packs a Grace CPU (up to 20 cores) and a Blackwell GPU (up to 6,144 CUDA cores) on one Arm SoC, both slurping from a shared LPDDR5X pool at 9,400 MT/s — up to 128 GB of unified memory, which is the whole point: run big local AI models without a chunky workstation. The 15.3" OLED hits 1,100 nits and 165 Hz, weighs a claimed 1.65 kg, and sips 80 W max. No prices, no independent benchmarks yet — first units land October 2026, so hold your damn horses.

## 26. The Best Nintendo DS Flash Cart Just Got Way Better — by Macho Nacho Productions

![Macho Nacho Productions](https://i.ytimg.com/vi/_GSlKA4cl3c/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=_GSlKA4cl3c
**Karakeep doc:** `z80hpc2pmg2k6xy4h9c748ip`

Tito's back with the DSPO IR, the upgraded version of the open-source Raspberry Pi Pico flash cart that already dethroned the R4. The new one swaps in a Pico 2 (RP2350), jumps from 264 KB to 8 MB of RAM, adds USB-C, and — the headline — real infrared support, so Pokémon HeartGold/SoulSilver can finally talk to a Pokéwalker. The extra grunt also enables real-time "seekable compression" that shrinks a 256 MB Pokémon White ROM to 78 MB with no in-game lag, and it draws up to 1/8th the power of the original. Pre-orders are open at ~$30, shipping mid-November, and there's a $25 Pico Walker coming too.

## 27. Pixelitor - advanced image editor with non-destructive editing - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2022/05/Google-Drawings.png)

**Source:** https://www.linuxlinks.com/pixelitor-advanced-image-editor-non-destructive-editing/
**Karakeep doc:** `v7gw1tz3crj0dasns3wqqf4a`

Pixelitor is a Java raster image editor that leans hard into non-destructive editing — layers, layer masks, smart objects, smart filters, adjustment layers, the works. It's got 110+ filters, unlimited undo, and can even build animations from layers with tweening. Native PXC format keeps your layer structure intact so you can come back and keep editing instead of flattening to a bitmap. Free, GPLv3, by László Balázs-Csíki.

## 28. 10 Best Free and Open Source Linux Project Management Software - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2019/03/project-management.jpg)

**Source:** https://www.linuxlinks.com/projectmanagement/
**Karakeep doc:** `adaof549lc8an9kih5e4gfrn`

LinuxLinks' roundup of free/open-source project management tools, with Gantt charts front and center as the industry standard. The list runs ProjectLibre (the MS Project replacement), Planify, GanttProject, Taskjuggler, Kanri, Planner, Calligra Plan, FlowInquiry, Scrumlens, and Schedule. Web-based PM tools got punted to a separate roundup, so this is all desktop/standalone stuff. Standard LinuxLinks fare — a ratings chart and a table, nothing revolutionary.

## 29. Avahi - service discovery for Linux - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2017/10/Configuration-Management.jpg)

**Source:** https://www.linuxlinks.com/avahi-service-discovery-linux/
**Karakeep doc:** `jy3urv70b9ahzwx9otltuy2m`

Avahi is the zero-config networking stack that implements DNS-SD over mDNS — the same protocol family as Apple Bonjour, so devices find each other without a central DNS server. It ships a daemon, client libs, CLI tools (avahi-browse, avahi-resolve, avahi-publish), a GTK browser, and even Bonjour libdns_sd compatibility shims. Targets Linux, with BSD and illumos support, LGPLv2.1, written in C.

## 30. Your Domain Could Be Deleted — by Better Stack

![Better Stack](https://i.ytimg.com/vi/sN-la5chrFU/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/sN-la5chrFU
**Karakeep doc:** `yki2hxkr51by2kqjsv44g2je`

Your fancy .ai or .su domain can just get deleted and there's fuck-all you can do about it. Neil Fraser registered neil.fraser.name 25 years ago and paid through 2040, then ICANN approved destroying the entire third level of .name in July 2026 — so someone can now grab fraser.name and squat neil.fraser as a subdomain pointing at a malicious service. Over 22,000 people hold .xy domains and will lose them with little notice. And .io, .ai, .su are all owned by countries — .su is already being retired for 2030, .io is shaky after the UK handed the Chagos Islands to Mauritius, and .ai only survives because it funds ~47% of Anguilla's budget. Build your next unicorn on a domain you actually control.

## 31. What Makes CachyOS So Popular — by Brodie Robertson

![Brodie Robertson](https://i.ytimg.com/vi/y0R5V4hDHwg/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=y0R5V4hDHwg
**Karakeep doc:** `wjgvakq9ki1p7turbn8y9368`

Brodie digs into why CachyOS is the #2 distro on the Steam Hardware Survey (behind SteamOS, ahead of Arch). His take: the "blazingly fast, CPU-optimized, custom scheduler" marketing is mostly placebo — nobody actually verifies the benchmarks, and ~95% of the real gaming gains come from CachyOS's Proton build, which you can run on any distro. The real draw is being Arch-based (fresh drivers, AUR access, SteamOS adjacency), a convenient Calamares installer with easy NVIDIA driver setup, and a self-reinforcing popularity feedback loop. He still wouldn't hand a rolling release to a first-timer.

## 32. ALTCHA – privacy-first CAPTCHA alternative - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/CAPTCHA-banner.png)

**Source:** https://www.linuxlinks.com/altcha-privacy-first-captcha-alternative/
**Karakeep doc:** `mykxp6ge90z7dcfa8cvlz4vk`

ALTCHA is a self-hosted CAPTCHA alternative that uses browser-based proof-of-work instead of "click the traffic lights" puzzles. No tracking, no fingerprinting, no data collection, and you can run the whole thing yourself without an external service. Ships as a Web Component with PBKDF2/SHA/Argon2id/Scrypt challenge algorithms, Web Worker offloading, WCAG accessibility, and server libs for TypeScript, Go, Python, PHP, Java, Ruby, Rust, Dart, Elixir and more. MIT licensed.

## 33. MAZANOKE - private browser-based image optimizer — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/MAZANOKE-example.jpg)

**Source:** https://www.linuxlinks.com/mazanoke-private-browser-based-image-optimizer/
**Karakeep doc:** `cbbbk4c8pb41ca7th76ohhl5`

MAZANOKE is a self-hosted image optimizer that runs entirely in the browser — no uploads, no cloud, your files never leave the machine. It handles JPG/PNG/WebP/ICO conversion, imports HEIC/AVIF/TIFF/GIF/SVG, strips EXIF, and works offline as an installable PWA. GPLv3, JavaScript, runs from static files or Docker. If you're tired of shoving photos through some sketchy web compressor, this is the "fuck it, I'll do it myself" answer.

## 34. Home — by OpenGitOps

![OpenGitOps](https://opengitops.dev/favicon.ico)

**Source:** https://opengitops.dev/
**Karakeep doc:** `dugtu7b33ckagwffoedvkrv3`

OpenGitOps is the CNCF-adjacent standards body that turned GitOps from a buzzword into four actual principles: declarative, versioned & immutable, pulled automatically, continuously reconciled. It's the spec behind Argo and Flux, with a v1.0.0 document and a pile of Kelsey Hightower quotes to make you feel warm inside. If you've ever wondered why your cluster config lives in git and reconciles itself, this is the canonical answer.

## 35. Linux ip command — by Thomas-Krenn.AG

![Thomas-Krenn.AG](https://www.thomas-krenn.com/favicon.ico)

**Source:** https://www.thomas-krenn.com/en/wiki/Linux_ip_command
**Karakeep doc:** `h6hgsudd8kl2str7dekoyyhm`

The `ip` command from iproute2 is the modern replacement for the long-dead `ifconfig`, and this wiki page is a clean cheat sheet for it. It maps every old net-tools command to its `ip` equivalent — `ip a`, `ip r`, `ip n`, `ip link show` — with real output examples. If you still type `ifconfig` out of muscle memory, this is your intervention.

## 36. List and Manage Linux Services with systemctl — by Contabo Blog

![Contabo Blog](https://contabo.com/blog/wp-content/uploads/2026/05/blog-head_linux-systemctl-command.webp)

**Source:** https://contabo.com/blog/list-and-manage-linux-services-with-systemctl/?utm_source=google&utm_medium=cpc&utm_campaign=brand-pmax-global&utm_term=&utm_content=&gad_source=1&gad_campaignid=23237090875&gbraid=0AAAAAD_Qy-elCk_d5NryPEj9eiPon5Kkc&gclid=Cj0KCQjwhsrUBhDxARIsAN3AQSdFEc-cAD9BlRICMMF-cIG9wHSdiyLbirZRaUNhgIgMcQ9i0a0fjxoaAjCUEALw_wcB
**Karakeep doc:** `vw7squsg386ezc6ld8ym07kr`

A solid systemctl walkthrough: listing units, filtering by state, start/stop/restart/reload, enable/disable, and reading journalctl. The useful bits are the five service states (enabled, disabled, masked, static, failed) and the reminder that `reload` beats `restart` for nginx because restart drops connections. The opening line — "a server with 40 running services and no idea which ones are needed is a security incident waiting to happen" — is the whole reason to bookmark this.

## 37. K3s — by Rancher

![Rancher](https://k3s.io/img/rancher-suse-logo-horizontal-color.png)

**Source:** https://k3s.io/
**Karakeep doc:** `q29j1c6um3ohisr5uvpqqkug`

K3s is the certified Kubernetes distro for edge, IoT, and ARM — a single <70MB binary that installs with one curl and gives you a working cluster in ~30 seconds. It's Rancher/SUSE's answer to "Kubernetes is too fat for a Raspberry Pi," and it's a CNCF sandbox project. If you want k8s without the k8s baggage, this is the default choice.

## 38. GitHub - croffasia/itsaplan — by GitHub

![GitHub](https://github.com/croffasia/itsaplan/raw/main/assets/banner.png)

**Source:** https://github.com/croffasia/itsaplan
**Karakeep doc:** `ke955lgsa4ok97s3p7kvalda`

It's a Plan is a self-hosted, AGPL-3.0 alternative to Linear/Jira/Plane where AI agents are first-class teammates — you give one a model, prompt, skills, and tools, then assign it an issue on the same board as your humans. Internal agents run on-instance via Mastra, external ones run on your machine through Claude Code/Codex/opencode, and everything is exposed over REST, MCP, and webhooks. 448 stars, active as hell, still pre-1.0 so expect breaking changes. The "agents as teammates, not a separate pipeline" angle is the interesting bit.

## 39. Xiaomi POCO X3 NFC (xiaomi-surya) — by postmarketOS Wiki

![postmarketOS Wiki](https://wiki.postmarketos.org/images/thumb/2/20/Xiaomi-surya.png/200px-Xiaomi-surya.png)

**Source:** https://wiki.postmarketos.org/wiki/Xiaomi_POCO_X3_NFC_(xiaomi-surya)#Installation
**Karakeep doc:** `y9247f0is23k1rsbjl9oob04`

The postmarketOS device page for the POCO X3 NFC (Snapdragon 732G, codename surya), now a generic port under qcom-sm7150 with a mainline kernel. Status is mostly green — screen, touch, WiFi, BT, NFC, calls, SMS, mobile data all work — but camera, GPS, fingerprint, and IR are broken, and battery is partial. Flashing works, and there's a note about a SIM-unlock quirk on slot 1. If you've got one of these in a drawer, it's a legit pmOS candidate.

## 40. GitHub - tt-a1i/archify — by GitHub

![GitHub](https://github.com/tt-a1i/archify/raw/main/docs/assets/archify-readme-hero.png)

**Source:** https://github.com/tt-a1i/archify
**Karakeep doc:** `trmpn3ioj1zwtbj6e7ja54e4`

Archify is an agent skill that turns a codebase or system description into a polished, interactive architecture/workflow/sequence diagram — agents emit typed JSON IR, and Archify deterministically compiles it into self-contained HTML/SVG with motion and crisp PNG/WebM export. It's for Cursor, Claude Code, Codex, and OpenCode, MIT-licensed, and sitting at a frankly absurd 49.4k stars. The "verifiable" angle is the hook: it diffs two snapshots as Before/Delta/After and won't let you invent topology.

## 41. GitHub - petergyang/no-ai-slop: Removes 20+ patterns of AI slop from any piece of writing. — by GitHub

![GitHub](https://github.com/favicon.ico)

**Source:** https://github.com/petergyang/no-ai-slop
**Karakeep doc:** `nib3b5yt0i2cyo0q9xusit50`

A skill that strips 20+ AI-slop patterns out of your writing without flattening your actual voice. It catches the usual crimes — "It's not X. It's Y.", "What nobody tells you is…", "The future isn't coming. It's already here." — plus weasel attribution like "experts agree" and fake-profound endings. Install it with one paste into ChatGPT, Claude Code, or Codex, or via `npx skills add`. 7.3k stars and MIT-licensed, so it's clearly scratching an itch a lot of people have. It can even generate the most cringe slop possible on purpose, for satire. 😏

## 42. SDNS – recursive DNS resolver with DNSSEC validation - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2023/01/System-Admin.jpg)

**Source:** https://www.linuxlinks.com/sdns-recursive-dns-resolver-dnssec-validation/
**Karakeep doc:** `nh1wx752gg3vy6x9ge5runwy`

A Go-based recursive DNS resolver that does its own iterative resolution from the root instead of leaning on someone else's resolver. It's aimed at operators who want to run their own thing while keeping modern security and privacy — DNSSEC validation, QNAME minimisation, DoT/DoH/DoQ, and a configurable policy layer. Also ships metrics, an HTTP API, dnstap, and a "recursion firewall" to cap how much work a single request can trigger. MIT-licensed, by Semih Halev. Solid pick if you're tired of trusting your ISP's DNS. 🛡️

## 43. Noctalia 5 Wayland Desktop Shell Is Now Officially Stable — by Linuxiac

![Linuxiac](https://cdn.shortpixel.ai/spai/q_lossy+ret_img+to_auto/linuxiac.com/wp-content/uploads/2026/09/noctalia50-1024x576.jpg)

**Source:** https://linuxiac.com/noctalia-5-wayland-desktop-shell-is-now-officially-stable/
**Karakeep doc:** `mvtw50rdi77ud68osy8jp0b4`

Noctalia 5 hit stable with 5.0.1, closing out its testing and beta phase. It's a Wayland desktop shell packing the usual suspects — panel, widgets, launcher, notifications, control center, wallpaper controls. New in this release: local vdir calendar support with vdirsyncer, an MRU window-switcher mode, and a pile of polish on Bluetooth pairing, fractional scaling, and blur for wayland-protocols 1.45. The privacy indicator can now even spot screen capture through xdg-desktop-portal-wlr. 🖥️

## 44. Noctalia - A Family of Native Wayland Projects — by Noctalia

![Noctalia](https://assets.noctalia.dev/noctalia-logo.svg)

**Source:** https://noctalia.dev/
**Karakeep doc:** `im6zwh7m2kfp18ugtc64ahtj`

Noctalia is actually three projects sharing one look and palette: the desktop shell (stable, v5), Umbriel the Wayland compositor (young, moving fast), and a greetd login screen that mirrors your wallpaper and font so boot looks consistent. The pitch is "quiet by design" — a clean, distraction-free desktop that gets out of your way. Claims 7+ supported compositors, 165+ plugins, and 137+ releases since July 2025. Run all three or just drop in the piece your setup is missing. 🌙

## 45. Fedora Media Writer - create bootable USB installation media - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2021/01/FlashOS.png)

**Source:** https://www.linuxlinks.com/fedora-media-writer-create-bootable-usb-installation-media/
**Karakeep doc:** `pglv6fxsw5jrglpfm7jpveu0`

Fedora's recommended GUI tool for writing bootable USB install media, written in C++ and QML. It downloads Fedora images directly, verifies them, writes with direct device access, then reads the image back off the USB to confirm the write actually worked. Also handles custom ISOs for other OSes and has a Restore function to return a drive to a normal single-partition layout. Cross-platform — Linux, Windows, macOS. GPL v2.0. A boring-but-solid utility that does one job and verifies its own work. 💾
