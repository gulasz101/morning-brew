---
date: 2026-09-03
slug: 2026-09-03-morning-brew
tags: karakeep,digest,LinuxLinks,Open-source Projects,YouTube,Linux,open source,CLI,GUI,Roundup,networking,astronomy,speech recognition,bookmark manager,VPN,distro,screen capture,font manager,test automation,audio editing,Rust,Python,C,C++,Go,PHP,Debian,Arch Linux,Wayland,Hyprland,Phosh,Niri,OpenRC,TUI,productivity,calibration,mailing list manager,self-hosted,privacy,hardware,software,free,text,automation,frameworks,testing,distribution,mobile,smartphone,multimedia,utilities,Internet,Web Apps,ARM,graphics,books,tutorials,programming,history,Apps,Audacity,News,audio editor,Proprietary Software,Software Alternatives,free software
---

# Morning Brew — 2026-09-03

Yesterday's hoard: **36 bookmarks** — 8 YouTube videos (all transcribed) and 28 articles. A heavy LinuxLinks day (17 items), a fat Open-source Projects feed (10), and a handful of videos worth your time. The bare date query dropped 16 of these — I unioned the domain feeds to catch them all, so nothing's missing this time.

---

## 1. 🎬 Video — Talking Heads Ep.448: GPUs are expensive; Everything old is new; Google = Monopoly — by Craft Computing

![Craft Computing](https://i.ytimg.com/vi/Fr68iH8A4p8/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=Fr68iH8A4p8
**Karakeep doc:** `c1s30hr8yfkbye2obiuz9nmp`

Jeff and Rhett's weekly beer-and-tech live show. The meat: TechSpot tracked GPU prices across 10 countries and found the average card is **28% above MSRP** — the RTX 5090 is 136% over. Jeff's take is that MSRP is a lie reviewers should stop repeating, and he's turning down NAS review samples because nobody can afford the hard drives to fill them. The long rant at the end is about Flock/Axon license-plate cameras: 78+ officers arrested for stalking exes with them, zero documented cases of them actually catching a violent criminal. Worth it for the surveillance-state rant alone.

---

## 2. ZFontManager — cross-platform font manager — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/05/044-font.png)

**Source:** https://www.linuxlinks.com/zfontmanager-cross-platform-font-manager/
**Karakeep doc:** `o7cgn0fgjb1vjbsv0epcsxw9`

A Rust font manager for Linux/Windows/macOS that keeps everything local — no account, no cloud, no telemetry. The killer feature is font activation/deactivation: you can yank a font out of app menus without uninstalling the file, in batches, or temporarily until the app closes. Grid/list/waterfall views, tags, collections, side-by-side comparison, variable-font and OpenType inspection. GPLv3, from TheHolyOneZ.

---

## 3. Gnuastro — manipulate and analyse astronomical data — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/04/063-astronomy.png)

**Source:** https://www.linuxlinks.com/gnuastro-manipulate-analyse-astronomical-data/
**Karakeep doc:** `otmhoooijg0kgmyajv6nm6o1`

GNU Astronomy Utilities — a collection of CLI programs and libraries for FITS data. The star is NoiseChisel, which detects faint diffuse structures *without* the usual fixed signal-to-noise threshold, and MakeCatalog for measuring labelled images. Consistent CLI across all tools so you can chain them into pipelines. GPLv3, C, by Mohammad Akhlaghi.

---

## 4. aTrain — automatically transcribe recorded speech — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/02/voice-recognition.jpg)

**Source:** https://www.linuxlinks.com/atrain-automatically-transcribe-recorded-speech/
**Karakeep doc:** `zcj7t4q9s49g9gxe54dqwixt`

A GUI app for transcribing interviews/research recordings *locally* — no audio leaves your machine, which matters for GDPR and confidential data. Uses faster-whisper for transcription and pyannote.audio for speaker detection. Outputs timestamped transcripts importable into MAXQDA/ATLAS.ti/nVivo. AGPLv3, Python, from the University of Graz.

---

## 5. 16 Best Free and Open Source Text-Based Bookmark Managers — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/01/019-bookmark.png)

**Source:** https://www.linuxlinks.com/best-free-open-source-text-based-bookmark-managers/
**Karakeep doc:** `v1v642y25jl25zjugc4oe65m`

The CLI companion to the GUI roundup, triggered by Pocket's shutdown. The list: nb, Shiori, buku, Tbmk, IntelliShell, GoSuki, bmm, Bookmark, Tempesta, star, Marcador, bkmr, crumbs, bookmarkmenu, book, bmk. If you're a terminal rat who hoards URLs, buku and nb are the two worth a real look.

---

## 6. 27 Best Free and Open Source Test Automation Tools — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/08/software-development-testing.png)

**Source:** https://www.linuxlinks.com/best-free-test-automation-tools/
**Karakeep doc:** `baj96chg1r33llfvyxerqf2s`

The full QA roundup: Appium, Cypress, Robot Framework, Cucumber, Selenium, Gauge, Nightwatch, WebdriverIO, Detox, Allure, Karate, TestCafe, Playwright, Maestro, CodeceptJS, Schemathesis, tox, nox, Carina, Testsigma, SeleniumBase, Watir, Serenity, Selenide, Cerberus, Galen. Playwright and Cypress are the two that actually matter for web work; Schemathesis is the sleeper for API property-based testing.

---

## 7. SlyOS — lightweight Arch-based distribution — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/04/Linux-Distributions.png)

**Source:** https://www.linuxlinks.com/slyos-lightweight-arch-based-distribution/
**Karakeep doc:** `tsorme35yidylj6fgi9rins3`

An Arch-based distro that's opinionated in a good way: Niri (scrollable tiling Wayland compositor) as the desktop, **OpenRC instead of systemd**, ReGreet + greetd for login, linux-cachyos-lts kernel, Calamares installer. Ships Minimal and Complete images. KISS principle, privacy-minded, avoids Qt where it can. From Minaucro.

---

## 8. Open Source Alternatives to Proprietary Software — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/Open-Source-Alternatives.png)

**Source:** https://www.linuxlinks.com/open-source-alternatives/
**Karakeep doc:** `rlulaoipbmb56attzodfquja`

The master index page for LinuxLinks' "alternatives to Big Tech" series — Microsoft, Google, Adobe, Apple, Autodesk, Oracle, Cisco, IBM, Atlassian, Corel, Intuit, SAS, Progress, Salesforce, Citrix. Each links to a per-company guide. The framing is honest: an alternative doesn't reproduce every feature, just the comparable core. Good bookmark if you're de-Googling.

---

## 9. jdaviz — interactive astronomical data visualisation and analysis tools — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2021/05/milky-way-arch-starry-sky-alps-panoramic-view-astro-photography-stargazing-light-pollution-valley.jpg)

**Source:** https://www.linuxlinks.com/jdaviz-interactive-astronomical-data-visualisation-analysis-tools/
**Karakeep doc:** `m3040jtaxhr0a5e5hw52hz6r`

STScI's Jupyter-based astronomy toolkit — image, spectrum, and cube viewers with aperture photometry, spectral extraction and line fitting. Runs in a notebook, standalone, or embedded in a website. Designed around JWST observing modes. BSD-3, Python.

---

## 10. Audacity 4.0 Open-Source Audio Editor Officially Released — by 9to5Linux

![9to5Linux](https://9to5linux.com/wp-content/uploads/2026/06/aud4b.webp)

**Source:** https://9to5linux.com/audacity-4-0-open-source-audio-editor-officially-released-heres-whats-new
**Karakeep doc:** `c58kq05qpw0ah3616uw2onxr`

Audacity 4.0 is out — a major revamp. New project manager, Nyquist/VST3/LV2/AU plugin support, spectral editing, a rebuilt Qt interface with native HiDPI, lead-in recording, loop-region export, clip grouping, and a new `.aup4` format that's backwards-compatible with v3 projects. The AppImage is now truly universal. (The karakeep feed title was a Cloudflare interstitial — the real headline is this.)

---

## 11. Linux: Software, Distros & Hardware — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2022/05/35940-linux-home.jpg)

**Source:** https://www.linuxlinks.com/linuxlinks-home-linux/
**Karakeep doc:** `spx2pvxscce9mryrqzvfpug9`

The LinuxLinks hub page — 13,109 articles since 1994. Indexes their software directory, distro list, hardware reviews (mini PCs, NAS, SBCs), and the alternatives series. A good landing page to keep around if you want the whole catalogue in one place.

---

## 12. 🎬 Video — Cloudflare Just Deleted 100TB of Memory — by Better Stack

![Better Stack](https://i.ytimg.com/vi/KoziBW5p--c/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/KoziBW5p--c
**Karakeep doc:** `i02t1yn8z5w5tma9fkrgjdfb`

Cloudflare reclaimed ~100TB of RAM across its fleet without adding a single server, just by re-laying-out DNS cache entries in Rust. A cached entry was 953 bytes, mostly bookkeeping — they swapped `Vec`/`String` (which carry a capacity field) for boxed slices/strings, and packed the answer/authority/additional sections behind 2-byte offsets. Result: 953 → 420 bytes (56% smaller), inserts 43% faster, lookups 19% faster. That's ~130 servers' worth of RAM for free.

---

## 13. Kickstart.nvim: a small, single-file Neovim config that's fully documented — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/nvim-lua/kickstart.nvim)

**Source:** https://www.opensourceprojects.dev/post/28914048-b5ea-49dc-adf0-169561443808
**Karakeep doc:** `yz6ogfncwmqjduz5fumkdffm`

The middle ground between "build Neovim from scratch" and "clone a stranger's dotfiles." A single `init.lua` where every line is commented, covering lazy.nvim, LSP, tree-sitter. Not a distribution — a teaching tool disguised as a config. Uses the "Use this template" workflow so you get your own fork with your own history.

---

## 14. freeCodeCamp's open-source codebase and free, self-paced full-stack curriculum — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/freecodecamp/freecodecamp)

**Source:** https://www.opensourceprojects.dev/post/e85d6848-d896-4a56-8a27-b626305e30fe
**Karakeep doc:** `x9rhbwlhrmdg8vyf7u05hzfj`

The whole freeCodeCamp platform is open source — curriculum *and* the site code. Certifications in Responsive Web Design, JS, Python, databases, back-end APIs, plus language certs (English A2/B1, Spanish, Chinese). 100,000+ people got their first dev job through it. Verifiable credentials, first-timers-friendly for contributors.

---

## 15. A desk pet for ESP32 that approves Claude prompts over BLE — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/anthropics/claude-desktop-buddy)

**Source:** https://www.opensourceprojects.dev/post/388a41a1-2522-42c3-8e28-a1f98b4d25b3
**Karakeep doc:** `uwnt03t4zml8ssikju3e0a1a`

Anthropic's `claude-desktop-buddy` — an ESP32 (M5StickC Plus) desk pet that connects to Claude over BLE and lets you approve/deny prompts from physical buttons. It gets visibly impatient when an approval is pending. They open-sourced the wire protocol too, so you can build your own hardware. 18 ASCII pets, GIF character packs, shake-to-dizzy. Delightful and genuinely useful if you live in Claude Code.

---

## 16. NPMplus: a hardened nginx-proxy-manager fork with HTTP/3, crowdsec, and OIDC — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/zoeyvid/npmplus)

**Source:** https://www.opensourceprojects.dev/post/771a0a5e-d4ab-4c9c-92c6-f8397a0e5ba5
**Karakeep doc:** `tyl3v4hy5kafraaczk1dfvqz`

A drop-in nginx-proxy-manager fork that actually cares about security: HTTP/3 (QUIC) out of the box, patched nginx with aws-lc, crowdsec/appsec, OIDC login, automatic OWASP security headers, short-lived Let's Encrypt certs. Alpine-based, smaller image. Caveat: AGPL-3.0 (not MIT like upstream), and some certbot DNS plugins were dropped.

---

## 17. Unlock GitHub's hidden badges with this multilingual achievement guide — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/4xmen/get-github-achievements)

**Source:** https://www.opensourceprojects.dev/post/cccc8d21-14fc-4280-9ca9-8cfaadea4243
**Karakeep doc:** `tgu47ag0vtipuh7bxyf8f3n2`

`get-github-achievements` — a community reference for every GitHub badge, from Pull Shark to Galaxy Brainster, with the exact (often undocumented) requirements and edge cases. Translated into 16+ languages. If you've ever wondered how someone got that one weird badge, this is the answer key.

---

## 18. WeChatFerry: a Windows WeChat tool with Python, HTTP, NodeJS clients — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/lich0821/wechatferry)

**Source:** https://www.opensourceprojects.dev/post/6876e054-4bc9-42f2-afa0-7f5b94d09acd
**Karakeep doc:** `t5u0ngl60vcvus6vhwalrwrr`

An SDK for automating the Windows WeChat client — hooks the desktop app via a native DLL, exposes messaging, contacts, group management, and direct SQL access to the local WeChat database. gRPC core with Python/HTTP/NodeJS/Java/C#/Rust clients. Operates in WeChat's unofficial gray area, so read the disclaimer.

---

## 19. rqbit: a Rust bittorrent client with streaming, UPnP, and a Web UI — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/ikatson/rqbit)

**Source:** https://www.opensourceprojects.dev/post/35b32cad-a03e-4e19-b786-3b9c02c89a5d
**Karakeep doc:** `onxuq2nrzz6lavm5r2spoc04`

A Rust torrent client that's more Swiss Army knife than downloader: streams files *while* downloading (prioritizes the pieces you're watching), advertises torrents to your LAN via UPnP for smart TVs, mDNS discovery at `rqbit.local`, web UI, and a reusable `librqbit` crate. Sips a few tens of MB of RAM — Raspberry Pi friendly.

---

## 20. FaceFusion: the face manipulation platform with a job queue built in — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/facefusion/facefusion)

**Source:** https://www.opensourceprojects.dev/post/a3b1dc69-a9b8-4f7b-b90e-f579b0044647
**Karakeep doc:** `mud6xm0dj4pvil4npq8nvchw`

Face-swapping treated like a real engineering pipeline: a full job lifecycle (draft → add steps → submit → run → track), batch processing, `job-retry-all` for failed batches, headless mode for servers. OpenRAIL-AS license. The learning curve is real, but the job queue is a genuinely thoughtful design you don't see in most face-swap tools.

---

## 21. A practical SOC handbook covering detection, response, and the metrics that matter — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/cyb3rxp/awesome-soc)

**Source:** https://www.opensourceprojects.dev/post/4cb3d58f-3b12-4a9a-ae24-e1c5ac30d42f
**Karakeep doc:** `jr3wfhcgu4yjqwvbpip1x4p8`

`awesome-soc` — an opinionated, curated handbook for building/running a SOC, from a SOC/CSIRT analyst and manager. Motto: "without reaction (response), detection is useless." Covers detection engineering, threat intel, playbooks, metrics/KPIs, management, HR, and AI use cases. Leads with MITRE's "11 Strategies" and FIRST's "Building a SOC." A living doc with a link-checker.

---

## 22. A tiny C/C++ webview library that wraps GTK, WebKit, and WebView2 — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/webview/webview)

**Source:** https://www.opensourceprojects.dev/post/da83c114-e686-40a9-9da7-3dba19317cc8
**Karakeep doc:** `dojcl9cd5px8koclictxqoh8`

The `webview` library — write your UI once in HTML/CSS/JS, run it natively on all three platforms by wrapping the OS's *existing* web engine (WebKitGTK, WebKit, WebView2). No bundled Chromium, no 200MB binary. Two-way JS↔C/C++ binding. A few source files total. The anti-Electron for tools and utilities.

---

## 23. colord — manage, install and generate colour profiles — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2018/01/no_signal_tv_1.jpg)

**Source:** https://www.linuxlinks.com/colord-manage-install-generate-colour-profiles/
**Karakeep doc:** `qw2fy5nc6rfx3e6wczn68y9m`

The system daemon that maps devices to ICC colour profiles, via D-Bus, with an SQLite-backed mapping DB. Includes `colormgr` CLI, `cd-create-profile`/`cd-fix-profile`, Little CMS, and optional ArgyllCMS/SANE integration. GPLv2, C, by Richard Hughes. The quiet plumbing that keeps your colours consistent.

---

## 24. 🎬 Video — This Is the World's Largest Hacking Conference — by NetworkChuck

![NetworkChuck](https://i.ytimg.com/vi/RYY0ibk4s60/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=RYY0ibk4s60
**Karakeep doc:** `wwq4nxuwi6rkvgruq3wlgvok`

NetworkChuck's Defcon 34 vlog — 30,000 hackers in Vegas, the Wall of Sheep (a live scoreboard of people who connected to the conference WiFi insecurely), the Packet Hacking Village, and a Shark Jack demo. The practical bit: before you walk in, disable WiFi and Bluetooth — everything can be fake. Sponsored by Twingate, which he used to securely ship footage home. Ends with him praying for his audience, which is very on-brand for Chuck.

---

## 25. 🎬 Video — Apple Won the AI Race — by Better Stack

![Better Stack](https://i.ytimg.com/vi/Ba3xunEk8Y8/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=Ba3xunEk8Y8
**Karakeep doc:** `nzuglx45j3f5a5a1nwklc907`

The argument: no single company has *maintained* an AI lead — Anthropic, Google, OpenAI, xAI all leapfrog each other every few weeks. Apple's play is to not compete on models at all, but on everything else: 2.5B devices, on-device AFM models (distilled with Google's Gemini, not *run* on it), privacy, and ecosystem lock-in. The thesis is that a "good enough" model + deep integration + distribution wins. A solid counter-narrative to the "Apple is too late" take.

---

## 26. 🎬 Video — Linux Defaults Are Usually Fine — by Brodie Robertson

![Brodie Robertson](https://i.ytimg.com/vi/pfjC1LknLRo/sd2.jpg?sqp=-oaymwEoCIAFEOAD8quKqQMcGADwAQH4AbYIgAKAD4oCDAgAEAEYZSBNKEwwDw==&rs=AOn4CLBwu7zVD5A8DwvovnIHSVHUsmkzLQ)

**Source:** https://www.youtube.com/shorts/pfjC1LknLRo
**Karakeep doc:** `v4jg5wuqbu51l91ovbmal3ml`

A short, honest take: ricing your distro is fun when you're new, but eventually you hit "I have shit to do, this is fine." Most default settings are fine, and you can live without most of the tweaks. A nice antidote to the endless-config rabbit hole.

---

## 27. 10 Best Free and Open Source Text Expander Tools — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2023/01/20945581-automation.jpg)

**Source:** https://www.linuxlinks.com/best-free-open-source-text-expander-tools/
**Karakeep doc:** `zibde7wt3l2uy673cz7x1afh`

Text expanders that replace a keyword as you type. The list: espanso, Kanata, keymapper, Compress, CrossMacro, Snippet Expander, espansoGUI, Snipt, Texpander, Snippet Pixie. espanso (Rust, cross-platform) is the standout. The comments section is a fun little "I vibe-coded one" → "AI slop then" exchange.

---

## 28. Scran — Wayland screen capture utility — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/03/screen-capture-roundup-c.png)

**Source:** https://www.linuxlinks.com/scran-wayland-screen-capture-utility/
**Karakeep doc:** `q1bpujl0vkri9kfuu3ybnee2`

A Wayland screenshot + screen-recording tool with an interactive region selector, clipboard support, stdout piping, and PipeWire audio. Freeze the screen with Z to grab changing content, slurp-compatible geometry, Sway/Hyprland/COSMIC support. MIT, C, by Stephan.

---

## 29. Droidian — Debian-based Linux distribution for mobile devices — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/04/Linux-Distributions.png)

**Source:** https://www.linuxlinks.com/droidian-debian-based-linux-distribution-mobile-devices/
**Karakeep doc:** `o441xygijcmbt4vmpl4qfyr1`

Debian on phones that originally shipped with Android, using Halium + libhybris to bridge GNU/Linux with Android's hardware layers. Phosh (Wayland) as the mobile shell, APT package management, fastboot/recovery-flashable images, full-disk encryption. Builds on Mobian. For Wojtek's postmarketOS experiments, this is the Debian-flavoured cousin.

---

## 30. 🎬 Video — The Linux Kernel Will Never Be The Same — by Brodie Robertson

![Brodie Robertson](https://i.ytimg.com/vi/i_4re683Nj4/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=i_4re683Nj4
**Karakeep doc:** `u0l7wu68vy454nvyzck59g5q`

The big one. A Greg Kroah-Hartman graph shows CVEs-per-release *tripling* at the 6.19 release (Feb 2026) — Brodie calls it an inflection point for the kernel and the whole industry. The cause: AI security tooling got good enough that people who actually know what they're doing can now use it to find real bugs, flooding maintainers (networking is burning out) and getting 30-year-old drivers pulled. The second half is a deep dive on AI crawlers hammering git.kernel.org — 98% of traffic is scrapers, 1.2 *quadrillion* valid URLs from a single fork, and Anubis proof-of-work as the losing defense. Worth the full watch.

---

## 31. 6 Best Free and Open Source GUI Bookmark Managers — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/04/047-bookmark.png)

**Source:** https://www.linuxlinks.com/best-free-open-source-gui-bookmark-managers/
**Karakeep doc:** `vlbdhsy1yiunngar19u7il7l`

The GUI side of the bookmark-manager roundup (Pocket's shutdown is the trigger). The six: KEditBookmarks, Cosmicding, RabbitMark, Frigoligo, Sitemarker, Marca. Frigoligo (Wallabag client) and Cosmicding (linkding client) are the two that plug into self-hosted backends.

---

## 32. justray — modern VPN client for the terminal — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/09/035-network.png)

**Source:** https://www.linuxlinks.com/justray-modern-vpn-client-terminal/
**Karakeep doc:** `vj0hliidd3r2cg1aaw2qfexz`

A terminal VPN client built on sing-box, with a keyboard-driven TUI and a background daemon. Supports VMess, VLESS, Trojan, Shadowsocks, Hysteria, TUIC, AnyTLS, SOCKS5, WireGuard. Imports subscriptions from raw links and Clash/Mihomo YAML. TUN and proxy modes, node testing, DNS over HTTPS. GPLv3, Go, by luynar.

---

## 33. 🎬 Video — Ok I'm a little worried now — by Less Bitter

![Less Bitter](https://i.ytimg.com/vi/tELhwwnW2dE/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=tELhwwnW2dE
**Karakeep doc:** `e102k6bk0wb28yb9f09014jf`

Less Bitter tests Meta's new Muse Spark 1.3 model and comes away genuinely unsettled — it's *better than he expected*. The pricing is the hook: the "big brother edition" (which trains on your input) is $0.10/M input, $0.20/M output — 5x cheaper than Opus. His verdict isn't "Meta is coming up," it's "AI training has become a commodity" — anyone with $40M (like Reuters, who just launched a frontier model) can do it now. The video is him building apps with it and being repeatedly surprised.

---

## 34. phpList — email marketing manager — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2021/05/email-text-keyboard-button.jpg)

**Source:** https://www.linuxlinks.com/phplist-email-marketing-manager/
**Karakeep doc:** `urb9al1h8rkv4tbn3cykps8k`

A self-hosted email marketing manager — newsletters, subscriber segmentation, personalisation, bounce processing, scheduling, Amazon SES support, RSS-to-email. Web UI + CLI, plugin architecture, multiple APIs. AGPLv3, PHP. The self-hosted alternative to Mailchimp.

---

## 35. 🎬 Video — This AI Chip Is 48x Faster… But There's a Catch — by Better Stack

![Better Stack](https://i.ytimg.com/vi/zdpG19wI4Q8/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/zdpG19wI4Q8
**Karakeep doc:** `nkr3rne4lyq4f7ehazh7mj2m`

AMD bought a startup (Pallas) that makes AI chips with the model weights *etched into the silicon* — not stored in memory. That's where the 48x-NVIDIA-B200 speed claim comes from (~17k tokens/sec). The catch: you can't update the model without manufacturing new silicon (~$1.5M per mask set), and the model they welded in (Grok) was deprecated the same month AMD bought the company. A chip with a dead model etched in could go straight to zero value. Fascinating bet.

---

## 36. Speech Note — note taking, reading and translating — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/02/voice-recognition.jpg)

**Source:** https://www.linuxlinks.com/speech-note-note-taking-reading-translating/
**Karakeep doc:** `e2c1s52umcsm8lg41s1bl5rr`

A Linux desktop app for speech-to-text, text-to-speech, and machine translation — all *local*. Pluggable engines: whisper.cpp, Faster Whisper, Vosk, Coqui STT for recognition; eSpeak NG, Piper, RHVoice, Kokoro, F5-TTS for synthesis; Bergamot for translation. Models downloaded separately via a browser. MPL-2.0, C++, by Michal Kosciesza. The privacy-first alternative to cloud transcription.
