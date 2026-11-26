---
date: 2026-11-25
slug: 2026-11-25-morning-brew
tags: libcurl, Command Line Tools, URL Manipulation, Trurl, URL Parsing, Homelab, LAN Party, Servers, Cloud Gaming, Craft Beer, Open Source Software, Ripgrep, Desktop Search, Searchmonkey III
---

Morning Brew for 2026-11-25: 35 items written from 37 hoarded bookmarks and feeds, 2 dropped after a failed retry.

### RSS

## 1. trurl - parse and manipulate URLs - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2022/06/170y-utilities.jpg)
**Source:** https://www.linuxlinks.com/trurl-parse-manipulate-urls/ · **Karakeep:** `bs6fdovuz8a3sjpzbubz3qhe`

**In short:** trurl is a curl-project command-line tool for parsing and rewriting URLs; I would say it is quite useful for shell scripts, but it is not a fetcher.

**Key points:**
- Developed in the curl project by Daniel Stenberg and contributors, using libcurl's URL parser.
- Parses, constructs and manipulates hierarchical URLs per RFC 3986, with libcurl extensions.
- Extracts components such as scheme, host, port, path, query, fragment and credentials, and handles IPv6 zone identifiers.
- Can append, replace, remove or sort query parameters, strip tracking parameters and normalise paths.
- Written in C, cross-platform on Linux, macOS and Windows, released under the curl License.
- Works on URL strings only; it does not transfer data over the network.

**Details:** It is the URL cousin of curl: one job, parse and manipulate addresses consistently with curl itself. Scripts can pull components out, build a URL from pieces, resolve redirects, handle IDNs and Punycode, and emit JSON. That is a lot of small URL jobs without regex. I would say it is worth keeping in the toolkit for shell work, especially query cleanup, but it is a utility around strings, so it will not replace curl for actual requests. Nothing for my projects, since none of my current pipelines need a dedicated URL parser and I am not about to add one for the sake of it.

**For my projects:** Nothing for my projects.

## 2. Cloud Gaming Server at a LAN Party w/ YCHTO; No Politics No Jensen - Talking Heads Ep.459, by Craft Computing
![](https://i.ytimg.com/vi/it8u2rWbxcU/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=it8u2rWbxcU · **Karakeep:** `qbp34c1xd4uo39ptdcbrwxqb`

**In short:** A Craft Computing Talking Heads episode about running a cloud gaming server at a LAN party, with no transcript available here. I would say there is nothing actionable in the title alone.

**Key points:**
- Source is a YouTube video from Craft Computing, episode 459 of Talking Heads.
- Title mentions a cloud gaming server at a LAN party with YCHTO.
- Title also says no politics and no Jensen.
- No transcript or article body was available.
- No versions, prices, benchmarks, setup details or candidate links can be taken from it.

**Details:** This is a Craft Computing Talking Heads episode, number 459, titled around a cloud gaming server at a LAN party with YCHTO, and it promises no politics and no Jensen. I could not get the transcript or page text, so I cannot tell what stack they used, what hardware was involved, or whether the result was stable. From the title alone it sounds like a fun event build rather than something I would copy into my homelab. I would not put a cloud gaming server on my cluster, and I do not have a LAN party to justify one. Nothing for my projects. So yeah, that's that.

**For my projects:** Nothing for my projects.

## 3. Searchmonkey III - real-time desktop search - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2021/10/search-searching-internet-finding-seeking-quest-concept.jpg)
**Source:** https://www.linuxlinks.com/searchmonkey-iii-real-time-desktop-search/ · **Karakeep:** `nnllkgb29mz9c4gghprwrg3w`

**In short:** Searchmonkey III is a ripgrep-backed desktop search GUI with no persistent index; I would say it is quite good for code and logs, but too much for a whole-disk search.

**Key points:**
- Desktop search application from Axonara Ltd, written in Rust with a Tauri and SvelteKit interface.
- Uses ripgrep and searches files directly on disk instead of maintaining a persistent index database.
- Streams matching results to the GUI while a search is running.
- Supports literal text and regular expressions, case-sensitive matching, glob include and exclude patterns, hidden files, optional symlink traversal, and ignore-file overrides.
- Reports skipped, filtered or inaccessible files, shows configurable context lines, and has a command-line interface.
- Optional commercial plugins add PDF text extraction, office document processing and OCR; cross-platform on Linux, macOS and Windows; MIT licence.

**Details:** Searchmonkey III has no persistent index, so every search reads the disk; that is the bad news. It is a desktop search application from Axonara Ltd, built in Rust with a Tauri and SvelteKit interface, and it uses ripgrep as the search engine, so there is no index database to maintain. It streams matches into the GUI while a search runs, so you see results as they arrive, and it supports literal text and regular expressions, case-sensitive matching, glob include and exclude patterns, hidden files, optional symlink traversal, ignore-file rules with an override, context lines, a match cap, and configurable applications for opening matches. It also reports skipped, filtered or inaccessible files, and has a command-line interface for searches and file-manager actions.

The document side is split off: optional commercial plugins handle PDF text extraction, office documents and OCR. It runs on three platforms, which that's decent, and the licence is MIT. I would say it is quite good for code and logs, but too much for a whole-disk search. So yeah, that's that.

**For my projects:** Nothing for my projects.

## 4. How to Run Inkling 2 Mini Locally on an RTX 3090 Using Unsloth Studio - KDnuggets, by KDnuggets
![](https://www.kdnuggets.com/wp-content/uploads/awan_run_inkling_2_mini_locally_rtx_3090_unsloth_studio_3.png)
**Source:** https://www.kdnuggets.com/how-to-run-inkling-2-mini-locally-on-an-rtx-3090-using-unsloth-studio · **Karakeep:** `xdirexo8a7h7geuvw6csfrze`

**In short:** Inkling 2 Mini is a 26B open-weight model from Thinking Machines Lab that the tutorial runs locally on an RTX 3090 through Unsloth Studio; I would say it looks capable for coding, but it needs real GPU hardware and is not a fit for my small machines.

**Key points:**
- Thinking Machines Lab released Inkling 2 Mini with 26 billion parameters, Mixture-of-Experts and a looping mechanism.
- It matches Qwen3.8-27B on the Artificial Analysis Intelligence Index and beats it on several coding, agentic and tool-use benchmarks.
- The tested build is unsloth/Inkling-2-Mini-GGUF with UD-Q4_K_XL, a 4-bit quantization that fits one RTX 3090 with 24GB VRAM.
- Unsloth Studio serves the model locally; the tutorial reports about 52 tokens per second on that GPU.
- They connect it to the Pi coding agent through an API on port 8080.
- Tests include web search, an oil market dashboard and a coding task through Pi.

**Details:** Thinking Machines Lab has released Inkling 2 Mini as an open-weight model, and the KDnuggets tutorial shows it running on one RTX 3090 through Unsloth Studio. The model has 26 billion parameters with a Mixture-of-Experts design and a looping mechanism, and the 4-bit quantized build is the one that fits 24GB of VRAM. They report about 52 tokens per second on that card, which is decent for a model of this size.

The tutorial is practical rather than benchmark-heavy. It installs Unsloth Studio, loads unsloth/Inkling-2-Mini-GGUF with UD-Q4_K_XL, then tests web search, an oil market dashboard and a connection to the Pi coding agent on port 8080. The dashboard example is the nice part: it simulated live price movement even though markets were closed.

I read this as another useful local-model recipe, not a new capability. It needs an RTX 3090 for the tested setup, so it is not something I can casually run on the M1 Air. I would say it is worth a look if you already have that GPU and want a local coding model behind Pi.

**For my projects:** Nothing for my projects.

## 5. 17 million lines of AI slop just cracked a 167-year-old math problem..., by Fireship
![](https://i.ytimg.com/vi/Jatwf_XOncE/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=Jatwf_XOncE · **Karakeep:** `y6ekqfaljxic4jt5y8qbxk7a`

**In short:** A Fireship report on a claimed Lean proof of the Riemann hypothesis produced with Claude over 41 days, plus a separate VP versus VNP claim by Anthropic. I would say it is more AI slop and hype than a usable result, and nothing for my projects.

**Key points:**
- Levent Alpagay announced a four-page PDF on his personal website after 41 days of work with Claude.
- The proof is 17 million lines of Lean, and a function called any geometry just returned true and was used 118 times.
- Terence Tao had predicted humans plus AI would reach this around 2050; Alpagay announced it last Friday.
- The Clay Institute bounty is one million dollars, but requires a published paper and a two-year wait.
- Alessandro Masulo's separate 940-page hand-written proof was rushed out the same night and people found problems within eight hours.
- Anthropic posted a Monday paper claiming VP versus VNP, with Claude as the only author and 73,000 lines of Lean, and no human mathematician has checked it.

**Details:** So a guy named Levent Alpagay says he and Claude produced a proof of the Riemann hypothesis in 41 days, and the whole thing is 17 million lines of Lean. The catch is that nobody understands it, including him, and a function called any geometry just returned true 118 times. I read that as leftover slop, and Jenny Nielsen published a paper declaring it invalid before others found almost nothing depended on that function.

There was also a rush job from Alessandro Masulo, 940 pages by hand over 12 years, which people started breaking within eight hours after feeding it into Claude. Then Anthropic posted a VP versus VNP claim on Monday with Claude as the only author and 73,000 lines of Lean, and no human mathematician has checked it yet.

The practical bit is small. The hypothesis was already assumed true, so encryption and primes do not suddenly change. Terence Tao had it around 2050, and this took 41 days, which is the real shock. But it is still not a paper, so the million dollar bounty is not collectable yet. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 6. MISO - Laboratory Information Management System for Sequencing - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2020/09/modern-laboratory-interior.jpg)
**Project:** [miso-lims](https://github.com/miso-lims/miso-lims)
**Source:** https://www.linuxlinks.com/miso-laboratory-information-management-system/ · **Karakeep:** `wawg8hze2rvhbpiesy3i8e6j`

**In short:** MISO is a free, open source Java LIMS for next-generation sequencing facilities, from the Ontario Institute for Cancer Research and Earlham Institute. It looks like quite a good fit for that niche, but nothing for my projects.

**Key points:**
- Free and open source, licensed under GNU GPL v3.0.
- Written in Java; source is at github.com/miso-lims/miso-lims (link 1).
- Developed by the Ontario Institute for Cancer Research and Earlham Institute.
- Tracks samples, libraries, pools and runs, with metadata, search and reporting.
- Supports different levels of sample detail and integration with sequencing infrastructure.

**Details:** MISO is a laboratory information management system for next-generation sequencing facilities. It gives a structured way to tie biological material to preparation history, sequencing requirements and instrument runs, instead of disconnected spreadsheets. It covers registration and tracking of samples, sample attributes and project information, library preparation, pools, runs, sample hierarchies, workflows and laboratory metadata. It also has search, reporting and data access, plus integration with related sequencing infrastructure. The article does not mention a version, and it does not mention Kubernetes, backups or metrics. For my homelab that matters, so I would leave it. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 7. CORAL - electronic resource management system - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2019/02/young-adult-working-library-office.jpg)
**Project:** [coral](https://github.com/coral-erm/coral)
**Source:** https://www.linuxlinks.com/coral-electronic-resource-management-system/ · **Karakeep:** `f11ue3a3tqwv2eubslprokyg`

**In short:** CORAL is a free, modular electronic resource management system for libraries, written in PHP and licensed under GPL v3. It looks capable for that niche, but there is nothing in it for my projects.

**Key points:**
- Designed for libraries managing electronic journals, databases, subscriptions and licensed resources.
- Modular: resources, licensing, organisations, management and usage statistics modules can run independently or together.
- Features include customisable workflows, licence clause tracking, supplier records, usage reports, import/export and permissioned access.
- Free and open source under GNU GPL v3; website listed as github.com/coral-erm/coral.
- Written in PHP; developer is the CORAL development community.

**Details:** I read about CORAL on LinuxLinks, not ran it. It is a library ERM, so the fit question is simple for me: nothing for my projects. The modules cover the full lifecycle of electronic resources, from resource records and supplier contacts to licence terms and usage statistics, and the workflow and permission controls are the useful-sounding parts. The Licensing Terms Tool showing licence conditions when accessing resources is a nice touch for a library. Still, it is PHP, it is a library system, and I have no library to run. So I would say it is a capable niche tool and not worth me touching.

**For my projects:** Nothing for my projects.

## 8. KDE’s New Terminal Has Arrived And It’s..., by Brodie Robertson
![](https://i.ytimg.com/vi/_I5yJtZGCXc/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=_I5yJtZGCXc · **Karakeep:** `bqoo5ev98r7yl8m8kxw9sfu5`

**In short:** KDE's new terminal is Qui, a 0.1.0 early release built on LibGhostie with GPU rendering and Kitty protocols; Brodie calls it a solid first release, but split panes are still missing.

**Key points:**
- Qui 0.1.0 is KDE's new experimental terminal, packaged on Flathub and Arch (pacman -S qui).
- It uses LibGhostie from the Ghostty project, with GPU-accelerated rendering, modern font rendering, Kitty protocols and improved mouse support.
- Brodie found typing and scrollback smooth, but window resizing felt slightly delayed compared with Alacritty.
- Split panes are not implemented yet; the scroll bar cannot be hidden and the preset UI requires duplicating an existing preset.
- There is a bug where About KDE does not open from Qui.

**Details:** Qui is KDE's new terminal, not a Console replacement yet, more an experiment with LibGhostie. This first release is 0.1.0, available on Flathub and Arch. Brodie found it a working terminal with smooth scrollback and true colour support, plus tabs, presets and the usual KDE shortcuts. The resize felt a bit behind Alacritty, the scroll bar cannot be hidden, and split panes are missing. There is also an About KDE bug. I would say it is a solid first release, but not something I need to move to yet. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 9. 10 GPUs You Should Get for Local AI Before Qwen 4’s Release!, by Kai
![](https://i.ytimg.com/vi/CSRrqRC9QJA/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=CSRrqRC9QJA · **Karakeep:** `ii90v8h9tk4l293ygy5m1d02`

**In short:** Kai went card by card through 10 GPUs for local AI and ranked them on the honest decode numbers you get before any pull request lands. I would say it's a useful reality check, but only if you care about buying hardware for a model that doesn't exist yet.

**Key points:**
- RTX 3090: 24GB, 936GB/s, 41.3 tok/s plain decode, about $1,445, roughly $35 per tok/s; fastest prefill on the list at 767 tok/s at 64k context
- Two RTX 3060 12GB: $616 pair, 34.2 tok/s, about $18 per tok/s, cheapest here; a 129k-token prompt takes roughly 4.5 minutes
- RTX 5090: about $80 per tok/s on short context at market price; strong for multi-user serving at roughly 970 tok/s across 32 agents on SGLang
- The fast column everyone quotes needs an MTP trick sitting in an unmerged draft PR for 90 days; Qwen 4's small models have no weights, no confirmed size and no release date
- Three of the four cheapest cards jumped since August, P100 doubled, V100 up 48%, 7900 XTX up 39%, while the 3060 pair moved only 6%

**Details:** Kai's point is that every GPU list you have read is quoting the right-hand column of one GitHub table, and that column needs a multi-token prediction trick stuck in a draft pull request. Qwen 3.8 ships with an MTP head that guesses the next two or three tokens so one pass produces several, which is how a 3090 jumps from 41 to 63 tokens per second. Qwen 4's new architecture runs four parallel residual streams and the prediction head has to run per stream, which is why the PR has sat there for 90 days. VLLM and SGLang already handle it on Nvidia, so day one depends on your engine.

So he ranks on the left column, the plain number, and goes card by card. The 3090 is the yardstick at $35 per token per second with the fastest prefill on the list. Two 3060 12GB cards come in at $18 per token per second, the cheapest here, but prefill is slow at roughly 4.5 minutes for a 129k prompt. The 5090 is $80 per token per second on short context and hard to recommend for one person. The P100 pair is wild on a fork at $11 per token per second but loses 9 to 11 minutes on large prompts. The market has already priced these cards for the trick number, not the honest one, which is why the 3060 pair barely moved while the others jumped.

I would say it's a solid, slightly nerdy buying guide. Nothing for my projects, since I am not buying a GPU this month.

**For my projects:** Nothing for my projects.

## 10. How Smart People Are Using AI Right Now (7 Insane Use Cases), by Riley Brown
![](https://i.ytimg.com/vi/4PO0x-myitw/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=4PO0x-myitw · **Karakeep:** `p5jy6qp2eoa9o1lx0nqvd4tw`

**In short:** Riley Brown argues AI removes slop across seven examples, from jailbroken TVs and Kindles to self-built desktop apps; it is entertaining and overhyped, but the idea of building only the features you use is sound.

**Key points:**
- Riley Brown's YouTube video lists seven ways people use AI to remove 'slop', including vibecoding a TV OS, jailbreaking a Kindle, and building desktop apps.
- One cited TV example claims 70% less RAM usage and a three times faster interface after removing bloatware and ads.
- A Kindle example removes Amazon bloat, adds Tailscale, and syncs saved articles through a home server.
- The video editing example uses Claude Code, Claude Projects and Blender to make a 3D intro in one shot.
- The feed-filtering example has an agent clean 99% of email before a weekly inbox sweep.
- The video includes a sponsor break for Revolute Business and several claims are demos with no verifiable numbers.

**Details:** This is a YouTube video by Riley Brown about seven ways people use AI to remove 'slop'. The examples run from vibecoding a TV interface that removes ads and bloat, to jailbreaking a Kindle, to using Claude Code with Blender for 3D video intros, to letting an agent filter email, to building small desktop apps instead of paying for big SaaS seats. The useful part is the idea that AI makes it cheap to build the tiny slice of software you actually use, like a Raycast-style logo finder or a thumbnail tool, instead of paying for an app full of features you ignore. The TV and Kindle stories are clever, but they depend on specific hardware and a tolerance for breaking things, and the video editing and agent examples are demos with no numbers I can check. I would say the video is entertaining and mostly hype. Nothing here is a tool I can run this month, and several claims are just vibes. The one idea I would keep is building small, single-purpose apps around an API gateway when a big SaaS is mostly clutter for a team. Still, that is common sense with a new cost curve, not a new method. The rest is content. So yeah, that's that.

**For my projects:** Nothing for my projects.

## 11. you need to self-host Google Photos RIGHT NOW!!, by NetworkChuck
![](https://i.ytimg.com/vi/Z9q4S0Phq_Q/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=Z9q4S0Phq_Q · **Karakeep:** `sx6dqu61s6yp8nw3y4uwoby2`

**In short:** A NetworkChuck tutorial on self-hosting a Google Photos replacement called Image, with local AI search and a lot of manual setup. I would say the idea is good, but the maintenance burden is the real cost.

**Key points:**
- Free open-source tool called Image, run in Docker on a spare laptop with an external drive or NAS.
- Automatic phone backup, anywhere access through Twingate, memories, face and object detection using local AI.
- Exports from Google Photos via Google Takeout, which takes a few days.
- Backup plan is 3-2-1, including off-site cloud backup to Backblaze B2 encrypted with Restic.
- Has an API; he wired it into a family portal for on-this-day memories and search.
- Part two promises AI video montage features on a 3090, but that is not shown here.

**Details:** Bad news first: this is still a hands-on Linux tutorial, with drive mounting, fstab, Docker and storage rules, not a one-click install. The export alone takes a few days through Google Takeout, which that's a bummer, and the AI editing part is only promised for part two.

The useful bit is the shape of it. Image runs in Docker on a spare laptop, stores new uploads in a mounted drive, and gets backed up with 3-2-1, including Backblaze B2 through Restic. He also shows an API and a family portal for on-this-day photos and search, which is the part I actually liked.

I would say it is worth a look if you want your photos off Google, but only if you are happy owning the backup story yourself. So yeah, that's that.

**For my projects:** Nothing for my projects.

## 12. Introducing Search for Agents, by Cloudflare Blog
![](https://blog.cloudflare.com/_emdash/api/media/file/01M87EHBMCJY691A3ADBXCMG6A.png)
**Source:** https://blog.cloudflare.com/search-for-agents/ · **Karakeep:** `yhqkmowe9cpiuw0oaij5269w`

**In short:** Cloudflare now offers Search for Agents as a managed way to make site content queryable by agents over REST or MCP. I would say it is useful for public sites, but it is another hosted endpoint, so not for my own stack.

**Key points:**
- Available to all customers from 2026-11-25, according to the post.
- Usage follows AI Search pricing: ingesting content, storing the index and serving queries.
- Subject to included usage and limits on both Workers Free and Paid plans.
- Can expose public REST API or MCP endpoints, be used from Workers, or embed AI Search for human visitors.
- Authors listed are Celso Martinho and Gabriel Massadas.
- The post recommends the Agent Readiness page for site owners.

**Details:** Search for Agents is Cloudflare's managed search product aimed at agents rather than people. From what I read, it lets a site owner make content queryable through a public REST API or an MCP endpoint, call it from Workers, or embed it on a normal page for human visitors. Pricing follows AI Search, so that means ingesting content, storing the index and serving queries, with the usual Workers Free and Paid usage limits. It is available to all customers now. Yeah, the useful part is the MCP and REST angle, because that is how an agent actually asks a question instead of scraping pages. The bummer is that it is still Cloudflare's hosted index and hosted query path, so it does not fit my homelab-2nd cluster or my morning-brew pipeline, which both want the moving parts under my own control. Nothing for my projects. If I wanted agents to read a public site I own, this is a quick way to do it, but I would not put my own docs behind it.

**For my projects:** Nothing for my projects.

## 13. The Omarchy vs Asahi Linux Dispute is Way Messier Than It Looks! ($23.6M vs Volunteers), by Linux Tex
![](https://i.ytimg.com/vi/sBALmNg44Og/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=sBALmNg44Og · **Karakeep:** `f50dxsni8ksm2mqvcqxdcwnl`

**In short:** Omarchy 4.5 and Aurora Silicon are shipping a slick Apple Silicon Linux installer on top of Asahi's reverse-engineered work, while Asahi's volunteers accuse them of lifting unfinished code and washing it with AI. I would say the installer is useful and the ethics are the problem.

**Key points:**
- Asahi Linux reverse-engineered Apple Silicon with M1N1 and Speaker Safety D in Rust; Hector Martin quit in February 2025 and seven core developers took over.
- Omarchy launched in June 2025 on Arch and Hyprland; Omarchy 4 was built almost entirely by AI agents with nearly 800 updates and Claude as co-author, and it passed one million downloads.
- The Omacom Foundation raised $23.65M in August 2026 against about $119k for Asahi; DigitalOcean cut a $50/month GNOME and Flatpak sponsorship, then gave Omarchy $3M.
- On 24 September 2026 Omarchy switched to Linux Aurora, an AI-powered fork renaming M1N1 to Aura and HoneyCrisp to Borealis and replacing Asahi's no-AI rule with an AI-written one.
- Omarchy 4.5 launched on 4 November 2026 as a Mac OS app installer; DHH claimed five Mac features, but Jaideep Subedi's blog says USB-C DisplayPort used an experimental Asahi branch.
- Asahi tightened code under GPL v2 and accused bad actors of ripping unfinished code from personal folders and using AI to scrub names; Cody Ho's Gravity Linux fork is a non-profit following clean-room rules.

**Details:** Asahi Linux spent five years reverse engineering Apple Silicon with a clean-room approach, watching macOS talk to the chip through M1N1 and writing Speaker Safety D in Rust so MacBook speakers do not cook themselves. Hector Martin burned out and quit in February 2025; seven core developers then chose slower upstream work. Omarchy is the opposite: David Heinemeier Hansson launched it in June 2025 on Arch and Hyprland, it passed one million downloads, and Omarchy 4 was built almost entirely by AI agents with nearly 800 updates. The Omacom Foundation raised $23.65M in August 2026 against about $119k for Asahi, and DigitalOcean gave Omarchy $3M after dropping a $50 a month GNOME and Flatpak sponsorship.

The fight turned ugly on 11 September 2026, when Omarchy M promised to finish what Asahi started. By 24 September Omarchy had switched to Linux Aurora, an AI-powered fork that renamed M1N1 to Aura and HoneyCrisp to Borealis and replaced Asahi's ban on AI with a rule written by AI. Twenty-four Aurora developers pushed 553 updates in five days. Omarchy 4.5 arrived on 4 November as a Mac OS app that sets up dual boot without a terminal or USB stick. DHH claimed five big Mac features, but Jaideep Subedi's August blog says the USB-C DisplayPort work used an experimental Asahi branch. Asahi says bad actors ripped unfinished code from personal folders and used AI to scrub names, and it tightened its code under GPL v2.

For a normal Mac user the installer and features matter, and Omarchy delivers those. For the people who did the undocumented hardware work, the victory lap looks like sitting on LeBron James's shoulder and bragging about a higher dunk. I would say the product is useful and the ethics are the problem. So yeah, that's that.

**For my projects:** Nothing for my projects.

## 14. BOSGAME VTA-439 Mini PC running Linux - Changing GPU Memory Allocation with sysfs - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2026/06/BOSGAME-VTA-439-banner.png)
**Source:** https://www.linuxlinks.com/bosgame-vta-439-mini-pc-linux-gpu-memory-sysfs/ · **Karakeep:** `d4nf9onr1rwdb85mem2hp0gg`

**In short:** A LinuxLinks walkthrough of changing the VTA-439's Radeon 890M memory carveout through sysfs instead of the BIOS. Useful for testing allocations without hidden menus, but only where the kernel and firmware support it.

**Key points:**
- Mini PC uses a Ryzen AI 9 HX 470 with a Radeon 890M sharing DDR5
- Tested on CachyOS with kernel 7.3.4-1-cachyos
- 64GB installed after swapping two 16GB SO-DIMMs for two 32GB modules
- Default allocation is 4GB; sysfs showed index 3 for 4GB and index 5 for 8GB
- sysfs offers 512MB to 32GB, while the BIOS also offers 48GB
- After reboot, usable RAM fell from 58GiB to 54GiB

**Details:** The BOSGAME VTA-439 is a mini PC with a Ryzen AI 9 HX 470 and a Radeon 890M that shares the machine's DDR5. On the tested CachyOS setup, kernel 7.3.4-1-cachyos, the GPU reservation went from 4GB to 8GB without opening the BIOS.

With 64GB installed after swapping to two 32GB SO-DIMMs, the BIOS still offers up to 48GB, while the sysfs interface tops out at 32GB, index 9. The interface appeared on this machine and is upstream since Linux 7.0, though it needs firmware support and may be backported.

The practical path is to read carveout_options, then write the wanted index to carveout for the actual card, then reboot. Here index 5 meant 8GB, and usable RAM dropped from 58GiB to 54GiB.

The 48GB option is the interesting one for local LLMs with Lemonade Server, because some backends read the reported dedicated graphics memory. For everyday desktop use, a huge reservation is unlikely to help, and it leaves less RAM for everything else. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 15. The Programming Monitor I Keep Coming Back To, by Alex Ziskind
![](https://i.ytimg.com/vi/dh0JBMDJe6s/maxresdefault.jpg)
**Source:** https://www.youtube.com/shorts/dh0JBMDJe6s · **Karakeep:** `smd27trpe5o2gzulsgbg746d`

**In short:** A short video about BenQ's 28-inch RD280UG programming monitor and why the presenter keeps coming back to the RD line. It is a hardware pitch with no software angle, so nothing for my projects.

**Key points:**
- BenQ RD programming monitors; presenter has used them since 2024.
- Current desk monitor is the 28-inch RD280UG with a 3:2 aspect ratio.
- 120 Hz refresh rate; built-in KVM for two computers.
- USB-C carries display data and laptop charging over one cable.
- Light and dark coating presets, low blue light, night-hours protection and rear moon-halo lighting.

**Details:** This is a short video from Alex Ziskind about the BenQ RD280UG, a 28-inch programming monitor with a 3:2 panel. He has used the RD line since 2024 and says the taller screen shows more code at once, with crisp text. The 120 Hz refresh makes scrolling and window movement smooth. There is a built-in KVM for two computers, with HDMI and DisplayPort, plus USB-C for display and charging in one cable. It also has light and dark coating presets, low blue light and night-hours protection, and a moon-halo light behind the screen. He mentions an adjustable desk arm and a full review of the 24-inch model. I would say it is a tidy hardware note, but it is not a tool I can run, so nothing for my projects.

**For my projects:** Nothing for my projects.

## 16. midgard - encrypted clipboard synchronisation across devices - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2025/03/003-clipboard.png)
**Source:** https://www.linuxlinks.com/midgard-encrypted-clipboard-synchronisation-devices/ · **Karakeep:** `qqgung9kcvxuixsw0azfqkq1`

**In short:** midgard is a self-hosted, end-to-end encrypted clipboard sync tool with a Go relay and clients for Linux, macOS and Windows; I would say it is interesting for multi-machine work, but the article gives no version and I have no reason to trust a clipboard relay with my actual clipboard.

**Key points:**
- Developer Changkun Ou; licence GNU GPL v3.0; written in Go.
- Linux uses a background daemon plus CLI; macOS adds a menu bar app with graphical history; browser access covers computers, tablets and phones.
- Pair devices with single-use codes or QR codes; queued updates catch up disconnected devices.
- Shareable links cover clipboard contents and files, with configurable expiry and revocation.
- Cross-platform support for Linux, macOS and Windows; the relay forwards encrypted data.

**Details:** midgard is a cross-device clipboard synchronisation system: copy on one machine, fetch on another, with each device keeping its own history and a self-hosted relay only forwarding encrypted data. That is the good part, because clipboard contents are usually the worst place to put secrets and a relay that cannot read them is the minimum bar.

The article lists a lot of machinery: Linux daemon plus CLI, macOS menu bar app with history viewer, browser access, single-use or QR pairing, queued updates, search, restore, delete, shareable links for text and files, expiry and revocation, auth and server allowlists. That is a lot of surface for a clipboard, and clipboard managers are the sort of thing that quietly becomes a second inbox.

I would say it is quite a good job on paper, but I did not see a version number, a container story, backups or metrics, and a self-hosted relay that handles my clipboard across machines needs all three before it goes near my homelab. So yeah, that's that.

**For my projects:** Nothing for my projects.

## 17. OpenScreen - screen recorder and video editor - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2018/11/man-recording-studio-music-production.jpg)
**Source:** https://www.linuxlinks.com/openscreen-screen-recorder-video-editor/ · **Karakeep:** `a9hwbbviiypsg4bnb8xivjw7`

**In short:** OpenScreen is a free MIT screen recorder and editor for software demos and tutorials, with local captions, GPU exports and a headless CLI. I would say it looks useful for polished walkthroughs, but I would not call it an OBS replacement yet.

**Key points:**
- MIT licence; written mainly in TypeScript and Rust; developers Siddharth Vaddem, Etienne Lescot and contributors.
- Cross-platform on Linux, macOS and Windows; on Linux it captures via X11 or PipeWire through the ScreenCast portal under Wayland.
- System audio capture requires PipeWire; recording mouse clicks under Wayland requires appropriate input device permissions.
- Editing includes timeline cropping, trimming, snapping, speed changes, annotations, custom backgrounds, motion blur and selective region blurring.
- Exports are GPU-accelerated MP4 and GIF with configurable resolutions and aspect ratios; rendering uses Vulkan on Linux with automatic CPU fallback.
- Headless recording, project editing and exporting are available through the command-line interface; captions can be generated locally.

**Details:** OpenScreen combines desktop capture and post-production in one application, with an emphasis on highlighting interactions in software interfaces. It records windows or the whole screen, captures microphone and system audio, and adds picture-in-picture webcam overlays, automatic or manual zooms, cursor smoothing, click effects, transcript editing, optional subtitle translation and custom backgrounds. There is also an optional natural-language editing assistant that uses user-supplied API credentials. I would say the local captions and headless CLI are the interesting parts, especially for repeatable demo exports. The Wayland permission friction and lack of streaming keep it in the walkthrough tool category for me. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 18. Anthropic just gave Claude users a new way to make Mac apps - 9to5Mac, by 9to5Mac
![](https://9to5mac.com/wp-content/uploads/sites/6/2026/03/claude-code-auto-mode.webp?resize=1200,628)
**Source:** https://9to5mac.com/2026/11/24/anthropic-just-gave-claude-users-a-new-way-to-make-mac-apps/ · **Karakeep:** `n8cuppl5ojf8esjhb968h6y3`

**In short:** Anthropic has put a beta 'Install as app' button on Claude artifacts so Mac and Windows users get their own icon and window, with permission gates and Claude usage attached. I would say it is clever packaging, not a reason to move my tools off the homelab.

**Key points:**
- Anthropic is rolling out 'Install as app' in beta for Claude artifacts on Mac and Windows.
- An installed artifact opens in its own window with its own icon instead of inside Claude.
- Apps can be shared, send notifications, add menu bar items and carry their own permissions.
- They can use Claude connectors, but Claude usage stays tied to those apps.
- Anthropic says this is the second Claude update this week aimed at builders.

**Details:** The interesting part is the permission model: it needs your permission before it can interact with your computer, and you choose how much to allow. That is the sensible bit. The less sensible bit is that Claude usage is still tied to the app, so this is not a way to escape the meter, it is a way to keep using Claude in a nicer shell. It can benefit from connectors and do desktop things like notifications and menu bar items, which makes it more than a bookmark, but it is still Anthropic's platform with Anthropic's limits. I read about it, I did not try it. Nothing for my projects: I already have a software factory and agent setup, and another desktop wrapper does not make either stricter or cheaper.

**For my projects:** Nothing for my projects.

## 19. 9 Best Free and Open Source Linux Personal Finance Trackers - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2024/10/018-invoice.png)
**Source:** https://www.linuxlinks.com/best-free-open-source-linux-personal-finance-trackers/ · **Karakeep:** `rsdin93ii4ksan0yjna9gdnv`

**In short:** LinuxLinks rounded up nine free and open source Linux personal finance trackers, from investment portfolios to minimalist spending diaries. It is a useful directory if you want a private ledger, but there is no fit for my homelab or factory.

**Key points:**
- Nine trackers: Wealthfolio, ExpenseOwl, Reckoner, OpenMoneyBox, Denaro, Spent, Treeline, Outlay, Mukwa.
- Only free and open source software qualifies for inclusion.
- Some are local-first or encrypted: Reckoner, Treeline, Outlay.
- ExpenseOwl is described as self-hosted; OpenMoneyBox targets small personal budgets.
- The roundup links to a dedicated page for each program.
- No versions, prices or benchmark figures are given in the article text.

**Details:** LinuxLinks put together nine free and open source personal finance trackers for Linux. The list mixes Wealthfolio for investments, ExpenseOwl as a self-hosted expense tracker, Reckoner with encrypted local-first use, OpenMoneyBox for small budgets, Denaro as a simpler ledger, Spent as a minimalist tracker, Treeline and Outlay as local-first apps, and Mukwa with a privacy focus. The page is a roundup of separate dedicated pages, not a hands-on review, so there are no install notes, versions or benchmark numbers in it. I would say it is useful if you want a privacy-first ledger on Linux and do not want to hand bank details to a hosted service. For my own setup there is no Kubernetes path, backup story or metrics shown, so nothing here goes into homelab-2nd without a fight. Nothing for my projects.

**For my projects:** Nothing for my projects.

**Projects:**
- [Wealthfolio](https://github.com/wealthfolio/wealthfolio): A beautiful, private, local-first personal finance tracker. Investments, net worth, spending, and simulations. - wealthfolio/wealthfolio.
- [ExpenseOwl](https://github.com/tanq16/expenseowl): Extremely simple, self-hosted expense tracker with a beautiful UI. - Tanq16/ExpenseOwl.
- [Reckoner](https://codeberg.org/Reckoner/app): Privacy first personal financial tracker.
- [OpenMoneyBox](https://gitlab.com/igi0/openmoneybox): ClownyRaven / openmoneybox · GitLab.
- [Denaro](https://github.com/NickvisionApps/Denaro): Manage your personal finances. Contribute to NickvisionApps/Denaro development by creating an account on GitHub.
- [Spent](https://github.com/FrogSnot/Spent): A high-performance, minimalist personal finance tracker for Linux. Local-first, privacy-focused, and built with little to no bloat. - FrogSnot/Spent.
- [Treeline](https://github.com/treeline-money/treeline): Open source personal finance app. Local-first, built on DuckDB. Import from any bank, write SQL against your transactions, extend with plugins. macOS, Windows, Linux. - treeline-money/treeline.
- [Outlay](https://git.lashman.live/lashman/outlay): Personal finance and expense tracking app built with Rust, GTK4 and libadwaita.
- [Mukwa](https://github.com/snubwoody/mukwa): Free and open source, personal finance app. Contribute to mukwa-app/mukwa development by creating an account on GitHub.

## 20. animfetch - animated terminal system information tool - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2023/06/cpu-motherboard-abstract-3d.jpg)
**Source:** https://www.linuxlinks.com/animfetch-animated-terminal-system-information-tool/ · **Karakeep:** `zzduqp79wh8zn8eac21x2bhb`

**In short:** animfetch is a Rust terminal fetch tool that pins an animated system-info panel above a live shell, and I would say it is neat but not something I need.

**Key points:**
- Terminal system information utility with animated artwork, by Andrew Velox, MIT licence.
- Keeps the animation and info panel pinned above a normal shell while commands scroll underneath.
- Layouts include classic, boxed, tree, sections, chips, iconic, card and minimal.
- Shows OS, CPU, GPU, memory, storage, kernel, shell and other details; can refresh changing stats.
- Runs on Linux and macOS; written in Rust; free and open source.

**Details:** animfetch is a Rust terminal system information tool that puts animated artwork next to OS and hardware details, and the interesting bit is that it can pin that panel above a normal shell while commands keep running underneath. That means the usual fetch output does not have to be a one-shot thing, and you keep your history, aliases and completion. It has layouts from classic to card and minimal, can run as a standalone animation viewer or a static display, and can refresh memory, uptime and disk numbers. It is free and open source under MIT, runs on Linux and macOS, and the GitHub repo is by Andrew Velox. I would say it looks like a fun terminal toy more than a tool I need: the persistent panel is the real feature, yeah, but on my machines I already have fetch output when I want it and I do not need artwork above my prompt. Nothing for my projects, unless I wanted a prettier login screen, which I do not.

**For my projects:** Nothing for my projects.

## 21. 9 Best Free and Open Source Serial Port and Telemetry Visualization Tools - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2025/01/018-coding.png)
**Source:** https://www.linuxlinks.com/best-free-open-source-serial-port-telemetry/ · **Karakeep:** `sjzq190hy3qovuyhollpuier`

**In short:** A LinuxLinks roundup of nine free and open source serial port and telemetry visualization tools, from simple port monitors to plotting dashboards. I would say it is a useful pointer list, but the text I have gives no versions or test results, so it is not a review.

**Key points:**
- Nine tools are named: Serial Studio, SerialTest, PlotJuggler, COMTool, SerialPlot, Serial Monitor, Tauno Serial Plotter, seriot and QSerial.
- They cover serial ports, Bluetooth, TCP/UDP, telemetry streams and time series data.
- Features mentioned include live plotting, logging, filtering, packet inspection and data playback.
- Only free and open source software is eligible, and the roundup is by Steve Emms on LinuxLinks.
- No versions, licences beyond free and open source, or benchmark numbers appear in the text I have.

**Details:** This is the classic LinuxLinks shape: a short intro, a ratings chart I cannot see, and a table of names with one-line descriptions. Serial Studio gets the telemetry dashboard slot, SerialTest covers serial plus Bluetooth, TCP and UDP, PlotJuggler is the time series one, and the rest are monitors or plotters. That is a decent spread for embedded work, and the free and open source filter is the part I trust. The bad news is that the page as supplied gives no versions, no install notes and no comparison beyond the one-liners, so I cannot tell which one is stable or which one is abandoned. I would treat it as a starting list for a Saturday afternoon, not as a verdict. Nothing for my projects.

**For my projects:** Nothing for my projects.

**Projects:**
- [Serial Studio](https://github.com/Serial-Studio/Serial-Studio): Open-source telemetry dashboard. Supports UART, BLE, MQTT, Modbus, CAN Bus and more. - Serial-Studio/Serial-Studio.
- [SerialTest](https://github.com/wh201906/SerialTest): Data transceiver(monitor)/realtime plotter/shortcut/file transceiver over serial port/Bluetooth/network on Windows/Linux/Android/macOS | 跨平台串口/蓝牙/网络调试助手，带数据收发/实时绘图/快捷发送/文件收发面板，可在PC和Android设备上使用 - w...
- [PlotJuggler](https://github.com/PlotJuggler/PlotJuggler): The Time Series Visualization Tool that you deserve. - PlotJuggler/PlotJuggler.
- [COMTool](https://github.com/Neutree/COMTool): Cross platform communicate assistant(Serial/network/terminal tool)（ 跨平台 串口调试助手 网络调试助手 终端工具 linux windows mac Raspberry Pi ）支持插件和二次开发 - Neutree/COMTool.
- [SerialPlot](https://github.com/hyOzd/serialplot): Small and simple software for plotting data from serial port in realtime. - hyOzd/serialplot.
- [Serial Monitor](https://github.com/hacknus/serial-monitor-rust): A cross-platform serial monitor/plotter written entirely in rust. - hacknus/serial-monitor-rust.
- [Tauno Serial Plotter](https://github.com/taunoe/tauno-serial-plotter): Serial Plotter for Arduino and other embedded devices. - taunoe/tauno-serial-plotter.
- [seriot](https://github.com/ak1932/seriot): A serial monitor and plotter. Contribute to ak1932/seriot development by creating an account on GitHub.
- [QSerial](https://github.com/tuna/QSerial): An advanced cross-platform serial port utility. Contribute to tuna/QSerial development by creating an account on GitHub.

## 22. A 10KB semantic UI library with zero dependencies, no build step, by Open-source Projects
![](https://opengraph.githubassets.com/1/knadh/oat)
**Project:** [oat](https://github.com/knadh/oat)
**Source:** https://www.opensourceprojects.dev/post/oat · **Karakeep:** `tr2tdocwitgrpuf1qxkgndoy`

**In short:** Oat is a dependency-free, ~10KB semantic UI library with no build step; I would say it is a nice small option, but not a design system.

**Key points:**
- Semantic HTML and CSS component library with zero dependencies and no build step.
- Around 10KB of CSS and JS combined.
- A few dynamic components are WebComponents; everything else is CSS.
- Styles semantic tags and attributes contextually, with no classes needed for base components.
- The README says it was written after the author got sick of bloat, dependencies and rug-pulls.
- Live demo and docs exist; it is not meant to compete with large frameworks.

**Details:** Oat is a semantic HTML and CSS component library from the knadh/oat repo, around 10KB of CSS and JS with zero dependencies and no build step. You drop in two files and style semantic tags, with WebComponents only for the few dynamic bits.

I would say it is quite good job for small pages, but it is not a design system. Around 10KB combined, which that's tiny, but the trade is no ecosystem and no complex components. It styles tags and attributes out of the box, so markup stays clean, and the README is blunt that it was built after the author got sick of bloat, dependencies and rug-pulls. That origin story is fair, though it also means you are buying one person's taste.

Nothing for my projects. So yeah, that's that.

**For my projects:** Nothing for my projects.

## 23. A richer git commit graph, rendered right in your terminal, by Open-source Projects
![](https://opengraph.githubassets.com/1/lusingander/serie)
**Project:** [serie](https://github.com/lusingander/serie)
**Source:** https://www.opensourceprojects.dev/post/serie · **Karakeep:** `zysmmfas3y5i02r1xyvp4cef`

**In short:** Serie is a Rust terminal UI that draws a Git commit graph through the terminal's image protocol instead of ASCII. I would say it is a focused viewer worth a try if your terminal is on the compatibility list, but it is not a full Git client.

**Key points:**
- Written in Rust with Ratatui; install with `cargo install --locked serie`
- Renders through iterm, kitty or kitty-unicode protocols, with auto as the default
- Edge styles are rounded, angular or curved; cell width can be auto, double or single; antialiasing toggles
- Can pin a primary branch to the leftmost column, set `--max-count`, and use chrono or topo ordering
- Config loads from `$SERIE_CONFIG_FILE` or `$XDG_CONFIG_HOME/serie/config.toml`; keybindings show on `?`
- Author is lusingander; the project states it is not a full-featured Git TUI and will not work in every terminal

**Details:** Serie takes the usual `git log --graph` output and replaces the ASCII lines with an image drawn through the terminal emulator's image protocol, so the graph reads more like a small GUI. It stays deliberately narrow: browse commits, keep a branch pinned with `--primary-branch`, limit output with `--max-count`, and choose chrono or topo ordering. You can tune edge style, cell width and antialiasing, pick the protocol with `--protocol`, and override keybindings or config. The stated reason for building it is that `git log --graph` was hard to read even with extra options. That honesty about scope is the good part. The catch is terminal support, which is listed as a non-goal rather than something to fix, so I would check compatibility before getting attached. For a full Git TUI this is not it, and the project says so directly.

**For my projects:** Nothing for my projects.

## 24. Install Linux next to Windows without a USB stick, by Open-source Projects
![](https://opengraph.githubassets.com/1/arjun-ingole/hop)
**Project:** [hop](https://github.com/arjun-ingole/hop), also [hop](https://github.com/Arjun-Ingole/hop)
**Source:** https://www.opensourceprojects.dev/post/hop · **Karakeep:** `ykljqmjuonejba2xqyl1yvxx`

**In short:** hop is a Windows app that installs a Linux distro next to Windows without a USB stick. I would say it's a neat fix for one specific friction point, but the supported list and disk rules are the real gate.

**Key points:**
- Windows 10 version 1803 or newer, or Windows 11, on a UEFI PC with a GPT disk; Linux must land on an internal disk, not a USB drive.
- Supported systems include elementary OS, Ubuntu and flavours, Linux Mint, Pop!_OS, Zorin OS, Debian, Fedora Workstation, Ultramarine, CachyOS, Arch Linux, Omarchy, and others; other Ubuntu-based ISOs should work if you select the file yourself.
- CachyOS, Arch, Omarchy and Pop!_OS need Secure Boot off; Kubuntu, Lubuntu and Ubuntu Unity are refused.
- Make room clears Windows files that block shrinking and restores settings; nothing changes until pre-flight checks pass.
- Undo gives space back and can remove another Linux; full erase needs a typed ERASE and more memory than the ISO size.

**Details:** hop is a single Windows application from Arjun Ingole's hop repo, published via Open-source Projects, that handles the whole dual-boot install from inside Windows. You pick a Linux system, choose a drive, drag a slider for space, and click Install; it downloads and verifies the ISO, or uses one you already have, then builds the same FAT32 installer structure a USB stick would have in a new partition. It also walks you through the choices in the Linux installer, where first-timers usually get stuck.

The useful part is the Windows-specific handling: drives can report free space and still refuse to shrink, and hop's Make room clears those files in one click and restores settings afterward. Nothing touches the disk until pre-flight checks pass, and undo gives the space back or removes another Linux. The catch is the list and the disk rules: Debian, CachyOS, Linux Mint and Zorin OS cannot go on a second disk yet, Omarchy only works from its own 4.0 ISO with BitLocker fully off, and the whole thing needs Windows 10 1803 or newer or Windows 11 on UEFI with GPT. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 25. An open-source take on Scion: Git hosting for AI agents, by Open-source Projects
![](https://opengraph.githubassets.com/1/feder-cr/git-ai)
**Project:** [git-ai](https://github.com/feder-cr/git-ai)
**Source:** https://www.opensourceprojects.dev/post/git-ai · **Karakeep:** `ujlugtgmhypt98xjomqws0iq`

**In short:** gitai is an open-source Git server built for fleets of coding agents, with compare-and-swap landing and server-side history. I would say it is interesting for agent-heavy teams and probably overkill for a solo developer.

**Key points:**
- Open-source Git server aimed at coding agents, implementing a design Anthropic described for Scion.
- Lands with compare-and-swap, rebasing onto the current tip, and batches concurrent lands into one reference update.
- Conflict resolution can use any LLM provider, a deterministic tool, or nothing, with a verify.command gate.
- History queries run server-side and are memoised as derived data, computed once per commit.
- SQLite for single node or PostgreSQL for scale-out, packs in file/S3/GCS object storage, stateless servers, MIT licensed.

**Details:** gitai is an open-source Git server aimed at coding agents rather than humans clicking around a web UI. Anthropic described an internal system called Scion for this problem and kept it to themselves; gitai implements that publicly described design, with no affiliation claimed.

The interesting bit is the landing model. Instead of a merge queue, a UserLand operation rebases a change onto the current tip and lands it with compare-and-swap, batching concurrent lands into one reference update. Conflict resolution is a proposal: any LLM provider, a deterministic tool, or nothing, and a model's resolution only lands by itself if your verify.command passes on the exact tree. There is also an author trail for accepted reference updates, plus sparse clones through graft clone and graft sparse.

Underneath it is normal Git: changesets in a write-ahead log, SQLite or PostgreSQL, packs in object storage, stateless servers. The server never calls a model, so it stays vendor-neutral.

I would say it is worth a look if you run fleets of agents against shared branches. If you push once a day, you probably do not need it.

**For my projects:**
- code-factory: Run code-factory agent commits through gitai so a land only succeeds when verify.command passes on the exact tree, with the accepted-update log as the audit trail.

## 26. A read-only, directory-first photo gallery that runs on a Raspberry Pi, by Open-source Projects
![](https://opengraph.githubassets.com/1/bpatrik/pigallery2)
**Project:** [pigallery2](https://github.com/bpatrik/pigallery2)
**Source:** https://www.opensourceprojects.dev/post/pigallery2 · **Karakeep:** `ldvnbn8e70lz45tqu9j7bszu`

**In short:** PiGallery2 is a read-only, directory-first photo gallery for low-resource servers, served from Docker with a simple volume setup; I would say it is a neat, low-risk browser for photos you already have, with a deliberately contained scope.

**Key points:**
- Read-only and directory-first: it shows your existing folder structure and mounts the photos as :ro.
- Runs in Docker on amd64 and arm64v8, with port 80 and four volume mounts.
- Default login is admin / admin, and the README says to change it immediately.
- Mentioned features include map, search, sharing, albums and faces; it is also a PWA.
- It has no built-in rate limiting, so anything beyond the local network needs a reverse proxy.
- It is maintained by one developer, described as working in nap-time windows.

**Details:** PiGallery2 points at an existing photo folder and browses it without renaming or reorganising anything, which is the bit I like. It indexes into its own database, serves a web UI, and the Docker command is short: four mounts, one port, and the photos mount is read-only. The default admin / admin login is a bummer, so that needs changing immediately. The demo can take up to 60 seconds on first load because it sleeps when idle, which is a bit wonky but understandable for a free demo.

The honest caveat is that it does not rate limit, so anything beyond the local network wants nginx or another proxy in front. It is built for modest hardware like a Raspberry Pi, and there are community extensions plus an Android client, but it is still one person's project. For my own use, I would treat it as a read-only browser, so nothing for my projects. So yeah, that's that.

**For my projects:** Nothing for my projects.

## 27. A quiet Mac browser built on WebKit, about 14 MB, by Open-source Projects
![](https://opengraph.githubassets.com/1/driceroland/search)
**Project:** [search](https://github.com/driceroland/search)
**Source:** https://www.opensourceprojects.dev/post/search · **Karakeep:** `imf5f8bu8439wopnyr7yp8wg`

**In short:** Search is a small Mac browser built on WebKit by Office Commun, about 14 MB, free on macOS 14 or later. I would say it is worth a try if you want a browser that stays out of the way.

**Key points:**
- Built by Office Commun, a design studio, for macOS 14 or later.
- About 14 MB, because it uses the WebKit engine already in macOS instead of bundling Chromium.
- Free, with a Homebrew cask: brew install --cask driceroland/tap/search.
- Includes tabs, pinned tabs, session restore, Split View, reading mode, and a floating video window.
- Ad blocking runs at the network level, and Chrome extensions run on WebKit's own extension engine.
- Passwords stay in the Mac keychain, with one-click import from Chrome, Arc, Dia, Brave, or Edge.

**Details:** The pitch is minimalism with details that are actually thought through. The search field completes from your own history and only sends what you type after Return. Pinned tabs shrink, last session tabs come back without cost until clicked, and ⌘K lists open tabs. Split View keeps a pair and its widths with a Space, and ⇧⌘H removes overlays for good on that site. Keep This Site Awake stops a site sleeping under memory pressure, but uses more memory, which the README says upfront.

Passwords are offered after a sign-in works, saved accounts and passkeys surface under the field, and nothing is autofilled on its own. The ad blocker runs before the page, and Chrome extensions are pasted in from the Web Store to run on WebKit's own engine. I would say the WebKit bet is the sane part, and the rest is a small set of features that earn their place rather than a checklist.

**For my projects:** Nothing for my projects.

## 28. A Material 3 YouTube Music client and local player, no longer maintained, by Open-source Projects
![](https://opengraph.githubassets.com/1/outertune/outertune)
**Project:** [github.com](https://github.com/ItzSkyeYT/InterTune), also [github.com](https://github.com/yuuichi-s/AsterTune), [github.com](https://github.com/MetrolistGroup/Metrolist), [github.com](https://github.com/koiverse/ArchiveTune), [github.com](https://github.com/FoedusProgramme/Gramophone), [github.com](https://github.com/outertune/outertune)
**Source:** https://www.opensourceprojects.dev/post/outertune · **Karakeep:** `c7xlnlsafeobtdiy711mcxd9`

**In short:** OuterTune is an Android Material 3 player that combined YouTube Music and local files, and it is no longer maintained, so I would treat it as a reference rather than install it.

**Key points:**
- Android Material 3 player, GPL-3.0, distributed via GitHub releases, IzzyOnDroid and Obtainium.
- YouTube Music side: downloads, ad-free and background playback, account sync; full playlist sync to remote account temporarily unavailable.
- Local side: MP3, OGG and FLAC, with a custom tag extractor instead of MediaStore.
- Features include multiple queues, synced lyrics in LRC and TTML with word-by-word and karaoke support, audio normalisation, and tempo and pitch adjustment.
- README recommends InterTune, AsterTune, Metrolist, ArchiveTune and Gramophone.
- No active development; third-party APIs and Android versions will move on without patches.

**Details:** OuterTune is a Material 3 music player for Android, built as a supercharged fork of InnerTune, and it tries to do two jobs in one queue: YouTube Music and local files. That local-plus-streaming combination is the real draw, and the custom tag extractor fixing backslash-delimited tags is a small honest signal that someone used it with messy libraries. The feature list is fairly complete, with multiple queues, synced lyrics in LRC and TTML, audio normalisation, and tempo and pitch adjustment. The bad news is at the top of the README: no active development. Yeah, for a client talking to a third-party service, that is a liability over time, because APIs shift and Android versions move on. The handoff is clean though, with four replacement YouTube Music clients named and Gramophone for local playback. I would say it is useful to study or fork. For everyday listening, take the README at its word and pick one of the recommended alternatives. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 29. Why Nvidia Brought Jensen Huang Back, by Better Stack
![](https://i.ytimg.com/vi/OgJ9nSM3hV0/maxresdefault.jpg)
**Source:** https://www.youtube.com/shorts/OgJ9nSM3hV0 · **Karakeep:** `p97tybzj8pulgr9r65tl6skj`

**In short:** A short video claiming Jensen Wang is back as NVIDIA CEO, then spending most of its time on the Megaspeed export-control story. I would say it is headline gossip, yeah, not much you can act on.

**Key points:**
- Claims Jensen Wang is back as NVIDIA CEO 11 days after quitting, with the stock up 30% that day.
- Says Jensen owns about 3.5% of NVIDIA, with one vote per share, so he does not control the board.
- Compares it to Sam Altman's 2023 firing and Matt Mullenweg returning after 33 hours.
- Megaspeed, run by Alice Wang, bought about $4.8 billion of NVIDIA hardware over three years while its assets rose from about $33 million to about $3 billion.
- NVIDIA says it cut Megaspeed off in June 2025, but trade records show another $787 million of chips that November.
- A unanimous board vote to bring him back followed input from senior levels of the US government; Congress questions him behind closed doors on December 1.

**Details:** The video's premise is odd: the man it calls Jensen Wang is back as NVIDIA CEO 11 days after he quit, and the stock is up 30% on the same day. It then asks how he could be forced out when he founded the company, and answers that he owns about 3.5% with one vote per share, so the board can move without him. From there it jumps to Sam Altman's 2023 firing and Matt Mullenweg's 33-hour return, where majority voting rights made the difference. The bulk of it is about Megaspeed, a Singapore company run by Alice Wang, which bought about $4.8 billion of NVIDIA hardware over three years while its assets went from about $33 million to about $3 billion. Reporters found locked doors in Singapore, and the Australian arm's director is a 29-year-old newspaper seller whose father says he has never heard of MegaSpeed. The video also says there are two possible routes for chips to reach China: physical shipment, which the US has been investigating since 2024, or remote rental from a Malaysia data centre, which was legal until this month. NVIDIA says it cut Megaspeed off in June 2025, but trade records show another $787 million of chips in November, and it is still an official NVIDIA cloud partner. No one has been charged and MegaSpeed denies all of it. Then the new chair said the board would never reinstate Jensen, and five days later they voted unanimously after input from senior levels of the US government. He is questioned by Congress behind closed doors on December 1. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 30. Sentence Transformers - text embeddings and semantic retrieval - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2019/10/nlp-natural-language-processing-cognitive-computing-technology-concept.jpg)
**Project:** [sentence-transformers](https://github.com/huggingface/sentence-transformers)
**Source:** https://www.linuxlinks.com/sentence-transformers-text-embeddings-semantic-retrieval/ · **Karakeep:** `f21bui7ygqifdl4xarkmeafy`

**In short:** Sentence Transformers is a Python framework from UKP Lab and Hugging Face contributors for embeddings and semantic retrieval, Apache 2.0. I would say it is worth a look if you need local search or reranking, and not worth it if you want a ready-made service.

**Key points:**
- Python framework for dense embeddings, sparse representations, cross-encoder reranking and token-level multi-vector retrieval.
- Ships pre-trained embedding models and supports training or fine-tuning on domain-specific data, including hard negative mining.
- Named uses include document retrieval, duplicate detection, recommendation systems and retrieval-augmented generation.
- Apache 2.0 licence; developed by UKP Lab and Hugging Face contributors; integrates with Hugging Face Transformers and the Hub.
- Also covers multilingual models, embedding quantization and evaluation tools.

**Details:** Sentence Transformers is about comparing meaning rather than matching words, so it fits semantic search, information retrieval and text analysis. It covers four retrieval styles, which is a lot for one library, but that is the point if you are building search. Unfortunately it is a library, so you still build the service yourself: there is no Kubernetes path, backup story or metrics out of the box, and my homelab would not accept it without a fight. For agent-fleet, its cross-encoder reranking could sit behind the docs server's existing index and re-score manual passages before an agent answers. I would say it is worth a look for local semantic search and reranking, and not worth it if you just want a box that runs. So yeah, that's that.

**For my projects:**
- agent-fleet: Use its cross-encoder reranking behind the docs server's existing index to re-score manual passages before an agent answers.

## 31. Attention Required! | Cloudflare, by Cloudflare
![](https://9to5linux.com/favicon.ico)
**Source:** https://9to5linux.com/pop_os-26-04-lts-is-now-available-for-download-based-on-ubuntu-26-04-lts · **Karakeep:** `fcvihos954im5ksooi5jjsas`

**In short:** Pop!_OS 26.04 LTS is System76's Ubuntu-based desktop distro with the Rust COSMIC desktop, now out as a fresh install; I would say it is interesting for a desktop machine but nothing for my projects.

**Key points:**
- System76 released it on 24 November 2026, based on Ubuntu 26.04 LTS, with Linux 7.2 and Mesa 26.2.
- COSMIC 1.12 is written in Rust and first appeared in Pop!_OS 24.04 LTS.
- COSMIC Theme Constellations ships eight bundled themes with wallpaper, accent colours, icons and fonts.
- Downloads are 64-bit and ARM64 live ISOs for Intel/AMD or NVIDIA systems.
- In-place upgrades from 24.04 LTS are due in December; new apps include COSMIC Image Viewer, COSMIC System Monitor and Popsicle ported to libcosmic.

**Details:** System76 released Pop!_OS 26.04 LTS on 24 November 2026, based on Ubuntu 26.04 LTS and aimed at developers, engineers and creators. It ships COSMIC 1.12, the Rust desktop that first appeared in 24.04 LTS, plus Linux 7.2, which is fine for a desktop, and Mesa 26.2. The release adds bundled themes, hybrid graphics support, Flatpak in the software store, remote desktop, VRR and a batch of gaming and input tweaks.

The practical catch is that upgrades from 24.04 LTS are not live yet, so this is a fresh install unless you wait for December. One commenter also hit a black screen after reboot on NVIDIA hardware, with the advice being to install the Intel ISO and then nvidia-driver-580 for 10 series cards. That is the sort of early-release wobble I would expect, yeah.

This is a desktop OS, and none of my projects need a new desktop. So yeah, that's that.

**For my projects:** Nothing for my projects.

## 32. SyncClipboard - cross-platform clipboard synchronisation tool - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2025/03/021-clipboard.png)
**Source:** https://www.linuxlinks.com/syncclipboard-cross-platform-clipboard-synchronisation-tool/ · **Karakeep:** `lgdxfs6dvekeuubzpyfa07ra`

**In short:** SyncClipboard syncs text, images and files across Linux, macOS and Windows from storage you control, but mobile access is limited by each OS.

**Key points:**
- Synchronises clipboard contents and clipboard history between multiple computers.
- Transfers text, images, individual files and groups of files.
- Uses a dedicated server, an integrated client server, WebDAV or S3-compatible storage.
- Companion mobile integrations exist, with automatic access depending on OS restrictions.
- Free and open source under the MIT License; written in C# by Jeric-X.

**Details:** SyncClipboard is a clipboard synchronisation app for people who move between desktops: copy on one machine, paste on another, with history for older entries and support for text, images and files. It runs on Linux, macOS and Windows, and keeps data on infrastructure you control through a dedicated server, an integrated server, WebDAV or S3. That flexibility is the useful part. Unfortunately automatic mobile clipboard access depends on each mobile OS, so it is not a clean phone-to-desktop story. I would say it looks quite good for ordinary multi-device work, but only if you already want to run or point it at storage. Nothing for my projects: it has no Kubernetes path, backup story or metrics that I can see, and clipboard sync is not something I need in the homelab.

**For my projects:** Nothing for my projects.

## 33. Clay helps sales teams win with Codex and ChatGPT, by OpenAI
![](https://images.ctfassets.net/kftzwdyauwt9/24rUSNlLR8iXQysKA6dq12/38954f25812d30bf772691824f747b84/clay-seo-1920.png?w=1600&h=900&fit=fill)
**Source:** https://openai.com/business/customer-stories/clay-plugins-openai/ · **Karakeep:** `b3p54vjnbihtefyiqb81o8pz`

**In short:** Clay is a sales-data and go-to-market tool wrapped in an OpenAI customer story; the concrete bits are Codex and ChatGPT plugins plus three GPT-6 model tiers, and I would say it is mostly marketing.

**Key points:**
- OpenAI customer story dated November 24, 2026
- Clay described as a self-learning revenue engine for sales teams
- Plugins for Codex and ChatGPT let reps research accounts and run go-to-market plays
- GPT-6 Sol is primary, GPT-6 Astra for harder tasks, GPT-6 Luna for cost-sensitive work
- Responses API used across model tiers; Decisions API and GPT-Live-1 mentioned as future directions
- Clay company size listed as startup, region North America, industry technology

**Details:** Clay helps sales teams turn prospect data into go-to-market plays, and the article is really OpenAI selling its own models through a customer. The concrete part is the plugin story: Codex for builders and reps, ChatGPT for account research, and GPT-6 Sol as the primary model with Astra for harder work and Luna for cheaper work. I read Jeff Barg's quote about Astra writing code, adding tests and running them, but that is one person's workflow inside Clay, not evidence I can use. The Decisions API and GPT-Live-1 bits are roadmap talk. Nothing here for my projects. I would say it is a customer story with a few model names and not much else.

**For my projects:** Nothing for my projects.

## 34. GTA6 Ported To PC After Just 3 Days (Open-Source), by Better Stack
![](https://i.ytimg.com/vi/pvciCWH3TQg/maxresdefault.jpg)
**Source:** https://www.youtube.com/shorts/pvciCWH3TQg · **Karakeep:** `ollhmgb6qrqrbnh7j81fthbp`

**In short:** Leonida is an open-source attempt to get GTA 6 running on PC by rebuilding the console system software around the game's own code, and I would say it is more stunt than usable port right now.

**Key points:**
- GitHub project Leonida has over 30,000 stars.
- It opened a day after launch and took over 10,000 commits in under three days, mostly from AI coding agents.
- It has translated all 26,000 of the game's shaders.
- On an RTX 4090 it is stuck on its 13th crash before drawing a single frame.
- The README says it does not actually run yet.
- Rockstar's owner, Type 2, has sued fan rebuilds of GTA 3 and Vice City before.

**Details:** It does not run yet, and on one RTX 4090 it is stuck on its 13th crash before drawing a single frame. Leonida skips the usual machine-code translation because the Xbox Series uses the same kind of AMD processor as many gaming PCs, so it runs the game's own code and rebuilds the console system software with stand-ins, the same trick Proton uses for Windows games on Linux. The speed is pretty wild, and one of the top contributors is called Slop Gobble Cobbler, but the game's main program only reportedly leaked on Monday. Rockstar has still not given a PC release date, and Type 2 has sued fan rebuilds before, so the legal side is the bigger bummer. Yeah, I read about it, I did not run it, and I would say it is not worth touching for my projects. Nothing for my projects. So yeah, that's that.

**For my projects:** Nothing for my projects.

## 35. whatscli - terminal-based WhatsApp client - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2025/07/008-chat.png)
**Source:** https://www.linuxlinks.com/whatscli-terminal-based-whatsapp-client/ · **Karakeep:** `hej444c0g4a8thos1a9k8t6v`

**In short:** whatscli is a terminal-based WhatsApp client in Go that talks through WhatsApp's multi-device protocol. I would say it is a tidy TUI, but not worth it for anything I run.

**Key points:**
- Terminal WhatsApp client written in Go, MIT licence, by normen and contributors.
- Cross-platform on Linux, macOS and Windows.
- Authenticates by QR code through WhatsApp's multi-device interface and keeps sessions between launches.
- Sends and receives messages, images, video, audio and documents, with media download and external attachment opening.
- Basic group management, desktop or terminal-bell notifications, and custom colours and keyboard shortcuts.

**Details:** whatscli is a terminal-based WhatsApp client written in Go under the MIT licence. It connects through WhatsApp's multi-device interface, authenticates with a QR code, and keeps the session between launches. It sends and receives messages, media and documents, does basic group management, and can use desktop notifications or the terminal bell. Interface colours and shortcuts are customisable. I would say it is a neat TUI for someone who lives in a terminal, but it is still WhatsApp, so it is not worth it for my homelab or agent setup. Nothing for my projects.

**For my projects:** Nothing for my projects.
