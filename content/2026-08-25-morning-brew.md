---
title: Morning Brew — 2026-08-25
date: 2026-08-25
slug: 2026-08-25-morning-brew
tags: AI Agents, API Integration, Apple, Apple Silicon, Arch Linux, Artificial Intelligence, Banking, Blockchain, Career Advice, Career Change, Command Line Interface, Command Line Tools, Commodore 64, Computer Hardware, Computer Vision, Computing, Credit Cards, Cryptocurrency, Cyberpunk 2077, Cybersecurity, Deep Learning, DevOps, Developer Tools, Docker, File Downloads, Frameworks and Libraries, Gaming Hardware, Generative AI, Google Drive, Hardware Engineering, Hyprland, Image Generation, Job Search, Kubernetes, Large Language Models, Leadership, Linux, Mac Mini, Mac Studio, Machine Learning, Malware Analysis, Management, Money Management, Multi-Agent Systems, OAuth Tokens, Open Source, Open Source Software, Operating Systems, Personal Finance, Private Cloud Compute, Productivity Tools, Programming Languages, Python, Retro Computing, Reverse Engineering, Reverse Proxy, Rust Programming Language, SSL Certificates, Self-Hosting, Semiconductors, Software Configuration, Software Development, Software Engineering, Software Security, Systems Thinking, Technology Careers, Technology Interviews, Terminal Navigation, Video Generation, Web Servers, Web3
---

# Morning Brew — 2026-08-25

A 20-item hoard from Tuesday, August 25th: 4 YouTube videos (now transcribed) and 16 articles. Heavy on the Omarchy/Arch-Linux hype cycle (DHH's interview, Brodie's rebuttal, the Apple Silicon port), a big Apple hardware day (M6/M5 Ultra Macs, Private Cloud Compute photos), and a stack of open-source dev-tool posts. The recurring thread: everyone's building AI agents that coordinate other AI agents, and Apple is quietly becoming the local-AI hardware king.

## 1. CDPR and Commodore Are Releasing a Cyberpunk 2077-Themed Commodore 64 Computer Called the Commodore 77 — by IGN

![IGN](https://assets-prd.ignimgs.com/2026/08/25/commodore-77-01-1787668050455.png?width=1280&format=jpg&auto=webp&quality=80)

**Source:** https://www.ign.com/articles/cyberpunk-2077-commodore-computer-reveal-gamescom-2026
**Karakeep doc:** `n5i193gztp9001o92o5jpa7y`

Commodore and CD Projekt Red are teaming up on the Commodore 77, a Cyberpunk 2077-themed follow-up to the C64 Ultimate (which IGN gave a 10). The case gets a weathered cyberpunk look with a real brushed-metal plate on the function keys, a Commodore 77 badge, and LED lights that dance to the demo music. Inside it's a serious spec bump: 77MHz (vs. the original C64's 1MHz) and 77MB of RAM (vs. the Ultimate's 16MB) — fast enough that your hand-written BASIC programs might run "impossibly fast," so you can toggle the speed down. It ships with a Cyberpunk-themed BASIC 2.0 boot screen, a lore-packed spiral-bound manual with type-in programs, and an Arasaka cartridge containing a demo by Polish demo group Arise with a chiptune soundtrack by LukHash (benefiting from the 24-track stereo SID chip). Preorders are live at $377, shipping sometime next year. Verdict: retro-futurist collector bait, but the demo cart and the SID soundtrack are genuinely the kind of thing old heads will lose an afternoon to.

## 2. New Macs and More: Here's Everything Apple Announced Today — by MacRumors

![MacRumors](https://images.macrumors.com/t/8b1-Ufc2jCCfy7pwognAoZn8nLE=/1600x/article-new/2026/08/Apple-New-Macs-and-Polishing-Cloth.jpg)

**Source:** https://www.macrumors.com/2026/08/25/everything-apple-announced-today/
**Karakeep doc:** `sqmk9g178oowvvuzmtvqxa1v`

Apple's big Tuesday drop: a new Mac mini with M6 and M5 Pro chip options, a new Mac Studio with M5 Max and M5 Ultra, a cheaper Polishing Cloth, and quietly refreshed Magic Keyboards. The headline silicon is the M6 — Apple's first-ever 2nm chip — and the M5 Ultra, billed as the most powerful chip Apple's ever made. The Mac mini and Mac Studio are up for preorder today with deliveries starting September 22; the Polishing Cloth and keyboards are available immediately. The comment section is predictably salty about the $899 base Mac mini still shipping 256GB in 2026, and there's a running joke about leasing the Polishing Cloth. Verdict: a hardware refresh day, with the 2nm M6 being the genuinely notable bit — and Tim Cook's final product announcement reportedly looming.

## 3. Is Linux the perfect operating system? - Omarchy interview with DHH — by NetworkChuck

![NetworkChuck](https://i.ytimg.com/vi/_CuibYl_Fh0/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=_CuibYl_Fh0
**Karakeep doc:** `ar4vrr4yabnaeu7ygs9vr89a`

NetworkChuck interviews DHH (David Heinemeier Hansson) about Omarchy, his "preconfigured, computer-lover-targeted" Linux distro. DHH's pitch: he spent ~3,000 hours over the past year building the "perfect OS" so nobody else has to — Arch + Hyprland tiling window manager + Quickshell, all pre-rice'd, installable in under a minute (he's clocked 56 seconds on a Framework 13 Pro with a Panther chip). The whole thing is unapologetically keyboard-driven (super+W closes a window, no mouse-hunting for the X), and he's all-in on AI: Omarchy Quatro ships crash-diagnosis skills that hand off to your agent harness, and he's merged 1,000+ PRs in ~90 days, partly by letting agents do the work. He demoed an agent translating a Python screensaver library to Rust — 27x faster, 2ms launch, and it now merges its own PRs and cuts releases. He runs a multi-machine setup via GL.iNet KVM boxes + Tailscale + Herder (a tmux-like agent-aware terminal). Verdict: a genuinely infectious hype pitch for a "malleable computer," with the honest caveat that it's for people who love computers, not people who just want one to work.

## 4. Omarchy Is Not A Real "Distro" — by Brodie Robertson

![Brodie Robertson](https://i.ytimg.com/vi/yIA4idIdY_k/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=yIA4idIdY_k
**Karakeep doc:** `ycevwmwus653ddwj1lwlbxr2`

Brodie pushes back on the "Omarchy is just config files" crowd after the Omarchy Foundation landed $8M (now $10M, with Drew Houston of Dropbox and Peter Steinberger of OpenClaw each adding $1M). His argument: a year ago, sure, it was Arch + a post-install script + a rice. But since then it's gained a dedicated mirror of the Arch repos with Stable/RC/Edge/Dev update channels, its own packages repo (AUR-style bins like 1Password beta, Cursor), first-party apps (Omarite editor, Oma Track motorsport analysis, Oma Snap, Oma Calc), kernel patches, and even its own zero-day exploits. If CachyOS, Manjaro, and EndeavourOS count as distros, so does Omarchy — consistency, please. But he's also blunt about the money: without Arch Linux, Omarchy doesn't exist, so some of that $10M should flow to Arch package maintenance and the volunteer projects it ships (GNU tools, systemd, Neovim, lazygit, OBS, etc.). He's glad Hyperland and Quickshell are now directly funded, but wants to see the rest allocated. Verdict: a fair "it's a distro now, but spend the money where it does good" take.

## 5. here's why you can't land a tech job no matter what you do. — by Mischa van den Burg

![Mischa van den Burg](https://i.ytimg.com/vi/QGMREKBP82w/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=QGMREKBP82w
**Karakeep doc:** `ypfgsmcixer96uuwyol1jyhl`

Mischa (a DevOps career coach who went from nurse to senior DevOps engineer, and runs CubeCraft) breaks down why people can't land tech jobs. His four mistakes: (1) focusing only on tech skills — they're maybe 30% of landing the job; the rest is soft skills, networking, and personal branding, because the hiring game is now flooded with auto-generated applications from around the world and a cold CV stack doesn't stand out. (2) Trying to do everything for free — he argues buying a course or paying a mentor is buying back your time, the most valuable resource (he cites the ~4,000 weeks of a life). (3) Bad goal-setting — "learn Kubernetes" isn't a goal; "run a web app on Kubernetes following industry best practices" is, and you need to learn how to study before you learn the tech. (4) No mentor — he credits his nurse-to-senior-engineer jump in ~5 years to mentors, and shares a raw personal story about asking for help to get sober (8 years clean). Verdict: a heavy dose of self-promotion for CubeCraft, but the core advice — tech skills alone won't get you hired, invest in yourself, get a mentor — is solid and delivered with real conviction.

## 6. International Cyber Digest (@IntCyberDigest) on X — by X (formerly Twitter)

![International Cyber Digest](https://pbs.twimg.com/media/HQgcsJtWcAEbmGL.jpg:large)

**Source:** https://x.com/IntCyberDigest/status/2091954008298491934
**Karakeep doc:** `rzabkel3jae96k7f78jaxgqr`

Photos have surfaced of what appears to be Apple's Private Cloud Compute hardware: custom PCBs built around official Apple M5 silicon, with Apple's custom heat spreaders, Apple Part Numbers on the service diagrams, and a modular blade/chassis design optimized for densely packing multiple low-power M5 chips for AI inference. Apple reportedly skipped the M3/M4 generations in its PCC infrastructure for better efficiency and performance, and the whole rack is orchestrated by a Mac Studio. The thread's a rare look inside Apple's actual server units — 105K views, 1.6K likes. Verdict: a peek at the hardware behind Apple Intelligence's private cloud, and a reminder that Apple's AI play is as much about custom silicon as it is about software.

## 7. How to let AI agents act on behalf of users without handing them access tokens — by WorkOS

![WorkOS](https://images.workoscdn.com/images/3b6999a3-68af-47d4-a9c3-04572333ddc4.png?auto=format&fit=clip&q=80)

**Source:** https://workos.com/blog/delegated-access-for-ai-agents
**Karakeep doc:** `sk7wdzbiohqybjhncu8feza1`

WorkOS's Maria Paktiti on why handing an OAuth token to an AI agent is a bad idea, and how to do delegated access instead. The core problem: an agent runtime erases the trusted-code/untrusted-input boundary — a GitHub issue, a scraped page, a PDF all land in the same context window as your system prompt. A single provider token in an agent runtime tends to end up in seven places: the context window, tool-call logs, model-provider logs, stdout/stderr, error payloads, scratch files/memory, and the exfiltration path itself. Scopes and rotation help less than you'd like (scopes are coarse, rotation shortens the window without closing it). Their answer is Relay: the agent sends its request to WorkOS, names the provider and user, and WorkOS attaches the credential on the way out — the token lives behind a boundary the agent can't cross. Honest caveats: it doesn't fix prompt injection, your WorkOS API key is still in the runtime, and provider permissions are still provider permissions. Verdict: a genuinely useful framing — "you can't leak what you never held" — and a good reminder that credentials belong in the least-reachable component that can still do the job.

## 8. Adapting to AI: Leadership — by Colin Breck

![Colin Breck](https://storage.ghost.io/c/d3/13/d313bae5-6633-4ef2-8565-d9e72c1a5da1/content/images/size/w1200/2026/07/create-the-future.png)

**Source:** https://blog.colinbreck.com/adapting-to-ai-leadership/
**Karakeep doc:** `zc48aymr7gyu06cat5x1m10s`

Colin Breck's essay on how AI changes leadership, part of his "Adapting to AI" series. His thesis: transformational times need transformational leaders, and AI will make the best leaders more valuable while exposing the mediocre ones. Routine, bureaucratic management is exactly the kind of thing an AI can do better — it's less biased, has no ego, isn't angling for promotion. But the human stuff — sitting with uncertainty, self-awareness, connecting people to purpose — is where leaders earn their keep, and AI can't fake that. He argues organizations will get flatter, with fewer managers and more exceptional leaders working directly with engineers and customers. The sharpest warning: AI is going to magnify existing organizational dysfunctions (people "building kingdoms with AI all over the company"), so leadership's critical job is actively shaping the human organization to avoid multiplying its own pathologies. Verdict: a thoughtful, systems-thinking take — AI doesn't replace leadership, it raises the bar on the parts of it that were always hard.

## 9. mflux-community — by GitHub

![mflux-community](https://avatars.githubusercontent.com/u/309522101?s=280&v=4)

**Source:** https://github.com/mflux-community
**Karakeep doc:** `qlc4efmzatdqh4pxxkoui13n`

The mflux-community GitHub org — home of MFlux, a library for running generative AI image models (Flux.2, Z-Image, Krea, Ernie, etc.) locally on Apple Silicon Macs (and Linux with CUDA). It leverages Apple's MLX framework for unified-memory, Metal-accelerated on-device inference, with a simple `mflux-generate` CLI. The org maintains quantized checkpoints (Q3/Q4/Q6/Q8/BF16) for a long list of models — Krea2, ERNIE-Image, Flux.2 Klein, Z-Image, Qwen-Image, Flux.1 — plus the main `mflux` repo (2.3k stars, MIT) and a model-library builder. Verdict: the go-to hub for running modern image-gen models on a Mac without a cloud GPU.

## 10. LLMKube - Kubernetes for Local LLMs — by Defilan Technologies LLC

![LLMKube](https://llmkube.com/og-image.jpg)

**Source:** https://llmkube.com/
**Karakeep doc:** `xfuf2ajkj4u0tjvx6au8fe9v`

LLMKube is a Kubernetes operator for self-hosted LLM inference — vLLM, llama.cpp, and TGI on NVIDIA, Apple Silicon, and AMD. It's driven by Foreman, an "agentic harness" where local models on your own fleet open their own pull requests, reviewed and merged alongside human contributors. The pitch: local LLMs are great for prototyping but scaling them for a team is where it gets hard — silent failures, multi-GPU memory math by trial and error, Docker Compose that doesn't scale. LLMKube gives you pluggable runtimes, HPA autoscaling on real inference metrics, GPU layer offloading with custom sharding, Grafana dashboards, and CUDA 13/Blackwell support. Deploy an LLM in seconds with a declarative YAML `Model` spec. Verdict: a serious-looking platform layer for teams that want to run their own inference fleet, with the agentic Foreman harness as the differentiator.

## 11. omarchy-mac — by Codeberg.org

![omarchy-mac](https://codeberg.org/favicon.ico)

**Source:** https://codeberg.org/malik-na/omarchy-mac
**Karakeep doc:** `uqzcevrgv9b7s303f1m8whu3`

The Apple Silicon port of Omarchy — an opinionated Arch/Hyprland setup for M1/M2 Macs, running via Asahi Linux. The `quattro` branch is the active one (6,640 commits, 29 branches), with a dedicated aarch64 package repo, an install path for fresh Apple Silicon machines, and macOS-behavior defaults (natural scrolling, no tap-to-click). It ships agent skills, a ChatGPT desktop app under Install > AI, and the full Omarchy rice. Verdict: for anyone who wants the Omarchy experience on a Mac instead of a Dell XPS — the same keyboard-driven, pre-rice'd Arch, now on Apple hardware.

## 12. FastMetal-QAD: Fast Local Video Generation on Apple Silicon — by Hao AI Lab @ UCSD

![Hao AI Lab @ UCSD](https://haoailab.com/img/fm_new.png)

**Source:** https://haoailab.com/blogs/fastmetal/
**Karakeep doc:** `w7i2pzoyqx47yahv2v7cpaxp`

Hao AI Lab's FastMetal-QAD brings Wan video models natively to Apple Silicon via a new MLX runtime. Three open-source models — 1.3B, 5B, and 14B — built to run on Macs. The 5B generates a five-second 720p clip in 151 seconds (47s in fast mode) peaking at 9.3 GiB, so 720p fits in 16GB of unified memory; the 14B targets 36GB+ Macs for the strongest local quality. The runtime uses MLX-first DiT with dense attention, INT8 quantization (chosen over MXFP4/NVFP4 for accuracy), pre-quantized checkpoints, and prompt caching. Generation modes include fast (frame interpolation via rife-mlx), refine (second denoising pass), quality (full Wan VAE), and prompt enhancement. Verdict: a genuinely impressive milestone — local video generation on a laptop-class GPU, with the 5B fitting in 16GB being the headline number.

## 13. Your Expired Credit Card Might Still Work (Visa Won't Fix This) — by Better Stack

![Better Stack](https://i.ytimg.com/vi/Wiccjk-3ihw/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/Wiccjk-3ihw
**Karakeep doc:** `ant1060w31tym8gqsnlb1qpn`

A short on an unpatched Visa exploit that lets expired credit cards still process transactions. Researchers at UMass discovered that in Visa's contactless configuration, the expiry field sits outside the card's cryptographic signature — it's unprotected while every other check passes. They built a relay using two Android phones (one a fake card talking to the terminal, one the real expired card) and swapped the expiry date the terminal sees; the card's cryptogram is never touched, so verification comes back clean. Whether the bank approves depends on whether it specifically checks for expired cards — they tested five major US banks and got mixed results. MasterCard, Amex, and Discover all rejected the altered data, so it's Visa-specific. There's an optional relay-resistance protocol that would catch it, but it wasn't enabled on any tested card/terminal. Researchers notified Visa in May and December 2025; Visa reproduced it internally but no fix or CVE has shipped. Verdict: a genuinely unsettling payment-security gap — and the practical advice is to cut through the chip and mag stripe of old expired cards before tossing them.

## 14. Turn your terminal agents into a self-coordinating office of clones — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/chaitanyagiri/munder-difflin)

**Source:** https://www.opensourceprojects.dev/post/f38220ee-1cf9-443c-bbf6-af6500261e8c
**Karakeep doc:** `zg00wjsoi0difi7kojghyb27`

Munder Difflin is an open-source agent harness that turns your existing terminal-agent CLIs (claude, codex, grok, kimi, qwen, opencode, pi, copilot) into a "self-coordinating office of clones." It's a desktop app (Electron/React/TypeScript/Pixi.js/xterm.js/node-pty) where each session becomes a full agent with long-term memory, a mailbox, and a desk on a 2D office floor, coordinated by "Michael" — your clone who routes work between them. You talk to Michael, Michael talks to the team. The clever bit: it wraps the CLIs you already pay for, on their existing hourly limits — no new API keys. It's a working prototype (v0.4.5, MIT). Verdict: a fun, practical take on multi-agent coordination that doesn't reinvent the wheel — it just adds a coordination layer and a visual office floor on top of the agents you already use.

## 15. The canonical curated list of Python frameworks, libraries, and tools — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/vinta/awesome-python)

**Source:** https://www.opensourceprojects.dev/post/43315590-1fe7-4cb3-b898-8e28b332744b
**Karakeep doc:** `yz1zwne32ub50mapxlwomcb9`

Awesome Python (github.com/vinta/awesome-python) — the #10 most-starred repo on GitHub — is a single, opinionated, curated list of the best Python frameworks, libraries, and tools. It's organized into a massive set of categories covering nearly the whole ecosystem: AI & ML (agents, deep learning, NLP, computer vision), web development, HTTP & scraping, database & storage, data & science, developer tools, DevOps, CLI & GUI, text & documents, media, security, and the Python language itself. Each entry is a direct link to the repo with a one-line description — no landing pages, no blog posts. The curation philosophy is the point: it's a filter, not a firehose, and it's actively maintained (recently added "Agent Skills" under AI). There's a searchable companion site at awesome-python.com. Verdict: the canonical starting point for "there has to be a Python library for this" — bookmark it.

## 16. Ghidra: NSA's open-source SRE framework with decompilation, graphing, and scripting — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/nationalsecurityagency/ghidra)

**Source:** https://www.opensourceprojects.dev/post/611d6322-a84f-4218-80a0-ba7fb3df1f06
**Karakeep doc:** `t39pqz4gxtz5eoron7cjtwry`

Ghidra is the NSA's open-source software reverse engineering framework — the free alternative to IDA Pro. It's a full-featured SRE suite running on Windows, macOS, and Linux, with disassembly, assembly, decompilation (reconstructing C-like pseudocode from binaries — the headline feature), graphing, and scripting in Java or Python. It supports a wide variety of processor instruction sets and executable formats, runs in interactive GUI or automated/scripted mode, and was built to solve scaling and teaming problems on complex SRE efforts. It's genuinely free, cross-platform, and designed for collaborative analysis. Honest caveat: check the Security Advisories — some versions have known vulnerabilities. Verdict: the gift that keeps on giving from the NSA — a serious RE toolkit with no enterprise price tag.

## 17. Nginx Proxy Manager: reverse proxying with SSL so easy a monkey could do it — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/nginxproxymanager/nginx-proxy-manager)

**Source:** https://www.opensourceprojects.dev/post/278e193b-c5a8-4d53-8b70-f60154ff5c8f
**Karakeep doc:** `kyta5pbvhfpvjkmz81kps88y`

Nginx Proxy Manager is a pre-built Docker image that wraps reverse proxying and SSL termination in a clean web interface — no hand-editing Nginx configs or wrangling certbot. You log into a web UI on port 81 and create forwarding domains, redirections, streams, and 404 hosts without touching a config file. SSL is handled automatically via Let's Encrypt (or your own certs), access control (lists + basic HTTP auth) is built in, and the admin UI includes user management, permissions, and an audit log. The quick start is a docker-compose file with three ports and two volumes. Honest caveat: it's Docker-first, so bare-metal Nginx with complex routing might not be a fit. Verdict: the "so easy a monkey could do it" framing is the actual design constraint — a genuinely painless gateway for self-hosted services.

## 18. The blockchain dark forest is real—this handbook is your survival map — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/slowmist/blockchain-dark-forest-selfguard-handbook)

**Source:** https://www.opensourceprojects.dev/post/7d8086d2-a9c8-4bee-bc19-ad4907276ccb
**Karakeep doc:** `bq6qdkmvxbt70yywc17nmic7`

The Blockchain Dark Forest Selfguard Handbook from SlowMist is a free, open-source survival guide for crypto security (darkhandbook.io). It's structured as a practical curriculum: wallet creation and backup, hot vs. cold wallets, DeFi and NFT security, signing dangers, traditional privacy protections (OS, browsers, password managers, 2FA, email, SIM, GPG), and the human factors that undo technical precautions. It includes a "What to do When You Get Hacked" section (stop loss first, protect the scene, root cause analysis, source tracing) and a "Misconception" section debunking "code is law" and "in blockchain we trust." The "dark forest" framing borrows from Liu Cixin's Three-Body Problem — assume every on-chain interaction is hostile until proven otherwise. It's multilingual (Chinese, Japanese, Korean, Arabic, Indonesian) and community-translated. Verdict: a genuinely comprehensive, brutally honest crypto-security handbook — the post-hack incident response plan alone is worth the read.

## 19. zoxide: a smarter cd that remembers your most-used directories — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/ajeetdsouza/zoxide)

**Source:** https://www.opensourceprojects.dev/post/c6b7af1a-5e75-4259-91c4-3cd2d0040c48
**Karakeep doc:** `zgjnb0uqgk54t8os7px5cxk7`

zoxide is a smarter `cd` that learns your habits — a drop-in replacement inspired by `z` and `autojump`. Under the hood it's a Rust binary that tracks how frequently and recently you visit directories, then ranks matches by your usage history. `z foo` jumps to the highest-ranked directory matching "foo"; it supports multiple args (`z foo bar`), subdirectory matching (`z foo /`), previous-dir (`z -`), an interactive `zi` mode with fzf, and tab completions. It's fast (compiled, not a shell script), works across bash/zsh/fish, and installation is a one-liner curl script or `cargo install zoxide`. Verdict: a small, focused tool that makes terminal navigation noticeably less annoying — the ranking-beats-searching shift is the clever part.

## 20. gdown: when curl and wget can't handle Google Drive downloads — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/wkentaro/gdown)

**Source:** https://www.opensourceprojects.dev/post/494ac32f-4b0e-4d0f-824a-8d8cac2448ef
**Karakeep doc:** `vtzmydcuztowh9qqtxnucv4c`

gdown is a Python-based CLI (Python 3.10+) built specifically for Google Drive downloads — the thing that breaks `curl` and `wget` (virus-scan warning pages, HTML files saved as your download, unresolvable URLs). You give it a Drive URL, file ID, or share link and it fetches the file, skipping the confirmation page Google serves for large files. It can recursively download entire folders, export Google Docs/Sheets/Slides to PDF/DOCX, resume interrupted downloads, limit speed, and route through a proxy — and it doubles as a plain HTTP/HTTPS downloader. The `--json` flag resolves the real filename without downloading. Verdict: the utility you install once and forget about until the next time a Drive folder download just works.
