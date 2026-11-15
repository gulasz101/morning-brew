---
date: 2026-11-14
slug: 2026-11-14-morning-brew
tags: Software Engineering, Operating Systems, Artificial Intelligence, Anthropic, Claude, selfhosted, Markdown, Wiki, Raneto, Self-Hosted, Knowledge Base, Linux, Open Source Software, Technical Writing
---

Morning Brew for 2026-11-14: 42 items written from 46 hoarded bookmarks and feeds, 4 dropped after a failed retry.

### RSS

## 1. Can Fable 5.2 REALLY Build an OS From Scratch? (We Tested It), by Better Stack
![](https://i.ytimg.com/vi/V8SZ6cJ6q5U/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=V8SZ6cJ6q5U · **Karakeep:** `quh3xei4qou265wcq8dh2n1l`

**In short:** Better Stack had Fable 5.2 build an operating system for a hand-built ESP32-S3 VGA computer. It produced a working 1.9 MB OS with Doom and a text browser, but the result still has plain-text passwords and system-wide crash restarts.

**Key points:**
- Fable 5.2 wrote about 11,000 lines of C plus a little assembly in one session of a little over an hour.
- The result is a 1.9 MB operating system on an ESP32-S3 with a desktop, filesystem, crash handler, loadable apps, text browser and Doom.
- The ESP32-S3 has two 240 MHz cores, 16 MB flash, 8 MB PSRAM and about 320 KB of fast memory.
- The VGA adapter gives 64 colours; Doom runs at about 32 frames per second at 640 by 400 with dithering.
- The browser supports HTTPS, links, history and bookmarks, but only renders plain HTML.
- Anthropic's separate demo used over 1,000 subagents for eight days; this video used one Claude Max subscription.

**Details:** Better Stack's Andris built a VGA box around an ESP32-S3, then asked Fable 5.2 to write the operating system. The model produced about 11,000 lines of C and some assembly in a little over an hour on one Claude Max session, turning the box into a 1.9 MB OS with a desktop, filesystem, crash handler, loadable apps, a text browser and Doom at about 32 frames per second. The browser does HTTPS with links, history and bookmarks, but only plain HTML, and the Wi-Fi password is stored in plain text. Any app that crashes inside an OS call can still restart the whole system. The hardware side was the painful part: soldering the VGA adapter, fixing a monitor that rejected the standard 640 by 480 mode by moving to 26.67 megahertz, and powering USB peripherals through extra breakouts. Anthropic's own demo used over 1,000 subagents for eight days, which is a different scale of sales pitch than one subscription and an hour. I would say it is an impressive coding stunt on a tiny machine, not proof that Fable can replace engineering judgement.

**For my projects:** Nothing for my projects.

## 2. Raneto - Markdown-powered knowledge base and wiki - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2019/03/wiki-engine.png)
**Project:** [Raneto](https://github.com/ryanlelek/Raneto)
**Source:** https://www.linuxlinks.com/raneto-markdown-powered-knowledge-base-wiki/ · **Karakeep:** `psqzorpfz5yt3pyj3gcac3x8`

**In short:** Raneto is a self-hosted Markdown wiki that keeps articles as plain files instead of a database; I would say it is a tidy option for published docs, but not an exciting one.

**Key points:**
- Self-hosted knowledge base and wiki for publishing Markdown as browsable, searchable web pages.
- Articles are stored as ordinary files in a content directory, so they can be edited outside the app, moved between servers and tracked with Git.
- Browser Markdown editor, username and password protection for editing, syntax highlighting and generated table of contents links.
- Search covers page titles and document contents, including fuzzy and partial matches.
- Appearance uses Bootstrap-based themes and Mustache templates; site title, base URL, content directory and interface language are configurable, with environment variable overrides.
- MIT licence; written in JavaScript; by Gilbert Pellegrom, Ryan Lelek and contributors.

**Details:** Raneto is aimed at product manuals, developer guides, support articles and internal reference material. It separates reading from editing, so a site can be public while edits need credentials. The file-based storage is the main draw: no database to back up, and Git handles revisions. The browser editor is there for people who do not want to touch files. It also has categories and nested subcategories, search with fuzzy and partial matches, code highlighting, table of contents links and Google Analytics integration. Configuration covers the site title, base URL, content directory and interface language, and overrides can come through environment variables. It runs on Linux and Windows. The catch is that it is still a traditional JavaScript wiki, and the article does not mention Kubernetes, metrics or a real backup story beyond moving files and Git. I would say it is stable enough for a small docs portal, but not something I would fight into the homelab without a container and monitoring plan. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 3. 20 Best Free and Open Source Linux Documentation Generators - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2020/10/documentation-generators.jpg)
**Source:** https://www.linuxlinks.com/documentationgenerators/ · **Karakeep:** `zhhwkrn1t2xh5n9nomnmahqr`

**In short:** LinuxLinks rounds up 20 free and open source documentation generators for Linux; it is a catalogue rather than a review, and I would say it is useful mainly as a starting point.

**Key points:**
- LinuxLinks lists 20 free and open source Linux documentation generators, from JSDoc and Javadoc to Sphinx, Doxygen and Docusaurus.
- The roundup is a table of one-line descriptions, with no versions, benchmarks or install notes.
- It covers API documentation tools for JavaScript, Java, Python, PHP, C and C++, TypeScript, Kotlin and Fortran.
- It also includes documentation site and publishing tools such as mdBook, Starlight, Antora, Quarto and Daux.io.
- Published by Steve Emms on 14 November 2026, and updated to reflect a recent announcement.

**Details:** This is a LinuxLinks roundup of 20 free and open source documentation generators for Linux, published by Steve Emms on 14 November 2026. It is a table of names with one-line descriptions, not hands-on reviews, so the useful part is the coverage map: API generators for JavaScript, Java, Python, PHP, C and C++, TypeScript, Kotlin and Fortran, plus site builders like Docusaurus, mdBook, Starlight, Antora and Quarto. I would say it is a handy index if you are choosing a doc tool and want the open source options in one place. It does not give versions, prices, licences beyond the free and open source label, or any sense of which ones are still maintained, so it is a starting point rather than a decision. Nothing for my projects, because a documentation generator does not make a factory stage stricter or a docs server more reliable, and it is not something I would run this month.

**For my projects:** Nothing for my projects.

**Projects:**
- [JSDoc](https://github.com/jsdoc/jsdoc): An API documentation generator for JavaScript. Contribute to jsdoc/jsdoc development by creating an account on GitHub.
- [Javadoc](https://www.oracle.com/java/technologies/javase/javadoc-tool.html): Javadoc is a tool from Sun Microsystems for generating API documentation in HTML format from doc comments in source code.
- [Sphinx](https://github.com/sphinx-doc/sphinx): The Sphinx documentation generator. Contribute to sphinx-doc/sphinx development by creating an account on GitHub.
- [phpDocumentor](https://github.com/phpDocumentor/phpDocumentor): Documentation Generator for PHP . Contribute to phpDocumentor/phpDocumentor development by creating an account on GitHub.
- [Doxygen](https://www.doxygen.nl/index.html): Source code documentation and analysis tool.
- [Docusaurus](https://github.com/facebook/docusaurus): Easy to maintain open source documentation websites. - meta/docusaurus.
- [mdBook](https://github.com/rust-lang/mdBook): Create book from markdown files. Like Gitbook but implemented in Rust - rust-lang/mdBook.
- [TypeDoc](https://github.com/TypeStrong/typedoc): Documentation generator for TypeScript projects. Contribute to TypeStrong/typedoc development by creating an account on GitHub.
- [Starlight](https://github.com/withastro/starlight): 🌟 Build beautiful, accessible, high-performance documentation websites with Astro - withastro/starlight.
- [Natural Docs](https://github.com/NaturalDocs/NaturalDocs): Natural Docs source code documentation system. Contribute to NaturalDocs/NaturalDocs development by creating an account on GitHub.
- [Quarto](https://github.com/quarto-dev/quarto-cli): Open-source scientific and technical publishing system built on Pandoc. - quarto-dev/quarto-cli.
- [Antora](https://gitlab.com/antora/antora): Antora / Antora · GitLab.
- [Dokka](https://github.com/Kotlin/dokka): API documentation engine for Kotlin. Contribute to Kotlin/dokka development by creating an account on GitHub.
- [pdoc](https://github.com/mitmproxy/pdoc): API Documentation for Python Projects. Contribute to mitmproxy/pdoc development by creating an account on GitHub.

## 4. PGlite - embedded PostgreSQL database - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2019/03/online-business-database.jpg)
**Project:** [pglite](https://github.com/electric-sql/pglite)
**Source:** https://www.linuxlinks.com/pglite-embedded-postgresql-database/ · **Karakeep:** `kggq3z4losnrrg40wieq91os`

**In short:** PGlite is an embedded PostgreSQL that runs through WebAssembly, built by Electric. I would say it is useful for local-first browser apps and not a fit for my homelab.

**Key points:**
- Runs PostgreSQL queries in browser apps and in Node.js, Bun and Deno without a separate database server
- Storage can be in-memory, IndexedDB in the browser, or the filesystem outside the browser
- Supports PostgreSQL extensions including pgvector and PostGIS
- Uses a single-user connection model instead of PostgreSQL's conventional multiprocessing server architecture
- Free and open source under the Apache License 2.0 and PostgreSQL License; written in TypeScript

**Details:** It runs PostgreSQL queries directly in the browser or in Node.js, Bun and Deno, with no separate server process. Storage can be in-memory, IndexedDB in the browser, or the filesystem outside it. It supports extensions such as pgvector and PostGIS, and it uses a single-user connection model instead of Postgres's normal multiprocessing server. The project is free and open source under the Apache License 2.0 and PostgreSQL License, and it is written in TypeScript. For my setup, the missing pieces are the hard ones: no Kubernetes path, no backup story and no metrics. So yeah, that's that.

**For my projects:** Nothing for my projects.

## 5. It Took Me TWO YEARS to Finally Build this Home Server, by Hardware Haven
![](https://i.ytimg.com/vi/_5Ey1wfRqgM/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=_5Ey1wfRqgM · **Karakeep:** `vf3g9170ef3si05hxwe0kob8`

**In short:** Hardware Haven's final home server is a two-year, used-parts 3U build with 128GB ECC, a Xeon W2135 and two GPUs. I would say it is worth watching for the used-hardware reality, and the 110W idle draw makes it a poor copy target.

**Key points:**
- Hardware Haven built it over roughly two years from used, unusual and broken parts, and it replaces a Geekom mini PC running Proxmox.
- The case is a used Rosewell RSV Z3200U 3U chassis at about $133; the motherboard is an X11 SRA-F bought faulty for about $120.
- Memory is 128GB from a 256GB registered ECC DDR4 kit that cost $315 in 2024; the CPU is a 6-core, 12-thread Intel Xeon W2135 at 3.7 and 4.5GHz.
- GPUs are an Intel Arc A310 for transcoding and an Nvidia V100 for local LLMs; idle draw is about 110W and the V100 is capped at 160W.
- It runs local agents, a mean personal-trainer bot, an email summariser and a Home Assistant voice backend; the closet sits at 74 to 80 degrees with the door closed.

**Details:** This is a YouTube build log, not a product. Hardware Haven spent nearly two years gathering used, unusual and broken parts for a 3U rack server that replaces a newer Geekom mini PC. The point was not raw speed. He wanted room for a GPU, faster networking and more memory, and he wanted to run small local models without handing data to cloud providers, so one goal was room for at least one GPU. The parts list is mixed: a used Rosewell RSV Z3200U case for $133, an X11 SRA-F board bought faulty for $120 and revived by using the right registered ECC memory, 128GB from a $315 256GB DDR4 kit, and a six-core Xeon W2135. For graphics he kept an Intel Arc A310 for transcoding and added an Nvidia V100 for LLM work.

The build is honest about its rough edges. Idle power is about 110W, the V100 is capped at 160W instead of 300W, and the closet runs 74 to 80 degrees with the door closed. The payoff is a Proxmox box running local agents, a mean personal trainer bot, an email summariser and a Home Assistant voice backend. Initial feedback is that it is helpful for small tasks, not a replacement for everything. I would say it is worth watching for the used-hardware reality. The 110W idle draw makes it a poor copy target, and it is not for my projects: there is no Kubernetes path, backup story or metrics story here.

**For my projects:** Nothing for my projects.

## 6. Discord Is Dropping Electron For Rust, by Brodie Robertson
![](https://i.ytimg.com/vi/ne3PMon7i9I/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=ne3PMon7i9I · **Karakeep:** `vrr9b0dzq0d92kyi9x5u95wa`

**In short:** Discord is rewriting its desktop and mobile clients in Rust and dropping Electron and React Native, with a Phoenix build using 300 MB RAM and much faster boot, but the framework claims are contradictory and the mod scene takes the hit. I would say it is a real performance win on paper, with a lot still unconfirmed.

**Key points:**
- Brodie Robertson covers Discord CTO hints about replacing Electron on desktop and React Native on mobile with a Rust codebase.
- The Phoenix client uses 300 MB RAM against the current Electron client's multiple gigabytes, often 3-4 GB, but Brodie says it should be under 100 MB.
- Boot time and navigation are shown as much faster, with clicking around described as instant.
- The Android build drives the OS native view layer through the same Rust codebase as the desktop app.
- The CTO's framework statements conflict: GPUI is named in one comment, then 'no framework, we made our own' in another.
- Electron-hooking mods such as Vencord and BetterDiscord are expected to break, while web-client injection may survive.

**Details:** Discord's CTO is hinting at a big client rewrite: Electron goes away on desktop, React Native goes away on mobile, and both share a Rust codebase. Brodie Robertson walks through the numbers. The Phoenix build uses 300 MB of RAM, which is still too much in his view, but the current client can use three or four gigabytes. Boot time and clicking around look much faster in the side-by-side video, and the Android build drives the native view layer through the same Rust code.

There is a framework muddle. One CTO comment names GPUI, another says Discord made its own framework, and a third says GPUI inspired the API while the internals are more like React Native. Brodie is not sure which applies to desktop and which to mobile, so I would treat the framework claims as unsettled until the app ships.

The web client stays, so browser use is unaffected. Mods are the casualty. Electron-hooking mods such as Vencord and BetterDiscord are expected to break, while web-client injection may survive. Vencord's maintainer says the desktop core would be easy to port but pointless without Vencord, and proxying or self-hosting the old web app raises copyright and trust problems. Brodie also dismisses the rumour that Linux loses the client, since there is no evidence for it and Discord is unlikely to keep two desktop versions. On AI, his line is blunt: assume it was used, the question is how much. He still sees engineers behind the work. Nothing for my projects. Still, I like the direction: a 300 MB Discord is still bad, and it beats a four gigabyte one.

**For my projects:** Nothing for my projects.

## 7. 54GB VRAM For $35 The Cheapest Local AI Hack?, by Kai
![](https://i.ytimg.com/vi/oUsXv7ZoYQg/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=oUsXv7ZoYQg · **Karakeep:** `q5j1uczxtx9k64rjrkqil50k`

**In short:** Kai's video is about a rusty nine-GPU mining rig that runs a 35B model fast. The useful bit is that a normal desktop with one 8GB card and 32GB RAM can match it with one llama.cpp flag. I would say test your own machine first.

**Key points:**
- Kai's video covers a buyer who paid 3,000 rubles, about $35, for a rusty nine-card mining rig with 54GB total VRAM.
- The cards are Nvidia P106 Pascal units with 6GB GDDR5 each, no display outputs, and about 192GB/s memory bandwidth per card.
- It ran Qwen 3.6 35B A3B at over 30 tokens a second in llama.cpp with --n-cpu-moe, because the MoE model reads only about 3B of its 35B parameters per token.
- A desktop with a single GTX 1080 and 32GB RAM reached about 25 tokens a second on the same model.
- A dense 70B model at 4-bit would be limited to roughly 4.5 tokens a second on that rig, since the nine cards act like one card's bandwidth.
- Kai's steps use llama.cpp directly, a 4-bit Unsloth build of about 23GB, --n-cpu-moe set to 30, and llama-bench runs with and without the flag.

**Details:** Kai tells the story of Mark Proncken, who bought the rig blind for 3,000 rubles and booted it from USB. Nine P106 cards give 54GB total, but in this pipeline they add memory, not speed. Each token moves through the cards one by one, so the rig has the bandwidth of one card, about 192GB/s. That is why a dense 70B model would crawl at under 3 tokens a second, even though it fits.

The fast result comes from Qwen 3.6 35B A3B, a mixture of experts model. It stores 35B parameters, but only about 3B are read per token, so the speed limit is far lower. Kai says the missing flag is --n-cpu-moe in llama.cpp, which keeps experts on the CPU and lets an 8GB card plus 32GB RAM hit about 25 tokens a second. He suggests checking Ollama with ollama ps, testing with llama-bench, and using dual-channel RAM before buying anything.

I would say the headline is about the wrong number. 54GB lets you load the model; it does not make it fast. The useful lesson is to price hardware by what the model reads per token, not by how much it holds. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 8. Frictionless - data validation and tabular data management framework - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2020/11/data-science-software.jpg)
**Project:** [frictionless-py](https://github.com/frictionlessdata/frictionless-py)
**Source:** https://www.linuxlinks.com/frictionless-data-validation-tabular-data-management-framework/ · **Karakeep:** `upxtk1ug8apt0vtdys8uvffu`

**In short:** Frictionless is a Python framework for describing, validating and transforming tabular data, with a CLI and MIT licence. I would say it is a credible data-quality tool, but nothing for my projects.

**Key points:**
- Python data management framework from Frictionless Data / Open Knowledge Foundation, MIT licence.
- Reads CSV, Excel, JSON, SQL databases and remote HTTP, FTP and S3-compatible storage.
- Infers table schemas and validates tables, resources and complete datasets.
- Detects missing cells, blank rows, duplicate headers, wrong data types and field constraint failures.
- Generates detailed validation reports and transforms datasets through reusable pipelines.
- Streams large datasets to limit memory use and can be extended with custom checks, formats and plugins.

**Details:** Frictionless is a Python framework from Frictionless Data and the Open Knowledge Foundation for describing, extracting, validating and transforming tabular datasets. It can infer schemas, read CSV, Excel, JSON and SQL sources, reach remote HTTP, FTP and S3-compatible storage, and validate tables, resources and whole datasets. It also detects missing cells, blank rows, duplicate headers and wrong types, applies field constraints, writes validation reports, and streams large datasets through a CLI.

I read about it rather than running it. The feature list is broad and the MIT licence is easy, so I would say it is a credible data-quality tool. Unfortunately I do not have a tabular data workflow where it would earn its place, so nothing for my projects.

**For my projects:** Nothing for my projects.

## 9. Techie uses voltage glitching hack to turn $2,500 Nvidia 8GB cryptomining GPU into a full-fat $20,000 A100 with 80GB of VRAM — hack carefully blows onboard fuses to unlock entire VRAM and shader modules, by Tom's Hardware
![](https://cdn.mos.cms.futurecdn.net/QaaiweaJKxjDDJTGrtCSU5-2048-80.jpg)
**Source:** https://www.tomshardware.com/pc-components/gpus/techie-turns-usd2-500-cmp-170hx-8gb-mining-card-into-a-full-fat-a100-80gb-with-voltage-glitching-carefully-blowing-onboard-fuses-to-unlock-entire-vram-and-shader-modules · **Karakeep:** `pinqf3pwxbo7lqo3uvg8fm7m`

**In short:** A $2,500 Nvidia CMP 170HX 8GB mining card was turned into a full-fat A100 with 80GB of VRAM by voltage glitching and blowing onboard fuses. I would say it is a bummer that the route is this risky, so it is not a buying plan.

**Key points:**
- Tom's Hardware piece by Bruno Ferreira about a hardware hack on a Nvidia CMP 170HX mining GPU.
- The card cost about $2,500 with 8GB of VRAM; the unlocked result is described as a full-fat A100 with 80GB of VRAM, worth about $20,000.
- The method is voltage glitching plus carefully blowing onboard fuses to unlock the whole VRAM and shader modules.
- No candidate links were supplied, so there is no repo or tool to point at.

**Details:** A techie took a $2,500 Nvidia CMP 170HX mining card with 8GB of VRAM and used voltage glitching, then carefully blew onboard fuses, to unlock the full 80GB of VRAM and shader modules of a full-fat A100 worth about $20,000. I read about this, I did not try it. I would say it is impressive as a hardware hack and a bit wonky as something to rely on, because one slip with fuses is too much for me. The useful lesson is that locked silicon was unlocked here, not that I should buy a mining card and hope. For my projects, nothing: ideogram4-local wants local image models that are cheaper and easier to control, not a card turned into a server GPU by force. So yeah, that's that.

**For my projects:** Nothing for my projects.

## 10. This Docker Alternative Starts Containers 8× Faster (Kiri), by Better Stack
![](https://i.ytimg.com/vi/qy4ajsBbOKw/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=qy4ajsBbOKw · **Karakeep:** `nbphd4pyvtri9zm1snqiimw3`

**In short:** Kiri is a free, open-source Docker-compatible runtime in Rust that claims roughly eight times faster container startup, plus local domains and one-click public sharing. I would say try it alongside Docker and keep Docker installed.

**Key points:**
- Docker-compatible runtime written in Rust; Mac uses a small Linux VM, Windows uses WSL2, Linux runs on the host
- Claims 22 ms to start a tiny container, roughly 8x faster than Docker Desktop
- Daemon uses around 10 MB RAM; VM shuts down after 60 seconds idle and boots back in about 0.1 s
- Free and open source, works on Mac, Linux and Windows
- Local domain names for containers, HTTPS on Mac, one-click public sharing via Kiri Cloud
- Single-node Kubernetes in around 20 seconds once the image is downloaded

**Details:** Kiri is a Docker-compatible container runtime written in Rust. On a Mac it runs a small custom Linux VM, on Windows it goes through WSL2, and on Linux it runs straight on the host. Your existing Docker commands, Compose files and Dockerfiles still work, and you can keep Docker Desktop installed and switch between the two via a Docker context. The headline number is startup: Kiri claims to start a tiny container in 22 milliseconds, roughly eight times faster than Docker Desktop, though that measures runtime overhead rather than how fast your app runs. The daemon uses around 10 megabytes of RAM, and the VM shuts down after 60 seconds with no containers running, booting back in about a tenth of a second.

There is more here than speed. Kiri gives containers local domain names, so an Nginx container is reachable by name without port mapping, with HTTPS on Mac. You can also share a running local app through a Kiri Cloud account, which produces a public link. The native app manages containers, images, volumes, logs and Compose projects, and it can import existing images and volumes from Docker Desktop or OrbStack. Single-node Kubernetes takes around 20 seconds once the image is downloaded. Kiri is free and open source across Mac, Linux and Windows.

The catch is maturity. Docker Desktop has been around far longer, and Kiri's own benchmarks show Colima faster at reading bind mounts and OrbStack handling more new HTTP connections per second. Networking, volumes, permissions, image builds and Compose edge cases are all still in play. The advice in the video is sensible: try it, keep Docker. I would say the local domains and one-click sharing are as useful as the speed, and since it costs nothing, there is little risk in giving it a spin.

**For my projects:** Nothing for my projects.

## 11. Lakasir - point-of-sale system for retail businesses - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2021/01/point-of-sale.jpg)
**Project:** [lakasir](https://github.com/lakasir/lakasir)
**Source:** https://www.linuxlinks.com/lakasir-point-of-sale-system-retail-businesses/ · **Karakeep:** `gma080ojrqdii25sy0hs2aae`

**In short:** Lakasir is a free, browser-based point-of-sale system for small and medium retail, with multi-tenant support and a GPL v3.0 licence; I would say it packs a lot of retail plumbing into one PHP app, and it is not worth it for me.

**Key points:**
- Free and open source under the GNU General Public License v3.0
- Written in PHP, used through a web browser, with one companion mobile app
- Multi-tenant, so separate businesses keep their own data
- Covers sales, products, inventory, purchase orders, suppliers, stocktaking, receivables, vouchers, discounts, barcodes, thermal receipt printing, roles, basic accounting, reports and a real-time dashboard
- Developed by the Lakasir team; code is on GitHub (link 1)

**Details:** Lakasir is a browser-based point-of-sale system for small and medium retail, with sales, product and stock control, supplier and purchase-order handling, receivables, vouchers, discounts, barcode scanning, thermal receipt printing, user roles, basic accounting, reports and a real-time dashboard. It is multi-tenant, so separate businesses keep their own data, and there is one companion mobile app for another way in. It is free and open source under GPL v3.0, written in PHP, and the developer is the Lakasir team.

The feature list is broad, and that is the bummer: stocktaking, receivables and accounting in one app is a lot of surface area for a small shop to trust. I would say it is quite a good job on paper, but the source says nothing about backups, metrics or a Kubernetes path, so for my homelab it is not worth the fight. Nothing for my projects.

So yeah, that's that.

**For my projects:** Nothing for my projects.

## 12. 19 Best Free and Open Source Status Page Systems - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2022/02/dashboard-template.jpg)
**Source:** https://www.linuxlinks.com/best-free-open-source-status-page-systems/ · **Karakeep:** `sl17rcbxw6abmq7l27mw613r`

**In short:** LinuxLinks lists 19 free and open source status page systems, from Uptime Kuma to status.sh. It is a directory, not a comparison, so it is good for finding names and little else.

**Key points:**
- 19 tools are listed, including Uptime Kuma, Gatus, HertzBeat, Kener and Tinystatus.
- The page gives short descriptions only, with no versions, prices, benchmarks or install steps.
- Everything listed is free and open source and aimed at Linux.
- The only community signal is a comment claiming 57.6K GitHub stars for Uptime Kuma.
- The list mixes full monitoring platforms with tiny static generators.

**Details:** I read this as a catalogue, not a test. It tells me what exists and points at portal pages, but I would still have to check Kubernetes support, storage and backups myself. For my homelab that matters more than the status page itself, because a page that cannot survive the cluster is just another thing to babysit. Uptime Kuma and Gatus are the two names I would look at first, since they are the ones most likely to fit a small k3s setup. The rest range from full platforms to shell scripts, so the spread is wide. So yeah, useful list, thin evidence.

**For my projects:**
- homelab-2nd: Put a status page in front of the Cloudflare-tunnelled services, but only consider tools with a real Kubernetes deployment and backup story; Uptime Kuma and Gatus are the first names to check.

**Projects:**
- [Uptime Kuma](https://github.com/louislam/uptime-kuma): A fancy self-hosted monitoring tool. Contribute to louislam/uptime-kuma development by creating an account on GitHub.
- [Statping-ng](https://github.com/statping-ng/statping-ng)
- [OneUptime](https://github.com/OneUptime/oneuptime): Complete open-source monitoring and observability platform. - OneUptime/oneuptime.
- [Checkmate](https://github.com/bluewave-labs/checkmate): Checkmate is an open-source, self-hosted tool designed to track and monitor server hardware, uptime, response times, and incidents in real-time with beautiful visualizations. Don&amp;#39;t be shy,….
- [OpenStatus](https://github.com/openstatusHQ/openstatus): Open-source status page, incident response and uptime monitoring - openstatusHQ/openstatus.
- [Upptime](https://github.com/upptime/upptime): ⬆️ GitHub Actions uptime monitor &amp; status page by @AnandChowdhary - upptime/upptime.
- [Kener](https://github.com/rajnandan1/kener): Stunning status pages, batteries included! Contribute to rajnandan1/kener development by creating an account on GitHub.
- [Gatus](https://github.com/TwiN/gatus): Automated developer-oriented status page with alerting and incident support - TwiN/gatus.
- [Vigil](https://github.com/valeriansaliou/vigil): 🚦 Microservices Status Page. Monitors a distributed infrastructure and sends alerts (Slack, SMS, etc.). - valeriansaliou/vigil.
- [cState](https://github.com/cstate/cstate): 🔥 Open source static (serverless) status page. Uses hyperfast Go &amp;amp; Hugo, minimal HTML/CSS/JS, customizable, outstanding browser support (IE8+), preloaded CMS, read-only API, badges &amp;amp….
- [UptimeFlare](https://github.com/lyc8503/UptimeFlare): ✔ Free and serverless uptime monitoring / status page on Cloudflare Workers, with Geo-specific checks - lyc8503/UptimeFlare.
- [HertzBeat](https://github.com/apache/hertzbeat): An AI-powered next-generation open source real-time observability system. - apache/hertzbeat.
- [PHP Server Monitor](https://github.com/phpservermon/phpservermon): PHP Server Monitor. Contribute to phpservermon/phpservermon development by creating an account on GitHub.
- [Lunalytics](https://github.com/KSJaay/Lunalytics): 🚀 Open source monitoring tool built with Node.js. Contribute to KSJaay/Lunalytics development by creating an account on GitHub.

## 13. $200 for ChatGPT, Claude or Gemini? I Did the Math, by Kai
![](https://i.ytimg.com/vi/xt-Wc2Nyf1M/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=xt-Wc2Nyf1M · **Karakeep:** `yctrmi4w6ac5p41qdcvolt38`

**In short:** It is a YouTube breakdown of the three $200 AI tiers, and the verdict is that the famous 5.6x Claude lead is mostly an API-price illusion, so the real question is whether you need a $200 ceiling at all.

**Key points:**
- Semi-Analysis measured Claude Max 20X at about $11,726 a month in API equivalent value against about $2,084 for ChatGPT Pro 200, a 5.6x gap.
- The same gap held at the $20 and $100 tiers: about $1,178 vs $211 and $5,725 vs $1,055.
- Agent workloads are 96.6% cache reads and 0.3% new code; Opus cache reads cost 20 cents per million tokens, Sol 10 cents.
- Raw token counts are about 29 billion a month on Max against about 10 billion on Pro, roughly 2.8x.
- Anthropic raised Opus allowances on Max by about 20%, while OpenAI cut new Pro 200 allowances to about half the API spend of the old plan.
- Claude Max 20X splits its weekly allowance: half for Claude Fable 5.1, half for Opus 5.5; Max also includes $200 a month API credit that does not work in Claude Code.

**Details:** This is a YouTube breakdown of the three $200 AI tiers: ChatGPT Pro 200, Claude Max 20X and Google AI Ultra 20X. Semi-Analysis measured Claude Max 20X at about $11,726 a month in API equivalent value against about $2,084 for ChatGPT Pro 200. That 5.6x lead repeats at the $20 and $100 tiers. Unfortunately that is fuel cost, not work done: 96.6% of agent tokens are cache reads, Opus charges twice what Sol charges for them, and raw token counts are only about 2.8x. So the honest lead is smaller than the thumbnail.

The plans also measure different things. ChatGPT Pro 200 has no 5-hour session window and a weekly allowance OpenAI no longer publishes. Claude Max 20X is 20x Claude Pro per 5-hour session with a weekly cap, half for Fable 5.1 and half for Opus 5.5, plus $200 a month API credit that does not work in Claude Code. Google AI Ultra 20X is $199.99 and still unmeasured. The effort dial moves cost per task more than switching companies: medium effort on Claude is about 4,270 tasks, while max effort is closer to $9,200. A dollar buys the same at $20 as at $200, so the top tier raises the ceiling without improving the per-dollar rate.

My read: Claude Max 20X is still strongest on volume for heavy agent work, but only if you are actually emptying a $100 plan. For chat, email and small debugging, the $20 plan is probably enough. Google Ultra only makes sense as a bundle with YouTube Premium and storage. Pay monthly, because allowances change without notice. So yeah, that's that.

**For my projects:** Nothing for my projects.

## 14. What’s the Best AI Model Your GPU Can Actually Run?16GB to 1TB VRam, by Kai
![](https://i.ytimg.com/vi/kTmUbRVsamo/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=kTmUbRVsamo · **Karakeep:** `bb4o8wre1dmy08f4mehbv9ac`

**In short:** This is Kai's memory-ladder video for local AI, from 16GB to 1TB. I would say it is worth it for the warning that most doublings buy the same model better stored, and for the 4 November jump at the top, but the ladder itself is still a shopping list.

**Key points:**
- Claude Opus 5.5 at max effort scores 58.4 on the Artificial Analysis Intelligence Index; Quen 3.827B scores 20.1 and DeepSeek V4.1 Flash scores 32.5.
- 16GB means a Mac Mini near $899 or an RTX 5060 Ti near $780; the 27B model runs at 3 bits and one measured 5060 Ti did 45 tokens a second on short prompts.
- 32GB is still the same 27B at 20.1, but with all 4 bits and a 128,000 token context; 64GB adds 8 bits, 256,000 context and up to 10 sessions.
- 128GB is the first real intelligence step, to GLM 5.3 Flash at 27.8, but Macs need one terminal command or they run a 93GB build instead of 111GB.
- From 4 November, a terabyte rung holds the best open model at 2-bit precision with a score of 46.0; the published hardware test runs 14 times slower than the API, at 2.2 tokens a second.
- Rent first via OpenRouter, the Artificial Analysis leaderboard or the model API; a 128GB task costs a fraction of a cent.

**Details:** Kai walks the ladder rung by rung and says most doublings do not buy a smarter model. 16GB is either an M series Mac Mini near $899 or a 16GB card near $780, and on a Mac the GPU only sees about three quarters of that memory, so a 16GB Mac Mini ends up on Google's Gemma 412B, the smaller model. 32GB is the first rung I would call sensible: same 27B, same 20.1 score, but all 4 bits and a 128,000 token context. 64GB is mostly bits and vibes, 8 bits and 256,000 context, and the useful part is concurrency, with one owner reporting 10 sessions and about 150 tokens a second combined. If you are one person with one agent, skip it.

128GB is where intelligence moves, from 20.1 to 27.8 on GLM 5.3 Flash, but the traps matter: the current index has not scored Quen 3.8 Flash Next yet, and a Mac's default limit leaves a 93GB model instead of the 111GB build. 256GB brings DeepSeek at 32.5, 512GB is the same score at 4 bits, and buying two 256GB boxes is cheaper. The terabyte rung changed on 4 November, with the best open model at 2 bits scoring 46.0, though the hardware test runs 14 times slower than the API and nobody knows how much of that score survives compression. Compliance, scale and control are the real reasons to own; otherwise rent first for a week and buy the smallest rung that fits. yeah, that is the ladder.

**For my projects:** Nothing for my projects.

## 15. You Don’t Need an Expensive GPU Anymore (Strata 100 tok/s), by Kai
![](https://i.ytimg.com/vi/mED-boddeWI/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=mED-boddeWI · **Karakeep:** `b6iwyfci0g8z64rjpee2kkbj`

**In short:** Strata is an MIT-licensed local inference engine with a desktop app, and it runs 125B Quen at 94 tok/s on a 12GB card. The 763B DeepSeek number is real but its decode speed on that card is only 4-6 tok/s, so check prefill versus decode before believing any screenshot.

**Key points:**
- MIT-licensed local inference engine with desktop apps for Windows, Linux and Mac; launched 24 Sep, 63 releases in 38 days, about 37,000 GitHub stars.
- Quen 3.8 Flash Next is 125B and runs about 94 tok/s on a 12GB card; DeepSeek V4.1 Flash is 763B with a 1M-token context and runs on a 12GB card via GPU, RAM and SSD tiers.
- On a 12GB RTX 5070, prefill is about 110 tok/s and decode is 4-6 tok/s; a 1000-token answer takes about 3.5 minutes.
- RAM tiers: 32GB is the sweet spot for Quen, 64GB is the target, 128GB or more makes DeepSeek useful; DDR4 is about $7.80 per GB against DDR5 at about $19 per GB.
- SSD storage is about 13 cents per GB, and the 196.6B-parameter engram tables live there.
- Strata's coder build keeps 256 of 512 experts per layer and needs about 30GB; Quen 3.6 35B measured 59.7 tok/s on a 3060.

**Details:** Strata is a local inference engine in the same bracket as llama.cpp or Ollama, but it moves parts of a mixture-of-experts model between GPU, RAM and SSD depending on how often they are used. That is how it runs the 763B DeepSeek V4.1 Flash on a 12GB card: the GPU holds the hot core, RAM holds common experts, and the SSD holds the rest, including the 196.6B engram tables. The Quen 3.8 Flash Next 125B model is the one that actually feels fast at 94 tok/s.

The viral 100 tok/s figure was prefill, the reading speed; decode, the writing speed, was only 4-6 tok/s on that card, so a 1000-token answer takes about 3.5 minutes. Quen is the better fit on 12GB; DeepSeek wants 128GB of RAM or more before it becomes a coding assistant instead of a patience test.

RAM is the new bottleneck: 32GB is the sweet spot for Quen, 64GB is the target, and DDR4 at about $7.80 per GB buys more capacity than DDR5 at about $19 per GB. I would say the expensive GPU has stopped being the price of entry, but the bill just moved to RAM, which is not much comfort this year. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 16. Can a $22K Mac Studio Replace Claude Subscription? (512GB M5 Ultra), by Kai
![](https://i.ytimg.com/vi/6UjDw-2s4ik/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=6UjDw-2s4ik · **Karakeep:** `qd4mbtywrgtdxkegqpc5gmim`

**In short:** Kai's video tests whether a $22,299 512GB M5 Ultra Mac Studio can replace Claude. My verdict: one box cannot, and the four-box version that gets close costs $89,610 and is slow.

**Key points:**
- $22,299 Mac Studio, 512GB M5 Ultra, 1.2TB/s memory bandwidth
- macOS leaves about 384GB available to the GPU
- GLM 5.3 at 418GB and DeepSeek V4.1 Flash at 432GB fit at 4-bit; Meta Muse Spark Open at 533GB does not
- Terminal Bench 4.0: Claude Opus 5.5 64.85%, GLM 5.3 41.82%
- Kimi K3.1 Pro: 2.8T params, 104B active, 1M context, 65.7% vs Opus 66.4%
- Four-Mac cluster costs $89,610, writes 15 tokens/s for one user, up to 2 minutes before first word

**Details:** Kai's video asks whether a $22,299 Mac Studio with 512GB M5 Ultra can replace Claude. The honest answer is no for one box, and only sort of for four. The machine has 1.2TB/s memory bandwidth and can access about 384GB for the GPU, so GLM 5.3 at 418GB and DeepSeek V4.1 Flash at 432GB fit, while Meta's Muse Spark Open at 533GB does not. On Terminal Bench 4.0, GLM 5.3 scores 41.82% against Claude Opus 5.5 at 64.85%, so that is a 23-point gap, and the 4-bit local score may not match server full precision. Then Kimi K3.1 Pro landed: 2.8 trillion parameters, 104 billion active, 1 million token context, native 4-bit, and 65.7% on the same benchmark against Opus at 66.4%. That is close on quality, but four Macs cost $89,610, write 15 tokens a second for one user, and can take up to two minutes before the first word on a complex agent task. So the hardware is never the cheap way to get the model. I would say the sensible split is a $10,799 256GB M5 Ultra with GLM 5.3 Flash for routine work and Claude Max at $100 a month for hard tasks. Buy the 512GB only if the model you need does not fit on 256GB and the data cannot leave the building. Rent Kimi first, since Moonshot charges $2 in and $10 out per million tokens, half of Opus, and the weights stay free. So yeah, that's that.

**For my projects:** Nothing for my projects.

## 17. I Tested Local AI on My Mac Studio So You Don’t Have To, by Kai
![](https://i.ytimg.com/vi/JLs10oOX6NY/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=JLs10oOX6NY · **Karakeep:** `zi6c5qzwgwx736xvhi6unnj2`

**In short:** A video about which Mac local-model runner to use for coding agents. Ollama is the better single-chat pick, but LM Studio wins when an agent fans out several requests at once on a bigger Mac.

**Key points:**
- Ollama 0.40, released 25 Sep, auto-runs supported models on MLX; Ollama 0.40.15, released 3 Nov, added parallel requests for recurrent and vision GGUF models, not MLX.
- GitHub issue #17280: the MLX runner processes requests sequentially even with parallel set to 8, giving wall time of 8x one request.
- Dark Factory benchmark: Ollama read a 16,000-token document at 1,442 tok/s versus LM Studio MLX at 1,372; Ollama showed the first word in 1.3s; writing speed was about 90 versus 42-48 tok/s.
- For each token the Mac reads the whole model from memory, roughly 18GB for a 4-bit Qwen 3 model; batching four requests gives about 2.7x combined output and 45s versus 2min in the example.
- LM Studio 0.4.2, from February, added continuous batching for MLX with four concurrent predictions by default.
- Verdict: Ollama for one chat window; LM Studio for agent use on M5 Pro or above with 48GB or more; on 16GB or 24GB Macs, use Ollama and revisit later.

**Details:** The short version is that the usual tokens-per-second chart is the wrong test once a coding agent fans out subagents. On MLX, Ollama 0.40 queues parallel requests, so four subagents wait in line; LM Studio batches them, and the same Mac and model can be 2 minutes versus 45 seconds. The bottleneck is not the maths. For every token, the Mac reads the whole model out of memory, roughly 18GB for a 4-bit Qwen 3 model, and Ollama's MLX runner handles requests one after another. Issue #17280 shows parallel set to 8 still behaving like a queue. The GGUF workaround uses llama.cpp and gives up the MLX speed. LM Studio added MLX continuous batching in 0.4.2 with four concurrent predictions by default. So for one chat window, Ollama is still the better pick: speculative decoding, MIT licence, headless server, and the fastest first word in the Dark Factory test. For agent use on M5 Pro or above with 48GB or more, LM Studio is the answer. On 16GB or 24GB Macs, most of this does not apply yet, so use Ollama and revisit later. I would say the defaults are the bottleneck: run ollama ps after loading, check whether the runner says MLX engine, and do not assume OLLAMA_NUM_PARALLEL reached it.

**For my projects:**
- agent-fleet: For the M1 Air agents, stay on Ollama; the batching advice only starts to matter on M5 Pro machines with 48GB or more.

## 18. The Local AI Hardware Mistake Almost Everyone Makes, by Kai
![](https://i.ytimg.com/vi/F7qf5Mibgu4/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=F7qf5Mibgu4 · **Karakeep:** `uhl873d78js13hohg37x7ud4`

**In short:** Kai's video says tokens per second is a single-stream number, so it can mislead once agents run several tasks at once. I would say it is a useful reminder to count streams and time the real job, not a reason to buy anything.

**Key points:**
- Kai says an RTX 3090 has about 936 GB/s memory bandwidth and lands around 40 to 46 tokens per second on one 17 GB 4-bit model.
- In the Hyper Quen VLLM test on one RTX 3090, throughput went from 45.4 tokens per second at one request to 1035 at 64.
- Kai's math puts that card at about 3.5% of its 71 trillion operations per second on one stream, with 96.5% idle.
- Claude Code can run up to 20 subagents in one session by default.
- Artificial Analysis stopped ranking models by tokens per second in November.
- Kai's practical steps are OLLAMA_NUM_PARALLEL of at least 4, or llama.cpp server auto, or VLLM, then time the actual task.

**Details:** Kai's point is that tokens per second describes one chat, where the model reads its whole weight set from memory for each token, and the math cores sit mostly idle. For casual chatting or one large document at a time, that single-stream advice still holds, and a Mac Studio's lead at one stream is real. The change is agents: Claude Code can spawn up to 20 subagents, and a developer with two RTX 3090s reported 2.43 times throughput just by running five OpenCode subagents at once. Kai also gives a cost example: the same 3090 is about 33 dollars per token per second at one stream and about 5 at eight streams. So the advice I would take away is to count active requests, set OLLAMA_NUM_PARALLEL to at least 4 or switch to VLLM or llama.cpp server auto, and benchmark the whole task from start to finish. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 19. I Run Full DeepSeek v4.1 Flash on a 12GB GPU, by Kai
![](https://i.ytimg.com/vi/nkb4mfa3S0A/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=nkb4mfa3S0A · **Karakeep:** `b43r2keoof0xdec7u4h1qwvs`

**In short:** Ryan Flavel's Promethevs claims to run the full 510GB DeepSeek V4.1 Flash on a 12GB card, and the honest picture is that full weights do about 2.14 tokens per second, so it is real but slow.

**Key points:**
- DeepSeek ships its experts at FP4, so the full model is 510GB rather than a 16-bit original.
- Each token touches 240 experts, about 4.5GB of expert weights.
- Full FP4 measured about 2.14 tokens per second on a 12GB RTX 3060.
- Strata's 2-bit copy reached about 4.7 tokens per second on an RTX 5070 with 64GB RAM.
- Promethevs uses a fast 2-bit pass, then a full FP4 correction when the top two candidates are close.
- A real coding question took 11 minutes 30 seconds, and the API costs under a dollar on most tasks.

**Details:** The video is about a headline problem rather than a benchmark: Ryan Flavel's Promethevs claims to run the full 510GB DeepSeek V4.1 Flash on a 12GB card. The useful part is the bytes-per-word framing. DeepSeek ships its experts at FP4, so the full model is already 510GB, and each token touches 240 experts, about 4.5GB of expert weights. That is why full FP4 lands near 2.14 tokens per second on a 12GB RTX 3060, while Strata's 2-bit copy reaches about 4.7 on an RTX 5070 with 64GB RAM.

Promethevs tries to get the speed of the 2-bit pass and recover accuracy by checking confidence and doing a full FP4 correction when the top two candidates are close. The video is honest that the correction data is large, the setup is Windows-focused, and real runs are slower than the headline: one coding question took 11 minutes 30 seconds. For paid output, under a dollar on most tasks makes the API look sensible. For finance, healthcare, legal or defence work, local remains the only route, and the slowness is acceptable because the alternative is not using it at all.

My verdict: it is clever, but I would treat it as a privacy tool first and a speed project second. With 32GB RAM the advice is simple, spend the ten dollars on a subscription. With 64GB, Strata's 2-bit file is the proven option.

**For my projects:** Nothing for my projects.

## 20. Is This the End of NVIDIA’s Memory Chip (NCM), by Kai
![](https://i.ytimg.com/vi/PWoc_SfcsAQ/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=PWoc_SfcsAQ · **Karakeep:** `pt9dbvtau1yr212g54nktv7z`

**In short:** This is a Stanford and Together AI paper called Next Concept Modeling that writes 1024 tokens in 32 passes. I would say it is clever research, not the end of NVIDIA memory chips.

**Key points:**
- Stanford and Together AI published Next Concept Modeling (NCM); the claim is 1024 tokens in 32 passes, a 32x reduction.
- On an H100, roughly 0.3% of compute is busy while writing one answer; the rest waits on memory at 3.35 TB/s.
- NCM fills whole levels of learned concept codes in one pass and solved 86.1% of hard Sudoku puzzles versus 1% for a same-size word-by-word model.
- A 27.8-billion-parameter model takes about 28GB at 8-bit, while a 128,000-token conversation needs about 8.6GB of KV cache.
- On a 288GB Rubin-class GPU, about 260GB of the 288GB goes to holding conversations, not model weights.
- TrendForce forecasts DRAM contract prices up 90-95% in Q1, 58-63% in Q2, 13-18% in Q3 and 10-15% in Q4, roughly 4x end-2025 levels.

**Details:** I read this as a useful reality check more than a threat. NCM is genuinely clever: it writes in coarse-to-fine levels, so 32 passes can cover 1024 tokens, and the Sudoku result is strong. But the headline skips the boring part, which is that memory does two jobs. Bandwidth feeds the math unit, and NCM helps that. Capacity holds the conversation, and NCM does not shrink the KV cache.

The numbers are lopsided. A 27.8-billion-parameter model is about 28GB at 8-bit, while a 128,000-token conversation needs about 8.6GB of cache. On a 288GB Rubin GPU, about 260GB is left for conversations, so roughly 30 of them fit. Batching helps with weight reads, but nobody shares your cache, so agents with long conversations keep the capacity problem growing.

Supply is not waiting for a preprint either. SK Hynix says HBM is effectively sold out through 2029, and TrendForce expects ordinary DRAM to cost about four times late-2025 levels across 2026. Nvidia also asked suppliers to build NVHBM base dies on TSMC's 3nm process, which is not the move of a company expecting memory to vanish. So yeah, NCM is worth watching, but I would say it makes writing cheaper, not remembering smaller.

**For my projects:** Nothing for my projects.

## 21. NVIDIA’s 4B Model That Re-Runs Its Own Layers, by Kai
![](https://i.ytimg.com/vi/XK_hz11tmuc/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=XK_hz11tmuc · **Karakeep:** `dkkur5gavav9bq89wv26388e`

**In short:** NVIDIA's Dory is a 4B model that reruns 20 of its middle layers up to four times per token, and the coding numbers are genuinely strong for an 8GB card. I would say it is worth a look for local coding agents, with the factual recall catch in mind.

**Key points:**
- 4B model, 3.7GB file, 61.8% on SWE-bench Verified at 4 loops, ahead of a 26B Gemma model.
- Eight bottom and eight top layers run once; 20 middle layers can loop 1 to 4 times, controlled by the user.
- Pretrained on 4.5 trillion tokens, then 1.5 trillion more with random loop counts; RL used a difficulty-aware loop curriculum.
- Loop gains show on reasoning tasks: SWE-bench 50.3% to 61.8%, Terminal Bench 12.5 to 22.2, GDP val 815 to 967.
- Pure factual recall barely moves: AA omniscience stays around 10.03 across loop counts.
- Runtime cost is about 2.4x at 4 loops today; wavefront scheduling could cut that to 1.4-1.7x.

**Details:** Dory is a 4 billion parameter model from NVIDIA that re-runs 20 of its middle layers before each token. The bottom eight and top eight layers run once, while the middle 20 can loop one to four times, and the file stays 3.7GB. At one loop it scores 50.3% on SWE-bench Verified; at four loops it scores 61.8%, ahead of a 26B Gemma model. The training story is the interesting part: 4.5 trillion tokens first, then 1.5 trillion more with random loop counts, plus reinforcement learning that sends harder prompts to deeper loops.

The weak point is factual recall, since AA omniscience stays flat around 10.03 while Terminal Bench and GDP val improve. On 8GB or 12GB, the advice is two loops with last loop enabled, all layers on the GPU, and context above 4096; use four loops for long agent runs. A 24GB card is better spent on Gemma 4 26B for facts and science. Four loops costs about 2.4x speed today, though better scheduling could bring that down to 1.4 to 1.7x.

**For my projects:** Nothing for my projects.

## 22. Apple’s Local AI App for Mac Is Coming (Harbor), by Kai
![](https://i.ytimg.com/vi/y9YXhEEwAwc/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=y9YXhEEwAwc · **Karakeep:** `suhp7wnoq5zbccr2rfxoilyb`

**In short:** Harbor is Claris's private Apple Silicon AI server for Macs, still in private preview with no price or ship date. I would say it is interesting for regulated offices, not a free personal ChatGPT replacement.

**Key points:**
- Claris, Apple's FileMaker subsidiary, posted then pulled Harbor from the App Store on November 10; the launch post drew over 732,000 views.
- It is meant to run as a local endpoint on Apple Silicon Macs, with multiple Macs pooled over Thunderbolt 5 and no per-token cloud fees.
- The clustered Mac screenshots are marketing mockups: RDMA was not enabled and the sidebar said standalone mode.
- A 16GB Mac screenshot proves the app opens, not that it runs a model; about 4GB would be left for an 11.4GB model.
- Claris has not said what it costs, when it ships, or whether the privacy toggle replaces recovery-mode RDMA setup.
- macOS 26.2 already ships RDMA over Thunderbolt; LM Studio and EXO already cover much of the same ground for free.

**Details:** Harbor is a private AI server for Macs, built by Claris rather than Apple's main software team. It gives other apps on the network an API address, so coding tools and document assistants can ask a Mac on the shelf and nothing leaves the building. That is the real appeal: local models, no seat bill, no cloud privacy question.

The catch is that it is enterprise software aimed at small offices with compliance worries. Pooling memory needs Thunderbolt 5 on every Mac, and the pretty three-Mac screenshot was not a working cluster. Setup is still the hard part too, since Apple's RDMA instructions still mean recovery mode and terminal commands; Jeff Gerling's four-Mac Studio test only worked when it worked. Claris has not published price, ship date, inference engine or batching, and its Technote still says recovery mode.

For a solo user, LM Studio is the better answer today: it is free, batches requests and serves an API. For a regulated office, Harbor is worth following, but size the Mac for the longest real document, not the biggest model, and ask how long the tenth person waits. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 23. Deepseek V4.1 Flash Runs With No GPU Just 64GB RAM, by Kai
![](https://i.ytimg.com/vi/wiMs92u-dk0/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=wiMs92u-dk0 · **Karakeep:** `bcid4n3twzmryzgul85dksps`

**In short:** DeepSeek V4-0731 is a 284B model that Syncopate's Lama Mod Chip squeezes into 56.93GB on a CPU, and the perplexity hit is 60.8%, so I would say it is not worth buying RAM for.

**Key points:**
- DeepSeek V4-0731 is MIT licensed, has 284.33B parameters, and scores 82.7 on Terminal Bench 2.1 versus 85.0 for Opus 4.8.
- The official download is 155GB; UnSloth's smallest version is 76.87GB and still runs out of memory on 64GB Linux.
- Lama Mod Chip is by Syncopate, Apache 2, went up on 29 Oct, and patches Llama.cpp with a 56.93GB DeepSeek file.
- On a Ryzen 99955HX with 64GB DDR5 it writes 8.66 tokens per second with all experts active.
- Perplexity on Atomic Chat's test set rises from 4.54 to 7.30, a 60.8% increase printed in the README.
- The same developer's Nemotron 30B rises 6.92% and runs at 22.44 tokens per second.

**Details:** DeepSeek V4-0731 is a mixture of experts model with 43 layers, 256 experts plus one shared expert per layer, and six active at a time, so about 13.17B parameters do the work while 284B sit in RAM. The headline file is 56.93GB and fits in 64GB with room for the OS, running at 8.66 tokens per second on a 16-core Zen 5 laptop chip. That is the impressive part, and the repo has over 1000 stars with reproduced runs.

The quality story is less pretty. A lossless score of 1 only compares the patched engine with an unpatched engine on the same 56GB file, so it says the speed tricks do not change answers. It says nothing about the distance from DeepSeek's weights. The newer perplexity number does: 4.54 for the official weights against 7.30 for the 64GB file, a 60.8% rise. The GPU path can move that by 4-5%, and the test is Wikipedia prose, not code, so treat it as early data. For comparison, the same developer's Nemotron 30B, squeezed to a smaller size, rises 6.92%. An old 512GB DDR4 box can run DeepSeek's native 144GB file with 0.2% perplexity loss on stock llama.cpp, and a pair of 2012 Xeon E5-2670s runs the 30B model at 10.69 tokens per second.

I would say do not buy 64GB specifically for this. The headline minimum works, and 96GB with an extra $460 buys roughly two-thirds of the quality back. If you already have 64GB and a supported chip, try it for chat, drafts and quick work, and keep a smaller high-precision model like Nemotron 30B for the things that matter. Nothing for my projects here, though the engineering is worth watching.

**For my projects:** Nothing for my projects.

## 24. Don’t Buy a Mac for AI Until You Watch This, by Kai
![](https://i.ytimg.com/vi/ixy-xP2gMnA/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=ixy-xP2gMnA · **Karakeep:** `alm96n72zrwqcx78e8cbcf4c`

**In short:** Kai's video is a buying guide for Macs used for local AI, and the useful argument is about dates rather than specs: return windows, shipping delays and memory prices. I would say the warning against buying RAM for a model you might run someday is the part worth keeping.

**Key points:**
- The $899 Mac Mini with the M6 chip can arrive this week and qualifies for the extended return window to January 8.
- The Mac Studio with M5 Ultra ships 7-8 weeks out, 10-12 weeks for 512GB, and gets only 14 days to return.
- Apple charges about $25 per GB on most memory steps, but the final 256GB to 512GB step costs $11,500 instead of $6,400; on the $22,299 Studio roughly $15,500 is RAM.
- macOS leaves about 107GB usable on a 128GB M5 Max, and about 72GB on a 96GB Studio by default.
- Apple raised prices: the M3 Ultra Studio went from $3,999 to $5,299, the M5 Ultra starts at $5,499, and the 14-inch MacBook Pro starts $400 higher than a year ago.

**Details:** Kai's point is that the calendar matters more than the spec sheet, and I think that holds up. The cheapest Mac gets the longest trial, because the $899 Mac Mini with the M6 chip can land this week and falls under the holiday return window to January 8, while the Mac Studio with M5 Ultra ships 7-8 weeks out and gets 14 days. So the machine that most needs testing gets the least time to test it.

The memory maths is the other thing. Apple mostly charges $25 a gig, but the last 256GB step costs $11,500 instead of $6,400, and on the $22,299 Studio about $15,500 is RAM. The shortage is real too: 512GB of plain DDR5 is already around $15,000 on Newegg. That makes future-proofing the expensive phrase.

The practical advice is good: run your real workload in the return window, watch memory pressure, test heat, try another inference engine, and if the machine cannot arrive before Christmas, rent the equivalent cloud model first. I would say the verdict is sound: buy what you can prove you need, and do not buy gigabytes for a model you might run someday. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 25. Attention Required! | Cloudflare, by Cloudflare
![](https://9to5linux.com/favicon.ico)
**Source:** https://9to5linux.com/shelly-3-3-gui-package-manager-for-arch-linux-brings-new-built-in-theme · **Karakeep:** `tpqdi1wq6dkidvvmyagzi7xl`

**In short:** Shelly 3.3 is a free open-source GUI package manager for Arch Linux and derivatives, and this release is mostly theme and Updates page polish. I would say it looks nicer, but it is not something I need.

**Key points:**
- Shelly 3.3 was released on 14 November 2026, ten days after Shelly 3.2.
- New default look inspired by Devario's Pearl DE, with windows, circular window controls, accent selections, card-style toolbars and larger page titles.
- Follows desktop light or dark preference by default; Light, Dark and Follow system are available under Settings > Look & Feel.
- Updates page shows source filters with package counts for System, AUR and Flatpak, total download size, individual AUR and Flatpak selection, and matching upgrade buttons.
- Progress card shows download and install stages, compact rows mark pending, downloading, building, completed and failed, and terminal output starts collapsed.
- Install or update with sudo pacman -S shelly or yay -S shelly; binaries and source tarball are on GitHub.

**Details:** The useful part is under the hood: update checks now recover from temporary contention with the tray after an upgrade, and restart handling recognises display-manager aliases including Plasma Login Manager, so session-critical services are reported instead of restarted automatically. The rest is presentation, but it is presentation with package counts, download size and per-source selection visible before you commit. It is an Arch GUI over pacman-style work with AUR and Flatpak mixed in. Nothing here touches my projects. No Kubernetes path, no backup story, no metrics, and I do not run Arch as a target. So yeah, that's that.

**For my projects:** Nothing for my projects.

## 26. 8 Best Free and Open Source Linux Reference Management Tools - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2019/10/reference-management.png)
**Source:** https://www.linuxlinks.com/referencemanagementtools/ · **Karakeep:** `t8zlhhz78lltd464txth6r9a`

**In short:** LinuxLinks lists eight free and open source Linux tools for storing and formatting bibliographic references; useful for researchers and authors, and nothing for my projects.

**Key points:**
- Eight tools named: KBibTeX, Zotero, JabRef, WIKINDX, BibLaTeX, I, Librarian, Citations and Papr.
- All featured software is free and open source.
- Reference management software records bibliographic citations and filters them into formats needed by scholarly journals and publishers.
- Typical functions include importing references, managing and editing them, exporting them and formatting bibliographies to international standards.
- The article is a LinuxLinks roundup updated to reflect changes from a recent announcement.

**Details:** LinuxLinks describes reference management software as a database-backed way to record bibliographic citations, filter them into formats wanted by scholarly journals and publishers, and cut down the tedious collecting and organising of sources. The roundup names eight free and open source Linux options: KBibTeX, Zotero, JabRef, WIKINDX, BibLaTeX, I, Librarian, Citations and Papr. It frames them for academics and authors, with functions such as importing references, managing and editing them, exporting them and formatting bibliographies to international standards. I read it as a catalogue entry, with no benchmarks or versions to compare, so I would not pick a winner from this page alone. It is useful if you write papers and live on Linux. For my own projects it has no fit: nothing here is a Kubernetes tool, image model helper, code factory stage or agent skill. So yeah, that's that.

**For my projects:** Nothing for my projects.

**Projects:**
- [KBibTeX](https://github.com/KDE/kbibtex): An editor for bibliographies used with LaTeX. Contribute to KDE/kbibtex development by creating an account on GitHub.
- [Zotero](https://www.zotero.org/): Zotero is a free, easy-to-use tool to help you collect, organize, cite, and share research.
- [JabRef](https://github.com/JabRef/jabref): Desktop app for managing BibTeX and BibLaTeX (.bib) libraries - JabRef/jabref.
- [WIKINDX](https://wikindx.sourceforge.io/): Wikindx.sourceforge.io.
- [BibLaTeX](https://github.com/plk/biblatex): Biblatex is a sophisticated bibliography system for LaTeX users. It has considerably more features than traditional bibtex and supports UTF-8 - plk/biblatex.
- [I, Librarian](https://github.com/mkucej/i-librarian-free): I, Librarian - open-source version of a PDF managing SaaS. - mkucej/i-librarian-free.
- [Citations](https://gitlab.gnome.org/World/citations): World / Citations · GitLab.
- [Papr](https://github.com/AfrozSaqlain/Papr): Papr is a fast terminal-based workspace written in Rust. Get daily new papers in your feed from your field of research, search, discover, and download papers directly from arXiv. Organize your libr...

## 27. Glance - terminal-based Git diff review and merge tool - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2020/01/Git-Clients.jpg)
**Project:** [glance](https://github.com/polyphilz/glance)
**Source:** https://www.linuxlinks.com/glance-terminal-based-git-diff-review-merge-tool/ · **Karakeep:** `d8fdcoie2kkdkvx0up1br8t9`

**In short:** Glance is a terminal Git diff review and merge tool built around Neovim, written in Lua and released under the MIT licence by Rohan Bansal. I would say it is quite good for manual terminal review, but it is not worth it for my automated code-factory flow.

**Key points:**
- Terminal application for reviewing Git changes, built around Neovim, with a clean separate configuration.
- Side-by-side diff views with syntax highlighting and a minimap.
- Unified file tree covering staged, unstaged, untracked and conflicted files.
- Stage, unstage and discard individual files or changes; resolve conflicts in a three-way merge editor.
- Floating multiline commit editor, commit history browsing, and copying commit hashes.
- Auto-refresh on repository changes, configurable themes and layouts, optional Tree-sitter highlighting, Linux and macOS support.

**Details:** Glance is a terminal Git diff review and merge tool built around Neovim, written in Lua and released under the MIT licence by Rohan Bansal. It launches in its own editor instance with a clean configuration, so the review setup stays separate from an existing Neovim config while keeping familiar keys. It has side-by-side diffs, syntax highlighting and a minimap, plus a unified file tree for staged, unstaged, untracked and conflicted files. You can stage, unstage and discard changes, resolve conflicts in a three-way editor, write multiline commits, browse history and copy hashes. It refreshes when the repository changes, and themes, layouts, keymaps and Tree-sitter highlighting are configurable. Cross-platform support covers Linux and macOS. That is a lot of manual review surface, and I would say it is quite good for someone who wants structure in the terminal. Unfortunately it still leaves me reading the diff myself, so for code-factory it is not worth it. Nothing for my projects. So yeah, that's that.

**For my projects:** Nothing for my projects.

## 28. Attention Required! | Cloudflare, by Cloudflare
![](https://9to5linux.com/favicon.ico)
**Source:** https://9to5linux.com/ubuntu-27-04-tenacious-t-rex-daily-builds-are-now-available-for-download · **Karakeep:** `kaoy4mhptyl3ekwptufwk43s`

**In short:** Canonical has put out the first daily build ISOs for Ubuntu 27.04 “Tenacious T-Rex”, based on 26.10, with a final release due April 22nd, 2027. I would say it is tester territory only, and nothing for my projects.

**Key points:**
- First daily builds published November 14th, 2026, by Canonical.
- Based on Ubuntu 26.10 “Stonking Stingray”; currently Linux kernel 7.3 and GNOME 51.
- Final release expected April 22nd, 2027; beta on April 1st; release candidate on April 15th.
- Nine months of support, ending January 2028.
- Expected stack includes GNOME 52, Mesa 26.3, GCC 16.2, Python 3.15 and GNU Binutils 2.47.
- One commenter reports an upgrade from 26.10 fixed Thunderbolt and trackpad issues and improved battery life on Dell and Lenovo laptops.

**Details:** Canonical published the first daily build ISO images for Ubuntu 27.04, codename Tenacious T-Rex, on November 14th, 2026. They are based on Ubuntu 26.10 and currently ship Linux kernel 7.3 with GNOME 51. Over the six month cycle they should pick up newer pieces such as Linux 7.4 or 7.5, Mesa 26.3, GNOME 52, GCC 16.2, Python 3.15 and GNU Binutils 2.47, and the final release is expected to land on Linux 7.6 with GNOME 52.

Unfortunately these are pre-release builds, so bugs and broken bits are expected and they should not go on a production machine. The final GNOME 52 and Linux 7.6 are still to come, while the first daily builds already have kernel 7.3 and GNOME 51. Support runs nine months to January 2028, which that's short for anything I would put near my cluster, so I would say skip it for now.

One comment says an upgrade from 26.10 fixed Thunderbolt and trackpad issues on Dell and Lenovo laptops and improved battery life, which is nice, but it is still one person's report. Nothing for my projects. So yeah, that's that.

**For my projects:** Nothing for my projects.

## 29. EJDB2 - embedded JSON database - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2019/03/online-business-database.jpg)
**Source:** https://www.linuxlinks.com/ejdb2-embedded-json-database/ · **Karakeep:** `voypaf114npc5cmzhwx0bdtm`

**In short:** EJDB2 is a MIT-licensed embedded JSON document database written in C by Softmotions Ltd. I would say it is useful for small local apps, but it is not a replacement for Postgres in my homelab.

**Key points:**
- Embedded document database for JSON records, stored in a single file via IOWOW.
- JQL query language with XPath-inspired syntax, plus nested queries, indexing and collection joins.
- Online backups, HTTP REST and WebSocket access, and a native programming interface.
- Document creation, modification, deletion and patching are supported.
- Written in C, MIT licensed, and runs on Linux, macOS and FreeBSD.

**Details:** EJDB2 keeps JSON documents in collections inside one file, so there is no separate database server to run. It queries them with JQL, which the article describes as XPath-inspired, and it supports nested structures, joins, indexing, document patching, creation, modification and deletion. There is online backup while it runs, plus HTTP and WebSocket interfaces for other processes. That is a decent feature list for an embedded store. The catch for me is that it is still a single-file database with no Kubernetes path in the article, and my homelab already runs Postgres on CloudNativePG with backups to MinIO. Nothing here changes that. I would say it is a neat tool for a small app, but nothing for my projects.

**For my projects:** Nothing for my projects.

## 30. Review your design docs with fresh eyes, not full context, by Open-source Projects
![](https://opengraph.githubassets.com/1/google/elephant-goldfish-model)
**Project:** [github.com](https://github.com/google/elephant-goldfish-model)
**Source:** https://www.opensourceprojects.dev/post/elephant-goldfish-model · **Karakeep:** `dgihmk6y2v6iwri55p156o3f`

**In short:** Elephant-Goldfish Model is a Google plugin that has one model draft a spec with full context, then has separate reviewers read it cold. I would say it is a small, sensible idea for catching blind spots in design docs, not a platform.

**Key points:**
- Built by Google as a plugin for AI coding assistants; repo is github.com/google/elephant-goldfish-model.
- The elephant holds project context and drafts the spec; goldfish reviewers see the draft and referenced material without the earlier conversation.
- Installs across ChatGPT and Codex desktop, Antigravity, Claude Code and Codex CLI, with setup notes for Claude Cowork and ChatGPT Work.
- Can review an existing Markdown doc against live code with /egm:egm-review and check a folder for doc/code drift with /egm:egm-drift-report.
- The README says you make the architectural trade-offs and approve the spec; it is not an autopilot.

**Details:** The idea is simple: the same assistant that helped write a spec is a poor critic of it, because it remembers the reasoning. EGM splits the job so the drafter keeps the context and the reviewers start cold. That is the part I like. It also works on docs you already have, so you can point /egm:egm-review at a Markdown design doc and have it check the design, clarity, fit with the codebase and implementation plan. The drift report is the other useful bit: compare a folder of docs with current source and decide which side to fix. It is narrow and slots into tools I already use, with one or two install commands. I would say it is worth trying on a doc you have already written, especially if design docs rot next to the code. The catch is that brainstorming and review need a session that can create fresh reviewers, so setup matters.

**For my projects:**
- code-factory: Add EGM as the cold review between the PM spec and the Tester: run /egm:egm-review on each work-order spec, then /egm:egm-drift-report on docs/designs before implementation.

## 31. A virtual display you can add, remove, and get screen updates from, by Open-source Projects
![](https://opengraph.githubassets.com/1/displaylink/evdi)
**Project:** [evdi](https://github.com/displaylink/evdi), also [evdi](https://github.com/DisplayLink/evdi)
**Source:** https://www.opensourceprojects.dev/post/evdi · **Karakeep:** `cx3n1hrhdxq4nvnik7o5wlde`

**In short:** EVDI is a Linux kernel module that creates on-demand virtual displays and hands screen updates to userspace through libevdi; I would say it is solid infrastructure for display tooling, but nothing for my projects.

**Key points:**
- Linux kernel module plus libevdi, with pyevdi as a Python wrapper.
- Virtual displays integrate with the standard DRM subsystem, so xrandr and GNOME, KDE and Unity display tools can manage them.
- Minimum kernel 4.15; verified with Ubuntu variants up to 6.15.
- Packaging covers deb on Ubuntu, community RPMs for Fedora, CentOS Stream, Rocky Linux and AlmaLinux, plus an AUR package.
- It is not a complete DisplayLink driver on its own, and kernel-to-libevdi communication is not access-controlled or authenticated yet.

**Details:** EVDI is a virtual display you can create and remove on Linux, with screen updates going to userspace through libevdi. It plugs into the standard DRM subsystem, so xrandr and desktop display tools can see the virtual screen. There is also pyevdi for Python. The minimum kernel is 4.15, with verified support up to Ubuntu variants of 6.15, and packaging covers deb, RPM for Fedora, CentOS Stream, Rocky Linux and AlmaLinux, and AUR. It is not a complete DisplayLink driver on its own, and the kernel-to-library channel is not access-controlled or authenticated yet. I would say it is a sensible primitive for remote desktop or capture tooling, but nothing for my projects.

**For my projects:** Nothing for my projects.

## 32. A bash script that emails Sam Altman about your unused RAM, daily, by Open-source Projects
![](https://opengraph.githubassets.com/1/iainkay/ram-altman)
**Project:** [github.com](https://github.com/IainKay/ram-altman.git)
**Source:** https://www.opensourceprojects.dev/post/ram-altman · **Karakeep:** `yvgcyp60hqzw7p1lfeamaz80`

**In short:** ram-altman is a bash script that emails Sam Altman once a day about idle RAM, and I would say it is a funny, well made joke rather than a tool worth running.

**Key points:**
- Sends at most one email per day, with 8 subject lines, 10 messages and 6 sign-offs.
- Checks whether more than 10% of RAM is available before sending.
- Uses MemTotal minus MemAvailable, with a fallback for kernels older than 3.14.
- Logs every sample to CSV and ships with 14 tests.
- Needs Linux, bash and a working sendmail, msmtp or mail command.
- Leans on Sam Altman's Cheeky Pint quote about global DRAM.

**Details:** ram-altman is a small bash script that checks Linux memory and, if more than 10% is available, sends a single email to Sam Altman about RAM that is not in a data centre. It tracks total, used and available memory, handles page cache with MemTotal minus MemAvailable, and on kernels older than 3.14 it estimates from free memory plus reclaimable cache. It also logs every sample to CSV and rotates 8 subjects, 10 messages and 6 sign-offs so the joke does not wear out too quickly.

The testing is real for a joke: 14 tests, plus honest memory accounting that most arguments about RAM never bother with. It needs Linux, bash and a working sendmail, msmtp or mail command. I read about it, I did not run it.

I would say it is well made and still a joke. The premise leans on Sam Altman's Cheeky Pint quote about global DRAM, which is the sort of enterprise theatre OpenAI is good at turning into a talking point. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 33. 479 SVG logos, each under 1KB, averaging 534 bytes, by Open-source Projects
![](https://opengraph.githubassets.com/1/edent/supertinyicons)
**Project:** [SuperTinyIcons](https://github.com/edent/SuperTinyIcons)
**Source:** https://www.opensourceprojects.dev/post/supertinyicons · **Karakeep:** `wm0le0hrz4633aahxea2dxtq`

**In short:** Super Tiny Icons is a set of 479 hand-tuned SVG logos, each under 1KB and averaging 534 bytes. I would say it is worth a bookmark for status pages and docs, but it is not a full icon library.

**Key points:**
- 479 logos, each under 1KB, average under 534 bytes
- GitHub logo is 527 bytes SVG versus 3,328 bytes PNG; Twitter 352 versus 2,987; Flickr 235 versus 1,615
- Consistent 512x512 viewbox with a circle of radius 256
- No build tools, package manager or dependencies; copy the SVG file
- README carries a Zenodo DOI
- Covers developer tools, consumer apps, payment providers, frameworks and Linux distributions

**Details:** Super Tiny Icons is a repository of minuscule SVG versions of well-known logos, from GitHub and Twitter to Alpine Linux and Ansible. Every file is hand-tuned and the average across 479 files is under 534 bytes, with Adobe at 220 bytes and Flickr at 235 bytes. The geometry is consistent too, using a 512x512 viewbox and a circle of radius 256, so icons line up without manual nudging.

The catch is scope. There is no theming, no variants and no CLI; it is just static assets. That is fine for a status page, docs site or offline-first app where every kilobyte counts, and less useful if you need a full icon system. The README also carries a Zenodo DOI, which is a nice signal that the maintainer treats it as a stable reference.

I would say it is a focused, slightly obsessive collection, and that focus is the point. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 34. An open-source framework for authorized social-engineering assessments, by Open-source Projects
![](https://opengraph.githubassets.com/1/trustedsec/social-engineer-toolkit)
**Project:** [github.com](https://github.com/trustedsec/social-engineer-toolkit/)
**Source:** https://www.opensourceprojects.dev/post/social-engineer-toolkit · **Karakeep:** `khxmk280ub47f32tclfytb6l`

**In short:** The Social-Engineer Toolkit is a TrustedSec Python framework for authorized social-engineering assessments, version 8.1.3 on Python 3.11 to 3.13. I would say it looks maintained and serious about authorization, but it is nothing for my projects.

**Key points:**
- Open-source Python framework for authorized social-engineering assessments, maintained by TrustedSec and written by David Kennedy (ReL1K).
- Version 8.1.3 targets Python 3.11 through 3.13 and runs as an interactive console.
- Linux is the primary target, macOS is experimental, and Windows works through WSL or WSL2 with Kali or another supported Linux.
- Install from the Kali repos with apt, from source in a virtual environment, or with the legacy system-wide installer.
- The README states it is only for testing where explicit permission and scope are established.
- Developer loop is editable install, pytest, compileall, then the test suite.

**Details:** SET is an open-source penetration-testing framework for authorized social-engineering assessments, maintained by TrustedSec and written by David Kennedy (ReL1K). It gives security teams guided attack vectors for testing user awareness and running consent-based red-team exercises, rather than assembling tooling from scratch. Version 8.1.3 targets Python 3.11 through 3.13 and runs as an interactive console.

The README is explicit that it is only for testing where permission and scope are established, which is the right tone for this kind of tool. Linux is the primary target, macOS is experimental, and Windows works through WSL or WSL2 with Kali or another supported Linux. You can install it from the Kali repos, from source in a virtual environment, or with the legacy system-wide installer, and the dev loop is editable install, pytest, compileall, then tests.

I have not used it; I only read the project page. It looks like a serious maintained tool for security teams, and the authorization framing is plain. It is nothing for my projects, so I am not picking it up.

**For my projects:** Nothing for my projects.

## 35. A native Excalidraw client for Apple platforms, built with SwiftUI, by Open-source Projects
![](https://opengraph.githubassets.com/1/chocoford/excalidrawz)
**Project:** [ExcalidrawZ](https://github.com/chocoford/ExcalidrawZ)
**Source:** https://www.opensourceprojects.dev/post/excalidrawz · **Karakeep:** `kg20xgcsqf2m5m9414alpq8y`

**In short:** ExcalidrawZ is a native SwiftUI Excalidraw client for macOS, iPadOS and iOS with proper file management, iCloud sync and history; I would say it is worth a look if you draw on Apple hardware, but it is Apple-only and there is nothing for my projects.

**Key points:**
- Native SwiftUI client for Excalidraw on macOS, iPadOS and iOS, from the solo developer behind chocoford/ExcalidrawZ.
- Treats drawings as app documents with groups, custom sorting, iCloud sync and restorable history checkpoints.
- Opens and edits .excalidraw, .excalidraw.png and .excalidraw.svg files, plus local folders and temporary external files.
- AI assistant can read, create and revise drawings, attach image context and show proposal previews; files can be hidden from AI.
- MCP server has a basic mode and an optimized mode with current-file editing, navigation, history, inspection, export and library workflows.
- Also imports PDFs, converts Mermaid diagrams, inserts LaTeX formulas and renders function graphs; available via App Store or direct .dmg.

**Details:** ExcalidrawZ puts the familiar Excalidraw canvas into a native Apple app instead of a browser tab. The useful part is file management: drawings become documents with groups, sorting, iCloud sync across macOS, iPadOS and iOS, and history checkpoints you can restore. It also opens .excalidraw, .excalidraw.png and .excalidraw.svg files, and can pull in local folders or temporary external files.

The extra layer is AI and MCP. An assistant can read, create and revise drawings, attach images for context and show proposal previews before changing the canvas, and you can hide files from it. The MCP server has a basic mode and an optimized mode with deeper current-file, navigation, history, inspection, export and library workflows. It also does PDF import, Mermaid conversion, LaTeX formulas and function graphs. Unfortunately it is Apple-only, so there is nothing for my projects. I would say the file management and history are the real reason to try it.

**For my projects:** Nothing for my projects.

## 36. A Docker Desktop replacement written in Rust, with a 2.5 ms container start, by Open-source Projects
![](https://opengraph.githubassets.com/1/libracoder/kiri)
**Project:** [kiri](https://github.com/libracoder/kiri)
**Source:** https://www.opensourceprojects.dev/post/kiri · **Karakeep:** `chydxlnrel2u8hp1ko8efr6x`

**In short:** Kiri is a Rust container runtime that speaks the Docker Engine API and aims to replace Docker Desktop without the weight. I would say the compatibility story is the interesting part, and the 2.5 ms claim needs your own benchmark.

**Key points:**
- Runs Docker images in one small Linux VM, or directly on Linux, and speaks the Docker Engine API.
- Container start and exit is about 2.5 ms; the README claims roughly 80 times faster than Docker Desktop.
- Daemon is around 15 MB, the VM sleeps after 60 seconds idle and wakes in about 0.15 seconds.
- Supports the docker CLI, Compose, buildx, docker login, amd64 via Rosetta, local domains and a one-command Kubernetes cluster.
- Available for macOS 14+, Windows 10 and 11 via WSL 2, and Linux via deb or rpm; ships in 38 languages.
- Source is Apache-2.0, at libracoder/kiri, and the project self-updates.

**Details:** Kiri is a Rust runtime that runs Docker images in one small Linux VM, or directly on Linux, and speaks the Docker Engine API. That means the docker CLI, Compose and buildx should keep working without a new toolchain. It also has a native window, menu bar item, local domains with HTTPS from its own CA, amd64 through Rosetta, docker login, a one-command Kubernetes cluster and Linux machines. The headline numbers are a 2.5 ms container start and exit, an 80x claim against Docker Desktop, a 15 MB daemon, a 60 second idle sleep and a 0.15 second wake. It ships for macOS 14+, Windows 10 and 11 through WSL 2, and Linux via deb or rpm, with 38 languages including right-to-left layouts. It self-updates and the source is Apache-2.0. The project is young, so the features doc matters more than the headline. I would treat the speed claim as something to benchmark rather than trust.

**For my projects:** Nothing for my projects.

## 37. Solara - reactive Python framework for web and Jupyter applications - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2024/12/030-framework.png)
**Project:** [solara](https://github.com/widgetti/solara)
**Source:** https://www.linuxlinks.com/solara-reactive-python-framework/ · **Karakeep:** `vpxpuvbinr5gqkxl05orfb46`

**In short:** Solara is a reactive Python framework for web and Jupyter apps, MIT licensed, by Maarten Breddels and contributors. I would say it is handy for data apps, but it is another UI layer to keep around.

**Key points:**
- Reactive Python framework for web and Jupyter applications, with a React-style component model.
- Uses Reacton and the ipywidgets ecosystem; runs in Jupyter Notebook, JupyterLab and standalone web environments.
- Standalone server is built around Starlette and FastAPI; cross-platform on Linux, macOS and Windows.
- MIT License; developer Maarten Breddels and contributors.
- Includes reactive hooks, layout components, plots, file browser support, automatic code reloading and type hints.

**Details:** Solara is a reactive Python framework for web and Jupyter apps, built by Maarten Breddels and contributors under the MIT licence. It uses a React-style component model through Reacton and the ipywidgets ecosystem, so the same components can run in a notebook or as a standalone app. Reactive state updates components when dependencies change, and the standalone server is built around Starlette and FastAPI.

I would say it is a decent fit for dashboards and scientific tools, and the shared notebook and web story is the useful part. The missing bit is any version or production deployment detail in the article, so I cannot tell how stable it is beyond the feature list. For my projects, nothing jumps out: it is not a Kubernetes service with backups and metrics, and it is not a factory stage either. So yeah, that's that.

**For my projects:** Nothing for my projects.

## 38. Shield helps technicians hand off legacy portal work with OpenAI, by link
![](https://openai.com/favicon.ico)
**Source:** https://openai.com/business/customer-stories/shield/ · **Karakeep:** `s8iz01fkbwtfumi0o72lphi6`

**In short:** This is an OpenAI customer story about Shield and legacy portal work, and since the page did not load I would not treat it as useful yet.

**Key points:**
- The source body was not available, so there are no facts, numbers, versions, prices or licences to report.
- Only the title is available: Shield, technicians, legacy portal work, OpenAI.
- No candidate links were supplied.
- It sits on OpenAI's business customer-stories channel, so it is a case study rather than a tool I can run.

**Details:** OpenAI's page did not load, so I am working from the title and nothing else. That title points at a customer story about Shield, technicians and legacy portal work. I did not get the workflow, product names, scale or result, so I am not going to pretend I did.

What I can say is that this is OpenAI's business channel, so the shape is familiar: enterprise case study, happy outcome, implied you could buy the same thing. I read about it, I did not try it, and I would not plan anything from a title.

Nothing for my projects.

**For my projects:** Nothing for my projects.

## 39. I was wrong..., by Theo - t3․gg
![](https://i.ytimg.com/vi/5BrgFY5jIn4/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=5BrgFY5jIn4 · **Karakeep:** `ty3ckd5wnt46ktwzz866va3x`

**In short:** Theo's video is a retraction of his earlier Gemini 4 Carbon take: in real work it was consistently five times slower than other models, with over 11 seconds before a response even starts, and he now says not to use it. Verdict: not worth it, get a $20 Claude sub instead.

**Key points:**
- Theo audited real-world usage and found Gemini 4 Carbon consistently five times slower than other models in like-for-like work.
- Requests take over 11 seconds from hitting Google's server to starting a response, and that compounds across multi-step agent turns.
- Artificial Analysis timings are not agentic: they measure from request acceptance to response, so real coding work is much worse.
- Subscription price doubles on 1 December; Vertex hosting is unusable and the reasoning level is baked into the model name.
- The only upside he concedes is slightly less flagging on cybersecurity work; otherwise he says there is no reason to use it.
- He recommends a $20 Claude subscription as the better value.

**Details:** This is Theo crashing out over Gemini 4 Carbon after his previous video gave it too much credit. He says he planned to be negative, found it oddly okay because it did not restrict him, and now thinks he was wrong. The real problem is speed: in like-for-like work it was consistently five times slower than anything else, and nine judge runs got so bad he changed his skill to tell agents to stop waiting for it and get back to work.

The headline number is the 11 seconds before a response starts, on every request, on top of Google's other latency problems. Artificial Analysis timings are not agentic, so the gap is worse in real multi-turn coding work. He also says Vertex hosting is unusable, the reasoning level is part of the model name, and the subscription price doubles on 1 December.

His verdict is blunt: no reason to use it for day-to-day engineering, except maybe cybersecurity where it flags less. He says friends should not let friends use Gemini, and a $20 Claude sub gets more done. I would say the same: speed is the feature, and this one does not have it.

**For my projects:** Nothing for my projects.

## 40. Evangelion - tactical stealth roguelike game - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2022/07/Roguelike.png)
**Project:** [evangelion](https://github.com/eduszesz/evangelion)
**Source:** https://www.linuxlinks.com/evangelion-tactical-stealth-roguelike-game/ · **Karakeep:** `ygdg8oxhxlma4u5eu5kl85j9`

**In short:** Evangelion is a free, GPL v3 Python roguelike about sneaking through twelve levels to recover a book; it sounds like a small text-symbol game rather than something I would build around.

**Key points:**
- Free and open source tactical stealth roguelike by Eduardo Szesz, GPL v3, written in Python.
- Procedurally generated facilities with guards, elite guards, cameras, drones and guard dogs.
- Hazards include laser barriers, sensors, traps and alarm systems; terminals can be hacked.
- Equipment includes EMP devices, antidote kits, smoke bombs, hacking tools and decoys.
- Twelve levels, English and Portuguese interface text, text-inspired coloured symbols.

**Details:** Evangelion is a tactical stealth roguelike by Eduardo Szesz, free under GPL v3 and written in Python. You infiltrate procedurally generated facilities, avoid patrols, cameras, drones and dogs, and try to finish without being detected. There are twelve levels, a religious theme, limited resources, hacking terminals, EMPs, smoke bombs, decoys, secret passages, and a faith mechanic with prayer and preaching. The presentation is text-inspired, with coloured symbols for objects, enemies and terrain, and the interface is English or Portuguese.

It is not for my homelab or image work, and there is no real fit with code-factory or agents. It is a game to read about, maybe try on a Linux box, but I would not call it a tool for anything I build. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 41. This $40 AMD GPU is Insane!, by Budget-Builds Official
![](https://i.ytimg.com/vi/ZBuL38dydcM/maxresdefault.jpg)
**Source:** https://youtu.be/ZBuL38dydcM?si=UsydDIDMoo1LsNUI · **Karakeep:** `eggaacwd2lvvjruwpl7wb6ra`

**In short:** A Budget-Builds Official video about a used AMD Radeon Pro WX 5100 that sells for around £30 to £40, with a BIOS mod turning it from a 30 FPS Cyberpunk card into something near 60 FPS. I would say it is good value for a low-power single-slot card, but only if you are happy to flash the BIOS.

**Key points:**
- Budget-Builds Official tests a used AMD Radeon Pro WX 5100, around £30 to £40 on eBay, single slot, no six-pin power, four DisplayPort outputs.
- Stock Pro drivers gave a 3DMark score of about 1700 and Cyberpunk at roughly 30 FPS on low and medium settings at 1080p.
- Modded RX 580X drivers added only 12 3DMark points and 0.2 FPS, so they were not the fix.
- A Polaris BIOS Editor flash unlocked the full 75 W, raised memory to 1850 and tightened timings; 3DMark rose to 3040 and Cyberpunk reached nearly 60 FPS.
- The card stayed under 70 W, and the video shows it running in an old Ivy Bridge i7-3770S system with a 300 W PSU.
- Driver updates look bleak, and the video says these are still used by businesses, so prices may fall later.

**Details:** The card is based on Ellesmere, 14 nm, 1792 shaders and 8 GB of GDDR5, but shipped clocked low. Out of the box it is quiet and draws no extra power, which makes it attractive for small or old machines, but the stock BIOS leaves a lot on the table. The useful part of the video is the modding path: save the VBIOS with GPU-Z, edit it in Polaris BIOS Editor, flash it, then use the WX drivers to avoid a code 43 error. That took about five minutes and roughly doubled the score, landing within 250 points of the best recorded result. The catch is that it is not a plug and play card, and the video is clear that the drivers are not gaming-focused. Nothing for my projects: I do not have a PC build or workstation upgrade on the list, and my image work is on the M1 Max.

**For my projects:** Nothing for my projects.

## 42. Portable Linux cheaper than a Raspberry Pi, by Tall Paul Tech
![](https://i.ytimg.com/vi/9M43oITcjUQ/maxresdefault.jpg)
**Source:** https://youtu.be/9M43oITcjUQ?si=5K2aVjUyCCX5xsa8 · **Karakeep:** `myesn7d0c2i8mp8qj3zt5kvz`

**In short:** This is a ten-dollar AliExpress 4G stick, model UZ801, that Tall Paul Tech reflashes with Debian via OpenStick. I would say it is cheap and clever, but the flashing is fiddly and the route handling is wonky.

**Key points:**
- Ten-dollar AliExpress 4G modem sticks, model UZ801, running Android stock.
- Reflashed to Debian using the OpenStick project after an EDL backup of the whole eMMC.
- Root filesystem starts at 1.5 GB and is resized to about 3.4 GB on a 3.6 GB device.
- Has Wi-Fi, USB and mobile WAN interfaces; the APN ends up as Telstra internet.
- SNMP shows low CPU use and a temperature sensor; mode is set to 4G only with retry.
- Flashing took about 14 minutes; he plans to use it as an OpenSense uplink for redundancy.

**Details:** I watched Tall Paul Tech turn a ten-dollar 4G dongle into a Debian box. He backs up the whole eMMC first, because the IMEI and radio calibration live in partitions, then flashes OpenStick Debian, restores the modem bits, and resizes the root from 1.5 GB to 3.4 GB. After that it gets an IP, SSH works, and he sets the APN to Telstra internet, 4G only, with retry on poor signal. SNMP shows low CPU use and a temperature sensor. It has Wi-Fi, USB and mobile WAN, so it is more than a modem. But the default route can take over the laptop, ping needs sudo, and the whole thing is a fiddle. I would say it is interesting as a toy or a failover stick, not as something I would trust without more work.

**For my projects:**
- homelab-2nd: Try one as a cheap 4G failover uplink for OpenSense, using its SNMP metrics; it is not a Kubernetes workload and has no backup story, so treat it as a manual box.
