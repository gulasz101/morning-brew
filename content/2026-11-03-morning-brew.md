---
date: 2026-11-03
slug: 2026-11-03-morning-brew
tags: Machine Learning, Artificial Intelligence, AI Safety, Technology, Open Source Software, Desktop Applications, Photography Tools, Linux Software, Image Gallery, Large Language Models, OpenAI, Linux, 3D Modeling, Software Tools
---

Morning Brew for 2026-11-03: 16 items written from 44 hoarded bookmarks and feeds, 28 dropped after a failed retry.

### RSS

## 1. “I don’t feel safe at Anthropic”, by Less Bitter
![](https://i.ytimg.com/vi/PR4RLsImTJg/maxresdefault.jpg)
**Source:** https://www.youtube.com/shorts/PR4RLsImTJg · **Karakeep:** `kqq0byp9luajkqf3spa4b8o9`

**In short:** A short clip of someone repeating that they do not feel safe at Anthropic, with no context or evidence beyond that. I would say it is weird and not worth treating as a safety claim.

**Key points:**
- Title is the direct quote: 'I don't feel safe at Anthropic'.
- The transcript repeats that line several times and adds 'Enthropic is bad for me'.
- A second voice asks whether 'safe' means physical or mental well-being.
- Source is listed as Less Bitter on YouTube Shorts, transcribed 2026-11-03.
- No names, roles, incidents, dates or evidence are given beyond the quoted line.
- No candidate links were supplied for this item.

**Details:** This is a very short transcript with almost no context. Someone repeats 'I don't feel safe at Anthropic', says 'Enthropic is bad for me', and asks why anyone is grasping at reasons to stay. Another voice then asks whether 'safe' means physical or mental well-being, and the clip ends there. That is the whole thing. There is no incident, no role, no date and no evidence, so I would not read it as a safety report about Anthropic. It reads more like a fragment of a conversation. For an Anthropic item, the useful part is that the safety language is being thrown around without anything behind it. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 2. OpenAI appoints Jill Hazelbaker as Chief Corporate Affairs Officer, by link
![](https://openai.com/favicon.ico)
**Source:** https://openai.com/index/jill-hazelbaker-chief-corporate-affairs-officer/ · **Karakeep:** `s1uinrzirjkxa3me2lwhk0v3`

**In short:** OpenAI announced Jill Hazelbaker as Chief Corporate Affairs Officer. I would say it is corporate news, not a tool, and nothing for my projects.

**Key points:**
- OpenAI announced Jill Hazelbaker as Chief Corporate Affairs Officer.
- The article body was not available, so responsibilities, background, start date and scope are not stated.
- No candidate links were supplied.

**Details:** OpenAI announced that Jill Hazelbaker is its Chief Corporate Affairs Officer. That is the whole fact I have, because the article body was not available and there were no candidate links to follow. I read about this, I did not try anything, and there is nothing to install or benchmark here. It is an executive appointment at a company that likes executive appointments, so I would call it corporate affairs theatre until someone shows me the actual scope, reporting line and budget. For my homelab, RiffRadar and local image work, this changes nothing. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 3. https://www.youtube.com/watch?v=k2ruCf_z75I, by Fireship
![](https://i.ytimg.com/vi/k2ruCf_z75I/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=k2ruCf_z75I · **Karakeep:** `yn6ie2vt74ngidsbihxgsq4m`

**In short:** Fireship's 3 November 2026 code report rounds up the Cursor extension backdoor, the Polymarket script hijack, the Binance theft, and a 9.8 Linux kernel bug. I would say it is grim reading, but useful if you run Linux or hold crypto.

**Key points:**
- Cursor's official Claude Code extension was live for about 11 hours and installed by around 5,000 people; its backdoor needed admin rights.
- A Debug Bear performance script used by Polymarket was hijacked, and hackers took over $2 million.
- Binance lost $6.3 billion across 10 blockchains in about 20 minutes after a DevOps laptop compromise; the FBI blamed the North Korean group Trader Trader.
- The Linux TCP bug has existed since 2016 and scored 9.8 CVSS; an unreleased Claude model got a kernel address in about 48 minutes and root in 5 more.
- Debian and Oracle patched within one day, Red Hat took two weeks, and Ubuntu still had no fix at the time.
- CodeRabbit Secure offers continuous code security checks, with a free 14-day trial and no credit card.

**Details:** The video is another security roundup, and bad news first: Cursor shipped an official Claude Code extension without knowing it, and it scanned machines for keys and tokens while opening a backdoor. It was up for about 11 hours, around 5,000 people installed it, and the backdoor needed admin rights, so the blast radius was limited. Around the same time, Polymarket users had funds drained because a Debug Bear performance script was hijacked, and the hackers got over $2 million before it was pulled.

The bigger number is Binance: about $6.3 billion across 10 blockchains left hot wallets in roughly 20 minutes after a DevOps laptop compromise, and Binance's own system signed the withdrawals. The FBI said the North Korean group Trader Trader was behind it, the same group behind the $1.5 billion Bybit theft. Tether and Circle froze about $3 billion of stolen stablecoins within an hour, Binance refilled from treasury and insurance funds, and users still withdrew $3.6 billion after proof of reserves.

The part I care about is the Linux kernel bug: since 2016, every kernel has mishandled new TCP connections, and the CVSS score is 9.8. Anthropic's red team gave it to an unreleased Claude model, which got a kernel memory address in about 48 minutes and root five minutes later. Debian and Oracle patched within a day, Red Hat took two weeks, and Ubuntu still had no fix. CodeRabbit Secure is the sponsor pitch, continuous security review with a free 14-day trial and no card.

**For my projects:**
- homelab-2nd: Add a Flux-managed CronJob or manual runbook that reports kernel versions and CVE status for the three k3s workers and the OMV box.

## 4. GPT-6 Just Fixed Another AI by Editing Its Weights! #ai #openai #llm, by Better Stack
![](https://i.ytimg.com/vi/jNuDdqEwI58/maxresdefault.jpg)
**Source:** https://www.youtube.com/shorts/jNuDdqEwI58 · **Karakeep:** `qpf6a28aobxm0h0i4ewxnu31`

**In short:** MIT researchers got GPT-6 Astra to edit another model's weights directly and lift its maths score from 7.9% to 48.1% by changing 0.016% of the weights. Clever, but it only removes a blocking bug, it does not teach the model anything new.

**Key points:**
- MIT team, paper called Sparks of Weight Space Programming, published full experiment logs in a GitHub repo named LM Understand Logs.
- GPT-6 Astra edited Qwen 3.5 0.8B by removing one direction from 64 output columns in MLP layers 15 and 19, about 131,000 weights, 0.016% of the model.
- Qwen 3.5 0.8B had 85 of its first 96 answers hit the 32,768 token limit; after the edit its Math 500 score went from 7.9% to 48.1%.
- Astra named Breakout, Pong, Pac-Man and Freeway from raw weights of four identical-architecture networks, and identified induction heads in tiny language models.
- It could not improve Gemma 3 270M, which barely loops, and could not spot sycophancy from weights alone until it saw attention patterns.

**Details:** An MIT team published research called Sparks of Weight Space Programming, where a frontier model, GPT-6 Astra, reads raw weights and edits them directly, with no gradient descent. In the headline test it took Qwen 3.5 0.8B, which gets stuck in thinking loops and hit the 32,768 token limit on 85 of its first 96 answers, traced the loop to one direction in MLP layers 15 and 19, and removed it from 64 output columns per layer. That is about 131,000 weights, 0.016% of the model, and Math 500 went from 7.9% to 48.1%. It also named four games from identical small networks and spotted induction heads in tiny language models, and even wrote a Breakout network from zero weights. The limits are the useful bit: it could not raise Gemma 3 270M's maths score because the errors were ordinary reasoning mistakes, and it could not tell which Gemma was trained to be sycophantic until it saw attention patterns. So this is a debugging trick. It does not add knowledge. I would say it is interesting for finding hidden faults before deployment, but not a replacement for training.

**For my projects:** Nothing for my projects.

## 5. 16 Useful Free and Open Source 3D Model Viewers - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2024/11/007-3d.png)
**Source:** https://www.linuxlinks.com/useful-free-open-source-3d-model-viewers/ · **Karakeep:** `ybtyk5qgrqq4chkg26huo6pw`

**In short:** LinuxLinks rounds up 16 free and open source 3D model viewers for Linux, from ParaView and MeshLab to terminal ASCII viewers. I would say it is a handy reference, and the catch is that most viewers do not cover every format.

**Key points:**
- 16 free and open source 3D model viewers, compiled by Steve Emms for LinuxLinks.
- No versions or prices are listed; only free and open source software is eligible.
- STL is the most used format for 3D printers, storing surface geometry as small triangles through tessellation.
- GUI tools include ParaView, F3D, MeshLab, Mayo, fstl, Castle Model Viewer, fstl-e, Exhibit and Tatlin.
- Terminal viewers include voxcii, dcat, Trophy, term3d and rasterminal; Online 3D Viewer and j3d are also listed.

**Details:** LinuxLinks puts sixteen viewers in one place, and the range is wide: ParaView for data analysis and visualisation, MeshLab for triangular meshes, F3D as a fast minimalist viewer, Mayo as a CAD viewer and converter, and several terminal viewers that render models as ASCII or with software rendering. That is a lot of choice, and the useful part is that it names the gap up front: there are many 3D formats and most tools do not support all of them. STL gets a plain explanation too, since it is the common 3D printing format and stores surface geometry as triangles through tessellation. I would say it is a good bookmark for "what can open this file", but I would not install the whole list. If I only need to inspect an STL before printing, a small viewer like fstl is enough; if I need mesh work, MeshLab is the one to look at. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 6. MicroCloud - automated private cloud infrastructure - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2018/01/SL-101820-36860-11.jpg)
**Project:** [microcloud](https://github.com/canonical/microcloud)
**Source:** https://www.linuxlinks.com/microcloud-automated-private-cloud-infrastructure/ · **Karakeep:** `sf27hb21b7oesw2iaqs5geig`

**In short:** MicroCloud is Canonical's LXD, MicroCeph and MicroOVN bundle for small private clouds; I read about it, and it looks capable, but it is not a fit for my Kubernetes homelab.

**Key points:**
- Developed by Canonical Ltd; licensed GNU AGPL v3.0; written in Go.
- Combines three components: LXD for VMs and system containers, MicroCeph for distributed Ceph storage, and MicroOVN for software-defined networking.
- Supports high availability, live migration of compatible VM workloads, isolated virtual networks, distributed routing, multi-site and edge deployment.
- Offers a graphical interface, command-line tools, REST API access and repeatable preseed configuration.
- Candidate link points to github.com/canonical/microcloud.

**Details:** MicroCloud is a platform for deploying and managing small private clouds. It brings LXD, MicroCeph and MicroOVN together so one cluster can run VMs and containers, keep replicated storage and provide virtual networking. The article says it automates much of the initial setup, supports live migration of compatible workloads, high availability, multi-site and edge use, and exposes a GUI, CLI and REST API. It is AGPLv3 and written in Go. I would say it is quite a complete small-cloud bundle, and the LXD, Ceph and OVN combination is the interesting part. The downside for me is that it is not my stack: my homelab is Flux-driven k3s with CloudNativePG and Cloudflare Tunnels, and the article does not mention Kubernetes, backups or metrics. So nothing for my projects. It might suit someone who wants a compact private cloud without building those pieces separately.

**For my projects:** Nothing for my projects.

## 7. REMnux - Linux distribution for malware analysis - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2024/04/Linux-Distributions.png)
**Source:** https://www.linuxlinks.com/remnux-linux-distribution-malware-analysis/ · **Karakeep:** `vjti7mt8dkm70qqw9epk1zkz`

**In short:** REMnux is an Ubuntu-based Linux distribution by Lenny Zeltser and contributors for malware analysis, reverse engineering and digital forensics. I would say it is a solid ready-made kit for analysts, but nothing for my projects.

**Key points:**
- Ubuntu-based Linux distribution for malware analysis, reverse engineering and digital forensics
- Developed by Lenny Zeltser and contributors; free and open source software
- GNOME desktop with command-line and graphical applications; usable as a workstation, in a VM, or as tools added to an existing Ubuntu install
- Feature areas include static and dynamic analysis, memory forensics, network analysis, malicious documents and scripts, system interactions and threat intelligence
- SaltStack-based configuration management and REMnux MCP server integration with AI assistants
- Working state active; release model fixed; platforms x86-64 and AArch64

**Details:** REMnux is a specialised Ubuntu-based Linux distribution for malware analysis, reverse engineering and digital forensics, built by Lenny Zeltser and contributors. It ships a GNOME desktop with command-line and graphical tools, and can run as a workstation, in a VM, or as tools added to an existing Ubuntu install. The feature list covers static and dynamic analysis, memory forensics, network analysis, malicious documents, scripts, system behaviour and threat intelligence, plus SaltStack configuration management and an MCP server for AI assistants.

Unfortunately it is another operating system to keep patched, and I do not do malware analysis. It supports two platforms, x86-64 and AArch64, which is fine, but the article gives no version number, just active status. I would say it is a solid ready-made kit for analysts, but nothing for my projects. For homelab-2nd, the missing bit is any Kubernetes path, backup story or metrics; the article describes a desktop distro, not a service. So yeah, that's that.

**For my projects:** Nothing for my projects.

## 8. LibreOffice 26.2.7 Is Out as the Last Update in the LibreOffice 26.2 Series, by Cloudflare
![](https://9to5linux.com/wp-content/uploads/2026/02/lo262.webp)
**Source:** https://9to5linux.com/libreoffice-26-2-7-is-out-as-the-last-update-in-the-libreoffice-26-2-series · **Karakeep:** `k060son35y4sbwesj74qtu7m`

**In short:** LibreOffice 26.2.7 is the last maintenance release of the 26.2 series, with 20 bug fixes and a nudge to move to 26.8.1. I would say it's a routine closer, nothing to chase.

**Key points:**
- Seventh and final maintenance update to LibreOffice 26.2, announced by The Document Foundation on November 3rd, 2026
- Addresses 20 bugs, including Web Query (.iqy) support in Calc, DOCX round-trip fixes and a Python upgrade to 3.12.16
- Fixes a startup crash on macOS 27 and restores audio playback in presentations on Windows
- LibreOffice 26.2 series supported only until November 30th, 2026, with no further maintenance updates
- Users urged to move to the LibreOffice 26.8 series, currently at 26.8.1

**Details:** LibreOffice 26.2.7 landed on November 3rd, 2026 as the seventh and last maintenance update for the 26.2 series. It comes two months after 26.2.6 and packs fixes for 20 bugs, with the notable ones being Web Query (.iqy) support in Calc, several DOCX round-trip problems, a Python bump to 3.12.16, a startup crash fix on macOS 27 and restored audio playback in presentations on Windows.

The 26.2 series itself shipped back on February 4th, 2026 with things like horizontal tabs in dialogs and clipboard screenshots of dialogs. Support runs out on November 30th, 2026, so The Document Foundation is telling everyone to get onto the 26.8 series, currently at 26.8.1. If you installed from your distro repos, wait for it to arrive there rather than grabbing the binary.

I would say it's a tidy closer rather than anything exciting. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 9. Heimstaden is changing residential real estate management with AI, by link
![](https://openai.com/favicon.ico)
**Source:** https://openai.com/index/heimstaden/ · **Karakeep:** `sjpvy3t2g4esqbt1kv9zqxa0`

**In short:** An OpenAI page about Heimstaden using AI in residential real estate management. The body was missing, so I cannot verify anything beyond the title; it reads like a customer story selling OpenAI to landlords.

**Key points:**
- OpenAI hosts the page at its index path for Heimstaden.
- The title frames it as AI changing residential real estate management.
- No article text was available, so there are no verifiable metrics, models, prices or deployment details.
- It is an enterprise case-study page, not a technical write-up I can judge.

**Details:** Heimstaden is the named customer and residential real estate management is the claimed use case. That is all the title gives me. The body did not load, so I cannot tell whether this is a chatbot, a maintenance triage tool, a leasing assistant, or a slide deck about efficiency. OpenAI customer stories usually sell the platform to other enterprises, and this one looks like that. I would say it is not worth much without the actual implementation details. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 10. SparkyOS onUSB - portable Linux distribution running from USB - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2024/04/Linux-Distributions.png)
**Project:** [sparkyos.sparkylinux.org/sparkyos.sparkylinux.org](https://sparkyos.sparkylinux.org)
**Source:** https://www.linuxlinks.com/sparkyos-onusb-portable-linux-distribution/ · **Karakeep:** `cbisma3vvnvjpw3fobv1hdeu`

**In short:** SparkyOS onUSB is a portable, fully installed Arch-based Linux that runs from a USB stick and keeps changes between sessions; I would say it is handy for carrying a familiar desktop around, but rolling Arch on removable storage is a bit wonky for daily trust.

**Key points:**
- Developed by the SparkyLinux team as an Arch-based edition, not the Debian-based SparkyLinux.
- Xfce desktop with systemd, Pacman and AUR access through Yay.
- Functions as a fully installed OS on removable storage, retaining installs, updates and files.
- Rolling release model for x86_64 only; working state is Active.
- Home page and project details are available via candidate link 1.

**Details:** SparkyOS onUSB is a fully installed operating system on removable storage, so installs, updates and personal files survive between sessions. The edition described here is Arch-based with Xfce, Pacman and Yay for the AUR, on a rolling release, for x86_64 only. That is a neat trick for carrying one working environment between machines, but my homelab wants Kubernetes paths, backups and metrics, and my image work wants local GPU control, so there is nothing for my projects here. I would call it interesting rather than essential, and I would not trust a rolling USB install as a primary daily system without a backup plan.

**For my projects:** Nothing for my projects.

## 11. Preparing our next security sprint to harden OpenAI, by link
![](https://openai.com/favicon.ico)
**Source:** https://openai.com/index/preparing-our-next-security-sprint-to-harden-openai/ · **Karakeep:** `lzo6edfugjouyv09waoez2es`

**In short:** OpenAI says it is preparing a next security sprint to harden OpenAI, and the body was not available. I would say it reads as enterprise reassurance until the details show up.

**Key points:**
- The headline says OpenAI is preparing a next security sprint to harden OpenAI.
- No article text was fetched, so scope, dates, owners, tools and success criteria are unknown.
- The supplied material contains no technical details beyond the title.

**Details:** This is one of those OpenAI posts where the headline does the work and the substance is missing. I read about it, I did not run it, and in this case I could not even read the body. What I can say is that OpenAI is framing a security sprint around hardening OpenAI itself, which is a bit circular and very enterprise. There are no versions, prices, licences or numbers in the supplied text, so I cannot judge the work from this. If it turns into a concrete report with scope and outcomes, that is when it becomes useful. For now, it is a security announcement with no detail attached. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 12. Scaling Git at OpenAI, by link
![](https://openai.com/favicon.ico)
**Source:** https://openai.com/index/scaling-git-at-openai/ · **Karakeep:** `ivxueisby5p4fma5obs1xiyg`

**In short:** OpenAI published a post called Scaling Git at OpenAI, but the body did not load, so I can only treat the title as a hint and not as evidence.

**Key points:**
- The source body was not available; only the title was usable.
- The title points to an OpenAI engineering post about scaling Git.
- No numbers, versions, prices, licence or implementation details were readable.
- No candidate links were supplied.

**Details:** I read about this, I did not run it, and in this case I could not even read the body. The title suggests OpenAI has enough Git pain to write a public post about scaling it, which is mildly interesting for anyone running GitOps, but I cannot tell whether it covers repository size, clone times, CI load, or something else. OpenAI is good at turning infrastructure work into enterprise confidence, so I would wait for the actual text before copying any lesson. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 13. A community catalog of Gridfinity baseplates, bins, and generators, by Open-source Projects
![](https://opengraph.githubassets.com/1/jeffbarr/gridfinity-catalog)
**Project:** [gridfinity-catalog](https://github.com/jeffbarr/gridfinity-catalog)
**Source:** https://www.opensourceprojects.dev/post/gridfinity-catalog · **Karakeep:** `tm85gi78mbsmadn97affv11z`

**In short:** Gridfinity Catalog is a community-maintained README that indexes Gridfinity baseplates, bins, lids, adapters and generators across several design sites. I would say it is a useful bookmark for anyone deep into Gridfinity, and nothing for my projects.

**Key points:**
- Hosted as a plain README on GitHub at github.com/jeffbarr/gridfinity-catalog; it stores no files and runs no code.
- Entries list sizes from 1x1 to 7x7, number of variants, file formats (STL, 3MF, STP, OpenSCAD, FCSTD) and date added.
- Covers baseplates, bins, lids, adapters, Stackfinity, templates, online and offline generators, and apps.
- Traces back to Zack Freedman's April 2022 Gridfinity video, building on earlier work by Alexandre Chappel, with a follow-on community video in July 2022.
- Contributions are by pull request, and entries range from 2022 into 2026 across Printables, MakerWorld, Thangs, GitHub and YouTube.

**Details:** Gridfinity is the modular drawer system where a gridded baseplate holds blocks sized for one or more cells, so shelves and drawers become modular. The catalog is an attempt to keep track of the resulting sprawl of designs across several publishing sites. It is a reference you bookmark. The catalog is the README, and you scan tables for sizes and formats that match your printer and drawer before clicking anything. The getting-started path is short: pick a baseplate, pick some boxes, print, use, share, learn about parameterisation. For anyone new, the videos at the top and the Gridfinity Master Collection on Printables are the suggested starting point. The honest caveat is that usefulness scales with contributors, and some tables will age. I would say it saves real time if you are already deep into Gridfinity, but it is not software to run.

**For my projects:** Nothing for my projects.

## 14. clj-depend - Clojure namespace dependency analyser - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2026/09/Linter-Tool-Banner1.png)
**Source:** https://www.linuxlinks.com/clj-depend-clojure-namespace-dependency-analyser/ · **Karakeep:** `hnnknakq0rtratr27ajhnf72`

**In short:** clj-depend is a Clojure namespace dependency analyser that checks whether namespaces break rules you define about architectural layers. I would say it sounds useful for a large Clojure codebase, but it has no fit for my current projects.

**Key points:**
- Analyses dependencies between Clojure namespaces and flags violations of configured restrictions.
- Supports architectural layers, regex or explicit namespace sets, circular dependency detection and same-layer controls.
- Uses declarative configuration and exposes a programmatic API.
- Runs through the Clojure CLI and has a dedicated Leiningen plugin.
- Free and open source under the Eclipse Public License v2.0; written in Clojure by Fabio Domingues.

**Details:** clj-depend checks whether Clojure namespaces depend on each other in ways that break rules you define. You can group namespaces into layers, allow controllers to reach business logic and data models, and stop lower levels from depending on controllers. It also finds circular dependencies and lets same-layer namespaces depend on each other or not.

Configuration is declarative, and there is a programmatic API, so it can sit in automated workflows rather than only being a manual check. It can restrict analysis to selected source paths, emit custom violation messages, and keep a baseline of existing violations so only new problems show up later.

It runs through the Clojure CLI and has a Leiningen plugin. The licence is Eclipse Public License v2.0 and the developer is Fabio Domingues.

I read about it, I did not try it. It sounds like a sensible architecture lint for a large Clojure codebase, but I have no Clojure project in my stack, so nothing for my projects.

**For my projects:** Nothing for my projects.

## 15. reorder-python-imports - automatically organise Python imports - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2026/09/Code-Formatter-banner2.png)
**Project:** [reorder-python-imports](https://github.com/asottile/reorder-python-imports)
**Source:** https://www.linuxlinks.com/reorder-python-imports-automatically-organise-python-imports/ · **Karakeep:** `ssufsn75mdshqk3g9jma1uln`

**In short:** reorder-python-imports is a Python CLI by Anthony Sottile that rewrites and groups imports with static analysis; I would say it is tidy but narrow, and probably not worth adding if Ruff or isort already covers your imports.

**Key points:**
- Python CLI by Anthony Sottile, MIT licensed, focused only on import statements.
- Groups imports into standard library, third-party and application-specific buckets, with alphabetical ordering.
- Splits multi-symbol imports into separate lines, removes duplicates, and can add, remove or rewrite selected imports.
- Handles compatibility imports: removes obsolete __future__ imports and rewrites selected six, mock and typing imports.
- Supports pre-commit, stdin and stdout, configurable application directories and noreorder comments.

**Details:** reorder-python-imports is a command-line utility by Anthony Sottile that rewrites Python import blocks using static analysis, so standard library, third-party and application imports end up in three groups, which is a sensible split. It puts regular imports before from-imports, splits multi-symbol statements into one line each, removes duplicates and orders groups alphabetically, so the file stays predictable. It can also add specified imports, remove unwanted ones, replace references to renamed modules, drop obsolete __future__ imports and rewrite selected compatibility imports from six, mock and typing-related modules. The merge-conflict argument is simple: one import per line means fewer edits touching the same line.

The catch is scope. It is an import-only formatter in a space where Ruff and isort already exist, and the page gives no benchmarks, version numbers or migration results, so the case for adding another tool is thin. Configurable application directories, pre-commit support, stdin and stdout handling and noreorder comments make it usable in real projects, and MIT licensing is sensible. I would say it is quite good at one job, yeah, but not worth it unless you specifically want its compatibility-import rewrites.

**For my projects:** Nothing for my projects.

## 16. GIMP 3.2.8 Image Editor Restores Support for Offset as a Non-Destructive Filter, by Cloudflare
![](https://9to5linux.com/wp-content/uploads/2026/11/g328.webp)
**Source:** https://9to5linux.com/gimp-3-2-8-image-editor-restores-support-for-offset-as-a-non-destructive-filter · **Karakeep:** `v3dq8y2tu3f7otuaupa4tka3`

**In short:** GIMP 3.2.8 is a maintenance release of the open-source image editor; it restores Offset as a non-destructive filter and fixes a pile of small things, so I would call it a useful tidy-up.

**Key points:**
- GIMP 3.2.8 is the fourth maintenance update in the 3.2 series, for GNU/Linux, macOS and Windows.
- It adds DPI information when copying an image to the clipboard.
- It restores Offset as a non-destructive filter.
- It lets you cancel font loading in the middle when quitting early.
- It improves Dot to Dot support on integer scaling.
- The GNU/Linux download is an AppImage bundle.

**Details:** GIMP 3.2.8 is the fourth maintenance update in the 3.2 series, and the changes are small rather than headline features. It adds DPI information when copying an image to the clipboard, restores Offset as a non-destructive filter, and lets you cancel font loading in the middle when quitting GIMP early. Dot to Dot support is improved to work better even on integer scaling, and the Text tool gets better support for RTL languages. There are also dialog positioning changes, theme leak fixes, and plugin updates such as Script-Fu Add Border taking alpha into account for fill opacity. I read this as a sensible tidy-up. It is worth taking when it reaches your distro, especially if you already use GIMP. Nothing for my projects.

**For my projects:** Nothing for my projects.
