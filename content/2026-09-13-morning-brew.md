---
date: 2026-09-13
slug: 2026-09-13-morning-brew
tags: Cybersecurity,Web Security,Cloudflare,Internet Technology,Open Source Software,Command Line Tools,Docker,Data Hashing,Software Development,Scala,Refactoring,Linting,Kubernetes,Infrastructure As Code,GitOps,FluxCD,Helm,Entertainment,Theme Park,Family Activities,Tourism,Leisure,PostgreSQL,Database Management,Platform Engineering,Cloud Native,DevOps,Networking,Repository Structure,Artificial Intelligence,Open Source,AI Agents,Context Management,Hardware,Microcontrollers,KVM Switch,Video Streaming,Benchmarking,Storage Systems,Distributed Storage,Performance Analysis,Linux,Data Analysis,Astronomy,Astrophysics,Software Engineering,Cloud Computing,Career Development,Operating Systems,Technology,Learning Path,Programming,Career Advice,Coding Education,Computing,Data Encryption,Tech Careers,Work Life Balance,Mental Health,Personal Growth,Automation,Technology Trends,Television,Celebrity Lifestyle,San Francisco,Home Tours,Information Technology,System Administration,Change Management,Windows Operating System,Software Documentation,Corporate IT,Tech Interviews,Retro Gaming,Video Games,Nintendo,Console Restoration,Sports,Football,FIFA World Cup,Broadcasting,Television Production,Network Engineering,Raspberry Pi,Single Board Computer,DIY Electronics,Computer Science,Routing Protocols,OSPF,Software Management,Gadgets,Debugging,Web Development,Chat Applications,Streaming Data,Object Relational Mapping,JavaScript Development,Command Line Interface,Shell Scripting,GitHub Copilot,JavaScript,Multi-Threading,Concurrency,E-commerce,Payment Processing,Stripe,User Experience,Performance Optimization,Python Programming,Serverless Architecture,Frontend Development,User Interface,UI Component Library,Animations,View Transitions API,Page Animations,Astro Framework,Data Storage,Hardware Engineering,Technology Projects,Technology News,Embedded Systems,Single-Board Computers,Hardware Review,IP KVM,Remote Access,Apple,Mac,Remote Control,Laptops,Product Analysis,Computer Hardware,Mac Computing,Processors,Time Synchronization,Technology Demo,Electronics,Gaming Hardware,Tech Review,Handheld Gaming,Consumer Electronics,Portable Storage,Telecommunications,GPS Technology,Hardware Modification,Timekeeping,Backend Development,Machine Learning,Google Gemini,Generative AI,Productivity,Professional Development,Handwriting,Calligraphy,Art,Writing,Functional Programming,Education,Footwear,Fashion,Lifestyle,Shoes,Distributed Systems,Service Discovery,Text To Speech,Malware Analysis,Reverse Engineering,Binary Analysis,Mathematics,Geometry,Theorem Proving,Mathematical Visualization,Video Editing,Multimedia,Non-Linear Editing,Desktop Applications,Edge Computing,Internet Of Things,Containerization,Linux Distribution,BLAKE3,Rust Programming,File Integrity,Privacy,Captcha,Bot Protection,Document Processing,LaTeX,Typesetting,File Management,Disk Usage,Rust Programming Language,Bootloader,Graphical User Interface,GRUB,Static Site Generator,Go Programming Language,Emoji Picker,Unicode Characters,Linux Software,Productivity Tools,Self-Hosted,Cloud Storage,Web Application,Computer Algebra,Julia Programming,Gaming,Immutable Operating System,Checksum Tool,Data Integrity,Hashing Algorithms,Perl Programming,Static Analysis,Software Security,Network Security,Honeypots,Virtualization
---

# Morning Brew — 2026-09-13

83 bookmarks flushed in from the RSS backlog on the 13th — 47 YouTube videos across 7 channels (Jeff Geerling, Beyond Fireship, The PrimeTime, NetworkChuck, Mischa van den Burg, Kai Lentit, Macho Nacho) plus a stack of linuxlinks.com and 9to5linux roundups, with 7 hand-bookmarked GitOps/homelab bits on top. Transcribed the lot, summaries below.

### Hand-bookmarked

## 1. flux2-kustomize-helm-example — by github.com

![github.com](https://github.com/favicon.ico)

**Source:** https://github.com/fluxcd/flux2-kustomize-helm-example
**Karakeep doc:** `it8vj53om79nnge6313jjm1i`

Flux's canonical multi-env example repo, now updated for Flux 2.7. Assumes two clusters (staging + production) and wires a `HelmRepository` + `HelmRelease` so Flux auto-upgrades podinfo on semver ranges. The layout is boring on purpose: `apps/`, `infrastructure/`, `clusters/`, with a `base/` holding shared Helm releases and per-cluster value overlays. It's the thing everyone copy-pastes from when they can't be arsed to reinvent GitOps. 😐

## 2. Karls Erlebnis-Dorf Oberhausen — by karls.de

![karls.de](https://karls.de/favicon.ico)

**Source:** https://karls.de/oberhausen/
**Karakeep doc:** `rrvzi02h78uljwypym7hzkn4`

The Karls theme park outpost in the Ruhrgebiet, 100% cashless because of course it is. Currently pushing Kürbiszeit (pumpkin season) and a Grusel-Oktober horror thing plus a "Grusel-Nacht." Bring your own food? Fuck no — they want your sandwiches left at home, only a half-liter water and baby snacks pass the gate. Peak German amusement-park capitalism. 🎃

## 3. The Database Dilemma — Mastering PostgreSQL on Kubernetes with CloudNativePG — by andreivasiliu.com

![andreivasiliu.com](https://andreivasiliu.com/favicon.ico)

**Source:** https://andreivasiliu.com/the-database-dilemma-mastering-postgresql-on-kubernetes-with-cloudnativepg/
**Karakeep doc:** `tnen0gylu3yoy6x8njtq5uqf`

The "double replication trap" in one table: Longhorn ×3 plus CNPG ×3 means you write every byte nine goddamn times. His fix is a `strict-local` StorageClass with `numberOfReplicas: 1`, letting CNPG handle HA while the storage acts like a dumb local disk — 3 copies total, native speed. Then a Kustomize base-Application pattern so each microservice's DB is two small YAML files instead of 500 lines of copy-paste. Backups go through Barman/WAL archiving, not Longhorn block snapshots, because snapshotting a live DB mid-flush is how you corrupt shit. 💾

## 4. NetBird Kubernetes Operator — by github.com

![github.com](https://github.com/favicon.ico)

**Source:** https://github.com/netbirdio/kubernetes-operator
**Karakeep doc:** `ds0ozsabmf964rjulrjfryav`

Declarative CRDs (`SetupKey`, `Group`, `NetworkRouter`, `NetworkResource`, etc.) so you manage NetBird peers/routes/groups as YAML instead of clicking through a dashboard. Secrets are auto-rotated, and it works against self-hosted or cloud NetBird. New `NetworkEgress` resource exposes NetBird stuff as Kubernetes services so you don't have to shove a sidecar into every pod. Install is one Helm command off their GHCR OCI chart. 🌐

## 5. Ways of structuring your repositories — by fluxcd.io

![fluxcd.io](https://fluxcd.io/favicon.ico)

**Source:** https://fluxcd.io/flux/guides/repository-structure/
**Karakeep doc:** `himtl7xnfy4s7ugt5h32s51a`

Flux's official rundown of the four repo layouts: monorepo, repo-per-environment, repo-per-team, and repo-per-app. The monorepo is the default answer — `apps/`, `infrastructure/`, `clusters/` with kustomize overlays, trunk-based merges, image automation for staging and manual PR gating for prod. Repo-per-team is for when you've got a platform team dishing out clusters as-a-service and dev teams owning their own app delivery. Useful reference to stop bikeshedding the folder structure. 📁

## 6. OpenCode Plugin — by docs.openviking.ai

![docs.openviking.ai](https://docs.openviking.ai/favicon.ico)

**Source:** https://docs.openviking.ai/en/agent-integrations/10-opencode
**Karakeep doc:** `c4pycdni9vcg49dlj1tmiov0`

OpenViking's memory plugin for OpenCode, giving it cross-project/cross-session recall and indexed repo context via the same stdio MCP proxy the Claude Code and Codex plugins share. Installs with a one-line curl script, registers an `openviking` MCP server exposing 15 namespaced tools (`openviking_find`, `openviking_remember`, etc.). Auto-recall pulls relevant memories into every conversation, and big tool outputs get externalized to a session store past a 20k-char threshold instead of clogging context. 🧠

## 7. Introducing JetKVM Mini — by jetkvm.com

![jetkvm.com](https://jetkvm.com/favicon.ico)

**Source:** https://jetkvm.com/blog/introducing-jetkvm-mini
**Karakeep doc:** `m29rotztpfrmiqxjtc03gvds`

A $39 KVM-over-IP in a matchbox-sized aluminium shell, and the wireless Mini W is $42. Runs on an ESP32-P4X with a hardware H.264 encoder — no Linux, no DRAM, no eMMC — doing 1080p30 (or 720p60) capture over WebRTC. Virtual media loads off a TF card you stuff with ISOs, and it keeps the full JetKVM web UI, cloud, OIDC, MQTT/Home Assistant, and OTA updates. Firmware is open source from day one and the ESP32-C5 on the W model throws in Zigbee/Thread radios for free. Ships Oct 26, 2026. 🔌

### RSS — YouTube

## 8. You're Leaving $500K on the Table by Ignoring Kubernetes — by Mischa van den Burg Highlights

![Mischa van den Burg Highlights](https://i.ytimg.com/vi/gi3p6oFQ0oU/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=gi3p6oFQ0oU
**Karakeep doc:** `sdzkixbabejdmbss9o97c788`

Dude breaks out the "truth serum" of job data to argue Kubernetes isn't dying, it's the actual money printer. 121k openings worldwide, 10% paying over $300k, average $171k — that's $50k over the average software engineer. Do the math and you're throwing away half a mil over a decade by pretending it's overkill. 🙄

## 9. How to actually learn Linux deeply (and where to stop) — by Mischa van den Burg Highlights

![Mischa van den Burg Highlights](https://i.ytimg.com/vi/CustI1yOPmI/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=CustI1yOPmI
**Karakeep doc:** `pxdt0ffmoyoggteb472kgmwt`

Start with Ubuntu Server, then just keep asking "how does this actually work" until you hit the kernel. His whole method is tracing stuff back to its origin — `ps`, `strace`, `pstree` — to actually see what your system is doing instead of trusting the magic. And he stops at the kernel level because, as he puts it, reading kernel source won't land you a six-figure Kubernetes job. It's a decent pitch for his Kubecraft course (8 free hours + 16 more behind the paywall), but the core advice — understand your processes, not your syscall traces — is sound. 👌

## 10. "Should I Still Learn to Code in 2026?" — A DevOps Engineer's Answer — by Mischa van den Burg Highlights

![Mischa van den Burg Highlights](https://i.ytimg.com/vi/EhfrzvRt6yo/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=EhfrzvRt6yo
**Karakeep doc:** `ob1r6sdfuqzql5p8fmz7aw60`

Yes, but just enough to read code and tell when the AI is steering you off a cliff. His bar is Python fundamentals — variables, functions, a bit of OOP — so you can spot when a vibe-coded FastAPI endpoint is wide open with no auth. The guy's not a software engineer himself, just a DevOps bro with thousands of lines of bash, but he's now building apps in weeks with Claude Code that used to take whole teams. The point lands: you can't prompt your way around architecture you've never actually built. 🤷

## 11. Your Laptop Isn't Encrypted. That's a Problem. — by Mischa van den Burg Highlights

![Mischa van den Burg Highlights](https://i.ytimg.com/vi/Y7rEXY_32tA/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=Y7rEXY_32tA
**Karakeep doc:** `kbnc0puyrcvlk4wirbyu7i5d`

A Framework laptop unboxing/setup with Fedora, where the actual point is: encrypt your goddamn disk because no installer does it for you by default. He ticks the LUKS encryption box manually, disables root SSH login ("because I'm not a peasant"), and rants about how insane it is that this isn't the default. The rest is him gushing that the Framework's screen and touchpad feel MacBook-quality, which he genuinely didn't expect. Fine PSA, mostly a flex about the new hardware. 💻

## 12. You're Not Ready for the DevOps Shift to AI — by Mischa van den Burg Highlights

![Mischa van den Burg Highlights](https://i.ytimg.com/vi/tiTdlHg8Drw/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=tiTdlHg8Drw
**Karakeep doc:** `jy8tbmnzz1we6t1ude0a3tgk`

The roadmap he's pushing: DevOps engineers who actually understand AI will eat their competition alive. He debunks the "the model learns as I chat" myth, tells you to go play with Claude/GPT for an hour a day like Anthropic's CEO said, and points at AI infra (GPU on Kubernetes, Kubeflow, Kaito, MLOps) as where the next decade's money lives. His citation is a MinIO article claiming your second hire at an AI startup should be a DevOps engineer. Self-serving, sure, but "GPU passthrough on Kubernetes" is a real, in-demand skill and not wrong. 🎯

## 13. I Quit My Job and My Anxiety Got Loud — Here's What I Control — by Mischa van den Burg Highlights

![Mischa van den Burg Highlights](https://i.ytimg.com/vi/81TjGyUzFRE/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=81TjGyUzFRE
**Karakeep doc:** `d5ji7fayrbfr8rgb429nfrsg`

He quit to go freelance and the anxiety is loud — "what if nobody hires me, what if the money runs out" on loop. The honest bit is the observation that his mind keeps playing out theoretical scenarios that are all wasted energy. His solution is blunt and old-school: you can't control whether you get the gig, only how hard you grind and how many applications you send. It's also a "content creator opens up about personal life" pivot, tied to his half-marathon grit metaphor. A little rambly, but it's real. 🫡

## 14. You're Not Ready for the AI That Replaces DevOps (Here's Why) — by Mischa van den Burg Highlights

![Mischa van den Burg Highlights](https://i.ytimg.com/vi/gVHj2WQyDYQ/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=gVHj2WQyDYQ
**Karakeep doc:** `alppkfr0u4143bnetr80dt70`

Answering "your job is just typing commands, so it's automatable" — no, it's debugging 20 dev teams' broken pipelines while SSHing into servers to figure out if it's a full disk or a network problem. His take on AI replacement: not worried, because no model understands your whole infra, its dependencies, or where to even start. The punchline is solid — AI has to run *somewhere*, so the people who learn Kubernetes and infra will be running the machines that replace everyone else. Cope? Maybe, but it's well-argued cope. 🔧

## 15. MTV Cribs - San Francisco [HD] — by Kai Lentit

![Kai Lentit](https://i.ytimg.com/vi/x0Cr-UhKhZI/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=x0Cr-UhKhZI
**Karakeep doc:** `z88g6oqkthvt0na9400widp5`

A parody of MTV Cribs set in a tech-bro hacker house, and it's genuinely funny. GPUs everywhere — on the table, in the table, under the pool heating it — imported-from-Japan wood "crafted to hit engineers," MIT/Stanford roommates, H1B chess club, black fiber into AWS, and a founder yelling at people to get back to work because they're "wasting my VC money." The punchlines land (the fridge is "walk, don't show that one," the GPU is "in the cloud... it's Azure"). If you've ever been near a startup, this hits a little too close to home. 😂

## 16. *Next-door Sysadmin* — by Kai Lentit

![Kai Lentit](https://i.ytimg.com/vi/sgZCoJ7axdA/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/sgZCoJ7axdA
**Karakeep doc:** `dk1uy0x3q5ieox5vt2d0r2ds`

A ninety-second punchline reel of every corporate IT cliché you've ever lived. Confluence with 4,000 pages that search can't find, Excel as the real database, a "Temp Excel Do Not Use" group with 91 members, SSO that means one password typed nine times a day. The kicker: my job isn't to fix things, it's to be the only one who could. 🥲 Painfully accurate.

## 17. Interview with a Sysadmin in 2026 [Corporate] — by Kai Lentit

![Kai Lentit](https://i.ytimg.com/vi/I7IHInNJZvE/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=I7IHInNJZvE
**Karakeep doc:** `b4orijr5codxghif6uqu182l`

The long-form version of the same bit — a deadpan fake interview where the sysadmin explains he keeps the company running while the company doesn't know and doesn't run well. Every line lands: "there's a form to get admin rights, the form requires admin rights," BitLocker keys stored in Active Directory, a critical macro written by a guy who left in 2013. Turbo Puffer sponsorship shoehorned in at the end, obviously. 😂

## 18. Restoring the Nintendo Console That Nintendo Didn’t Make — by Macho Nacho Productions

![Macho Nacho Productions](https://i.ytimg.com/vi/KmLr0IxVhQ0/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=KmLr0IxVhQ0
**Karakeep doc:** `byy31wav51ssbvw826migtxq`

Tito tears down a Sharp Twin Famicom — the officially-licensed 1986 Famicom + Disk System combo unit Sharp made with Nintendo's blessing. The disk drive belt had snapped (classic), so he swaps it, recaps both boards with a Console5 kit, cleans the read/write head, and straightens the kinked controller cables. Solid retro-restoration ASMR with a Fantik screwdriver and air duster plug stuffed in the middle. 🔧

## 19. I got inside FIFA’s Secret World Cup Broadcast Network — by NetworkChuck

![NetworkChuck](https://i.ytimg.com/vi/LhnH0juUaGw/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=LhnH0juUaGw
**Karakeep doc:** `xg4jh8j5qtgf1ol9cvfs0qtl`

Chuck tours the World Cup's International Broadcast Center in Dallas and nerd-maxes over 150,000 live multicast flows, three 200G fiber links per stadium, and dual red/blue packet streams where receivers just use whichever arrives first. He even got a real PCAP — 530k packets = one second of uncompressed 1080p — and had ChatGPT decode it back into video. He built a couple janky Hermes-agent side projects mid-edit, then prayed for you at the end because that's his thing now. 🎥

## 20. AI’s Impact on Network Engineers | LIVE AMA | Summer of CCNA — by NetworkChuck

![NetworkChuck](https://i.ytimg.com/vi/O7XOUK4B5pg/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=O7XOUK4B5pg
**Karakeep doc:** `lwj56ccxl5ksrhplbjlw3tot`

A Cisco Press author (Jason Gooley) tells the Summer of CCNA crowd that GUIs die by 2030 and it's all chat + MCP agents after that. The whole panel's verdict on "will AI replace network engineers": no, stop doomscrolling — you're a problem solver, not a CLI typist. Best anecdote: a customer's first-year agentic-AI cloud bill was $230 million. The optimism is relentless and borderline exhausting, but they're not wrong. 🤖

## 21. this Raspberry Pi belongs on your wall — by NetworkChuck

![NetworkChuck](https://i.ytimg.com/vi/34D1imLordU/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=34D1imLordU
**Karakeep doc:** `lsjpn8wws2bs6dh1rabkx1bo`

Chuck bolts a Raspberry Pi Touch Display 2 (10-inch portrait) to his wall as a Home Assistant dashboard running Touch Kiosk. The catch that bit him: it only works on Pi 5 / CM, and a fresh Pi 5 needed an EEPROM firmware update before the screen would fire up. Also there's no wall mount included, so it's a drill, screws, and hope. His AI has full access to the Pi to crank out graphs he's too busy to build himself. 🖥️

## 22. OSPF From Zero: Let’s Build the Internet (Well...Almost) | Summer of CCNA — by NetworkChuck

![NetworkChuck](https://i.ytimg.com/vi/HUXUnMbeOyo/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=HUXUnMbeOyo
**Karakeep doc:** `fwim5unti9wj30q9ilixv4cp`

A full live OSPF lab dressed up as a Matrix scenario — DR/BDR elections, route summarization at the ABR, stub vs totally-stubby areas, and OSPF cost to force a preferred path. Jeremy has Claude generate the real-world lab, then proves the DR election needs `clear ip ospf process` because it's non-preemptive, and that specificity wins in the routing table. Runs over into CCNP territory and the "Claude got spanked" bit is half the fun. 🕸️

## 23. You need to switch to Linux RIGHT NOW!! — by NetworkChuck

![NetworkChuck](https://i.ytimg.com/vi/9SDkU5VDQEQ/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=9SDkU5VDQEQ
**Karakeep doc:** `zdz97xa4cznlr3d6yuicva79`

Chuck is losing his goddamn mind over Omachi — DHH's Arch-based "malleable" Linux distro that installs in under a minute and is supposed to finally make Linux not look like ass. It ships with a tiling window manager, a single-process desktop called QuickShell, and an AI agent baked in that can rice your themes (he made a goddamn ThreatLocker theme and a fake Windows XP desktop) on command. The pitch is that it's opinionated like Mac/Windows but actually *yours* — you can change every damn thing. Chuck's clearly about to switch his whole life to Linux off the back of a sponsor segment, which tracks for him.

## 24. This New Device is 10x Better Than Your Router — by NetworkChuck

![NetworkChuck](https://i.ytimg.com/vi/a3RI4DjFBzw/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=a3RI4DjFBzw
**Karakeep doc:** `s8w9yxftwc95f9usn7iked86`

Chuck swaps his editor Mike's garbage ISP router for a mini PC running OPNSense — the open-source firewall that's basically pfSense but not paywalled to hell. He walks through flashing it, setting up interfaces, and enabling DNS-over-TLS plus ad-blocking blocklists, all from the GUI. Then the fun part: he points a Hermes agent (named Pig 🐷) at the OPNSense API with a "cancel/rollback so we don't lock ourselves out" pattern, and it adds Google DNS, sets a DHCP reservation, and blocks the entire country of China via firewall aliases. AI managing your firewall — Mike never has to text Chuck at 3am again.

## 25. Your App Crashed. Now AI Gets to Work. — by NetworkChuck

![NetworkChuck](https://i.ytimg.com/vi/JP9_clebjDE/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/JP9_clebjDE
**Karakeep doc:** `o5wsz9lem445bncdnvynhfc6`

A short on Omachi's crash workflow: any app that dies pops a "click to diagnose with AI" dialog that loads into your preferred harness (Pi, Clot, OpenCode, whatever). The agent loads a diagnosis skill, figures out the crash, then loads a second reporting skill that checks whether it's actually an Omachi bug and files it straight to GitHub via the CLI if you set one up. Then an agent reviews the report and turns it into a PR if it reproduces. It's DHH's whole "iterate on the OS itself" turbo-boost pitch, and honestly it's kind of a slick loop.

## 26. I built a *streaming* AI chat app — by Beyond Fireship

![Beyond Fireship](https://i.ytimg.com/vi/mG8UupGkbGo/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=mG8UupGkbGo
**Karakeep doc:** `ph4wh3kwub313s4m4it3nzem`

Fireship builds a ChatGPT-style streaming chat app in SvelteKit using Vercel's freshly-released AI SDK. The SDK handles server-side text streaming via a `StreamingTextResponse` class, with callbacks you can hook into `onStart`/`onCompletion` to save prompts and responses to a DB. Front-end is just a `useChat` helper that gives you stores to bind and render tokens in real time. Not sponsored, but he name-drops his SvelteKit course like it's a reflex.

## 27. I tried 8 different Postgres ORMs — by Beyond Fireship

![Beyond Fireship](https://i.ytimg.com/vi/4QN1BzxF8wM/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=4QN1BzxF8wM
**Karakeep doc:** `ngkvk58us0fz91ykr6efq3wi`

Fireship runs the same tweet-CRUD app through eight ways to talk to Postgres from JS: raw `pg`, `postgres.js`, Knex, Kysely, Sequelize, TypeORM, Prisma, and Drizzle. The through-line is the eternal tradeoff — raw SQL gives you control but zero type safety, while ORMs give you intellisense but bury you in abstractions. Sequelize's lack of out-of-the-box TypeScript inference gets called a deal-breaker; Drizzle comes out looking like the sensible middle ground. No real winner declared, just the usual "benchmarks exist, go find them" shrug.

## 28. GitHub Copilot now controls your command line... — by Beyond Fireship

![Beyond Fireship](https://i.ytimg.com/vi/P8MfgV9us4o/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=P8MfgV9us4o
**Karakeep doc:** `yzaevdzsqb1qbf662omy58yy`

GitHub Copilot CLI hit general availability, so Fireship turns it loose on the terminal. Two commands: `explain` (what does this alien shell incantation do) and `suggest` (write a command from plain English). It stumbles hard on some things — it botched escaping a `!` in an HTML string and needed a follow-up prompt to serve the app locally — but nails the finale, an `ffmpeg` one-liner to turn an MP4 into a GIF. His take: it makes Linux/PowerShell wizardry accessible to people who'd rather save their brain cells for TikTok dances, and Codium exists if you don't want to pay Microsoft $10/mo.

## 29. PROOF JavaScript is a Multi-Threaded language — by Beyond Fireship

![Beyond Fireship](https://i.ytimg.com/vi/-JE8P2TiJEg/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=-JE8P2TiJEg
**Karakeep doc:** `ymuudd969qn0bgrqajk7am6k`

Fireship debunks the "JS is single-threaded" party line using Node's `worker_threads` and the browser's web workers. He walks through concurrency (one chef, many pots) vs parallelism (multiple cooks), then benchmarks a billion-iteration loop across 1, 2, 4, 8, and 16 workers — going from 44 seconds down to 4.7, roughly 10x. His warning is the useful bit: multi-threading only pays off for CPU-bound work, not I/O, and past your core count you're just burning the machine. The outro gag is an infinite `while(true)` loop that freezes your browser so he can rack up infinite watch time, which is the most Fireship thing possible.

## 30. Build better payment forms using new “embedded” Stripe Checkout — by Beyond Fireship

![Beyond Fireship](https://i.ytimg.com/vi/7WFXl4-aCxs/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=7WFXl4-aCxs
**Karakeep doc:** `uxuj4fb72m87khajqx00vpa9`

Stripe finally lets you embed Checkout directly in your own site instead of punting users to a stripe.com redirect. The gist: create a checkout session server-side with `ui_mode: embedded`, grab the `client_secret`, and feed it to an `<EmbeddedCheckoutProvider>` in React — Stripe handles the rest. A `return_url` carries the session ID back, which you then poll with `checkout.sessions.retrieve` to figure out if they actually paid or bailed. Same locked-down branding (no CSS, just colors/fonts) but zero friction now.

## 31. JavaScript performance is weird... Write scientifically faster code with benchmarking — by Beyond Fireship

![Beyond Fireship](https://i.ytimg.com/vi/_pWA4rbzvIg/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=_pWA4rbzvIg
**Karakeep doc:** `rwh5cldwyatqiror97rswwdn`

Deno ships a built-in `bench` tool and it's genuinely nice for settling "which loop is fastest" arguments. Spoilers: a plain `for` loop crushes `forEach`/`reduce`/`for...of` once arrays get big (function-call overhead), but at ~100 elements it's basically a wash. The real winner is `Set.has()` over `Array.includes()` — a million times faster on large datasets because it's O(1), like a DB index. His takeaway is the boring truth: built-ins are good enough, and you can't guess the bottleneck until you actually measure.

## 32. How I deploy serverless containers for free — by Beyond Fireship

![Beyond Fireship](https://i.ytimg.com/vi/cw34KMPSt4k/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=cw34KMPSt4k
**Karakeep doc:** `qr79h0oirnffhm5jdqzgb7f2`

He built a background-remover Flask app (because `remove.bg`'s Python package is stupid easy to wrap) and Dockerized it so he can drag-drop images straight into Premiere. The free deploy path: push the image to Google's Artifact Registry, then spin it up on Cloud Run with "allow unauthenticated" and the memory bumped to 2GB for the AI model. Cold starts hit 4–5s unless you keep the CPU always-on, which eats your free seconds — fine for a personal utility, not for anything viral.

## 33. This UI component library is mind-blowing — by Beyond Fireship

![Beyond Fireship](https://i.ytimg.com/vi/RPa3_AD1_Vs/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=RPa3_AD1_Vs
**Karakeep doc:** `qkuifdqgx0cg1cymi9bhkc0n`

Aceternity UI is shadcn's coked-up cousin — same copy-paste-the-source model, but every component ships with framer-motion animations that'd take you a weekend to fake. The entire MacBook demo is HTML/CSS (every key is its own div, absolute madman energy), the "sparkles" effect is just tsParticles on a canvas, and the Gemini line-draw is SVG path-length tied to scroll position. His honest take: half these effects are wildly inefficient (`generateRandomString` with a 1500-char loop on every mousemove), but if it looks cool, the code is correct.

## 34. Mind-blowing page animations are easy now... View Transitions API first look — by Beyond Fireship

![Beyond Fireship](https://i.ytimg.com/vi/lsXqparnx24/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=lsXqparnx24
**Karakeep doc:** `fa5gryb9swicoo0bnqwmptfy`

Astro finally got a View Transitions API, which means client-side routing without a full page reload — the one thing that made him skip it and hand-roll "Flamethrower" instead. Hero animations (image sliding from a grid to its detail page) are as easy as slapping the same `transition:name` on the thumbnail and the detail image. The catch: it's ~4.5KB of JS (no more "zero JS" bragging rights) and your per-page scripts stop firing after the first soft navigation, so you have to hook `astro:beforeload` or use `transition:persist` to keep state alive.

## 35. Amazon wouldn’t let me, so I built my own 20TB Snowball — by Jeff Geerling

![Jeff Geerling](https://i.ytimg.com/vi/v0DEI4Ad7Ik/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=v0DEI4Ad7Ik
**Karakeep doc:** `zwwza1zefmdr0p81yp9h3wh6`

Jeff's pigeon experiment gets a sequel: since Amazon won't rent a Snowball to a mere YouTuber, he built his own 20TB hard drive in a rugged case and flew it to Canada. The payoff is real math — 18TB over his fiber would take ~3 days, the flight took 2 hours. Of course he brought a blank drive and proved nothing data-wise, but the actual content is him and Sean Hodgens setting up a 45Drives "Beast" server: 6×16TB Toshiba drives in RAID-Z2, SATA SSD special VDEV (thanks Wendell), all wrapped in their Houston UI on Rocky Linux.

## 36. Raspberry Pi 6 update: You’re not gonna like this... — by Jeff Geerling

![Jeff Geerling](https://i.ytimg.com/vi/ODUbrIuxPtc/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=ODUbrIuxPtc
**Karakeep doc:** `rbkdpzx3b83y23m2rr34tvar`

The Pi engineers' AMA basically confirms the Pi 6 is way off — likely early 2028, thanks to a global DRAM shortage and a "why launch a $70 board into this market" mindset. Don't hold your breath for an M.2 slot or an NPU; it'll just be a faster CPU and I/O, with the CPU doing AI duty. Pi Zero 2 W stock is also strained (substrate supply), but a Zero 3 isn't coming because newer RAM breaks the $15 price point. Silver lining: the Pi 3 B still moves nearly a million units a year, so at least the decade-old board's alive.

## 37. I tested EVERY single IP KVM — by Jeff Geerling

![Jeff Geerling](https://i.ytimg.com/vi/4wYxgPfQAjM/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=4wYxgPfQAjM
**Karakeep doc:** `pvbozfoas5ps5kca6ptwbjtt`

Jeff runs through basically every IP KVM on the market after months (sometimes years) of testing. The short version: they're all "pretty good" now, and you just pick the one that fits your budget and use case — PiKVM is the gold standard but pricey at $275–400, BliKVM and Geekworm undercut it by forking the same software. He opens with the fun disclaimer that one of these boxes literally earned him an FBI visit, because a remote KVM is an open door into your network with BIOS-level access. 🔓 Treat 'em like root keys and firewall the hell out of them.

## 38. Apple FINALLY lets you do this! — by Jeff Geerling

![Jeff Geerling](https://i.ytimg.com/vi/9prKU2Vuo-0/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=9prKU2Vuo-0
**Karakeep doc:** `mrmki22i73plb2bvru8s9mga`

macOS 26.5 adds "always start up when power is connected" — remote power-on for Macs, which homelabbers have wanted for a decade. Jeff pairs it with a Third Reality Zigbee smart outlet in Home Assistant and walks through booting his M4 Mac mini over the network, then SSHing in to unlock FileVault before the boot completes (a Tahoe-era feature). Only works on 2024+ iMacs/Mac minis and 2025+ Mac Studios, so his old Xserve G4/G5s stay cold and silent. ⚡

## 39. The Framework 12 is dead. Apple killed it. — by Jeff Geerling

![Jeff Geerling](https://i.ytimg.com/vi/aPVAnwuSjfk/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=aPVAnwuSjfk
**Karakeep doc:** `i9kmtv3dcn3wwce9zhdw60fk`

Jeff compares the Framework 12 against Apple's MacBook Neo as a graduation gift for his nephew, and it's not close. Even with used RAM/SSD and the DIY build, the Framework runs ~$250 more than the Neo while being ~30% slower on CPU, demolished on GPU, and saddled with a washed-out screen and worse speakers. The only real wins are upgradeability, port selection, and the hinge — none of which justify paying 40% more. His verdict: not a bad laptop, just a bad value. 💸

## 40. Fast Mac networking is too expensive. I fixed that. — by Jeff Geerling

![Jeff Geerling](https://i.ytimg.com/vi/_--JjauL19A/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=_--JjauL19A
**Karakeep doc:** `xd61gk85xew013u41ibvxnxo`

Jeff wants 25Gb networking on his Mac Studio but refuses to drop $1k on a Sonnet Thunderbolt adapter, so he went the server-pull route — a cheap OCP NIC that was $160 in January (now $299). Two problems: old iperf3 capped him at ~15Gb/s until he compiled a newer multithreaded build, and the passively-cooled enclosure was cooking the chips. His fix was printing a custom Noctua-beige fan shroud on a Prusa Core One, tapping ~5V straight off the NIC to power an 80mm fan. 🌬️

## 41. Intel just matched Apple Silicon. Seriously. — by Jeff Geerling

![Jeff Geerling](https://i.ytimg.com/vi/A2B7oI0FYqo/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=A2B7oI0FYqo
**Karakeep doc:** `ujudonlh0hgk5ypmj4tlmblf`

Dell's $699 XPS 13 is a direct shot at the MacBook Neo, and Intel finally learned what "efficiency" means. The new Core 5 chip matches Apple on idle power and compute-per-watt, even beating some M-series Macs on efficiency benchmarks — real all-day battery territory. The iGPU still gets absolutely bodied by Apple's A19, and it ships Windows-only (though Fedora 44 works with a little USB-ethernet coaxing). No headphone jack though, which Jeff calls flatly inexcusable. 🎧

## 42. I'm completely out of time — by Jeff Geerling

![Jeff Geerling](https://i.ytimg.com/vi/h3RW3bSp9v8/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=h3RW3bSp9v8
**Karakeep doc:** `qamppg0pfxdar8ci0x8lz4ol`

Jeff is frantically prepping a vintage NTP time-distribution demo for VCF Midwest. He resto-modded a 2004 Xserve G5 into a stratum-two server (recapped the PSU, coaxed an SSD into the old SATA bays), and is pairing it with a Macintosh SE/30 that predates NTP being built into Mac OS 8.5. The SE/30 needed the full treatment: a newer BlueSCSI, a custom boot image from Infinite Mac, a 3D-printed hard-drive LED bracket, a Noctua fan swap, and a hand-printed CRT adjustment tool. 🕰️

## 43. This PSP Pi mod just keeps getting better — by Jeff Geerling

![Jeff Geerling](https://i.ytimg.com/vi/tNmPTgMoZUI/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=tNmPTgMoZUI
**Karakeep doc:** `eprpc2xpdymkjo8jlzueve8c`

Jeff wasn't a Sony kid but he's getting into the PSP via PiPS, an open-source kit that swaps a PSP-1000's guts for a Raspberry Pi Zero 2 W or CM4. He loves the no-accounts, no-80GB-updates nostalgia of it, and the shoulder buttons, home button, and even the built-in WiFi all work — the PSP's antenna plugs straight into the CM4. The catch is heat: the CM4 runs hot in that thin board, so a Zero 2 W is the smarter pick unless you want the extra horsepower for heavier games. 🎮

## 44. This was never a good deal. — by Jeff Geerling

![Jeff Geerling](https://i.ytimg.com/vi/53AkaYvw63U/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=53AkaYvw63U
**Karakeep doc:** `ecly40uq57d0e5t04xetpybz`

Raspberry Pi is trending for "price issues" because some moron posted a Pi 5 16GB for $426.95. Jeff's verdict: it was never a good deal, now it's just a bad deal — the entire cost is one giant DRAM chip, because AI is eating all the fab capacity. He walked his whole studio/rack and the punchline is he runs almost everything off 1–2GB Pi 4s, so nobody actually needs the 16GB Pi 5. Ragebait, basically — go buy a used mini PC or a $50 Pi 400 instead.

## 45. Unplug it. Move it. It never goes down. — by Jeff Geerling

![Jeff Geerling](https://i.ytimg.com/vi/qclCCQeg-RQ/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=qclCCQeg-RQ
**Karakeep doc:** `cxn5mfroiu47s2y4foiu7bpr`

Jeff builds a portable "network in a box" for his Stratum One NTP demo at VCF Midwest, sponsored by Micro Center. It's a 3U mini rack with a UniFi Cloud Gateway Fiber, a Flex 2.5G PoE switch, a U7 Lite AP, and a 5G backup — 27W at the wall, runs off a tiny UPS or solar. He confirms you can set up the whole UniFi stack with zero Ubiquiti account, and the 5G stick tops out at ~30 Mbps because T-Mobile is the only carrier properly supporting the "RedCap" feature it uses. The proprietary bootloaders bug him (future e-waste), but for 80% of IT folks the slick UI wins.

## 46. I modded a 30-year-old GPS Time Server (Telstra should've) — by Jeff Geerling

![Jeff Geerling](https://i.ytimg.com/vi/CivRNW0b1H8/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=CivRNW0b1H8
**Karakeep doc:** `aurmr71uusrary0a7tn6ons2`

Jeff guts a 1995 TrueTime GPS time server — the kind that took down all of Australia's cell service for 12 hours — and shoves a Pi 5 with a GNSS hat inside as the new engine. The old box is a time bomb thanks to the GPS week rollover bug (10-bit week counter, dead 30-year-old battery, one reboot = thinks it's 2007). He wire-wraps for the first time, burns an LCD chip in reverse, and gets the front display showing a 3D fix and satellite count. All reversible — unplug the Pi, plug the old guts back in.

## 47. 🚨🚨 Working on Omarchy Automation Framework 🚨🚨 — by The PrimeTime

![The PrimeTime](https://i.ytimg.com/vi/Qwekj_ZtmeY/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=Qwekj_ZtmeY
**Karakeep doc:** `vijsmapm86gull13673oo6s6`

Prime stream-vibe-codes his "Omarchy Automation Framework" — a Linear issue with an `agent test` label triggers a Cursor agent that reads the ticket, hits his server through a Cloudflare tunnel, runs the test, and writes results back. The whole point is to let an agent walk the UI the way DHH does for six hours, store every action/log/intent in a database, and flag runs pass/fail. He admits he could've built it in three focused days, but he's got four kids and no time, so the vibes are the workflow. Also a long tangent about DH, racism accusations, particles, and "use Go and HTMX, loser."

## 48. Dunking of Gemini 3.7 — by The PrimeTime

![The PrimeTime](https://i.ytimg.com/vi/FCnaem1SnJU/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/FCnaem1SnJU
**Karakeep doc:** `cqn7tnvbzukga2xhu1lflf35`

Everyone's dunking on Gemini 3.7, but Prime's got receipts: the same people declaring "software engineering is over" back when ChatGPT 3.5 Turbo dropped are now calling Gemini 3.7 garbage. His point — GPT-3.5 Turbo was absolute trash compared to 3.7. Perspective, dipshits.

## 49. Gemini spent all my money — by The PrimeTime

![The PrimeTime](https://i.ytimg.com/vi/7vBb4VvYX7g/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/7vBb4VvYX7g
**Karakeep doc:** `vbxy1pp82sayd5hn225ifcgb`

Prime shows off a 40-minute Gemini session that did nothing but "explore files" — then explore more files — then explore some more files. Cost: $118, because he didn't look at it. He still loves Gemini though. "Do you even understand? You don't."

## 50. How to be a good engineer in 2026 — by The PrimeTime

![The PrimeTime](https://i.ytimg.com/vi/37qyCtvCc4k/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/37qyCtvCc4k
**Karakeep doc:** `tzqzrxdcs77z6t0zs6zy9plx`

Prime's honest answer to "how to be a good engineer in 2026": I truly don't know, good is dead. It depends on what you're building — a website's whole job is to not nuke your database, not cost a kajillion on AWS, be up, and feel smooth. So the whole thing collapses into: use Go and HTMX, loser.

## 51. Beautiful Handwriting — by The PrimeTime

![The PrimeTime](https://i.ytimg.com/vi/kBPjj_3I9PQ/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/kBPjj_3I9PQ
**Karakeep doc:** `tr7nt28b1wu29peztnvlagff`

PrimeTime showing off his backwards "pandriting" on stream and demanding validation that it's beautiful handwriting. A classic 20-second clip of a grown man fishing for compliments. Nothing else happens. It is, in fact, genuinely nice handwriting.

## 52. 🚨🚨 LEARNING EFFECTJS - Learning in the age of AI🚨🚨 — by The PrimeTime

![The PrimeTime](https://i.ytimg.com/vi/O2__t8lceCg/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=O2__t8lceCg
**Karakeep doc:** `t6t6kun67uqvchsstyt6ke6h`

PrimeTime livestreams himself actually reading the EffectJS v4 docs, top to bottom, instead of just asking an AI to explain it. His thesis: you still have to know how to read when coding agents do the writing for you, because AI skips the small concepts and then you slam into a wall. The stream is a slow, honest walk through `Effect<Success, Error, Requirements>`, lazy execution vs Promises, and his own "type masturbation" jokes, with the usual chat chaos in between.

## 53. Your CS Degree Is Teaching You the Wrong Things | TheStandup — by The PrimeTime

![The PrimeTime](https://i.ytimg.com/vi/ZKxq7lgqpIM/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=ZKxq7lgqpIM
**Karakeep doc:** `puiiiv6dyj8e8j9e9zvcuknk`

A panel debate over what CS programs should actually teach in the age of AI agents — Python-first vs going low-level in C/Rust. The crew lands on the point that the real value isn't the language but how easily it "extends downward" into caches, SIMD, and memory, and that those concepts have barely changed since the 1970s. Python is fine as a gateway, the argument goes, but skipping the low-level stuff leaves grads who can balance a tree and understand nothing about the machine underneath.

## 54. Appreciate the Crocs! — by The PrimeTime

![The PrimeTime](https://i.ytimg.com/vi/IPyCUovKzbA/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/IPyCUovKzbA
**Karakeep doc:** `i9ai7ww5lsc981j861v39z5n`

PrimeTime is genuinely wounded that nobody in chat acknowledged his Windows-branded Crocs. Actual Windows Crocs. He points at them and pleads with the audience for a single comment. Streamers, man.

### 9to5Linux (RSS)

## 55. 9to5Linux Weekly Roundup: September 13th, 2026 — by 9to5linux.com

![9to5linux.com](https://9to5linux.com/favicon.ico)

**Source:** https://9to5linux.com/9to5linux-weekly-roundup-september-13th-2026
**Karakeep doc:** `yr84yudihd0c5pql7plhz4o5`

The 309th weekly dump of Linux releases, and it's a busy one. Ubuntu 24.04.5, Debian 13.7, KaOS 2026.09, COSMIC 1.8, KDE Plasma 6.7.5, GIMP 3.2.6, NVIDIA 615, plus new Linux Mint apps and OpenSSL 4.1 alpha. Basically a week's worth of "your distro got an update" spam in one handy page. 😴

## 56. Shelly 3.1.4 GUI Package Manager for Arch Linux Adds More Improvements — by 9to5linux.com

![9to5linux.com](https://9to5linux.com/favicon.ico)

**Source:** https://9to5linux.com/shelly-3-1-4-gui-package-manager-for-arch-linux-adds-more-improvements
**Karakeep doc:** `j6fzj9f2smle8rz5q84x015v`

Shelly, the pacman alternative with AUR and Flathub support, ships another point release a week after 3.1.3. Native builder handles more complex PKGBUILDs, collapsed diffs for AUR reviews, better optional-dep handling, and fixes systemd home-directory isolation. It's incremental polish, not a revolution — but if you live in Arch land it's quietly becoming the GUI to beat. 🔧

## 57. Linux Mint Devs Introduce New EPUB Reader and Calendar Apps — by 9to5linux.com

![9to5linux.com](https://9to5linux.com/favicon.ico)

**Source:** https://9to5linux.com/linux-mint-devs-introduce-new-epub-reader-and-calendar-apps
**Karakeep doc:** `c4qgvioin6awkxrclbn8xaac`

Linux Mint is rolling out two new XApp toys: **Xepub**, a Kindle-ish EPUB reader with bookmarks, annotations, and configurable lookup/translate hooks, and **Clockenstein**, a calendar that handles local, Google, and CalDAV sources with a background sync daemon. Clockenstein even goes read-only when a remote calendar drops so you're not staring at stale garbage. Also got a redesigned Library app. Lands in Mint 23 later this year, based on Ubuntu 26.04. Clockenstein — genuinely one of the better FOSS app names I've seen in a while. 📚

## 58. DietPi 10.7 Adds Support for Containers with Network and ARMv8 VMs — by 9to5linux.com

![9to5linux.com](https://9to5linux.com/favicon.ico)

**Source:** https://9to5linux.com/dietpi-10-7-adds-support-for-containers-with-network-and-armv8-vms
**Karakeep doc:** `pzoq2zmruxoq5g0nc79dxefw`

DietPi 10.7 drops with containers that ship a network stack and SSH pre-installed, ARMv8 VM support, and LubanCat 4 (RK3588S) SBC support. DietPi-Software picks up HomeBox and Scrypted, a new `dietpi-network` tool handles multiple Ethernet/Wi-Fi interfaces, and `run_ntpd` gets renamed to `dietpi-timesync` for consistency. Bug fixes across Pi, Orange Pi, and Radxa boards. If you're still coaxing life out of a Pi 2 in 2026, this is your distro. 🥧

## 59. Shotwell 0.33 Open-Source Image Viewer for GNOME Is Here with GTK4 Port — by 9to5linux.com

![9to5linux.com](https://9to5linux.com/favicon.ico)

**Source:** https://9to5linux.com/shotwell-0-33-open-source-image-viewer-for-gnome-is-here-with-gtk4-port
**Karakeep doc:** `mtjga9ezhvrsgy8nhq8a5mir`

Shotwell 0.33 finally lands after years of work as the first GTK4 release, which means proper Wayland compatibility and drag-and-drop exporting again. Also in the box: keyboard-shortcut help, reworked printing, Toasts instead of clunky dialogs, a "peek password" toggle for Piwigo export, and a pile of bug fixes for faces, slideshows, and background-setting. Publishing now uses a localhost web server instead of a separate auth helper. Slow as hell to get here, but it's a genuinely modern Shotwell now. 🖼️

### LinuxLinks (RSS)

## 60. Directory Checksum - recursively hash directory contents — by linuxlinks.com

![linuxlinks.com](https://www.linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/directory-checksum-recursively-hash-directory-contents/
**Karakeep doc:** `mcc7oa6dwquz41i78jdmdkxb`

A Go CLI that recursively hashes a directory tree and shows you *which* file changed, not just one opaque blob for the whole thing. Built to debug why Docker/BuildKit/Buildah keep nuking your layer cache on COPY/ADD instructions. SHA-1 on files, directory hashes derived from children, empty dirs and symlinks handled sensibly. Genuinely useful if you've ever stared at a rebuild wondering what the hell invalidated it. 🤔

## 61. Scalafix - refactoring and linting tool for Scala — by linuxlinks.com

![linuxlinks.com](https://www.linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/scalafix-refactoring-linting-tool-scala/
**Karakeep doc:** `ae44dktx0v78csfp8i6s1mvz`

Scalafix does both linting and automated rewrites for Scala, with syntactic rules that don't need a compile and semantic rules powered by SemanticDB. Can ban vars, nulls, exceptions, loops and unsafe casts, or organize imports and strip dead code. Configurable via a `.scalafix.conf`, works in CI, and you can restrict it to files changed against a Git ref. For anyone still stuck in Scala land, this is the scalpel. ✂️

## 62. elbencho - distributed storage benchmark — by linuxlinks.com

![linuxlinks.com](https://www.linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/elbencho-distributed-storage-benchmark/
**Karakeep doc:** `wh6b1umcmz3erd9cdmdax9qi`

One CLI to bench filesystems, object stores and block devices, locally or across a cluster via a service mode. Measures latency, throughput and IOPS, with libaio async I/O, GPU storage via CUDA/GPUDirect, live stats, CSV/JSON export, and data-integrity checks. Handles S3 and NVMe-oF too. If fio leaves you wanting on the distributed side, this is the grown-up option. 📊

## 63. 20 Best Free and Open Source Linux Astronomical Data Analysis Tools — by linuxlinks.com

![linuxlinks.com](https://www.linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/astronomicaldataanalysis/
**Karakeep doc:** `jn6grs4y7eqiq1dk3jw3kbb6`

Roundup of 20 FOSS tools for chewing on astronomy data, with FITS as the lingua franca. Top picks are Astropy, CARTA and AstroImageJ, backed by the usual suspects — TOPCAT, DS9, Siril, Gnuastro, SunPy, Gammapy, PyRAF. Astronomers apparently spend more time analyzing data than looking at the sky, so Linux has them covered. 🌌

## 64. 8 Useful Free and Open Source Linux Service Discovery Tools - LinuxLinks — by linuxlinks.com

![linuxlinks.com](https://linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/useful-free-open-source-linux-service-discovery-tools/
**Karakeep doc:** `ql788a7ck1glggc1meyxhujt`

A LinuxLinks roundup of eight free/open-source service discovery tools — etcd, Consul, Nacos, Eureka, Serf, ZooKeeper, Avahi, and dnsdock. Standard LinuxLinks format: a quick explainer on client- vs server-side discovery, then a ratings chart and a link farm of tool blurbs. Useful if you're standing up a service mesh and can't remember which one does what.

## 65. 22 Best Free and Open Source Linux Speech Synthesis Tools - LinuxLinks — by linuxlinks.com

![linuxlinks.com](https://linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/speechtools/
**Karakeep doc:** `mltg18s4qyr222p9eu67a894`

Another LinuxLinks roundup, this time 22 open-source TTS tools ranging from neural heavyweights (Piper, Coqui, Bark, Tortoise) down to formant dinosaurs like eSpeak and Festival. The comment section is half people fighting about whether Julius (a speech *recognizer*) belongs in a TTS list, and half recommendations for Kokoro. Handy cheat sheet if you want local TTS without paying someone.

## 66. Nyxelf - static and dynamic ELF malware analysis - LinuxLinks — by linuxlinks.com

![linuxlinks.com](https://linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/nyxelf-static-and-dynamic-elf-malware-analysis/
**Karakeep doc:** `fj6jpu52vgyfb4w0suhv3r5u`

Nyxelf is a Python GUI framework for analyzing suspicious Linux ELF binaries, combining static analysis (readelf, objdump, Capstone, angr) with a QEMU sandbox built from a minimal Buildroot image. Dynamic runs get traced with bpftrace and Valgrind, network traffic captured with tcpdump, and there's even optional gen-AI summarization of the traces. MIT-licensed, aimed squarely at Linux malware RE nerds.

## 67. GCLC – mathematical illustrations and automated geometry theorem proving — by linuxlinks.com

![linuxlinks.com](https://linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/gclc-mathematical-illustrations-automated-geometry-theorem-proving/
**Karakeep doc:** `du731zazgayj6i9pqx5ym421`

GCLC is a C++ tool for drawing geometry figures and, get this, *proving* geometry theorems automatically. You describe your construction in its own little language, then it throws Wu's method, the area method, and Gröbner bases at it to crank out actual proofs. Exports to LaTeX, TikZ, PSTricks, EPS, SVG — basically everything a masochist needs for their thesis figures. MIT-licensed, Qt GUI plus a WebAssembly browser version.

## 68. Drift – desktop video editor built with Qt 6 and FFmpeg — by linuxlinks.com

![linuxlinks.com](https://linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/drift-desktop-video-editor/
**Karakeep doc:** `bt75t1i4avfn753t5j43vurh`

Drift is a non-linear video editor in C++ that's basically trying to be a free DaVinci Resolve. Multitrack timeline, GPU-accelerated effects, keyframes, green-screen, multicam, scene detection, face tracking, even local speech-to-text models. Bonus weirdness: it ships an optional MCP agent endpoint so external tools can inspect and edit your open project. GPLv3, from CutWire Studios.

## 69. Fedora IoT – container-based Linux distribution for edge devices — by linuxlinks.com

![linuxlinks.com](https://linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/fedora-iot-container-based-linux-distribution/
**Karakeep doc:** `bstkvyixwhm77niv7s69y2jf`

Fedora's official IoT edition, built on rpm-ostree for image-based, transactional updates you can roll back when they inevitably break. Ships Podman for OCI containers, SELinux, and greenboot for health-checking boot/update cycles. It's the "reliable host OS, apps in containers" play for edge hardware, x86_64 and aarch64.

## 70. paq – fast BLAKE3 file and directory hashing — by linuxlinks.com

![linuxlinks.com](https://linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/paq-fast-blake3-file-directory-hashing/
**Karakeep doc:** `x725yt6bauw34ccuinibeurn`

paq is a Rust CLI that hashes files or whole directory trees with BLAKE3, in parallel, and sorts intermediate hashes so results are deterministic. Smart call: it deliberately ignores ownership, permissions, timestamps, ACLs, and xattrs, and hashes symlink *targets* instead of following them. Output lands in a `.paq` file as valid JSON. Clean, focused, MIT.

## 71. Best Free and Open Source CAPTCHA Tools — by linuxlinks.com

![linuxlinks.com](https://linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/best-free-open-source-captcha-tools/
**Karakeep doc:** `wbmzxu7n1g2a27w04obvc9ui`

A roundup of privacy-first bot protection that skips the distorted-text bullshit in favor of proof-of-work — the browser does a tiny computational task, server verifies, done. Three picks: ALTCHA, Cap, and mCaptcha. All self-hostable, none of them farming your visitors' data to a third party.

## 72. 15 Best Free and Open Source Linux Document Processors — by linuxlinks.com

![linuxlinks.com](https://linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/documentprocessors/
**Karakeep doc:** `uelhxia0txvsp6ja44r6rwc9`

Fifteen document prep systems that make you think about structure instead of fonts. Most are LaTeX-flavored — LyX, TeXstudio, TeXmacs, Kile, AUCTeX — but the interesting ones are the typst newcomers: typst itself, Typewriter, Typesetter, and Katvan. If you still hand-format page borders in Word, this list is a polite intervention.

## 73. Excise – interactive terminal storage navigator — by linuxlinks.com

![linuxlinks.com](https://linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/excise-interactive-terminal-storage-navigator/
**Karakeep doc:** `tbaaa0ffc3p16hn3o25cgxax`

Excise is a Rust TUI disk-navigator, a fork and spiritual successor to Diskonaut. It maps your storage visually with color-coded sizes, but the real story is the paranoia: it revalidates every deletion target, won't silently nuke changed/missing/replaced entries, doesn't follow symlinks, and has no trash/undo. Destructive ops stay visible and deliberate, which is exactly right.

## 74. 5 Useful Free and Open Source Graphical GRUB Config Tools — by linuxlinks.com

![linuxlinks.com](https://www.linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/free-open-source-graphical-grub-config-tools/
**Karakeep doc:** `izfud0svqvbacz7tir24e0yt`

GRUB is the thing that actually boots your box, and editing /etc/default/grub by hand still makes me want to throw the machine out a window. This roundup gives you five GUIs so you don't have to. Standouts are YaST2 (the openSUSE one) and Grub Customizer, which most people actually use. If you dual-boot and hate vi, one of these is worth a look.

## 75. Gojekyll – Jekyll-compatible static site generator — by linuxlinks.com

![linuxlinks.com](https://www.linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/gojekyll-jekyll-compatible-static-site-generator/
**Karakeep doc:** `gzduxojlxoerhi4i7b7f465p`

Jekyll but written in Go, so your build stops taking forever. It keeps front matter, Liquid templates, layouts, includes, collections and data files, with a dev server that live-reloads and incremental builds. The catch is it's *substantial* compatibility, not total — anything leaning on random Ruby plugins will need rework. Still, if your Jekyll site rebuilds slower than you'd like, this is a straight swap worth testing.

## 76. rofimoji – emoji and Unicode character picker — by linuxlinks.com

![linuxlinks.com](https://www.linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/rofimoji-emoji-and-unicode-character-picker/
**Karakeep doc:** `goaybbl9pcfgk154wzp1oiw3`

A rofi-powered character picker for emoji and Unicode that can actually *type* into whatever window had focus, or copy to clipboard, or dump the code point. It fuzzy-searches, remembers your recent picks, and does skin tones. Bundles CJK, Font Awesome, Nerd Fonts, kaomoji and more, and works on both X11 and Wayland. If you've ever wanted 😅 without reaching for a phone, this is it.

## 77. chibisafe – self-hosted file uploader and file vault — by linuxlinks.com

![linuxlinks.com](https://www.linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/chibisafe-self-hosted-file-uploader-vault/
**Karakeep doc:** `b6dohcblv668siv5y3mdl8od`

Your own private Imgur/CDN — upload files, get shareable links, browse a masonry gallery, make albums and even text gists. It does S3-compatible storage, chunked uploads, API keys, native ShareX support, and a URL shortener, with no ads or tracking. Runs public, account-based, or invite-only, deployable via Docker. Basically the self-hosting nerd's answer to "why am I paying for file hosting."

## 78. OSCAR – comprehensive computer algebra research system — by linuxlinks.com

![linuxlinks.com](https://www.linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/oscar-comprehensive-computer-algebra-research-system/
**Karakeep doc:** `x96crr1wj83h1vqt0p7jcm20`

A Julia-based computer algebra system that glues together four heavyweight math systems — GAP, Polymake, Antic and Singular — under one programmable roof. You get group theory, algebraic geometry, polyhedral geometry, number theory and exact symbolic arithmetic, all composed in a normal Julia session. Reproducible research calculations instead of copy-pasting between five separate tools. If you do serious math, this is genuinely the grown-up option.

## 79. Kazeta – cartridge-based gaming Linux distribution — by linuxlinks.com

![linuxlinks.com](https://www.linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/kazeta-cartridge-based-gaming-linux-distribution/
**Karakeep doc:** `sa59tn8zkrnrywpitbs4ckv1`

A gaming distro that pretends SD cards are 90s game cartridges — pop one in, boot straight into the game, no desktop, no launcher, no store. It makes /usr, /home and /etc read-only, runs games through Gamescope, and keeps saves on internal storage via overlayfs. Built on ChimeraOS tech, handles native Linux, Windows (via Proton) and retro emulation, and pointedly skips accounts, clouds and subscriptions. A lovely middle finger to modern gaming's always-online bullshit.

## 80. bitrat – fast multi-algorithm file checksum tool — by linuxlinks.com

![linuxlinks.com](https://www.linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/bitrat-fast-multi-algorithm-file-checksum-tool/
**Karakeep doc:** `mptt1h75tx2y11xgubc8tqts`

A Go CLI for hashing entire directory trees to catch bit rot and silent corruption before it bites you. Supports BLAKE3, BLAKE2, SHA-3 and SHA-2, plus HMAC for keyed hashes, and parallelizes across cores for speed. Cross-platform (Linux, macOS, FreeBSD, Windows). If you care whether your backups are actually still intact, this beats praying.

## 81. Zarn - static security analysis for Perl applications — by linuxlinks.com

![linuxlinks.com](https://linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/zarn-static-security-analysis/
**Karakeep doc:** `mbb4fg5qx190952fsh6n13l9`

Zarn is a SAST tool for Perl that actually tries to figure out if a scary construct is *exploitable* instead of just nagging you about style. It parses files into an AST, hunts for dangerous tokens, and runs taint tracking — code injection, path traversal, weak crypto, missing `strict`/`warnings`, all the classics. Single-file scope only for now, so cross-file vulns slip through, but it spits out SARIF and drops right into GitHub Actions. If you're still shipping Perl in 2026, this might be the first security tool that actually speaks your language. 😬

## 82. 5 Best Free and Open Source Linux Honeypot Tools — by linuxlinks.com

![linuxlinks.com](https://linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/best-free-open-source-linux-honeypot-tools/
**Karakeep doc:** `hrciiln6ogtufdt96ctxyuvy`

A LinuxLinks roundup of five honeypots for people who enjoy watching attackers flail. OpenCanary is the multi-protocol decoy, Dionaea traps exploits and grabs malware samples, SentryPeer watches SIP/VoIP fraud, Heralding logs the credentials morons keep typing in, and h0neytr4p is a web-focused trap for hostile HTTP. Different jobs, same idea — dangle a fake target and record the carnage. All free, all open source, all infinitely more fun than reading firewall logs. 🍯

## 83. DRAKVUF Sandbox - agentless malware analysis platform — by linuxlinks.com

![linuxlinks.com](https://linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/drakvuf-sandbox-agentless-malware-analysis-platform/
**Karakeep doc:** `guuwxso3pa68j6otmghe6y7o`

DRAKVUF Sandbox is a black-box malware analysis rig from CERT Polska built on the DRAKVUF virtual-machine-introspection engine. It detonates suspicious files in isolated Windows guests while the monitoring sits *outside* the VM, so there's no agent inside for malware to notice — clever. Web UI plus an API, runs on Xen (KVM for nested testing), needs Intel EPT, and upstream is blunt that it'll demand serious debugging chops. Not a weekend toy; this is for actual labs and IR teams. 🔬
