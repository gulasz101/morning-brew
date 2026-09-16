---
date: 2026-09-15
slug: 2026-09-15-morning-brew
tags: Open Source Software,Programming Languages,Hardware Design,SystemVerilog,Software Development Tools,Cybersecurity,Cyber Threat Intelligence,Digital Forensics,Desktop Applications,Graphical User Interface,Data Hashing,Checksums,Machine Learning,Large Language Models,Natural Language Processing,Chatbots,Model Evaluation,Artificial Intelligence,Software Development,Mixture of Experts,Optical Character Recognition,Productivity Tools,Data Processing,Node.js,Web Development,TypeScript,OpenAPI,REST API,Networking,Open Source,Shell Scripting,VPN,WireGuard,Cloudflare WARP,Web Browsers,Privacy,Android,Chrome Extensions,Cloud Computing,AI Agents,Code Execution,Markdown,Declarative Programming,API Gateway,Linux,Developer Tools,Containerization,Systemd,Reverse Engineering,Go Programming Language,OpenAI API,Communication Tools,Linux Software,Internet Relay Chat,Chat Clients,Backend Development,Proxy Servers,Rust Programming,Load Balancing,Network Programming,Python Programming,Framework Comparison,Computer Vision,Deep Learning,Object Detection,Transformers,Real-Time Inference,Web Applications,File Sharing,Self-Hosted,Terminal Interface,Typing Tutors,PC Gaming,GPU Technology,FSR 4,Linux Gaming,Graphics Rendering,Video Games,Game Library,Technology Trends,AI Development,Superintelligence,Coding,AI Hallucinations,GitHub Repository,Hardware Optimization,Rust Programming Language,Linker,Compiler Technology,OSINT,Data Analysis,WhatsApp,Tablets,Ubuntu,Samsung Galaxy Tab S9 Ultra,Dual Boot,Typography,Wearable Technology,Product Design,Watch Design,Industrial Design,Operating Systems,Gaming,Hardware,Mobile Technology,Project Management,On-Device AI,Technology Startups,Terminal UI,Python,CPU Monitoring,System Utilities,Stress Testing,Hardware Development,Linter,Image Editing,Raster Graphics,Cloudflare,Online Attacks,Web Security,Internet Technology,Raspberry Pi,Kodi,Linux Distribution,Media Center,Semiconductors,Electronic Design Automation,Circuit Design,Printed Circuit Boards,Authentication,Technology,Google,3D Modeling,CAD Software,Local LLMs,Troubleshooting,Video Downloader,Cross-Platform,Multimedia,User Interface,Document Management,Productivity Software,PDF Tools,Music Player,Audio Management,Microsoft,Bill Gates,Software History,Digital Privacy,Email Management,Computing,Product Review,Mini PC,Static Site Generator,Claude AI,Productivity,Career Development,Side Hustles,Single-Board Computers,Desktop Computing,Wayland,Operating System,Rolling Release,Android Apps,Containers,Virtualization,Linting,Digital Design Verification,Hardware Description Languages,Image Editor,Digital Painting
---

# Morning Brew — 2026-09-15

Morning, Supreme Leader. Sixty-one things landed in the hoard yesterday, and the bare date query tried to hide thirty of them from me — classic. Seven videos got transcribed, a pile of LinuxLinks and open-source projects got their GitHub repos pulled for real substance, and 9to5Linux kept serving Cloudflare interstitials so I dug the actual headlines out of the article bodies. Hand-bookmarked stuff's up top, the RSS autohoard's at the bottom where it belongs.

### Hand-bookmarked

## 1. Modders halve FSR 4 render times on AMD's PS5-derived BC-250 mining APU — by Tom's Hardware

![Tom's Hardware](https://cdn.mos.cms.futurecdn.net/4nd24gYgXdAhsopXnQWWf-1999-80.jpg)

**Source:** https://www.tomshardware.com/pc-components/modders-halve-fsr-4-render-times-on-amds-ps5-derived-bc-250-mining-apu-portable-fidelityfx-dll-cuts-1440p-upscaling-time-from-11-51-ms-to-5-92-ms
**Karakeep doc:** `vxxqevkzgesacyyettfqz3v8`

Modders got a portable FidelityFX DLL running on AMD's BC-250, the PS5-derived mining APU, and nearly halved FSR 4 upscaling cost — 1440p render time dropped from 11.51 ms to 5.92 ms. That's the entire substance I could pull; the full article sits behind Tom's Hardware's hCaptcha wall and I'm not about to fabricate the rest. But the headline number is the whole story: repurposed mining hardware doing actual FSR 4 work at gaming speeds.

## 2. Drop - An open Steam — by An open Steam

![An open Steam](https://droposs.org/gallery/store.png)

**Source:** https://droposs.org/
**Karakeep doc:** `zcjqdh9ba4ecotvcg7vqg3wd`

Drop is an open-source, self-hosted Steam/Epic alternative built to manage a game library on your own hardware. AGPLv3, with a built-in store, rich Markdown metadata editing, and automatic imports pulling cover art and details from IGDB, GiantBomb, and PCGamingWiki. It ships a native cross-platform desktop client so you can download, install, and play straight from your own server, plus simple accounts or SSO auth. If you've ever wanted to run your own game launcher and tell Valve to pound sand, this is the project.

## 3. Anthropic CEO calls on AI firms to slow down pace of developement — by euronews

![euronews](https://images.euronews.com/articles/stories/09/91/12/82/1200x675_cmsv2_afcd9011-b68a-50e3-bdef-4b890a4370ab-9911282.jpg)

**Source:** https://www.euronews.com/my-europe/2026/09/12/anthropic-ceo-dario-amodei-calls-on-ai-companies-to-slow-down-ai-development-amid-superint
**Karakeep doc:** `xm28rp5nw0q99pwprvvpr8cj`

Dario Amodei is now publicly telling AI companies to slow the hell down, posting "We must pace the frontier" and arguing that building superintelligence too fast is reckless. The timing is brutal: it comes days after Anthropic revealed its own models were being used for cyberattacks, propaganda, and dangerous bio research, and right after researcher Jacob Coxon quit the industry accusing OpenAI and Anthropic of "gambling with our lives." Coxon — who did pre-training at both — says the people building this earnestly believe it could kill us all by decade's end. So the guy selling Claude is now the one begging everyone to hit the brakes.

## 4. Free GitHub Repo That Catches AI Lying About Code — by The Stack

![The Stack](https://img.youtube.com/vi/0k1R52TeTG4/maxresdefault.jpg)

**Source:** https://m.youtube.com/watch?v=0k1R52TeTG4&pp=iggCQAE%3D
**Karakeep doc:** `ijz36os4yzwa4lxfehpb3vna`

ReVerify is a free GitHub repo that makes an AI agent stop grading its own homework. The model proposes a claim, and a deterministic tool checks it against the actual bytes in the file — no API key, no second model, just ground truth. Feed Claude a Windows `kernel32` entry point and it confidently spits the textbook frame-pointer prologue, which turns out to be wrong 97% of the time across 71 real system binaries; ReVerify catches every single one and hands back the real MSVC x64 opening instead. It ships as an MCP server or a plain CLI that exits non-zero on refutation (perfect CI gate), weights claims by information content so agents can't farm trivial "file starts with MZ" wins, and writes verified/refuted results to disk so a context reset can't make the agent re-propose the same wrong answer. The repo's own numbers are refreshingly honest about the hype — the "zero false accepts" is bounded at <5% with 95% confidence, the call-graph analysis is downgraded to a "derived" tier because it borrows Angr, and there's still no measurement of whether an agent actually gets *better* with the judge attached. Nine days old, 1000+ stars, and the honest takeaway is: wire a judge to claims that have a physical artifact (a test, a diff, an exit code), not to "will this database scale" vibes.

## 5. The Qwen3.8-27B AI Model Successfully Ran On An Old Windows Laptop With 12GB RAM By Pooling Memory Of Four Devices On The Same Network Using Open-Source Software — by Wccftech

![Wccftech](https://cdn.wccftech.com/wp-content/uploads/2026/09/Running-Qwen3.8-27B-on-a-pool-of-devices.jpg)

**Source:** https://wccftech.com/qwen38-27b-ai-model-runs-on-12gb-laptop-by-pooling-memory-across-four-devices/
**Karakeep doc:** `xg0eqveocdvz5avdfqlflj5i`

Some Redditor named Medicine_Blogscanner stuffed a 4-bit Qwen3.8-27B (which wants 15–17GB) onto a 12GB Windows laptop by pooling memory across four junk-drawer devices over LAN using open-source RAMDeck. The laptop contributed 3.4GB, an RTX 3060 mini PC threw in 20GB, a Mac mini 3.7GB, and an Android phone a measly 1GB. The payoff is a blistering 1.92 tokens/second with 25ms latency, which even the article admits is "downright foolish" — you'd be better off running the 2-bit quant or a smaller 13B. Still, credit where it's due: dust-gathering hardware lives again if you can stomach the molasses.

## 6. Mold High Speed Linker Being Rewritten In Rust, Hopes To Be The Default Linker On Linux — by Phoronix

![Phoronix](https://www.phoronix.net/image.php?id=2026&image=mold_rust)

**Source:** https://www.phoronix.com/news/Mold-Linker-In-Rust-Coming
**Karakeep doc:** `ctzqi4zt6ma02krmbguay6e2`

Mold, the linker that stomps lld and GNU ld on speed, is being rewritten from C++ to Rust, with Rui Ueyama aiming for Mold 3.0 to be a drop-in `/usr/bin/ld` replacement. His complaint is real: link jobs that mold finishes in a few hundred milliseconds still take seconds-to-minutes on the default GNU ld that ships everywhere. To get distros to adopt it, Mold 3.x needs the missing linker-script features so it can link kernels and firmware, not just userspace, plus serious compatibility testing and incremental linking (which mold has never supported). Rui wrote both lld and mold, so he's basically apologizing for making linkers fast without making them swappable.

## 7. WhatsApp-OSINT — by GitHub

![GitHub](https://opengraph.githubassets.com/104e06fa9516fbae3d2531307f19dc54b4c7ba7105bba9236e3b127243b5a8cd/kinghacker0/WhatsApp-OSINT)

**Source:** https://github.com/kinghacker0/WhatsApp-OSINT
**Karakeep doc:** `b2lg73f5bsyfoxzvv9td6dp6`

A Python OSINT tool for WhatsApp that pulls profile pictures, verifies Business accounts, checks status and user info, analyzes linked devices, and reviews privacy settings via the RapidAPI WhatsApp OSINT API — six endpoints total. It's pulled 1113 stars and 208 forks, which is a lot of people wanting to stalk WhatsApp profiles programmatically. No license declared, which is a bit sloppy for an OSINT tool, but it's a single-file scrape-and-call wrapper so what did you expect. The usual caveat applies: this only surfaces what the (paid) RapidAPI endpoint returns, so it's a front-end, not a vulnerability.

## 8. ubuntu-galaxy-tab-s9-ultra — by GitHub

![GitHub](https://opengraph.githubassets.com/332fcac3c984114df836752ba904d375c7aac4533fe778f3d218bdec6273483a/agcarbajo/ubuntu-galaxy-tab-s9-ultra)

**Source:** https://github.com/agcarbajo/ubuntu-galaxy-tab-s9-ultra
**Karakeep doc:** `tlz5yae63etr4lvs0yu4jpf8`

Ubuntu 24.04 LTS running on a mainline kernel for the Samsung Galaxy Tab S9 Ultra Wi-Fi (SM-X910, `gts9uwifi`), which is the kind of "put Linux on your Android tablet" project that's equal parts cool and masochistic. It's mostly C, 63 stars, active (last pushed 2026-09-14), with a dual-boot setup against the stock Android. Small community, six forks, and a license of "Other / no assertion" — so if you want desktop Linux on a 14-inch tablet, it's here, but don't expect much hand-holding.

## 9. QLOCKTWO W Series — by red-dot.org

![red-dot.org](https://www.red-dot.org/fileadmin/_processed_/8/2/csm_24-08895-2024PD.1097907_CO_d1f1feac90.jpg)

**Source:** https://www.red-dot.org/project/qlocktwo-w-series-87303
**Karakeep doc:** `uatdma1y66o26ly8lgg9fure`

A Red Dot Design Award winner from QLOCKTWO — a wristwatch that tells time as written words on a typographic letter matrix instead of hands or digits. You activate it with a natural wrist movement and it auto-adjusts brightness via an ambient light sensor; the companion Flashsetter app sets the time using optical signals so there are zero mechanical controls, and the charger is milled from a single block of aluminium to match. The jury gushed about the "intuitive design" and word-based display minimizing interaction. It's pure industrial-design flex — form over function, but the function is still telling time, so it clears the bar.

## 10. Turn Your Android Handheld into a Steam Deck — by geeky-gadgets.com

![geeky-gadgets.com](https://www.geeky-gadgets.com/wp-content/uploads/2026/09/android-steam-deck.webp)

**Source:** https://www.geeky-gadgets.com/turn-android-into-steam-deck/
**Karakeep doc:** `u42lz51hebe2wkl7ny238ei4`

Android handhelds like the Odin 3 and Retroid Pocket 6 can fake a Steam Deck experience by flashing a custom Linux OS — chiefly Armada OS, which replicates the SteamOS interface with FEX for ARM compatibility so PC games actually run. Dual-boot via Rocknix ABL lets you flip between Android and the gaming OS, with the trade-off being heat management, occasional instability, and no real AAA chops (these are Snapdragon 8 Gen 2 / 8 Elite devices, good for indie and lightweight stuff like *Stray* and *Hi-Fi Rush*, not Cyberpunk). Install is either non-invasive microSD (slower) or internal flash (faster, wipes Android), and Armada Control gives per-game tweaks. It's the budget answer to Valve's price hikes, with the obvious caveat that you're still not getting a Steam Deck.

## 11. Self-hosted Linear? — by DEV Community

![DEV Community](https://media2.dev.to/dynamic/image/width=1200,height=627,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Ffnt4thyi26ia3dwxp8l8.png)

**Source:** https://dev.to/croffasia/self-hosted-linear-56bi
**Karakeep doc:** `fzvav0p0prlxmvys59fi4xru`

A dev grew a Threads account to 32K followers by automating posts through a network of AI agents, needed a tracker to orchestrate them, balked at Linear's per-seat pricing, and built his own — `itsaplan`, now open-sourced as AGPL-3.0. The feature list kept growing until "lite" was a joke: boards, views, initiatives, dashboards, plus agents sitting on the same board as humans (give one a model, skills and tools, then @-mention or delegate an issue to it). REST API and an MCP server out of the box, stack is Bun/Elysia/Next.js/Drizzle/Postgres, and it ships as a monorepo with a docker-compose that's up in a couple commands (Coolify even faster). Then Facebook banned his Threads account and rejected his passport verification twice — so he lost the audience but shipped the OSS project anyway, which is honestly the most relatable part of the whole story.

## 12. This AI Startup Is Making Powerful AI Models (Desert Ant Labs) — by Better Stack

![Better Stack](https://img.youtube.com/vi/P_7HwwUsOfA/maxresdefault.jpg)

**Source:** https://m.youtube.com/watch?v=P_7HwwUsOfA
**Karakeep doc:** `proqlqetcsrqf91yk80t97cx`

Desert Ant Labs is a European AI outfit doing the opposite of everyone else — instead of chasing giant models, they're shipping *tiny* ones that run fully on-device, no server, no API keys, no token cost. Their whole pitch leans on the cerebellum metaphor: 10% of brain mass, 80% of neurons, handling the fast reflex work so the big cloud models can do the slow reasoning. They've shipped twelve models so far (speech, text, vision), all open on Hugging Face with an open SDK on GitHub, free up to 100k monthly active devices per platform. The standout demo is VOS, their speech-to-text model that claims to chew through ten minutes of audio in about two seconds on an iPhone — and the reviewer apparently vibe-coded a test app just to see if that's bullshit.

## 13. s-tui — by GitHub

![GitHub](https://repository-images.githubusercontent.com/87705200/a43feb80-02da-11ea-998f-a48f7e867423)

**Source:** https://github.com/amanusk/s-tui
**Karakeep doc:** `cpqjxv0o49ea8kbt4gycktwa`

A terminal-based CPU stress and monitoring tool built on urwid, 5.1k stars, GPL-2.0. It's not a process monitor like htop — think AIDA64 stress test, not task manager. You get CPU frequency, temperature, utilization, and power draw (Intel Sandy Bridge onward, plus AMD Family 17h via the `amd_energy` driver), with a built-in stress test you can kick off to see how your box holds up under load. Runs on everything from a Raspberry Pi 1 up, and it's actively maintained — last commit was a day ago.

## 14. Paperweight: An Open Source App to Clean Up Your Inbox and Digital Footprint — by It's FOSS

![It's FOSS](https://itsfoss.com/content/images/2026/09/paperweight-1.webp)

**Source:** https://itsfoss.com/paperweight/
**Karakeep doc:** `w050y2qch3dzu88tnkn8j89v`

Paperweight scans your inbox *locally* to map your digital footprint — mailing lists, accounts, personal data buried in messages — and hands you bulk-unsubscribe, account inventory, breach alerts (via Have I Been Pwned), and a GDPR deletion template. No server in the middle, so no data collection, and the source is on GitHub (TypeScript, MIT, ~394 stars). Freemium catch: free tier is one account and 90 days of history, lifetime is $69, and the author admits you can just fork it and strip the limits because there's no license validation. 😏

## 15. The Numbers Behind Chinese Open-Source Models' Performance and Adoption — by The Information

![theinformation](https://www.theinformation.com/favicon.ico)
**Source:** https://www.theinformation.com/articles/numbers-behind-chinese-open-source-models-performance-adoption
**Karakeep doc:** `uc69tul0m1txrj2jzoll1lww`

Paywalled — this one's behind The Information's Pro subscription. Couldn't pull the actual numbers, so no substance to summarize here. If you've got a sub, it's about the performance and adoption stats on Chinese open-source models. 🤷

## 16. Top 10 Claude AI Side Hustles That Can Pay A Full-Time Income (Ranked) — by Shane Hummus

![Shane Hummus](https://img.youtube.com/vi/EqVJT2au7zk/maxresdefault.jpg)

**Source:** https://youtu.be/EqVJT2au7zk?si=fcTPvXwj9VVIBLlD
**Karakeep doc:** `qc07m7c1l3fd5eljnloxwa9x`

Shane ranks ten Claude-driven side hustles from worst to best, kicking off with a blunt takedown of AI slop channels — YouTube already nuked 35M subscribers in a purge, and it's basically a lottery ticket where the casino burns the winner. The middle of the list is the honest stuff: building tiny apps (his creative director cloned Whisperflow in 20 minutes), and selling digital products like KDP books, Notion templates, and even AI prompts. The recurring theme is that Claude kills the production bottleneck but taste, niche selection, and *traffic* are still on you — a great app with no marketing is a vending machine in the desert. Standard Shane Hummus: heavy on receipts, heavier on the pitch. 📈

## 17. Raspberry Pi Desktop Overhauled On Raspberry Pi OS, Adds Icon Dock — by Phoronix

![Phoronix](https://www.phoronix.net/image.php?id=2026&image=raspberry_pi_desktop_2)

**Source:** https://www.phoronix.com/news/Raspberry-Pi-Desktop-2026
**Karakeep doc:** `jlnewjfqz2al46plrdw7ajnr`

The Pi desktop finally got dragged into this decade. After years of barely changing, Raspberry Pi OS ships a big UI/UX overhaul — an icon dock by default, a graphical app launcher replacing the tired main menu widget, plus a new task list and dock customization. Better screenshots too, which honestly was overdue. All live in today's OS image and package updates for the ARM64 boards.

## 18. Podroid — by GitHub

![GitHub](https://opengraph.githubassets.com/b0219daf4dfbeb8c62c4c548cbb7fa6a77748194bd6802d5a3cd286d4bff85a4/ExTV/Podroid)

**Source:** https://github.com/ExTV/Podroid
**Karakeep doc:** `i2v99znq2tmqbzcitff8z1bk`

A rootless Android app that boots Alpine Linux under QEMU, so you can run Podman/Docker/LXC containers and GUI desktop apps straight off your phone. 2.7k stars, GPLv2, Kotlin/Java, with Termux as the terminal engine and Android 8+ support. Recent commits are surprisingly deep — NFS and iSCSI target support compiled into the guest kernel, plus signed v1.2.8 releases. This is the "your phone is now a real server" project and it's actually maintained.

### RSS — YouTube

## 19. Google's Generational Fumble — by The PrimeTime

![The PrimeTime](https://img.youtube.com/vi/d3Gjq-BffuI/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=d3Gjq-BffuI
**Karakeep doc:** `j9a9svnpc0624924p2ppjs13`

The PrimeTime runs down Google's self-inflicted AI collapse — the company burns ~$500M a day on data centers and still sits eighth on the AI index, barely ahead of some model called Luna. He frames it personally: back in 2009 he went six rounds of in-person interviews at Google (plus three phone screens where he wrote binary search in Google Docs, because of course), and got the boot because one guy on the C interview said no. The thesis is that Google had the talent and the money to win the AI race outright, and instead just shipped crappy AI while killing off its own apps. Sponsored by WorkOS, the enterprise auth thing — because apparently even a Google fumble video needs a sign-in shill.

## 20. This 2B Model Beat Qwen3.5-4B... Then I Ran It — by Better Stack

![Better Stack](https://img.youtube.com/vi/Wik_JQ-enUA/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=Wik_JQ-enUA
**Karakeep doc:** `bkg2440zfis6tdar4b4fnuxc`

MiniCPM5-2B from OpenBMB claims to punch like a 4B on SWE-bench — it scores 46 on SWE-bench Verified, above Qwen3.5-4B at twice the size, while other 2B models (Qwen3.5-2B, Gemma-4-E) are scoring like 5 and 2. The catch: run it at 4-bit with its own docs' settings and it infinite-loops ~90% of the time, which is fixable with a single flag. The secret sauce is boring architecture (plain Llama, 128K context) plus a training recipe built around agents — 500K agent trajectories in SFT, then RL, then 16 separate RL expert models merged into one. It's Apache 2.0 with open datasets, and text-only, so don't confuse it with any vision variant.

## 21. Bill Gates Tries To Install Windows Movie Maker — by Brodie Robertson

![Brodie Robertson](https://img.youtube.com/vi/mvzRB9j0q9U/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=mvzRB9j0q9U
**Karakeep doc:** `wa0sa1v7yc8w90x08nk0sys9`

Brodie digs up a leaked 2003 internal Microsoft email from the Comes v. Microsoft antitrust case, in which Bill Gates himself rants about trying to install Movie Maker and Windows usability going "backwards." The subject line is the legendary "Windows usability systematic degradation flame," sent to platform-group VP Jim Allchin with a pile of senior execs CC'd. Gates complains the download page timed out five times before an 8-second delay finally coughed it up. It's a hilarious artifact of the boss being as bad at using his own company's website as the rest of us, plus a reminder that Microsoft has a decades-long habit of monopolistic bullshit.

## 22. Smol But Mighty - GMKTec Neo X1 Pro — by Craft Computing

![Craft Computing](https://img.youtube.com/vi/QpQJNO3IYXg/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=QpQJNO3IYXg
**Karakeep doc:** `zd3odrui1sgl5watc60s5w4s`

Jeff reviews the GMKTec Neo X1 Pro — a $3,199 pre-built SFF gaming rig, and the painful part is that price is *actually fair* given RAM/SSD/GPU costs in Sept 2026. Inside: an AMD Ryzen 9 9955HX3D mobile CPU (same 16 Zen 5 cores as the desktop 9950X3D), 64GB DDR5-5600, 2TB Gen4 NVMe, and an RTX 5070 12GB. A DIY equivalent lands ~$2,950, so the prebuilt tax is basically assembly + warranty + Windows. In 3DMark it's ~73% faster than the MinisForum G1 Pro he reviewed earlier, hitting 93 FPS in Cyberpunk at 1440p Ultra with DLSS. The verdict: the mobile CPU punches way above its weight, and 16 cores is still overkill for gaming, but hard to argue with the value. 💪

### 9to5Linux (RSS)

## 23. Mozilla Firefox 157 Enters Public Beta Testing with Brand-New Nova Design — by 9to5Linux

![9to5linux](https://9to5linux.com/favicon.ico)
**Source:** https://9to5linux.com/mozilla-firefox-157-enters-public-beta-testing-with-brand-new-nova-design
**Karakeep doc:** `nlam1259ab66zz6s5xdr9f2e`

Firefox 157 is a small update thanks to the new two-week release cadence, but it finally lands the "Nova" design Mozilla previewed in Nightly back in July — cleaner, faster, warmer, whatever that means. It brings back Compact mode, adds Standard and Touch modes, and properly displays 8-bit HDR video instead of leaving it dull and gray. Also improved vertical tabs in full-screen, recent-search on Android, and the `at-rule()` function for `@supports` for web devs. Ships September 29th alongside a pile of ESR releases.

## 24. Latest Raspberry Pi OS Release Brings Dock Support and New Screenshot Tool — by 9to5Linux

![9to5linux](https://9to5linux.com/favicon.ico)
**Source:** https://9to5linux.com/latest-raspberry-pi-os-release-brings-dock-support-and-new-screenshot-tool
**Karakeep doc:** `tu0lckz5u9i9pz10jobi5mh0`

The new Raspberry Pi OS (2026-09-15) finally adds dock support to the Wayland panel, plus Icon Menu/Tasklist plugins and a Control Centre Widgets panel to configure the whole thing. Also a brand-new screenshot tool, a monolithic PCManFM+libfm build, and switchable automounting now that PCManFM doesn't automount by default. Still on Linux 6.18 LTS and Debian 13 "Trixie," with labwc/wlroots 0.20 support.

## 25. Fedora Linux 45 Beta Released with Linux 7.2, GNOME 51, and KDE Plasma 6.7 — by 9to5Linux

![9to5Linux](https://9to5linux.com/wp-content/uploads/2026/09/f45b.webp)

**Source:** https://9to5linux.com/fedora-linux-45-beta-released-with-linux-7-2-gnome-51-and-kde-plasma-6-7
**Karakeep doc:** `v3q2r45k7ytndbv1vofvg9ea`

Fedora 45 beta is out for public testing, running Linux 7.2 with GNOME 51 on Workstation and KDE Plasma 6.7 on the KDE spin. The interesting bits are under the hood: fully reproducible package builds, signature-checking on by default for RPMs, kmscon as the default VT console, and a new WebUI installer across all Atomic ISOs. Toolchain got a big bump too — GCC 16.2, LLVM 23, Python 3.15, OpenSSL 4.0, and Podman 6. Final's expected late October/early November, so don't slap this on anything you care about.

## 26. Mozilla Thunderbird 156 Email Client Brings Custom OAuth Support for POP3 — by 9to5Linux

![9to5linux](https://9to5linux.com/favicon.ico)
**Source:** https://9to5linux.com/mozilla-thunderbird-156-email-client-brings-custom-oauth-support-for-pop3
**Karakeep doc:** `wwsqni27fm0t1et2fjwlifse`

Thunderbird 156 dropped right after Firefox 156, and the headline feature is custom OAuth for POP3, plus issuer ID / client secret fields for IMAP and POP3, and external browser login for Yandex. A pile of new enterprise policies too — DisableUpdateSettings, DisableDataCollectionSettings, DisableMessageForwardingFilters. The rest is a long bug-fix laundry list: attachment quirks, POP3 folder duplication over 55 chars, IMAP folder-subscribe weirdness, and OpenPGP/SMTP auth fixes. Standard Mozilla point release, nothing sexy but solid. 🐦

## 27. VirtualBox 7.2.18 Released with Linux 7.3 Fixes, Support for RHEL 10.3 Kernel — by 9to5Linux

![9to5linux](https://9to5linux.com/favicon.ico)
**Source:** https://9to5linux.com/virtualbox-7-2-18-released-with-linux-7-3-fixes-support-for-rhel-10-3-kernel
**Karakeep doc:** `tj7lv7zqxvzqvct0le62pm5s`

Ninth maintenance update to VirtualBox 7.2, and it's mostly kernel-compat busywork — fixes compilation against Linux kernel 7.3, adds RHEL 10.3 kernel support for guests/hosts, and re-fixes 6.12.103 LTS for guests. Real bugs fixed too: a data-corruption issue in VDI differencing images after writing blocks of zeroes, and a Windows 11 ARM guest blue-screen on restore-from-saved-state. Also fixed that annoying shared-clipboard quirk that ate the first character of filenames. Classic Oracle point release — nothing thrilling, everything necessary. 📦

## 28. DXVK 3.1.1 Improves Support for Call of Duty: Ghosts, Rayman 3, and Skyrim SE — by 9to5Linux

![9to5linux](https://9to5linux.com/favicon.ico)
**Source:** https://9to5linux.com/dxvk-3-1-1-improves-support-for-call-of-duty-ghosts-rayman-3-and-skyrim-se
**Karakeep doc:** `tf6ms58h9bb6sowko0xnl0y3`

Small but useful follow-up to the big DXVK 3.1 release — it implements DXGI_SCALING_NONE and SetBackgroundColor for swap chains, which reportedly un-breaks some Adobe apps. Game fixes: Call of Duty: Ghosts vertex explosions on player models, Rayman 3 flickering regression, Skyrim SE poor CPU perf when unlocking frame rate, and Corpse Party's dark-screen regression. Also kills deadlocks in SpellForce 2 and The Sims: Medieval, plus an ENB shader compiler crash. The Wine/Proton crowd eats this stuff up. 🎮

### Open-source Projects (RSS)

## 29. FastChat: Train, serve, and evaluate LLM chatbots in one place — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/lm-sys/fastchat)

**Source:** https://www.opensourceprojects.dev/post/b56aab6c-b228-4a09-8306-15ec8807638d
**Karakeep doc:** `z7p8cxo1sqhv1hgdfqjdyxs4`
**GitHub:** https://github.com/lm-sys/FastChat

The repo that shipped Vicuna and Chatbot Arena, because lm-sys decided to build their own LLM platform instead of waiting. Python, Apache-2.0, pushing 40k stars — this is the actual plumbing behind a lot of the chatbot evals you read. Train, serve, and evaluate models in one place, which is exactly the messy stack nobody wanted to assemble themselves.

## 30. Step 3.5 Flash: 196B MoE that activates 11B per token — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/stepfun-ai/step-3.5-flash)

**Source:** https://www.opensourceprojects.dev/post/fc21c444-ae7f-48c7-b79d-c1ac96ad9cb0
**Karakeep doc:** `rne4o57dxubu8t0smmyi1y58`
**GitHub:** https://github.com/stepfun-ai/Step-3.5-Flash

StepFun dropped a 196B Mixture-of-Experts that only fires 11B parameters per token — fast, sharp, and supposedly reliable for agentic work. C++, Apache-2.0, ~2k stars. The marketing says "Fast, Sharp & Reliable Agentic Intelligence," which is a hell of a claim for a model nobody's done the independent evals on yet. MoE economics with a 196B billboard number, basically.

## 31. Umi-OCR: free offline OCR for Windows and Linux, with batch and HTTP API — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/hiroi-sora/umi-ocr)

**Source:** https://www.opensourceprojects.dev/post/cd7e8f47-074b-4d0b-a0a8-f035a44c2586
**Karakeep doc:** `lzsvkgri5b07f6gkpdctihvw`
**GitHub:** https://github.com/hiroi-sora/Umi-OCR

Offline OCR that actually doesn't phone home — Python, MIT, a ridiculous 47k stars. Screenshot or batch-import images and PDFs, strips watermarks and headers/footers, scans and generates QR codes, ships with a pile of language packs. Qt/QML frontend, PaddleOCR underneath, HTTP API for the automation nerds. This is the "just give me text from an image" tool everyone wishes the OS shipped.

## 32. Generate OpenAPI specs from your TypeScript controllers and models — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/lukeautry/tsoa)

**Source:** https://www.opensourceprojects.dev/post/9bace1e9-37bc-41a2-9d48-0110915b927d
**Karakeep doc:** `lq1so5b59rb6j2nlfd59oyl9`
**GitHub:** https://github.com/lukeautry/tsoa

tsoa builds OpenAPI-compliant REST APIs straight from your TypeScript controllers and models, so the spec and the code stop drifting apart. TypeScript, MIT, ~4k stars, still actively pushed. Decorators on your routes become a living API contract instead of a hand-maintained YAML nobody updates. The classic fix for "the docs lie about the endpoints."

## 33. A WireGuard setup and management tool for people who'd rather not do it by hand — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/complexorganizations/wireguard-manager)

**Source:** https://www.opensourceprojects.dev/post/cbdc2873-dd50-4a2f-b04b-1cecd7a14f64
**Karakeep doc:** `lkh3tezub8x2g1peujdecumx`
**GitHub:** https://github.com/complexorganizations/wireguard-manager

A shell script that turns WireGuard config hell into a guided menu, because hand-rolling peer keys is nobody's idea of a good time. Shell, license unasserted, ~1.9k stars. Built for road-warrior setups and censorship circumvention, so the GFW topics tell you who the audience is. Covers the private key/peer management dance without making you memorize wg-quick flags.

## 34. A desktop VPN built on Cloudflare WARP, with a Golang WireGuard implementation — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/bepass-org/oblivion-desktop)

**Source:** https://www.opensourceprojects.dev/post/089256f4-bfa8-4262-99b8-b1862c3981b2
**Karakeep doc:** `l5qm9l2vuz0xzgdr61lx0iho`
**GitHub:** https://github.com/bepass-org/oblivion-desktop

Oblivion is an unofficial WARP client for Windows, Mac and Linux, 8.3k stars and still kicking. It rides Cloudflare's WARP network with a Go WireGuard core and TypeScript frontend, plus MASQUE support for the censorship-adjacent crowd. If you want Cloudflare's infrastructure as a personal VPN without their official client breathing down your neck, this is the obvious pick. The "anticensorship" tag tells you exactly who this is for.

## 35. A Chromium-based Android browser that supports Chrome extensions — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/jqssun/android-helium-browser)

**Source:** https://www.opensourceprojects.dev/post/b5a81e74-b23b-4f30-9827-839e96e32941
**Karakeep doc:** `eifjfu4v1gukn3c3dxh5oav1`
**GitHub:** https://github.com/jqssun/android-titanium-browser

Titanium Browser, 2.4k stars, is a secure Android browser that actually runs Chrome extensions — the thing desktop users take for granted and mobile has never really gotten right. GPL-2.0, Shell-tagged repo, still actively pushed a week ago. The kicker: extensions on a phone browser means uBlock Origin on Android without the Kiwi/Brave song and dance. Solid pick if you're tired of ads on your phone.

## 36. Run AI-generated code in secure isolated cloud sandboxes — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/e2b-dev/code-interpreter)

**Source:** https://www.opensourceprojects.dev/post/067c590e-c90e-4eb9-ac6f-613c5662f89c
**Karakeep doc:** `b6eh7oc6kxrdk6o9j96u5u0f`
**GitHub:** https://github.com/e2b-dev/code-interpreter

E2B's code-interpreter is the Python/JS SDK for running AI-generated code in sandboxes, the backend behind every "let the model execute something" demo. Apache-2.0, 2.4k stars, and it plays nice with Anthropic, Cohere, and GPT tooling. If you're building an agent that needs to actually run code rather than hallucinate output, this is the boring-but-correct piece you were going to reinvent anyway. Pushed four days ago, so it's not dead.

## 37. Declare AI work as Markdown contracts, reconcile the results — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/openprose/prose)

**Source:** https://www.opensourceprojects.dev/post/df358cbd-519b-410e-b6cc-e2a8bca26b5e
**Karakeep doc:** `v4w43bf4vz07ay1ponmoqern`
**GitHub:** https://github.com/openprose/prose

Prose bills itself as "a new kind of language for a new kind of computer" — which is either profound or the kind of tagline that makes you roll your eyes. 1.7k stars, TypeScript, MIT, zero topics listed because it's too cool for labels. The pitch is declaring AI work as Markdown contracts and then reconciling the results, which smells like the declarative-AI-agent thing everyone's trying to make stick. Pushed yesterday, so someone's grinding on it.

## 38. One interface for 100+ LLMs, in OpenAI format — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/berriai/litellm)

**Source:** https://www.opensourceprojects.dev/post/7b9ed558-a031-4f40-9822-0c8756a169a3
**Karakeep doc:** `rx14mm68sw8p7jyoj86o3muw`
**GitHub:** https://github.com/BerriAI/litellm

LiteLLM is the de facto AI gateway, 58.8k stars and a Rust core under a Python SDK. It fronts 100+ LLM APIs in OpenAI format with cost tracking, guardrails, load balancing, and logging across Bedrock, Azure, Anthropic, VertexAI, vLLM, Nvidia NIM — the whole damn zoo. If you've ever hand-rolled an abstraction over two model providers and then added a third, you already know why this exists. Pushed today, because it never sleeps.

## 39. Run full Linux with systemd on Android, no Termux needed — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/ravindu644/droidspaces-oss)

**Source:** https://www.opensourceprojects.dev/post/fc872f5c-2d35-4fba-aaef-cfea8d1c5f69
**Karakeep doc:** `hg9frsix7r8e01gntcdd60n9`
**GitHub:** https://github.com/ravindu644/Droidspaces-OSS

Droidspaces is an LXC-like container runtime for Android and Linux that runs full distros natively with "zero performance penalty" — the magic words that make it worth a look. 1.9k stars, Kotlin, GPL-3.0, and it wants kernel SU and namespaces, so it's aimed at rooted devices rather than the casual Termux crowd. Docker topics plus systemd means you get a real init system, not a chroot pretending. Pushed two days ago.

## 40. A reverse-engineered adapter that fronts a bunch of AI chat backends with one Op... — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/bincooo/chatgpt-adapter)

**Source:** https://www.opensourceprojects.dev/post/355c5ea0-e733-4df6-adda-b14c6b0d10a7
**Karakeep doc:** `geonmnlmw4eywtmv34nmwugr`
**GitHub:** https://github.com/xllm-go/bypass

Bypass is a Go adapter that reverse-engineers a pile of AI chat backends — openai-api, coze, deepseek, cursor, windsurf, qodo, blackbox, you, grok, bing — and shoves them all behind one OpenAI-format endpoint. 1.2k stars, GPL-3.0, and the README is in Chinese, which tells you the whole story. This is the sketchy-but-useful tool for when you want to route traffic at services that really don't want you routing traffic at them. Last pushed in June, so it's semi-abandoned but the endpoints probably still work-ish.

## 41. Cloudflare's Rust framework for building fast, programmable networked systems — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/cloudflare/pingora)

**Source:** https://www.opensourceprojects.dev/post/7c64a75f-1947-42ef-bdcf-5e9ee75813e7
**Karakeep doc:** `qkws3oor7l193smlse3hesq6`
**GitHub:** https://github.com/cloudflare/pingora

Pingora is Cloudflare's Rust library for building fast, reliable, evolvable network services. It's the same thing they use to power their own edge proxies and load balancers, now Apache-2.0 and open for anyone. 27k stars and still actively pushed as of last week. If you've ever wanted to write a proxy that doesn't shit the bed under load, this is basically the cheat code.

## 42. One API to run and evaluate agents across six frameworks — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/mozilla-ai/any-agent)

**Source:** https://www.opensourceprojects.dev/post/e12aa5c2-71ba-4971-aef5-642a663f9589
**Karakeep doc:** `nn22dtkl3uhjoz9q6kw2cnl7`
**GitHub:** https://github.com/mozilla-ai/any-agent

Mozilla AI's any-agent gives you a single interface to spin up and benchmark agents across six different frameworks instead of learning six separate APIs. It's Python, Apache-2.0, and tags itself with agent-evaluation and MCP, so it's aimed squarely at people who are tired of the agent-framework churn. 1.2k stars. One entrypoint, evaluate everything, stop rewriting your harness every time a new framework drops.

## 43. DETRs beat YOLOs on real-time object detection, now with v2 and v4 — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/lyuwenyu/rt-detr)

**Source:** https://www.opensourceprojects.dev/post/125d4ccf-a9df-4cc8-92fc-0d6a1825a13b
**Karakeep doc:** `bff7lbwb0brtbjko642olxqg`
**GitHub:** https://github.com/lyuwenyu/RT-DETR

RT-DETR is the CVPR 2024 paper that finally made DEtection TRansformers run fast enough to compete with YOLO in real time, and it's since picked up v2 and v4 variants. Official paddle and pytorch implementations, Apache-2.0, ~5.5k stars. The repo description literally shouts "DETRs Beat YOLOs" with three fire emojis, and the code backs it up.

### LinuxLinks (RSS)

## 44. Verible — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/01/018-coding.png)

**Source:** https://www.linuxlinks.com/verible-systemverilog-parser-linter-formatter-language-server/
**Karakeep doc:** `dm0plc9wmw8ii4ew06jn8pmp`
**GitHub:** https://github.com/chipsalliance/verible

Chips Alliance's take on taming SystemVerilog, because Google's own HDL was a dumpster fire to lint. C++, ~1.9k stars, license unasserted so good luck with that. Parser, style-linter, formatter, and an actual language server — so your editor finally stops gaslighting you about module syntax. If you've ever hand-wrangled Verilog at 2am, this is the tool you wished existed.

## 45. Yeti — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2023/08/people-holding-cloud-network-security-symbols.jpg)

**Source:** https://www.linuxlinks.com/yeti-forensics-intelligence-platform/
**Karakeep doc:** `g6ue2kwyrzobf7v5422d2hda`
**GitHub:** https://github.com/yeti-platform/yeti

"Your Everyday Threat Intelligence" — Python, Apache-2.0, ~2k stars, and the DFIR crowd actually uses it. Ties together observables, indicators, and enrichment into one huntable graph instead of a pile of CSVs. Threat-sharing, enrichment, hunting — the usual CTI buzzword bingo, but it's real software that stays alive.

## 46. HashGarten — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/07/028-checking.png)

**Source:** https://www.linuxlinks.com/hashgarten-graphical-frontend-jacksum/
**Karakeep doc:** `juw2d4peyj9lu8l2kj2yvgfc`
**GitHub:** https://github.com/jonelo/HashGarten

A Swing GUI bolted on top of Jacksum, because somebody genuinely wanted a clicky window for checksums. Java, GPL-3.0, 17 stars — this thing is niche as hell and proud of it. Every CRC and hash function you can name, wrapped in a cross-platform desktop app for verifying file integrity without touching a terminal. Nobody's racing to star it, but it works.

## 47. 14 Best Free and Open Source Linux Graphical IRC Clients — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2019/02/group-diverse-people-with-speech-bubble-icon.jpg)

**Source:** https://www.linuxlinks.com/bestirc/
**Karakeep doc:** `a8u09cxdsh4mwhsi77e72itz`

LinuxLinks rounds up 14 graphical IRC clients in their usual ratings-chart format. The heavy hitters are there — Konversation for KDE, Quassel for the distributed core/client split, HexChat the XChat heir, plus a Rust newcomer in Halloy. A bunch of newer cross-platform picks like Tithon, MERK, and Communi fill out the list for people who don't want to live in 2005. IRC's still kicking via IRCv3, and apparently that's enough for a full roundup.

## 48. Pingvin Share X - self-hosted file sharing platform — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2022/05/Transfer_Files41021.jpg)

**Source:** https://www.linuxlinks.com/pingvin-share-x-self-hosted-file-sharing-platform/
**Karakeep doc:** `ym6ls84j6wnz5qfr9oxd0n05`
**GitHub:** https://github.com/smp46/pingvin-share-x

Pingvin Share X is a secure, self-hosted file sharing platform forked off the original Pingvin Share, written in TypeScript. BSD-2-Clause, docker-friendly, with tags screaming fileshare, self-hosted, and share. It's still being actively pushed as of mid-September, so someone's actually maintaining the fork rather than letting it rot. If you want a self-hosted WeTransfer without the cloud dependency, this is the drop-in.

## 49. 18 Best Free and Open Source Linux TUI Typing Tutors — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2019/02/Typing-Tutor.jpg)

**Source:** https://www.linuxlinks.com/best-free-open-source-linux-tui-typing-tutors/
**Karakeep doc:** `pqkk6fbgmpetqnar12t9fpjb`

Eighteen TUI typing tutors, ranked in classic LinuxLinks chart fashion, for people who want to touch-type without leaving the terminal. The top of the list is ttyper (multi-language support), with Smassh (a MonkeyType clone), GitType (turn your source code into typing challenges), and typtea (dozens of programming languages) rounding out the standouts. It's all free and open source, GUI tools get their own separate roundup, and the whole thing leans on the old argument that touch typing is less tiring and saves your wrists from carpal tunnel. Solid weekend project fuel if you type like a caveman.

## 50. svlint – configurable SystemVerilog linter — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/02/034-proofreading.png)

**Source:** https://www.linuxlinks.com/svlint-configurable-systemverilog-linter/
**Karakeep doc:** `s968ueepxkebp6zk0i7vybqm`
**GitHub:** https://github.com/dalance/svlint

A SystemVerilog linter written in Rust — which is a nice flex, hardware folks getting the memory-safety treatment. 393 stars, MIT license, covers `lint`, `systemverilog`, and `verilog` topics. Last pushed November 2025, so it's not dead. If you write HDL and are tired of the usual C++ linter soup, this one's actually readable.

## 51. JS Paint – classic MS Paint recreation with modern features — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2023/04/brushes-colorful-painting.jpg)

**Source:** https://www.linuxlinks.com/js-paint-classic-ms-paint-recreation/
**Karakeep doc:** `qzki2g5yvrrs2zo4ip0d3wlz`
**GitHub:** https://github.com/1j01/jspaint

A faithful MS Paint recreation in the browser, done in pure JavaScript/HTML5 canvas. 7.9k stars, MIT license, and it's a full app plus image editor, not a toy. The README literally says "Classic MS Paint, REVIVED + ✨Extras," which tells you the author knows exactly the vibe they're chasing. Still actively pushed as of mid-2026.

## 52. XBian - Debian-based media center Linux distribution — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/04/Linux-Distributions.png)

**Source:** https://www.linuxlinks.com/xbian-debian-based-media-center-linux-distribution/
**Karakeep doc:** `lo2lg2zk4o8lzd9knvtlbp59`

A lightweight Debian-based distro that turns small boards into dedicated Kodi media centers. Unlike appliance-style setups that hide the OS, XBian keeps Debian's flexibility so you can apt-install extra stuff and repurpose the box. It runs a rolling-release model, uses Btrfs for the root filesystem with snapshot/rollback boot, and targets Raspberry Pi, CuBox-i, and Hummingboard. Ships NFS, Samba, AirPlay, CEC, LIRC, and PVR support out of the box.

## 53. 19 Best Free and Open Source Electronic Design Automation Tools — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2019/05/electronic-design-automation-tools.jpg)

**Source:** https://www.linuxlinks.com/eda/
**Karakeep doc:** `jratgcn486xgk75938g3556c`

A roundup of 19 free Linux EDA tools for PCB and chip design, from the obvious KiCad and gEDA down to niche picks like KLayout, xschem, and Magic. Each entry gets a portal page, feature breakdown, screenshot, and links. Handy if you're doing circuit design and want to avoid the Altium/Cadence tax. The comments section is the usual "KLayout only has 100 stars, scandalous" nerding.

## 54. Chili3D – browser-based 3D CAD application — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/02/worker-drawing-blueprint.jpg)

**Source:** https://www.linuxlinks.com/chili3d-browser-based-3d-cad-application/
**Karakeep doc:** `arkoc56r33h4rqg097kdh8vg`
**GitHub:** https://github.com/xiangechen/chili3d

Chili3D is a full 3D CAD tool that runs entirely in the browser, no install, no native client. Under the hood it's TypeScript wrapping OpenCascade (OCCT) geometry — the same kernel real CAD packages use — so you're getting actual parametric modeling, not some toy viewer. 4,840 stars, AGPL-3.0, still actively pushed as of a couple weeks ago. If you've ever wanted SolidWorks-in-a-tab without the SolidWorks price tag, this is the closest free thing going.

## 55. Open Video Downloader – cross-platform yt-dlp GUI — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/03/women-holding-youtube-icon.jpg)

**Source:** https://www.linuxlinks.com/open-video-downloader-cross-platform-yt-dlp-gui/
**Karakeep doc:** `be5p3ca8o7g7uh3irnkgeuu4`
**GitHub:** https://github.com/jely2002/youtube-dl-gui

Open Video Downloader is a cross-platform GUI for youtube-dl built in Rust with Tauri, Vue, and TypeScript — so it's fast, native-ish, and not another Electron pig. 9,207 stars, AGPL-3.0, pushed within the last few days, so it's alive. If you're sick of typing yt-dlp flags into a terminal every time you want to rip a video, this wraps it in a clean point-and-click shell. The name says youtube-dl but it inherits yt-dlp's full site support, so it's not just YouTube.

## 56. 23 Useful Free and Open Source PDF Tools — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2019/04/PDF-File.png)

**Source:** https://www.linuxlinks.com/pdftools/
**Karakeep doc:** `r3pjtbzzfwfcc3ual6b8fsgp`

A curated roundup of 23 free/open-source PDF utilities, and unlike the usual filler lists this one's actually useful. It splits the heavy hitters — Scribus, Ghostscript, PDFBox, PoDoFo — from the niche stuff you'd never find on your own, like pdfgrep for searching text, Dangerzone for sanitizing sketchy PDFs, and pdfresurrect for digging into a file's guts. Each entry has its own portal page with screenshots and feature breakdowns. PDF viewers and manipulation tools are deliberately carved out into separate articles, so this list stays focused on creation and the oddball utilities.

## 57. Meloville - local music player — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/08/Music-Player-GUI-Review.png)

**Source:** https://www.linuxlinks.com/meloville-local-music-player/
**Karakeep doc:** `oj11rpxy8rko4ybngrhh3jwf`
**GitHub:** https://github.com/NevPeth/meloville-arch

Meloville is a C++ desktop music player that leans hard into album artwork, feeling more like Spotify than your average local player. The standout features are Big Picture mode (great for a TV or second display), synced LRC lyrics, MPRIS integration, and "Listen Along," which spins up a tiny web server so someone in a browser can hear what you're playing without installing anything. The reviewer's one hard complaint is no gapless playback, which is a dealbreaker for live albums. ~270MB RAM, GPLv3, still young but genuinely polished.

## 58. StaticPipes – flexible pipeline-based static site generator — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/10/SSG-3.png)

**Source:** https://www.linuxlinks.com/staticpipes-flexible-pipeline-based-static-site-generator/
**Karakeep doc:** `d9b52yvzn3gmvx29hiwo4voj`
**GitHub:** https://github.com/TeacakeTech/staticpipes-core

StaticPipes is an "unopinionated" static site generator in Python that — refreshingly — actually checks the output for you. BSD-3-Clause licensed, single star, last pushed Aug 2026, so it's early-days territory. The pipeline-based design is the hook: chain steps together and it validates what comes out the other end. One star means you're basically the beta tester. 🐍

## 59. Akira Linux - Niri-based rolling-release Linux distribution — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/04/Linux-Distributions.png)

**Source:** https://www.linuxlinks.com/akira-linux-niri-based-rolling-release-linux-distribution/
**Karakeep doc:** `ge6blngufnvp329t1sr5r2xh`

A rolling distro for people who hate conventional desktops, built on Void-based Vostok and centred on the Niri scrollable-tiling Wayland compositor. Keyboard-driven, console-oriented, systemd-free — runit for init, XBPS for packages, Calamares for the graphical install. Ships a separate Nvidia edition with proprietary drivers baked in, and claims zero telemetry. If assembling your own Void setup sounds like a chore, this does it for you.

## 60. Verilator - SystemVerilog simulator and lint system — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/01/013-coding.png)

**Source:** https://www.linuxlinks.com/verilator-systemverilog-simulator-lint-system/
**Karakeep doc:** `ozqg8mcykbdrqq3l2tqcrzfj`
**GitHub:** https://github.com/verilator/verilator

Open-source SystemVerilog simulator and lint system that compiles Verilog/SystemVerilog down to C++/SystemC for cycle-accurate, fast simulation. ~3.9k stars, SystemVerilog/C++, actively pushed as of this month. This is what real chip designers reach for when they want speed over the slow, heavyweight commercial simulators. A legit workhorse, not a toy.

## 61. paint.software – Paint.NET-style raster image editor for Linux — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2018/10/Painting-tools.jpg)

**Source:** https://www.linuxlinks.com/paint-software-paint-net-style-raster-image-editor/
**Karakeep doc:** `bau1xlmvhvdlar65929z6iep`
**GitHub:** https://github.com/Univers4craft/paint.software

An open-source Paint.NET clone for Linux — C++/Qt6 with layers, effects, and adjustments. MIT licensed but a paltry 21 stars, so it's early days and clearly hungry for contributors. If you've been missing Paint.NET's no-nonsense editing on Linux, this is the gap-filler in progress. Don't expect it to replace GIMP overnight.
