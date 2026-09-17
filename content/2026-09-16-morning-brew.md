---
date: 2026-09-16
slug: 2026-09-16-morning-brew
tags: Backend Development,Model Context Protocol,Artificial Intelligence,Web Development,Laravel,Linux,Raspberry Pi,Mobile Computing,Android,Hardware Repurposing,Electric Vehicles,Logistics,Autonomous Vehicles,Transportation Technology,Internet Technology,Domain Names,Web Infrastructure,Top Level Domains,Coding,Software Development,Future Of Technology,Product Management,Metaverse,Technology Reviews,Productivity,Voice Coding,Coding Techniques,Technology Trends,Cloud Computing,Big Data,Software Architecture,Data Engineering,Cybersecurity,Computer Hardware,Technology News,Datacenters,Local AI,Machine Learning,Large Language Models,Cloudflare,Online Attacks,Web Security,Open Source,Code Editor,Real-Time Collaboration,Programming,Developer Community,Prompt Engineering,Model Evaluation,Natural Language Processing,Network Security,Open Source Software,Bastion Host,Session Recording,Audit Logging,Software Tutorials,V2Ray,Proxy Tools,Shadowsocks,Clash,Distributed Systems,Service Discovery,AI Agents,Transformers,Object Detection,Computer Vision,Open-Vocabulary Detection,User Interface,.NET Framework,WinForms,Python Programming,Generative AI,Automation,Developer Tools,Open Source Projects,Rule Sets,Markdown,Data Processing,Code Formatting,C# Programming,Threat Intelligence,Malware Analysis,Data Analysis,Rust Programming,Command Line Tools,Package Management,Shell Scripting,Zsh,Package Manager,Data Visualization,3D Graphics,Chemistry,Periodic Table,Video Encoding,AV1,FFmpeg,Networking,Network Configuration Management,Network Automation,Linux Distribution,Operating System,Terminal Interface,Systemd,Service Management,Astronomy,Space Exploration,Linux Software,Terminal User Interface,RDMA,Network Monitoring,Terminal,Text User Interface,Clocks,File Synchronization,Cloud Storage,Self-Hosted Software,Python,Static Site Generator,Rust Programming Language,Multimedia,Video Processing,Video Editing,Media Converter,Privacy,FinTech,Data Breach
---

# Morning Brew — 2026-09-16

2026-09-16 — 39 hoarded. 3 hand-bookmarked, 7 YouTube videos (all transcribed), the rest autohoarded RSS. Hand stuff first, feed-firehose at the bottom.

### Hand-bookmarked

## 1. Laravel MCP 1.0 Is Released — by Laravel News

![Laravel News](https://laravelnews.s3.amazonaws.com/featured-images/2026-09-15-laravel-mcp-1-0.png)

**Source:** https://laravel-news.com/laravel-mcp-1-0
**Karakeep doc:** `ka7n6oakjqxzz978pqevc04r`

Laravel MCP hit 1.0, the first stable release of the package for building Model Context Protocol servers in Laravel. It targets protocol revision 2026-07-28, so you get searchable tool catalogs (keep common tools in the list, stash the rest behind `ToolSearch`), cache hints so clients know what to reuse and for how long, and stateless servers where every request carries its own protocol version. OAuth now demands PKCE and adds Client ID Metadata Documents, and old `initialize` clients still work. Upgrade notes are the usual gotcha pile: new `ValidateMcpHeaders` middleware, required `MCP-Protocol-Version`/`Mcp-Method` headers on POSTs, and a header mismatch returns HTTP 400 with error code -32020. If you're on 0.9, read the upgrade guide before you ship.

## 2. My old phone replaced my Raspberry Pi, and there's only one thing I miss — by MakeUseOf

![MakeUseOf](https://static0.makeuseofimages.com/wordpress/wp-content/uploads/wm/2026/03/native-terminal-with-system-info-on-android-pixel-9a-1.JPG?w=1600&amp;h=900&amp;fit=crop)

**Source:** https://www.makeuseof.com/old-phone-replaced-raspberry-pi-one-thing-miss/
**Karakeep doc:** `nrbrklrvb4l1f0f1prwzh894`

Author had a cracked-screen phone sitting in a drawer and decided it was a better always-on server than a Pi. Small web apps, cron jobs, file sync, dashboards, and SSH over Tailscale all run fine on Android via Termux, and it costs nothing. The catch is the obvious one: no GPIO pins, so anything needing sensors, relays, or motors still needs a real board or an ESP32 bolted on over USB. Their verdict is blunt — the Pi isn't obsolete, but when prices are sky-high in 2026, most Pi projects are just "small always-on computer" projects and a retired phone does that cheaper and tidier. The only thing they actually miss is that row of pins.

## 3. Ciężarówka bez kabiny na testach w Lidlu - wyeliminowano i kierowcę, i przewoźnika — by 40ton

![40ton](https://40ton.net/wp-content/uploads/2026/09/einride_tpod_lidl_2026_1.webp)

**Source:** https://40ton.net/ciezarowka-bez-kabiny-na-testach-w-lidlu-wyeliminowano-i-kierowce-i-przewoznika/
**Karakeep doc:** `cllhzyrg7hqwuyhbr4rlej5i`

Germany just issued its first-ever permit for a driverless truck on a public road, handed to Lidl to test the Swedish Einride T-Pod. The T-Pod is a fully electric three-axle chassis that ditches the driver's cab entirely for autopilot and remote control — 8 meters long, hauls 15 euro pallets. Lidl will run it for four months in Edermünde near Kassel, three trips a day on a measly 500-meter route from distribution center to the nearest store. The 40ton author isn't impressed by the distance but flags the real kicker: no cab means no driver *and* no carrier, since the manufacturer runs the whole transport service itself. It lines up neatly with Volvo Group's report that autonomous trucks could hand manufacturers billions by eating carriers' lunch.


### RSS — YouTube

## 4. 🎬 Video — by Brodie Robertson

![Brodie Robertson](https://i.ytimg.com/vi/0sa6EXQk1eY/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=0sa6EXQk1eY
**Karakeep doc:** `ajm3hounjfkma367l14p7jqm`

Brodie digs into the death of `.name`, the one TLD where `neil.frazier.name` and `beverly.frazier.name` are two *separately registered* domains, not subdomains — the only TLD on the internet that works this way. Verisign proposed killing the entire third level of the hierarchy, and ICANN approved it in July 2026, so 22,000 people are about to lose their `x.y.name` registrations while the second-level `.name` stays. The guy who wrote the original post (the author behind frazier.name) has used it for 25 years, so his website, email, and any IoT devices tied to it all become bricks in February — and if someone snags `frazier.name`, they could hijack every account linked to that email. His one-line summary of ICANN's justification: "it's hard, we don't want to deal with it." A reconsideration request was filed and already rejected, so spread the word because almost nobody's talking about this.

## 5. 🎬 Video — by The PrimeTime

![The PrimeTime](https://i.ytimg.com/vi/xOz2wXb-TiE/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/xOz2wXb-TiE
**Karakeep doc:** `dq3vvy5hic1ovb7oh0ox8do2`

The PrimeTime riffs on "the end of programming" — i.e. the idea that human review is dead. His hook is Paul Dix (InfluxDB) pointing at the Bun→Zig→Rust rewrite, where AI allegedly wrote a million lines of code, spent $165k in API costs over 11 days, and shipped software now running on millions of machines. His take: stop hand-waving it as "they had an oracle to diff against." If you can build a verification system and give proper direction, AI produces genuinely complex software — and yeah, he agrees, even if it makes people mad.

## 6. 🎬 Video — by Less Bitter

![Less Bitter](https://i.ytimg.com/vi/aSGHPm7pu_Q/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=aSGHPm7pu_Q
**Karakeep doc:** `gk533zya9uvlrostzldodp84`

Less Bitter does a two-parter: first, Zuckerberg's "shut up and build" dunk on Sam Altman and Dario holding hands over safety. Zuck delayed shipping Muse for months over "bugs," not some grand alignment sermon, and didn't demand everyone else slow down first — which Less Bitter reads as a direct callout of OpenAI/Anthropic's self-aggrandizing PR theater. Then he reviews Meta's new "Gary" AI assistant, poking it to build websites, docs, podcasts, and a satirical GSTAC video, before concluding it's decent but not the thing that gets a billion users. He still prefers Grokbot, and thinks AI companies wildly overestimate how much assistant people actually want.

## 7. 🎬 Video — by Theo - t3.gg

![Theo - t3.gg](https://i.ytimg.com/vi/NvVbCqDgfCs/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=NvVbCqDgfCs
**Karakeep doc:** `gnn2k4kbhaxbx4nrzx0kmv49`

Theo broke his hand, so this is a personal diary of staying productive one-handed — and the punchline is that he's shipping more than ever. Talking out code directly is useless, so he leaned hard into vibe coding, a $70 podium mic for near-silent Whisperflow dictation, and his "Fleet" repo that documents all his machines so he never SSHes or types terminal commands. The real shift is mental: bring agents in earlier, let them run longer, and stop caring about speed — Astra's merged 100+ PRs and Fable 50+ fully autonomously with only two minor animation regressions, a better hit rate than most devs. He's done with terminals and never going back.

## 8. 🎬 Video — by Kai Lentit

![Kai Lentit](https://i.ytimg.com/vi/FG8sUgjBGXs/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=FG8sUgjBGXs
**Karakeep doc:** `v115bzvm9qf9q66bbgh4at4b`

A deadpan mock interview with a 2026 Big Data engineer, packed with one-liner truth bombs: "big data is anything that crashes Excel," "if the join fits in memory, it belongs in Postgres," and a stack of Kafka/Airflow/Spark/Flink/Iceberg that exists mostly to clean logs. The whole bit is a FinOps roast — the AI team burns $4M and calls it investment, his $340k cloud bill is a "review," and he's on call with his phone off. Data isn't the new oil, it's the new asbestos. Sponsored by Railway, obviously.

## 9. 🎬 Video — by Craft Computing

![Craft Computing](https://i.ytimg.com/vi/xTnouFZKvos/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=xTnouFZKvos
**Karakeep doc:** `x3coobt1xooqxps365mfmtue`

Talking Heads ep. 450. Micron drops the first 512GB DDR5-9200 RDIMM — bit-for-bit ECC, 16W per stick, but four of these things cost more than Jeff's house. Then a Cisco CVE scored 9.8: their email security gateway gets rooted by just *sending it an email*, because the input sanitizer let the text it reads run as code. The kicker is the US AI datacenter story — by 2035 American AI datacenters are projected to be the fifth-largest consumer of natural gas, burning gas while China's doing the same buildout on solar.

## 10. 🎬 Video — by Better Stack

![Better Stack](https://i.ytimg.com/vi/hM_mEE8BXfU/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=hM_mEE8BXfU
**Karakeep doc:** `z8uipcqathe8h0qvt4cdwbd3`

A 35B Qwen MoE model running on an iPhone at 11 tokens/sec, via the Flash-MoE engine's iOS port. The trick: MoE models only activate ~3B of their 35B params per token, so the hot experts stay resident in RAM (~1.4GB) while the rest stream off SSD on demand, and the OS page cache does most of the heavy lifting. Tiered quantization keeps hot experts at 4-bit and cold ones at 2-bit, shrinking the whole model from ~19GB to ~13GB. Downside: the phone heats up from literally saying "hello."


### 9to5Linux (RSS)

## 11. GNOME 51 "A Coruña" Desktop Environment Officially Released, This Is What's New — by 9to5Linux

![9to5Linux](https://9to5linux.com/wp-content/uploads/2026/09/g51.webp)

**Source:** https://9to5linux.com/gnome-51-a-coruna-desktop-environment-officially-released-this-is-whats-new
**Karakeep doc:** `natasc2ybbm64e574pwt6ap3`

GNOME 51 "A Coruña" shipped as the latest stable desktop. Highlights: monitor brightness save/restore, elogind as a libsystemd provider, a QR code API, initial reduced-motion support, and ext-background-effect-v1 blur. Nautilus got drag-count badges and new-tab location opens, Settings got auto-rotate and fingerprint management, and Disks finally got ported to GTK4/libadwaita. It'll be the default on Ubuntu 26.10 and Fedora 45.


### Open-source Projects (RSS)

## 12. Zed — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/zed-industries/zed)

**Source:** https://www.opensourceprojects.dev/post/bada5741-d16d-4eeb-afec-0341a7e85665
**Karakeep doc:** `adhc67e271bl2patuo2lfuqa`
**GitHub:** https://github.com/zed-industries/zed

Zed — the high-performance multiplayer code editor from the Atom and Tree-sitter crew. 90,360 stars, written in Rust, still actively pushed. Built around gpui and rust-lang for speed-of-thought editing with real-time collaboration.

## 13. Books Free Books — by Open-source Projects

![Open-source Projects](https://www.opensourceprojects.dev/images/open-source-logo-830x460.jpg)

**Source:** https://www.opensourceprojects.dev/post/a4fd5b7c-b720-4c1c-a82f-ca7d1cbc6d45
**Karakeep doc:** `bu88tf0znnfsv9vou3mosof9`

The headline repo (`ltbgykio/books-free-books`) is a 404 on GitHub — gone, deleted, or never existed. The opensourceprojects.dev post is dead too. A "pile of free books" that evaporated before you could pirate a single PDF. Honest stub: there's nothing here to summarize. 🤷

## 14. A unified library for evaluating and understanding large language models — by Open-source Projects

![Open-source Projects](https://www.opensourceprojects.dev/images/open-source-logo-830x460.jpg)

**Source:** https://www.opensourceprojects.dev/post/c4116659-2359-4ae1-937c-ac39b994b98d
**Karakeep doc:** `chuf0szxl1wy71rmyutcixlr`

**GitHub:** https://github.com/microsoftarchive/promptbench

PromptBench is a benchmark-and-eval framework for LLMs, with adversarial-attack and robustness tooling baked in. 2.8k stars, Python, MIT. Heads up though — it's now under `microsoftarchive` and marked archived, so Microsoft has officially put it on the "we used to care" shelf. Still fine for poking at prompt robustness if you don't expect updates.

## 15. A lightweight bastion host with session recording and 4A access control — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/veops/oneterm)

**Source:** https://www.opensourceprojects.dev/post/48d31f39-6f6c-434b-857c-a4ef950a044f
**Karakeep doc:** `ev2n39mwx8locsefcd8puwqk`

**GitHub:** https://github.com/veops/oneterm

OneTerm is a Go bastion host that funnels all your infra access — SSH, RDP, VNC, the lot — through one place with session recording and access control. 1.7k stars, AGPL-3.0, active. If you've got servers and no audit trail, this is the "who the hell typed that" insurance policy you're missing.

## 16. A pile of tutorials for V2ray, Shadowsocks, and Clash, all in one repo — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/bannedbook/fanqiang)

**Source:** https://www.opensourceprojects.dev/post/72224ca8-defc-42b4-beaf-430c040f2526
**Karakeep doc:** `j6u4ojhmumqv9cg95vzb5cmb`

**GitHub:** https://github.com/bannedbook/fanqiang

Fanqiang ("翻墙", literally "climb the wall") is a 53.5k-star mega-repo of tutorials and guides for getting past censorship — V2Ray, Shadowsocks, Clash, Psiphon, and friends. Kotlin-labeled, no license, very much alive as of September 2026. It's the go-to handbook for anyone whose government thinks the internet is optional. 🌍

## 17. Add workers at runtime and let agents discover them live — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/motiadev/motia)

**Source:** https://www.opensourceprojects.dev/post/4281a438-91e1-440e-b4d9-f3e3d5d62d08
**GitHub:** https://github.com/iii-hq/iii
**Karakeep doc:** `j792g2seuq1eahu1zb9gdhxr`

`iii` claims to be the first tool that composes, extends, and observes every service in real time. Rust under the hood, 18.7k stars. If it actually does live agent discovery without shitting the bed, that's genuinely useful for distributed systems.

## 18. Open-vocabulary object detection at 100 FPS on a single A100 — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/om-ai-lab/omdet)

**Source:** https://www.opensourceprojects.dev/post/530b836f-47ab-45b7-83a1-cb07344fe71e
**GitHub:** https://github.com/om-ai-lab/OmDet
**Karakeep doc:** `kfheudfr5rywvz90o8p873zf`

OmDet does open-vocabulary, end-to-end object detection in real time. 100 FPS on an A100 is a brag-worthy number, though the repo hasn't been pushed since March so maybe don't hold your breath for fixes. Apache-2.0, 1.4k stars, zero-shot vision-and-language.

## 19. A WinForms control library with themes for .NET projects — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/taiizor/realtaiizor)

**Source:** https://www.opensourceprojects.dev/post/0dfdb45b-fd19-4220-bca0-42c90731d8cd
**GitHub:** https://github.com/Taiizor/ReaLTaiizor
**Karakeep doc:** `npq34dquv9edeo6c36br2m5g`

ReaLTaiizor is a WinForms control library with a pile of components and a design-first bent. Fluent, Material, custom themes — for the folks still shipping .NET desktop apps in 2026. MIT licensed, 2.3k stars, and still actively pushed.

## 20. Copy/paste code snippets for building AI systems that actually work — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/daveebbelaar/ai-cookbook)

**Source:** https://www.opensourceprojects.dev/post/efbcfccb-285b-40a5-b554-0dceef96b6b5
**GitHub:** https://github.com/daveebbelaar/ai-cookbook
**Karakeep doc:** `p9rfh1dv2szjl2bzd02q85nq`

ai-cookbook is a collection of examples and tutorials for building AI systems — agents, LLMs, OpenAI and Anthropic bits. 4.5k stars, MIT, mostly Python. Handy when you don't want to re-derive the same RAG boilerplate for the fifth time this month. 😮‍💨

## 21. A list of GKD third-party subscription links, sorted by maintenance status — by Open-source Projects

![Open-source Projects](https://www.opensourceprojects.dev/images/open-source-logo-830x460.jpg)

**Source:** https://www.opensourceprojects.dev/post/cd9162a9-f8df-4ad7-85d3-bc1383b06249
**Karakeep doc:** `pgxpbk2osdkozl9093ruvu9t`
**GitHub:** https://github.com/Adpro-Team/GKD_THS_List

A maintained index of third-party subscription links for GKD, the Android ad-blocker that intercepts in-app ads via rules. 5.2k stars, written in TypeScript, and someone's actually keeping the maintenance status current instead of letting it rot like every other rules list. If you're tired of apps shoving ads in your face, this is the curated list to grab.

## 22. Converting PDFs to Markdown with multimodal LLMs — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/markpdfdown/markpdfdown)

**Source:** https://www.opensourceprojects.dev/post/a744d6e9-2c69-41ca-856b-14eac73abf91
**Karakeep doc:** `uf3ph8sclvk10s6v15m97rse`
**GitHub:** https://github.com/MarkPDFdown/markpdfdown

MarkPDFdown turns PDFs into Markdown by feeding them to a multimodal LLM's visual recognition instead of fumbling with text extraction. 2.2k stars, Apache-2.0, Python. When traditional parsers choke on layouts and tables, just let a vision model read the damn page.


### LinuxLinks (RSS)

## 23. 4 Useful Free and Open Source Code Formatters for C# — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/Code-Formatter-banner3.png)

**Source:** https://www.linuxlinks.com/useful-free-open-source-code-formatters-csharp/
**Karakeep doc:** `bw6rjwvyvqzpm6cdbc42fepm`

A roundup of four free code formatters for C#: Uncrustify, Artistic Style, CSharpier, and ClangFormat. The pitch is the usual LinuxLinks spiel — cede your hand-formatting, get speed and determinism, stop bickering about style. CSharpier's the standout if you want zero-config, opinionated formatting that just works.

## 24. IntelOwl - threat intelligence enrichment and analysis platform — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/09/Data_security_02.jpg)

**Source:** https://www.linuxlinks.com/intelowl-threat-intelligence-enrichment-analysis-platform/
**Karakeep doc:** `ckyi602bt8wxj9gt92u5qw6p`
**GitHub:** https://github.com/intelowlproject/IntelOwl

IntelOwl is a threat-intel enrichment platform that cuts the manual grind of checking IPs, domains, URLs, hashes, and files across a pile of separate sources. Built by Certego in Python/Django, it chains analysers, connectors (MISP, OpenCTI), pivots, and playbooks into repeatable SOC workflows. AGPL-3.0, ~4.7k stars, and still actively pushed — one of the few threat tools that isn't abandonware.

## 25. emplace – synchronize installed packages across multiple machines — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2022/06/170y-utilities.jpg)

**Source:** https://www.linuxlinks.com/emplace-synchronize-installed-packages-across-multiple-machines/
**Karakeep doc:** `dx2q5tn61h0iriem8ielv5vy`

Another "dotfiles but for packages" toy, except this one is actually sane. emplace records whatever you decide to mirror in a human-readable RON file, keeps it in Git, and its shell integration nags you after `apt install`/`pip`/`npm` to add the new package. Covers Apt, Pacman, Nix, Cargo, Go, the works. Rust, AGPLv3, on Codeberg.

## 26. ZPico – tiny package manager for Zsh — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2023/02/147_linux_interface.jpg)

**Source:** https://www.linuxlinks.com/zpico-tiny-package-manager-zsh/
**Karakeep doc:** `g764lyf3uzi6x34rocy1b68w`
**GitHub:** https://github.com/thornjad/zpico

A deliberately minuscule Zsh plugin manager, all pure Zsh, no framework bloat. Packages are just Git repos you can pull from GitHub, GitLab, Codeberg, or local paths, with branch and file-glob selection. Atomic self-update so a flaky download doesn't nuke your script. Six stars. ISC license. Basically antidote with the ambition dialed way down.

## 27. 3D Periodic Table – visualize element properties in three dimensions — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2019/10/alchemist-table-production-magical-potions-elixir-colored-bottles-flasks-are-table-alchemist-wizard-fantasy-fairy-tale-3d-illustration.jpg)

**Source:** https://www.linuxlinks.com/3d-periodic-table-visualize-element-properties-three-dimensions/
**Karakeep doc:** `gtx7ubyekoi15btpbijqyhwt`
**GitHub:** https://github.com/suhdonghwi/3d-periodic-table

The periodic table, but as a rotatable Three.js scene where pillar height maps to whatever property you care about — atomic radius, crust abundance, whatever. Log scaling, category/block/phase coloring, click an element for details. React + TypeScript + React Three Fiber, MIT. Honestly just a fun way to see why uranium towers over everything.

## 28. ab-av1 – AV1 encoding with fast quality sampling — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2019/05/video-conversion.jpg)

**Source:** https://www.linuxlinks.com/ab-av1-encoding-fast-quality-sampling/
**Karakeep doc:** `l8flmgktq6ckes0u71b86ig9`
**GitHub:** https://github.com/alexheretic/ab-av1

Stops you from doing the encode-reencode-encode dance to find a CRF. ab-av1 encodes short samples, measures VMAF (or XPSNR), and binary-searches its way to a CRF that hits your quality target, then hands the full encode to FFmpeg. Works beyond AV1 too — H.264/H.265, even images. Rust, MIT, ~1k stars, JSON output for scripts.

## 29. 13 Useful Free and Open Source Network Configuration Management Tools - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2023/02/20944989-network.jpg)

**Source:** https://www.linuxlinks.com/network-configuration-management-tools/
**Karakeep doc:** `mk6b75xa6zhmg8gusv8kuz67`

LinuxLinks rounds up 13 open-source tools for the thankless job of babysitting network config — discovery, inventory, backups, change tracking, compliance. The usual suspects show up: NetBox for modeling, Oxidized and RANCID for config backup/diffing, phpIPAM for IP addressing, Nautobot as source-of-truth. One caveat buried in the fine print: rConfig's open-source v3 is abandoned, so the "free" label is doing some heavy lifting there. 🧱

## 30. LCOS - Linux distribution based on Devuan - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/04/Linux-Distributions.png)

**Source:** https://www.linuxlinks.com/lcos-linux-distribution-devuan/
**Karakeep doc:** `mohhhlixlnwrvg5rem6ie7lq`
**GitHub:** https://github.com/BryanLunduke/LCOS

LCOS is Bryan Lunduke's pet distro — a minimal Xfce desktop built on Devuan with SysV init, so no systemd and, notably, zero online accounts or age verification. The whole pitch is a "practical OS that doesn't ask who you are," which is either refreshing or a bit tinfoil depending on your mood. It's x86_64 only, APT-managed, fixed release. 376 stars and CSS as its listed language, which tells you most of the repo is docs and a website. 🤷

## 31. systemd_commander - TUI for managing systemd services - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2021/11/command-schedulers.png)

**Source:** https://www.linuxlinks.com/systemd_commander-managing-systemd-services/
**Karakeep doc:** `mzp16ef2cqwifw60mtdqtw2r`
**GitHub:** https://github.com/nilseuropa/systemd_commander

systemd_commander is a ncurses TUI for driving systemd without hammering out `systemctl` every five seconds. It ships with a paired journal_viewer, so you can start/stop/restart/enable services and then jump straight into the logs for that unit. The smart bit: it only asks for root on the actual privileged ops instead of running the whole UI as root. C++, Apache-2.0, 21 stars — small but genuinely useful. 🖥️

## 32. 21 Best Free and Open Source Linux Astronomy Apps - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2021/05/milky-way-arch-starry-sky-alps-panoramic-view-astro-photography-stargazing-light-pollution-valley.jpg)

**Source:** https://www.linuxlinks.com/astronomy/
**Karakeep doc:** `n05xh7xeqeekp1snxkxtt5kf`

A roundup of 21 astronomy apps for Linux, from the heavyweight Stellarium virtual planetarium down to terminal star maps like astroterm and skyterm. Covers the whole hobbyist spectrum — sky charting, telescope control, ephemerides, FITS image viewing, even a Mars simulator. KStars for KDE, Gaia Sky for VR, and Celestia for the nostalgia crowd all make the cut. Enough here to burn a whole weekend pointing at the sky. 🔭

## 33. rdmatop - real-time TUI monitor for RDMA network traffic - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/10/utility-tool.jpg)

**Source:** https://www.linuxlinks.com/rdmatop-real-time-tui-monitor-rdma-network-traffic/
**GitHub:** https://github.com/uccl-project/rdmatop
**Karakeep doc:** `prlx7vpuq796ihrzm6vx46p6`

htop for your InfiniBand. rdmatop gives you a live TUI of RDMA device throughput, packet drops, retransmits, and RDMA read/write counts, then maps queue pairs back to the processes that own them via netlink and /proc. It reads the kernel's RDMA netlink interface instead of a vendor SDK, so it doesn't give a shit whether you're on ConnectX, RoCE, or AWS EFA. Written in Rust, spits Chrome traces for Perfetto, and it's the thing you reach for when NCCL stalls at 3am. 🖥️

## 34. 15 Best Free and Open Source Linux Terminal-Based Clocks - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/02/038-clock.png)

**Source:** https://www.linuxlinks.com/best-free-open-source-linux-terminal-based-clocks/
**Karakeep doc:** `tsmy9rnf553qthd444uugace`

Because your taskbar clock is just too fucking mainstream, LinuxLinks rounded up 15 terminal clocks. The list runs from the obvious (tty-clock, Peaclock) to the genuinely weird — TetroTime renders the time using falling tetromino pieces, and stardial is space-anime themed for reasons nobody asked for. Most are TUIs, a couple are bare CLI. If you need to know it's 2pm and want a weather forecast with animated effects, Tenki's got you covered. 🕐

## 35. Best Free and Open Source Alternatives to Apple iCloud Drive - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/08/003-cloud-storage.png)

**Source:** https://www.linuxlinks.com/best-free-open-source-alternatives-apple-icloud-drive/
**Karakeep doc:** `tz4hgx7q016ma89nyy0m2g70`

Five ways to stop paying the Apple tax on your files. Syncthing is the decentralized pick — no server, direct device-to-device sync with TLS and per-device crypto identity. Seafile and OpenCloud give you the classic server-based cloud drive, Nextcloud is the sprawling self-hosted everything-platform, and Peergos is for the paranoid who want end-to-end encryption with metadata minimised. Basically: pick Syncthing if you want sync, Nextcloud if you want to replace half of iCloud, Peergos if you wear a tinfoil hat. ☁️

## 36. Picogen – minimalist static website generator - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/10/SSG-4.png)

**Source:** https://www.linuxlinks.com/picogen-minimalist-static-website-generator/
**GitHub:** https://github.com/vlatan/picogen
**Karakeep doc:** `wo80zxa9zdo1j2xefjy55l7m`

Yet another Python static site generator, and honestly the 2 stars on GitHub tell you how excited the world is. It converts Markdown to a static site via Jinja templates, splits content into posts and pages, reads metadata (title, date, category, slug) straight from the Markdown front matter. Site config comes from env vars, ships a default theme but supports custom ones, and it can push the build to an S3 bucket or back up your Markdown to S3. If you need one more Python SSG to add to the 25 already in LinuxLinks' own roundup, here you go. 🤷

## 37. sdctl - security-focused TUI for managing systemd services - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2021/11/command-schedulers.png)

**Source:** https://www.linuxlinks.com/sdctl-tui-managing-systemd-services/
**Karakeep doc:** `y6ug9akhmjjkz2omcaw9i919`
**GitHub:** https://github.com/ruiiiijiiiiang/sdctl

Another systemctl wrapper, this time in Rust. sdctl is a TUI for managing systemd units with a "security-focused" angle — journalctl, logs, and the usual start/stop/restart dance. 13 stars and MIT license, so it's early days. If you hate typing `systemctl` flags, this is your jam. Otherwise, `systemctl` itself works fine.

## 38. LoMux – lightweight FFmpeg media converter - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2019/05/video-conversion.jpg)

**Source:** https://www.linuxlinks.com/lomux-lightweight-ffmpeg-media-converter/
**Karakeep doc:** `zain1r509ejk3mp9xtko6evg`
**GitHub:** https://github.com/zblauser/LoMux

A cross-platform GUI slapped on top of FFmpeg so you don't have to memorize `-c:v libx264` incantations. Batch processing, lightweight, Rust, MIT. 18 stars — basically HandBrake's nerdy little brother. Fine if you want a button instead of a command line. For one-offs, the CLI is still faster.


### Other RSS

## 39. Poważna wpadka Revoluta: przekazał dane klientów oszustom. Poszkodowani mają być też Polacy — by NieBezpiecznik.pl

![NieBezpiecznik.pl](https://niebezpiecznik.pl/wp-content/uploads/2026/09/revolut-kv-600x338.png)

**Source:** https://niebezpiecznik.pl/post/powazna-wpadka-revoluta-przekazal-dane-klientow-oszustom-poszkodowani-maja-byc-tez-polacy/
**Karakeep doc:** `lworsjletb8rouv379ykh730`

Revolut handed over customer data to scammers posing as a government agency — full names, DOB, KYC selfies, passport scans, and complete transaction histories including Bitcoin. They answered fake "European Investigation Order" requests from a hijacked Italian PEC mailbox for five months before noticing. Ransom demand: 10,000 BTC, over $780M. Poles are on the hit list, and it's not the first time Revolut's leaked data. 🚨
