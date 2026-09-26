---
date: 2026-09-25
slug: 2026-09-25-morning-brew
tags: Open Source Software,Command Line Interface,Manga,Comic Reader,Linux,Networking,Asset Management,Network Inventory Management,Log Viewer,Software Tools,Text Processing,Multimedia,PipeWire,Audio Routing,Graphical Interface,Terminal User Interface,Container Management,Open Source,Podman,Linux Software,Rust Programming,JSON,Operating Systems,Cybersecurity,Linux Distribution,Privacy,Operational Security,Debian,CachyOS,Live Build,Code Formatting,Web Development,Language Server Protocol,Html,Robot Operating System,Robotics,Data Visualization,Web Dashboard,Telemetry,Bioinformatics,Genetics,Genome Browser,Molecular Biology,Go Programming Language,Static Site Generators,Functional Programming,Software Development,Haskell,Source Code Formatter,Cabal Project,Route Planning,Web Mapping,OpenStreetMap,Geographic Information Systems,Privacy-Friendly,Command Line Tools,Log Analysis,Media Players,YouTube,Video Downloaders,Machine Learning,Artificial Intelligence,Vector Databases,Benchmarking,Data Science,AMD Ryzen,Computer Hardware,Local AI Models,Programming,Gaming,Microsoft,Technology,Technology Trends,Google,Smartphones,Mobile Technology,Android,Homelab,Computing,Events,App Development,Monetization,Software Business,Entrepreneurship,Business Strategy,AI Applications,Xiaomi,Open Weights,Startup,Innovation,Large Language Models,AI Tips,Productivity Tools,AI Agents,Electronics,DIY Projects,Hardware,Tablet PC,Developer Tools,Remote Access,Claude Code,Rust Programming Language,AI Coding Agent,Productivity,Shell Scripting,macOS,Menu Bar Apps,MacOS Apps,Curated Lists,Bash Scripting,Package Manager,Ubuntu,Inference Engine,Generative AI,Deep Learning,Programming Languages,Newsletters,Learning Resources,LLM Systems,Machine Learning Research,Agentic Systems,C++ Programming,Package Management,Dependency Management,Build Systems,Workflow Automation,Wi-Fi Technology,VPN,Networking Hardware,Travel Router,OpenWrt
---

# Morning Brew — 2026-09-25

Yesterday's hoard, brewed. 42 bookmarks — three you grabbed by hand, the rest autohoarded from the RSS feeds. 13 YouTube videos (all transcribed) and 29 articles, heavy on the LinuxLinks roundups and opensourceprojects.dev stubs this time. A couple of 9to5Linux items came through with Cloudflare interstitials for titles, so I fetched the real pages and retitled them. The roundups got their project lists resolved to live links so you don't have to google each one. Let's dig in.

### Hand-bookmarked

## 1. you need to try Paperclip RIGHT NOW! — by NetworkChuck

![NetworkChuck](https://i.ytimg.com/vi/7RVf25Rg0Mc/maxresdefault.jpg)

**Source:** https://youtu.be/7RVf25Rg0Mc?si=nQk2ZzNiFZQao8Fw
**Karakeep doc:** `fyo1i2457deson3w0athk7a8`

NetworkChuck demoes Paperclip, a "meta-harness" from creator Doda that turns your pile of AI agents into an actual company with an org chart. You bring Claude Code, Codex, Hermes, and other harnesses into it, and your agents become employees with managers and tasks. The key design decision: agents talk to each other *through tasks* — intentional and focused — not in some agent-conference-room free-for-all, which Chuck correctly calls low-value. His real-world test: solve the mystery of why flushing the toilet at his studio disconnects everyone from the NAS. He stands up an agentic IT department — Ron the CTO, Fred the Network Engineer, George the Storage Engineer (all pre-trained Hermes agents he "hires" off the shelf), a Claude Code CEO named Dumbledore, plus Codex and local-model agents. After a genuinely impressive run of autonomous diagnosis (network maps, spanning-tree checks, SFP link-down forensics), the verdict lands: four broken links on his MikroTik switch had been failing for 15 months, and the culprit was a bad batch of cheap third-party Amazon SFPs with a 50% failure rate. He swaps in vendor-branded modules and lets it ride for a couple weeks. Also in the mix: routines (scheduled tasks) that run his daily agent standups, a Flare integration that found 76 leaked credentials, and org export/import. Verdict: the "meta-harness" pitch is the interesting part — harness-maxing means you're never locked to one vendor — even if the toilet mystery is mostly a great story.

## 2. I Built a Tablet PC From a Broken Laptop! — by GameRig

![GameRig](https://i.ytimg.com/vi/OO5go2GSdSw/maxresdefault.jpg)

**Source:** https://youtu.be/OO5go2GSdSw?si=ji-hlCEYj4x09w9k
**Karakeep doc:** `bu9uuuolw9eg2x1f6oxn26d5`

GameRig buys a mystery laptop off eBay for under ten bucks, and it arrives as a screenless, keyboard-dead husk — genuinely just a slab of plastic and hope. He doesn't even know the model until the Dell logo pops up on an external monitor like a jump scare. Miraculously it boots straight into Windows, which is the only reason this project doesn't end in the bin. The guts turn out to be an Intel Core i5-5200U, four threads, and 8GB of DDR3 — nothing to write home about, but he paid pocket change so who's complaining. The built-in keyboard is completely dead, confirmed by plugging in an external one that works fine. To get the motherboard out he has to strip the entire machine, prying the keyboard up carefully so he doesn't rip the ribbon cable underneath. Inside is a 120GB SSD and two 4GB RAM sticks, and the board itself looks suspiciously clean — protected by being sandwiched in the chassis. The actual build is a from-scratch 3D-printed case, made possible by the fact that he finally bought his own 3D printer and is absurdly proud of it. Four hours per panel, one botched print from a wrong temperature setting, and a miscalculated mounting screw for the WiFi card that he fixes with a scrap of plastic. The display is a 14-inch portable touchscreen he's reused from prior projects, driven over mini-HDMI and powered by USB-C that also carries the touch input. The speakers are borrowed from that same display, and the power button is nicked from his previous HP build — he asks, gets silence, calls it a yes. No battery though, so the thing has to stay plugged in forever. The end result looks like a wall-mounted picture, and he's calling it one of his most professional builds ever. It pulls 60-70 FPS in Minecraft, sits at 47°C, and doubles as an all-in-one PC when you dock it. For under ten bucks plus a pile of filament, that's a pretty damn good resurrection.

## 3. Pocket-sized OpenWrt router offers dual-band Wi-Fi 5 and Gigabit Ethernet — by LinuxGizmos.com

![LinuxGizmos.com](https://linuxgizmos.com/files/Mango-2-.jpg)

**Source:** https://linuxgizmos.com/pocket-sized-openwrt-router-offers-dual-band-wi-fi-5-and-gigabit-ethernet-2/
**Karakeep doc:** `r6sz5aiucd2jkluqjb96rdse`

GL.iNet's Mango 2 (GL-MG1300) is a pocket travel router, and it's a real upgrade over the original Mango, not a refresh. The headline: dual-band Wi-Fi 5 (802.11a/b/g/n/ac, 2×2 MIMO), Gigabit Ethernet WAN and LAN ports, and a USB 3.0 host port. The old Mango was 2.4GHz-only at 300Mbps; the new one hits 400Mbps on 2.4GHz and 866Mbps on 5GHz.

Inside is a dual-core MediaTek at 880MHz (GL.iNet won't name the exact model), 128MB DDR3L, plus 2MB NOR and 128MB NAND flash. Power switched from Micro-USB to USB-C. The whole thing is 89×63×15mm and 100g.

VPN throughput is where it's actually useful for a travel router: up to 184Mbps WireGuard and 95Mbps OpenVPN DCO, versus 45/11Mbps on the original. Claims compatibility with 30+ VPN providers, plus Tailscale and GoodCloud remote management.

Four ways to get online — Ethernet, Wi-Fi repeater, USB tethering, or a USB cellular modem — and Multi-WAN fails over between them if the primary drops. Runs GL.iNet's OpenWrt-based firmware with separate main/guest/IoT networks, DNS, IPv6, port forwarding, and dynamic DNS.

Two caveats that matter. GL.iNet hasn't announced pricing or availability yet. And the Mango 2 is currently unavailable in the US due to "recent FCC-related developments" — read that however you like. For a compact travel router with real VPN throughput and cellular fallback, it's a solid spec sheet. Just don't hold your breath for a US release date. 🧳

### RSS — YouTube

## 4. Why You Can’t Trust Vector Database Benchmarks — by Better Stack

![Better Stack](https://i.ytimg.com/vi/NMJk6CO9vos/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/NMJk6CO9vos
**Karakeep doc:** `dwjgcj94dktqlapq18xd4mvt`

Picking a vector database is a fucking minefield, and the reason is obvious once you look: every vendor publishes a benchmark page and every one of them wins their own benchmark. That's not always flat-out lying, though. Honest vector-search benchmarking is genuinely hard, and nearly every public benchmark cuts corners and bakes the results.

Take recall. It measures "of the true nearest neighbors for a query, how many did the engine actually hand back?" But to measure recall you need to already know the ground truth — someone has to compute the *exact* nearest neighbors first, not approximately. At ten billion vectors × 120k queries, that's north of a quadrillion distance computations (10^15). That's precisely why nobody had done it. Qdrant went and burned a pile of GPU compute to produce a 10-billion-vector dataset, then this guy ran it against four engines: Qdrant, Milvus, Elasticsearch, and pgvector.

Here's the interesting bit — where each engine taps out. Elasticsearch can't break 95% accuracy no matter how hard you push it. Qdrant and Milvus both hit 98%. So they're good at different things: Elasticsearch is the fastest way to be *roughly right*; Qdrant is the one that's both fast and precise. The takeaway isn't the specific numbers, it's that we finally have a dataset big enough to benchmark these things honestly against each other. And it's a reminder to stay skeptical of vendor-published numbers — benchmarking vector DBs is super hard, and nothing is black and white. Test it yourself. The "truth" is in the ground-truth dataset, not the marketing page.

## 5. Donato has a few tips for running local AI models on the AMD Ryzen AI Max+ 395 Framework Desktop. — by Framework

![Framework](https://i.ytimg.com/vi/QIEdK8haaTw/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/QIEdK8haaTw
**Karakeep doc:** `mytwt0zemghvfhg91bn4yvw6`

This is a ~40-second Short, so the transcript is thin. Donato's one real tip for image and video generation on the Ryzen AI Max+ 395 Framework Desktop: these diffusion models start from noise and strip it away over a series of "de-noising steps," and some workflows use anywhere from 20 to 50 of them. On a strict scheduler that adds up to a lot of wall-clock time.

His fix: use workflows that apply LoRA adapters — small adapters trained on top of the base model — rather than grinding through full de-noising passes every time. That's the whole video. Practical if you're already sitting on a Framework Desktop with one of these chips and wondering why your image gen is slow, but it's a teaser, not a tutorial. Don't go in expecting benchmarks or actual numbers; there are none.

## 6. Microsoft’s AI just banned a game with no game in it — by Better Stack

![Better Stack](https://i.ytimg.com/vi/De9OigyLipg/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/De9OigyLipg
**Karakeep doc:** `pvhfi4aa18lev4n26rhejpyb`

A long-running open-source project just got kicked off the Play Store because an AI decided it was ripping off Minecraft. It's called Luanti — you might still know it as Minetest. It's a voxel game *engine*, not a game. It ships with no games and almost no assets. The team even posted a screenshot of every texture in the entire app and they all fit on one screen.

In August a DMCA notice was filed against Luanti on Microsoft's behalf by a company called Tracer AI, claiming Luanti used copyrighted Minecraft assets. The "evidence" was laughable: a US copyright registration number for Minecraft Java Edition 1.9, and nothing else. No specific asset, no filename, no pointer to what was actually copied. Google delisted the app anyway.

And it's not even the first time. Tracer filed basically the same notice in 2023; Luanti appealed and won. Then this year Tracer hit a company called Alumira with another one. Same automated system, firing the same bogus claims at different products over and over. A bot saw 3D blocks, matched "distribution styles," and assumed it was copied. That's the part that should worry you: once copyright strikes get automated like this, the burden lands entirely on devs to prove the AI is wrong and fight back. Expect this to become routine.

## 7. This Might Be the Best AI Release of 2026 — by The PrimeTime

![The PrimeTime](https://i.ytimg.com/vi/BHPDsGVciDk/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=BHPDsGVciDk
**Karakeep doc:** `xfp2xvys243za1frh98r5iux`

This isn't a chatbot and it's not going to usher in the apocalypse — it's the first AI release the guy's actually been excited about in a long time. It's called **Jev**, a "decision model" built for System 1 thinking: fast, cheap, instant yes/no classification, not conversation. You can't chat with it. You hand it a *state* (what the world looks like) and a set of questions that each must be answered yes/no, and it answers them all in parallel.

The pitch comes straight from their manifesto — "composable AI, build pro not God" — and the early-cars-had-whip-holders analogy: we're using LLMs (horse-shaped cars) for decision-making when they're not actually good at it. Jev claims to be 190× faster and 444× cheaper, though the video admits nobody's sure which model that's benchmarked against. What you get: a state plus typed questions — "choice" (pick one of N), a Bernoulli-derived "nuel" that scores 0–1 confidence, etc. His demo: "state: I pooped my pants at a weightlifting competition" → 95% confidence "go clean up, do not keep working out."

Where it shines: real-time moderation. He ran a Super Smash Bros event where 2,000 people were feeding messages to four characters. The old flow — batch messages through a slow agent to filter the inappropriate ones — took ~90 seconds of dead air. With Jev he could classify each message as it arrived, in parallel, and pipe it straight to code. He also had Jev playing Balatro live (wins ~30% of the time, still refuses to grab a joker) and playing Doom/Mario by answering "dodge or stand still / fire or hold fire" questions every frame.

The killer stat: 345 input tokens for the Smash question, charged on input only, at **$42 per billion tokens**. He estimates you could ask that question ~3 million times for $44. It's named after Jevons Paradox — the cheaper it gets, the more you use it. Verdict: it's a classification hammer, and a shocking number of "AI" problems (content moderation, context filtering, test assertions, computer-use routing) are secretly just classification problems. This is worth actually trying, not just eyeballing.

## 8. Google is locking Android behind Pixel — by Better Stack

![Better Stack](https://i.ytimg.com/vi/o-7Ohr_2Mlg/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/o-7Ohr_2Mlg
**Karakeep doc:** `zvmi7w4op227e6iugfxd198d`

Android's been "open source" for ~15 years, but the version that just shipped to Pixels now has developer APIs that no other manufacturer is allowed to touch. The GrapheneOS team — the folks who build the hardened Pixel Android — spotted it. Android 17 QPR1 (quarterly platform release) rolled out to Pixels on September 15th, and it's the first Android release since Honeycomb in 2011 to add *new* app APIs without publishing them to AOSP.

Those APIs are Pixel-only right now, and it didn't happen overnight. Starting with Android 16, Google stopped publishing the first and third quarterly releases to AOSP entirely — only the yearly release and the second quarterly drop make it out. QPR1 goes a step further because one of those private releases now actually *contains* new dev APIs, so every other manufacturer waits until December for QPR2. And it gets worse: the September Pixel security bulletin includes fixes to standard Android platform code that non-Pixel phones also run, but those fixes weren't published to the normal bulletin either. Other manufacturers wait until December for those too.

GrapheneOS actually finished porting QPR1 *before it launched* — they're just not allowed to ship it. So Google's own phones now get months of head start on APIs and security fixes over Google's own partners. Android is still technically "open source," but the open part shrinks a little every quarter. The moat is real and it's being poured in quarterly installments.

## 9. I’m starting a homelab festival (you’re invited) — by Jeff Geerling

![Jeff Geerling](https://i.ytimg.com/vi/7I0pjHC4U7I/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=7I0pjHC4U7I
**Karakeep doc:** `t60ydk4ue5qu8pbskukamfq1`

Jeff Geerling is done with the "I'm on screen, you're in the comments" loop. He's been building mini racks and testing mini PCs for years, and the best part of every convention he's attended was never the talks — it was the hallway track, actually meeting the people he interacts with online. So he's throwing a festival.

**HomelabFest**, September 12–14, 2027, in Saint Charles (his hometown, closer to the St. Louis airport than the city proper). He's inviting the homelab content creators he knows, and says that list is only the beginning, plus he's trying to pull in the homelab and self-hosting companies that actually contribute to the community. Whether you run an old laptop as an everything-server or a 42U rack doing HPC, there's something for you. If you've got a project, rack, or build to show off, community tables are available at basically cost — or just bring the cool build for someone to sign.

The advice he got when planning: (1) don't do it, you'll go insane — ignored, obviously; (2) don't go into massive debt doing it — which is where the sponsors, especially this year's platinum ones, come in. Registration just opened and there are **250 super-early-bird tickets** that disappear in a couple weeks. All info at homelabfest.org. Why Wojtek cares: it's a homelab meetup actually worth flying to, and the super-early-bird window is genuinely short. If you're remotely on the fence, register now, not in a month when the price doubles.

## 10. Your AI App Works. Can You Sell It? — by NetworkChuck

![NetworkChuck](https://i.ytimg.com/vi/zXeL8KbDmi4/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/zXeL8KbDmi4
**Karakeep doc:** `q3uage4tvnvgc47qomjg6qwx`

Same NetworkChuck short as the one below — a Vanta ad wrapped in a "can you actually sell your AI app" framing. The thesis: building something that works is easy, selling it to an enterprise is where it dies. The one question that kills the deal isn't "is your model good," it's "are you SOC 2 compliant." Vanta pitches itself as an "agentic trust platform" that gets you compliant fast — SOC 2, ISO 27001, HIPAA, GDPR — then keeps watching your controls so you stay compliant. A Vanta agent lives in Claude Code and Cursor so you fix compliance stuff without leaving the terminal. The whole thing is a $1,000-off promo code for vanta.com/chuck. This one has no transcript in the hoard, so the summary below from the duplicate carries the actual substance. Real talk: it's a sponsored shill, but the "trust closes enterprise deals" point is legit if you've ever watched a founder get yanked off the roadmap to screenshot stuff for an auditor.

## 11. Your AI App Works. Can You Sell It? — by NetworkChuck

![NetworkChuck](https://i.ytimg.com/vi/d1i1V4StMVI/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/d1i1V4StMVI
**Karakeep doc:** `ptoeorpl3y3er3e7j9z4yo7k`

A NetworkChuck short that's 100% a Vanta ad. The hook: you built something with AI, a big company wants to buy it, and the deal stops dead on one question — not "how good is your product," but "are you SOC 2 compliant?" Now your engineer's been pulled off the roadmap to grab screenshots for an auditor, and every enterprise call is a fire drill. Vanta's pitch is "agentic trust platform" — marketing speak for "we make you compliant fast." It covers SOC 2, ISO 27001, HIPAA, GDPR, and then keeps monitoring your controls so you stay that way. The proof point is Hyperbound, an AI startup (Y Combinator, two founders, zero security team) that got compliant during YC before big customers showed up — one deal needed ISO 27001 for a $1.5M contract in under three months, and they pulled 1,400 customers in a year. Vanta's agent now lives in Claude Code and Cursor, so you fix compliance without leaving the terminal. Verdict: it's a shill with a promo code, but the "trust is what closes enterprise deals" observation is the one true thing here.

## 12. Xioami Released The World's Best Open-Weights Model — by Better Stack

![Better Stack](https://i.ytimg.com/vi/jmER3mBbMY8/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/jmER3mBbMY8
**Karakeep doc:** `l41nz9p80o3wq96vj0t6t9le`

Xiaomi — the phone company — just dropped what Better Stack calls the most powerful open-weights model in the world, MiMo version 2.6. It can build interactive games, Blender models (a car, a ship, a house), and websites that don't look AI-generated at all. The demo site, "Salazar," is genuinely pretty. On the Artificial Analysis benchmark it beats Kimi, DeepSeek, and Qwen, and matches Grok 4.7 on x-high reasoning while being 28x cheaper per task. Three flavors: Flash, Pro, and Pro Ultra Speed (up to 20x faster output at equal quality). Pro pricing is 43¢ in / 87¢ out per million tokens — cheap enough for intense agentic workflows at a fraction of closed-source cost. The catch is raw speed: ~54 tokens/sec, which still beats Grok but is 4–5x slower than latest DeepSeek Flash and Gemini Flash. So for a fast model behind your own APIs, those still win; for long tasks you can leave running, MiMo is a solid pick. Verdict: another open-weights model eating the mid-tier, and the "cheap per task" angle is the part that matters.

## 13. This $40M Startup Was Replaced After Just 3 Days! — by Better Stack

![Better Stack](https://i.ytimg.com/vi/9ywqgu3R_mw/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/9ywqgu3R_mw
**Karakeep doc:** `thqu92shlna98yn2bhynhojq`

TypeSafe AI went viral with "Jeff" (transcript spelling), a $40M-valuation model for classification and structured decisions inside your software — runs up to 200x faster and 400x cheaper than doing the same work with a normal LLM. Three days later a free open-source alternative called Layer dropped with better performance. Both are essentially "smart if statements": feed it a question (e.g. "is this email spam?"), get a probability back, then act on it. The trap here isn't structured output — both guarantee the shape you define — it's correctness. Jeff is wrong about a quarter of the time (0.727 accuracy on a typed-decisions benchmark); Layer beats it at 0.766, and it's free. The punchline Better Stack draws: in 2026 the lifespan of software has shrunk to days. Layer's on Hugging Face and is genuinely good for cheap, fast decisions over large datasets. Verdict: the "probability, not certainty" caveat is the useful bit — these things confidently mark non-spam as spam, so treat the score as a signal, not a verdict.

## 14. Getting the most out of Opus 5.5 — by Theo - t3.gg

![Theo - t3.gg](https://i.ytimg.com/vi/ejjBbaq9RmY/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=ejjBbaq9RmY
**Karakeep doc:** `p8kkoij6lvahmj21njq479m4`

Theo walks through Addy Osmani's (ex-Chrome, now Anthropic) official guide to squeezing value out of Opus 5.5. The core thesis: high-tier models now work well if you *tell them what "done" looks like* — name the finish line, give the whole task in one message, and they'll grind until they hit it. Otherwise they stop at random to ask permission. His headline advice is "prompt wider": hand over the whole task, define done states ("build this, verify with a screenshot, file a PR after"), and let it run. Don't tell it to "think hard" — it already knows how much to think, and reasoning levels are "think up to this much," not "think this much." That's why he's on a crusade against Max mode: on Skate Bench it went from 338 avg tokens/response to 5,000, average duration 6s→50s, worst case 600s, 13x the cost and 15x the tokens for *one* extra correct answer (78%→79%). He calls it "jack-fuckin-shit." Other gold: steer long runs mid-flight (modern models treat interruptions as steering, not a reason to drop prior tasks), name the stops you want in claude.md, split big audits/reviews across subagents, and when a run ends ask "what are the risks of merging this today?" — his most-used prompt. Design note: Opus 5.5 needs explicit "don't do this" negatives or it falls back to default styles; screenshot-and-annotate beats prose errors. Verdict: dense, practical, and the Max-mode takedown alone is worth it.

### 9to5Linux (RSS)

## 15. OBS Studio 33 Promises Support for Latest NVIDIA Broadcast SDKs, Beta Out Now — by 9to5Linux

![9to5Linux](https://9to5linux.com/wp-content/uploads/2026/09/obs33b.webp)

**Source:** https://9to5linux.com/obs-studio-33-promises-support-for-latest-nvidia-broadcast-sdks-beta-out-now
**Karakeep doc:** `adifulvsmqdxq0qh2sr8xhqz`

OBS Studio 33 is in public beta, and it's a major release for the open-source streaming/recording workhorse. The headline: support for the newest NVIDIA Broadcast SDKs covering both Audio Effects and Video Effects, so RTX owners get the fancy denoise/background tricks. There's also a check for missing encoders when loading a profile, hotkeys for audio monitoring, and NVENC support on AArch64/ARM64 — good news for anyone running OBS on ARM hardware.

The internals got real work too. Plugin loading is completely overhauled, spinboxes behave better, source snapping in the preview gets a new visual indicator, full-screen game detection improves, and macOS Screen Capture transparency handling is cleaned up. PipeWire screencast sources improve, B-frame offset math in AMF gets fixed, and a pile of crashes are squashed.

There's a startup error if obs-transitions fails to load, better file splitting for Hybrid MP4/MOV, and better output when you set a nonsense rescale resolution. The browser-source framework gets updated, Window Capture naming adjusts on Windows, and simple-output audio bitrate now scales by channel count. Notably, Ubuntu 24.04 LTS support is dropped — if you're still on Noble, this one ain't for you.

Standard caveat: it's a beta, don't run it in production. Final release lands next month. Binaries are out for Ubuntu 26.04, macOS, and Windows.

## 16. Shelly 3.1.5 GUI Package Manager for Arch Linux Adds Atoll-Powered AUR Browser — by 9to5Linux

![9to5Linux](https://9to5linux.com/wp-content/uploads/2026/08/sly304.webp)

**Source:** https://9to5linux.com/shelly-3-1-5-gui-package-manager-for-arch-linux-adds-atoll-powered-aur-browser
**Karakeep doc:** `uddkdfbl6ezif3apvvodnklc`

Shelly 3.1.5 is out, two weeks after 3.1.4, and the big add is an optional Atoll-powered AUR browser. You can now page through a sorted AUR package list, sort by votes or popularity, and inspect dependency info plus what's installed or out of date. That's a meaningful step for anyone who'd rather not fight `paru` in a terminal.

The `shelly build` command gains an `--install` flag to install the archives it produces, plus a predictable system PATH for native builds, custom toolchain dirs, and native tools for maintaining your own repos. The native builder got another round of fixes: dependency-only metapackages, restrictive directory permissions, global build deps, source extraction, isolated builds, and empty/zero epochs.

Elsewhere: install optional dependencies straight from package details, better detail loading, opening local `.flatpakref`/`.flatpak` files, and improved AppImage desktop-entry and icon detection. Stale AppImage entries get removed even when files vanish, malformed JSON settings recover across CLI/desktop/tray, search commands default back to repo packages, and AUR installs improve.

The fun one: Nerd Font progress-bar rendering for compatible terminal fonts. If you're not up to speed, Shelly is a modern pacman alternative supporting AUR, Flathub, Flatpak, AppImage, and native Arch packages with both GUI and CLI. Install on CachyOS via `sudo pacman -S shelly`.

### Open-source Projects (RSS)

## 17. Your Claude Code agent, now reachable from Slack and Telegram — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/avibe-bot/avibe)

**Source:** https://www.opensourceprojects.dev/post/cd6f10ea-679b-48f5-b57f-719a02e02544
**Karakeep doc:** `qgvz77c50wx6g0fiyp9m1zyb`

Avibe is a local-first "Agent OS" that lets you steer Claude Code, Codex, or OpenCode from a browser or your chat apps instead of being glued to a terminal. One install command turns your own machine into the home base, and it drives the official tools rather than forking them. Your code and keys stay on your box — avibe.bot never sees your data, and that's structural, not a marketing line. The distributed setup means you start a task at your desk, walk away, and keep steering the same agent from your phone with no state transfer. The Workbench is more than a chat box: it has file inspection, code editing, and terminal execution in one panel, closer to an IDE than a messenger. It talks to Slack, Discord, Telegram, WeChat, and Lark/Feishu, which is genuinely useful if you want to kick off a refactor while waiting for coffee. It's Python 3.9+, MIT licensed, and the short install URL is just a 307 redirect to a readable script, so you can audit before you pipe to bash. The maintainer dogfooded it to build itself, steering agents from browser and phone, which tends to surface rough edges early. The honest tradeoff is real: you're running a service on your machine and exposing it remotely. If you already lean on one of the supported agents, this is a decent front door — just don't expect it to be the house.

## 18. AI coding agent in Rust, no Electron, 36 built-in tools — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/dicklesworthstone/pi_agent_rust)

**Source:** https://www.opensourceprojects.dev/post/03c5f7ae-417d-4fb3-8fe8-69bb7e7a739b
**Karakeep doc:** `rsgpwefevm17wucj2xirszb7`

pi_agent_rust is a from-scratch Rust port of Pi Agent that exists to kill Electron bloat and slow startup for terminal users. It's rebuilt on two purpose-built libraries — asupersync for structured concurrency and rich_rust for terminal formatting — and installs a single `pi` binary with no runtime to babysit. The tool count is genuinely large at 36, but they're layered sensibly: 19 in the default list, 14 always in the model's schema, and the rest behind an `xdev` dispatcher so the context doesn't balloon. It does streaming responses, session persistence, and a single-shot mode for when you don't want a session at all. The repo carries an "unsafe forbidden" badge and targets Rust 2024, which matters for a tool that touches your files from a shell. The one caveat worth flagging: it's no longer chasing drop-in compatibility with the TypeScript Pi. The README is blunt that parity became impractical, and OMP is now the closer reference for feature surface while this port keeps its own architecture. Builds run through Doodlestein Self-Releaser, and contributors are told not to touch Cargo directly, which is an odd but traceable stance. If you want a fast native binary and a clearly stated direction over backwards compatibility, it's worth a look.

## 19. Custom macOS menu bar programs in three easy steps, no third step — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/swiftbar/swiftbar)

**Source:** https://www.opensourceprojects.dev/post/a8049b1c-fc4f-4448-8e9a-6e8809610421
**Karakeep doc:** `imeqlmutnn2xnrrbc3un23tm`

SwiftBar turns any executable script into a macOS menu bar app by dropping it in a Plugin Folder, and the pitch is genuinely accurate — there is no third step. The script's stdout becomes what you see, split into a Header for the menu bar and a Body for the dropdown, with errors going to stderr. The naming convention is the clever bit: `date.1m.sh` refreshes every minute, and duration modifiers cover milliseconds through days, so your refresh schedule lives in the filename instead of a config file. It runs on Monterey and later, and it adopts the BitBar and xbar plugin API, meaning the entire existing ecosystem of plugins drops straight in without modification. You don't need Swift or Xcode — if you can print to stdout, you can build a menu bar app, which is a stupidly low barrier. Nested folders and symlinks are traversed, hidden folders ignored, and there's a `.swiftbarignore` file for exclusions. You can Cmd-drag plugins to reorder them, though renaming the file resets the position. There's a bundled plugin repository plus the BitBar collection, so odds are someone already built what you need. Install via `brew install swiftbar`, pick a folder, and you're about ten minutes from permanent visibility for whatever data you keep forgetting to check.

## 20. A curated list of macOS apps, with sponsors up top — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/jaywcjlove/awesome-swift-macos-apps)

**Source:** https://www.opensourceprojects.dev/post/12a78679-36ed-43b9-9b0b-21f9e9d890a9
**Karakeep doc:** `rqyi84g4dbdlq2ombijze4h2`

This is a curated list of macOS apps maintained by jaywcjlove, hosted as a plain GitHub README — no build step, no database, the curation is the product. The structure is refreshingly honest: sponsors sit up top with clear labels and a thank-you note, so you know exactly what you're looking at before you scroll. Below that, the maintainer lists his own apps — DockLift, Zipora, Scap, Screen Test, Deskmark, Keyzer, and a pile of video tools — each with an icon and a direct Mac App Store link. That matters because he actually ships Mac software, so the list is curated by someone who lives in the ecosystem rather than a random list-keeper. It doubles as a portfolio, a practical cross-section of window management, archives, screenshots, and keyboard customization. The format is frictionless: no sign-up, no newsletter, no "click to reveal," just a README you can star and revisit. Sponsors get real estate but don't crowd out the substance — the balance feels deliberate rather than spammy. It's not a tool you'll use daily, and it isn't trying to be. If you're tired of bloated app roundups stuffed with affiliate links, this is worth a bookmark.

## 21. Pacstall: an AUR-style package manager for Ubuntu, built in bash — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/pacstall/pacstall)

**Source:** https://www.opensourceprojects.dev/post/b03643da-7f66-4348-af5c-4a3dc93bd323
**Karakeep doc:** `e2uo9e64egoljn7rzbt4n3j0`

Pacstall brings Arch's AUR concept to Ubuntu, calling itself "the AUR Ubuntu wishes it had," and it's written entirely in bash. It installs software from multiple repositories using binaries, git repos, appimages, release artifacts, and existing `.deb` packages, filling the gap where apt doesn't have what you need. The most interesting trick is how it handles `-git` packages: upgrading one always pulls the latest build straight from the developer's latest commit, no waiting on a recipe maintainer. That's a real difference from normal distro packaging and suits people who want to live on the edge. It's not just for installing — it can also produce prebuilt `.deb` packages for distribution, so it doubles as a packaging tool. Being bash keeps it accessible; it runs wherever bash runs, which on Ubuntu is everywhere. Install is a curl-to-bash one-liner, or via `sudo apt install pacstall`, or a `.deb` from GitHub releases. Commands feel apt-like: `pacstall -I foo` installs, `pacstall -R foo` removes, `pacstall -L` lists. One gotcha: if you installed via APT, remove your Pacstall packages before uninstalling the tool itself, and `pacstall -U` tells you which path you took. It's not trying to replace apt — just reach the stuff the official repos don't carry.

## 22. SGLang: day-0 support for new open models and 25x inference on GB300 — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/sgl-project/sglang)

**Source:** https://www.opensourceprojects.dev/post/dd44474d-b607-41b3-a118-5e91feed566f
**Karakeep doc:** `tmb6ri8j9rdcxpgpvm2v8poy`

SGLang is an inference engine for LLMs and other generative workloads, and its whole pitch is speed-to-new-model. The "day-0 support" claim isn't marketing fluff — the README's news section is a timeline of same-day launches: Kimi K3, DeepSeek-V4, Mistral Large 3, MiniMax M2, on and on. The point is you can actually evaluate a model while it's still relevant, not a month later after the hype died.

The hardware story is broader than the usual CUDA-only engines. There's SGLang-Jax for TPUs, plus recent work with Google and RadixArk to get full features onto TPUs. So you're not vendor-locked, which is nice if you care about that sort of thing.

The numbers are concrete and tied to named gear. A benchmark shows 25x inference on NVIDIA GB300 NVL72, and a separate DeepSeek-on-GB200 writeup claims 3.8x prefill and 4.8x decode throughput. Those are figures you can actually reason about instead of vibes.

It's not text-only either. There's an SGLang Diffusion component for image and video, and TTS support for models like Higgs Audio v3. Speculative decoding gets real investment too — DFlash and a "Spec V2" thing they're teasing.

Install is a one-liner: `pip install sglang`. Docs, roadmap, Slack, weekly dev meetings — the project moves fast and actually documents it. Verdict: if you're serving in production or doing serious eval across multiple hardware targets, it's worth a look. If you're running one model on one box for fun, it's probably overkill.

## 23. A curated list of newsletters for frontend, backend, mobile, and everything in between — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/zudochkin/awesome-newsletters)

**Source:** https://www.opensourceprojects.dev/post/9dbff96e-f01c-4db7-9350-4389d820c05c
**Karakeep doc:** `qvel5c1k41rq16ofdsjmkpog`

`awesome-newsletters` is exactly what it sounds like — a GitHub awesome-list of newsletters, no install, no runtime, just a README you browse. It's community-driven and follows the standard awesome-* format: one directory organized by topic and subtopic.

The taxonomy is where it earns its keep. Frontend alone has subsections for React, EmberJS, VueJS, and Svelte, plus CSS, design, SVG, and GraphQL. The Programming section covers twenty-plus languages — Python, Java, Rust, Go, plus archival curiosities like ObjectiveC and Groovy. Then it sprawls into open source, Git, editors, databases, Kubernetes, mobile, AI/ML, blockchain.

The non-technical sections are the pleasant surprise. Leadership, career growth, marketing, finance, security, even a "Resilience" section. Most dev lists stop at code; this one acknowledges you have a career after you stop shipping.

Each entry is a link with a one-line description — Friday Front-end sends 15 curated articles every Friday, Dev Tips sends a weekly GIF, FreeCodeCamp sends five picks. No paywalls in the list itself, just pointers.

The stated goal is deliberately modest: a categorized collection of well-known resources, not an exhaustive authority. Contributions are welcome. Verdict: it won't change your life, but it solves the "which newsletter is actually good" problem without wading through SEO listicles. Fifteen minutes, pick one or two, done. 🙄 The real win is replacing three mediocre subscriptions with one decent one.

## 24. A curated list of LLM systems papers, tracked by research trend — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/amberljc/llmsys-paperlist)

**Source:** https://www.opensourceprojects.dev/post/d0546a30-f55e-4a10-b834-7cc21ac78b56
**Karakeep doc:** `qlvugi9ee1vch8qvv7zuvzk7`

`llmsys-paperlist` is a curated reading list of LLM systems papers, articles, slides, and projects. It's not a tool you run — it's a resource you return to, aimed at grad students and engineers drowning in a dozen new arXiv drops a week.

The taxonomy is practical, not academic. Training splits pre-training from post-training/RLHF and fault tolerance. Serving covers agent systems, edge serving, and system-model co-design. There's multi-modal, LLM-for-systems, industrial technical reports, frameworks, benchmarks, and surveys.

The real draw is the trend section. The maintainers treat the list itself as data and frame 2024–2026 around a single question: what unit of work is the system optimizing? The answer shifts from a request in 2024, to a session/reasoning trace in 2025, to a whole agent trajectory in 2026.

The numbers are concrete. Serving is still the biggest area but its share dropped from 49% to 33% between 2024 and 2026. Kernel/model co-design went from 3 to 29 papers, agentic systems from 4 to 22, edge from 2 to 14. Fastest-rising techniques: agentic/multi-agent (1.0% to 13.1%), compiler/kernel/megakernel (0.0% to 10.2%), speculative decoding (1.0% to 5.7%).

Reproduction scripts live in `trends/` if you want to check the math. Honest caveat: curated lists live or die by maintenance, and this one's value depends on the maintainers updating through 2026. Still, the "track units of work, not just topics" lens is worth stealing even if you never open the repo again.

## 25. vcpkg: a C/C++ package manager for CMake, MSBuild, and everything in between — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/microsoft/vcpkg)

**Source:** https://www.opensourceprojects.dev/post/2a97c0e9-f2c9-4aa3-8820-8c2648f15aeb
**Karakeep doc:** `nr6yt5xrpw3shml1o3v1qxgq`

vcpkg is Microsoft's open-source C/C++ package manager, and the headline is that it actually understands C++ — unlike most package managers designed for other languages and retrofitted onto C++. It started in 2016 as a migration helper for Visual Studio and grew into a cross-platform tool for Windows, macOS, and Linux.

The feature list hits real pain points. Manifest mode declares dependencies in your project (`vcpkg new --application` then `vcpkg add port fmt`) so they're versioned and reproducible. Explicit version control kills the "works on my machine" bug. Binary caching reuses compiled artifacts so you stop rebuilding the same deps every time you switch branches. Asset caching handles offline and air-gapped CI.

ABI compatibility and transitive dependencies — the stuff that makes C++ dependency hell actual hell — are first-class concerns here. Build-system agnostic, so CMake, MSBuild, or a custom setup all work. You can publish your own packages through registries.

Install path is gentle: pick your quick-start guide by build system, then either manifest mode or the classic `vcpkg install fmt`. Tab completion is a nice touch.

Verdict: it's not trying to be everything to everyone. It's for C++ devs tired of manual, error-prone dependency management. Reproducible builds, version control, binary caching — the payoff is real on any project with more than a couple deps. Actively maintained by Microsoft plus the community. Worth checking before your next 2 AM linker-error session. 😤

## 26. Rome: an agentic OS where agents build their own harnesses — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/rome-os/rome)

**Source:** https://www.opensourceprojects.dev/post/cd726025-b9a8-4dd0-b655-673645cd7b5a
**Karakeep doc:** `i5qtvgq688y2jxae76k0d0dh`

Rome bets on a genuinely different thesis: most AI-agent progress comes from scaling the model, but Rome scales the *environment* — tools, workflows, memory, interfaces — and lets agents keep their own tooling over time. The core idea is recursive: agents build their own harnesses, design their own SOPs, and orchestrate workflows under your guidance, with proven capabilities persisting across sessions.

It positions itself as an open-source alternative to Grok Bot and Meta's Muse for persistent agents, scheduled tasks, and custom apps. The stack is Node.js 24+, Corepack with pnpm 11.6, and Docker Compose. There's a "Rome Apps" concept pitched as a better home for repeated work than chat — an inbox that remembers what was asked before.

The security defaults on the Docker path are refreshingly careful. The dashboard binds to loopback only (`localhost:7663`), first-run onboarding is open to whoever reaches it first, exposing it requires an explicit `--bind`, state lives in named volumes so re-running upgrades without nuking data, and telemetry export stays off unless you set an env var.

Three ways in: Rome Cloud (preview, `romeos.cc/login`), a one-line Docker quickstart script, or `pnpm dev:all` from source. The README itself flags that self-hosting isn't final yet.

Verdict: it's early, but it's building real infrastructure around an arguable claim rather than just talking. The recursive-agent framing gets more interesting the longer you sit with it. If you're sick of stateless assistants and want to experiment with persistent, self-improving agent workflows, the Docker path is low-risk enough to just try. 👀

### LinuxLinks (RSS)

## 27. Tanko - CLI Manga Reader and Downloader — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/07/manga_young_woman_and_man_futuristic_color8.jpeg)

**Source:** https://www.linuxlinks.com/tanko-cli-manga-reader-downloader/
**Karakeep doc:** `s4f20marmrzcmvqyfsd979fy`

Tanko is a command-line manga reader and downloader that actually renders artwork in the terminal — not some half-assed text dump. It supports MangaDex and LeerCapitulo out of the box, with a provider architecture so more sources can be bolted on later. MangaDex is hit directly without needing a browser, while sources that need browser automation go through Playwright. That's a sensible split.

The clever bit is the display stack. Tanko renders images via the Kitty Graphics Protocol, Sixel, and iTerm2 protocols, so you get real pictures inside a proper terminal. When none of those are available it falls back to ASCII art, which is both charming and slightly cursed. Chapters download as PDF, ZIP, or CBZ, or as loose image files if you prefer raw panels.

It keeps reading history and progress locally, so you don't lose your place mid-series. There's preliminary AniList integration for tracking, and the interface ships in English, Spanish, and French. It's free and open source under the ISC license, by Alexandro Mendez.

Wojtek, if you still read manga at all this beats a browser by a mile — no ads, no bullshit, just panels in your terminal. The ASCII fallback is a genuinely funny emergency option.

## 28. 15 Best Free and Open Source Network Inventory Management — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/10/inventory-management.png)

**Source:** https://www.linuxlinks.com/networkinventorymanagement/
**Karakeep doc:** `bktvaxrsz1im24089q7smtq5`

Network inventory management software exists to kill the spreadsheet. The whole pitch is: stop tracking switches, servers, and cabling in a horrid Excel file or Word doc and let software collect and update the infrastructure data for you. When an admin can see what's on the network, how it's configured, and when it changed, day-to-day troubleshooting gets faster and service provisioning stops being a guessing game.

The value is concrete — up-to-date inventory means you can optimize devices to actually earn their keep and meet needs cost-effectively, with reporting functions and process modeling to automate the back-office grunt work. This is a curated list of 15 network inventory solutions for Linux, with a ratings chart on the article to back up the picks.

One thing worth flagging: the author originally had InvenTree in this list, and a commenter correctly called it out as a manufacturing execution / inventory system, not network inventory management. The author agreed and pulled it. So the list has been sanity-checked, not just auto-generated. Decent sign the curation is actually curated.

Wojtek, if your homelab's "inventory" is still whatever's in your head plus a half-dead spreadsheet, this is your nudge. NetBox alone is worth a look if you have any racked gear worth documenting.

**Projects:**

- **[NetBox](https://github.com/netbox-community/netbox)** — Manage and document computer networks
- **[Snipe-IT](https://snipeitapp.com/product)** — Asset management system
- **[Ralph](https://github.com/allegro/ralph)** — Simple yet full featured Asset Management, DCIM and CMDB
- **[Foreman](https://theforeman.org/)** — Life cycle systems management tool
- **[GLPI](https://www.glpi-project.org/en/)** — Asset and IT management software
- **[Racktables](https://www.racktables.org/)** — Robust solution for datacenter and server room asset management
- **[Nornir](https://github.com/nornir-automation/nornir)** — Pluggable multi-threaded framework
- **[openDCIM](https://www.opendcim.org/)** — Data Center Inventory Management application
- **[Open-AudIT](https://www.open-audit.org/)** — Network auditing application
- **[OCSING](https://ocsinventory-ng.org/?lang=en)** — Hardware and software inventory tool
- **[opsi](https://opsi.org/en/)** — Client management system to manage heterogeneous environments
- **[Netdisco](https://github.com/netdisco/netdisco)** — Web-based network management tool
- **[Netshot](https://github.com/netshot-net/Netshot)** — Automates configuration compliance, backups and change tracking
- **[TeemIp](https://github.com/TeemIp)** — Manage network addressing data and related infrastructure records
- **[FusionInventory](https://fusioninventory.org/)** — IT asset and inventory management

## 29. Giant Log Viewer - view extremely large log files — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/Logfile-viewer2.png)

**Source:** https://www.linuxlinks.com/giant-log-viewer-view-extremely-large-log-files/
**Karakeep doc:** `a562wl40ak9m99elmnngd5kc`

Giant Log Viewer is a graphical app for opening log files so big a normal editor chokes. The trick is architectural: it deliberately caps the JVM heap at a small size and reads file content on demand, so it never loads the whole thing into memory. That means a multi-gigabyte log opens fast instead of hanging while your editor chews through it.

It's written in Kotlin, by Sunny Chung, and ships under Apache 2.0 with a native DEB package for Linux. Navigation is familiar — keyboard or pointer — with key bindings inspired by the `less` pager, plus drag-and-drop to open files. It reads UTF-8, UTF-16, and ASCII, including UTF-8 with a byte-order mark, handles very long individual lines, and correctly renders emoji sequences (which is the kind of edge case that makes or breaks a log viewer).

The whole point is a low memory footprint independent of total file size. If you've ever tried to `vim` a 10 GB access log and watched your machine swap itself to death, this is the fix. Not much else to say — it does one thing and does it without eating your RAM.

Wojtek, next time you're staring at some giant app log in the homelab, this is faster than praying that `less` doesn't OOM. The `less`-style bindings mean zero relearning.

## 30. Helvum - graphical patchbay for PipeWire — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2022/02/Sound-Systems.jpg)

**Source:** https://www.linuxlinks.com/helvum-graphical-patchbay-pipewire/
**Karakeep doc:** `vjr1jbnjmv5tf4tex1r5xcx5`

Helvum is a graphical patchbay for PipeWire — think Catia for JACK, but for the modern PipeWire graph. It shows applications and hardware devices as nodes, with the ports connecting them, and lets you create or remove links by hand. That's the whole pitch: when PipeWire's automatic routing isn't good enough, you stop fighting command-line utilities and just drag a connection in a GUI.

Use cases are concrete — redirecting an app's output, connecting software to virtual devices, building complicated audio paths, or handling apps that expose a pile of PipeWire ports. It deliberately stays a patchbay rather than trying to become a full audio control panel, which keeps it uncluttered. Because PipeWire represents more than desktop audio, the graph can include video and MIDI objects too, so it's not just an audio tool.

It's written in Rust, uses GTK 4 and libadwaita, and updates the graph live as PipeWire objects appear and disappear. Notably it's built specifically around PipeWire, not the PulseAudio compatibility layer, so you get the real graph. Licensed GPL v3, by Tom A. Wagner and Naveen Prashanth, hosted on freedesktop.org's GitLab.

Wojtek, if your audio routing on the desktop ever needs a manual nudge — or you just want to see what PipeWire is actually doing — this is the clean GUI for it. Beats `pw-cli` incantations any day.

## 31. podman-tui - terminal user interface for Podman environments — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2021/11/Docker-Containers2.jpg)

**Source:** https://www.linuxlinks.com/podman-tui-terminal-user-interface-podman-environments/
**Karakeep doc:** `k8674v6zvzqvfdd64x0kie06`

podman-tui is a terminal UI for managing Podman — containers, pods, images, volumes, networks, and secrets, all from a keyboard-driven character-cell interface. It uses Podman's Go bindings, so it talks to either a local install or a remote Podman machine over SSH. That second part matters: you can keep an eye on Podman workloads on another box without opening a browser-based management UI.

Navigation is heavily keyboard-oriented, with vi-style h/j/k/l movement alongside arrow keys and function-key shortcuts. The interface is split into dedicated screens per resource type — system info, pods, containers, volumes, images, networks, secrets — and you flip between them with function keys. You can sort, delete, and run operations on selected resources without leaving the TUI. It needs the Podman system service socket available for the account you're using.

Written in Go by Navid Yaghoobi, Apache 2.0, hosted under the containers org on GitHub. The 2.x release series supports Podman 6.x, and it runs 256-colour mode on Unix-like systems, plus Windows with standard ANSI colours.

Wojtek, if you're on Podman instead of Docker and miss the old `lazydocker`/Portainer convenience, this is the TUI that fills that gap. SSH to remote Podman is the killer feature for a homelab with more than one box.

## 32. fblog - view and filter JSON logs — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/Logfile-viewer1.png)

**Source:** https://www.linuxlinks.com/fblog-view-filter-json-logs/
**Karakeep doc:** `qbxs3tqcjfs6mnq2p2vojj4d`

fblog is a command-line tool for viewing JSON logs that turns structured records into readable output while keeping the individual fields accessible. It auto-detects common fields like message, severity, and timestamp, and you can pick specific fields to display or customize formatting with Handlebars templates. Handlebars helpers give you text styling, colors, case conversion, and size formatting.

The real power is filtering. Filters are written as Lua expressions that operate on fields from each JSON record — nested JSON objects become Lua records, arrays become Lua tables — so you're filtering structured data, not grepping an opaque line of text. That's a genuinely different approach from `jq` or `grep`, and it means conditions can reach into nested structure naturally.

It handles the prefixed output that Kubernetes tools produce when combining logs from multiple pods, supports message placeholder substitution, configurable mappings for log levels, and shell completion generation. Default severity levels are trace, debug, info, warn, error, and fatal, each colorized. It reads continuous log streams via stdin and respects `NO_COLOR`. Written in Rust by Patrick Haun, licensed WTFPL — which tells you the author's sense of humor.

Wojtek, if you're swimming in structured logs (looking at you, anything Kubernetes or JSON-logging), Lua-filterable log viewing beats a `jq` pipeline you have to re-type every time. The WTFPL license is just a bonus.

## 33. PH4NTXM – Debian-Based Cybersecurity and Privacy Distribution — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/04/Linux-Distributions.png)

**Source:** https://www.linuxlinks.com/ph4ntxm-debian-cybersecurity-privacy-distribution/
**Karakeep doc:** `ymagq4thxzulcad7a97qt6sc`

PH4NTXM is a Debian-based live distro built for opsec nerds, not for people who just want a browser that blocks ads. It boots from a USB stick, loads into RAM, and lets you yank the drive out once it's up. Every boot is a fresh disposable session — no identity reused from last time, which is the whole goddamn point.

The standout feature is the Adaptive Identity Engine. It generates a per-session identity covering hostname, MAC addresses, reported hardware, browser config, and network behavior, then keeps all of it consistent so you don't leak your real fingerprint through some stupid mismatch.

Three boot modes: Linux (Linux-aligned identity + Firefox ESR), Windows (pretends to be Windows while still running Debian underneath), and Lone Wolf (Linux identity, routes supported traffic through Tor with its own firewall rules).

The security stack is genuinely stacked. Packet Transformation Engine mangles network traffic using Rust, C, NFQUEUE, and eBPF. Document Airlock opens and converts files inside a disposable offline KVM sandbox so a malicious PDF can't nuke your host. There's Encrypted DNS via Unbound, a Lockdown mode that kills traffic until you re-enable it, a panic button, USB nuke, and a whole OpSec Suite with Network, Kernel, Process, Radio, ConnWatch, and Shredder tools.

XFCE desktop, systemd, APT, fixed release, x86_64 only. GPLv3, meant to be built from source and independently reviewed. This thing is serious — it's the kind of project that gets a raised eyebrow if you're the type to say "opsec" unironically, but the feature list is legitimately more thoughtful than most "privacy distros" that are just Firefox with a VPN icon. 😶

## 34. Building the PH4NTXM ISO on CachyOS — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/Tutorial-banner.png)

**Source:** https://www.linuxlinks.com/building-ph4ntxm-iso-cachyos/
**Karakeep doc:** `r5wq29aswkhdou6iqdvtmrls`

PH4NTXM's build docs assume Debian 13 "trixie" on amd64. LinuxLinks runs CachyOS for most of their work, so they wanted to know if they could skip spinning up a separate Debian box. Answer: yes, with a couple of PATH headaches.

The core friction is where CachyOS keeps its tools. First snag: `make install` for live-build died at `po4a - command not found` — because CachyOS sticks po4a in `/usr/bin/vendor_perl`, not `/usr/bin`. Fix is `sudo env PATH="/usr/bin/vendor_perl:..." make install`. They also had to grab a specific live-build version, `20250505+deb13u1`, straight from Debian's pool and unpack it under `/tmp`.

Second snag hit at the EFI image stage: `/usr/lib/live/build/efi-image: 86: mkfs.msdos: not found`. dosfstools was installed, but the Debian script expects `/usr/sbin` in PATH. Re-running with `PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"` fixed it.

Net result: the ISO built fine. Both fixes are PATH-only — no source edits to PH4NTXM itself. You can build the Abyss edition with `./build.sh --edition abyss`, or Ghost (same guts, lighter theme) with `--edition ghost`. Output lands in timestamped directories under `~/PH4NTXM/output/` with the ISO and a SHA256SUMS file together.

The whole article is honestly just "we fought PATH for twenty minutes and won," but if you're the type to build your own privacy distro on an Arch derivative, this saves you the exact same two head-scratchers. 😤

## 35. SuperHTML – HTML validator, formatter and language server — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/01/018-coding.png)

**Source:** https://www.linuxlinks.com/superhtml-html-validator-formatter-language-server/
**Karakeep doc:** `fe55sdkr2tdopre6r1vbszlt`

SuperHTML is one binary that does three jobs: validates HTML, formats it, and runs a Language Server Protocol server. Written in Zig, by Loris Cro (the guy behind Zig's zls), MIT license.

The validator actually understands the WHATWG living spec, not just "is this XML-ish." So it catches element-nesting mistakes and bad attribute values, not just unclosed tags. It makes deliberately stricter calls than browsers do, on the theory that permissive parsing hides real authoring bugs.

The formatter is whitespace-sensitive, so you get control over vertical and horizontal element layout — the thing that drives everyone insane with prettier. It can also check formatting in CI without rewriting files.

The LSP part is the selling point: drop it into VS Code, Neovim, Helix, Vim, Zed, or anything LSP-capable. There's a syntax-only mode for files full of template constructs it can't fully validate yet, and it flags unsupported doc types instead of silently guessing. Full validation of third-party template syntax is still limited — that's the honest caveat.

If you've ever wanted a fast, spec-aware HTML linter that also formats and doesn't need Node, this is it. The templating-language library is a nice bonus for people building their own tooling. 👍

## 36. ROSboard – lightweight web dashboard for visualizing ROS topics — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2019/07/two-friends-doing-science-experiments.jpg)

**Source:** https://www.linuxlinks.com/rosboard-lightweight-web-dashboard/
**Karakeep doc:** `zv800fy253kzkz990aq0r2ey`

ROSboard is a web dashboard that runs a ROS node, spins up a web server, and lets you eyeball your robot's topics from any browser on the network — phone, tablet, whatever. By Dheera Venkatraman, BSD 3-Clause, written in JavaScript and Python.

The pitch is "field diagnostics without dragging a workstation out to the robot." Topics show up as responsive cards in a mobile-friendly UI, with visualizers for images, point clouds, GPS, diagnostics, and time-series data. It compresses big image and point-cloud messages before sending them over a WebSocket bridge, so it's not eating your robot's bandwidth.

3D stuff goes through WebGL components; geographical data (like satellite position messages) uses Leaflet. It can also replay recorded ROS bag files. And it's deliberately stingy with resources when idle.

Two things stand out as smart design. One: custom visualizers can be added with a plain JavaScript viewer file, no recompiling anything. Two: it does NOT hand the browser unrestricted access to the whole ROS system — you get a scoped view, not a root shell on your robot.

The whole point is a lightweight alternative to Rviz that doesn't assume you're sitting at a fat desktop. For quick sensor checks or telemetry on a field robot, it's a genuinely good idea. 🤖

## 37. 12 Best Free and Open Source Linux Desktop Genome Browsers — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2019/07/3d-render-illustration-dna-structure-blue-background.jpg)

**Source:** https://www.linuxlinks.com/best-free-linux-desktop-genome-browsers/
**Karakeep doc:** `th16ocrczibphzn1a585aokj`

A genome browser is a graphical window into genomic data — think gene structure, proteins, expression, variation, comparative analysis, all zoomable from megabase scale down to individual DNA bases. The human genome is 3+ billion base pairs, so you need tooling that can load whole-genome FASTA files and not keel over.

LinuxLinks rounds up twelve standalone *desktop* browsers, explicitly excluding web-based ones (those get a separate article). Most of these are Java-based and therefore cross-platform, and most need zero programming knowledge — which is the whole appeal for bench biologists.

There's heavy overlap in what these do, and each one has its own specialty: some are built for high-throughput alignment viewing, some for annotation, some for Sanger traces, and one is literally a text-only terminal browser. If you're picking one, the deciding factor is usually your data type and whether you need collaborative annotation or just a fast viewer.

The chart is the usual LinuxLinks verdict thing, and each entry gets a full portal page with features and a screenshot. This is desktop-only — if you want UCSC or Ensembl in a browser tab, that's the other roundup. Solid list if you actually work with genomics; mostly academic curiosity otherwise. 🧬

**Projects:**

- **[Hugo](https://gohugo.io/)** — Fast framework for building websites
- **[Plenti](https://plenti.co/)** — Go backend and Svelte frontend
- **[Gitmal](https://github.com/antonmedv/gitmal)** — Static page generator for Git repositories
- **[InkPaper](https://imeoer.github.io/blog/ink-blog-tool-en.html)** — Elegant static blog generator
- **[Hastie](https://github.com/mkaz/hastie)** — Takes Markdown text files, applies a template, and generates an HTML site
- **[gostatic](https://github.com/sansolovyov/gostatic)** — Dependency tracking and re-rendering only changed pages
- **[Zas](https://github.com/darccio/zas)** — Billed as the most simple static site generator ever
- **[Gojekyll](https://github.com/osteele/gojekyll)** — Jekyll-compatible static site generator
- **[Gozer](https://github.com/dannyvankooten/gozer)** — Fast and simple static site generator
- **[LitePub](https://github.com/mirovarga/litepub)** — Lightweight static blog generator
- **[Magnanimous](https://github.com/renatoathaydes/magnanimous)** — Simple and fast static website generator
- **[depp](https://git.8pit.net/depp/)** — Static page generator for Git repositories
- **[Underblog](https://github.com/freetonik/underblog)** — Extremely simple, fast static blog generator
- **[Krems](https://github.com/mreider/krems)** — For markdown-based blogs
- **[Sitegen](https://github.com/altlimit/sitegen)** — Simple but flexible static site generator
- **[Notebrew](https://github.com/bokwoon95/notebrew)** — Static site CMS and blogging platform
- **[Anna](https://github.com/anna-ssg/anna)** — Builds websites from Markdown content
- **[verless](https://github.com/verless/verless)** — Simple and lightweight static site generator
- **[kew](https://github.com/uint23/kew)** — Extremely minimal static site generator
- **[Hindsite](https://github.com/srackham/hindsite)** — Fast, lightweight static website generator
- **[gohan](https://github.com/bmf-san/gohan)** — Incremental builds, syntax highlighting, Mermaid diagrams
- **[Ago](https://github.com/DavidSatimeWallin/ago)** — Small static blog generator without any fuzz

## 38. 23 Best Free and Open Source Go Static Site Generators — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2021/10/SSG.png)

**Source:** https://www.linuxlinks.com/best-free-open-source-go-static-site-generators/
**Karakeep doc:** `qg63wqgwq72hruy6cqq0hx2t`

LinuxLinks opens by admitting their own site is dynamic (database → HTML on request), but makes the case for full static generation anyway. Prebuilt pages load stupidly fast, need a smaller software stack (better security), are immune to most common attacks, cost less in server load, are previewable locally, export easily, and version cleanly in Git.

The tradeoff is real but narrow: the only difference from a dynamic site is that all HTML gets generated before upload. For docs especially, static is a no-brainer.

Then they list 23 Go SSGs, all under free licenses. Hugo is the obvious headliner — explicitly recommended as the fast, powerful default. The rest are a long tail of niche options: Jekyll-compatible (Gojekyll), Svelte-frontend (Plenti), Git-repo generators (Gitmal, depp), minimal one-file things (kew, Zas), blog-specific tools (InkPaper, LitePub, Underblog), and a few with unusual hooks like Mermaid diagrams (gohan) or a static CMS feel (Notebrew).

Realistically, if you're reaching for a Go SSG you already know whether you want Hugo or some hyper-minimal toy. This list is the full menu of alternatives for the contrarian who refuses Hugo on principle. Most of the entries are tiny or unmaintained, so caveat emptor. 📄

**Projects:**
- Hugo — fast framework for building websites (the recommended default)
- Plenti — Go backend, Svelte frontend
- Gitmal — static page generator for Git repositories
- InkPaper — elegant static blog generator
- Hastie — Markdown + template → HTML site
- gostatic — dependency tracking, re-renders only changed pages
- Zas — self-billed "most simple SSG ever"
- Goldsmith — extensible static website generator
- Gojekyll — Jekyll-compatible SSG
- Gozer — fast and simple SSG
- LitePub — lightweight static blog generator
- Magnanimous — simple, fast static website generator
- depp — static page generator for Git repositories
- Underblog — extremely simple, fast static blog generator
- Krems — for Markdown-based blogs
- Sitegen — simple but flexible SSG
- Notebrew — static site CMS and blogging platform
- Anna — builds websites from Markdown content
- verless — simple, lightweight SSG
- kew — extremely minimal SSG
- Hindsite — fast, lightweight static website generator
- gohan — incremental builds, syntax highlighting, Mermaid diagrams
- Ago — small static blog generator "without any fuzz"

## 39. Tilia - formatter for Haskell source code — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/Code-Formatter-banner3.png)

**Source:** https://www.linuxlinks.com/tilia-formatter-haskell-source-code/
**Karakeep doc:** `jwyspgi0g9chjfdgb80h799r`

Tilia is an opinionated Haskell formatter that leans on ghc-lib-parser instead of rolling its own parser. That's the boring-but-correct choice, since parsing Haskell by hand is a goddamn minefield. The "opinionated" part is the headline: it deliberately ships with basically no config knobs. That'll either feel refreshing or infuriating depending on how much you love bikeshedding `stylish-haskell` options files.

The clever bit is that it lets the existing source decide single-line vs multiline layout, so it doesn't force one rigid shape onto every expression. It treats Cabal components as the unit of formatting, not bare files, which means it actually respects your default language extensions and dependencies. It discovers projects through `cabal.project` and `.cabal` files and handles libraries, executables, test suites, benchmarks.

Two commands: `tilia inplace` rewrites in place, `tilia check` just tells you if you're already clean. It also offers optional AST-equivalence and idempotence checks, which is the kind of paranoia you want in a formatter. CPP gets first-class treatment — it preserves and formats the Haskell hiding inside conditional branches instead of vomiting on `#ifdef` blocks. A `.tiliaignore` handles exclusions.

Written in Haskell, BSD 3-Clause, by Mark Karpov. If your formatter's whole sales pitch is "I won't reformat your code into mush," that's worth a look.

## 40. FacilMap - privacy-friendly collaborative OpenStreetMap web map — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/05/029-city-map.png)

**Source:** https://www.linuxlinks.com/facilmap-privacy-friendly-collaborative-openstreetmap-web-map/
**Karakeep doc:** `na7myoscllq3cxktrxjmwrxh`

FacilMap is a privacy-friendly web map built on OpenStreetMap and friends, trying to cover more ground than a dumb map viewer while still working in a normal browser. It runs as a progressive web app on desktop and mobile, so no native client to install — handy for trip planning and field use. It's a long-running hobby project that marries a public map with tooling for people who want to organize their own geographic data.

The feature list is genuinely long. Map styles for roads, topography, cycling, hiking, public transport, and water navigation. Place search that surfaces details like websites and opening hours. Route planning with draggable waypoints and an elevation profile, plus road-surface info where the data exists. The standout is live collaborative maps — markers, lines, and routes that update in real time for everyone sharing the link.

Imports GPX, KML, OpenStreetMap, and GeoJSON; exports GPX and GeoJSON. You can make read-only or editable share links and embeds, define custom marker and line types with your own form fields, and build filtered custom views with configurable legends. Stored field values export as HTML or CSV. There's a Socket.IO API for devs who want to bolt mapping into their own apps.

TypeScript, AGPL v3. If you're tired of Google Maps tracking your every pan and want something you can self-host without guilt, FacilMap is a serious contender.

## 41. Logalize - extensible log colorizer — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/Logfile-viewer4.png)

**Source:** https://www.linuxlinks.com/logalize-extensible-log-colorizer/
**Karakeep doc:** `l4gpbni8yki6pjtk2njkp5lm`

Logalize is a CLI log colorizer that reads lines from stdin and slaps color and styling onto them, making walls of plain-text logs actually scannable. The trick is it's not hard-coded like a lot of `grep --color` hacks — everything is configured through YAML. You define complete log formats, regex patterns that highlight portions of a line, and groups of words that each get their own style.

Config files live system-wide, in your user config dir, in the current directory, or you pass one explicitly. Multiple configs merge, so you can keep general rules alongside project-specific ones. Built-in formats, patterns, word groups, and themes can be supplemented, overridden, or disabled outright. Themes control fg/bg colors plus bold, italic, underline, reverse, and more. Recent releases added Solarized light and dark.

The neat bit is the word handling understands English inflections — a rule for "complete" also catches "completed" and "completing." Good and bad word groups can even account for negation, so "not failed" doesn't light up red. Input normally comes from a pipe, so it drops in cleanly next to anything that emits logs or `cat`.

Written in Go, MIT license, by Rufus Deponian. Packages available for several distros plus standalone binaries. A small, boring tool that does one job well — the best kind.

## 42. 29 Best Free and Open Source Graphical YouTube Tools Bypassing the Web-Only Barrier — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/03/women-holding-youtube-icon.jpg)

**Source:** https://www.linuxlinks.com/excellent-youtube-tools-bypassing-web-barrier/
**Karakeep doc:** `rcnp4xintmd21yn7w9yp2k7e`

YouTube's been around since 2005 and Google-owned since 2006, but the recurring gripe is that you're stuck in a web browser to watch anything. This roundup collects 29 free and open-source graphical tools that bypass the web-only barrier for a more TV-like experience. It's the usual LinuxLinks roundup formula: a ratings chart plus a table of every tool with a one-line description.

The list spans a few distinct jobs. Downloaders dominate — Media Downloader, Open Video Downloader, Tartube, ClipGrab, ytdl-gui, NeoDLP, GDownloader, Pulsar, and Video Downloader are all yt-dlp or youtube-dl frontends in various wrappers. Privacy-focused players like FreeTube, Piped, pipe-viewer, and youtube-local stand out as the "fuck the algorithm" crowd. Then there are music clients — AudioTube, Mixtapes, Sunder, SpMp, NouTube, MellowPlayer — for turning YouTube into a music app.

A few niche picks: PlasmaTube integrates with KDE, VacuumTube wraps YouTube Leanback, Materialious is a frontend for Invidious, Youwee and Sunder are Tauri/Rust builds, PsTube is Flutter, Minitube is the ancient "no Flash" client. The comments section is the usual love letter to FreeTube, and one guy plugs Harmony Music, which the author notes is effectively unmaintained since v1.12.0.

Verdict: it's a directory, not a review, so the "best" label is doing a lot of work. But if you want a browser-free YouTube life, the table is a solid starting map. FreeTube and Piped are the ones worth your time first.

**Projects:**

- **[FreeTube](https://github.com/FreeTubeApp/FreeTube)** — Privacy-focused YouTube client (desktop)
- **[Media Downloader](https://github.com/mhogomchungu/media-downloader)** — yt-dlp GUI frontend for downloading media
- **[OmniGet](https://github.com/tonhowtf/omniget)** — Download media and files from a broad range of online sources
- **[Piped](https://github.com/TeamPiped/Piped)** — Uses NewPipe Extractor, a library for extracting
- **[Open Video Downloader](https://github.com/jely2002/youtube-dl-gui)** — Easy-to-use graphical frontend for downloading online videos
- **[Tartube](https://github.com/axcore/tartube)** — GUI frontend for youtube-dl/yt-dlp with a video database
- **[AudioTube](https://invent.kde.org/multimedia/audiotube)** — Qt-based music streamer
- **[Videomass](https://github.com/jeanslack/Videomass)** — GUI for FFmpeg and yt-dlp
- **[ClipGrab](https://clipgrab.org/)** — Downloader for YouTube and other sites
- **[Minitube](https://flavio.tordini.org/minitube)** — Application for watching YouTube without using Flash
- **[Materialious](https://github.com/Materialious/Materialious)** — Fontend for YouTube and Invidious
- **[youtube-local](https://github.com/user234683/youtube-local)** — Browser-based YouTube client
- **[SMTube](https://www.smtube.org/)** — Search, play and download YouTube videos
- **[Pipeline](https://gitlab.com/schmiddi-on-mobile/pipeline)** — Watch YouTube and PeerTube videos
- **[MellowPlayer](https://github.com/ColinDuquesnoy/MellowPlayer)** — Cloud music integration for desktop
- **[ytdl-gui](https://codeberg.org/impromptux/ytdl-gui)** — Graphical interface for yt-dlp
- **[Youwee](https://github.com/vanloctech/youwee)** — Built with Tauri and React
- **[PlasmaTube](https://apps.kde.org/plasmatube/)** — Designed to be integrated with KDE Plasma
- **[PsTube](https://github.com/prateekmedia/pstube)** — Flutter-based video client
- **[Video Downloader](https://github.com/Unrud/video-downloader)** — Download videos from YouTube and other websites
- **[VacuumTube](https://github.com/shy1132/VacuumTube)** — Unofficial wrapper of YouTube Leanback
- **[NeoDLP](https://github.com/neosubhamoy/neodlp)** — Feature-rich video/audio downloader based on yt-dlp
- **[Mixtapes](https://github.com/m-obeid/Mixtapes)** — Modern, Linux-first YouTube Music player
- **[GDownloader](https://github.com/hstr0100/GDownloader)** — GUI for downloading videos, audio and galleries
- **[Sunder](https://github.com/FrogSnot/Sunder)** — Built with Tauri v2 and Rust
- **[SpMp](https://github.com/sayaka-sh/spmp)** — YouTube music client with a focus on customization
- **[Pulsar](https://github.com/FuzjaJadrowa/Pulsar)** — yt-dlp GUI
- **[NouTube](https://github.com/nonbili/NouTube)** — YouTube and YouTube Music in a single app
