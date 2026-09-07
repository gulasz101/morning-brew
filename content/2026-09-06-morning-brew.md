---
date: 2026-09-06
slug: 2026-09-06-morning-brew
tags: ARM,Apache HTTP Server,Atom,C,CAPTCHA,CLI,Caddy,DNSSEC,Discord,Distro,Documents,Domain Name Service,FTP,GTK+,GUI,Go,Graphics,HPC,IIS,ISO,Internet,Internet Information Services,JavaScript,LaTeX,Lua,Microsoft,Multimedia,Nginx,Other,Perl,Productivity,RSS,Reviews,Roundup,Rust,System Software,Tauri,TypeScript,Utilities,VoIP,Web Apps,artisanry,benchmark,btrfs,calibration,chat,client modification,communication,containers,crafting,distribution,feed reader,flash,free,handicrafting,handicraftsmanship,instant messaging,mind map,mind-mapping,monitors,network security,noise,open source,open source alternatives,openSUSE,performance monitoring,plugins,privacy,proof of work,security,self-hosted,server,servers,service discovery,themes,web,web servers
---

# Morning Brew — 2026-09-06

Yesterday's hoard: 47 bookmarks — 9 videos (transcribed) and 38 articles. Hand-bookmarked stuff first, then the RSS autohoarded pile (Open-source Projects + LinuxLinks) grouped at the bottom.

### Hand-bookmarked

## 1. Did OpenAI actually build AGI? GPT-6 Astra first look — by Fireship

![Fireship](https://i.ytimg.com/vi/FluKUJyeYD8/maxresdefault.jpg)

**Source:** https://youtu.be/FluKUJyeYD8?si=pUSAMj8peSC2ZYKU
**Karakeep doc:** `s72scsxkdcco9c9haf0cf3xk`

A week of AI whiplash: Anthropic dropped Fable/Mythos 5.1, Meta dropped Musepark 1.3 (cheap as hell if you let them train on your data), then OpenAI announced GPT-6 Astra and Brockman called it AGI. The launch was a mess — ChatGPT, Claude, Grok and Cursor all went down at once, OpenAI yanked the announcement for 90 minutes, and Sam Altman told a pro subscriber to "go to bed." Astra's pitch is computer use: it scored 73% on OS World (vs Soul's 65%), 99% on ARC-AGI-3, and is the first model to hit OpenAI's "critical cyber" threshold — meaning it can find zero-days on its own. But Artificial Analysis scored it a 61, same as GPT-5.6 Soul and five points behind Fable 5.1, so the AGI label is doing a lot of heavy lifting.

## 2. 3AM Observability Crash Course (A True Story) — by pouria

![pouria](https://i.ytimg.com/vi/AmHYfEW7CCg/maxresdefault.jpg)

**Source:** https://youtu.be/AmHYfEW7CCg?si=3fb8NAc7-X8x_u1O
**Karakeep doc:** `bwqvj6z4u6lo2oew4piws301`

A narrated story about Wojak, a frontline engineer on his first on-call shift, hit with a "high checkout latency" alert at 3AM with zero clue how production works. The video walks the whole observability stack as he learns it live: PagerDuty alert → Grafana dashboards → Prometheus metrics (counters, gauges, histograms) → Elasticsearch logs → distributed traces. The root cause turns out to be a classic connection pool exhaustion in the inventory service — 20 connections all in use, 7 requests waiting, and the SQL query itself only took 4ms while acquiring the connection ate 3 seconds. The punchline: nobody's touched that service in a year, the guy who wrote it left, and the "fix" everyone actually does is just restart the service to clear the pool.

## 3. Omarchy Can Do WHAT?! 50 Features You're Missing — by NetworkChuck

![NetworkChuck](https://i.ytimg.com/vi_webp/2IDjteRQgMQ/maxresdefault.webp)

**Source:** https://youtu.be/2IDjteRQgMQ?si=Dws0FZ2Wa5qeYd7Y
**Karakeep doc:** `u6p3ljruq2ozsp26zzomockf`

A rapid-fire tour of 50 Omarchy (Arch-based, Hyprland) features Chuck thinks you're sleeping on. It's mostly keyboard-driven: super-key bindings for tiling, workspaces, scratchpads, grouping, plus built-in goodies like fuzzy finder, zoxide, eza, and a clipboard with image history. The genuinely neat stuff: BTRFS snapshots on every update, per-device restarts (WiFi/Bluetooth/audio without a full reboot), persistent SSH sessions across WiFi drops, local Whisper transcription (VoxType), airdrop-style file sharing (LocalSend), and an AI-first agent harness with Claude/Codex/Copilot preinstalled. He also shills ThreatLocker hard for the "don't let AI agents roam free at work" angle.

## 4. From COBOL to Copilots: Why No-Code Never Kills the Coder - Sam Bishop (PyCon AU 2026) — by PyCon AU

![PyCon AU](https://i.ytimg.com/vi/kpNXG7M_5mg/maxresdefault.jpg)

**Source:** https://youtu.be/kpNXG7M_5mg?si=quAhRMBWg0YUCy6-
**Karakeep doc:** `qamhd7um5i8h1arccmo3m4el`

A history lesson with a point: every "this will replace programmers" pitch has failed the same way for 70 years. Sam runs through Flow-Matic, COBOL, BASIC, 4GLs, HyperCard, Visual Basic, executable UML, and low-code/no-code — each promised English-like code that business users would write themselves, and each still needed specialists to actually ship anything real. The AI era is the same story: prompt injection, hallucination, and zero reproducibility mean it can't touch safety-critical work, and it's just made the boring scaffolding faster while the hard thinking stays yours. His advice: document everything like you have amnesia, and treat AI agents like enthusiastic junior devs who'll happily write ten thousand wrong lines if you don't supervise.

## 5. How to Make PERFECT Moka Pot Coffee (Better Than 90% of People!) — by Dero_De_Barista

![Dero_De_Barista](https://i.ytimg.com/vi_webp/eVe_KwFQSd0/maxresdefault.webp)

**Source:** https://youtu.be/eVe_KwFQSd0?si=U6EaPW0faN7aB7KD
**Karakeep doc:** `bvmnrrku3xmnt3ifbgxt28ej`

A step-by-step for pulling an espresso-like shot out of a moka pot. The recipe: 18g of medium-dark coffee, freshly ground to a medium-fine size (slightly coarser than espresso), 120ml of water pre-boiled to 80°C so you don't scorch the grounds, and a low flame for slow extraction. He uses a needle/WDT tool to break up clumps, optionally an Aeropress filter for a cleaner cup, and cuts the brew after ~15 seconds of flow so it stays concentrated instead of over-diluted. Result is a strong, low-acid, chocolatey shot with a foam he's happy to call crema.

## 6. Can You Build A MacBook Using Only Aliexpress Parts? — by Phone Repair Guru

![Phone Repair Guru](https://i.ytimg.com/vi_webp/E8V9csFkmMo/maxresdefault.webp)

**Source:** https://youtu.be/E8V9csFkmMo?si=M1gWzEFsRb1auwvU
**Karakeep doc:** `hm9kymz6vbkjlqe3cz8cx4jc`

Dude tries to build an M1 MacBook Air from scratch using only AliExpress parts, and it's a shitshow from the jump. Missing screws, a flex cable that shorted the whole board, mismatched colors because cheaper parts came in different shades. The kicker: it cost $939 CAD, about $330 more than just buying a refurbished one on Amazon. Everything actually worked in the end — Touch ID, speakers, camera — except the display, which Apple's diagnostic menu flagged as non-genuine. Fun project, terrible economics. 🤦

## 7. Is it time for the Linux TV? — by Haggis on Toast

![Haggis on Toast](https://i.ytimg.com/vi/nROKp0BpFek/maxresdefault.jpg)

**Source:** https://youtu.be/nROKp0BpFek?si=k0F2A-ooU5eIUnEq
**Karakeep doc:** `ddypu1bwsxurfhaph2f7mfid`

Guy's Nvidia Shield died, so instead of dropping a couple hundred quid on a new one he frankensteins a Linux TV box out of a spare mini PC. Nobara + Waydroid for Android TV, Flex Launcher to hop between Steam, Blu-ray ripping, and IPTV. It mostly works, but the verdict is "not a perfect all-in-one" — no Dolby Vision/Atmos, HDR is dodgy, and Netflix is locked to 720p because of Widevine DRM bullshit. He's keeping it anyway and already planning a full Steam machine next. 🎮

### RSS — YouTube

## 8. Apple Will Dominate AI — by Better Stack

![Better Stack](https://i.ytimg.com/vi/jaDs0vGFi9Q/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/jaDs0vGFi9Q
**Karakeep doc:** `goqenye6dxk4kz4j8r0nut4x`

The argument: no AI company has held a lead for more than a few weeks, so Apple doesn't need the best model — just one that's good enough, wrapped in the integration, hardware, and user base nobody else has. Apple's whole playbook is sitting back, letting others iron out the wrinkles, then sliding in late with a better product. iPhone, Watch, AirPods, Apple Silicon all did it; Maps, HomePod, and Vision Pro didn't. The bet is that "good enough model + everything else" wins this time.

## 9. The Arch Linux Malware Is Getting Creative — by Brodie Robertson

![Brodie Robertson](https://i.ytimg.com/vi_webp/fLJTemwd_bc/maxresdefault.webp)

**Source:** https://www.youtube.com/watch?v=fLJTemwd_bc
**Karakeep doc:** `qtauek1lt6zq0zj5fgt0xbjl`

The AUR finally fixed the "abandoned package, I'll take it" hole — now it's a no unless the maintainer says yes, and unverified accounts get nuked after 14 days. But the malware didn't stop, it just got dumber and weirder. Brodie walks through three recent cases: an XSNO package that social-engineered its way in as a co-maintainer and used `curl` to pull a "system manager" off Tor, a deleted-but-still-cloneable Gentor package (AUR git repos never actually get purged), and a "hyprland-fixes" package whose author left code comments documenting their own backdoor — installs Tailscale, drops an SSH key, spawns sshd on ports 3 and 4, and wipes logs. The lesson: even outside a spam wave, read the damn PKGBUILD before you install.

### Open-source Projects (RSS)

## 10. One-stop C#/.NET learning hub for tutorials, interviews, and career growth — by Open-source Projects

![Open-source Projects](https://www.opensourceprojects.dev/images/open-source-logo-830x460.jpg)

**Source:** https://www.opensourceprojects.dev/post/e4a70742-fad0-4c9d-b6f9-84909d42c678
**GitHub:** https://github.com/YSGStudyHards/DotNetGuide
**Karakeep doc:** `zoh6ro1fmvrwhlllyfwxcuj7`

DotNetGuide is a massive Chinese-language C#/.NET learning hub — 10.8k stars — covering tutorials, interview prep, learning paths, and dev tools for the whole .NET ecosystem. It's an awesome-list style knowledge base: ASP.NET Core, Blazor, Avalonia, Azure, plus interview questions and resume templates. MIT licensed, C#. If you're prepping for a .NET interview or just want a curated map of the ecosystem, this is the reference.

## 11. OpenCV: the open source computer vision library with docs, forums, and contribution guidelines — by Open-source Projects

![Open-source Projects](https://www.opensourceprojects.dev/images/open-source-logo-830x460.jpg)

**Source:** https://www.opensourceprojects.dev/post/cc4031db-553d-4b06-b6ad-3bb7e6246381
**GitHub:** https://github.com/opencv/opencv
**Karakeep doc:** `dxts4btk6qnb7ud4808dkfge`

OpenCV is the open-source computer vision library — 90k stars, C++, Apache 2.0. It's the de facto standard for image processing, object detection, and deep-learning inference, with bindings for Python, Java, and more. You already know what this is; the opensourceprojects.dev post was just a stub pointing at the docs and forums.

## 12. Single-header OpenType shaping and Unicode segmentation for C/C++ — by Open-source Projects

![Open-source Projects](https://www.opensourceprojects.dev/images/open-source-logo-830x460.jpg)

**Source:** https://www.opensourceprojects.dev/post/749c86ec-ca7d-4074-b46b-21ed322f5b43
**GitHub:** https://github.com/JimmyLefevre/kb
**Karakeep doc:** `u1ruh1ydsw3thcd3lh8ql1ty`

The opensourceprojects.dev page is a 404 stub, but the actual project is JimmyLefevre/kb — a set of single-header, permissively-licensed C/C++ libraries for Unicode text segmentation and OpenType shaping. It's ~22k LOC in one header, so you drop it in without dragging in HarfBuzz's whole build system. Handy if you need text shaping without the dependency hell.

## 13. QAnything 2.0 merges old Docker and Python versions into one Docker Compose command — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/netease-youdao/qanything)

**Source:** https://www.opensourceprojects.dev/post/2ba45da2-d364-440b-bc12-1112f3bffa8b
**GitHub:** https://github.com/netease-youdao/QAnything
**Karakeep doc:** `nkd62x4ecsjn6of18ghyjerp`

QAnything is NetEase Youdao's self-hosted RAG system — ask questions against your own PDFs, Word docs, and databases, and it retrieves chunks and feeds them to an LLM. The 2.0 release collapses the old split Docker/Python setup into a single `docker compose up`, and adds a feature to inspect data at each pipeline stage so you can actually debug wrong answers. AGPL-3.0, so watch the copyleft if you're thinking commercial. Runs fully offline, which is the whole point if your docs are sensitive.

## 14. Statically recompile N64 binaries into portable C with this tool — by Open-source Projects

![Open-source Projects](https://www.opensourceprojects.dev/images/open-source-logo-830x460.jpg)

**Source:** https://www.opensourceprojects.dev/post/a118c447-ed2d-4870-80b2-12f74c3cb588
**GitHub:** https://github.com/N64Recomp/N64Recomp
**Karakeep doc:** `in7czirkmmelmxgcr0nf22we`

The opensourceprojects.dev post is a 404 stub, but the real thing is N64Recomp/N64Recomp — a tool that statically recompiles N64 game binaries into portable C you can compile for any platform. It's how people are turning old ROMs into native PC ports, Donkey Kong 64 included. If you've ever wanted to run an N64 game without an emulator, this is the magic trick.

## 15. 100 lines of Python still scores 74% on SWE-bench verified — by Open-source Projects

![Open-source Projects](https://www.opensourceprojects.dev/images/open-source-logo-830x460.jpg)

**Source:** https://www.opensourceprojects.dev/post/8eb509e5-538e-4d16-9f1e-f9e061489aff
**GitHub:** https://github.com/SWE-agent/mini-swe-agent
**Karakeep doc:** `hyzk0ly9znvh9wne9zyhemup`

mini-swe-agent is SWE-agent's stripped-down agent: ~100 lines of Python that solves GitHub issues or helps in your CLI, no giant config or monorepo — and it still scores >74% on SWE-bench verified. MIT, Python, 7k stars. The pitch is radical simplicity: a single file you can actually read and understand, instead of a framework with a thousand knobs.

## 16. Markdown resumes that render cleanly in Typora, VSCode, and Obsidian — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/bingyanstudio/lapiscv)

**Source:** https://www.opensourceprojects.dev/post/37c22596-5466-49b5-9c50-f9dd68f3804e
**GitHub:** https://github.com/BingyanStudio/LapisCV
**Karakeep doc:** `gopagdp1xyr20x9i7sbem3pc`

LapisCV is a pile of CSS themes that turn plain Markdown into a resume that actually looks designed. You write headers and bullets, the CSS does the spacing, and it exports to PDF with proper A4 margins. Works in Typora, VSCode, and Obsidian, so your resume becomes a git-trackable text file instead of a Word doc you're scared to touch.

## 17. Build and run agents your team can chat with, in the open — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/agenta-ai/agenta)

**Source:** https://www.opensourceprojects.dev/post/4bb4496c-ad23-4faf-8f86-3a7ce81b40a4
**GitHub:** https://github.com/Agenta-AI/agenta
**Karakeep doc:** `g3nw2w3edsxwhdfb5us190v2`

Agenta is an MIT-licensed workspace for building agents and letting your whole team chat with them instead of leaving them to rot in a notebook. The chat window is the actual product, not a demo, and agents can run in the background hooked into your apps. Self-host it or use their cloud — no vendor lock-in.

## 18. Header-only C++ libraries, organized from argument parsers to web frameworks — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/p-ranav/awesome-hpp)

**Source:** https://www.opensourceprojects.dev/post/319a2f18-3acd-47f6-a486-e723b7965379
**GitHub:** https://github.com/p-ranav/awesome-hpp
**Karakeep doc:** `g0ueiht9vawsujjjilox5o2c`

awesome-hpp is a curated list of header-only C++ libraries across 50+ categories, from arg parsers to web frameworks. Each entry has a stars badge, a one-liner, and the license right there so you don't have to click through. It's a README, not a package — bookmark it and stop rewriting the same utilities.

## 19. ArtCraft is the open-source IDE for interactive AI image and video creation — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/storytold/artcraft)

**Source:** https://www.opensourceprojects.dev/post/6583a6e4-cd36-4d50-91c0-c8332b7babf1
**GitHub:** https://github.com/storytold/artcraft
**Karakeep doc:** `st8fk0j3po3usmbynxqzk0vp`

ArtCraft is an open-source IDE that treats the scene, not the prompt, as the interface for AI image and video. You import images, turn them into 3D meshes, pose characters, and block out shots before the AI renders — so two frames actually feel like the same room. They're calling it "Photoshop for everyone," which is a big swing, but the feature set backs it up.

## 20. Peergos: a p2p encrypted filesystem that puts users in control of their data — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/peergos/peergos)

**Source:** https://www.opensourceprojects.dev/post/cd071847-c974-4275-bcce-2e32789092bf
**GitHub:** https://github.com/Peergos/Peergos
**Karakeep doc:** `pt0r6brxv2dkgantgveic6ly`

Peergos is a p2p encrypted filesystem where access control is baked into the crypto, not a permissions database some company can flip. On top of the drive it stacks a messenger, an email client, and a social network that also hides your social graph. It's been through real security audits in 2019 and 2024, so "encrypted" here isn't just marketing.

## 21. Curated Swift agent skills for Claude Code, Codex, and more — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/twostraws/swift-agent-skills)

**Source:** https://www.opensourceprojects.dev/post/ed15f44c-6bc2-4c23-8e43-fe79b286e682
**GitHub:** https://github.com/twostraws/Swift-Agent-Skills
**Karakeep doc:** `b5igdki1vl06l5xwpmlsx6jp`

Swift Agent Skills is a directory of community agent skills that make Claude Code, Codex, Cursor, and Windsurf write idiomatic Swift instead of generic boilerplate. It's organized by framework — SwiftUI, SwiftData, Concurrency, Testing — with multiple authors' takes on the same topic. The README leads with an all-caps warning to read any third-party skill before you install it, which is the right call for what's basically executable instructions.

## 22. Campfire: a self-hosted chat app with Docker images and guided deployment — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/basecamp/once-campfire)

**Source:** https://www.opensourceprojects.dev/post/8d7fd913-7bdf-464e-a56e-2fce95fc63f7
**GitHub:** https://github.com/basecamp/once-campfire
**Karakeep doc:** `we7dravz4lnu6qo4cgdu92vv`

Basecamp's open-source chat app, and the whole pitch is one Docker image that bundles web app, background jobs, caching, and SSL termination. No separate Redis/Postgres/Nginx containers to wire together. It pairs with ONCE, their guided installer — one curl command, pick Campfire from a menu, and it handles setup plus auto-updates. Rooms, DMs, file previews, full-text search, Web Push, and a bot API. If you've been putting off ditching Slack because self-hosting sounded like a weekend project, this might actually be an afternoon one.

## 23. direct multi-scan registration on factor graphs for any range sensor — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/koide3/glim)

**Source:** https://www.opensourceprojects.dev/post/bbe8f7d4-fd91-430a-aef7-47a6e681a810
**GitHub:** https://github.com/koide3/glim
**Karakeep doc:** `sj0suq9nyevwaf2gpb5s4plo`

GLIM is a 3D mapping framework that doesn't give a shit what sensor you feed it — spinning LiDAR, Livox, Realsense, Azure Kinect, all treated the same. It does direct multi-scan registration on factor graphs (GTSAM under the hood) instead of feature matching. The killer feature is an interactive map-correction interface, so when the point cloud turns into abstract art you fix it manually instead of rerunning the whole pipeline. Dependency list is not trivial though — you'll be rebuilding GTSAM 4.3a0 and gtsam_points yourself, so this is for people who know their way around a build system.

## 24. WayVR brings your Wayland desktop into VR with minimal performance impact — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/wlx-team/wayvr)

**Source:** https://www.opensourceprojects.dev/post/04c32eb5-6640-437e-abac-7068954e3b3e
**GitHub:** https://github.com/wayvr-org/wayvr
**Karakeep doc:** `rvt7bx9y9hiw5dxofhrgqd5m`

Formerly WlxOverlay-S, this is a lightweight OpenXR/OpenVR overlay that floats your Wayland or X11 desktop inside your headset. The whole point is low overhead — no fancy shaders, just functional desktop access that doesn't eat your frame time while you're gaming. Works with Monado, WiVRn, and SteamVR, and the README even covers the Flatpak Steam permission nightmare. One annoyance: SteamVR bugs mean it won't auto-start, so you launch it manually each time.

## 25. Run IB Gateway and TWS in Docker with zero human interaction — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/gnzsnz/ib-gateway-docker)

**Source:** https://www.opensourceprojects.dev/post/684c54e6-b534-452c-94e9-407b3bd0db76
**GitHub:** https://github.com/gnzsnz/ib-gateway-docker
**Karakeep doc:** `p3czkk3b1cd31rcat6eldy7v`

Interactive Brokers' gateway is a desktop app that expects a human to click through login dialogs — a pain in the ass for headless servers. This Docker image fixes that with IBC (simulates the clicks), Xvfb (fake display), and socat (relays the localhost-only port). Supports live and paper trading in parallel, Docker secrets for credentials, and aarch64 so it runs on a Pi or Apple Silicon. If your broker connection is the flakiest part of your trading stack, this turns it into just another container.

## 26. Simple.css: a CSS template for a good looking website, really quick — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/kevquirk/simple.css)

**Source:** https://www.opensourceprojects.dev/post/c34ec602-a5b4-499a-ba19-baf7b4261f13
**GitHub:** https://github.com/kevquirk/simple.css
**Karakeep doc:** `nbsrwqh8sd112e04smkc2dw8`

One CSS file, no JS, no build step, no classes — you write semantic HTML and it styles it for you. Drop a single `<link>` tag in and your bare page turns presentable. It's opinionated (clean, content-focused) and the whole stylesheet is readable enough to learn from. Perfect for blogs and docs where you don't want to fight margins for an hour. IE11 users are out of luck, and the README isn't sorry about it.

## 27. Building GLaDOS from Portal as a proactive voice assistant with vision and MCP tools — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/dnhkng/glados)

**Source:** https://www.opensourceprojects.dev/post/a28d3e39-29ec-48b3-b5bd-ebaae80efcb5
**GitHub:** https://github.com/dnhkng/GLaDOS
**Karakeep doc:** `k05udr6g04xp23p70n635534`

A multi-agent voice assistant that brings Portal's GLaDOS to life — vision, long-term memory, emotional state (PAD model), and MCP tool use, running on a Rock5b SBC. The twist is she's proactive: she watches and speaks when she has something to say instead of waiting for a wake word. Getting round-trip latency under 600ms meant training a custom TTS model. It's a fan project that's also a serious look at hard voice-AI problems.

## 28. Mimic native iOS system notifications in SwiftUI with a simple view modifier — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/danielsaidi/systemnotification)

**Source:** https://www.opensourceprojects.dev/post/fe0d5cbd-e163-4b24-a4e5-40e5529ce3ac
**GitHub:** https://github.com/danielsaidi/SystemNotification
**Karakeep doc:** `gruib91wpnom154ankza5g9j`

A SwiftUI library that recreates those native iOS banners (silent switch, AirPods connect) with a single `.systemNotification` view modifier. Two modes: a boolean binding for simple cases, or a `SystemNotificationContext` for triggering from anywhere in the hierarchy. Ships a `SystemNotificationMessage` view with icon/title/text out of the box, but the body is a view builder so you can drop in anything. If you've ever hacked together a custom notification view, this is the "why was I doing it the hard way" library.

## 29. Nginx RTMP Docker image for streaming from OBS to multiple clients at once — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/tiangolo/nginx-rtmp-docker)

**Source:** https://www.opensourceprojects.dev/post/31e2775c-5c69-4389-9357-66cf9c28f1ad
**GitHub:** https://github.com/tiangolo/nginx-rtmp-docker
**Karakeep doc:** `dzpgo29ra4ku9yb2oo9bc3rk`

One `docker run` and you've got a private RTMP server on port 1935. Point OBS at it, and anyone with VLC can watch the same stream — no Twitch, no latency, no bullshit. It's Nginx 1.15 with the RTMP module baked in, so the fan-out to multiple viewers is handled for you. No web UI, no auth, no transcoding, but for the core job of getting video from OBS to a few friends it just works.

## 30. Reverse-engineering cheap Amazon drones to replace their closed-source mobile apps — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/marshallrichards/turbodrone)

**Source:** https://www.opensourceprojects.dev/post/8def3dbc-a4b3-4fe0-afcd-a9ed38eb267d
**GitHub:** https://github.com/marshallrichards/turbodrone
**Karakeep doc:** `dq4f21p8ew5ffwdmfcg5yawp`

Turbodrone is a Python client that speaks the undocumented WiFi protocols on those $50 Amazon toy drones, so you can fly them from your computer instead of some sketchy phone app. It maps out several protocol families (`s2x`, `wifi_uav`, `cooingdv`, `x69_lg`) across brands like Hiturbo and Plegble, with an honest "tested vs suspected" compatibility table. For fifty bucks you get a programmable drone you can crash without crying — way better sandbox than a DJI.

### LinuxLinks (RSS)

## 31. Cap – lightweight privacy-focused CAPTCHA — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/CAPTCHA-banner2.png)

**Source:** https://www.linuxlinks.com/cap-lightweight-privacy-focused-captcha/
**GitHub:** https://github.com/tiagozip/cap
**Karakeep doc:** `hofbzndk77qhf518o5g3uhdz`

Cap ditches the "click all the traffic lights" bullshit and swaps in proof-of-work plus browser instrumentation to weed out bots. No telemetry back to the devs, self-hostable, and it even has an invisible mode that verifies in the background. Written in JavaScript, Apache 2.0, and you can restyle the widget with CSS variables. If you're sick of feeding visitor data to Google's reCAPTCHA, this is the one to try.

## 32. Moodist – ambient sounds for focus and calm — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2021/09/abstract-background-with-sound-waves-design.jpg)

**Source:** https://www.linuxlinks.com/moodist-ambient-sounds-focus-calm/
**GitHub:** https://github.com/remvze/moodist
**Karakeep doc:** `wniuyzz2uy61o3ceq8x9fk5t`

Moodist is a browser-based ambient sound generator with 84 curated sounds you can layer into custom soundscapes. It does binaural beats, isochronic tones, breathing exercises, Pomodoro timers, a todo list, and a notepad — basically a whole focus toolkit in one tab. TypeScript, MIT license, works offline as a PWA and self-hosts with Docker. Good replacement for the five different noise apps you already have open.

## 33. Calibrate your Monitor with these Open Source Tools — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2018/01/no_signal_tv_1.jpg)

**Source:** https://www.linuxlinks.com/monitorcalibration/
**Karakeep doc:** `jxa7ma9fzriexmyo3imfdxh6`

What your screen shows and what the image should look like are two different things, and if you do photography or design you already know it. The roundup covers eight tools — DisplayCAL-py3, ArgyllCMS, DisplayCAL, GNOME Color Manager, LPROF, ddcui, lcms2, and colord. Hardware colorimeters beat eyeballing it, but these get you real ICC profiles and accurate color without spending a dime.

## 34. Serf – decentralized service discovery and orchestration — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/09/Configuration-Management-1.png)

**Source:** https://www.linuxlinks.com/serf-decentralized-service-discovery-orchestration/
**GitHub:** https://github.com/hashicorp/serf
**Karakeep doc:** `ebyxw6s8s46uk20kc26y3gx4`

HashiCorp's Serf is a masterless cluster tool — every node runs an agent that gossips membership data, so there's no central server or single point of failure. It's a CLI plus an embeddable Go library, with broadcasts, filtered queries, and shell handlers for turning events into local actions. No external database needed, and it encrypts the gossip traffic. Good little building block for automated infra.

## 35. 11 Best Free and Open Source Linux Crafting Tools — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/07/postcard-with-embroidery-kettle-macro-shot-closeup.jpg)

**Source:** https://www.linuxlinks.com/craftingtools/
**Karakeep doc:** `azuweh8983vifswvhwvg7l34`

Cross-stitch and knot design software, because apparently Linux people also embroider. The list runs KXStitch, Ink/Stitch, Embroidermodder, Crosti, Cstitch, and a handful more — tools to build charts from scratch or generate them from imported photos. Good open source in this niche is thin, but there are a few real gems here.

## 36. openSUSE MicroOS – immutable rolling-release Linux distribution — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/04/Linux-Distributions.png)

**Source:** https://www.linuxlinks.com/opensuse-microos-immutable-rolling-release-linux-distribution/
**Karakeep doc:** `yfj5nlur88leyse2barh3fmv`

MicroOS is openSUSE's immutable, rolling-release distro aimed at container workloads and single-purpose servers. Read-only Btrfs root plus transactional updates — changes land on a new snapshot, not the running system, so rollback is trivial when something breaks. You run apps in containers instead of bolting them onto the base OS, and it ships images for physical, VM, cloud, and ARM.

## 37. mCaptcha – privacy-respecting proof-of-work CAPTCHA — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/CAPTCHA-banner.png)

**Source:** https://www.linuxlinks.com/mcaptcha-privacy-respecting-proof-of-work-captcha/
**GitHub:** https://github.com/mCaptcha/mCaptcha
**Karakeep doc:** `q3v88599cuzrtq5zpraefp6w`

A self-hosted CAPTCHA that makes bots burn CPU instead of making you squint at blurry traffic lights. The client does a SHA-256 proof-of-work, gets a token, and the server checks it before letting the request through. No cookies, no visitor tracking, and it runs on your own infra instead of Google's. Written in Rust, obviously.

## 38. Mintstick – create and format USB sticks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2021/01/FlashOS.png)

**Source:** https://www.linuxlinks.com/mintstick-create-format-usb-sticks/
**GitHub:** https://github.com/linuxmint/mintstick
**Karakeep doc:** `ohq68qaq16iswavv4kgjuwbl`

Linux Mint's little GTK tool for writing ISO/IMG files to USB sticks and formatting drives. Handles FAT32, exFAT, NTFS, and ext4, plus SHA-256 and GPG verification for Mint/Ubuntu/Debian images. It's the boring utility you only remember exists when you need to boot a rescue disk at 2am. Written in Python.

## 39. 6 Best Free and Open Source Linux Web-Based Discord Tools — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2018/06/Gaming-Chat.jpg)

**Source:** https://www.linuxlinks.com/best-free-open-source-linux-web-based-discord-tools/
**Karakeep doc:** `vyuhfbfp70gf9zb2tt764flq`

Discord's official Linux client is proprietary, so this roundup lists open-source web-based clients and mods for people who still need the platform but want more control. The pitch is customization, themes, and plugins without handing Discord full run of your box. For the FOSS diehards who can't quit their servers.

## 40. Best Free and Open Source Alternatives to Microsoft Internet Information Services — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2021/08/Open-Source-Alternatives-Microsoft.jpg)

**Source:** https://www.linuxlinks.com/best-free-open-source-alternatives-microsoft-internet-information-services/
**Karakeep doc:** `wlez5jmvv17bjlp4ifqbp6je`

IIS is Windows-only and proprietary, so here's the obvious trio: Apache for fine-grained config and a huge module ecosystem, nginx for high-concurrency and reverse proxying, and Caddy for automatic HTTPS with a dead-simple config file. Pick your poison based on whether you want control, speed, or not thinking about TLS certs ever again.

## 41. Latexmk – fully automated LaTeX document generation — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2021/07/typesetting-tools.jpg)

**Source:** https://www.linuxlinks.com/latexmk-fully-automated-latex-document-generation/
**Karakeep doc:** `swkp1s6gpjgtsaizv2khot9c`

A Perl build tool that figures out how many times to run LaTeX so your cross-references, citations, and tables of contents actually resolve. It auto-invokes BibTeX, Biber, and makeindex when needed, and has a preview-continuous mode that rebuilds on every save. Basically it stops you from running `pdflatex` five times by hand like a caveman.

## 42. TeamMapper – Collaborative Mind Mapping Web App — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/11/Minder-mapping.png)

**Source:** https://www.linuxlinks.com/teammapper-collaborative-mind-mapping-web-app/
**GitHub:** https://github.com/b310-digital/teammapper
**Karakeep doc:** `wfyagu8upugm34tq7x04dkr0`

A self-hosted web app for mind maps you can share via URL or QR code and edit with other people. Imports/exports JSON and Mermaid, stores everything in PostgreSQL, and can optionally generate maps through an OpenAI-compatible service (off by default). Written in TypeScript, because of course it is.

## 43. WyrmRSS – RSS and Atom feed reader — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/latest-news-2.png)

**Source:** https://www.linuxlinks.com/wyrmrss-rss-atom-feed-reader/
**GitHub:** https://github.com/kryoseu/WyrmRSS
**Karakeep doc:** `o6ods0kra93jjqearyjq34up`

An RSS/Atom reader that ships as both a self-hosted web app and a desktop program, with three feed modes (River, Feed, Radar) and notifications to Discord, Slack, or a webhook. The desktop edition stores feeds locally and won't sync with your server, so don't confuse it for a client. Rust + TypeScript, ~260 MB of RAM in testing.

## 44. 10 Best Free and Open Source Linux FTP Servers — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/04/002-ftp.png)

**Source:** https://www.linuxlinks.com/best-free-open-source-linux-ftp-servers/
**Karakeep doc:** `xaqsf4jhh05u2kuk5ez3bkea`

A roundup of ten free/open-source FTP servers, with the usual caveat that plain FTP is insecure and you should really be using SFTP over SSH instead. The list: Pure-FTPd, SFTPGo, ProFTPd, bftpd, vsftpd, tnftpd, umftpd, Inetutils, FileZilla Server, and unFTP. Each entry links to a fuller review, and the article notes FTP's popularity has tanked for general downloads in favor of HTTP, BitTorrent, and metalink — but it still works fine for moving big files.

## 45. LIKWID – performance monitoring and benchmarking suite — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/03/Benchmarking-Vector.png)

**Source:** https://www.linuxlinks.com/likwid-performance-monitoring-benchmarking-suite/
**GitHub:** https://github.com/RRZE-HPC/likwid
**Karakeep doc:** `qo5icdc6l7jf5aafd15cxhtu`

LIKWID is a command-line performance engineering suite for people who actually need to know what their CPU and memory are doing. Topology discovery, hardware counters, thread pinning, energy reads via RAPL, and a microbenchmarking tool all in one. It's aimed squarely at HPC nerds chasing NUMA and cache bottlenecks across multi-socket boxes. Free, GPLv3, from the RRZE-HPC crew. If you're not doing HPC you'll never touch it, but it's the real deal. 🔬

## 46. DNS – recursive and authoritative DNS server — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2023/01/System-Admin.jpg)

**Source:** https://www.linuxlinks.com/dns-recursive-authoritative-dns-server/
**GitHub:** https://github.com/ZerosAndOnesLLC/rDNS
**Karakeep doc:** `q9mz575qafgrlerrz7nvft23`

rDNS is a Rust DNS server that does recursive, forwarding, and authoritative duty all in one binary. Built on Tokio with a sharded cache, DNSSEC validation, DNS-over-TLS, and RPZ filtering for blocking domains. Zones can live in memory from zone files or a PostgreSQL backend. MIT licensed, from ZerosAndOnes LLC. Handy if you want self-hosted DNS with filtering without running three separate daemons. 🛡️

## 47. tex-fmt – fast LaTeX formatter written in Rust — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2021/07/typesetting-tools.jpg)

**Source:** https://www.linuxlinks.com/tex-fmt-fast-latex-formatter/
**GitHub:** https://github.com/WGUNDERWOOD/tex-fmt
**Karakeep doc:** `v0n5iq96qmd4045wtuock5ke`

tex-fmt is a fast, opinionated formatter for LaTeX source, written in safe Rust. Indents environments, wraps long prose, aligns table ampersands, and respects `.gitignore` when recursing. Has check and fail-on-change modes so it slots into pre-commit hooks and CI. TOML config at user, repo, or working-dir level. If you write LaTeX and hate hand-formatting it, this is the tool you didn't know you wanted. 📄

