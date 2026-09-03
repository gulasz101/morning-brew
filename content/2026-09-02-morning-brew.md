---
date: 2026-09-02
slug: 2026-09-02-morning-brew
tags: Apps,Arch,CLI,Desktop,Distro,Documents,GNOME,GNOME Shell,GNOME extensions,GTK+,GUI,Gaming,Go,Graphics,Internet,JavaScript,Kernel,Lightweight,Linux 7.1,Linux kernel,Linux kernel 7.1,Mozilla Thunderbird,Multimedia,News,PHP,Productivity,Python,QR code,Reviews,Roundup,Rust,Scientific,Steam,Steam Client,TUI,Thunderbird,TypeScript,Utilities,Web Apps,barcode,bookmark manager,chmod,collecting,collection manager,color palette,console,desktop customization,desktop environment,distribution,email client,end of life,file permissions,forecasting,free,libadwaita,media players,meteogram,open source,open source software,photo management,photo manager,productivity tools,project management,software,speech recognition,system administration,terminal,tiling window manager,tui,video players,wayland,weather,web browser,window management
---

# Morning Brew — 2026-09-02

A hoard of **40 items** hoarded on 2026-09-02 — 7 of them youtube/instagram videos (all transcribed), the rest fetched and summarized. Buckle up.

## 1. Barcoder – barcode and QR code generator — by linuxlinks.com

![linuxlinks.com](https://www.linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/barcoder-barcode-qr-code-generator/
**Karakeep doc:** `gqeglxissrsu3d94qn1pdvcz`

Barcoder is a no-bullshit GTK4 + libadwaita utility by Ondřej Kolín that turns text into 1D barcodes and 2D codes, all generated locally with the rxing library in Rust. No network calls, no cloud, just type a value, pick a symbology and it renders a live preview you can save as PNG or vector SVG. It covers the boring-but-useful linear formats — EAN-13, EAN-8, Code 128, Code 93, Code 39, UPC-A, UPC-E — plus QR and Aztec. Input validation actually checks your values against the code type and surfaces failures in the UI instead of silently spitting out an unprintable mess. It's got four size presets from compact product labels up to high-detail print, remembers your last type/format/size across sessions, and filenames are auto-derived from the barcode value. Free, GPL v2, and it behaves itself on small screens — a genuinely handy little tool for anyone printing labels or shipping stuff.

## 2. Mozilla Thunderbird 155 Adds Custom OAuth Support for IMAP and SMTP Servers — by 9to5linux.com

![9to5linux.com](https://9to5linux.com/favicon.ico)

**Source:** https://9to5linux.com/mozilla-thunderbird-155-adds-custom-oauth-support-for-imap-and-smtp-servers
**Karakeep doc:** `mdqxlirbt100oqw3dcveqlj1`

Thunderbird 155 dropped right after Firefox 155, and the headline feature is custom OAuth support for IMAP and SMTP servers — with new PKCE and external-browser fields, plus OAuth add-ons that can override built-in settings for specific domains. That's a real unlock for self-hosters running non-Gmail providers. The S/MIME pop-up got an upgrade to show signature, digest, encryption algorithms and key sizes. Manual account config is smarter now: Exchange, Graph and custom OAuth are all streamlined, and Enterprise policies can disable QR export and experimental features. A solid heap of bug fixes too — IMAP tags now sync across clients without reverting on refresh, attachment filters stopped disappearing from global search, and a failed encrypted send actually preserves your draft instead of nuking it. Mac users get their dock unread badge back. The usual Thunderbird cadence: nothing flashy, just quietly making an aging workhorse less infuriating.

## 3. Steam Client Now Supports HDR Streaming on Steam Deck OLED — by 9to5linux.com

![9to5linux.com](https://9to5linux.com/favicon.ico)

**Source:** https://9to5linux.com/steam-client-now-supports-hdr-streaming-on-steam-deck-oled
**Karakeep doc:** `fuyk12u4yv8mpch71q3rzj3x`

Valve's September 1st stable Steam Client update finally brings HDR streaming to the Steam Deck OLED via Remote Play, and bumps video color range on every platform during Remote Play — so streaming games now actually looks decent instead of washed out. There's a big workflow win in there too: you can now switch accounts while a game is running, with an optional "ask which account to use on startup" toggle and the confirmation dialog removed in most cases. The client also waits for just-exited games to finish cloud sync before shutting down, so no more corrupted saves from impatient shutdowns. Friends & Chat now flags suspicious content in group chats with one-click report/block. Steam Input splits Steam Controller configs from Deck configs and clarifies shared vs device-unique layouts, and Big Picture grabs the left trackpad of the Deck/Controller as a scroll wheel in the web browser. Linux-specific fixes include the Big Picture overlay keyboard no longer mangling keystrokes and a crash on suspend/resume after unplugging a controller.

## 4. Omnom - self-hosted web content preservation service — by linuxlinks.com

![linuxlinks.com](https://www.linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/omnom-self-hosted-web-content-preservation-service/
**Karakeep doc:** `bdicgzfguzfn4yxsrw66v9td`

Omnom (by asciimoo/Adam Tauber, AGPL v3, written in Go) is a self-hosted web content preservation service that's essentially a bookmark grab-bag: web archiving, feed aggregation and Fediverse support all in one. The clever bit is that it captures pages as actually rendered by a browser rather than just stashing a URL, so dynamic content and locally-saved multimedia survive — and it keeps multiple snapshots of the same URL with summary/comparison and diff views to track how a page changes over time. It doubles as an RSS/Atom reader and follows ActivityPub streams. Multi-user web interface, filtering by date, text, tags, users, domains and URLs. Firefox and Chromium extensions, installable from a single binary or Docker, auth via one-time login tokens, OAuth or trusted remote-user headers, plus a documented API and CLI admin tools. If you're the type who likes your archive-self-hosted and is mildly amused that karakeep itself is on the related-software list, this is your jam.

## 5. Fable 5.1 is here, and its REALLY good — by Better Stack

![Better Stack](https://i.ytimg.com/vi/0lBvjhcRqyU/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=0lBvjhcRqyU
**Karakeep doc:** `f8q6nfgtpix1rz50rfo5aihz`

A real hands-on breakdown of Anthropic's Fable 5.1 / Mythos 5.1 release, built around actual benchmark numbers and the host's own code/design tests rather than just the press release. The setup: Mythos 5.1 is "apparently the exact same model, just with fewer safeguards," gated to Anthropic's trusted-access program — so everything in the video is about Fable 5.1.

**The pricing catch is the meat.** Anthropic claims ~25% cheaper than Fable 5 on typical token-billed workloads and up to ~45% on highly agentic work, because cache-read pricing drops from $1/MTok to $0.25/MTok (cheaper than Geopity 5.6). But the host flags the fine print: that applies only "wherever usage is billed by token" — i.e. API usage, *not* subscriptions — which stings more because Anthropic simultaneously cuts subscription limits 17% on September 14th. And Artificial Analysis found the cost math murkier than the headline: on a *max* effort level, Fable 5.1 was actually *more* expensive per task than Fable 5, because 5.1-max burns more tokens (45K vs 36K per task), and cache-write/reasoning/answer costs went up despite cheaper cache reads.

**The effort-level insight is the practical takeaway.** Fable 5.1 on *high* effort matches Fable 5 max for intelligence at more than half the price and a third of the tokens. The host argues the new low/medium/high effort levels are a genuine output-token improvement — every model variant that scores above GPT 5.6 medium is matched or beaten by some Fable 5.1 effort level on both intelligence and token usage. His advice to subscribers: drop the effort level to stretch your plan, but *stay clear of max effort* — it will still burn through your subscription. His broader gripe: Anthropic models always command a premium and sit at the end of every price chart; if they got closer to OpenAI's pricing they'd be dominant.

**Benchmarks don't fully agree.** Deep SWE isn't out yet, but Cursor Bench favors 5.1: on max effort, cost per task dropped from $17.32 to $9.64 *while* scoring 3% higher and using 30K fewer tokens; on high effort it beats Fable 5 on extra-high while cheaper and using ~half the tokens; and 5.1 on *medium* beats GPT 5.6 on *max* effort and is cheaper. Anthropic's own blog benchmarks unsurprisingly show sweeping wins — double the scores on Terminal Bench Science and a ~30% lead on agentic coding. Net: everyone agrees 5.1 is a new frontier for intelligence, but you may pay more if you run it at max.

**Hands-on test 1 — Formula 1 browser game** (single self-contained HTML file, Three.js, with requested features like AI opponents and wheel steering), a gauntlet of frontier models. Fable 5.1 (extra high) took 59m58s, ~$18.87 via API (8.1M tokens, "an absolute thinker" — no other model thought anywhere near an hour), and delivered the most bug-free result he's gotten from any model: working track (no objects in the road), proper braking/steering/collisions, correct steering direction, working minimap/timing/lap records. Fable 5 took 25m30s for $13.73 at half the tokens, but is more basic (backwards text, "post-it note" grandstand, clip-through collision). GPT 5.6 (extra high) was cheapest/fastest — 6m54s, ~$5.15, 6.8M tokens — but produced one of the *worst* results he's seen: no start page, a nonsensical 90° opening turn, trees in the road and a broken track map. Grok 4.6 (9 min, $0.38, 200K tokens) wasn't playable at all — starting on grass, pass-through barriers, sharp impossible corners. Kimi 3 (max, 35 min, $1.26, 1.7M tokens) was the open-model stand-in: genuinely playable (completes a lap) though twitchy steering and a basic look. Verdict: Fable 5.1 wins, Fable 5 second — a clear Anthropic lead, likely because it simply thinks far longer.

**Hands-on test 2 — website design** (bold minimalist site for a tennis centre; booking, facilities, coaching, memberships). Fable 5.1 took 51 min / ~$17 but produced a site the host genuinely likes — strong typography, all requested features working, and "doesn't scream AI generated," though with that telltale new-AI style. Fable 5 did it in 8 min / ~$4.15, nearly identical but dark-mode and image-light; GPT 5.6 sol was the former UI champ with GPT-image-2-generated graphics and a worse booking section, but it was the *only* one that built a full-stack app (hosting quirk he dislikes) for 22 min / $4.10. Grok 4.6 (8 min, $0.65) had the best price/performance and actually the best court-booking picker, though the font bugged him. Kimi 3 was cheapest (9 min, $0.55) and decent but more barebones. Takeaway: 5.1's design is next-gen, but at 17 bucks it's 4× the Fable 5 price for a marginal bump — for price and speed he'd pick Fable 5 here.

**The other two promised fixes.** Data retention is mostly hype for normal users: "nothing really changes unless you're a special enterprise customer" — the standard retention policy still applies. Safeguards are the genuine win: cybersecurity false positives down ~60%, because Fable 5.1 can discover software vulnerabilities but not craft exploits. Also improved writing style — Fable 5 / Opus 5 were jargon machines, and the host says online sentiment is that 5.1 reads more naturally.

**Overall verdict:** a genuine new frontier and "a step in the right direction" for Anthropic, best-in-class on intelligence and his real-world tests, with real savings available to subscribers who drop the effort level — but the pricing story is more nuanced than the headline (subscription caps, max-effort token burn) and model choice varies heavily by task.

## 6. Free 9-week course for productionizing ML services, from training to monitoring — by opensourceprojects.dev

![opensourceprojects.dev](https://opengraph.githubassets.com/1/datatalksclub/mlops-zoomcamp)

**Source:** https://www.opensourceprojects.dev/post/6a8883ca-8256-4b2f-94b7-d4018f41e1b1
**Karakeep doc:** `r5zpqyadk5b302vbfm5h9mso`

MLOps Zoomcamp from DataTalksClub is a free 9-week course that takes your model from "nails the validation set" to actually reliable in production — experiment tracking, orchestration, deployment strategies, monitoring and alerting, with a real industry stack rather than toy frameworks. It assumes you already know ML (Python, Docker, CLI basics, plus their ML Zoomcamp as recommended primer), so it respects your time and skips the hand-holding. Two routes: a live cohort with graded homework, leaderboard, peer review and a certificate, or self-paced — both free, though the catch is no live cohort is scheduled for 2026, so right now self-paced is the only game, unless you register for a notify. There's an active Slack community and a final project that's genuinely portfolio-grade, which is worth more than most paid certs when you're gunning for an MLE title. The opensourceprojects writeup is solid and honest about the live-vs-self-paced tradeoff. If you're tired of throwing models over the wall into a production void, this is legitimately a zero-dollar way to fix that gap.


## 7. Unity MCP server gives your AI agent direct access to the Unity Editor — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/ivanmurzak/unity-mcp)

**Source:** https://www.opensourceprojects.dev/post/cccf6720-58d8-4b8d-948e-764cbfc16a3c
**Karakeep doc:** `zf1km9tdnao6wen8rsoh2xhr`

Every Unity dev who's made an AI write C# knows the pain: the bot cranks out code in a complete vacuum, blind to your scene hierarchy, your assets, your actual project state. Like asking a mechanic to fix your car from a different continent. Unity MCP fixes that by plugging Claude, Codex, Cursor, Copilot, Gemini and the rest straight into the editor via the Model Context Protocol — the AI can actually inspect your scene, nudge components around, and modify things in real time instead of guessing. Architecture is clean: an OpenUPM package dropped into your Unity project, plus a lightweight server (local or Docker image `aigamedeveloper/mcp-server`) that translates AI requests into real editor operations. The killer part is that it's not vendor-locked — MCP means you can swap Claude for Cursor mid-project and keep the whole pipeline. That's the difference between an AI rubber duck and an actual collaborator. Worth a weekend experiment if you've ever cursed at an LLM that had no clue what was in your scene.

## 8. One-click portable builds for local LLMs, no telemetry or setup — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/oobabooga/text-generation-webui)

**Source:** https://www.opensourceprojects.dev/post/547b378a-455f-479b-bba0-621fed54c449
**Karakeep doc:** `pdga8qvv55zlhzujy8v4f51h`

This is oobabooga's TextGen (formerly text-generation-webui) reborn as a "get started in one minute" desktop app: download, unzip, double-click, and a local model is running — no Python environments, no CUDA-dependency hell, no telemetry, no remote update nudges. Portable builds ship for Linux, Windows, and macOS with CUDA, Vulkan, ROCm, and CPU-only variants, and they eat GGUF models straight from Hugging Face via llama.cpp. Under the hood it's not stuck on one backend either — llama.cpp, ik_llama.cpp, Transformers, ExLlamaV3, and TensorRT-LLM are all swappable without restarting. It's a full-featured UI too: chat mode, custom-character stuff with Jinja2 prompt templates, a notebook tab for free-form generation, vision, PDF/texfile upload, and OpenAI/Anthropic-compatible APIs with tool-calling. Tools are single `.py` files and it even does LoRA fine-tuning plus diffusers image generation. The "no sysadmin required" pitch is the real win — for anyone who wanted to run a local LLM but bounced off the setup ritual, this removes most of the barriers. It's not the most advanced tool in the space, but it's the most accessible.

## 9. Phi Cookbook: practical examples for running Microsoft's efficient SLMs anywhere — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/microsoft/phi-3cookbook)

**Source:** https://www.opensourceprojects.dev/post/1d645a3a-b42d-474d-ae06-a3b687f118df
**Karakeep doc:** `gvxel43i53uqkeahj2echrk1`

Microsoft's Phi models are the anti-GPU-flex answer to "run AI without a cluster of A100s in your closet," and this cookbook (`microsoft/phi-3cookbook`) is the practical on-ramp for actually using them — on a laptop, a phone, or an edge device. Phi positions itself as the most powerful, cost-effective small language model around, and the README covers reasoning, chat, coding, plus image-and-audio tasks, all designed to run on limited compute. The repo is structured as a proper learning resource, not a marketing page: runnable examples for cloud and edge deployment, spanning text/chat/coding/vision/audio scenarios, with GitHub Codespaces and Dev Containers support so you skip the environment-wrestling entirely. It's also a genuinely global project — the README is translated into Arabic, Bengali, Bulgarian, Chinese (multiple regional variants), Czech, Danish, Dutch, Estonian, Finnish, French, German, Greek, Hebrew, Hindi, Hungarian, Italian, Japanese and more. For somebody prototyping on a budget or who wants on-device, privacy-sensitive assistants, this kills the need to rent expensive cloud compute. It's not a magic bullet, but it's a fast, honest way to test whether a small model fits your use case before committing to architecture.

## 10. The W3C WebAuthn spec editor's copy, now built with mise — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/w3c/webauthn)

**Source:** https://www.opensourceprojects.dev/post/c1ed6921-f6e6-4140-ae86-d3ae45f90053
**Karakeep doc:** `fp7qr736javcnkzx6zm6kafv`

Turns out the W3C standard you trigger every time you tap a security key isn't drafted in some closed committee room — the WebAuthn spec lives in a public GitHub repo (`w3c/webauthn`) with a real CI/CD pipeline. The editor's copy auto-publishes to `w3c.github.io/webauthn` from the `gh-pages` branch every time someone pushes to `main`, while the frozen working-draft snapshot sits at `www.w3.org/TR/webauthn`. The interesting bit for tooling nerds: it's built with mise, the new tool that folds runtime versions and task definitions into one command — `mise setup`, `mise build`, `mise serve` (live-reloading dev server at localhost:8000). That replaces the old mishmash of Ruby, Python, and custom scripts that plague W3C spec repos — if you've wrestled with `rvm` AND `pipenv` in the same project, you'll feel this one in your soul. It's also a genuine testing ground: the spec is backed by the Web Platform Tests webauthn suite, so the prose is verifiable browser behavior, not just words. And there's a real contribution path — CONTRIBUTING.md, issues, mailing-list archives. Not flashy, but a refreshing peek at the machinery behind web authentication, and a clean example of mise on a docs-heavy project.

## 11. 每周五更新的科技爱好者周刊，值得长期关注 — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/ruanyf/weekly)

**Source:** https://www.opensourceprojects.dev/post/da57fa1c-9834-4a76-b184-b37f721f0a07
**Karakeep doc:** `d7lll2hk11big981kb0x2ysi`

This is Ruan Yifeng's 科技爱好者周刊 (Tech Enthusiast Weekly) — a Friday-published tech digest that's been quietly curating the best corners of the tech world for years. No algorithm, no hype machine: just one person's informed editorial voice, published as numbered markdown files (like `docs/issue-410.md`) in a plain GitHub repo. The structure is gloriously low-tech — a README index organized by year and month, each issue a single well-organized text file you can read in the browser or clone and browse locally. Topics swing hard: one week AI memory management, the next why Dropbox didn't make it, then a debate on whether 6GHz spectrum is actually a problem. It's refreshingly honest about the industry too — issues with titles like "Token 费用难以负担" (token costs are hard to afford) and "为什么软件股下跌" (why software stocks are falling) ask uncomfortable questions instead of cheerleading. There's even a long-running free "谁在招人" (who's hiring) job board in the discussions. Zero signup, zero paywall, content lives in a public repo, and the archive is a two-year time capsule of the AI wave crashing in real time. High-signal and worth a spot in any reading routine.

## 12. Run Claude Agent SDK from any ACP-compatible client — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/agentclientprotocol/claude-agent-acp)

**Source:** https://www.opensourceprojects.dev/post/82862bc9-3609-4508-9ac3-ec9464b59a13
**Karakeep doc:** `d3li1hcp5nce7zj6q46w27o2`

Sick of being locked into Anthropic's own interfaces just to use the Claude Agent SDK? This npm package (`@agentclientprotocol/claude-agent-acp`) is an ACP adapter that wraps the SDK so any Agent Client Protocol–speaking client can drive Claude's agent underneath, no custom glue code. ACP is the standard that lets different AI clients and agents talk to each other, and this adapter makes Claude's SDK look like any other ACP-compliant agent. The feature parity is genuinely impressive for a "bridge" — context @-mentions, image support, tool calls with permission requests, follow-up turns, edit review, TODO lists, nested subagent transcripts, interactive and background terminals, custom slash commands, and client-side MCP servers. It even handles long-running session-scoped goals via a provider-neutral extension, plus opt-in extensions for structured errors/recovery and fine-grained tool permissions. There's a pragmatic touch around the still-evolving protocol: subagent sessions only surface after bilateral capability negotiation, falling back to legacy tool-call representations when the client doesn't advertise support. If you're building ACP tools or want to standardize your AI setup across clients, this is solid, well-scoped infrastructure.


## 13. step-ca: the online certificate authority that makes PKI manageable for DevOps — by Open-source Projects

![step-ca](https://opengraph.githubassets.com/1/smallstep/certificates)

**Source:** https://www.opensourceprojects.dev/post/27a3a2aa-4817-4674-8e81-7aea4b1aa5bb
**Karakeep doc:** `beb35h4pge6pr6103solyz1d`

Every team that has punted on running its own PKI because "we don't have a full-time security engineer" owes it to its collective certificate-expiry anxiety to look at `step-ca`. It's a Go-based, online certificate authority — the server-side half of the Smallstep `step` CLI toolkit — that responds to cert requests in real time instead of sitting there like a dusty signing authority someone has to manually tend. It issues RFC5280 / CA/Browser Forum–compliant HTTPS certs that actually work in browsers, DevOps TLS certs for VMs, containers, APIs, and Kubernetes pods, plus SSH certificates for logins backed by SSO tokens and cloud instance identity docs. The automation angle is the whole point: it's a full ACME server, so your existing Let's Encrypt-style tooling speaks to it without learning a proprietary API, uniting web and SSH infrastructure under one authority. Short-lived certs are the default mindset, which only works if renewal is automated — exactly the workflow it's built for. The README is refreshingly honest about limits, too: no active revocation via CRL/OCSP, no multi-CA setups, no FIPS in the open-source build — those live in their commercial product. Two-tier PKI for standard container-and-SSH setups it handles beautifully; just don't expect it to solve every enterprise cert nightmare.

## 14. komorebi brings tiling window management to Windows via a CLI — by Open-source Projects

![komorebi](https://opengraph.githubassets.com/1/lgug2z/komorebi)

**Source:** https://www.opensourceprojects.dev/post/862c0aad-c01d-43e3-a338-3ae2c84ceed9
**Karakeep doc:** `a3chut1j8c8j4e2hrleh7f39`

If you've ever gone back to Windows after living with a tiling window manager and wanted to throw something, komorebi is here to stop the regression. It's an open-source tiling window manager for Windows 10 and 11 that extends the existing Desktop Window Manager rather than replacing your whole desktop — it slots into your current setup as a focused tool. Everything is CLI-driven: windows, virtual workspaces, and monitors are all controlled through commands, so you can script your entire layout — coding layout, browsing layout, presentation layout — into a single command. There's no imposed keybinding system; you wire the commands into `whkd` or AutoHotKey and keep your existing shortcuts. The philosophy is refreshingly respectful of your machine: by default it makes as few OS modifications as possible, with deeper customization opt-in and off by default. It's actively maintained with a Discord server and docs, and there's even a separate macOS version if you bounce between platforms. The MDM splash-screen thing is a bit of a footgun for students on enrolled devices (email the author to get it removed, usually under 24h), but for anyone who wants keyboard-driven windows on Windows, this is the real deal.

## 15. PocketSphinx - speaker-independent continuous speech recognition engine — by LinuxLinks

![PocketSphinx](https://www.linuxlinks.com/wp-content/uploads/2020/02/voice-recognition.jpg)

**Source:** https://www.linuxlinks.com/pocketsphinx-speaker-independent-continuous-speech-recognition-engine/
**Karakeep doc:** `y46gqax9nd8lxwne2efqdoz1`

While everyone's busy renting GPU racks to run Whisper-scale neural speech models, PocketSphinx is the little engine that refuses to die — and refuses to call home. Originating from Carnegie Mellon's CMU Sphinx work, it's a compact, speaker-independent continuous speech recognition engine that deliberately skips the neural route and sticks with established statistical techniques whose modest resource requirements are perfect for embedded systems, offline command recognition, constrained hardware, and niche recognition jobs. Current builds fold in what used to be the separate SphinxBase library, and it delivers big-vocabulary, speaker-independent, continuous recognition with compact acoustic and language models. It's fully offline — no audio piped to external services — and offers a standalone command-line program to decode audio files and stdin streams, plus live recognition that chunks speech into segments and single-utterance mode. Forced alignment against known text (with optional phone- and state-level timing), line-delimited JSON output for scripting, JSGF grammar support for constrained command vocabularies, a C API, and Python bindings round it out. It's written in C, licensed under BSD-2-Clause, and maintained by David Huggins-Daines. If your use case is "recognize commands on a Raspberry Pi without phoning OpenAI," this is your engine.

## 16. 10 Best Free and Open Source Console Web Browsers — by LinuxLinks

![Console web browsers](https://www.linuxlinks.com/wp-content/uploads/2020/10/web-browsing.jpg)

**Source:** https://www.linuxlinks.com/best-free-open-source-console-web-browsers/
**Karakeep doc:** `pdtshy42ma2oqh48oln9g4zs`

LinuxLinks is back with a roundup for the terminal faithful: ten free, open-source console web browsers, because even in 2026 there's a case for reading the whole damn web from a tty. Console browsers are light on resources for low-spec machines, faster and more efficient than their GUI cousins, keep working when X/Wayland needs a restart, and are dreamy to script. The obvious stars are here — Lynx (legendary, still maintained), the feature-rich ELinks with its Lua/Guile extension angle, w3m (browser and pager in one), Links with its pull-down menus, and eww, the Emacs Web Wowser integrated into that famous text editor. Then it gets spicy: Offpunk is an offline-first command-line browser, Chawan is a TUI browser with actual CSS support (including FTP, Gopher, and Gemini), Carboxyl renders modern websites in a console via Chromium, edbrowse is a weird text-editor/browser/email-client mashup inspired by ed, and Brow6el adds graphics support to the terminal. Browsh gets a mention even though it technically cheats by leaning on headless Firefox. It's a "verdict chart" article, so you get the LinuxLinks trademark ratings and honest takes on which console browser fits which use case.

## 17. 20 Best Free and Open Source Media Players — by LinuxLinks

![Media players](https://www.linuxlinks.com/wp-content/uploads/2021/07/3d-render-3d-illustration-minimal-style-video-player-media-with-play-button-white-background-video-playback-concept.jpg)

**Source:** https://www.linuxlinks.com/best-free-open-source-media-players/
**Karakeep doc:** `eyia3fb4t5edr3r5rb68sxpq`

LinuxLinks rounds up twenty free and open-source media players whose minimum bar is that they handle both video and audio properly, in console form or GUI. It's a who's-who of the Linux playback scene: the usual suspects VLC and mpv (plus libmpv, which quietly powers half of everything), the Qt-flavored QMPlay2 and SMPlayer, and the venerable MPlayer. Then it goes niche — GridPlayer plays multiple videos simultaneously, clapper is a GNOME-native GJS/GTK4 build, xine still handles your CDs/DVDs/BluRays/VCDs, and SparkPlayer is a terminal-based multimedia player for local collections. Showtime, Glide, Phantom Player, Daikhan, QtAV, Rage, Kaffeine, Parole, MPC-QT, Totem, and the gloriously simple Dragon Player all make the cut. The article explicitly fences off audio-only players (covered elsewhere), media centers, and mpv front-ends so the list stays focused on genuine video-and-audio players. The comments deliver the expected LinuxLinks-adjacent pettiness: VLC apparently still lacks gapless playback, which one commenter refuses to let die, even as people hold out hope for VLC 4.0. A solid, honest benchmark if your player-of-choice keeps disappointing you.

## 18. rwx – TUI file permissions and ownership manager — by LinuxLinks

![rwx](https://www.linuxlinks.com/wp-content/uploads/2022/06/170y-utilities.jpg)

**Source:** https://www.linuxlinks.com/rwx-tui-file-permissions-ownership-manager/
**Karakeep doc:** `ka6fghknesu0kqcj1ccwimou`

If `chmod 777` has ever filled you with quiet shame, rwx is the interactive TUI that drags Unix file permissions out of the blind-grep-and-make-it-worse world and into a friendly grid. Written in Rust and MIT-licensed by Vinícius Manoel, it's an interactive terminal application for inspecting and modifying file permissions and ownership — you navigate the filesystem, pick a file or directory, and edit its mode and ownership from a dedicated interface. The killer detail is that it doesn't paper over Unix's permission model; it shows read/write/execute bits for owner, group, and others in a grid you can toggle bit by bit, with direct octal input (validated) for the old-school crowd, and support for SetUID, SetGID, and Sticky bits. It handles ownership changes with user/group validation before applying, shows a live symbolic permission preview while you edit, and can recurse through directory trees including symlinks, collecting traversal errors rather than bailing at the first failure. Edits stay pending until you explicitly apply them, and a custom panic hook restores your terminal state if something blows up. A live demo GIF sells it, and it slots into a category of chmod alternatives alongside chmod-cli and setfacl. For anyone who's eyeballed `ls -l` output with dread, this is a genuinely nicer way to reason about permissions.


## 19. Alternatives to popular CLI tools: chmod — by LinuxLinks

![chmod alternatives](https://www.linuxlinks.com/wp-content/uploads/2023/04/documentation-alternatives.png)

**Source:** https://www.linuxlinks.com/alternatives-popular-cli-tools-chmod/
**Karakeep doc:** `dwlmvuozq7lzbbtnl7cgxbhl`

LinuxLinks keeps grinding through its "alternatives to popular CLI tools" series, and this time the old warhorse `chmod` gets put under the microscope. Yes, chmod — the command you've typed a million times without thinking, the one that turns file permission errors into "oh right, I needed that +x flag." The roundup surfaces three honest replacements: chmod-cli, which generates chmod commands so you stop fumbling octal notation, rwx, a proper TUI for poking at file permissions and ownership without the cryptic `7 5 5` memory game, and setfacl, which drags access control lists kicking and screaming into your workflow. The piece also reminds you that `mkdir` and `install` set permissions at creation time, which is the kind of nugget that saves you a whole re-chmod ritual later. Is this going to change your life? Not remotely. But if you've ever squinted at `chmod 775` and wondered what unholy arrangement of rwx that actually is, this is a pleasant two-minute read that finally explains it.

## 20. 16 Best Free and Open Source Linux Collection Managers — by LinuxLinks

![Linux collection managers](https://www.linuxlinks.com/wp-content/uploads/2026/09/Best-Free-Open-Source-Software-Collection-Managers-2026c.png)

**Source:** https://www.linuxlinks.com/collectionmanagers/
**Karakeep doc:** `dl65oxno1iec6vdozpdujqgu`

LinuxLinks tackles humanity's ancient urge to hoard shiny objects with a roundup of 16 open source collection managers, and it's a surprisingly deep roster. The lead pick is HomeBox, a self-hosted inventory and organisation system that's become the darling of homelab addicts, but the list is far from one-trick. GCStar and Tellico handle the general-purpose cataloguing, while the specialist tools cover everything from coins (OpenNumismat) to vinyl (DVinyl) to books (Alexandria) — because apparently we all collect something, and stamps are so 1980. The more self-hosting-curious picks like Koillection, Yamtrack, and Ryot straddle the line between collection tracker and full media manager, while hydrus sneaks in for anyone who needs Danbooru-style image tagging. It's the kind of read that makes you suddenly aware of the junk drawer of digital hoarding apps you could be running on your NAS, and given Wojtek's track record, at least one of these is ending up in Docker tonight.

## 21. 50 Excellent GNOME Shell Extensions for GNOME 50 — by LinuxLinks

![GNOME Shell extensions](https://www.linuxlinks.com/wp-content/uploads/2022/04/gnome-extensions.png)

**Source:** https://www.linuxlinks.com/top-gnome-shell-extensions/
**Karakeep doc:** `l64k1n5ma7t2ofpmtjc25ial`

LinuxLinks serves up a sprawling 13-page guide to 50 GNOME Shell extensions tuned for GNOME 50, and if the default desktop feels a bit too "conservative" for your tastes, this is your shopping list. The spread runs from the genuinely transformative — Dash to Dock yanking your launcher out of the Activities Overview into an always-available, autohiding dock, and ArcMenu bringing back a proper app menu for the traditional desktop crowd — down to the small-but-handy stuff like Places Status Indicator, which saves you an embarrassing number of clicks when you just want your Downloads folder. Page two onwards keeps the hits coming: Dash to Panel, Tiling Assistant, PaperWM, Blur My Shell, Burn My Windows, and Space Bar for those of us who think workspaces should be actual workspaces. Since Wojtek is apparently married to GNOME, this is the kind of rabbit hole that ends with a desktop that looks vaguely like a cyberpunk spaceship and half a dozen extensions you'll never actually use but absolutely need.

## 22. Nvidia Could Own Hugging Face... This Is Huge — by Better Stack

![Better Stack short](https://i.ytimg.com/vi/spQE4s7tMzY/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/spQE4s7tMzY
**Karakeep doc:** `zezxiq4xybaa82o6vw1xr9cg`

Better Stack drops a short that should probably worry anyone who downloads models for a living: Nvidia is reportedly in talks to acquire Hugging Face for around $13 billion. The figure gets all the headlines, but the real story is the stack — the GPU maker already owns the silicon and CUDA, the software layer literally everything is built against, and now it could own the distribution layer where the whole open-weight world lives. The video leans on the "Switzerland of open weights" analogy, pointing out that Hugging Face has been the neutral ground where pip installing transformers didn't care whose hardware you ran it on, and that neutrality evaporates once Nvidia owns the default sort order and decide which model formats get first-class support. Nobody's predicting outright sabotage — the concern is a lot more boring and more insidious. To create a monoculture you don't block competitors, you just make the easiest path the one that works best on your own hardware. Nothing changes today, but if the deal lands, the neutral ground open weights grew up on suddenly answers to the company that makes the metal underneath all of it.

## 23. alex (@alextalksai) on X — by X (formerly Twitter)

![alex @alextalksai](https://pbs.twimg.com/amplify_video_thumb/2094760961764732929/img/j69zAj8Vmo55htTG.jpg)

**Source:** https://x.com/alextalksai/status/2094761014738796618
**Karakeep doc:** `c4yiqlxgav4kp02q9krahnne`

Alex is pumping a Spanish-language bomba over a "free" AI video tool called MoneyPrinterTurbo that's apparently blown past 100,000 GitHub stars. The pitch is the usual seductive spam: type a topic or keyword, and the AI writes your script, generates narration and subtitles, scrapes the visual material, and hands you a finished TikTok/Reels/Shorts video — all in one automated workflow. It's the kind of thing that promises to turn anyone into a faceless content factory with zero effort, which is exactly why it's blowing up. The top comment nails the vibe: "every day that Chinese dev just released it." Still, 100K stars is 100K stars, and if you've ever wanted to mass-produce shorts without touching a timeline, this repo is genuinely worth a look. Just don't expect it to make your content any less robotic.

## 24. Leonard Rodman (@RodmanAi) on X — by X (formerly Twitter)

![Leonard Rodman @RodmanAi](https://pbs.twimg.com/media/HRIq_vYbkAA5Ngd.png:large)

**Source:** https://x.com/RodmanAi/status/2094784063576113434
**Karakeep doc:** `r587wb0yqfwepxpul96pu5in`

Rodman goes after Chrome with an unearned "fired the whole browser team" headline to hype a Rust browser called Obscura, built specifically for automation, web scraping, and AI agents. The spec sheet reads like a meme: about 30MB of RAM, 85ms page loads, blocks 3,500+ trackers, no Chromium, no Node.js, a single binary, native rendering, and it randomizes browser fingerprints between sessions to keep scrapers from getting fingerprinted to death. It's sitting at 22K+ stars and it's free and open source. The reply section is where the fun happens though — one commenter points out that a headless no-sandbox browser is basically an RCE waiting to happen the moment any sketchy site serves a payload, and that the reason modern browsers are fat is because they're defending against two trillion edge cases. Fair warning: if you're going to run this thing for scraping, treat any site that lands in it like it's actively hostile.



## 25. Mojo Is Finally Open Source… So I Tested It — by Better Stack

![](https://i.ytimg.com/vi/uIqjWeO91p4/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=uIqjWeO91p4
**Karakeep doc:** `mo4b9tnnn40ih8frzdhn8ggs`

So Mojo finally hit 1.0 and the timing around it is suspicious as hell — closed compiler at launch, open-sourced seven days later, and Qualcomm just bought the company. The whole pitch is "Python that doesn't shit the bed on speed": write code that looks and feels like Python but runs the hot parts on CPU and GPU without dropping to C++ or CUDA. I ran the same loop in both languages on my machine: 26.5× faster than pure Python, and about 2× per op vs NumPy — respectable numbers, though nowhere near the absurd 68,000× (and 35,000×, and "50% faster than Rust") marketing figures floating around, which were benchmarks comparing vectorized Mojo against hand-rolled triple loops nobody in their right mind would write. But here's the actual problem: 1.0 shipped with 41 unstable API warnings covering core built-ins like `int`, `print`, and `len`, while removing the `fn` keyword outright broke the ecosystem. And the compiler being Apache 2.0 is great and all, but it landed three weeks after the Qualcomm acquisition closed, which makes the "openness milestone" timing feel less like generosity and more like a chipmaker making sure its language compiles well to its silicon. Still worth a day or two if you write GPU kernels, but I wouldn't bet my workflow on it yet.

## 26. Linux Kernel 7.1 Reaches End of Life, It’s Time to Upgrade to Linux Kernel 7.2 — by 9to5Linux

![](https://9to5linux.com/wp-content/uploads/2026/09/lk71eol.webp)

**Source:** https://9to5linux.com/linux-kernel-7-1-reaches-end-of-life-its-time-to-upgrade-to-linux-kernel-7-2
**Karakeep doc:** `zfjk8v8sc2i930klvffr7sdz`

Greg Kroah-Hartman pulled the plug on the Linux 7.1 series today, marking it EOL on kernel.org and releasing 7.1.13 as the final patch for anyone too lazy to move off it. The 7.1 branch was always a short-lived one, shipped in June with the new NTFS filesystem implementation — four years of work finally landing with full write support, delayed allocation, iomap, and folio integration — but if you want any further maintenance you need to jump to 7.2. That one dropped August 16th and brings cache-aware load balancing, initial HDMI 2.1 FRL support to the AMDGPU driver, devres-based ACPI notify handling, and the "Fair(er)" GPU scheduler. If you actually care about longevity rather than shiny features, 7.2 is also short-lived, so you'd be better off settling on an LTS branch like 6.18, 6.12, 6.6, or 6.1, which stay supported into 2027–2028. Arch and openSUSE Tumbleweed users are already on 7.2 in stable repos, as you'd expect. Nothing earth-shattering, just the quarterly "your kernel is old, upgrade or get pwned" reminder.

## 27. K’uychi — generate colour palettes from a base tone — by LinuxLinks

![](https://www.linuxlinks.com/wp-content/uploads/2026/09/Kuychi-example.png)

**Source:** https://www.linuxlinks.com/kuychi-generate-colour-palettes/
**Karakeep doc:** `bt9wkaizeqxvgu6l6gzrr83a`

K'uychi is a GNOME-native colour palette generator that flips the usual eyedropper approach: you pick one base colour and it cooks up a whole scale of lighter and darker tones around it. The magic is that it works in OKLab colour space rather than doing naive RGB arithmetic, so the resulting steps look perceptually uniform instead of janky. It's a compact GTK 4 + libadwaita app that fits right into the GNOME desktop, uses colorjs.io under the hood, and runs entirely locally — no online palette service needed. You get instant palette refresh as you tweak the source colour, one-click copying of any shade as a hex value for CSS or UI work, and you can open multiple windows to compare palettes side by side. Written in TypeScript with GJS by Naiara Gomez Castro, licensed under the Blue Oak Model License, and it follows the GNOME Human Interface Guidelines — name means "rainbow" in Quechua, which is a nice touch. Nothing revolutionary, but a clean little tool if you're tired of fighting perceptually-broken palettes by hand.

## 28. Tom Dörr (@tom_doerr) on X — by X (formerly Twitter)

![](https://www.google.com/s2/favicons?domain=x.com&sz=128)

**Source:** https://x.com/tom_doerr/status/2095077116593295673
**Karakeep doc:** `iqdqi98tgij29ml21ktv3l8e`

Tom Dörr — the guy behind Obsidian, naturally — boosted an open-source face recognition SDK that does the whole pipeline privately and on-premise. It detects faces, maps facial landmarks, and compares identities without shipping your biometric data off to some cloudy API. The repo is Faceplugin-ltd/Open-Source-Face-Recognition-SDK, and the pitch is a self-hosted Python SDK for identity-comparison use cases where privacy actually matters. 435 likes and 56 retweets suggests the surveillance-cautious crowd is paying attention, even if the comments are, uh, not exactly a deep discussion (the top reply is literally "H"). Given his track record of caring about local-first tooling, it's the kind of thing that fits his feed — useful for anyone who wants face-match capability without handing control to a third party.

## 29. I self-host my passwords without running a password manager server — by MakeUseOf

![](https://static0.makeuseofimages.com/wordpress/wp-content/uploads/wm/2026/09/syncthing-and-joplin-showing-as-download-options-on-computer-screen.jpg)

**Source:** https://www.makeuseof.com/self-host-my-passwords-without-running-password-manager-server/
**Karakeep doc:** `a6iu7k4c42phd3m96nuty5a5`

Afam Onyimadu kills the password-manager server and replaces it with KeePassXC plus Syncthing, because a KeePass vault is just an encrypted `.kdbx` file — no server, no reverse proxy, no updating container, no web UI to keep reachable. The first sync is nearly boring: he changes a password on the laptop, locks the screen, and a minute later the updated entry is already on his phone, because Syncthing moves the file like it's a JPEG and just doesn't give a shit what's inside. It gets interesting when two devices disagree — edit the same entry on laptop and phone before they talk, and you get a `sync-conflict` copy with a timestamp, which Syncthing resolves at the file level while KeePassXC merges by UUID and keeps the older revision in entry history. The real kicker he learned the hard way: deletes propagate too, so a synced copy is NOT a backup — he recommends keeping version history enabled and a real separate backup, and warns that reintroducing an old vault into the synced folder immediately starts distributing it as a change. It trades a bit of convenience for zero server maintenance, but recovery is on you. Solid practical write-up for the self-hosting crowd that doesn't want to babysit a Vaultwarden box.

## 30. Is Debian About To Have Another Systemd Moment? — by Brodie Robertson

![](https://i.ytimg.com/vi/sjE07z8fL5A/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/sjE07z8fL5A
**Karakeep doc:** `zdd94s20vjmnp17jlqd6v6k0`

Brodie Robertson, as ever, smells drama in Debian and can't help but poke at it. He's drawing the parallel between the current AI-infrastructure grumbling and the systemd fights of 2014 and 2019 — both were contentious votes that chased a bunch of people off the project. The 2014 vote in particular is infamous because it's what birthed Devuan, the "Debian minus systemd" distro, after the community was told they could explore alternatives and then, surprise surprise, that never actually happened, and the dissatisfied folks never came back. He's careful to say he's not predicting the exact same thing here with the AI stuff, but the conditions look awfully familiar — enough people genuinely not wanting any part of a direction is exactly what spawned a fork last time. If enough Debian people feel that way again, he wouldn't be shocked to see a competing project materialize. Classic Brodie: pointed, a little conspiratorial, but the historical receipts are real. Short but spicy.



## 31. FerrumPix — desktop photo manager and image editor — by LinuxLinks

![FerrumPix](https://www.linuxlinks.com/wp-content/uploads/2019/10/Photo-Metadata.png)

**Source:** https://www.linuxlinks.com/ferrumpix-desktop-photo-manager-image-editor/
**Karakeep doc:** `eg5v0qtp2ku7i9q6ck8swfkq`

Another week, another LinuxLinks entry proving the FOSS photo world isn't dead. FerrumPix is a VB.NET beast built on Avalonia UI that mashes a photo manager, RAW developer and layer-based image editor into one app — because sure, why stop at just one job. The library side handles ratings, favourites, keywords and saved searches, and it actually respects your existing setup by reading Lightroom, darktable and digiKam sidecar files instead of pretending you don't have years of tagging to lose. The viewer throws in fullscreen mode, slideshows, side-by-side comparison and a proper histogram plus waveform plus RGB parade for the pixel-obsessive crowd. Editing is where it gets real: crops, perspective correction, curves, masks, retouching, text, shapes, layers and actual RAW development with lens corrections for a large catalogue of glass. Batch processing covers everything from renaming and conversion to watermarking and metadata cleanup, and it connects straight to self-hosted Immich and Nextcloud servers for photo transfer. GPLv3, cross-platform Linux/Windows, developed by Bitpainter75 — the sort of tool that makes you wonder why Adobe charges a mortgage for Photoshop.

## 32. Fight Against OS Age Verification Had A Minor Win — by Brodie Robertson

![Fight Against OS Age Verification Had A Minor Win](https://i.ytimg.com/vi/1T3EGzs1yxA/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=1T3EGzs1yxA
**Karakeep doc:** `z7tmf1wa78nsio77obz0qoln`

Brodie's back on his anti-age-verification soapbox, and honestly, with California shovelling this shit into law he's entitled to it. California's AB 1043, the "Digital Age Assurance Act" — the least-terrible of the bunch, he admits — passed the Senate unanimously back in September 2025, was signed in October, and kicks in January 2027, so there's still a window to fight. Unlike the Texas and Utah bills, it doesn't demand a strict ID check; instead OSes and app stores have to expose an age-preference API that buckets users into under-13, 13-16, 16-18 and 18+ cohorts for apps to query in real time. Windows, macOS and ChromeOS already have the infrastructure to do this, but Linux has jack shit — no centralised account flow, no user tracking, and package managers aren't centralized app stores, so compliance is basically impossible for volunteer projects with no legal team. Enter the minor win: the amendatory AB 1856, also introduced by Buffy Wicks and also passed unanimously, adds definitions that could exempt FOSS-licensed OSes (GPL, BSD, MIT, Apache) from "operating system provider" status, and carves out extensions/plugins that run inside a host app. Brodie's read — package managers like Flatpak/Flathub are still covered, AUR helpers probably, though someone's trying to argue Android escapes via AOSP. Not signed yet, still Gavin Newsom's call, and the man signed 1043 so don't hold your breath. His real point lands hard: none of this was ever about protecting kids — it's social media companies offloading liability onto the OS so they can claim "we were told they're an adult." One battle won, the war's still very much on.

## 33. Faved — self-hosted bookmark manager — by LinuxLinks

![Faved](https://www.linuxlinks.com/wp-content/uploads/2026/09/Faved-example.png)

**Source:** https://www.linuxlinks.com/faved-self-hosted-bookmark-manager/
**Karakeep doc:** `pjia3khl5n4y2339ulx4t8dm`

A self-hosted bookmark manager aimed squarely at the hoarders with thousands of links — which, let's be real, is most of us. Faved's headline feature is nested tags, so instead of one flat pile of labels you get actual hierarchies, with tag colours, descriptions, pinned favourites and an optional rollup that folds a parent tag's children into its views. It auto-fetches page titles, descriptions and preview images when you save a link, and it checks for duplicates so you stop saving the same damn thing four times. Search, filter and sort live right in the interface, and bulk actions let you delete, refetch or retag a whole stack of bookmarks at once. The UI switches between card, list and table layouts and plays nice on desktop and mobile, plus it installs as a PWA; browser capture comes via a Chrome extension and a barebones bookmarklet, with Apple Shortcuts as an extra route from Apple gear. Data lives in SQLite when self-hosted, and you can import existing collections from the browsers, Raindrop.io and Pocket. PHP backend, TypeScript/React frontend, MIT-licensed by Denis Dvali — arguably the most relevant piece of software the morning brew threw at you, given what our karakeep workflow does.

## 34. SweetPotatOs – Arch-based Linux distribution for low-spec PCs — by LinuxLinks

![SweetPotatOs](https://www.linuxlinks.com/wp-content/uploads/2026/09/SweetPotatOs-example.png)

**Source:** https://www.linuxlinks.com/sweetpotatos-arch-based-linux-distribution/
**Karakeep doc:** `dnzfxc0y50dlu0ikzaqqvmzn`

Yet another Arch-based distro, this time named like a side dish at a state fair — SweetPotatOs, designed to resurrect old and low-spec PCs. The gimmick is the Sweet Potato desktop on top of Swirl, a featherweight Wayland compositor derived from Sway (and Scroll) that cribs the Niri scrolling-tiling idea: windows line up in columns across one continuous horizontal strip instead of the usual overlapping clutter, with workspaces stacked vertically. It stays compatible with normal Sway tooling, which is genuinely smart, but hands you a preconfigured desktop rather than making you assemble a rolling Arch system from scratch. Touchpad gestures sweep you horizontally between windows and vertically between workspaces, and there are boatloads of keyboard shortcuts for screenshots, screen recording, wallpaper picks, workspace juggling and power controls. Apps in the box: Firefox, Thunar, Geany, foot, mpv, GIMP, MuPDF, swayimg, Transmission, GNOME Disks, btop, Spore for music/web radio and LocalSend for file sharing. Installation's via the graphical Calamares installer, booting with GRUB and logging in through Ly, with pacman plus yay for packages and even a Shelly GUI on top. Rolling release, x86_64, systemd, NetworkManager — an active little experiment if you've got a dusty potato begging for a second life.

## 35. Local AI on the Framework Desktop: Best Models for 32GB, 64GB, and 128GB — by Framework

![Local AI on the Framework Desktop](https://i.ytimg.com/vi/mmntN7zIekU/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=mmntN7zIekU
**Karakeep doc:** `ksgz59gh91lae2twuqa2yvwz`

A long one from Framework's own channel (first half of a paid collab) that actually gets into the weeds of what local AI you can run on all three Strix Halo memory configs, not just the flagship 128GB. The core physics lesson: unified memory means the CPU and iGPU share one pool, and on 32GB the OS, desktop and Chrome eat into your inference budget — so for serious use they recommend a headless, stripped-down Linux install. Model basics are covered properly: gguf quantization via llama.cpp (and the GGUF ecosystem) vs vLLM (enterprise-throughput, but way less standardised quants), with a rule of thumb that 8-bit is ~half of BF16 and 4-bit half that again; the clever UD quants from Unsloth and the new RockmFPX formats aimed at RDNA are called out as promising. Strix Halo's 256 GB/s memory bandwidth is high for an iGPU but LLM inference is hungry, so smaller quants run much faster, and mixture-of-experts models win hard — Qwen 3.8 27B hits 300+ tok/s prefill and ~25-27 tok/s generation, while the MoE Qwen 3.6 35B blows past 1200/90. Speculative decoding (MTP) is a "use it, it's basically free speed" tip. Per-config picks: 32GB gets Qwen 3.8 27B 4-bit as the main rec; 64GB jumps to Qwen 3.5 122B (MoE, 2-3 bit) with room for a couple of models and decent context; 128GB lets you hold multiple models and run big MoEs like GLM 5.3 Flash (321B params) and Inkling Small at 2-3 bit, with image/video/audio gen via ComfyUI. Donato-from-the-future drops that Qwen 3.8 Flash Next and GLM 5.3 Flash just landed too — open-weight world refusing to nap.

## 36. 14 Best Free and Open Source GUI Weather Tools — by LinuxLinks

![Weather tools](https://www.linuxlinks.com/wp-content/uploads/2023/07/aerial-shot-breathtaking-clouds-amazing-blue-sky-up.jpg)

**Source:** https://www.linuxlinks.com/excellent-free-weather-software/
**Karakeep doc:** `x3iirtiiqugttyhbjhsyeqd0`

LinuxLinks rounds up 14 (their body says 12, because of course it does) free and open-source weather widgets for people too posh to just look out the window. The editorial nags early about global warming and London's weird recent patterns, then clarifies weather vs climate in case you skipped elementary science. Most of these tools pull from the free OpenWeatherMap API, which covers current conditions and forecasts for 200,000+ cities — and if you're the type to stream personal weather data, they're pushing WeeWX paired with a Raspberry Pi as the cheap-and-cheerful station setup. The list leans desktop GUI picks: WeeWX for churning out graphs and reports from an actual weather station, Mousam for glanceable current weather in Python, GTK Meteo and meteo-qt for forecast panels (the qt one lives in the system tray), Typhoon for real-time updates, plus KWeather for Plasma heads, and small applets like Nimbus. Terminal people are pointed at a separate roundup rather than being served GUI slop. As usual there's a ratings chart and their verdict up top — a decent bookmark if you've ever wanted a proper little weather station that reports to its own website instead of trusting the iPhone's default app.


## 37. Postmarks - self-hosted bookmark manager and linkblog — by LinuxLinks

![Postmarks](https://www.linuxlinks.com/wp-content/uploads/2025/04/275-bookmark.png)

**Source:** https://www.linuxlinks.com/postmarks-self-hosted-bookmark-manager-linkblog/
**Karakeep doc:** `k652t4v4i3e0ceji1p2yszdp`

Postmarks is a self-hosted bookmark manager and linkblog by Casey Kolderup, and the fun bit is it doesn't sit in a corner sulking — it talks to the Fediverse via ActivityPub. So your bookmark collection is not just a private hoard; your instance gets its own Fediverse identity with a username, display name, bio and avatar, and other Postmarks boxes plus Mastodon can find and interact with it. You add, edit and delete bookmarks in a web UI after auth, import existing ones, and grab a bookmarklet for saving links while browsing. It runs on Node.js or Docker Compose, stores stuff in SQLite, and config lives in environment variables like the public URL and admin credentials. MIT licensed, written in JavaScript — a properly personal, self-controlled take on bookmarking for the chronically link-obsessed.

## 38. I gave up trying to test it — by Less Bitter

![I gave up trying to test it](https://i.ytimg.com/vi/cmDVxxOILq8/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=cmDVxxOILq8
**Karakeep doc:** `sulyps6raebg0ov2noykilfw`

Less Bitter is fed up because AI models got near-impossible to benchmark — there's no honest way to tell how much better one flagship is over the last, so everyone just runs their own little bullshit tests. He blew two hundred bucks on a shootout between Fable 5 and Opus 5, and the funniest symptom he's noticing is "claudisms" leaking into AI-generated games — that same tell-tale aesthetic and voice you spot in text, but now baked into rendered worlds. First challenge was four egregiously impressive Three.js apps: a reading app for his daughter that went from kindergarten to "undefined" as a legit lesson word (peak), a computer-teaching app, a piano improv teacher in full 3D, and an AI factory clone. Second challenge was a thirty-second "five million dollar" promo for G Stack — Opus spit out total ass, while Fable 5.1 hit hard enough that he's downloading it, even if a real video editor would call it slop. His verdict after the whole circus: he still has no idea which model is actually better, and he wants you on his Substack, plus Ship Academy if the AI's got you spinning in circles.

## 39. Schedule - kanban-style planner — by LinuxLinks

![Schedule](https://www.linuxlinks.com/wp-content/uploads/2019/03/project-management-700x450.jpg)

**Source:** https://www.linuxlinks.com/schedule-kanban-style-planner/
**Karakeep doc:** `g7ct1nm5f2izjwxey9g05zrz`

Schedule (aka ThisWeekInMyLife) is a kanban-style planner from dev zhrexl, built for organizing tasks across customizable columns. Yes, it's pitched at planning a week, but the columns aren't chained to individual days — you can add, remove, rename and reorder them into whatever workflow your brain actually runs on. Tasks are cards you drag and drop between columns, and each card can carry expandable/collapsible details so the board stays tidy without throwing away context. It's written in C with GTK 4 and libadwaita, so it slots neatly into a modern GNOME desktop and supports keyboard, mouse and touch input. Data stays local, no cloud hostage-taking. GPL v3, open source — a solid minimal tracker if you want your planning under your own thumb rather than handed to some server farm.

## 40. faster-whisper - reimplementation of OpenAI's Whisper — by LinuxLinks

![faster-whisper](https://www.linuxlinks.com/wp-content/uploads/2020/02/voice-recognition.jpg)

**Source:** https://www.linuxlinks.com/faster-whisper-reimplementation-openai-whisper/
**Karakeep doc:** `nuungkxznnofgx4o4tryifyn`

faster-whisper is SYSTRAN reimplementing OpenAI's Whisper ASR on top of CTranslate2, the Transformer-optimized inference engine — same recognition behavior, way lower latency and a leaner memory footprint than the original PyTorch stack. It runs on CPU or NVIDIA GPU, and throws INT8 quantization at the CPU path for people who actually care about RAM pressure. This is a developer library, not a pretty GUI — you get model acquisition, audio decoding, language detection and segmented transcription through a clean Python API. Standout tricks: batched inference for throughput, word-level timestamps for precise timing, Silero VAD to skip speech-free stretches, and PyAV for audio decoding so you skip the whole "install FFmpeg" chore. It also handles Distil-Whisper checkpoints and fine-tuned models once they're converted to CTranslate2 format. MIT licensed — realistically the fastest cheap path to local/self-hosted transcription that actually moves.

