---
date: 2026-09-08
slug: 2026-09-08-morning-brew
tags: Apps,Arch,Beelink,C,C++,CAPTCHA,CLI,Debian,Desktops,Distro,Distros,EQi Core 3 304,Earth Observation,Education,Environmental Science,GNOME,GStreamer,GUI,Gentoo,Git,Go,Google,Graphics,Hardware,Haskell,IRC,Intel,Intel Core 3 304,Internet,KDE,KDE Plasma,Linux distribution,Llama 3.2,MPD,Mini PC,MocaccinoOS,Multimedia,NPU,News,Ocean Science,Oceanography,OpenVINO,Productivity,Python,Qt 4,Remote Sensing,Reviews,Roundup,Rust,Satellite Imagery,Scientific,Security,TUI,Ubuntu,Utilities,Web Apps,artificial intelligence,audio,bash,calculator,circuit simulator,clock,desktop environment,distribution,distro,free,geospatial,image compression,mathematics,multimedia framework,music player,noise,noise generator,open source,podcast,privacy,productivity,ratatui,reCAPTCHA,scanner,security,self-hosted,systemd,tui,typing,web,web security,wireless
---

# Morning Brew — 2026-09-08

Nine things you actually saved by hand, then the RSS firehose. The hand-picked stuff: two Linux-vs-Mac videos, a HeyGen HTML-to-video repo, two X posts (a self-hosted PaaS and a Burp alternative), plus mise, DevPod, AMD's "personal supercomputer," and Linus blaming AI for a fat kernel. The rest is seventeen LinuxLinks roundups, three 9to5Linux news bits, and two more videos.

## 1. 🎬 Video — The BEST Way To Learn Linux — by Capped Dev

![Capped Dev](https://img.youtube.com/vi/pC8-qBFsQ08/maxresdefault.jpg)

**Source:** https://youtu.be/pC8-qBFsQ08?si=Px-Y_nXkfkoaJyr3
**Karakeep doc:** `wbaz4u72rve33b5a4trzd0m5`

Guy nukes his own drivers, breaks his displays, then types `help` and the terminal basically says "no." His five-step plan: pick a distro, actually install it (and ditch your other OS so you're forced to use it), learn the terminal, customize everything, then brag about your config files online. Recommends linuxjourney.com for the basics. Standard "Linux is a superpower, Windows is garbage" pitch, but the self-deprecating opener is honest about how much it sucks at first. 🙄

## 2. 🎬 Video — I tried using Linux to see if it's better than Mac — by Reysu

![Reysu](https://img.youtube.com/vi/3WfPq-_ehaM/maxresdefault.jpg)

**Source:** https://youtu.be/3WfPq-_ehaM?si=MY0coDKhbAnc3q-n
**Karakeep doc:** `aluv5l6o9oq07cc69scbxyvn`

Parallels-sponsored video where he slaps Omakub (DHH's keyboard-first distro) on a Windows laptop and turns it into a "productivity machine." The pitch: everything's built in — AI dictation, screen recording, Tailscale, flux, window tiling — no hunting for apps or paying subscriptions. He admits Mac still wins on creative apps and local LLMs, but realizes he's not actually locked into Apple. The "I can SSH into my Mac for the AI agents" bit is the only part that matters. 🤷

## 3. heygen-com/hyperframes: Write HTML. Render video. Built for agents. — by heygen-com

![heygen-com](https://opengraph.githubassets.com/6907f34051e739f4f359e3c80e8f5cdd2752c667cb8fa5f07a11b8fe76e48ca7/heygen-com/hyperframes)

**Source:** https://github.com/heygen-com/hyperframes
**Karakeep doc:** `jcyek4z7ps6eobx0qvcehfeo`

HeyGen's tool for turning HTML into rendered video, aimed at agents. Write markup, get a video out the other end. That's the whole pitch — no docs, no fluff, just "write HTML, render video." Could be useful if you're building anything that needs programmatic video generation. 🎬

## 4. bex: self-hosted AI-native PaaS — by Dan Kornas

![Dan Kornas](https://pbs.twimg.com/media/HRh0hZkWcAMeJ0r.jpg:large)

**Source:** https://share.google/HK3SeqGI8QWGWZQPx
**Karakeep doc:** `jwpwb4j81hxhipu5do6fksvj`

Self-hosting doesn't mean hand-operating Kubernetes. bex is an open-source, AI-native PaaS that deploys apps from Git to HTTPS on infra you own. Turns a Render-style `render.yaml` blueprint into a running service without building a separate control plane. Basically "Render, but on your own boxes." 🚀

## 5. Open-source Burp Suite alternative — by Tom Dörr

![Tom Dörr](https://pbs.twimg.com/media/HRdBI9ZasAAa1QH.jpg:large)

**Source:** https://share.google/wO2IlY3cgr0bmFhEm
**Karakeep doc:** `v6g87jn3afyvgxtn4yn2o496`

Intercepts HTTP traffic, replays requests, and does detailed log searching — a fully open-source alternative to Burp Suite for security research. If you're tired of Burp's licensing, this is the free option. 🔍


## 6. Dev tools, environments, and tasks — by mise-en-place

![mise-en-place](https://mise.jdx.dev/social/0b47721f68214833.png)

**Source:** https://mise.jdx.dev/
**Karakeep doc:** `ryqzgq0ot7x5hlqxmtxco52f`

asdf on steroids. One config file for tools, env vars, tasks, packages, and dotfiles. Replaces the pile of half-broken shell scripts I've been dragging around for years. Worth a look before I hand-roll yet another setup script.

## 7. DevPod — by DevPod

![DevPod](https://cdn.prod.website-files.com/645b6806227d4a212e2d01ca/67d8d6796238b736fb3b37b8_Open%20Graph.png)

**Source:** https://devpod.sh/
**Karakeep doc:** `jckbmyaajcx0j7qbsnp61yqu`

Codespaces but open-source and client-only. Runs against any infra, any IDE, any language. No vendor lock-in, no server to babysit. "Unopinionated" is doing a lot of work there, but the idea's solid.

## 8. AMD unveils 'personal super computer' for new era of computing — by euronews

![euronews](https://images.euronews.com/articles/stories/09/90/46/69/1200x675_cmsv2_7aa071d9-e235-5fe2-9be5-38f4b60909a3-9904669.jpg)

**Source:** https://www.euronews.com/next/2026/09/08/amd-unveils-personal-super-computer-for-new-era-of-computing
**Karakeep doc:** `uaqj1g3sn0rpcme6uhqxur6e`

AMD's calling a workstation a "personal supercomputer" and hoping the AI buzzword does the marketing. Launched in Berlin, aimed at the "completely new era of computing" — whatever that means. Marketing fluff, but the hardware specs might actually be worth a look.

## 9. Might as well blame AI for this giant Linux release candidate, says Linus Torvalds — by theregister

![theregister](https://image.theregister.com/5238260.jpg?imageId=5238260&x=0&y=0&cropw=100&croph=100&panox=0&panoy=0&panow=100&panoh=100&width=1200&height=683)

**Source:** https://www.theregister.com/os-platforms/2026/09/07/might-as-well-blame-ai-for-this-giant-linux-release-candidate-says-linus-torvalds/5294697
**Karakeep doc:** `lg9gisirrmkvx795o0i17fom`

Linus can't find a single cause for why Linux 7.3's rc2 is so fat, so he's blaming AI — "whether that's really the cause or not, it's an easy thing to blame." Last week he called himself a "grade A nincompoop" for doing a system upgrade mid-merge-window. The man's self-deprecation is the only honest thing in kernel land.


## 10. Yutovo – visual calculator and mathematical text editor — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/01/035-calculator.png)

**Source:** https://www.linuxlinks.com/yutovo-visual-calculator-mathematical-text-editor/
**Karakeep doc:** `mj1jd22r4yl955racfeikj59`

A graphical calculator and math editor that does WYSIWYG formulas, symbolic calculations, unit conversion, and function plotting all in one window. Basically a calculator that thinks it's a word processor. If you still reach for a physical TI-84, this might finally drag you into the 21st century. Qt 4 under the hood, so it's old-school but functional.

## 11. hcxtools – Analyze Wi-Fi Capture and Hash Files — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/03/WiFi-Internet-c.png)

**Source:** https://www.linuxlinks.com/hcxtools-analyze-wi-fi-capture-hash-files/
**Karakeep doc:** `f2rakwpfq6mw1ahfrj3iukm9`

A command-line suite for converting, filtering, and analysing wireless captures and authentication hashes during authorised security assessments. The "authorised" part is doing a lot of work there. If you're pentesting Wi-Fi, this is the toolbox you actually need instead of whatever sketchy script you found on a forum. Pure C, CLI only, no hand-holding.

## 12. 7 Useful Free and Open Source Linux Background Noise Generators — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2021/09/abstract-background-with-sound-waves-design.jpg)

**Source:** https://www.linuxlinks.com/useful-free-open-source-linux-background-noise-generators/
**Karakeep doc:** `cjgcphowuy5bjrg8kouy8atw`

A roundup of seven ambient noise generators that don't demand attention but supposedly make a workspace feel calmer. Rain, ocean, brown noise — the standard set for drowning out your open-plan office neighbour. If you need white noise to focus, one of these beats a YouTube tab that autoplays ads. Nothing revolutionary, just a niche filled competently.

## 13. MERK – cross-platform graphical IRC client — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2019/02/group-diverse-people-with-speech-bubble-icon.jpg)

**Source:** https://www.linuxlinks.com/merk-cross-platform-graphical-irc-client/
**Karakeep doc:** `uc5tmwmwkhhjuau4u4rg7k4u`

A highly configurable open source graphical IRC client with multiple server connections, scripting, plugins, theming, and logging. Yes, IRC still exists, and someone's still building clients for it. If you're nostalgic for the 90s or actually still hang out on Libera, this is a Python-based option that won't make your eyes bleed. Configurable to a fault, which is either a feature or a warning.

## 14. Pulsar OS – Linux distribution with a macOS-style workflow — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/04/Linux-Distributions.png)

**Source:** https://www.linuxlinks.com/pulsar-os-linux-distribution-macos-style-workflow/
**Karakeep doc:** `vbhf2pm77cexniwtpz34bvnz`

A GNOME-based Linux distribution with Arch and Debian editions, built to give you a familiar macOS-style desktop workflow. So you can have the Apple look without the Apple price tag or the Apple walled garden. Comes in both Arch and Debian flavours, which is a nice touch for people who can't agree on anything. If you want macOS muscle memory on Linux, this is the shortcut.

## 15. 12 Best Free and Open Source GUI Image Compression Tools — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2021/09/3d-rendering-3d-text-discount-broken.jpg)

**Source:** https://www.linuxlinks.com/best-free-open-source-gui-image-compression-tools/
**Karakeep doc:** `zjz5istp04ql7y2603lahm2k`

A roundup of twelve GUI tools for shrinking images without the command line. Headliners include Curtail and Converseen, plus a few you've probably never heard of. If you're tired of `optipng` flags and just want a button to click, one of these will do the job. Compression is boring, but bloated images are worse.


## 16. QucsatorRF – RF and microwave circuit simulator — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2023/03/circuit-board-close-up-with-different-components.jpg)

**Source:** https://www.linuxlinks.com/qucsatorrf-rf-and-microwave-circuit-simulator/
**Karakeep doc:** `gr2zp289n257fglz5o75w0fg`

QucsatorRF is a command-line circuit simulator for RF and microwave circuits, and it's the backend that Qucs-S leans on. If you're doing anything with high-frequency stuff, this is the engine doing the actual math. No GUI, just a CLI — which is either a feature or a pain in the ass depending on your mood. 🤷

## 17. Termitype – feature-rich terminal typing test — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2019/02/young-woman-typing-keyboard.jpg)

**Source:** https://www.linuxlinks.com/termitype-feature-rich-terminal-typing-test/
**Karakeep doc:** `owemt4cngz6lpdggrcetq25p`

Termitype is a terminal typing test with multiple modes, themes, stats, custom word sets, and local results tracking. Written in Rust, so it's fast and doesn't phone home. If you want to flex your WPM without leaving the terminal, this is the one. ⌨️

## 18. Beelink EQi 304 Mini PC – NPU and Llama — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/07/Beelink-EQi-304-banner.png)

**Source:** https://www.linuxlinks.com/beelink-eqi-304-mini-pc-npu-llama/
**Karakeep doc:** `b0bq4511l30mok623k685el1`

Steve tests the Beelink EQi Core 3 304's 15-TOPS Intel NPU with OpenVINO and Llama 3.2 1B to see if modest NPUs are actually worth a damn. Spoiler: it's a real-world benchmark, not marketing fluff. If you've been wondering whether those little NPUs on cheap mini PCs do anything useful, this is the answer. 🤖

## 19. tenki – terminal clock with animated weather effects — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/02/038-clock.png)

**Source:** https://www.linuxlinks.com/tenki-terminal-clock-animated-weather-effects/
**Karakeep doc:** `rj0z46xq2lycmqy9a9fd4l87`

tenki is a Rust terminal clock with animated rain, snow, and meteor effects, plus configurable wind, colours, and animation speed. It's built on ratatui, so it looks way better than a terminal clock has any right to. Pointless but delightful — the best kind of tool. ⏰

## 20. 15 Best Free and Open Source Graphical Podcast Tools — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2021/08/podcast_neon_2.jpg)

**Source:** https://www.linuxlinks.com/podcasttools/
**Karakeep doc:** `e9t4e0z5dvukoewmcdx6cwhd`

A roundup of 15 free and open source graphical podcast tools, covering everything from catchers to full-blown managers. Headliners include gPodder and Vocal, so there's something for both the "just play it" crowd and the "curate my whole feed" crowd. If you're still using a proprietary podcast app, this list is your excuse to stop. 🎙️

## 21. hympd – simple responsive web interface for MPD — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/04/musical_notes_700x350-c.png)

**Source:** https://www.linuxlinks.com/hympd-simple-responsive-web-interface-mpd/
**Karakeep doc:** `viyl5nuh486qym5ro3g4rpf6`

hympd is a lightweight responsive web interface for MPD with queue management, search, playback controls, themes, and Vim-style navigation. Written in Haskell, because of course it is. If you run MPD and want a browser tab instead of a native client, this does the job without the bloat. 🎵


## 22. 5 Best Free and Open Source Earth Observation and Ocean Science Tools — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/09/3d-render-sunrise-view-from-space-planet-earth.jpg)

**Source:** https://www.linuxlinks.com/best-free-open-source-earth-observation-ocean-science-tools/
**Karakeep doc:** `hlzijyrvas2us579wg7odb9v`

Roundup of free tools for Earth observation, remote sensing, ocean science, and satellite data. Covers QGIS for geospatial work, plus a few ocean-simulation and satellite-imagery tools if you're into that sort of thing. Nothing revolutionary, but a decent starting list if you're poking at environmental data without paying for ArcGIS.

## 23. Best Free and Open Source Alternatives to Google reCAPTCHA — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/CAPTCHA-banner2.png)

**Source:** https://www.linuxlinks.com/best-free-open-source-alternatives-to-google-recaptcha/
**Karakeep doc:** `p770q2v0onyj5r653zgzpu29`

Roundup of self-hosted CAPTCHA options so you can stop feeding Google your traffic data. Names a few headline picks like hCaptcha and Friendly Captcha, plus some fully self-hosted ones if you want zero third-party calls. Handy if you're sick of reCAPTCHA's privacy grab and want something you actually control.

## 24. Gitleaks – detect secrets in Git repositories and files — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/12/117-security.png)

**Source:** https://www.linuxlinks.com/gitleaks-detect-secrets-git-repositories/
**Karakeep doc:** `a4erwxk2ru8ggwyen74algnh`

Gitleaks scans Git repos, files, and stdin for passwords, API keys, tokens, and other hard-coded secrets. Go-based CLI, fast, and it'll catch the AWS key someone committed at 2am before it ends up in a breach. If you're not running something like this in CI, you're asking for trouble.

## 25. Fluxion – Wireless Security Auditing Tool — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2023/01/1946-wifi.jpg)

**Source:** https://www.linuxlinks.com/fluxion-wireless-security-auditing-tool/
**Karakeep doc:** `bno9ixlhtxbtjpj50ktjsek4`

Fluxion is a terminal-based tool for testing WPA/WPA2 network exposure via controlled captive-portal attacks. It's the "evil twin" social-engineering trick — fake a login page, grab the password. Bash-based, and only for auditing networks you actually own, obviously.

## 26. XicTools – electronic design and circuit simulation suite — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2023/03/circuit-board-close-up-with-different-components.jpg)

**Source:** https://www.linuxlinks.com/xictools-electronic-design-and-circuit-simulation-suite/
**Karakeep doc:** `gz8z7r67ku4qxvyjqnfb1cjq`

XicTools is an electronic design suite with the Xic IC layout editor, WRspice circuit simulator, and extraction tools. C++-based, aimed at chip and circuit design rather than hobbyist breadboarding. Niche, but if you're doing actual IC layout it's a real open-source option.


## 27. GStreamer 1.28.7 Open-Source Multimedia Framework Adds Support for OpenCV 5 — by 9to5linux

![9to5linux](https://9to5linux.com/favicon.ico)

**Source:** https://9to5linux.com/gstreamer-1-28-7-open-source-multimedia-framework-adds-support-for-opencv-5
**Karakeep doc:** `jn82c03ltnnyxlzr1z0vsdxn`

Seventh maintenance drop in the 1.28 series, a month after 1.28.6. The headline is OpenCV 5 build support, plus a pile of fixes: keyframe detection regressions in mxfdemux, off-by-one errors in ssdtensordec that were mislabelling objects, and a bunch of memory leaks. Nothing sexy, just the usual "we broke it, we fixed it" churn. Install from your distro repos, don't bother compiling the tarball.

## 28. KDE Plasma 6.7.5 Desktop Environment Is Out with Many Improvements and Fixes — by 9to5linux

![9to5linux](https://9to5linux.com/favicon.ico)

**Source:** https://9to5linux.com/kde-plasma-6-7-5-desktop-environment-is-out-with-many-improvements-and-fixes
**Karakeep doc:** `o97bz3gadnmxubjm3gkttyri`

Fifth point release for Plasma 6.7, mostly Discover and Spectacle fixes. Discover stops crashing on RPM-OSTree, stops getting stuck on Snap backends, and Spectacle takes screenshots faster. Also fixes a daemon crash on Wi-Fi connect and a DrKonqi crash loop. Next up is 6.7.6 in November, then the Wayland-only 6.8 lands October 14th — so enjoy your X11 while it lasts.

## 29. MocaccinoOS 26.09 Adds x86-64-v3 Optimized Builds for Improved Performance — by 9to5linux

![9to5linux](https://9to5linux.com/favicon.ico)

**Source:** https://9to5linux.com/mocaccinoos-26-09-adds-x86-64-v3-optimized-builds-for-improved-performance
**Karakeep doc:** `cpv69iu2k9dq4p9sn2e3ees7`

Gentoo-based distro, new stable ISO. The interesting bit is opt-in x86-64-v3 builds — you run `sudo luet install layers/X-v3` manually, and they rebuild Mesa, FFmpeg, Vulkan-loader and friends at v3 level. Devs call v3 "the sweet spot" since it covers a decade of mainstream CPUs without the v4 hardware exclusions. COSMIC edition bumps to 1.7, Mesa to 26.2.1. Still a niche Gentoo wrapper, but the v3 angle is a decent reason to glance at it.

## 30. 🎬 Video — This Free Database Client Has One Serious Problem... (DBX) — by Better Stack

![Better Stack](https://img.youtube.com/vi/b6rVCrBPbe8/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=b6rVCrBPbe8
**Karakeep doc:** `n8sc5owudooxsdl6vlqek02x`

DBX is a free database client with 90+ engines and 18k stars, and the MCP server is genuinely neat — your coding agent talks to saved connections without you pasting passwords into chat. But the catch is a doozy: it stores saved passwords in plain text in a local SQLite file called DBX.db, and the issue's been open since June 12th. The maintainer fixes everything else at warp speed but keeps losing on local credential storage. Free is nice, but don't put production creds in a tool that leaves them sitting in cleartext.

## 31. 🎬 Video — This Security Issue Is Too Funny To Ignore — by Brodie Robertson

![Brodie Robertson](https://img.youtube.com/vi/DYu9391lVP0/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=DYu9391lVP0
**Karakeep doc:** `yshztt7ypyh55n3lcqqiu728`

Omarchy shipped a custom Kitty config with `allow_remote_control yes` since day one, which means catting a file with escape sequences can run arbitrary commands in your terminal. The "exploit" is literally `cat pwn` — you're not executing anything, just printing a file, and it runs `touch /tmp/pwn`. Kitty's dev has known remote control is insecure since 2019 and basically shrugged. Omarchy's fix is switching to `socket-only`, which is what it should've been from the start. Don't enable remote control yourself unless you've got a damn good reason.

