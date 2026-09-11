---
date: 2026-09-09
slug: 2026-09-09-morning-brew
tags: CLI,Git,Python,Security,scanner,security,wireless,MPD,MPD client,Multimedia,Roundup,Web Apps,free,open source,Education,Rust,TUI,terminal,tui,typing,Database,Documents,database,databases,Productivity,clock,stopwatch,timer,ARM,Distro,Fedora,GNOME,KDE Plasma,distribution,wayland,C++,EDA,FPGA,GUI,IP-XACT,Scientific,system-on-chip,Go,DNS,DNS resolver,DNSSEC,Internet,System Software,networking,privacy,recursive DNS,self-hosting,Reviews,backup,data protection,deduplication,disaster recovery,encryption,restic,QML,Qt,alarm clock,Drivers,News,Nvidia,graphics driver,video driver,Apps,KDE,KDE Frameworks,software suite,OpenSSL,SSL,3D graphics,ArmorPaint,Blender,Graphics,Material Maker,PBR,Substance 3D Designer,adobe,material authoring,procedural textures,texture creation,Cosmic,productivity,task managers,Honeypot,network security,timezone,world clock
---

# Morning Brew — 2026-09-09

Sixteen things you saved by hand, then the RSS firehose. The hand-picked stuff is mostly YouTube — a Proton privacy double-feature, a Teenage Engineering-style Pi, a DIY all-in-one PC, a 30-day Linux phone experiment, and a tour of the distro ladder — plus a spy-satellite-in-your-browser repo, Framework cutting RAM prices, and Neovim finally getting real async. The rest: seven more RSS videos, three 9to5Linux news bits, and sixteen LinuxLinks roundups.

### Hand-bookmarked

## 1. GitHub - bilawalsidhu/gods-eye-view: A spy satellite simulator in your browser, except the data is real. Live open source spatial intelligence on a photorealistic 3D globe. — by GitHub

![GitHub](https://opengraph.githubassets.com/007ff8aeff7a6c2aa6ff5dbe65290ce9c31dbdc4547ee322dc4a6a3dee747eb3/bilawalsidhu/gods-eye-view)

**Source:** https://github.com/bilawalsidhu/gods-eye-view
**Karakeep doc:** `uz83ak0dq1a5yd2eu6qschn1`

21k stars in under three months, so yeah, people noticed. It's a browser-based "spy satellite" sim built on Cesium/WebGL that pulls real geospatial data — flight tracking, satellite positions, photogrammetry — onto a photorealistic 3D globe. The catch is the data is actual, not fake, so you're basically doing OSINT with a pretty UI. License is "NOASSERTION" which is a fancy way of saying the author hasn't bothered to pick one, so don't go building a product on it. Still, 4.4k forks and 175 open issues means it's alive and people are poking at it. If you like maps and hate paying for GIS tools, this is a fun toy.

## 2. 🎬 Video — Stop Using Tailscale. Use Open Source Instead. — by DevOps Toolbox

![DevOps Toolbox](https://i.ytimg.com/vi/7Jja20nWcqo/maxresdefault.jpg)

**Source:** https://m.youtube.com/watch?v=7Jja20nWcqo&pp=ugUEEgJlbg%3D%3D
**Karakeep doc:** `etjchhg6hp4vatqzt8p9khvo`

Transcript came back empty, so I got nothing to work with here. Title says it all though — some DevOps channel telling you to ditch Tailscale for an open source alternative. Probably Headscale or Netbird or whatever the flavour of the month is. Can't vouch for the argument since there's no actual text, so take the clickbait with a grain of salt.

## 3. 🎬 Video — Seven Digital Tools Experts Use To Vanish Online — by Proton

![Proton](https://i.ytimg.com/vi/5mq_7IMJF6g/maxresdefault.jpg)

**Source:** https://youtu.be/5mq_7IMJF6g?si=clT9yV_pOOqkYUvh
**Karakeep doc:** `r4jedaa826wrt34kd73baqe8`

Proton's privacy expert Harley runs through the seven tools she actually uses day to day. GrapheneOS (Android with Google stripped out, per-app network kill switch, and a "duress PIN" that wipes the phone — so spicy the US gov is apparently trying to jail someone for using it), Qubes OS (your life split into colour-coded VMs so a malicious click in one can't touch the others), Tor (three-hop routing, letterboxing so every user looks identical, and yes it's slow as fuck), Organic Maps (OpenStreetMap data, works in airplane mode), an RSS reader (because "I am the algorithm"), F-Droid (open source app store, which Google is trying to kill — she calls it a monopoly), and Cape Mobile (a privacy-first carrier that barely collects anything and lets you rotate your IMSI daily to dodge stingrays). She admits she huffs the privacy paint hard and you don't need all of it — one tool is a start. Fair, honest framing, not preachy.

## 4. 🎬 Video — How to Disappear Online and Become Untraceable — by Proton

![Proton](https://i.ytimg.com/vi/sGbixee041A/maxresdefault.jpg)

**Source:** https://youtu.be/sGbixee041A?si=RImNPP5Xhf8XtpKi
**Karakeep doc:** `ulxmhqml3ru25ooc278xb4zc`

Guy got swatted in 2017 and decided to figure out how to vanish. Five steps, escalating from sane to full tinfoil. Step one: ad blockers, framed as anti-surveillance not anti-annoyance — he claims big tech extracts ~$700/year from your data and uses it for "digital discrimination" (jack up prices if they see you on luxury hardware). Step two: kill the spies in your house — your TV and vacuum phone home to dozens of "trusted partners", so ditch smart devices or Pi-hole the traffic. Step three: live a hundred separate lives — one email is a single point of failure, so run segregated identity stacks (email, phone, card) per silo and never cross-contaminate. Step four: burn the paper trail — own property through trusts and corps so the true owner isn't you, and rent a decoy apartment to satisfy the DMV's address demands. Step five: disappear completely — no phone, no smart devices, no modern car, no KYC travel, carry a passport instead of a driver's licence because it has no address. He's upfront that each step costs convenience and step five is basically permanent paranoia. The "best way to keep a secret is if one of them is dead" opener is a bit much, but the tradeoff framing is honest.

## 5. 🎬 Video — What if Teenage Engineering made a Raspberry Pi? — by PamirAI

![PamirAI](https://i.ytimg.com/vi/lSBIMaUBJJg/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=lSBIMaUBJJg
**Karakeep doc:** `cd2zqimhd1zdfhqfoeumqmzp`

Kevin, co-founder of PamirAI, pitches the Lapis One — a Linux computer that's basically "a Raspberry Pi if Teenage Engineering made a baby". Monochrome Playdate-style display you can write games for or use as a dashboard, A-core (transcript garbled, probably A76 or similar), 8GB RAM, its own battery, fingerprint reader, GPIO header, and a built-in KVM to remote-control other machines. There's a headless agent you can message over a Tailscale tunnel to hand off long-horizon tasks like fixing a PR. Price gag: "$5.99... oh wait, $359 for limited time." It's a product launch video, so take the hype with salt, but the "pretty enough to keep on your desk" angle is genuinely the thing most Linux SBCs get wrong.

## 6. 🎬 Video — The device you've been waiting for! — by andy kirby

![andy kirby](https://i.ytimg.com/vi/z6IOVYemF20/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=z6IOVYemF20
**Karakeep doc:** `jvkh29mans74l6wqu4fvrgf7`

Andy's been heads-down for months building what he calls a world's first: a standalone Meshcore device running on the ESP32-P4, the new high-power Espressif chip. It's a LilyGO T-Display P4 dev board, not a phone, but he's running it as his daily driver with a full "Mesh OS" on top — channel messaging, advert decoding, a terminal app showing raw packets, a UK map with nodes dotted in green, notification badges, and emoji (which he says was the hardest thing to get working, go figure). FreeRTOS multitasking, an RF switch to flip between internal and external antennas in software, always-on display. He's clearly having a blast tinkering and Meshcore just passed 10k users on the map. Early days, screen sensitivity is janky, but the "no Google, no AI watching you" angle is the whole point.

## 7. 🎬 Video — My Daily Tech Stack: Apps and Tools I Actually Use — by Christian Lempa

![Christian Lempa](https://i.ytimg.com/vi/lG-TFEZwywc/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=lG-TFEZwywc
**Karakeep doc:** `ml2j1sl5tm75qztxlfsqlkp8`

Christian walks through his actual homelab workflow, not a boring list. Obsidian for docs (markdown files, backlinks, frontmatter — he's not married to it, just uses what works), Ghostty terminal instead of Warp because Warp locked him in, Open Whisper for local voice-to-text with a "polish" feature that cleans up his German accent before it hits the AI agent, Kolima as a Docker-compatible container runtime (swapped from OrbStack because it's not truly open source), Zed as his editor (written from scratch in Rust, not a VS Code fork), and Orca for orchestrating multiple AI agents in parallel. The meat is a live demo: he has an agent review a Renovate merge request for an update, then spins up a local Docker PoC of an app called Notify, then lets Orca deploy it to a test server behind Traefik with DNS records and a migration plan — all while he goes for coffee. He's blunt that he hates "AI slop" model-review videos but thinks agent orchestration for homelab work is the real value, and that "there's no way going back" from the post-AI era. Solid, practical, and he admits he didn't test anything before recording.

## 8. 🎬 Video — 10 GitHub repos that will save you money — by The Next New Thing

![The Next New Thing](https://i.ytimg.com/vi/rVoAyD2Zrfs/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=rVoAyD2Zrfs
**Karakeep doc:** `g8ge5grirnig9xihreumjiiw`

Andrew runs through ten open-source swaps for the SaaS you're already paying for, and the pitch is simple: stop renting, start owning. The standouts are Vaultwarden (a Bitwarden-compatible server, 66k stars, works with the official apps) and Ghost (55k stars, zero percent cut vs Substack's 10% forever). He's honest about the tradeoffs though — Doodle Note is Mac-only with two stars, Cap's free cloud caps at five minutes, and self-hosting Ghost or Nextcloud is actual work, not a Sunday afternoon. The recurring theme is that your data leaves your machine on the paid stuff, and the free stuff keeps it local. Worth a skim if you're tired of the upsell treadmill, but half of these are "you host it, you own the backups" territory.

## 9. 🎬 Video — Building pi in a World of Slop — Mario Zechner — by AI Engineer

![AI Engineer](https://i.ytimg.com/vi/RjfbvDXpFls/maxresdefault.jpg)

**Source:** https://youtu.be/RjfbvDXpFls?si=GA_dHT3ATOb3VZjT
**Karakeep doc:** `w143sscx4cmsvkwb41z5n0jw`

Mario Zechner (the libGDX guy) gives a three-act talk about why he ditched Claude Code and built his own agent harness called Pi. His beef with Claude Code: the system prompt and tool definitions change every release, it injects "may or may not be relevant" reminders into your context, and there's zero observability or model choice. Pi is deliberately minimal — four tools, a tiny system prompt, and extensions that are just TypeScript modules the agent can write and hot-reload itself. The real meat is act three, where he argues agents compound "booboos" (errors with no learning, no bottleneck, delayed pain) and that a review agent is an ouroboros that doesn't actually work. His verdict: scope tasks so the agent can't miss context, let it wipe on non-critical stuff, and read every fucking line of anything important.

## 10. 🎬 Video — I Tried 100 Self-Hosted Apps - These 10 Are Worth It — by NetBird

![NetBird](https://i.ytimg.com/vi/EtHpkMlyMHE/maxresdefault.jpg)

**Source:** https://youtu.be/EtHpkMlyMHE?si=E_NcH7mOBB7EDUka
**Karakeep doc:** `dd3hl8ggxz7lks3cjvseusux`

Five years of homelab tinkering distilled into a top-ten list, and it's a solid one. The picks: Vaultwarden (self-hosted Bitwarden), Immich (Google Photos replacement with facial recognition and a map view), RustDesk (TeamViewer alternative), AdGuard Home, Home Assistant, Syncthing, Beszel (lightweight monitoring), Ollama, Jellyfin, and Nextcloud. The through-line is sovereignty — everything runs on your own box, gated behind your home network or a NetBird VPN. He's a fanboy for Jellyfin and Nextcloud specifically, and admits he got into all this because Chromecast annoyed him. Nothing revolutionary if you already run this stuff, but it's a clean, honest starter list with the usual "subscribe for the deep-dive videos" outro.

## 11. 🎬 Video — 4:3 PC Games on Android Handhelds — by TechDweeb

![TechDweeb](https://i.ytimg.com/vi/DgqV38F6JsU/maxresdefault.jpg)

**Source:** https://youtu.be/DgqV38F6JsU?si=NKnMb014lFHiqU_E
**Karakeep doc:** `rbum1lalnujquolttrqw0yf6`

TechDweeb shows how to run PC games at proper 4:3 on a 4:3 Android handheld using GameNative, which installs Steam/Epic/GOG games locally with translation layers. The trick is that GameNative defaults every game to 1280x720 widescreen, so you have to go into settings and change the default resolution to something 4:3 (like 1280x960 on the Retroid Pocket Nova), then sometimes also flip the in-game resolution and display mode. He's clear this isn't magic — games that don't support 4:3 won't suddenly do it, and there's no master database, just two Steam curators and trial and error. He name-drops a pile of games that work great: A Short Hike, Balatro, Skyrim, Dirt 3, Halls of Torment, Kingdoms of Amalur, Tomb Raider remasters. The whole thing is wrapped in his usual rambling "more or less obsessed" bit, which is either charming or exhausting depending on your mood.

## 12. 🎬 Video — A new way to build a PC in 2026! — by DIY Perks

![DIY Perks](https://i.ytimg.com/vi/7FStfdGjAwc/maxresdefault.jpg)

**Source:** https://youtu.be/7FStfdGjAwc?si=m5KthJVIrSenphBO
**Karakeep doc:** `a1vyiom6buomm81a8hbtfqr3`

DIY Perks builds a full all-in-one PC out of salvaged parts, and the core idea is genuinely clever: laptop motherboards are dirt cheap because they're only useful as spare parts for one specific damaged model. He pulls a board with an AMD AI chip, RTX GPU, and 32GB of onboard DDR5 for less than a desktop RAM kit alone. The catch is powering it on — no power button, so he reverse-engineers the keyboard connector with a multimeter to find the power pin, then builds a custom ribbon cable out of paper and copper foil tape. The rest is his usual craftsmanship: delaminating a smashed iMac's retina display with a heat gun and wire, a wooden frame, a tripod stand from an old oak floorboard, and a speaker bar with a subwoofer and a hand-built filter circuit. It's a long, satisfying build video with real technical meat, not just pretty shots.

## 13. 🎬 Video — iOS and Android suck now, so I used a Linux Phone for 30 days — by The Linux Experiment

![The Linux Experiment](https://i.ytimg.com/vi/uWWPebWHs8s/maxresdefault.jpg)

**Source:** https://youtu.be/uWWPebWHs8s?si=VF9wdX5sVqVleby1
**Karakeep doc:** `n8gq308yup6hb5zmw6unawt8`

Nick spent 30 days on a Volla Phone Quintus running Ubuntu Touch, including a full week of vacation with no other phone, and the verdict is genuinely mixed. What worked: the interface, Nextcloud apps (Next Notes/Tasks), Sonic Player for music, and the fact that you can plug it into a PC and grab files directly. What didn't: the Morph browser was based on ancient Chromium and "sucked ass" until a beta update, banking apps flat-out don't work on Waydroid, and there's no clipboard or notification bridge between Ubuntu Touch and Waydroid, which nearly broke the whole experiment. The 24.04.2 beta fixed the browser, keyboard, and random disconnects, which is what convinced him to keep it. His honest take: it's not for most people, but for him it's a de-locked-down daily driver he actually enjoys.

## 14. 🎬 Video — Your Life At Every Level of Linux (Ubuntu to Arch) — by DevPsyche

![DevPsyche](https://i.ytimg.com/vi/TRsH-Fd4VvQ/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=TRsH-Fd4VvQ
**Karakeep doc:** `tcmvg50id8hoo15685qdifop`

A tour through the Linux distro ladder, framed as "your distro chose you, not the other way around." Mint is the fridge — it just works and gets out of your way, and the people who stay there are the ones who don't need their OS to have a personality. Ubuntu is where you start calling yourself a Linux user and feel like a hacker for thirty seconds, until you discover Snaps quietly replacing your apps with slow sandboxed containers and realize the distro that was supposed to be on your side just undermined your control. Debian is the granite foundation — old software, boring as a compliment, servers that haven't rebooted since the pandemic. Fedora is the engineering middle ground (Linus runs it, which is the first thing every Fedora user tells you), and Arch is the summit where you hand-partition your drive, break everything twice, and then never shut up about it. The kicker: the most experienced users all land on "I use whatever works," because the distro obsession was never about distros, it was about figuring out how much control and identity you want to tie to a piece of software.

## 15. Framework cuts 32GB and 64GB memory prices for new Laptop 13 Pro, issues retroactive refunds — modular laptop maker secures 'limited quantity' of LPCAMM2 RAM at lower cost — by Tom's Hardware

![Tom's Hardware](https://cdn.mos.cms.futurecdn.net/nQnvmqf85YQXwytYeZhs85-1920-80.png)

**Source:** https://www.tomshardware.com/laptops/framework-cuts-32gb-and-64gb-memory-prices-for-new-laptop-13-pro-issues-retroactive-refunds-modular-laptop-maker-secures-limited-quantity-of-lpcamm2-ram-at-lower-cost
**Karakeep doc:** `hy4lf6c5g2vq0ulzuf9ammb7`

Framework found a "limited quantity" of Micron 32GB/64GB LPCAMM2 modules at lower cost and is passing the savings back — including retroactive refunds to people whose orders already shipped. That's the kind of move that makes you actually like a hardware company. Context matters though: back on July 22 they nearly doubled these same prices, so this is a partial clawback, not a gift. It's first-come-first-serve through Batch 10, and only applies to the Intel Core Ultra Series 3 models — the AMD Ryzen AI 300 ones use SO-DIMMs instead. If you already got a DIY Edition shipped, there's a contact form to swap to the cheaper modules.

## 16. vim.async's Addition Modernizes Neovim's Async Architecture for Better Stability — by InfoQ

![InfoQ](https://res.infoq.com/news/2026/09/async-lua-neovim/en/card_header_image/generatedCard-1788859636927.jpg)

**Source:** https://www.infoq.com/news/2026/09/async-lua-neovim/
**Karakeep doc:** `cc1icksz1ll429xh25d79lk5`

Neovim finally got a real structured concurrency library in core, under the `vim.async` namespace. Before this, plugin authors were juggling bare Libuv callbacks via `vim.uv` or pulling in plenary.nvim / async.nvim, which meant nested callback hell and competing coroutine wrappers stepping on each other. The new model gives you `vim.async.run()` tasks, cooperative scheduling, parent-child task scopes, and primitives like semaphores, timeouts, and `pawait()` (async pcall). Reddit was mostly happy about it, mainly because it kills the plugin dependency collisions. If you write Neovim plugins, this is the thing you've been waiting for.

### RSS — YouTube

## 17. 🎬 Video — This Open-Weights TTS Beat ElevenLabs... Then I Read the License — by Better Stack

![Better Stack](https://i.ytimg.com/vi/kJppefEh2ZA/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=kJppefEh2ZA
**Karakeep doc:** `xwsb1scl1ln4gttp8uqrc7ol`

Breeze TTS 2, a 3GB open-weights model from Breeze Blue, technically beat ElevenLabs on Artificial Analysis — but Josh digs into why that headline is basically bullshit. The cool part is "voice design": you describe a voice in a sentence ("warm, thoughtful, wise old man, think Morgan Freeman") and it generates it with no reference audio, which fills a real gap since Kokoro gives fixed presets and Chatterbox needs a reference clip. The benchmark win is selective though — Breeze has the fewest votes near the top (~1200 vs ElevenLabs' 4500+), and on the apples-to-apples leaderboard where every model gets the same prompt it drops to 3rd among open-weights and 16th overall, behind Mistral's Voxtral. The real problem is the license: code is Apache 2.0 but the weights use a "research and non-commercial" license that explicitly blocks production use, hosting behind an API, AND using the outputs for internal operations — no creator exception, no revenue threshold, nothing. Paying for the API doesn't grant commercial rights to self-hosted outputs either, which makes the whole setup obvious: the open weights are a demo, the API is the product. Verdict: fun to play with, but if you're shipping anything commercial, use something else — Kokoro (Apache 2.0), Chatterbox (MIT), or VoxCPM2 which he thinks crushes them all.

## 18. 🎬 Video — You Need to Get Your CCNA Right Now!! — by NetworkChuck

![NetworkChuck](https://i.ytimg.com/vi/f9IolErKgsw/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=f9IolErKgsw
**Karakeep doc:** `c2kdy027q778m6axbpaiyegy`

A five-reason pitch for getting your CCNA now, and it's mostly an ad for his own academy. The reasons: networking skills are still relevant (AI runs on networks, and no company is letting AI run their network unsupervised), the CCNA opens doors to basically any IT career, and it gets you the interview — his friend Eric couldn't even get a Wells Fargo interview without one. The urgency hook is real though: the CCNA is getting a major revamp announced May 20 2026, and the last day to take the current exam is February 2 2027, so waiting for the "better" new exam is a mistake because all the study material will be slow to catch up. Then it pivots hard into the "Fall Into CCNA" program — 13 weeks, $250, taught partly by him and partly by Jeremy Cioara, with browser labs on real Cisco IOS, quizzes, and a community to keep you from quitting like every other course you've started. He's upfront that the whole video exists to sell this, and it ends with him praying for the audience, which he flags as weird and skippable.

## 19. 🎬 Video — I Go To The Cloud. — by Kai Lentit

![Kai Lentit](https://i.ytimg.com/vi/i5GTwBTCQJI/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=i5GTwBTCQJI
**Karakeep doc:** `k1wgrivezqy41rfx2u90tqy2`

Kai flies to Germany to tour a Hetzner data center in Falkenstein (not Frankfurt, which he calls "Seoul 2025") because he's hosting a new Oserbus server and wants to see the promised land of Hacker News in person. It's a comedy tour: he shows a Nintendo WePass as ID, gets told he can't eat anywhere, walks through like six transponder doors because "we always work in Germany so we keep going like twenty thousand steps per day," and asks the tour guide a stream of troll questions — can he turn down other customers' bandwidth, does hosting petabytes of data get you German citizenship, can he get 20 megawatts by tomorrow. The actual substance: Hetzner's pitch is "do it yourself" — they build and design everything in-house, no outsourcing, which is how they keep prices low, 100% renewable energy, air cooling (no water cooling for GPUs), 99.9% uptime with UPS battery failover and diesel generators, and GDPR compliance as the main draw for international customers. He keeps asking about ping and esports servers, and the guide keeps patiently explaining that no, you can't just take the GPU cables.

## 20. 🎬 Video — LHC Just Abandoned Red Hat For Debian Linux — by Brodie Robertson

![Brodie Robertson](https://i.ytimg.com/vi/LfZnfadTkFs/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=LfZnfadTkFs
**Karakeep doc:** `lripmgz41us3gk9z2exasnji`

CERN is moving the 2,200 machines that power the Large Hadron Collider (17,000 devices) from CentOS over to Debian, and the reason is a single compile flag. They used Scientific Linux back in the RHEL 5/6 days, then CentOS for 7/8, but CentOS got replaced by CentOS Stream — which is the rolling source of RHEL, not a stable clone, and that's a problem for CERN's weird custom hardware where any change needs expensive verification. The straw that broke it: RHEL 9 set the CPU baseline to x86-64-v2, which would kill 47% of their hardware, and RHEL 10's v3 would kill another 17% — 64% of the accelerator's machines just wouldn't boot, and replacing them isn't "buy a new motherboard," it's millions in testing, custom PCB redesigns, more rack space, more buildings, more permits. They had a hard deadline of Q4 2026 because the accelerator runs on a 30-year schedule and that's the next long shutdown window — miss it and you wait seven years. Debian's release cadence is awkward (Bookworm EOLs just before the window, Trixie EOLs mid-window), but Freexian's extended LTS support makes Trixie or Forky actually viable. The remaining pain is packaging: no standard tooling for building/publishing packages, no policy on binary kernel modules, and running multiple versions of the same package is a pain — they're exploring Debosign from Freexian to build their own custom distro.

## 21. 🎬 Video — We brought the Wireless Touchpad Keyboard to PAX West for a typing contest. Here’s how that went... — by Framework

![Framework](https://i.ytimg.com/vi/lpswjPZYXx4/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/lpswjPZYXx4
**Karakeep doc:** `sj1nkqh3phz1z300hxvg02db`

Transcript is basically empty — just a few garbled words ("Oh no! This is adding too much frustration... It's over. Fast is actually"). So no real substance to summarize. From the title it's a Framework short about bringing their wireless touchpad keyboard to PAX West for a typing contest, and the tiny bit of transcript suggests someone struggling with it on camera. That's all I got.

## 22. 🎬 Video — Linux has a BLACK HOLE in it! — by typecraft

![typecraft](https://i.ytimg.com/vi/XURtvqq5ooo/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/XURtvqq5ooo
**Karakeep doc:** `nehp0me1zqvf5y85n0s8acan`

Short explainer on /dev/null. You cat it, it's empty. You pipe /dev/urandom into it, still zero bytes. The trick is the first char in its permissions is a `c`, not `-` or `d` — it's a character device, an interface straight to the kernel that just throws away whatever you write. So it's not a file on disk at all, it's a data black hole. The actual use: redirect output you don't wanna see, like silencing `ls` errors or hiding junk in bash scripts. Fine little 60-second thing, nothing you didn't already know if you've ever touched a terminal.

## 23. 🎬 Video — Website Age Verification is still bad; Discord bringing it back anyway - Talking Heads Ep.449 — by Craft Computing

![Craft Computing](https://i.ytimg.com/vi/sPXF3y81sGk/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=sPXF3y81sGk
**Karakeep doc:** `ccea40uyyrdfj5hnjg44rbzp`

Weekly beer-and-tech live show, and this one's a long ramble. The headline is Discord bringing back age verification — webcam selfie or scan your ID — which Jeff calls stupid, and he's got receipts: Discord leaked 70k scanned IDs three months ago, and a third-party verification company (based in Louisiana, lol) had a live feed of 153 million driver's licenses for over a year, which Krebs traced back by renting a car with his mom. His actual fix is state-level attestation — a binary "is this person over 18" API — not a federal ID system, but good luck getting 50 states to agree on anything. Rest of the show is the usual grab bag: AMD's new Threadripper AI workstation (96 cores, 576GB HBM3E, liquid cooled, probably $100k), Mullvad shutting down their DNS and sponsoring Quad9, a PVE-UPS tool that shuts down Proxmox on a UPS signal, and a long Docker-vs-virtualization fight where Jeff basically says he doesn't trust devs who can't document their dependencies. He also goes off on AI slop — the DMV car-insurance ad that's fully AI-generated and pays zero actual humans — and teases a phone-booth phreaking project with a Mac Mini running a Qwen model that plays a capture-the-flag game when you blow 2600Hz into it. Good episode if you like the format, but it's two hours of two dudes drinking and riffing, so skip around.

### 9to5Linux (RSS)

## 24. NVIDIA 615 Linux Graphics Driver Improves Support for Vulkan-Native Games — by 9to5Linux

![9to5Linux](https://9to5linux.com/wp-content/uploads/2023/03/nv53030.webp)

**Source:** https://9to5linux.com/nvidia-615-linux-graphics-driver-improves-support-for-vulkan-native-games
**Karakeep doc:** `tndqr7d2a15fk7w9aw7794tv`

NVIDIA 615 is out for Linux, FreeBSD and Solaris, and the headline is rev 2 of the VK_NV_low_latency extension, which means out-of-the-box Proton support for NVIDIA Reflex in Vulkan-native games. Also new: cgroups-based memory partitioning and the VK_EXT_cluster_acceleration_structure extension. There's a new RmDisableDisplayGlitchPerfLimit token to cut idle power on some multi-monitor setups, at the cost of possible momentary display glitches. The bug list is the usual grab bag — a file descriptor leak, corruption on Blackwell GPUs with display scaling, resume-from-suspend failures, alt-tab hangs with Smooth Motion. One Blackwell correctness fix may cost a bit of performance unless you recompile with NVCC 13.2.2+. It's a new feature branch, so NVIDIA themselves say maybe don't run it in production yet.

## 25. KDE Frameworks 6.30 Improves Baloo File Indexer, KWallet, and System Monitor — by 9to5Linux

![9to5Linux](https://9to5linux.com/wp-content/uploads/2025/11/kf620.webp)

**Source:** https://9to5linux.com/kde-frameworks-6-30-improves-baloo-file-indexer-kwallet-and-system-monitor
**Karakeep doc:** `or1xq5i5bzlh3q9mi4y9hh5c`

Monthly KDE Frameworks release, 6.30, mostly small quality-of-life stuff across the 80+ Qt add-on libraries. Baloo now correctly ignores Btrfs snapshots in your home dir instead of pointlessly indexing them, which is a real win if you use snapper or timeshift. KWallet stops spamming your log with errors in some configs, and the KDE Connect app no longer eats 100% of a CPU core. Also fixed: very large clipboard images failing to paste, and dialogs once again let you open executable text/script files in an editor after an upstream shared-mime-data change broke it. Nothing flashy, just the kind of papercut fixes that make Plasma feel less janky over time.

## 26. OpenSSL 4.1 Promises Support for DTLS 1.3, IKEV2 KDF, and GREASE, Alpha Out Now — by 9to5Linux

![9to5Linux](https://9to5linux.com/wp-content/uploads/2023/11/opnssl.webp)

**Source:** https://9to5linux.com/openssl-4-1-promises-support-for-dtls-1-3-ikev2-kdf-and-grease-alpha-out-now
**Karakeep doc:** `aacd9ld399huom1zupwq488f`

OpenSSL 4.1 is in alpha, and the big-ticket items are DTLS 1.3, the GREASE mechanism to keep the TLS ecosystem from ossifying, and the IKEV2 KDF. There's also initial Elbrus2000 (e2k) architecture support, plus a pile of crypto optimizations — ML-DSA/ML-KEM NTT on ppc64le, AVX-512 SHAKE x4 for ML-DSA, and AVX-512/VAES for AES-CBC on x86_64. They're also dropping the no-ecdsa and no-echd Configure options because they never actually disabled anything, so you now use no-ec. Windows-on-Itanium and Windows CE targets are gone too. It's a pre-release, not for production, but the post-quantum optimization work is the part worth watching.

### LinuxLinks (RSS)

## 27. detect-secrets - detect and prevent secrets in source code - LinuxLinks — by LinuxLinks

![LinuxLinks](https://opengraph.githubassets.com/1/Yelp/detect-secrets)

**Source:** https://www.linuxlinks.com/detect-secrets-detect-prevent-secrets-source-code/
**GitHub:** https://github.com/Yelp/detect-secrets
**Karakeep doc:** `gg6p9rjps98ee01j71fnxk4o`

Yelp's tool for catching credentials before they land in a commit. The whole point is baselines — you scan once, mark the existing secrets as "known", and then only new ones trip the alarm, so you don't get buried in a wall of false positives on a legacy repo. It's got plugins, filters, and Git hooks, and it's Apache-2.0 so you can actually use it at work. 4.6k stars, Python, still maintained. If your team keeps accidentally committing AWS keys, this is the boring-but-correct fix.

## 28. WHAD Client - Wireless Protocol Exploration Framework - LinuxLinks — by LinuxLinks

![LinuxLinks](https://opengraph.githubassets.com/1/whad-team/whad-client)

**Source:** https://www.linuxlinks.com/whad-client-wireless-protocol-exploration-framework/
**GitHub:** https://github.com/whad-team/whad-client
**Karakeep doc:** `qknenjsjxy5d5lmt757c949t`

WHAD is a framework for poking at wireless protocols — capture, analyse, replay, and experiment with traffic from supported devices. The client is the command-line front end that talks to the actual hardware (the WHAD dongles and boards), so you can script your radio shenanigans in Python instead of clicking through a GUI. It's MIT licensed, 331 stars, and the team behind it is the same crew doing the WHAD hardware. Niche as hell, but if you're into RF reverse engineering or security research it's a clean abstraction over a bunch of messy radio protocols.

## 29. 10 Best Free and Open Source Web-Based MPD Clients - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2021/06/open-source-music.png)

**Source:** https://www.linuxlinks.com/best-free-open-source-web-based-mpd-clients/
**Karakeep doc:** `cqp76ujr7up0ckhb8s4lu9q9`

Roundup of web front-ends for MPD, the server-side music player you run on a headless box and control from your phone or laptop. The list is RompЯ, myMPD, Sola MPD, ampd, CYP, Retrotube, cryMPD, Audioloader, ympd, and hympd — a mix of PHP, Crystal, Go, and Angular/Spring Boot. The comments are the real gold: one guy rage-quit RompЯ because upgrades kept breaking it and it's written in PHP, another just runs the Docker container and calls it a day. If you've got a Hi-Fi hooked to a Pi, myMPD is the safe pick; RompЯ is feature-rich but fiddly.

## 30. typa – minimal terminal typing speed test — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2019/02/young-woman-typing-keyboard.jpg)

**Source:** https://www.linuxlinks.com/typa-minimal-terminal-typing-speed-test/
**Karakeep doc:** `ywrg4ucskk22vfuk8zszyyia`
**GitHub:** https://github.com/uint82/typa

A tiny Rust TUI for testing how fast you type, with timed, word, quote and code modes plus stats and custom themes. It's a 4-star repo so basically a weekend project, but it does the one thing cleanly and doesn't try to be monkeytype. If you live in the terminal and want to check your WPM without opening a browser, this scratches that itch. Don't expect a leaderboard or fancy graphs, it's just a typing test that stays out of your way.

## 31. 17 Useful Free and Open Source Linux Column-Oriented Databases — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2019/03/online-business-database.jpg)

**Source:** https://www.linuxlinks.com/useful-free-open-source-linux-column-oriented-databases/
**Karakeep doc:** `j7vjltt6lbcp9mherlnl8y5r`
**GitHub:** https://github.com/duckdb/duckdb

A roundup of 17 column-store databases, the kind of thing you reach for when your analytics queries are chewing through rows and you need columns on disk instead. The usual suspects are all here — DuckDB for the embedded single-file OLAP crowd, ClickHouse for real-time analytics at scale, Druid and Pinot for the streaming/rollup world, MonetDB and Kudu for the old-school and the storage-engine folks. It's a decent cheat sheet if you're trying to figure out which one fits your workload, but it's a listicle so don't expect deep benchmarks. DuckDB is the one I'd actually point a team at first, it's stupidly easy to drop into a project.

## 32. clock-rs – modern digital clock for your terminal — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2018/06/Clocks-Images.jpg)

**Source:** https://www.linuxlinks.com/clock-rs-modern-digital-clock-terminal/
**Karakeep doc:** `rjn3fjb2fr0f58oql1objzbx`
**GitHub:** https://github.com/Oughie/clock-rs

A configurable Rust terminal clock with timer and stopwatch modes, flexible positioning, colours, date formatting and UTC support. 180 stars, Apache-2.0, so it's a real little tool not a toy. If you want a clock, a countdown timer and a stopwatch all in one TUI without dragging in a GUI app, this does it. The positioning and colour options mean you can actually make it look like it belongs in your setup instead of some default block of text.

## 33. Fedora Asahi Remix – Fedora Linux for Apple Silicon Macs — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/04/Linux-Distributions.png)

**Source:** https://www.linuxlinks.com/fedora-asahi-remix-linux-apple-silicon-macs/
**Karakeep doc:** `ca3nsut0hdhiz7j2aq1tzpo3`

Fedora Linux running natively on Apple Silicon Macs, built on top of the Asahi Linux work that reverse-engineered the M-series hardware. Ships with KDE Plasma on Wayland, hardware acceleration and integrated audio, which is the stuff that used to be a total pain on these machines. If you've got an M1/M2 Mac and want a real Linux distro instead of macOS, this is the most polished path there is right now. It's still not a daily-driver-for-everyone situation — some hardware bits lag — but it's come a long way from the "good luck getting sound to work" days.

## 34. Kactus2 – graphical EDA tool based on the IP-XACT standard — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2019/05/electronic-design-automation-tools.jpg)

**Source:** https://www.linuxlinks.com/kactus2-graphical-eda-tool/
**Karakeep doc:** `h1g9zh6zl2cq0w2p8c04p3n0`
**GitHub:** https://github.com/kactus2/kactus2dev

A C++ graphical EDA tool for designing system-on-chips, packaging reusable IP blocks, building hardware hierarchies and tying hardware and software together, all around the IP-XACT standard. 262 stars, GPL-2.0, so it's a niche but real tool for the FPGA/SoC crowd. If you're doing IP reuse and need a GUI to wire up components and generate the metadata, this is the open-source option. It's not going to replace the big commercial EDA suites, but for IP-XACT work it's genuinely useful and free.

## 35. Talisman – detect sensitive data before Git commits — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/09/Data_security_02.jpg)

**Source:** https://www.linuxlinks.com/talisman-detect-sensitive-data-git-commits/
**Karakeep doc:** `lijit8dnk3jpehc3ct6l24xp`
**GitHub:** https://github.com/thoughtworks/talisman

A Go pre-commit hook from Thoughtworks that scans your outgoing changeset for passwords, tokens, private keys and other stuff you really don't want in git history. 2098 stars, MIT, so it's battle-tested and widely used. The whole point is catching secrets before they get committed or pushed, which is way cheaper than trying to scrub them out of history after the fact. If your team has ever had a "someone committed an AWS key" incident, this is the kind of guardrail that stops the next one.

## 36. 9 Best Free and Open Source Recursive DNS Resolvers — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2023/01/System-Admin.jpg)

**Source:** https://www.linuxlinks.com/best-free-open-source-recursive-dns-resolvers/
**Karakeep doc:** `j68tkt7xtvb2nc400fhhfupq`

Roundup of nine self-hosted recursive resolvers, the usual suspects plus a few I hadn't heard of. BIND, PowerDNS, Knot Resolver, Unbound, Technitium, Hickory, MaraDNS, SDNS and rDNS all get a slot. The pitch is the standard one: run your own resolver so your lookups don't get logged and sold by your ISP or some public DNS provider. Unbound is still the boring, correct default for most homelab people — validating, caching, DNSSEC out of the box. Hickory is the interesting one if you're a Rust nerd, and Technitium is the one with a web UI if you hate config files. Nothing revolutionary here, but it's a decent checklist if you're finally sick of 8.8.8.8.

**GitHub:** https://github.com/NLnetLabs/unbound

## 37. NPBackup – secure and efficient file backup solution — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/01/Backup-software.png)

**Source:** https://www.linuxlinks.com/npbackup-secure-efficient-file-backup-solution/
**Karakeep doc:** `vzbwz656dzuqv82y7ipzw1ff`

NPBackup is a wrapper around restic that gives you the stuff restic deliberately doesn't ship: a GUI, scheduling, monitoring and multi-repo management. Under the hood it's still restic's encrypted, deduplicated engine, so you get the good parts without having to babysit cron jobs and shell scripts. It's Python, GPL-3.0, and aimed at both sysadmins (CLI) and normal humans (GUI). 347 stars, so it's not huge but it's real. If you already run restic and are tired of hand-rolling your retention and forget-to-backup problems, this is worth a look.

**GitHub:** https://github.com/netinvent/npbackup

## 38. Lumalarm – smart alarm clock that wakes your computer from sleep — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/02/038-clock.png)

**Source:** https://www.linuxlinks.com/lumalarm-smart-alarm-clock/
**Karakeep doc:** `posd04h2mk6n6yenfxed1zr8`

Lumalarm is a Qt/QML alarm clock that can suspend your PC and then auto-wake it right before the alarm fires, so you don't have to leave the thing running all night. It's got the usual timers, stopwatch, custom sounds, plus "anti-oversleep challenges" — basically it makes you prove you're actually awake instead of slapping snooze. Cute idea, but it's a 0-star repo with no proper license, so treat it as a toy, not something to rely on for getting to work on time. The suspend-and-wake trick is the only genuinely clever bit.

**GitHub:** https://github.com/shinigami1231111/lumalarm

## 39. Best Free and Open Source Alternatives to Adobe Substance 3D Designer — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/04/3d-render-abstract-background-with-space-your-text-digital-3d-illustration-design.jpg)

**Source:** https://www.linuxlinks.com/best-free-open-source-alternatives-adobe-substance-3d-designer/
**GitHub:** https://github.com/RodZill4/material-maker
**Karakeep doc:** `m5rto23vgpc61cjqc1lbu4c0`

Substance 3D Designer is Adobe's node-based material authoring tool for procedural textures, PBR materials and environment lighting. It's one of the few Adobe apps with actual Linux support (RHEL for enterprise, Ubuntu via Steam), but it's still proprietary, so LinuxLinks rounds up the open source stand-ins. Top pick is Material Maker, a Godot-based procedural authoring and 3D painting app that's the closest match to Designer's graph workflow — it spits out albedo, metallic, roughness, normal and depth maps and even adds model painting on top. Blender gets a nod for its shader-node materials and Cycles baking, and ArmorPaint for GPU-accelerated painting, though neither is a true drop-in for Designer's dedicated graph environment. Verdict: if you want a real Designer replacement, Material Maker is the one — 5.9k stars, MIT, GDScript, actively maintained.

## 40. Tasks – simple task manager for the COSMIC desktop — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2019/04/notepad-pen-with-words-from-todo-list-multicolored-background.jpg)

**Source:** https://www.linuxlinks.com/tasks-simple-task-manager/
**GitHub:** https://github.com/cosmic-utils/tasks
**Karakeep doc:** `admsqw2xdms8o9ht3e8f7dvk`

Tasks is a native COSMIC desktop to-do app written in Rust with libcosmic, so it follows the desktop's own conventions instead of looking like a foreign Electron thing. It's got the basics done right: global search, reminders with desktop notifications, drag-and-drop manual sorting that actually persists between sessions, favourites, and a trash with restore/undo. There's also file watching, theme detection, single-instance handling and Wayland/accessibility support, plus it ships on Flathub. It's a small project — 122 stars, GPL-3.0, by Eduardo Flores — but for a COSMIC user who just wants a clean native task list without the bloat, it's a solid little tool.

## 41. OpenCanary – modular multi-protocol network honeypot — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/Honeypot-banner1.png)

**Source:** https://www.linuxlinks.com/opencanary-modular-multi-protocol-network-honeypot/
**GitHub:** https://github.com/thinkst/opencanary
**Karakeep doc:** `xbsxfoojjmnz7bya3ecs85bd`

OpenCanary is a lightweight daemon that fakes a bunch of network services — Git, FTP, HTTP, MySQL, MSSQL, Redis, RDP, SIP, SSH, Telnet, TFTP, VNC and more — to lure attackers into touching decoys and trip an alert. The point is early warning on recon and lateral movement, and it's deliberately cheap on resources so you can scatter multiple sensors around instead of running one fat honeypot. It's config-driven rather than running deliberately vulnerable apps, supports SNMP via Scapy, Samba file-share monitoring, iptables port-scan detection, honey credentials, and Docker deployment. This is Thinkst's baby (the Canary folks), 3k stars, BSD-3-Clause, Python — a genuinely useful, battle-tested tool if you want to know when someone's poking around your network.

## 42. worldclock-tty – real-time terminal-based world clock — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/02/038-clock.png)

**Source:** https://www.linuxlinks.com/worldclock-tty-real-time-terminal-based-world-clock/
**GitHub:** https://github.com/carlosplanchon/worldclock-tty
**Karakeep doc:** `lau0exmh0ow1rjgbrkfjsq83`

worldclock-tty is a terminal world clock that shows your local time next to a configurable list of time zones, refreshing on an interval. It uses IANA names, can sort by UTC offset, supports 12/24-hour and NATO/military time (including Zulu and Date-Time Groups), and comes with a handful of colour themes plus per-element colour overrides. Config lives under XDG, and it ships with a sane default set of zones across the Americas, Europe, Asia, Australia and the Pacific. It's a tiny one — 1 star, MIT, Python, by Carlos A. Planchón — so it's more "neat little utility" than "project with a community", but if you're juggling people across time zones from a terminal it does exactly what it says.
