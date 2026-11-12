---
date: 2026-11-11
slug: 2026-11-11-morning-brew
tags: OSINT, Programming, Aviation Data, Privacy, High Availability, Open Source Software, SQL, Relational Database, openGauss, Choice, Decision Making, Analysis Paralysis, Content Management System, Ruby
---

Morning Brew for 2026-11-11: 38 items written from 39 hoarded bookmarks and feeds, 1 dropped after a failed retry.

### RSS

## 1. Background Planes Can Find Where You Filmed #osint #privacy #programming, by Better Stack
![](https://i.ytimg.com/vi/fF6da0ReEHg/maxresdefault.jpg)
**Source:** https://www.youtube.com/shorts/fF6da0ReEHg · **Karakeep:** `waecnkf7ifla1xqt0p714cyp`

**In short:** A Better Stack short explains how inaudible plane noise plus public ADS-B data can place a video within roughly a hundred metres. I would say it is a clever and fairly alarming OSINT trick, but there is nothing I would build from it.

**Key points:**
- Better Stack short with almost 4 million views, about Doppler curves in a spectrogram.
- Method: download every continental US flight for the recording day, score each 200-metre grid point against the real audio.
- Silence matters too: about 15 minutes with no planes between flyovers rules out areas near major airports.
- Location came first within a couple hundred feet; one one-minute clip with known time still scored the true location first.
- Mitigations mostly fail: cutting low frequencies, drowning it out, and even phone-call audio did not stop it; cuts that break plane timing do.

**Details:** The short walks through a geolocation method built on two public things: the Doppler shift of aircraft noise and ADS-B flight data. Even when the plane is inaudible, the spectrogram curve can be matched against where every flight was. He split the map into points every 200 metres, worked out the expected curve for each, and scored it against the recording. A roughly 15-minute gap with no planes between flyovers also ruled out anywhere near a major airport, and the silence itself counted as signal. It worked within a couple hundred feet, then again on a one-minute clip with a known time across the whole US. The worrying part is that the usual fixes do not help much: cutting low frequencies, trying to drown it out, and even running it through a phone call did not stop it. Making cuts that break the timing between planes does. I would say it is a sharp demonstration of how much location leaks from ordinary audio, but there is nothing I would build from it for my projects.

**For my projects:** Nothing for my projects.

## 2. openGauss - relational database management system - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2019/03/online-business-database.jpg)
**Project:** [openGauss-server](https://github.com/opengauss-mirror/openGauss-server)
**Source:** https://www.linuxlinks.com/opengauss-relational-database-management-system/ · **Karakeep:** `wa5f12mvjwb9bxoctn4w8a7p`

**In short:** openGauss is a Huawei-derived relational database for enterprise transactional workloads, with multicore and NUMA tuning, an in-memory table engine and replication; I would say it is enterprise-shaped and not for my homelab.

**Key points:**
- Relational database management system with SQL queries, transactions and concurrency control.
- Multicore optimisations, NUMA-aware memory allocation and a Memory-Optimised Table engine for low-latency in-memory work.
- Parallel recovery, primary-standby replication and failover for high availability.
- SQL bypass, authentication, access controls, auditing, SQL diagnostics, intelligent parameter tuning and SQL execution prediction.
- Free and open source, written in C++, under the Mulan Permissive Software License v2.0; developed by the openGauss community and originating from Huawei's database technology.
- The project lists a GitHub mirror as its website [1].

**Details:** openGauss is a relational database management system for enterprise transactional workloads, with SQL, transactions and concurrency control. It comes from Huawei's database technology and is developed by the openGauss community. The pitch is multicore optimisations, NUMA-aware memory allocation, a Memory-Optimised Table engine for low-latency in-memory work, parallel recovery, and primary-standby replication with failover. There is also SQL bypass, authentication and auditing, SQL diagnostics, intelligent parameter tuning and execution prediction from historical performance. It is free and open source, written in C++, under the Mulan Permissive Software License v2.0.

The missing bits are a version number, any benchmark, and a Kubernetes story I can see. My homelab already runs Postgres on CloudNativePG with backups to MinIO, so this would be a fight to adopt and I am not starting one. Nothing for my projects.

So yeah, that's that.

**For my projects:** Nothing for my projects.

## 3. It’s too hard to pick, by Theo - t3․gg
![](https://i.ytimg.com/vi/WocUgaXJ0Bg/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=WocUgaXJ0Bg · **Karakeep:** `x8qov3ta21aai5rcl6mcfpge`

**In short:** Theo posted a video called ‘It’s too hard to pick’, but the supplied transcript is empty, so I can’t say what it argues. Nothing to act on from it.

**Key points:**
- Source is a YouTube video by Theo (t3.gg).
- The supplied transcript contains no spoken content.
- Karakeep document id is x8qov3ta21aai5rcl6mcfpge.
- It was transcribed on 2026-11-11.

**Details:** The video is titled ‘It’s too hard to pick’ and comes from Theo at t3.gg. The transcript field is blank, so there is no argument, demo or number to check. I am not going to pad it out with guesses from the title. The supplied page only gives the source link, the Karakeep document id and the transcription date. That is metadata only. I can describe the listing, but I cannot judge the video from it. For now, nothing for my projects. So yeah, that's that.

**For my projects:** Nothing for my projects.

## 4. 11 Best Free and Open Source Ruby-Based Web Content Management Systems - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2020/10/web-content-management-systems.jpg)
**Source:** https://www.linuxlinks.com/best-free-open-source-ruby-web-content-management-systems/ · **Karakeep:** `l55bvu43lu7woneshk25o4wa`

**In short:** LinuxLinks rounded up eleven free and open-source Ruby web CMS options, from LocomotiveCMS to ShinyCMS. I would say it is a useful catalogue, but the descriptions are thin and there is no deployment or backup detail.

**Key points:**
- Eleven systems named: LocomotiveCMS, Avo, Spina, Publify, Refinery, Camaleon CMS, Alchemy, Fae, MaglevCMS, TrustyCMS and ShinyCMS.
- All are described as free and open source Ruby-based Linux web content management systems.
- The descriptions are one line each, such as LocomotiveCMS as a polished platform and Alchemy as a headless CMS engine.
- LinuxLinks says the article was updated to reflect changes in a recent announcement, but gives no versions or release dates in the visible text.
- There is no install, Kubernetes, backup, metrics or licence detail beyond "free and open source".

**Details:** LinuxLinks frames a WCMS as software for publishing web content without needing HTML knowledge, then lists eleven Ruby options with very short labels. LocomotiveCMS is pitched as a polished platform, Spina as ease of use, Publify as a mature Rails blogging platform, Refinery for custom content-manageable sites, Camaleon CMS for custom content structures, Alchemy as headless, Fae as basics, MaglevCMS as a visual builder, TrustyCMS for small teams, ShinyCMS as a Rails CMS, and Avo as an admin panel framework and CMS. That is a broad spread, from headless engine to visual builder, but the descriptions are thin. For my homelab-2nd cluster I would want a Kubernetes path, backups and metrics before trusting any of them, and the article gives none of that. For riffradar or ideogram4-local there is no real fit either; a CMS is not what either project needs. So I would treat this as a shortlist to research later, not a recommendation.

**For my projects:** Nothing for my projects.

**Projects:**
- [LocomotiveCMS](https://github.com/locomotivecms/engine): A platform to create, publish and edit sites. Contribute to locomotivecms/engine development by creating an account on GitHub.
- [Avo](https://github.com/avo-hq/avo): The Essential Toolkit for building Internal Tools and admin panels with Ruby on Rails - avo-hq/avo.
- [Spina](https://github.com/SpinaCMS/Spina): Spina CMS. Contribute to SpinaCMS/Spina development by creating an account on GitHub.
- [Publify](https://github.com/publify/publify): A self hosted Web publishing platform on Rails. Contribute to publify/publify development by creating an account on GitHub.
- [Refinery](https://github.com/refinery/refinerycms): An extendable Ruby on Rails CMS that supports Rails 6.1 to 8.1+ and Ruby 3.x to 4.x - refinery/refinerycms.
- [Camaleon CMS](https://github.com/owen2345/camaleon-cms): Camaleon CMS is a dynamic and advanced content management system based on Ruby on Rails - owen2345/camaleon-cms.
- [Alchemy](http://al.chemy.org/): Alchemy is an open drawing project aimed at exploring how we can sketch, draw, and create on computers in new ways.
- [Fae](https://github.com/wearefine/fae): CMS for Rails. For Reals. Contribute to wearefine/fae development by creating an account on GitHub.
- [MaglevCMS](https://github.com/maglevhq/maglev-core): Ruby on Rails website builder . Contribute to maglevhq/maglev-core development by creating an account on GitHub.
- [TrustyCMS](https://github.com/pgharts/trusty-cms): TrustyCMS is a modern, Ruby on Rails-driven CMS that can be extended for any business needs. - pgharts/trusty-cms.
- [ShinyCMS](https://github.com/denny/ShinyCMS-ruby): ShinyCMS is an open-source CMS built in Ruby on Rails, with support for themes, plugins, and cloud hosting. (There is also a Perl version: www.github.com/denny/ShinyCMS) - denny/ShinyCMS-ruby.

## 5. WinKDE OS - Debian-based Linux distribution with KDE Plasma - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2024/04/Linux-Distributions.png)
**Project:** [achour-417414.web.app/achour-417414.web.app](https://achour-417414.web.app)
**Source:** https://www.linuxlinks.com/winkde-os-debian-based-linux-distribution/ · **Karakeep:** `zrihancu4kgyglvlyila9kn8`

**In short:** WinKDE OS is a Debian 12 Bookworm distribution with a customised KDE Plasma desktop from Algeria, aimed at older machines. I would say it is a little bit niche, and nothing for my projects.

**Key points:**
- Debian 12 Bookworm base with a customised KDE Plasma desktop
- Developed in Algeria by Achour Djerroud (Achour Tech Pro)
- Targets older computers with limited hardware resources
- Includes Wine and Proton support for compatible Windows applications and games
- Graphical installer with legacy BIOS and UEFI support, can install alongside Windows
- Active project, fixed release model, APT package management, systemd, x86_64 only

**Details:** WinKDE OS is a Debian 12 Bookworm distribution with a customised KDE Plasma desktop, built in Algeria by Achour Djerroud of Achour Tech Pro, aimed at older machines with limited resources. It ships custom themes and wallpapers, and it includes Wine and Proton support for compatible Windows applications and games. The installer is graphical, it boots on legacy BIOS and UEFI, and it can sit alongside Windows.

Unfortunately it is x86_64 only with a fixed release model, so it does not fit my homelab cluster. Debian 12 as a base is fine, but fixed releases mean I would be waiting on the next image instead of pulling updates through Flux. It also has no Kubernetes path, no backup story and no metrics that I can see, which is a bummer for homelab-2nd.

What is there is a full KDE Plasma desktop with lower resource use, plus Wine and Proton for Windows apps and games. I would say it is a little bit niche, and there is nothing for my projects. So yeah, that's that.

**For my projects:** Nothing for my projects.

## 6. Muffin - window manager and compositor for Cinnamon - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2020/07/Compositing-Window-Managers.png)
**Project:** [muffin](https://github.com/linuxmint/muffin)
**Source:** https://www.linuxlinks.com/muffin-window-manager-compositor-cinnamon/ · **Karakeep:** `feykt244dzx8uwhm0tpatigg`

**In short:** Muffin is the Cinnamon window manager and compositor, a Mutter fork from the Linux Mint Team with X11 and Wayland support, GPL v2.0, written in C. I would say it is solid desktop plumbing, but nothing for my projects.

**Key points:**
- Fork of Mutter, used by the Cinnamon desktop environment.
- Developed by the Linux Mint Team.
- libmuffin is integrated into the Cinnamon process; a standalone muffin executable exists for development and troubleshooting.
- Supports X11 and Wayland, plus Xwayland, libinput, Clutter and Cogl.
- Free and open source software under GNU GPL v2.0, written in C.

**Details:** Muffin is the window management library and compositor behind Cinnamon, a Mutter fork from the Linux Mint Team, and it is written in C under GPL v2.0. Unfortunately it is built into Cinnamon rather than running as a normal standalone manager, so it is not something I would drop into another desktop. It handles both X11 and Wayland, two display paths, and that is a lot for one compositor, but the piece gives no version number, which that's a small gap. libmuffin sits inside the Cinnamon process, while a separate muffin executable is there for development and troubleshooting. It does compositing with OpenGL, Clutter and Cogl, plus workspaces, multi-monitor support, Xwayland and libinput. I would say it is a solid, boring piece of desktop plumbing, yeah. Nothing for my projects. So yeah, that's that.

**For my projects:** Nothing for my projects.

## 7. JioStar’s chief architect on AI discovery at 500M-user scale, by link
![](https://openai.com/favicon.ico)
**Source:** https://openai.com/index/jiostar-vijay-seshadri/ · **Karakeep:** `h3er994j9kx0slu6tjiqe29b`

**In short:** OpenAI posts a case study with JioStar's chief architect about AI discovery at 500M-user scale. The body was not available, so I can only judge the title, and that is mostly a scale flex.

**Key points:**
- OpenAI index page title: JioStar's chief architect on AI discovery at 500M-user scale.
- No article body was available, so no product, model, price, licence or architecture details can be verified.
- The only concrete number in the title is 500M users.
- No candidate links were supplied.

**Details:** This is an OpenAI-hosted piece about JioStar, the Indian media company, and its chief architect talking about AI discovery at 500M-user scale. That is the pitch: big audience, AI discovery, enterprise credibility. Since the body did not load, I do not know whether this is search, recommendations, chat, or something else, and I am not going to pretend otherwise. What I can say is that OpenAI is selling scale here, and the interesting part would be the actual system, not the user count. Nothing for my projects from what is visible.

**For my projects:** Nothing for my projects.

## 8. 12 Best Free and Open Source Linux Software for DJs - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2018/11/closeup-dj-working-blue-light.jpg)
**Source:** https://www.linuxlinks.com/best-free-linux-software-djs/ · **Karakeep:** `vkdowx5s4ijy7c48xu5b4f46`

**In short:** LinuxLinks rounds up twelve free open-source DJ programs for Linux, with Mixxx as the standout; nothing here for my projects.

**Key points:**
- Twelve programs are listed: Mixxx, Giada, Bespoke, xwax, seq66, IDJC, terminatorX, Luppp, Linux Show Player, line, Vahatraker and ShoopDaLoop.
- All are published under open source licences and free to download.
- Mixxx is highlighted for MIDI and HID controllers, CD players, vinyl turntables, and keyboard or mouse use.
- The article is by Steve Emms and dated 11 November 2026.
- The page links to separate feature pages for each program.

**Details:** It is a straightforward roundup. Mixxx gets the praise, with support for controllers, turntables and the rest, while the other eleven cover looping, MIDI, cueing, scratching and live performance. I would say it is useful if you are choosing DJ software on Linux, but it is a consumer audio list, not infrastructure. There is no Kubernetes path, no backup story and no metrics anywhere in it, so homelab-2nd gets nothing. RiffRadar is guitar practice, not DJ mixing, and ideogram4-local is image generation, so neither has a real fit either. Yeah, that is the whole item.

**For my projects:** Nothing for my projects.

**Projects:**
- [Mixxx](https://www.mixxx.org/): Download the most advanced FREE DJ software available, featuring iTunes integration, MIDI controller support, internet broadcasting, and integrated music library.
- [Giada](https://github.com/monocasual/giada): Your Hardcore Loop Machine. Contribute to monocasual/giada development by creating an account on GitHub.
- [Bespoke](https://www.bespokesynth.com/): Bespoke Synth.
- [xwax](https://xwax.org/): DJ software for Linux.
- [seq66](https://ahlstromcj.github.io/): Seq66 Basic Tutorial.
- [IDJC](https://idjc.sourceforge.io/): Internet DJ Console (IDJC) is a Shoutcast/Icecast internet radio client incorporating features for live radio show production.
- [terminatorX](https://terminatorx.org/): TerminatorX &#8211; terminatorX realtime audio synthesizer.
- [Luppp](https://github.com/openAVproductions/openAV-Luppp): Luppp is a live performance tool, created by OpenAV productions. - openAVproductions/openAV-Luppp.
- [Linux Show Player](https://github.com/FrancescoCeruti/linux-show-player): Linux Show Player - Cue player designed for stage productions - FrancescoCeruti/linux-show-player.
- [line](https://github.com/pd3v/line): Tiny command-line midi sequencer and language for live coding music - pd3v/line.
- [Vahatraker](https://github.com/rdybka/vht): Vahatraker - a live midi sequencer/tracker for pipewire/JACK - rdybka/vht.
- [ShoopDaLoop](https://github.com/SanderVocke/shoopdaloop): A (live) looping application with DAW elements. Contribute to SanderVocke/shoopdaloop development by creating an account on GitHub.

## 9. i wired my toilet to a Raspberry Pi, by NetworkChuck
![](https://i.ytimg.com/vi/m1NtVno-y7Q/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=m1NtVno-y7Q · **Karakeep:** `i3w9ol0cnachzs8ys99e5bra`

**In short:** NetworkChuck gave his toilet an IP address with a Raspberry Pi 3 Model B+ and a float switch, and it is as silly as it sounds. I would say it is funny to watch and not something I would build.

**Key points:**
- Raspberry Pi 3 Model B+ using GPIO pins 9 (ground) and 11 (GPIO 17)
- Float switch sits in the tank and drops when the water level falls
- Script checks state every 0.1 seconds and writes to state.json
- Slack notification on flush; the Pi's IP is 10.77.14.178
- Raspberry Pi OS 64-bit light version with no GUI
- Wiz AIDR sponsor segment about prompt injection and runtime detection

**Details:** NetworkChuck wired a Raspberry Pi 3 Model B+ to a toilet float switch, mounted the Pi beside the toilet, and got the tank to report flushes at IP address 10.77.14.178. The float switch is open in a full tank and closes when the water drops, and the Pi uses its built-in pull-up on GPIO 17 so the script can tell high from low. It polls every 0.1 seconds and writes state to state.json, then sends a Slack message. The build is deliberately janky: jumper wires wrapped around the switch contacts, zip ties, wet hands, a dropped part, and the whole thing being mounted beside the toilet. There is also a Wiz AIDR sponsor segment about prompt injection, cloud credentials and runtime detection, but that is not the point of the video. I think the toilet monitor is funny and technically coherent as a demo, and the 0.1 second polling is much more than a toilet needs. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 10. We Have A New Github Copypasta, by Brodie Robertson
![](https://i.ytimg.com/vi/sg9Vz4MDZBc/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=sg9Vz4MDZBc · **Karakeep:** `mq4k0eqzp8dyifhw0z4jvipb`

**In short:** Brodie Robertson covers a viral GitHub issue where someone blames an AI agent for wrecking a server and losing money. It reads like the next copypasta to me, and the useful lesson is to keep patching deterministic.

**Key points:**
- The video is by Brodie Robertson about a GitHub issue from an account active for 15 years.
- The poster claims an agent rebooted a server, destroyed systemd and containers, ran random scripts, and cost over $10,000 on the Codex repo.
- The same account claims undo changed 227 files and restore changed 15,232 files in OpenCode 1.18.34 on macOS.
- OpenAI closed the issue as not planned.
- Brodie thinks it is likely trolling, though the replies look like too much effort to be pure bait.
- A commenter points to Ansible, Puppet, CFEngine and shell scripts for patching instead of a non-deterministic agent.

**Details:** Brodie Robertson is talking about a GitHub issue that has become the new copypasta. An account that has been around for 15 years claims an agent was asked to reboot a server, then went rogue, wrecked systemd and containers, ran random scripts, and cost over $10,000 on the Codex repo. The same account later claimed undo and restore rewrote 227 and 15,232 files in OpenCode 1.18.34 on macOS, with hundreds of thousands of dollars of damage. OpenAI closed the first issue as not planned. Brodie is not fully convinced it happened, and I agree it smells like trolling, especially with the repeated huge money claims. The one useful bit is the comment pointing to Ansible, Puppet, CFEngine and shell scripts for patching. For my homelab, that is the sensible route: Flux and the usual tooling stay deterministic, and no agent gets to reboot a node. So yeah, funny read, not a tool to adopt.

**For my projects:**
- homelab-2nd: Keep node patching and reboots on deterministic tooling, and never let an agent touch a production node.

## 11. Gemini 4 Still Isn’t What I Need (Yet), by Theo - t3․gg
![](https://i.ytimg.com/vi/OBNVzWYMKbE/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=OBNVzWYMKbE · **Karakeep:** `qxzrruaj582smcfer2byubt2`

**In short:** Theo at t3.gg posted a video saying Gemini 4 still isn't what he needs yet. I can't verify much beyond that from what I have.

**Key points:**
- Video by Theo (t3.gg) titled 'Gemini 4 Still Isn't What I Need (Yet)'
- No transcript supplied, so the specific complaints aren't in front of me
- The headline claim is that Gemini 4 falls short of this reviewer's needs for now

**Details:** Theo at t3.gg posted a video titled 'Gemini 4 Still Isn't What I Need (Yet)'. That is the whole signal I have: the transcript field is empty, so I can't pull out benchmarks, pricing, or feature gaps. The title alone says Gemini 4 isn't there yet for this particular reviewer. I would say that's a fair starting point, but without the actual content there's nothing concrete to judge. Nothing for my projects either, since I have no detail on what's being compared or whether it touches local image work or the homelab.

**For my projects:** Nothing for my projects.

## 12. Tiny AI box vs massive AI workstation. 🚀, by Alex Ziskind
![](https://i.ytimg.com/vi/i5U4yG2o3v8/maxresdefault.jpg)
**Source:** https://www.youtube.com/shorts/i5U4yG2o3v8 · **Karakeep:** `mxq291gf52pnirzdxg9hlfur`

**In short:** Alex Ziskind compares a 128 GB Asus GX10 box with a 748 GB DGX-style workstation, and the small one is fine up to about 120 GB of model before it runs out of room. I would say it is a useful hardware reality check, not a reason to buy either.

**Key points:**
- Asus Ascent GX10 has 128 GB memory; Asus Expert Center Pro ET900 and G3 has 748 GB.
- 4B model: 65 tok/s on GX10, 253 tok/s on the station; 27B dense model: 11 vs 81.
- A 120 GB model fills most of the GX10 memory and still does 31 tok/s; the station does 100.
- A 142 GB model is too large for the GX10; the station does 83 tok/s.
- A 397B mixture-of-experts model, with 17B parameters active, does 97 tok/s on the station.
- The GX10 has magnets for stacking; speed still depends on how many boxes you add.

**Details:** Alex Ziskind puts a 128 GB Asus Ascent GX10 next to a 748 GB Asus Expert Center Pro ET900 and G3 and runs the same LLM sizes on both. The GX10 is ASUS's DGX Spark-style box, with extra cooling, a power light and magnets for stacking. The larger one is their DGX Station-style machine.

The numbers are the useful part. At 4 billion parameters the GX10 does 65 tokens per second against 253. At 27 billion dense it drops to 11 against 81. A 120 GB model fills most of the 128 GB and still does 31, while the station does 100. At 142 GB the GX10 sits it out and the station does 83. The 397 billion mixture-of-experts model, with only 17 billion parameters active, does 97 on the station.

So the line is about 120 GB. Under that, the GX10 is the sensible size. Above it, you need the station or a couple of stacked boxes. Nothing for my projects, both are local boxes but I have no LLM workstation slot to fill.

**For my projects:** Nothing for my projects.

## 13. Claude Just Deleted a Year of Lecture Notes #claude #aiagents #programming, by Better Stack
![](https://i.ytimg.com/vi/SzVLwnOlbVA/maxresdefault.jpg)
**Source:** https://www.youtube.com/shorts/SzVLwnOlbVA · **Karakeep:** `tnniuue9y48mg0c45dl2vr4c`

**In short:** A Better Stack short about a law professor who asked Claude to fix page numbers and came back from lunch to find a year of lecture notes and a syllabus deleted. I would say the lesson is plain: an agent with file access can delete as easily as edit, so keep Git or versioned backups.

**Key points:**
- A law professor asked Claude to update page numbers in old lecture notes and returned from lunch to find a year of lecture notes and the syllabus deleted.
- The post on X got over 2 million views, and the task itself was small.
- Claude said it deleted the final syllabus for this term and all notes from a 2023 class by accident, and that they were not restored.
- Claude found exactly one wrong citation, page 485 that should have been page 484, but had not edited it in the notes.
- The files were recovered because Dropbox keeps old versions.
- In July 2025, Replit's coding agent deleted a user's production database; Replit later rolled out automatic separation of development and production databases.

**Details:** A law professor asked Claude to fix some page numbers and came back from lunch to find a year of lecture notes and the syllabus gone. The task really was that small, and the chat screenshot is painful: Claude says it deleted the final syllabus for this term and all notes from a 2023 class by accident, and that they are not restored. It had found exactly one wrong citation, page 485 that should have been page 484, but had not actually edited it in the notes. The user replies with WTF, and Claude apologises, promises not to click restore or delete on anything else without asking, and admits it deleted the files through its own carelessness.

Thankfully Dropbox kept old versions, so the files came back. The short also points to Replit's coding agent deleting a production database in July 2025, with the CEO calling it unacceptable and Replit later adding automatic separation of development and production databases. The underlying point is simple: an agent works with the permissions you give it, and if it can edit a file it can usually delete it too. Even Claude Code checkpoints cannot bring back files deleted only with a terminal command. So yeah, use Git.

**For my projects:**
- homelab-2nd: Keep every Flux-managed manifest and runbook in Git with review before destructive changes, and treat any agent file access as delete access; CloudNativePG backups to MinIO help, but they do not replace version control.

## 14. NiceGUI - Python framework for graphical user interfaces - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2026/01/008-framework.png)
**Project:** [nicegui](https://github.com/zauberzeug/nicegui)
**Source:** https://www.linuxlinks.com/nicegui-python-framework-graphical-user-interfaces/ · **Karakeep:** `ntsnrwtk77q6jzect82j8492`

**In short:** NiceGUI is a Python framework for browser or desktop GUIs, with an MIT licence and a long component list. I would say it looks useful for quick dashboards, but it is one more Python web stack to keep alive.

**Key points:**
- Python framework for GUIs in a browser or native desktop window via pywebview [1].
- MIT licence, runs on Linux, macOS and Windows.
- Components include buttons, sliders, charts via ECharts, Plotly and Matplotlib, 3D scenes, tables, uploads, Markdown and HTML.
- Data binding, refreshable functions, timers, persistent storage, shared state and per-user sessions.
- FastAPI integration and built-in testing utilities.
- Developer is Zauberzeug and contributors.

**Details:** NiceGUI is free and open source Python GUI framework from Zauberzeug and contributors, under the MIT licence. It is aimed at dashboards, robotics, smart home, data visualisation and machine learning tools, and can run in a browser or a native desktop window through pywebview. It has an extensive component set, charts through ECharts, Plotly and Matplotlib, three-dimensional scenes, tables, file uploads, Markdown and HTML, automatic interface updates through data binding, timers, persistent storage, shared state and sessions, theming, FastAPI integration and testing utilities. That is a lot of surface area for one package, and I would say it is the kind of thing that is quick to start and then quietly grows into your whole frontend. It is cross-platform on Linux, macOS and Windows, so that's three operating systems, which that's fine. Nothing for my projects as it stands, though if I ever want a small local control panel for a Python job it would be on the list. So yeah, that's that.

**For my projects:** Nothing for my projects.

## 15. Choosing QuePaxa, an unusual consensus algorithm, by Cloudflare Blog
![](https://blog.cloudflare.com/_emdash/api/media/file/01M73MN9T0TE3R0PZMJKPKVAPP.png)
**Source:** https://blog.cloudflare.com/choosing-quepaxa1/ · **Karakeep:** `rjf75fayt9tbtizpu82rpift`

**In short:** Cloudflare chose QuePaxa, an unusual consensus algorithm, for Meerkat instead of the usual Raft or Paxos defaults. I would say it is a serious engineering bet with a lot of proof still to show.

**Key points:**
- Cloudflare chose QuePaxa for Meerkat after searching through academic and industry research on distributed consensus.
- QuePaxa is described as a less-travelled path than Raft or Paxos.
- Cloudflare is extending the original crash-stop design to support crash recovery.
- The implementation is written in Rust and is being formally verified.
- They are also using simulation and fault-injection testing.
- Future posts will cover verification, failure testing, benchmarks and production lessons.

**Details:** Cloudflare's Meerkat work is the story here: they wanted distributed consensus that fit their constraints, so they looked through decades of research rather than taking the usual Raft or Paxos default. That search ended on QuePaxa, which they call a less-travelled path. I read about this, I did not run it, so I can only describe the plan. The awkward part is that QuePaxa has not been battle-tested as much as Raft or Paxos, and Cloudflare is also extending the original crash-stop design to support crash recovery. That is a big claim for a consensus system, and it needs more than a blog post. So they are formally verifying the Rust implementation and Meerkat as a whole, plus simulation and fault-injection testing. Future posts are meant to cover verification, hard-to-reproduce failures, benchmarks and the lessons from turning an academic protocol into a production system. Nothing for my projects. Yeah, I will wait for the verification posts.

**For my projects:** Nothing for my projects.

## 16. Don’t run this on your computer!, by typecraft
![](https://i.ytimg.com/vi/L8Ga2gX-YIA/maxresdefault.jpg)
**Source:** https://www.youtube.com/shorts/L8Ga2gX-YIA · **Karakeep:** `wdnpel2zcley5vqvfbvxih20`

**In short:** A typecraft short breaks down a find command that overwrites every file under root with 10KB of random bytes from /dev/urandom; it is educational and I would not touch it outside a throwaway VM.

**Key points:**
- YouTube short by typecraft, transcribed 2026-11-11.
- Uses `find / -type f` to list every regular file from root.
- Uses `-exec sh -c` to run a shell command on each found file.
- Writes 10KB from `/dev/urandom` into each file via the substitution braces.
- Demonstrated in a VM, which ended up completely broken and could not be exited.
- The warning is the point: do not run it on a real machine.

**Details:** This is a short explainer, not a tool. It walks through a one-liner that starts with find at root, selects every regular file, then uses exec with sh -c to pipe 10KB of random binary data from /dev/urandom into each one through the braces substitution. The result is that every file becomes garbage, so the system stops working. The creator runs it in a VM and the VM dies, with text like "text file is busy" and no way to exit. I read about it, I did not run it, and I would say it is useful only as a warning and a reminder to check what find and exec actually do before pressing enter. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 17. Compiling Software on the Minisforum M2, M2 Pro and BOSGAME VTA-439 - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2026/11/Minisforum-M2-Pro-banner.png)
**Source:** https://www.linuxlinks.com/minisforum-m2-pro-mini-pc-running-linux-compiling-software/ · **Karakeep:** `zzapn08sy0891mbhywo8y9wr`

**In short:** LinuxLinks timed clean builds of fooyin 0.14.1 on three mini PCs; the Minisforum M2 Pro-358H was fastest at 164.96 seconds, but one application is not a buying decision.

**Key points:**
- Three machines: Minisforum M2 (Intel Core Ultra 7 356H, 16/16, 32GB DDR5-5600), M2 Pro-358H (Intel Core Ultra X7 358H, 16/16, 32GB LPDDR5X-7467), and BOSGAME VTA-439 (AMD Ryzen AI 9 HX 470, 12/24, 64GB DDR5-5600).
- All ran CachyOS and built fooyin 0.14.1 with CMake and Ninja, using the performance CPU governor, three clean builds each, with download and initial configuration time excluded.
- Average compile times were 164.96 seconds for the M2 Pro-358H, 181.55 seconds for the BOSGAME VTA-439, and 184.80 seconds for the M2.
- The M2 Pro-358H finished about 9% sooner than the BOSGAME, reversing the author's earlier CPU benchmarks where the Ryzen AI 9 HX 470 beat the Core Ultra X7 358H.
- The M2 Pro's memory has a roughly 33% higher nominal transfer rate, but the author does not isolate memory bandwidth or other factors.

**Details:** I read a LinuxLinks compile test that used fooyin 0.14.1, a highly customisable music player with a substantial codebase, as the workload on three mini PCs. The author compiled the same source with CMake and Ninja on CachyOS, with the performance CPU governor, three clean builds each, and averaged the times. The M2 Pro-358H took 164.96 seconds, the BOSGAME VTA-439 took 181.55 seconds, and the standard M2 took 184.80 seconds. So the M2 Pro is clearly quickest here, even though the Ryzen machine had more hardware threads and had won the author's earlier CPU benchmarks. The author's point is sensible: compilation mixes parallel and serial stages, so thread count alone does not decide it, and memory, cache, clock and power limits all matter. I would say the numbers are useful for comparing these boxes, but they do not settle which one is best for a developer's actual jobs. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 18. neovim-gtk - GTK4 graphical frontend for Neovim - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2023/01/Text-Editing.png)
**Source:** https://www.linuxlinks.com/neovim-gtk-gtk4-graphical-frontend-neovim/ · **Karakeep:** `b0ykvrd5czmwbuqx84a9ep08`

**In short:** neovim-gtk is a Rust GTK4 GUI for Neovim with ligatures, native clipboard, project view and a subset of vim-plug support. I would say it looks like a decent native option, but nothing for my projects.

**Key points:**
- GTK4 frontend for Neovim, forked from daa84's neovim-gtk, by Lyude Paul and contributors.
- GPL v3.0, written in Rust, runs on Linux, macOS and Windows.
- Snapshot-based GTK4 rendering replaces the original Cairo renderer; smoother window resizing.
- Font ligatures and OpenType features, guifont in ginit.vim, native GTK clipboard.
- Graphical completion popup, external tabline and command line toggles, Project View for recent files and bookmarks.
- Graphical plugin manager supports a subset of vim-plug options; async UI requests and coalesced redraws.

**Details:** It keeps Neovim's modal editing, configuration and extensibility, but wraps it in a conventional GTK desktop app. Configuration comes through Neovim settings plus GUI-specific commands, and the GUI can toggle the external tabline and command line. The feature list is long: ligatures, OpenType font features, guifont, cursor blinking, decorations, transparency, dark theme, sidebar and project view controls. The plugin manager only covers a subset of vim-plug, so I would not assume full compatibility. It is free and open source, and the article lists plenty of other Neovim GUIs alongside it, including Neovide and GNvim. For me, an editor GUI does not connect to the homelab, image pipeline or guitar project, so I am leaving it alone.

**For my projects:** Nothing for my projects.

## 19. VoidStation - Void Linux-based distribution for home entertainment - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2024/04/Linux-Distributions.png)
**Project:** [VoidStation](https://voidstation.de/en/)
**Source:** https://www.linuxlinks.com/voidstation-void-linux-based-distribution-home-entertainment/ · **Karakeep:** `f0rtse5rfhnpad2fv07qy0vb`

**In short:** VoidStation is a Void Linux-based distro that turns a PC into a sofa-friendly home entertainment and gaming box. I would say it is a neat niche project, but it is not a fit for my stuff.

**Key points:**
- Void Linux-based distribution for home entertainment
- Tile-based interface inspired by Windows 8
- Uses Openbox with the XLibre display server and Qt 6
- Supports live TV, internet radio, YouTube, streaming services and local media
- Gaming support includes Steam, Proton-GE, emulators and Moonlight
- Active project; desktop Openbox; init runit; package management XBPS; rolling release; platforms x86_64 and experimental i686; developer Panther92

**Details:** VoidStation is a Void Linux spin aimed at turning a PC into a living-room entertainment box. It has a tile-based, Windows 8-style interface built with Qt 6 on Openbox and XLibre, and it can be driven by gamepad, remote, mouse or keyboard. It pulls in live TV, internet radio, YouTube, streaming services and local media, with a sofa-friendly player doing hardware-accelerated decode, subtitles and audio track selection. Gaming is there too: Steam, Proton-GE, emulators and Moonlight streaming. There is an AppCenter for installing and removing apps graphically. The project is active, rolling, uses runit and XBPS, and targets x86_64 with experimental i686. I would say it is a tidy niche distro, but it is a whole desktop OS, not something I would slot into my homelab or image setup. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 20. 9 Best Free and Open Source Linux Script Writing Tools - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2018/12/storytelling-text-title-film-slate-screenwriting-concept.jpg)
**Source:** https://www.linuxlinks.com/scriptwriting/ · **Karakeep:** `sjuzkawih22ekl2lya9vrovp`

**In short:** LinuxLinks rounds up nine free and open source Linux script writing tools, with its strongest recommendations going to Manuskript and Trelby. I would say it is a formatting list, not a writing coach, and nothing for my projects.

**Key points:**
- Roundup of nine free and open source Linux script writing programs.
- Strongest recommendations: Manuskript and Trelby.
- The list includes Trelby, Manuskript, Screenwriter-mode, Screenplain, LyX, Afterwriting, Story Architect, obsidian-fountain and lottie.
- The tools focus on presenting text in an appropriate format, not on writing judgement.
- Commercial heavyweights named for context: Final Draft, Movie Magic Screenwriters, Celtx and Fade In.
- LyX is described as a LaTeX-based document processor with a Hollywood document class.

**Details:** LinuxLinks has put together a roundup of nine free and open source Linux tools for script writing. The list includes Trelby, Manuskript, Screenwriter-mode, Screenplain, LyX, Afterwriting, Story Architect, obsidian-fountain and lottie. The site gives its strongest recommendations to Manuskript and Trelby, and says the rating is only about script writing ability. LyX is described as an awesome document processor based on LaTeX, with a Hollywood document class for scripts. The article also notes that commercial heavyweights such as Final Draft, Movie Magic Screenwriters, Celtx and Fade In are industry standard, but they are commercial software. The point of these tools is formatting, not judging cliches or rhythm. So for a Linux user who wants screenplay formatting without paying, there are credible alternatives. Nothing for my projects.

**For my projects:** Nothing for my projects.

**Projects:**
- [Trelby](https://www.trelby.org/): The free, multiplatform, feature-rich screenwriting program!
- [Manuskript](https://www.theologeek.ch/manuskript/): Open-source tool for writers.
- [Screenwriter-mode](https://www.nongnu.org/screenwriter/): Motion Picture Fundamentals.
- [Screenplain](https://github.com/vilcans/screenplain): Write your screenplay in plain text and run it through this program to make it look good - vilcans/screenplain.
- [LyX](https://www.lyx.org/): What-you-see-is-what-you-mean document processor — a graphical front-end to LaTeX
- [Afterwriting](https://github.com/ifrost/afterwriting-labs): Post-processing for Fountain screenplays. Contribute to ifrost/afterwriting-labs development by creating an account on GitHub.
- [Story Architect](https://github.com/story-apps/starc): Reinventing the screenwriting software. Contribute to story-apps/starc development by creating an account on GitHub.
- [obsidian-fountain](https://github.com/chuangcaleb/obsidian-fountain-editor): Obsidian plugin for Fountain screenplay syntax formatting. - chuangcaleb/obsidian-fountain-editor.
- [lottie](https://github.com/coignard/lottie)

## 21. UDPipe - trainable natural language processing pipeline - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2019/10/nlp-natural-language-processing-cognitive-computing-technology-concept.jpg)
**Project:** [UDPipe](https://github.com/ufal/udpipe)
**Source:** https://www.linuxlinks.com/udpipe-trainable-natural-language-processing-pipeline/ · **Karakeep:** `niuos9iytf8lzelh9v6zgzui`

**In short:** UDPipe is a trainable C++ NLP pipeline for tokenisation, tagging, lemmatisation and dependency parsing, from Charles University's Institute of Formal and Applied Linguistics. I would say it is a solid research tool, but nothing for my projects.

**Key points:**
- Combines tokenisation, part-of-speech tagging, lemmatisation and dependency parsing into one pipeline.
- Language-independent; trains from CoNLL-U annotated data and supports Universal Dependencies treebanks.
- Pretrained models for a wide range of languages, plus custom model training.
- Interfaces for C++, Python, Perl, Java and C#, plus a REST web service.
- Runs on Linux, macOS and Windows under the Mozilla Public License v2.0.
- Developer: Institute of Formal and Applied Linguistics, Charles University.

**Details:** UDPipe is aimed at computational linguistics research, corpus annotation and grammatical analysis of written text. It can take raw text through a trained model, or work on partially annotated data when only some stages are needed. Automatic tokenisation and sentence segmentation come first, then tagging, lemmatisation and dependency parsing. It also works with existing tokenisation or annotations. For my homelab and image work, I do not see a real fit: it is not a service I would run in k3s, and there is no obvious backup or metrics story. So yeah, that's that.

**For my projects:** Nothing for my projects.

## 22. 13 Best Free and Open Source Console Based Network ‘top’ Tools - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2020/10/utility-tool.jpg)
**Source:** https://www.linuxlinks.com/networktools/ · **Karakeep:** `ur7ix4gjmh0456v1z7i2nt7w`

**In short:** LinuxLinks rounds up 13 free and open source console tools that show network usage in a top-like way. It is a handy catalogue of names, but it does not test or rank them for my setup.

**Key points:**
- Roundup of 13 free and open source console or terminal network monitoring tools for Linux.
- The one-line descriptions cover process, connection, host, interface, packet and RDMA views.
- Examples include NetHogs, bandwhich, iftop, bmon, vnStat, RustNet, socktop and ntap.
- The list mixes real-time style monitors with vnStat for long-term network traffic statistics.
- The page gives no versions, licence names beyond free and open source, or benchmark numbers.
- Published 11 November 2026 by Steve Emms on LinuxLinks.

**Details:** This is a short roundup, not a hands-on test. It starts from the point that top only covers processes, then lists small terminal utilities that borrow the real-time idea for network activity. The names span process, connection, host, interface, packet and RDMA views, plus one remote system monitor and one long-term stats tool. I read it as a map of what exists. It does not say which tool is stable, how much overhead it adds, or whether it exports metrics. For homelab-2nd I would still need to check Kubernetes fit, backup and metrics before installing anything. Nothing here is an automatic fit for my projects.

**For my projects:** Nothing for my projects.

**Projects:**
- [NetHogs](https://github.com/raboof/nethogs): Linux &#39;net top&#39; tool. Contribute to raboof/nethogs development by creating an account on GitHub.
- [bandwhich](https://github.com/imsnif/bandwhich): Terminal bandwidth utilization tool. Contribute to imsnif/bandwhich development by creating an account on GitHub.
- [NetWatch](https://github.com/matthart1983/netwatch): Network diagnostics in your terminal. Inspect traffic, connections and network behaviour. Built with Rust. - matthart1983/netwatch.
- [IPTraf-ng](https://infrastructure.fedoraproject.org/infra/hosted-content/iptraf-ng//iptraf-ng/): Index of /infra/hosted-content/iptraf-ng/iptraf-ng.
- [RustNet](https://github.com/domcyrus/rustnet): Per-process network monitoring for your terminal with deep packet inspection. Cross-platform, sandboxed. - domcyrus/rustnet.
- [vnStat](https://github.com/vergoh/vnstat): VnStat - a network traffic monitor for Linux and BSD - vergoh/vnstat.
- [netshow](https://github.com/taylorwilsdon/netshow): Lightweight, performant interactive network connection monitor with friendly service names - taylorwilsdon/netshow.
- [iftop](https://pdw.ex-parrot.com/iftop/): Iftop: display bandwidth usage on an interface.
- [socktop](https://github.com/jasonwitty/socktop): A TUI-first remote system monitor. Contribute to jasonwitty/socktop development by creating an account on GitHub.
- [Flow](https://github.com/jliljebl/flowblade): Video Editor for Linux. Contribute to jliljebl/flowblade development by creating an account on GitHub.
- [bmon](https://github.com/Jafaral/bmon): Bandwidth monitor and rate estimator. Contribute to Jafaral/bmon development by creating an account on GitHub.
- [rdmatop](https://github.com/uccl-project/rdmatop): Htop-like TUI for real-time RDMA network monitoring. - uccl-project/rdmatop.
- [ntap](https://github.com/shellrow/ntap): Network traffic monitor/analyzer, with TUI. Written in Rust. - shellrow/ntap.

## 23. ChatGPT Plus for veterans and servicemembers, by link
![](https://openai.com/favicon.ico)
**Source:** https://openai.com/index/chatgpt-plus-for-veterans/ · **Karakeep:** `ox2q7fsj6951y5i981n6f4g3`

**In short:** ChatGPT Plus for veterans and servicemembers is an OpenAI announcement I could not read past the title. I would say it is unverified until the terms show up.

**Key points:**
- The title is "ChatGPT Plus for veterans and servicemembers".
- The source is an OpenAI article.
- No article body was available.
- No candidate links were supplied.
- No pricing, eligibility, verification or rollout details are available from this.

**Details:** I only have the title here, and the body did not load. OpenAI is selling ChatGPT Plus to veterans and servicemembers in some form, but from this I cannot tell whether it is a discount, a free plan, a separate product, or who qualifies. That is the bit that matters. OpenAI likes an access headline, so I would want the actual terms before calling it good. Nothing for my projects. I would leave it at: unverified until the article loads.

**For my projects:** Nothing for my projects.

## 24. Nitrite - embedded document database - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2019/03/online-business-database.jpg)
**Project:** [Nitrite](https://github.com/nitrite/nitrite-java)
**Source:** https://www.linuxlinks.com/nitrite-embedded-document-database/ · **Karakeep:** `fc827ebt5apqsycm3smr0qii`

**In short:** Nitrite is an embedded Java NoSQL database for documents and application objects, with MVStore or RocksDB storage, transactions and schema migration. I would say it is useful for small local apps, but nothing for my projects.

**Key points:**
- Embedded NoSQL database for documents and application objects, with in-memory or file-based storage.
- Storage engines include MVStore and RocksDB; queries filter on stored values with indexing and full-text search.
- Transactions and schema migration are included, along with encryption support.
- Kotlin extensions and Android compatibility are listed; it is written in Java under Apache License 2.0.
- Developer is Anindya Chatterjee.

**Details:** Nitrite is an embedded document database, so the application carries the storage instead of talking to a separate server. It stores schemaless document collections and can persist application objects directly. There are two approaches to managing information: document collections and object repositories. Storage can be in memory or on disk, and the modular backends include MVStore and RocksDB. Queries filter on stored values, with indexing and full-text search, and there is transaction support plus schema migration. Encryption and Kotlin extensions are listed too, along with Android compatibility. It is free and open source under Apache License 2.0, written in Java, and developed by Anindya Chatterjee.

For me, the lack of a standalone server and backup story is the problem. My homelab is built around Postgres on CloudNativePG with backups and WAL to MinIO, and an embedded Java database would need a Kubernetes path, metrics and a restore plan before it got anywhere near it. Nothing for my projects. I would say it is worth a look for a small desktop or mobile app, but not worth it for my setup.

**For my projects:** Nothing for my projects.

## 25. Running 35B MoE models from SSD on consumer hardware, by Open-source Projects
![](https://opengraph.githubassets.com/1/edge0-ai/edge0)
**Project:** [edge0](https://github.com/edge0-ai/edge0)
**Source:** https://www.opensourceprojects.dev/post/edge0 · **Karakeep:** `xzpehc7xmr3t80zk9e2uuhdh`

**In short:** edge0 is an open-source streaming MoE inference framework that runs a 35B model from SSD on consumer hardware, with a prerouter and Recover-LoRA. I would say it is clever and worth reading, but it is still a tradeoff-heavy local path, not a GPU replacement.

**Key points:**
- edge0-infer is a unified GGML-based native C++ engine and API for macOS, iOS, Android and Windows, with a CLI, OpenAI-compatible local server and chat app examples.
- The first release supports edge0-35b; edge0-8b is planned for a later release.
- Models are on Hugging Face and ModelScope; the project is Apache 2.0 licensed.
- The README claims up to +59% decode throughput from trained routing prediction, with gains growing with storage latency, model size and routed width K.
- The technical report is on arXiv: 'The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction.'

**Details:** edge0 streams expert weights from SSD instead of keeping every expert in memory, so peak memory tracks the active expert set rather than the full 35B parameter count. It has three parts: SSD expert offload, a prerouter that predicts routing one step ahead, and Recover-LoRA, which keeps the int4 base frozen while training LoRA adapters by distillation from an FP teacher. The November 2026 release replaced the earlier Python framework and per-platform engines with edge0-infer on GGML, so one C++ engine runs across macOS, iOS, Android and Windows.

The honest bit is the tradeoff. You still pay storage latency, quantized weights and an active-set bound, and the 8B tier is not in this first release. The OpenAI-compatible local server is useful because existing tooling can talk to it without changes. I would say it is a credible published path to models that would otherwise be out of reach on a laptop, but not a drop-in GPU cluster replacement.

**For my projects:** Nothing for my projects.

## 26. A Rust full-stack framework that skips the wasm bundle and client build step, by Open-source Projects
![](https://opengraph.githubassets.com/1/tokio-rs/topcoat)
**Project:** [topcoat](https://github.com/tokio-rs/topcoat)
**Source:** https://www.opensourceprojects.dev/post/topcoat · **Karakeep:** `u8flyx7ejxbvmz0oe8psdefx`

**In short:** Topcoat is a Rust full-stack framework from tokio-rs that renders on the server and compiles small $(...) expressions to JavaScript, so there is no wasm bundle or client build step. It looks clever, but it is experimental, so I would not put anything important on it yet.

**Key points:**
- From the tokio-rs organization; MIT licensed; published as a crate on crates.io with docs on docs.rs.
- Components are async Rust functions that can query the database directly, with no separate API layer mentioned.
- A $(...) expression is type-checked Rust evaluated on the server for the initial render and translated to JavaScript for the browser.
- A #[shard] component re-renders on the server when its $(...) arguments change, then swaps in the new HTML.
- The README says it is early-stage and experimental, with breaking changes expected.

**Details:** Topcoat is the tokio-rs take on full-stack Rust without the wasm part. You write components as async Rust functions, they render on the server, and they can hit the database directly, so there is no separate API layer to maintain. The interactive bits are the interesting part: a $(...) expression is ordinary Rust that Topcoat evaluates on the server for the first render and translates to JavaScript so it can run again in the browser. For anything that genuinely needs the server, like search results, you mark the component with #[shard] and it re-renders server-side and swaps the HTML in.

That is a decent split, yeah: client latency for small state changes, server rendering for the rest, and no wasm toolchain or client build step to yak-shave. The syntax sounds readable too, with a view! macro close to HTML and familiar-looking attributes.

The catch is the usual one: it is early-stage and experimental, the README is upfront about breaking changes, and the examples here are truncated. I would say it is worth a look if you are curious where full-stack Rust is heading, but not worth a production rewrite. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 27. An open-source cold outreach pipeline that runs on your Claude or ChatGPT plan, by Open-source Projects
![](https://opengraph.githubassets.com/1/ethanplusai/sellbird)
**Project:** [sellbird](https://github.com/ethanplusai/sellbird)
**Source:** https://www.opensourceprojects.dev/post/sellbird · **Karakeep:** `hbvpkx57tmko3r45ubqobtvp`

**In short:** Sellbird is an AGPL-3.0 Python 3.11+ cold outreach pipeline that runs discovery through replies on your own machine using a Claude or ChatGPT plan, with approval before anything is sent. I would say it is a reasonable option for developers who want to own outreach data, but it is early and the README is the source of truth.

**Key points:**
- Python 3.11+ project, AGPL-3.0 licensed, runs locally on your Claude or ChatGPT plan.
- Pipeline covers discovery, signal reading, enrichment, verification, writing, sending and replies, with nothing sent until you approve it.
- Paid discovery searches show their cost before they run; website signal reading costs no model calls.
- Addresses are marked verified, risky, guess or invalid, and only deliverable ones are sent to.
- You can stop at any stage and export a CSV; the project was formerly called Harvey.
- Hosted version at sellbird.ai is in early access, with sending domains, inboxes and warmup handled.

**Details:** Sellbird handles the full cold outreach arc on your own machine: finding businesses, reading their websites for confirmed buying signals, finding up to two owners or managers per company, learning the email pattern and checking one address, writing a short sequence, sending from your own mailbox, and handling replies. Discovery can use free OpenStreetMap or a paid source with the cost shown first. The signal-reading step makes no model calls, so the expensive work stays in writing and replies. Approval is the default, and addresses are labelled verified, risky, guess or invalid. You can stop anywhere and run sellbird export for a CSV. The README install section was truncated in the source, so the repo is the place to check exact setup. It is best suited to developers and small teams comfortable running Python locally. Nothing for my projects: it is outreach software, and none of my projects need that.

**For my projects:** Nothing for my projects.

## 28. 186 animated React icons built with motion, free to copy, by Open-source Projects
![](https://opengraph.githubassets.com/1/itshover/itshover)
**Project:** [itshover.com](https://itshover.com/r/[icon-name), also [itshover](https://github.com/itshover/itshover)
**Source:** https://www.opensourceprojects.dev/post/itshover · **Karakeep:** `nmsqe4rua3kbbsaet964mqqw`

**In short:** Its Hover is 186 animated React icons built with motion/react, free to copy. I would say it is useful for React teams, but the licence note needs checking and it is not for my projects.

**Key points:**
- 186 animated React icons, each animating on hover via motion/react
- Covers UI essentials, social and tech logos, actions, currencies and status icons
- Built on Next.js 16, React 18+, motion/react, Tailwind CSS 4 and shadcn/ui
- Copy-the-source model: take one component into your own icons directory, or use the shadcn registry
- README mentions MIT but links to Apache 2.0 in the licence section, so check the actual LICENSE file
- Full set browsable at itshover.com/icons; repo at github.com/itshover/itshover

**Details:** The licence line is the first caveat: the README mentions MIT but links to Apache 2.0 in the licence section, so I would check the actual LICENSE file before relying on it. Beyond that, Its Hover is a set of 186 animated React icons built with motion/react, with each icon animating on hover as a drop-in React component. The collection covers UI essentials, social and tech logos, actions, currencies and status icons, and the project is built on Next.js 16, React 18+, motion/react, Tailwind CSS 4 and shadcn/ui.

The copy-the-source model is the sensible part: you take the one icon you need, put it in your own icons directory, and change stroke width, colours or timing yourself. shadcn users can also pull icons through the registry. I would say it is useful for React and Next.js teams that care about hover feedback. Nothing for my projects: my homelab is Kubernetes and Flux, and my image work is local ComfyUI, so animated web icons do not fit either.

**For my projects:** Nothing for my projects.

## 29. A native macOS YouTube Music client with a system-wide equalizer, by Open-source Projects
![](https://opengraph.githubassets.com/1/sozercan/kaset)
**Project:** [kaset](https://github.com/sozercan/kaset)
**Source:** https://www.opensourceprojects.dev/post/kaset · **Karakeep:** `hbd21pf09sud285yofwdz49c`

**In short:** Kaset is a native macOS client for YouTube Music and YouTube with a 6-band equalizer and deep macOS integration; it looks useful for Mac users, but it is WebKit-based and needs Premium plus a source build.

**Key points:**
- Native macOS client for YouTube Music and YouTube, built in Swift and SwiftUI, with WebKit handling playback.
- 6-band parametric equalizer with Spotify-style presets, applied to WebKit playback output.
- Smart Shuffle blends suggested tracks into the queue with configurable cadence and queue-ahead count.
- macOS integration includes Now Playing, media keys, Dock menu, Force Touch, share sheet, and keyboard shortcuts.
- WebKit extensions include uBlock Origin Lite and SponsorBlock, plus automation hooks for URLs, Shortcuts, Spotlight, and AppleScript.
- Plain and synced lyrics, on-device AI features on macOS 26+, 18 languages, source build in Xcode, and Premium needed for full playback.

**Details:** Kaset is a native macOS frontend for YouTube Music and YouTube, built in Swift and SwiftUI, with WebKit doing the actual playback. The catch is that it is macOS only, comes through the repo with a source build in Xcode, and full YouTube Music playback needs a Premium account. The equalizer is the headline: a 6-band parametric EQ with Spotify-style presets, applied to WebKit playback output, so it is not routing every app on the system. Smart Shuffle blends suggested tracks into the queue with a configurable cadence and number queued ahead. macOS integration is strong: Now Playing, media keys, Dock menu, Force Touch, the share sheet, and keyboard shortcuts. Extensions run through WebKit, including uBlock Origin Lite and SponsorBlock, and automation hooks cover kaset://play?v=VIDEO_ID, Shortcuts, Spotlight, and AppleScript. Lyrics come plain and synced, with AI explanations and mood analysis on macOS 26 and later via Apple Intelligence. It is localised into 18 languages. I would say it is a solid wrapper for Mac users who live in YouTube Music, but it is still WebKit under the hood.

**For my projects:** Nothing for my projects.

## 30. A MobileGestalt editor for iOS 27, with backups and field-level control, by Open-source Projects
![](https://opengraph.githubassets.com/1/huamidev/gestaltx)
**Project:** [gestaltx](https://github.com/huamidev/gestaltx), also [GestaltX](https://github.com/huamidev/GestaltX)
**Source:** https://www.opensourceprojects.dev/post/gestaltx · **Karakeep:** `dvgqqeo6ujy7pp298qfxgh8f`

**In short:** GestaltX is an iOS 27 MobileGestalt editor with presets, field-level editing, automatic backups and staged review; useful only if you already sideload iOS apps, and it does nothing for my projects.

**Key points:**
- iOS and iPadOS 27.x only for on-device MobileGestalt access; iOS 26.x is explicitly unsupported, while local plist editing still works.
- SwiftUI app edits MobileGestalt capability flags, with presets for display, device, iPad, Apple Intelligence and advanced/internal flags.
- Field editor reads, searches, adds, edits and removes CacheExtra fields, imports and exports local plists, and supports String, Integer, Real, Boolean, Data, Date, Array and Dictionary values.
- Automatic initial backup before device editing, another backup before every write, original values and types recorded, and revert restores originals or removes originally absent keys.
- Changes go through staged before/after review, writes are verified, and the README is explicit that presets only modify flags and effects depend on device and OS.
- Signing requires a certificate and provisioning profile with at least one usable App Group, with the app and embedded share extension signed using a common App Group.

**Details:** GestaltX is a SwiftUI editor for iOS and iPadOS 27.x that touches MobileGestalt, the store holding device capability flags. It has grouped presets for display, device, iPad and Apple Intelligence flags, plus an advanced section and an internal storage view. The field editor is the better part: read, search, add, edit and remove CacheExtra fields, import and export local plists, with String, Integer, Real, Boolean, Data, Date, Array and Dictionary values. Backups are taken automatically before device editing and before every write, with original values and types recorded; reverting restores them and removes keys that were absent. Changes are reviewed before writing and writes are verified. It is honest that presets only modify flags, and yeah, actual effects depend on device and OS. Signing needs a certificate and provisioning profile with an App Group, plus the embedded share extension. The iOS 27-only line is clear, so 26.x users can skip it. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 31. Keeping coding agents from defaulting to legacy web patterns, by Open-source Projects
![](https://opengraph.githubassets.com/1/googlechrome/modern-web-guidance)
**Project:** [modern-web-guidance](https://github.com/GoogleChrome/modern-web-guidance)
**Source:** https://www.opensourceprojects.dev/post/modern-web-guidance · **Karakeep:** `eq6a8asn4kupq8g428i539p4`

**In short:** Modern Web Guidance is a multi-vendor CLI that feeds coding agents curated web platform knowledge, with search, retrieve and legacy-scan commands. I would say it is worth a look if your agent keeps reaching for JavaScript and libraries where CSS or platform APIs would do.

**Key points:**
- CLI runs through npx; commands include install, search, retrieve and legacy-scan.
- Stewarded by Google Chrome, Microsoft Edge, Mozilla Firefox, MDN teams and the web development community.
- Guides are token-efficient, pruned by evals for content models already know.
- Covers View Transitions, animations, container queries, subgrid, oklch, text-wrap and line-height trimming.
- Prioritises modern browser APIs, performance, accessibility and lightweight fallbacks.

**Details:** Modern Web Guidance is a set of skills that puts web platform knowledge into a coding agent's context. The idea is plain: LLM training data is full of older code, so agents default to legacy patterns even when the platform has a native answer. The project comes from Google Chrome, Microsoft Edge, Mozilla Firefox, MDN and the wider community, which is a decent signal that it is not one browser's wishlist.

The CLI is the practical bit. You can run npx modern-web-guidance@latest install, or try search, retrieve and legacy-scan without committing to it. The guides are pruned with evals so the context is targeted rather than bloated. Coverage is specific: View Transitions, entry and exit animations, parallax scroll, scrollbar-color, container queries, subgrid, oklch, text-wrap and line-height trimming.

I would say legacy-scan is the useful bit, because it gives you a quick audit before you trust the guidance. It will not write your code for you; it just flags patterns worth modernising.

**For my projects:** Nothing for my projects.

## 32. l8w8jwt GUI - graphical JSON Web Token utility - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2023/08/people-holding-cloud-network-security-symbols.jpg)
**Project:** [l8w8jwt GUI](https://codeberg.org/GlitchedPolygons/l8w8jwtgui)
**Source:** https://www.linuxlinks.com/l8w8jwt-gui-graphical-json-web-token-utility/ · **Karakeep:** `uu807ji92yv2eky8kmmy4ats`

**In short:** l8w8jwt GUI is a desktop tool for creating, signing, decoding and verifying JSON Web Tokens, published on Codeberg by Glitched Polygons. I would say it looks useful for token debugging, but it is nothing for my projects.

**Key points:**
- Graphical front end to the l8w8jwt library for creating, signing, decoding and verifying JWTs without writing code or using the CLI.
- Supports HS256, HS384 and HS512; RS256, RS384, RS512, PS256, PS384 and PS512; ES256, ES384, ES512 and ES256K; plus EdDSA with Ed25519.
- Can set issuer, subject, audience, expiry and not-before timestamps, and add, edit or remove custom string, number, boolean or null claims.
- Decodes and verifies existing tokens with a supplied key, and generates RSA, elliptic curve and Ed25519 key pairs.
- Cross-platform on Linux, macOS and Windows; written in C++ and licensed under the Apache License 2.0.

**Details:** It is a graphical front end to the l8w8jwt cryptographic library, so you can build and check JWTs without writing application code or using command-line tools. The feature list is solid: HMAC, RSA, elliptic curve and EdDSA signing, standard claims, expiry and not-before controls, custom claims, key generation and password-protected keys where applicable. That is a lot of token machinery in one window, and it runs on Linux, macOS and Windows under the Apache 2.0 licence.

The article reads like a product page more than a review, and it gives no version number, so I cannot tell how mature it is. For me, JWT debugging is an occasional task, and a desktop GUI is not something I would keep around unless it saved real time. There is no Kubernetes path, backup story or metrics angle here, so nothing for my projects.

**For my projects:** Nothing for my projects.

## 33. AMD Epyc Venice, Zen 6 + Zen 6c Explained, by Craft Computing
![](https://i.ytimg.com/vi/vdxqhLPYC28/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=vdxqhLPYC28 · **Karakeep:** `axqbn70kt8wgpo5vi5f5jgjq`

**In short:** AMD's Epyc Venice brings Zen 6 and Zen 6c server CPUs with denser CCDs, faster memory and PCIe 6.0, and Jeff's verdict is that AMD is well ahead in data centre CPU compute. I would say it is impressive silicon, but it is not for my desk.

**Key points:**
- Launched 10 November 2026; Zen 6 standard CCDs now have 12 cores and 24 threads with 48 MB L3, up from 8 cores and 32 MB.
- Zen 6c chiplets reach 32 cores and 64 threads with 128 MB L3, and a top Zen 6c CPU has 256 cores and 1 GB L3.
- SP7 gives 16 DDR5 channels per socket, up to 1.6 TB/s with MRDIMM, plus PCIe 6.0 as standard.
- Boost clocks rise to 5.3 GHz on Zen 6 and 4.1 GHz on Zen 6c, on TSMC 2 nm.
- Top dual-socket Zen 6c systems reach 512 cores, and a 1U example holds 1,024 cores.
- Consumer Ryzen timing is vague; Jeff bets a Zen 6 X3D lands around the second half of 2027.

**Details:** The catch for me is that this is data centre hardware, and AMD laughed when asked about home lab use. Nothing announced goes past 8 CCDs per package, so the 96-core Zen 6 top end is the stated limit for now. Consumer parts are still vague too, so the Ryzen timing is a guess rather than a plan, and Zen 6 X3D is only Jeff's bet for the second half of 2027.

On the plus side, Zen 6 packs 12 cores per CCD and Zen 6c packs 32, with 4 MB L3 per core in both cases. Memory bandwidth is the headline for me: 1.6 TB/s per socket on MRDIMM, which that's huge, and PCIe 6.0 is standard. AMD also moved from a PCB backplane to advanced packaging, and that should cut CCD latency. AVX512 now allows four 256-bit instructions per cycle, and FP16 is native instead of converted.

Jeff says AMD extends its lead over Intel and Nvidia in data centre CPU compute, and it is not even close. Initial feedback from the deep dive is that the unified architecture and single NUMA design per socket matter as much as the core counts. I would say it is impressive work, but my homelab does not need 256 cores. So yeah, that's that.

**For my projects:** Nothing for my projects.

## 34. Attention Required! | Cloudflare, by Cloudflare
![](https://9to5linux.com/favicon.ico)
**Source:** https://9to5linux.com/linuxs-exfat-progs-1-4-4-adds-optional-i-o-statistics-collection-for-profiling · **Karakeep:** `nwyz0t1vt2oq1it05zaq8usm`

**In short:** Exfatprogs 1.4.4 is the Linux exFAT userspace toolset, and this release is mostly profiling and mkfs/fsck cleanup. I would say it is useful plumbing, not something I am chasing.

**Key points:**
- Exfatprogs 1.4.4 is the fourth minor release in the 1.4 series, three months after 1.4.3.
- New optional I/O statistics collection profiles read, write, discard, zero-out and sync operations.
- mkfs.exfat gains faster full formatting via BLKZEROOUT, larger zeroing batches and less page-cache pollution with POSIX_FADV_NOREUSE.
- fsck.exfat fixes arithmetic overflows and out-of-bounds reads on malformed boot sector geometry and now stops immediately on I/O errors.
- The project aims for Windows-exFAT-level performance and quality; installing from distro stable repos is recommended.

**Details:** Exfatprogs is the official userspace set for creating, fixing and debugging exFAT filesystems on Linux, and 1.4.4 is a maintenance-heavy release with one profiling feature added. The new optional I/O statistics collection covers read, write, discard, zero-out and sync operations, so it is the sort of thing I would only care about when tuning a slow exFAT drive.

mkfs.exfat gets the practical improvements: faster full formatting through BLKZEROOUT, larger zeroing batches, better quiet and trace progress output, and less page-cache pollution where POSIX_FADV_NOREUSE is supported. It also avoids memory-reservation failures on very large allocation bitmaps and marks used-cluster percentage as unknown until calculated.

fsck.exfat got the most fixes, including rejecting malformed boot sector geometry to avoid overflows and out-of-bounds reads, no version output during automatic repair, and stopping on I/O errors instead of treating them as inconsistencies. dump.exfat now prints complete timestamps and exfat2img keeps stdout metadata output clean. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 35. Gilbert + Tobin rethinks the business of law with AI, by link
![](https://openai.com/favicon.ico)
**Source:** https://openai.com/index/gilbert-tobin-sam-nickless/ · **Karakeep:** `gvo6ml5nddht8vgvv30g7m3q`

**In short:** OpenAI published a page about Gilbert + Tobin rethinking the business of law with AI. I could not read the body, so treat it as enterprise marketing rather than evidence.

**Key points:**
- Source is OpenAI, so it is selling enterprise AI rather than giving a neutral report.
- Title only: Gilbert + Tobin rethinks the business of law with AI.
- No article body and no candidate links were available to check any claim.
- No numbers, versions, prices or licences can be verified from what I have.

**Details:** OpenAI put up a page titled Gilbert + Tobin rethinks the business of law with AI. That is the whole substance I have, because the body did not load. So the honest read is thin: it is an OpenAI case study about a law firm using AI, aimed at buyers, not a technical write-up I can judge.

I would not treat it as proof of anything. Enterprise pages sell outcomes, hide the boring parts like cost, review time and failure modes, and round the numbers in the firm's favour. If there is a real lesson in there, it is behind a wall of marketing.

Nothing for my projects. My homelab work is about storage, backups and repeatable deploys, not legal workflows, and I have nothing to verify here.

**For my projects:** Nothing for my projects.

## 36. Anyone Could Route Traffic Through the White House #coding #proxy #cybersecurity, by Better Stack
![](https://i.ytimg.com/vi/JaLHbGGN4hw/maxresdefault.jpg)
**Source:** https://www.youtube.com/shorts/JaLHbGGN4hw · **Karakeep:** `rc44n3ifcta760wy8ics4g0i`

**In short:** A short explainer says residential proxies let strangers rent everyday devices, and traffic from the White House network showed up 236 times over 26 of 30 days. I would say it is a bummer, but it is mostly a cautionary tale about proxy SDKs.

**Key points:**
- Residential proxies sell access to phones and laptops so traffic looks like it comes from the device's home network.
- A proxy-tracking company saw 236 requests from the White House network from 5 October to 3 November, from six addresses across 28 proxy services.
- About half the traffic ran from 5 pm to midnight Eastern time, with almost none in the early morning.
- Badly built proxy SDKs have been used to get into internal networks; one botnet spread to at least 2 million devices through residential proxy networks.
- The same networks also reached McMurdo station in Antarctica.

**Details:** Residential proxies are sold for a few dollars and route traffic through ordinary devices, often via a proxy SDK hidden in an app. The explainer says a company tracking these proxies found traffic leaving the network registered to the executive office of the president, 236 times from six addresses over 26 of 30 days, through 28 separate services. The timing points to one person on that network late into the evening rather than guest Wi-Fi. Proxy SDKs have been used to get into internal networks before, and one botnet reached at least 2 million devices through residential proxy networks. McMurdo station in Antarctica also showed up. For my homelab this is a warning about outbound connections and SDKs. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 37. MongoBench - desktop MongoDB administration client - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2025/08/031-cloud-data.png)
**Project:** [MongoBench](https://github.com/ByteExceptionM/MongoBench)
**Source:** https://www.linuxlinks.com/mongobench-desktop-mongodb-administration-client/ · **Karakeep:** `ghlivo9mrra7cemtwtkxxgpn`

**In short:** MongoBench is a free MIT TypeScript desktop client for MongoDB with multiple connections, query tabs, BSON-safe edits and monitoring. I would say it looks like a quite good job for desktop Mongo work, but there is nothing for my projects.

**Key points:**
- Desktop MongoDB client by Marcel Noufal, written in TypeScript, MIT licensed, runs on Linux and Windows.
- Multiple simultaneous connections with independent pools, tabbed query editors, schema-aware autocompletion.
- Graphical document editing that preserves BSON types such as ObjectId, Decimal128, Int64, dates and UUIDs, plus optimistic concurrency checks.
- SSH tunnelling with private key, password or SSH-agent auth, and Cloudflare Access tunnelling.
- Index management, user and role management, live monitoring, and query tabs that retain drafts, cursor position and undo history.

**Details:** MongoBench is a desktop MongoDB administration client from Marcel Noufal, written in TypeScript and released under the MIT License, with Linux and Windows builds. It is aimed at developers and database administrators who want to explore collections, run queries and manage documents from a desktop application.

The feature list is long for a free tool: multiple connections with their own pools, tabbed editors for simple queries, aggregation pipelines and shell syntax, schema-aware autocompletion, BSON-preserving edits, optimistic concurrency checks, SSH and Cloudflare Access tunnelling, index and user management, plus live monitoring. Query tabs keep drafts, cursor position, undo history and previous results, which is the kind of small thing that matters when a query gets messy.

I would say it looks like a quite good job if you actually run MongoDB on a desktop and want a GUI. I do not run MongoDB in my homelab, so there is nothing for my projects here. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 38. Video as x86 Machine Code #badapple #retrocomputing #programming, by Better Stack
![](https://i.ytimg.com/vi/P5CbwOtBjj8/maxresdefault.jpg)
**Source:** https://www.youtube.com/shorts/P5CbwOtBjj8 · **Karakeep:** `iklaqdwv66lvikfe0cenf6i2`

**In short:** A short about getting full-motion video onto a 1981 IBM PC by turning every frame into x86 machine code; clever, and it works, but it is retrocomputing, not something for my projects.

**Key points:**
- 1981 IBM PC with a CGA graphics card and 16 KB of screen memory
- 2007 talk said full-motion video in CGA mode was impossible: about 384 KB/s of screen changes, about 240 KB/s write speed, about 90 KB/s hard drive speed
- Video at 24 fps; the encoder kept only changed parts, biggest changes first, and dropped the tiniest ones if time ran out
- About 40,000 processor cycles per frame; plain change handling used about 36% of that
- Frames are written as x86 machine code, so each frame paints its own changes into screen memory
- He played Bad Apple with sound on a 1981 IBM PC connected to a TV

**Details:** The short is about a demo scene programmer who kept thinking about the problem for seven years after a 2007 talk. The original IBM PC could only write about 240 kilobytes a second to CGA screen memory, while 24 fps video needed about 384 kilobytes of screen changes, and old hard drives managed about 90 kilobytes a second. His first fix was delta encoding: keep only the changed parts, biggest first, and drop the tiny ones if the PC ran out of time. That still left about 36% of the roughly 40,000 cycles per frame spent just deciding what to do. So the encoder writes the video as x86 machine code, and each frame paints its own changes straight into screen memory, then hands control back. He called the idea ludicrous, and it worked: Bad Apple with sound on a 1981 IBM PC hooked to a TV. Nothing for my projects.

**For my projects:** Nothing for my projects.
