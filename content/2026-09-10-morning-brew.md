---
date: 2026-09-10
slug: 2026-09-10-morning-brew
tags: CLI,Honeypot,Python,Security,network security,security,Go,Internet,file transfer,networking,Multimedia,Roundup,artificial intelligence,free,machine learning,open source,speech algorithms,Android,GUI,Jetpack Compose,Productivity,kotlin,productivity,task managers,Graphics,graphics,photo,photo management,Scientific,plotting,science,scientific plotting,RSS,React,Rust,Web Apps,podcast,self-hosted,web,Arch,Distro,KDE Plasma,desktop,distribution,wayland,C++,Slint,time tracking,Apps,KDE,KDE Gear,News,software suite,Calamares,Calamares installer,graphical installer,Utilities,configuration,shell,zsh,GNOME,GTK+,Pomodoro,Vala,Desktops,KDE Plasma 6.8,desktop environment,IAM,Microsoft,Microsoft Entra ID,Office,SSO,access control,authentication,identity and access management,identity federation,identity management,network authentication,COSMIC,Tauri,TypeScript,encryption,file sharing,peer-to-peer,Distros,Linux distribution,Ubuntu,Ubuntu 24.04 LTS,Debian,LXQt,Xfce,CPU scheduling,CachyOS,E-cores,FFmpeg,Hardware,Intel Core Ultra 7 356H,LP E-cores,Linux scheduler,MINISFORUM M2,Mini PC,OpenSSL,P-cores,Panther Lake,Reviews,hybrid processors,perf,stress-ng,turbostat,TUI,news,tui,JavaScript,GIMP,image editing,image editor
---

# Morning Brew — 2026-09-10

Four things you saved by hand, then the RSS firehose. The hand-picked stuff: a guy restoring a '91 Mercedes to prove the economy's rotting, a $25K/month job board, a multi-agent-systems book repo, and an old MacBook coding its own GPU drivers via a mirror and a webcam. The rest: eight RSS videos, six 9to5Linux news bits, twelve Open-source Projects, and nineteen LinuxLinks roundups.

### Hand-bookmarked

## 1. 🎬 Video — I Bought And Restored “Old” Technology To Prove The Economy Is Imploding — by Quincy Sandbank

![Quincy Sandbank](https://i.ytimg.com/vi/C_0xBbEFjLk/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=C_0xBbEFjLk
**Karakeep doc:** `i71d9s7pqh2o72hgkkixt412`

Quincy bought a 1991 Mercedes 190E — calls it Gunther — to prove the economy is rotting from the inside. His thesis: enshittification isn't just greedy companies, it's structural. The economy needs growth, real innovation stalled, so firms extract value instead of creating it. He spent ~$10K restoring the thing and now daily-drives it. Long, rambling, occasionally brilliant.

## 2. 🎬 Video — I make $25K/month from one simple website — by Starter Story

![Starter Story](https://i.ytimg.com/vi/xEoLsAQFnOY/maxresdefault.jpg)

**Source:** https://youtu.be/xEoLsAQFnOY?si=Cf_XZCe6vScvvDfe
**Karakeep doc:** `j68y89nc30xf8130nkr3718g`

Roman runs Career Hound, a job board that scrapes listings straight off company sites. $25K last month, and the guy can't code. The whole trick is marketing — he calls it "content thrifting," scrolling TikTok/Reddit until he spots timeless formats, then pays older creators ~$20 a pop to read them. Hard paywall, $7/week, 31% churn. Boring product, boring answer, still works.

## 3. GitHub - victordibia/designing-multiagent-systems: Building LLM-Enabled Multi Agent Applications from Scratch — by GitHub

![GitHub](https://repository-images.githubusercontent.com/799574583/62116413-3960-41c8-b94c-09b4fd755557)

**Source:** https://github.com/victordibia/designing-multiagent-systems
**Karakeep doc:** `nkao05maiy6knpt2nsjxswav`

Victor Dibia's companion repo for his book "Designing Multi-Agent Systems." Implements every pattern from the book — tool-calling agents, sequential workflows, round-robin orchestration — plus a minimal framework called picoagents. 853 stars, Apache-2.0, mostly Python. If you want the theory and the code side by side, this is it.

## 4. Old MacBook uses a mirror, webcam, and AI agent to code its own AMD GPU drivers — 'agent-first' Omarchy Linux debugs itself, AI can check its own progress on screen in real-time — by Tom's Hardware

![Tom's Hardware](https://cdn.mos.cms.futurecdn.net/c3WrJMcfqqatjiW9w8iTwD-1920-80.jpg)

**Source:** https://www.tomshardware.com/tech-industry/artificial-intelligence/old-macbook-uses-a-mirror-webcam-and-ai-agent-to-code-its-own-amd-gpu-drivers-agent-first-omarchy-linux-debugs-itself-ai-can-check-its-own-progress-on-screen-in-real-time
**Karakeep doc:** `ge23g6udgy26usvkpm52l9vx`

Some guy named Schroeder pointed a webcam at a mirror so an AI agent could "see" an old MacBook's screen and write AMD GPU drivers for it. The distro is Omarchy, an "agent-first" Linux. Tim Sweeney called it "HAL 9000 lip-reading vibes." Peak vibe-coding absurdity, and honestly kind of neat.

### RSS — YouTube

## 5. 🎬 Video — Columnar Databases Are Incredibly Fast. Here’s Why. — by Better Stack

![Better Stack](https://i.ytimg.com/vi/mR06J55fLvo/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=mR06J55fLvo
**Karakeep doc:** `wq8mulccjero3z2twdc4i31u`

Postgres is great until you need to aggregate a hundred million rows, then it's a nine-second nap. ClickHouse and DuckDB run the same group-by in a quarter second because they store columns together and skip whole blocks instead of reading every row. The catch is single-row lookups and updates — ClickHouse takes 168ms to find one ID and 5.8 seconds to update a row because its files are immutable. DuckDB sits in the middle, more like SQLite, but its single-file design kills concurrency. Pick your poison based on workload, not demo speed.

## 6. 🎬 Video — Python’s Weirdest Security Bug Is Just .lower() #programming #security #python — by Better Stack

![Better Stack](https://i.ytimg.com/vi/nqZDvM53_A4/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/nqZDvM53_A4
**Karakeep doc:** `ybhzjin8mpodry3g98psesbw`

A CVE shipped because one `.lower()` call used your interpreter's Unicode version instead of the frozen Unicode 3.2 that stringprep is defined against. Same domain name, two different ASCII results depending on which Python you run. The fix was just adding every code point where modern lowercase disagrees with 3.2 as an exception. CVE-2026-1784, and a reminder that the nastiest bugs hide in the most boring lines.

## 7. 🎬 Video — Windows Took 90 Minutes. Omarchy Took 1. — by NetworkChuck

![NetworkChuck](https://i.ytimg.com/vi/6HPG3WGd1wQ/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/6HPG3WGd1wQ
**Karakeep doc:** `hgsuhzl8qzdl87w35a87ydyi`

Chuck timed it: a brand-new Windows box took 90 minutes of updates before it was usable, and a fresh MacBook took 42. Both ship from the factory in a state he calls unusable. So he spent weeks with agent help optimizing Omarchy's install down to one damn minute. The pitch is basically "stop assembling Legos every time you set up a machine."

## 8. 🎬 Video — The legendary coffee pot — by Brodie Robertson

![Brodie Robertson](https://i.ytimg.com/vi/do57XPNYtv8/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/do57XPNYtv8
**Karakeep doc:** `s804omtpxf71us4zbdp9bug0`

The Trojan Room coffee pot — the first webcam on the internet — got refurbished, used in Der Spiegel's offices, then donated to the Heinz Nixdorf MuseumsForum in Paderborn. It's been sitting in a museum since 2016 with a live webcam still pointed at it. It spawned the Hypertext Coffee Pot Control Protocol (RFC 2324) and even got parodied in Hitman 2: Silent Assassin. A whole chunk of internet history, now a museum piece with a camera on it.

## 9. 🎬 Video — Everyone Thought Dijkstra Couldn’t Be Beaten #algorithm #programming #computerscience — by Better Stack

![Better Stack](https://i.ytimg.com/vi/iDv0oQKTcgM/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/iDv0oQKTcgM
**Karakeep doc:** `vvgj0rzzon6fbyqe76r8eivn`

Five researchers proved the "sorting barrier" in Dijkstra was never actually necessary, running in O(m log^(2/3) n) instead of O(m + n log n). But the viral posts left out the fine print: it only beats Dijkstra on sparse graphs, and the paper is from April 2025, just re-viraled last week. Google Maps isn't rewriting anything. The real story is that a four-decade "fundamental limit" was just an assumption nobody got underneath.

## 10. 🎬 Video — Open Source Fight Between Anti-AI & Vibe Coders Never Ends — by Brodie Robertson

![Brodie Robertson](https://i.ytimg.com/vi/UudhdvY946c/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=UudhdvY946c
**Karakeep doc:** `fjpspu5aeuyc5b5uk4dmp1yk`

A rambly tour of the FOSS civil war over AI. Codeberg says "we don't like AI but real projects with real users are fine," SourceHut says "no AI, period, as of Sept 10 2026," while GitHub and GitLab lean hard the other way. Projects like NetworkManager and Ghostty are planting prompt-injection canaries in their AGENTS.md files to catch the laziest slop commits. Brodie's honest take: nobody has a time machine, but the greybeards hate it and the new kids can't avoid it, and the split is only going to widen.

## 11. 🎬 Video — A Human Just Beat the World’s Strongest Go AI #ai #google #programming — by Better Stack

![Better Stack](https://i.ytimg.com/vi/iySQNsNGD7g/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/iySQNsNGD7g
**Karakeep doc:** `rvydbgbw60u039ddq4jrubwm`

Shin Jinseo, the world's top Go player, beat KataGo in a three-game series while giving it a two-stone handicap — the first human to win an official series against a state-of-the-art engine at that handicap. His trick was refusing to copy the AI: he stopped imitating its moves, opened on the opposite side to break its mirroring, and played patient defense to a 99% win probability. The way to beat the machine was to stop playing like it.

## 12. 🎬 Video — AI Still Needs Network Engineers — by NetworkChuck

![NetworkChuck](https://i.ytimg.com/vi/BzfsGEr8lFg/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/BzfsGEr8lFg
**Karakeep doc:** `kkn54z3lp33fk615zwhqm3av`

Chuck's doing his usual "get your CCNA now" pitch, and the hook is that AI hasn't killed networking — it's made it more necessary. Every prompt you send to ChatGPT or Claude or whatever you do with Hermes rides over a network a network engineer built and is still running. The exam's changing, so time's running out, blah blah. Standard NetworkChuck urgency, but the underlying point is fair: all this AI runs on someone's infrastructure.

### 9to5Linux (RSS)

## 13. KDE Gear 26.08.1 Is Out with More Improvements for Your Favorite KDE Apps — by 9to5Linux

![9to5Linux](https://9to5linux.com/wp-content/uploads/2026/04/kg264.webp)

**Source:** https://9to5linux.com/kde-gear-26-08-1-is-out-with-more-improvements-for-your-favorite-kde-apps
**Karakeep doc:** `tg5mv2ui8zsq16l2d6doy9o5`

First maintenance drop for KDE Gear 26.08, and it's a grab bag of small fixes. Okular stops crashing when you save, Dolphin finally closes tabs with a middle click, and Kdenlive stops dying on half a dozen crash paths. Itinerary learned to parse Air Canada flights and Lufthansa PDFs, so your travel nerd app got smarter too. Nothing flashy, just the usual "update and move on" release.

## 14. Calamares 3.4.3 Linux Graphical Installer Improves Disk Partitioning, Locale — by 9to5Linux

![9to5Linux](https://9to5linux.com/wp-content/uploads/2026/03/calam.webp)

**Source:** https://9to5linux.com/calamares-3-4-3-linux-graphical-installer-improves-disk-partitioning-locale
**Karakeep doc:** `i53cthqmlmgrgczxcfc24jm8`

The installer half the Arch-based distros ship with got a maintenance bump. It stops accidentally marking /boot as the EFI partition, which was quietly breaking things with systemd-gpt-auto-generator. Locale page now handles those weird Etc/GMT timezones, and Wayland keyboard input got un-fucked. You won't install this yourself — it shows up in the next CachyOS or EndeavourOS ISO.

## 15. KDE Plasma 6.8 Desktop Environment Is Now Available for Public Beta Testing — by 9to5Linux

![9to5Linux](https://9to5linux.com/wp-content/uploads/2025/11/kp.webp)

**Source:** https://9to5linux.com/kde-plasma-6-8-desktop-environment-is-now-available-for-public-beta-testing
**Karakeep doc:** `egjglt8z3mfpy53a0ilviw3q`

Big one: Plasma 6.8 is the release that kills the X11 session entirely. Wayland-only, no X11 login option, XWayland for your legacy apps. NVIDIA triple buffering is on by default, Spectacle can record audio during screen recording, and multi-monitor setups get color-coded badges so you stop confusing your two identical panels. Beta now, second beta September 24th, don't run it on your work machine.

## 16. COSMIC 1.8 Desktop Environment Is Officially Out, Improves Touchscreen Support — by 9to5Linux

![9to5Linux](https://9to5linux.com/wp-content/uploads/2026/07/cos13.webp)

**Source:** https://9to5linux.com/cosmic-1-8-desktop-environment-is-officially-out-improves-touchscreen-support
**Karakeep doc:** `hleu8jz9lyz48ttbb6musx9r`

System76 shipped COSMIC 1.8 two weeks after 1.7, which is a hell of a cadence. Touchscreen support got better, server-side decorations are now configurable, and hybrid GPU laptops get some love. Also fixed the bug where windows vanished when you dragged them onto the same workspace. The Rust desktop keeps grinding forward.

## 17. Ubuntu 24.04.5 LTS Is Now Available for Download with Linux 7.0 and Mesa 26.2 — by 9to5Linux

![9to5Linux](https://9to5linux.com/wp-content/uploads/2026/09/u2445.webp)

**Source:** https://9to5linux.com/ubuntu-24-04-5-lts-is-now-available-for-download-with-linux-7-0-and-mesa-26-2
**Karakeep doc:** `tebd3nkr44g57nirv5xqpjie`

Fifth and probably last point release for Noble Numbat. It's just a fresh install medium with Linux 7.0 and Mesa 26.2 baked in, so you don't download a mountain of updates after installing. Existing users just run `sudo apt update && sudo apt full-upgrade` and move on. Supported until June 2029, then Canonical wants your money for Ubuntu Pro.

## 18. GIMP 3.2.6 Released with UX Improvements, New Rotation Stylus Dynamics Input — by 9to5Linux

![9to5Linux](https://9to5linux.com/wp-content/uploads/2026/09/g326.webp)

**Source:** https://9to5linux.com/gimp-3-2-6-released-with-ux-improvements-new-rotation-stylus-dynamics-input
**Karakeep doc:** `dxt0tyf2bocn9iu16fct3iao`

Second maintenance release for GIMP 3.2, and the headline is stylus rotation dynamics for Wacom Art Pens. The Heal tool stops leaving dark smudges, the Color Picker now respects layer filters, and there's early prep work for a GTK4 port. KDE Plasma users get server-side decorations instead of GNOME-style CSD, plus a pile of security fixes. AppImage is up for grabs.

### Open-source Projects (RSS)

## 19. Open source AI coding agent you can install with curl — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/anomalyco/opencode)

**Source:** https://www.opensourceprojects.dev/post/0a850261-2637-40db-8b9e-28223e24a417
**Karakeep doc:** `zg9lylqp0pzs2v1wpvxsuhjt`
**GitHub:** https://github.com/anomalyco/opencode

206k stars on a TypeScript coding agent, MIT licensed. That's not a niche toy, that's the whole damn neighborhood showing up. Install with curl and it just works — no YAML ceremony, no "sign up for our cloud first" bullshit. If you're still paying for a closed-source agent, this is the repo that makes you feel dumb.

## 20. An open-source e-book reader that lets you ask questions about what you're readi... — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/codedogqby/readany)

**Source:** https://www.opensourceprojects.dev/post/696150dc-9049-4501-9441-dca941abf7c0
**Karakeep doc:** `z51k97lg3zzdd3gnupbqlle3`
**GitHub:** https://github.com/codedogQBY/ReadAny

TypeScript e-book reader that bolts RAG chat, semantic search, a local vector store, TTS, and WebDAV sync onto your EPUBs. 2.3k stars, license is a shrug (NOASSERTION), so read the fine print before you build a product on it. The "ask questions about the book you're reading" bit is genuinely useful, not just a demo gimmick. Cross-platform via Expo, so it runs on your phone and your desktop.

## 21. Nomad: run containers and legacy apps together on the same infra — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/hashicorp/nomad)

**Source:** https://www.opensourceprojects.dev/post/bf8de59c-f0c5-463b-b72d-092dc8cbfba1
**Karakeep doc:** `voxavosa7ngmqnm9u12lrxjw`
**GitHub:** https://github.com/hashicorp/nomad

HashiCorp's workload orchestrator in Go, 16.8k stars, and it'll happily run your containers, batch jobs, and crusty non-containerized legacy apps on the same box. Native Consul and Vault integration means you don't have to bolt on service discovery and secrets after the fact. It's the "I don't need a PhD in Kubernetes" answer to scheduling. License is NOASSERTION these days, which is HashiCorp-speak for "we changed the terms, go read them."

## 22. Axum: HTTP routing that gets tracing, compression, and timeouts for free via tow... — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/tokio-rs/axum)

**Source:** https://www.opensourceprojects.dev/post/eb6fcfa2-8227-4cf6-aacf-d945c424b174
**Karakeep doc:** `v3t7iitkqqb1t919afyd1tiq`
**GitHub:** https://github.com/tokio-rs/axum

Rust HTTP routing library from the tokio crew, 27k stars, MIT. The pitch is ergonomics and modularity — you get tracing, compression, and timeouts through tower middleware instead of hand-rolling them. It's the default "I want a web server in Rust without fighting the borrow checker all day" pick. If you're on actix-web and annoyed, this is where everyone's been migrating.

## 23. OBS plugin for showing keyboard, mouse and gamepad input on stream — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/univrsal/input-overlay)

**Source:** https://www.opensourceprojects.dev/post/3c1f0e86-4de1-45c8-9a75-b14878c11b1d
**Karakeep doc:** `udg9aid92hxdzwubqbuu1kfo`
**GitHub:** https://github.com/univrsal/input-overlay

C++ OBS plugin that overlays your keyboard, mouse, and gamepad inputs on stream, GPL-2.0, 4.1k stars. It's the thing every speedrunner and fighting-game streamer uses to prove they're not cheating. Customizable layouts so you can show a full keyboard or just the buttons that matter. Dead simple, does one job, no bloat.

## 24. A collection of Java algorithms meant for learning, not production — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/thealgorithms/java)

**Source:** https://www.opensourceprojects.dev/post/4d2ebdbc-838a-4ba7-98e0-ee8767c5938f
**Karakeep doc:** `t6f3f0iamy85wpoz14jethve`
**GitHub:** https://github.com/TheAlgorithms/Java

66k stars of Java algorithms and data structures, MIT, and it's explicitly for learning, not shipping. Every classic — sorting, searching, graphs, dynamic programming — implemented cleanly so you can actually read the code. It's the repo you point a junior at when they ask "how does Dijkstra actually work." Hacktoberfest magnet, so expect a steady stream of half-baked PRs alongside the good stuff.

## 25. Building explorable 3D worlds with natural language, running locally — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/localgpt-app/localgpt)

**Source:** https://www.opensourceprojects.dev/post/679fcb7e-67f4-4370-bba4-a21a4fe26cf6
**Karakeep doc:** `msjknrf76l7f2g05cg3ysx6l`
**GitHub:** https://github.com/localgpt-app/localgpt

A local AI assistant that "dreams explorable worlds" — Rust, Apache-2.0, 1.1k stars. It's built on Bevy, so the whole thing runs on your own box instead of phoning some cloud. The pitch is natural-language world-building, which is either genuinely cool or a fancy way to say "chatbot that renders a scene." Still, Rust + Bevy + local is a solid combo if you want to poke at it without a GPU bill.

## 26. An open-source coding agent for the Grok API, with Telegram remote control — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/superagent-ai/grok-cli)

**Source:** https://www.opensourceprojects.dev/post/67e7b944-7179-4fa6-9e78-46ad4c646196
**Karakeep doc:** `m53sthcidq4z0off3jlr5j20`
**GitHub:** https://github.com/superagent-ai/grok-cli

A coding agent wired to the Grok API, TypeScript, MIT, 3.5k stars. You can drive it from a CLI or remotely over Telegram, which is a neat trick for kicking off builds from your phone. It's basically Claude Code but pointed at xAI's model instead. If you're already paying for Grok, this is a cheap way to get agentic coding without another subscription.

## 27. A Web UI component library that never actually stopped updating — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/layui/layui)

**Source:** https://www.opensourceprojects.dev/post/fe3fdce1-b0a6-4c0a-b01f-90e8160b5d85
**Karakeep doc:** `klctphpffmyzipom2qc67ry5`
**GitHub:** https://github.com/layui/layui

Layui, a Web UI component library that follows the browser's native dev model — JavaScript, MIT, 30.5k stars. The description is in Chinese, which tracks, since this thing is huge in the Chinese web dev scene. It's been around forever and somehow still gets commits, which is more than you can say for half the JS frameworks that flared up and died. If you want a no-build-step UI kit that just works, this is it.

## 28. Apache Answer: Q&A platform software with a plugin system, built in Go and React — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/apache/answer)

**Source:** https://www.opensourceprojects.dev/post/ef7330fa-268f-4765-86eb-b5776cdc68ad
**Karakeep doc:** `gy8mlcjwh1wkfek36cz1xlcn`
**GitHub:** https://github.com/apache/answer

A Q&A platform for teams at any scale — community forum, help center, or knowledge base — Go + React, Apache-2.0, 15.7k stars. It's Apache-backed, so it's not going to vanish next week, and the plugin system means you can bolt on whatever you need. Basically a self-hosted Stack Overflow clone without the "closed as duplicate" attitude. Solid pick if you want your own support forum without paying Discourse.

## 29. Real-time Whisper transcription with word timestamps and speaker diarization — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/collabora/whisperlive)

**Source:** https://www.opensourceprojects.dev/post/11f2ea55-28ba-4a7a-9809-b7cda6ef872a
**Karakeep doc:** `f67q9hn2katcp66cx9c7vneq`
**GitHub:** https://github.com/collabora/WhisperLive

A nearly-live implementation of OpenAI's Whisper — Python, MIT, 4.3k stars. It does word-level timestamps and speaker diarization, and it's got backends for TensorRT, OpenVINO, and ROCm, so you can actually squeeze real-time out of it on decent hardware. From Collabora, the same folks who keep Linux graphics from being a dumpster fire. If you need live captions or dictation, this is the one to grab.

## 30. An ad-free Reddit client for Android with a built-in lazy scrolling mode — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/docile-alligator/infinity-for-reddit)

**Source:** https://www.opensourceprojects.dev/post/4021c101-fe94-4666-9f20-1a6df161970d
**Karakeep doc:** `ajaff8ntnbatjz6jejdp33t4`
**GitHub:** https://github.com/Docile-Alligator/Infinity-For-Reddit

A Reddit client for Android — Java, AGPL-3.0, 5.4k stars. No ads, and it's got a lazy scrolling mode so you can doomscroll hands-free, which is either a feature or a cry for help. It survived the great API-pocalypse by letting you plug in your own key, so it still works when the official app is busy shoving ads in your face. The AGPL license means any fork has to stay open too, which is a nice middle finger to Reddit.

### LinuxLinks (RSS)

## 31. Dionaea - honeypot for capturing exploit and malware activity — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/Honeypot-banner2.png)

**Source:** https://www.linuxlinks.com/dionaea-honeypot-capturing-exploit-malware-activity/
**Karakeep doc:** `bg8h225on3zh2pxm5oa20w3g`
**GitHub:** https://github.com/DinoTools/dionaea

A honeypot that sits there pretending to be a juicy target and logs whatever malware comes knocking. 819 stars, Python, GPL-2.0. Last pushed in 2024, so it's not exactly sprinting, but honeypots don't need to be fast — they need to be patient. Set it up, point some traffic at it, and watch the script kiddies trip over themselves. 🍯

## 32. LocalGo - LocalSend-compatible command-line file sharing — LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2022/05/Transfer_Files41021.jpg)

**Source:** https://www.linuxlinks.com/localgo-localsend-compatible-command-line-file-sharing/
**Karakeep doc:** `oudgfkz0bo6mt2rslkrxg23a`
**GitHub:** https://github.com/bethropolis/localgo

A Go implementation of the LocalSend protocol, so you can sling files across your LAN from a terminal instead of fiddling with a GUI. 16 stars, MIT, still actively pushed as of August 2026. Tiny project, but it does one thing and does it without making you install a whole Electron app. If you already use LocalSend on your phone, this is the CLI side you didn't know you wanted. 📡

## 33. 20 Best Free Linux Speech Recognition Tools — LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/02/voice-recognition.jpg)

**Source:** https://www.linuxlinks.com/best-free-linux-speech-recognition-tools-open-source-software/
**Karakeep doc:** `xumopb2s6izjeqtjzm9378t7`

A roundup of 20 open source speech-to-text toolkits, and it's basically the Whisper family reunion. Whisper, whisper.cpp, faster-whisper, sherpa-onnx, Kaldi, SpeechBrain, ESPnet — the usual suspects plus a few oddballs like Julius and Simon. If you want local dictation without shipping your voice to some cloud, this is the list to skim. Just don't expect any of them to nail your accent on the first try. 🎙️

## 34. Autasker – flexible offline task manager — LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2019/04/notepad-pen-with-words-from-todo-list-multicolored-background.jpg)

**Source:** https://www.linuxlinks.com/autasker-flexible-offline-task-manager/
**Karakeep doc:** `mjo4v7lhbz0t7xf41kgtj5vg`
**GitHub:** https://github.com/vadimerenkov/Autasker

A Kotlin Multiplatform to-do app that runs on Windows, Linux, and Android, and it's explicitly tagged "no-ai-used" — which is honestly refreshing. 33 stars, GPL-3.0, and it's got habit tracking plus "neurodivergent-support" in the topics, so someone actually thought about how real humans use task lists. Offline-first, no cloud bullshit. If your current to-do app is a subscription trap, this is worth a look. ✅

## 35. 16 Best Free and Open Source Linux Photo Management Software — LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/04/close-up-man-holding-photos-with-beautiful-landscapes-his-hands.jpg)

**Source:** https://www.linuxlinks.com/photomanagement/
**Karakeep doc:** `hnhunul70eqap9kkk9dtaxq1`

Sixteen tools for wrangling your photo hoard, and the heavy hitters are all here — digiKam, darktable, Shotwell, gThumb, KPhotoAlbum. Plus a few newer faces like TagStudio and Lap for the tag-and-search crowd. If you've got thousands of RAW files and no idea where anything is, this is the list. The web-gallery stuff is split into a separate roundup, so don't go looking for it here. 📷

## 36. 27 Best Free and Open Source Linux Plotting Tools — LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2019/02/plotting-software.jpg)

**Source:** https://www.linuxlinks.com/excellent-free-plotting-tools/
**Karakeep doc:** `tb4y9jfxya79ty53k0bxza06`

Twenty-seven ways to turn numbers into pretty pictures, from matplotlib and ggplot2 down to terminal plotters like Uniplot and Charta. The framing is simple: pick your poison based on language — Python folks get matplotlib, R folks get ggplot2, and everyone else can fight over gnuplot and ROOT. Some of these have been around since the mid-80s, which is either reassuring or a warning sign depending on your mood. 📊

## 37. PodFetch - self-hosted podcast manager with gPodder integration — LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2021/08/podcast_neon_2.jpg)

**Source:** https://www.linuxlinks.com/podfetch-self-hosted-podcast-manager/
**Karakeep doc:** `sbphvl1lzv53jel804w8aygp`
**GitHub:** https://github.com/SamTV12345/PodFetch

A self-hosted podcast downloader in Rust with a React frontend, so you can hoard episodes on your own box instead of trusting some app to keep them. 506 stars, Apache-2.0, actively pushed as of September 2026. It plays nice with gPodder, which means your existing podcast app can point at it. If you're already running a homelab, this slots right in next to the rest of the self-hosted pile. 🎧

## 38. UrsaOS - Arch-based Linux distribution with Plasma — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/04/Linux-Distributions.png)

**Source:** https://www.linuxlinks.com/ursaos-arch-based-linux-distribution/
**Karakeep doc:** `mlgo9gtkf4ohjod174r56dac`

Another Arch spin, because the world clearly needed one more. This one ships KDE Plasma on Wayland with a preconfigured desktop, an "Aurora" theme, and Btrfs snapshots out of the box. It even bundles its own package manager (BearHub) and an internet radio app (BearWave), because nothing says "rolling distro" like a built-in radio. If you want Arch without the blank-slate homework, this is that.

## 39. HPR – automatic offline activity tracker — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/08/022-hurry.png)

**Source:** https://www.linuxlinks.com/hpr-automatic-offline-activity-tracker/
**Karakeep doc:** `hcolj3wv63h4n7woo1r8115m`
**GitHub:** https://github.com/plexescor/HPR

A lightweight offline activity tracker for Windows and Linux, written in C++. 30 stars, so it's basically a ghost town, but it does the job without phoning home. Tracks what you do on your machine and keeps it local. Fine if you want a time log that doesn't sell your data.

## 40. Zephyr - lightweight modular Zsh framework — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2023/02/147_linux_interface.jpg)

**Source:** https://www.linuxlinks.com/zephyr-lightweight-modular-zsh-framework/
**Karakeep doc:** `ui8r30dv4bu1su17o9bh3gt0`
**GitHub:** https://github.com/mattmc3/zephyr

A Zsh framework that bills itself as "as nice as a cool summer breeze" — cute. 253 stars, MIT, pure Shell. Modular, so you only load the plugins you actually want instead of the whole oh-my-zsh kitchen sink. If your shell startup time makes you twitch, this is worth a look.

## 41. Focus Timer – Pomodoro time-management application — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/08/022-hurry.png)

**Source:** https://www.linuxlinks.com/focus-timer-pomodoro-time-management-application/
**Karakeep doc:** `wfpb1tldcluyp7dpfjyf8lpo`
**GitHub:** https://github.com/focustimerhq/FocusTimer

A GNOME Pomodoro timer in Vala, GPL-3.0, and a healthy 2,246 stars. It's the classic "work 25, break 5" thing, but native to GNOME so it doesn't look like a web app vomited onto your desktop. If you need a timer to guilt you into actually working, this does it cleanly.

## 42. Heralding - credentials-catching network honeypot — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/Honeypot-banner3.png)

**Source:** https://www.linuxlinks.com/heralding-credentials-catching-network-honeypot/
**Karakeep doc:** `oi74jwysoy38jt5b2cjjusyk`
**GitHub:** https://github.com/johnnykv/heralding

A Python honeypot that sits on your network and catches credentials from anyone dumb enough to try logging in. 395 stars, GPL-3.0. It fakes a bunch of services and logs every password some bot throws at it. Great for watching the script-kiddie traffic roll in and laughing.

## 43. Best Free and Open Source Alternatives to Microsoft Entra ID — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2021/08/Open-Source-Alternatives-Microsoft.jpg)

**Source:** https://www.linuxlinks.com/best-free-open-source-alternatives-microsoft-entra-id/
**Karakeep doc:** `x4lgyjbzr4zm1vsnav7tgtv1`

Entra ID (née Azure AD) is Microsoft's cloud identity thing, and no single open source project covers the whole mess. The roundup picks four: Keycloak for SSO/federation, Janssen for enterprise identity standards, Kanidm for Linux-heavy shops, and FreeIPA for Kerberos/LDAP networks. Keycloak gets the top nod. If you're tired of paying Microsoft to manage your logins, one of these probably fits.

## 44. Croc GUI – secure cross-platform file transfer — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/04/Transfer_Files41021-c.png)

**Source:** https://www.linuxlinks.com/croc-gui-secure-cross-platform-file-transfer/
**Karakeep doc:** `udbgrqz75ak39sd4szrp4s5r`
**GitHub:** https://github.com/interfluve-wav/croc-gui

A desktop GUI for croc, the encrypted P2P file transfer tool, so you don't have to remember the terminal flags. TypeScript, 21 stars, drag-and-drop plus QR codes and LAN mode. macOS, Windows, Linux. If you've ever watched a non-technical friend's eyes glaze over at a croc command line, this is for them.

## 45. 4 Best Free and Open Source Secret Scanning Tools - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2023/08/people-holding-cloud-network-security-symbols.jpg)

**Source:** https://www.linuxlinks.com/best-free-open-source-secret-scanning-tools/
**Karakeep doc:** `ndwkh2xmj52p3i3bq59cl0sp`

LinuxLinks rounds up four tools that hunt for API keys and passwords you accidentally committed. The lineup is Gitleaks, TruffleHog, detect-secrets, and Talisman. Gitleaks and TruffleHog scan repos and commit history, detect-secrets and Talisman try to catch the leak before it lands. If you've ever pushed an AWS key to a public repo, one of these is your new best friend. 🙃

## 46. Spacefun - lightweight Debian-based Linux distribution - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/04/Linux-Distributions.png)

**Source:** https://www.linuxlinks.com/spacefun-lightweight-debian-based-linux-distribution/
**Karakeep doc:** `svsisplbnmsw40kh424ao0bg`

Another Debian Blend, because the world clearly needed one more. Spacefun ships stable and rolling editions, with LXQt as the flagship desktop and GNOME, KDE, and Xfce variants on the rolling side. It runs on 1GB of RAM and 20GB of storage, so your grandma's 2012 laptop is back in business. Live media included, install if you dare. 🚀

## 47. MINISFORUM M2 - Does Linux Schedule Panther Lake Correctly? - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/05/MinisforumM2-banner.png)

**Source:** https://www.linuxlinks.com/minisforum-m2-does-linux-schedule-panther-lake-correctly/
**Karakeep doc:** `cc53raohdvq9i9uwnuc60qrd`

LinuxLinks digs into whether the kernel actually schedules Intel's three-tier Panther Lake cores properly on the MINISFORUM M2. The Core Ultra 7 356H has 4 P-cores, 8 E-cores, and 4 LP E-cores, and the kernel does tell them apart — P-cores get capacity 1004-1024, E-cores 714, LP E-cores 637. Then it's nine pages of taskset-pinned OpenSSL benchmarks to see where work actually lands. Spoiler: the topology looks right, the real question is whether the scheduler uses it sanely under load. 🔬

## 48. Watchtower - terminal-based global intelligence dashboard - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/latest-news-2.png)

**Source:** https://www.linuxlinks.com/watchtower-terminal-based-global-intelligence-dashboard/
**Karakeep doc:** `yn4y13sytrskuwyyr46kerlq`
**GitHub:** https://github.com/lajosdeme/watchtower

A clean, minimal terminal dashboard for global intelligence, written in Go. 314 stars, MIT license. It's the kind of thing you open in a tmux pane to feel like you're in a spy movie while actually just reading headlines. Not archived, last pushed March 2026. 🕵️

## 49. CastCharm - self-hosted podcast manager with clean web UI - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2021/12/podcast-icon-neon-podcast-light-signs-sign-boards-line-art-light-banner-illustration.jpg)

**Source:** https://www.linuxlinks.com/castcharm-self-hosted-podcast-manager/
**Karakeep doc:** `lbwaj1kce0klihw4s1wimdln`
**GitHub:** https://github.com/CastCharm/castcharm

A self-hosted podcast manager with a clean web UI, JavaScript, MIT license. One star, so it's basically a personal project with a nice README. Still, if you want your podcast queue off some cloud service and on your own box, here's a starting point. 🎙️
