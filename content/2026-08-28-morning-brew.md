---
date: 2026-08-28
slug: 2026-08-28-morning-brew
tags: AI Agents,AI Tools,Android,Anthropic,App Development,Apps,Artificial Intelligence,Audio Control,Audio Editing,Audio Processing,Big Tech,Bluetooth,Browser Automation,Business Automation,C++,CLI,Calibre,Claude,Cloud Computing,Cloudflare,Coding Agents,Coding Tools,Coding Tutorials,Command Line Interface,Computer Architecture,Computer Peripherals,Computer Science,Computing,Computing Hardware,Consumer Electronics,Content Creation,Cross-Platform,Cross-Platform Development,Custom Keyboards,Customer Support,Cybersecurity,DNS,DXVK,Data Analysis,Data Management,Data Visualization,Database,Database Management,Debian,Desktop,Desktop Applications,Desktop Customization,Digital Media,Digital Signal Processing,Distro,Distros,Documents,EPUB,Ebooks,Embedded Systems,Emulation,Entrepreneurship,File Conversion,Fitness Tracking,GTK+,GUI,Gadgets,Gaming,Google,Handheld Consoles,Hardware,Headphones,Humor,Idea Generation,Information Overload,Input Devices,Internet,Internet Culture,Internet Technology,Inventory Management,JavaScript,JavaScript Frameworks,KDE Plasma,Knowledge Base,Kobo,Laptops,Large Language Models,Linux,Linux Desktop,Linux Distribution,Linux Software,Linux distribution,Machine Learning,Mail,Mail Notifications,Marketing,Media Management,Memory Management,Meteorology,Mobile Development,Mobile Gaming,Multimedia,Music Production,Network Administration,Networking Tools,News,No-Code,Open Source,Open Source Software,Operating Systems,Orange Pi,PHP,Penetration Testing,Perl,PlayStation 3,PlayStation Portable,PostgreSQL,Privacy,Product Design,Productivity,Productivity Tools,Programming,Progressive Web Apps,Project Based Learning,Proton,Proxy Management,Python,Qt,Radar Viewer,Roundup,Rust,Rust Programming,SMB Protocol,Sample Preparation,Scientific,Scientific Modeling,Self-Hosted,Single Board Computer,Software Architecture,Software Development,Software Engineering,Software Optimization,Sound Editor,Sound Engineering,Spreadsheets,SwiftUI,System Monitoring,System Software,Systems Programming,Tauri Framework,Technology,Ticketing System,Tiling Window Managers,Troubleshooting,TypeScript,Ubuntu,Ubuntu 26.04 LTS,User Interface,Utilities,Vala,Version Control,Video Games,Vulkan,Wallpaper Manager,Waveform Editing,Weather Forecast,Web Applications,Web Apps,Web Development,Web Scraping,Web Security,Web Testing,Website Statistics,Window Managers,Windows Software,Wine,Workflow Orchestration,airtable,analytics,audio,audio editor,bookmark manager,collection manager,computer peripherals,data analysis,database,desktop,distribution,distro,earth science,ebook,ebook editor,ebook manager,ebook organizer,ebook viewer,email,flatpak,free,geology,help desk,issue tracking,live system,macOS,machine learning,multimedia,notification,open source,programming,research,science,spreadsheet,test automation,ticket system,tiling,version control,wallpaper,wayland,weather,web,web analytics,window managers
---

# Morning Brew — 2026-08-28

A heavy LinuxLinks day (a dozen self-hosted and open-source tool writeups), a fresh batch of 9to5Linux release news, and a whole lot of Less Bitter / Better Stack AI-agent content — Grok Bot, Claude's browser, Perplexity's "Computer," and the internet rotting into AI junk. 46 items total: 14 videos, 32 articles. Buckle up.

## 1. Ubuntu 26.04.1 LTS Is Now Available for Download, Here's What's New — by 9to5Linux

![9to5Linux](https://9to5linux.com/wp-content/uploads/2026/08/u2641.webp)

**Source:** https://9to5linux.com/ubuntu-26-04-1-lts-is-now-available-for-download-heres-whats-new
**Karakeep doc:** `uup3zki8fyhvfaiqu47ug6ic`

Canonical dropped the first point release of Resolute Raccoon, bundling all the security patches and software updates since April into fresh ISOs so you don't have to pull hundreds of updates post-install. The big deal: it finally unlocks upgrades from 24.04 LTS (Noble Numbat), so all you holdouts can stop sitting on the old LTS. Next point release, 26.04.2, lands February 2027 with kernel 7.2 and Mesa 26.2. New installs only, obviously.

## 2. DVinyl — self-hosted collection manager — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/dvinyl-self-hosted-collection-manager/
**Karakeep doc:** `ew5i9op7v8szr0jh05atyq2x`

A TypeScript self-hosted cataloguer for physical media and collectibles — vinyl, CDs, cassettes, books, manga, Blu-ray, VHS, video games, even LEGO sets. Metadata gets pulled from Discogs, Hardcover, TMDB, IGDB and Rebrickable, and the plugin-based design means you only enable the media types you actually hoard. It's got a barcode scanner, bulk Discogs imports, market-value estimates for music, wishlists, and a no-code editor for custom collection types. MIT-licensed, Docker Compose deploy.

## 3. Calibre 9.14 Open-Source E-Book Manager Is Out with More AI Features — by 9to5Linux

![9to5Linux](https://9to5linux.com/wp-content/uploads/2026/08/cal914.webp)

**Source:** https://9to5linux.com/calibre-9-14-open-source-e-book-manager-is-out-with-more-ai-features
**Karakeep doc:** `t1zy7xa8aent2y3shavd32i3`

Kovid Goyal shipped Calibre 9.14 with yet more AI shoved in — AI-generated book covers in romance/sci-fi/pulp styles, plus Anthropic and Grok backends for Claude and Grok models (GitHub backend got the boot). The Edit book file browser now shows floating image previews and the Tags editor ignores accents. A pile of security fixes landed too: a remote code execution vuln for authenticated users, XSS in the Legacy book details page, and arbitrary file write bugs. The comments are predictably furious about the AI bloat.

## 4. SWE-agent lets your LLM autonomously fix real GitHub issues via a single YAML file — by Open-source Projects

![Open-source Projects](https://www.opensourceprojects.dev/favicon.ico)

**Source:** https://www.opensourceprojects.dev/post/ee7b25d1-aef2-499e-a0c8-de77a23d9161
**Karakeep doc:** `t0uc51606i9encrpiev3u9sg**

SWE-agent is the Princeton NLP agentic software-engineering framework that hands an LLM a terminal, a file editor, and a search tool and lets it autonomously work through real GitHub issues. The whole agent — tools, prompts, model, loop — is configured from a single YAML file, which is the whole point: you can define your own agent without touching Python. It's the thing that made the SWE-bench benchmark famous and it's still the reference for "LLM fixes your bugs" workflows. (Note: the source post 404'd, so this is from the project itself.)

## 5. Capacitor: run your web app natively on iOS, Android, and the web from one codebase — by Open-source Projects

![Open-source Projects](https://www.opensourceprojects.dev/favicon.ico)

**Source:** https://www.opensourceprojects.dev/post/47aacb96-16f2-447d-ac1a-a8b4ca47b7f2
**Karakeep doc:** `ssb8fchz4rljj0duxqe5fw6f`

Ionic's Capacitor is the "stop rebuilding your app for every platform" tool — your web app runs in a native webview on iOS/Android and Capacitor bridges to native SDKs (camera, file system, biometrics) via JS APIs. Unlike some alternatives, the generated native projects are real, editable source you can open in Android Studio or Xcode, not opaque build artifacts. It's drop-in for existing web apps, backward-compatible with most Cordova plugins, and doesn't force Ionic Framework on you. `npm install @capacitor/core @capacitor/cli` and `npx cap init` gets you going.

## 6. PHP gets a full agentic framework: workflows, MCP, and multi-agent orchestration — by Open-source Projects

![Open-source Projects](https://www.opensourceprojects.dev/favicon.ico)

**Source:** https://www.opensourceprojects.dev/post/d5d3c40a-fc9d-4f07-8247-bfea91e68fa1
**Karakeep doc:** `spihkb6jug3vcr0wasx28606`

Neuron AI is a PHP 8.1+ framework for building actual agentic systems, not just bolting API calls onto a form. It brings event-driven workflows with checkpointing, human-in-the-loop interruptions, multi-agent orchestration, an MCP connector, and streaming via AG-UI and the Vercel AI SDK protocol. The pitch is that the same workflow engine scales from a "getting started" agent to production stateful systems, and monitoring/debugging is built into the core rather than bolted on. Install via Composer as `neuron-core/neuron-ai`.

## 7. SnafflePy: run Snaffler-style SMB file hunting from non-Windows machines — by Open-source Projects

![Open-source Projects](https://www.opensourceprojects.dev/favicon.ico)

**Source:** https://www.opensourceprojects.dev/post/3dd46081-0074-4bb4-8717-f29a0dcc5160
**Karakeep doc:** `l6lds7rh0s3zu1ogivl4ziik`

A Python port of Snaffler for when you're on a Linux laptop but need to hunt juicy files across Windows SMB shares. It LDAP-discovers domain-joined machines, then authenticates over SMB with a graceful fallback chain (your creds → Guest → NULL session) and pulls files matching Snaffler's TOML interest rules — password files, backups, SSNs via regex. The `--go-loud` flag skips filtering and just enumerates everything it can reach, with a well-earned "use at your own risk." Not a full port yet (classifier system still on the roadmap), but the core hunting works.

## 8. Atoll turns the MacBook notch into a live command surface with SwiftUI animations — by Open-source Projects

![Open-source Projects](https://www.opensourceprojects.dev/favicon.ico)

**Source:** https://www.opensourceprojects.dev/post/bed47425-5116-4ad8-a968-269e5d6c4ad5
**Karakeep doc:** `l09mrf85rx8qrw0ycok3kskl`

Atoll is a Dynamic Island for macOS — it repurposes the notch into an interactive panel that stays invisible until you hover, then expands with smooth SwiftUI animations. It does media controls (Apple Music, Spotify, Cider), Live Activities for Focus/screen-recording/privacy status, lock-screen widgets, system stats (CPU/GPU/mem/network/disk), and productivity tools like timers, clipboard history, and a color picker. Needs macOS 14+, a notched MacBook, and a pile of permissions. Configurable layouts, animations, and shortcuts.

## 9. Project-based learning curated by language, from OS kernels to game emulators — by Open-source Projects

![Open-source Projects](https://www.opensourceprojects.dev/favicon.ico)

**Source:** https://www.opensourceprojects.dev/post/fe524595-11df-47b4-84e3-0e1cb265a5f9
**Karakeep doc:** `gt75v0ax5y9lwl9bql87u7hb`

The practical-tutorials/project-based-learning repo is a curated list of tutorials where the goal is a real, working project built from scratch — shells, text editors, CHIP-8 emulators, key-value stores, even OS kernels — organized by language from C# to Swift. The "from scratch" constraint is the whole point: no heavy frameworks hiding the interesting bits, so you actually learn memory, algorithms, and architecture. Actively maintained with a link-rot sweep action. Pick a project that scares you a little and block out a few weekends.

## 10. Clash Verge Rev: a Tauri-based Clash Meta GUI with built-in mihomo kernel — by Open-source Projects

![Open-source Projects](https://www.opensourceprojects.dev/favicon.ico)

**Source:** https://www.opensourceprojects.dev/post/441b5d2b-4c97-4e32-8a20-ed0e2f9b2116
**Karakeep doc:** `eqxle6ficrogpkhbveq0vcht`

A community continuation of the abandoned Clash Verge, rebuilt on Tauri 2 + Rust so it's fast and light on RAM compared to Electron alternatives. It wraps the mihomo (Clash.Meta) kernel with profile management, merge/script enhancements, visual node/rule editing, TUN mode, and WebDAV backup/sync. The mihomo kernel ships bundled but you can swap to an Alpha build for bleeding-edge features. Windows, Linux, and macOS 11+ all covered. If you manage Clash configs through a browser tab, this is the upgrade.

## 11. FxSound: open-source digital audio processing for Windows with a clean passthrough — by Open-source Projects

![Open-source Projects](https://www.opensourceprojects.dev/favicon.ico)

**Source:** https://www.opensourceprojects.dev/post/cbfc5ff6-a244-4f79-b9c3-5d8656092120
**Karakeep doc:** `e92h8i4c7daw7kux2izhi18p`

FxSound is a system-wide Windows audio processor built on a high-fidelity engine whose key design decision is clean passthrough — when no effects are active, your audio is unaltered, so you're not forced into a "sound signature." On top of that you get volume, timbre, and EQ effects. Architecture is three cleanly separated components: a JUCE-based GUI, an `audiopassthru` module, and a `DfxDsp` DSP module. It needs a virtual audio driver ("FxSound Audio Enhancer") installed to intercept system audio. Now open source, so you can build it yourself and see exactly what's under the hood.

## 12. 9 Best Free and Open Source No-Code Database Tools — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/best-free-open-source-no-code-database-tools/
**Karakeep doc:** `u0c7zqilgfod2efer5j40q3v`

A roundup of hybrid spreadsheet-plus-database tools that let you build databases without a developer. The lineup: NocoDB, Teable, Baserow, Directus, Grist, rowy, Saltcorn, Mathesar, and UNDB. The pitch is these sit between LibreCalc and a real database, letting you filter and visualize large datasets without code. All open source, though many offer paid extras — LinuxLinks only rates the open-source versions. If you're tired of Airtable's pricing, this is your menu.

## 13. EKO — graphical sound editor — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/eko-graphical-sound-editor/
**Karakeep doc:** `nqj7fgxkq1dft09exwbfrtnx**

A Qt 6 graphical sound editor (public domain, C++) that loads audio into memory and runs a 32-bit floating-point mixing/DSP engine with PortAudio for I/O. It handles a ton of formats via libsndfile, opens MP3s, extracts audio from video via FFmpeg, and exports MP3 through LAME. Features include waveform editing, cut/copy/paste with auto-resampling, recording with input monitoring, reverse/fade/RMS tools, DC-offset correction, volume envelopes, and named sessions. Single-instance, with an integrated manual.

## 14. 10 Best Free and Open Source X11 Tiling Window Managers — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/best-free-tiling-window-managers/
**Karakeep doc:** `qw57v8faoitp2ii577c2jmvh`

A roundup of X11 tiling window managers for the keyboard-driven crowd who want to stop dragging windows around. The ten: i3, StumpWM, bspwm, EXWM, herbstluftwm, wmderland, Notion, zwm, Ratpoison, and NWM. The pitch is efficient screen real-estate use and keyboard-only workflows that boost productivity and cut RSI. Dynamic WMs for X11 get covered separately, so this is strictly the tiling set. If you've been meaning to ditch your floating WM, here's the shortlist.

## 15. 6 Best Free and Open Source Geology and Earth-Surface Science Tools — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/best-free-open-source-geology-earth-surface-science-tools/
**Karakeep doc:** `g4swrncqh03ldrxwimrmh0ty`

A roundup of open-source geoscience tools, leaning on the reproducibility argument — researchers can inspect and improve the algorithms rather than trust a black box. The six: Survex (cave surveying/mapping), GPlates (plate-tectonic visualization), Therion (2D/3D cave drawing), GemPy (3D structural geological modeling with uncertainty analysis), Landlab (component-based numerical modeling of Earth surface processes), and Grock (UK geological map display). Covers everything from cave mapping to simulating erosion.

## 16. Atmos Weather — cross-platform weather client — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/atmos-weather-cross-platform-weather-client/
**Karakeep doc:** `ajd4pdbgh0oq0wpfhpome1or`

A cross-platform (Linux, macOS, Windows, Android) weather client focused on the US, pulling forecasts from Open-Meteo and official warnings from the National Weather Service API. It monitors alerts across multiple locations with per-warning-type and per-location priority config, shows warning polygons on an interactive map, and delivers alerts via desktop notifications and text-to-speech. Location search uses OpenStreetMap Nominatim. Shares its interface code across desktop, web, and Android. GPLv3, JavaScript.

## 17. I replaced my entire tech stack with Postgres — by Better Stack

![Better Stack](https://i.ytimg.com/vi/MZfhhl6ej-k/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=MZfhhl6ej-k
**Karakeep doc:** `z462soe01oq6kyan69g2hzi9`

The "poor man's web stack" video: replace Redis, a vector DB, Elasticsearch, PostGIS, cron, and MongoDB with just Postgres, because we can, damn it. Caches via UNLOGGED tables (fast writes, wiped on crash — perfect for a cache), vector search via pgvector, full-text search via tsvector + GIN indexes, geospatial via PostGIS (with the classic "longitude goes first" gotcha), scheduling via pg_cron, and document storage via JSONB or DocumentDB. The honest caveat: this only makes sense if you're not targeting hundreds of thousands of users. Genuinely useful tour of the extension ecosystem.

## 18. BracefaceOS — Debian-based Linux distribution — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/bracefaceos-debian-based-linux-distribution/
**Karakeep doc:** `sivlla1zw4o1uzole0zwtzdm`

A customized Debian-based distro by Jacob Yee, running KDE Plasma with systemd, APT package management, and a fixed release model for x86_64. It's part of LinuxLinks' Big List of Active Linux Distributions. Not much else to say — it's a Debian + KDE Plasma customization, active, and that's about the whole pitch. If you want a pre-tweaked Plasma-on-Debian without doing the work yourself, this is the kind of thing you'd look at.

## 19. Qisutu — open source ticket system — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/qisutu-open-source-ticket-system/
**Karakeep doc:** `bso1wucccfrsyws1e675lcpa`

A self-hosted ticket system (AGPLv3, Perl/CGI + MariaDB/MySQL + Template Toolkit) with separate agent and customer portals, email processing over IMAP/SMTP, automation, reporting, a knowledge base, a CMDB, and a REST API. It supports Microsoft 365 and Google Workspace auth via OAuth2/XOAUTH2, LDAP/AD auth, CSV imports, TOTP 2FA, encrypted stored secrets, and eleven interface languages. The installer configures the web server, services, database, and initial admin account. A proper helpdesk if you want to self-host and don't mind Perl.

## 20. Orange Pi Zero 4 with Octa-Core Allwinner A733, PCIe 3.0, and Wi-Fi 6 — by LinuxGizmos.com

![LinuxGizmos.com](https://linuxgizmos.com/favicon.ico)

**Source:** https://linuxgizmos.com/orange-pi-zero-4-with-octa-core-a733-wi-fi-6-and-gigabit-ethernet/
**Karakeep doc:** `d2bsvr6y4vmd9ytjy95u6jry`

Orange Pi's Zero 4 is a 50×55mm SBC built on the Allwinner A733 — 2× Cortex-A76 + 6× Cortex-A55 up to 2.0GHz, a PowerVR BXM-4-64 GPU, a 3 TOPS NPU, up to 16GB LPDDR5/LPDDR4X/LPDDR4, Gigabit Ethernet, Wi-Fi 6, and Bluetooth 5.4. Display is Mini HDMI up to 4K@60 plus USB-C with eDP/DisplayPort, and there's PCIe 3.0 + USB 3.1 on a 16-pin FPC. The comment section is predictably salty about Allwinner's spotty Linux support. Download links and purchase links weren't live at publication.

## 21. I've never laughed this hard in my entire life — by Less Bitter

![Less Bitter](https://i.ytimg.com/vi/QAx6Qn3W23Y/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=QAx6Qn3W23Y
**Karakeep doc:** `paabqmmkzjx0v9hfkqgxg5tb`

Less Bitter takes a swing at Perplexity's new "Computer" agent product and finds it a UX nightmare — nested models, endless permission prompts, and a "create skill" button that just types "create skill" into chat. The verdict: busted, pure hype, especially next to Grok Bot. The highlight is a satirical website he builds ("Complexity — the answer engine, but harder") with copy that absolutely skewers Perplexity's over-engineered onboarding: "we surveyed zero users," "47-step onboarding," "ambient progress bars that never finish." He calls it the best copywriting he's ever seen and credits GLM 5.2.

## 22. Wtf is Anthropic even doing anymore — by Less Bitter

![Less Bitter](https://i.ytimg.com/vi/YAs85Ceuhf4/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=YAs85Ceuhf4
**Karakeep doc:** `n6kbgysld9qk205vcxbf8vfq`

Less Bitter pokes at Claude's new built-in browser and CoWork, and finds the whole thing slow, clunky, and bolted onto the same awkward linear-chat interface. The Chrome extension can summarize pages and fill forms, but it's painfully slow and the "browse in CoWork" feature wasn't even wired into his session yet — announced as if available, then "rolling out over the next week." His recurring thesis: Anthropic and OpenAI are tethered to a chat UX while Grok Bot already solved this with a Slack-like, character-based agent interface. "Fuck you Anthropic" energy throughout.

## 23. OpenAI is advertising on scientists like Nike advertises on players — by Less Bitter

![Less Bitter](https://i.ytimg.com/vi/RwWodJu7DYw/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=RwWodJu7DYw
**Karakeep doc:** `x5mifijz7g8dkh2v84gicu6g**

Less Bitter's take on the OpenAI-scientists hype cycle: it's Nike advertising on athletes and pretending the shoes won the game. The key line he keeps hammering is that the dialogue between physicists and LLMs can generate new knowledge — but the LLMs aren't generating it; the humans are, using AI to automate the laborious parts. He cites François Chollet's counterpoint that base LLMs scaled 50,000× but made zero progress on ARC until labs shifted to test-time adaptation, and Lee Cronin's claim that AI can't in principle make novel discoveries. The media (NYT, WSJ) is susceptible to the hype; the real story is humans + AI as a tool, like a calculator.

## 24. How to come up with profitable app ideas — by Less Bitter

![Less Bitter](https://i.ytimg.com/vi/yeyFYMhyiiM/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=yeyFYMhyiiM
**Karakeep doc:** `pstxm0di4bsnwc22ijtp7b9l`

The core argument: ideas don't arrive through inspiration, they come from motion. If you don't have an idea, start with your worst one — even cloning an app you already use — because ideas start flowing while your hands are busy building. Cloning something that exists also skips the hardest product question (does anyone want this?) since you already know they do, and a small indie founder with a unique distribution channel can win customers who'd rather not pay Google or Microsoft. Software is fashion, taste, marketing, and distribution, not just utility — so there's always room for one more.

## 25. Grok Bot Is Weirdly Revolutionary — by Less Bitter

![Less Bitter](https://i.ytimg.com/vi/K6BYzjwkp24/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=K6BYzjwkp24
**Karakeep doc:** `oe10daj5igf51ixd9cp7olbc**

Less Bitter is genuinely blown away by Grok Bot, and it's not the AI capability — it's the UX. He sets up a whole factory of little character-bots: an analytics bot that navigates his Plausible dashboard, a press bot that pings him when the NYT cover story changes, an espionage bot that watches competitors' pricing pages, an uptime bot, a substack assistant, and a personal blog manager that publishes posts by editing markdown and pushing to git. Notifications arrive as separate people per bot. He calls it "worth the $60 billion Elon paid" and predicts Claude and OpenAI will copy it. The rare video where he's not annoyed.

## 26. The internet is filling with junk — by Less Bitter

![Less Bitter](https://i.ytimg.com/vi/lQIfkCeJKss/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=lQIfkCeJKss
**Karakeep doc:** `gt9k34aqlgiqxbozw4z07028`

The thesis: AI research is broken because 79% of top news sites now block AI crawlers, so models read the sketchy part of the internet and cite AI content farms. A May 2026 study ran 712 questions through ChatGPT, Copilot, Gemini, and Perplexity and found one in six citations pointed at another AI's content — on politics, health, and environment, not air fryers. He calls it a "fake news launderer": 49.9% of Q1 2026 news articles were AI-generated, and fabricated citations in academic papers jumped from 1-in-2800 to 1-in-277. The advice: click every source yourself with your "disgusting blood-filled veiny eyeballs" before submitting anything. Also, the code is 10% of a software business; marketing is the rest.

## 27. MorphEdit — browser-based and desktop audio editor — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/morphedit-browser-based-and-desktop-audio-editor/
**Karakeep doc:** `vfead25d7c1vdjm3uicdxbsd`

A TypeScript audio editor (GPLv3) built for preparing samples for hardware instruments, with dedicated support for Make Noise Morphagene reels. All processing is local — nothing uploaded to a server — and it runs in the browser, offline as a PWA, or as an Electron desktop app. Features: high-res waveform with zoom, splice markers with transient detection and zero-crossing snapping, sample-level cropping, fades, normalization, tempo/pitch via Rubber Band, BPM detection and slicing, and Morphagene-compatible 48kHz/32-bit WAV export. Batch processing and undo/redo included.

## 28. This Makes Claude Code Free Forever — by Better Stack

![Better Stack](https://i.ytimg.com/vi/vxrZWbZ2fZA/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=vxrZWbZ2fZA
**Karakeep doc:** `dismobyrfa5oxp611fcpsiy9`

Better Stack tests "Free Claude Code" (FCC), a 48k-star open-source proxy that sits between Claude Code/Codex/Pi and the model, letting you route requests to free, cheaper, or fully local models while keeping the exact same interface. He installs it, points it at NVIDIA NIM, and refactors a React component — it works, and the interface looks identical (it even still says "Opus 5"). The real value isn't "Claude for free," it's tier routing: use strong models for hard tasks and free ones for boilerplate, instead of paying premium prices out of habit. His caveat: reliability matters more than token cost, so don't cheap out on the hard stuff.

## 29. Don't Throw Away Your Old Laptop— This Tiny OS Might Surprise You! — by Spec Tech

![Spec Tech](https://i.ytimg.com/vi/qPwzveYKHt8/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=qPwzveYKHt8
**Karakeep doc:** `f1gp6612bv8zs16c5mps4pv8`

Spec Tech boots KolibriOS — a 1.44MB assembly-written OS that fits on a floppy — on a 19-year-old Fujitsu FMV Biblo running Windows Vista. The whole OS loads into RAM (the 1.4MB system disk is a RAM drive), so it's absurdly fast and responsive on a single-core Sempron with 1.5GB DDR2. It's got a full GUI, three file managers, media tools, a PDF viewer, 3D modeling, over 30 games (including a literal Chrome dinosaur clone and Doom), and even a benchmark tool. The catch: no internet on this machine due to missing network drivers. A fun "how much can a tiny OS do" experiment.

## 30. XDA (@xdadevelopers) on X — by X (formerly Twitter)

![X (formerly Twitter)](https://pbs.twimg.com/profile_images/1470454627825029122/6pOlVWyd_400x400.jpg)

**Source:** https://share.google/xkvQSQmp3NhNA4NlW
**Karakeep doc:** `y3ka2kanwhvi58evpxp57yte`

XDA's tweet: "I tested PS3 emulation on Android, and the Pixel's biggest limitation isn't what I thought." The post links to their article (bit.ly/4y1KDug) about running PS3 emulation on a Pixel, teasing that the real bottleneck isn't what you'd expect — presumably not raw CPU/GPU but something like thermals, memory bandwidth, or driver support. 12.2K views, 39 likes, 7 reposts. A teaser for the full XDA writeup.

## 31. When did the Rabbit R1 become this good? — by Reysu

![Reysu](https://i.ytimg.com/vi/14TBuOFw4KM/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=14TBuOFw4KM
**Karakeep doc:** `o81fra45idx46p2rhc2qhzrw`

Reysu revisits the Rabbit R1 two years after it was "barely reviewable" and finds it quietly became a genuinely useful productivity device — not because the hardware changed, but because frontier models improved and the company kept shipping. The killer feature is integration with AI agents (OpenClaw, Claude Code, and Hermes), letting you run frontier models on a dedicated, distraction-free pager device with a single push-to-talk button. He uses it to check YouTube Studio stats and summarize videos into Obsidian. The main criticism: Rabbit's own built-in AI still feels like a two-year-old model, and the dictation is mediocre.

## 32. The PSP Can Play These Games? — by Macho Nacho Productions

![Macho Nacho Productions](https://i.ytimg.com/vi/dsCWVhGh1N8/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=dsCWVhGh1N8
**Karakeep doc:** `y7bsznqlc950u3fzs3km8hrz**

Macho Nacho builds the updated PSP6 kit from Othermod — a Raspberry Pi Compute Module 4-powered PSP that can emulate a wide range of systems and, via Steam Link, play your Steam library on the 20-year-old handheld. He UV-prints a "Steam Portable" shell with the E1 printer, then walks through the solderless build. Steam Link works over the home network or remotely via a Unifi travel router, and a PS5 controller pairs over Bluetooth for modern games. The big con remains the lack of a second analog stick, though Othermod is working on a replacement shell. He's also at RetroWorld Expo in September.

## 33. The Little Clock On Every CPU — by Brodie Robertson

![Brodie Robertson](https://i.ytimg.com/vi/2FuhK087pHw/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/2FuhK087pHw
**Karakeep doc:** `qyw9cybtyoeegmp4ovj3x83k`

A short explainer on the Time Stamp Counter (TSC), the register on every x86 CPU that counts CPU cycles since reset. It's used for performance profiling and low-level timekeeping, but it's not fully reliable on multi-CPU systems (which TSC do you trust? — you just pick one as the source of truth). Early TSCs were tied to internal clock speed, which broke when boosting or power-saving changed the frequency, so modern CPUs use an invariant TSC that runs at a steady rate independent of CPU speed. Long story short: it's a clock, used for clock things.

## 34. Kepublicity – create Kobo-formatted ebooks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/kepublicity-create-kobo-formatted-ebooks/
**Karakeep doc:** `ftjmj17hattugstpttqkdq3x`

A Vala/GTK+ graphical app (GPLv3) that turns standard EPUBs into Kobo-formatted KEPUB files without touching the command line. It uses kepubify as the conversion engine — the Flatpak bundles kepubify alongside the app rather than relying on a separate install. You can add EPUBs via drag-and-drop, batch-process multiple books, and either save the KEPUBs locally or send them straight to a connected Kobo device. A simple GUI wrapper for a CLI tool, by Nathan Dyer.

## 35. SeleniumBase — all-in-one Python framework — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/seleniumbase-all-in-one-python-framework/
**Karakeep doc:** `fi2vn1y5bniyi8bne5xdwanc`

An MIT-licensed Python framework that extends Selenium WebDriver with higher-level APIs, automatic smart waiting, test runners, and recording/reporting tools for browser automation, end-to-end testing, crawling, and scraping. It integrates with pytest, unittest, nose, and Behave, and includes a CDP Mode for stealthy Chromium automation plus a stealthy Playwright mode built on it. It can record browser activity and generate Python tests, run tests concurrently across browser instances, emulate mobile devices, and generate dashboards, reports, screenshots, and logs. A one-stop shop for web testing.

## 36. 15 Best Free and Open Source Google Analytics Alternatives — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/googleanalytics/
**Karakeep doc:** `e541fzez1p0pi6rfm3ahjie7`

A roundup of self-hosted web analytics tools for people who don't want Google controlling their data. The 15: Matomo, GoAccess, Umami, Rybbit, Openpanel, Open Web Analytics, Plausible, Shynet, GoatCounter, W3Perl, Tianji, Swetrix, Medama, Ackee, and AWStats. The pitch is that self-hosting keeps full control over your data and visitor privacy, versus Google Analytics where your data is used for Google's own purposes. If you're privacy-conscious or just hate giving Google your traffic data, this is the full menu.

## 37. DXVK 3.1 Released with Initial Support for DXGI Present Parameters — by 9to5Linux

![9to5Linux](https://9to5linux.com/wp-content/uploads/2026/08/dxvk31.webp)

**Source:** https://9to5linux.com/dxvk-3-1-released-with-initial-support-for-dxgi-present-parameters
**Karakeep doc:** `g79r1q6wbeggeji2bcsrnwii`

DXVK 3.1 is out, the Vulkan-based D3D9/D3D10/D3D11 implementation for Linux/Wine. Highlights: initial DXGI present parameters support to fix UI rendering in VirtualDJ and launchers like Ubisoft Connect, render target views on buffers directly (helps older Frostbite titles like Battlefield 3), and loading Intel-specific extension libraries for future Proton Intel vendor extensions. It also fixes a D3D9 fog regression that broke Mabinogi and The Witcher 1, works around an NVIDIA out-of-memory crash, and improves Ghost Recon Breakpoint, RaceRoom, and Mirror's Edge. Grab it from GitHub or wait for your distro's repos.

## 38. bmm — command-line bookmark manager — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/bmm-command-line-bookmark-manager/
**Karakeep doc:** `uyd8sx44e20wlmgszymxzlj6`

An MIT-licensed CLI bookmark manager (by Dhruv Thakur) that stores bookmarks locally in SQLite and offers both a traditional CLI and an interactive terminal interface. Every action is available from the command line, so it integrates with fzf and shell scripts. It imports bookmarks from HTML, JSON, and plain text (including standard Netscape browser exports), searches by URI/title/tags, opens results in a browser, copies addresses to the clipboard, and outputs in formats for other CLI tools. A fast, scriptable way to manage bookmarks without leaving the terminal.

## 39. Mail Notification Tools: 8 Best Free and Open Source Software — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/best-free-open-source-mail-notification-tools/
**Karakeep doc:** `ryzjlemilymf70wjac54uytk`

A roundup of lightweight mail notification tools that passively tell you when new email arrives without chugging system memory. The eight: Bubblemail, Mailutils, Ayatana Webmail, Birdtray, gnubiff, CheckMails, Go IMAP notify, and Mailnag. The pitch is non-obtrusive notifications so you can focus on work, and the tools are deliberately lightweight. Even if you get notifications on your phone, having them on the desktop too is handy. A shortlist for anyone who wants desktop mail alerts.

## 40. Ryot — track media consumption, exercise, workouts and body measurements — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/ryot-track-media-consumption-exercise-workouts-body-measurements/
**Karakeep doc:** `b4xjzrh1z8rl0h4ptderjm9t`

A self-hosted (GPLv3, TypeScript + Rust) platform that tracks media consumption, exercise, workouts, and body measurements. The media catalogue covers movies, TV, anime, manga, books, audiobooks, podcasts, music, and video games, with imports from Goodreads, Trakt, MyAnimeList, Plex, Jellyfin, and more, plus automatic tracking via Jellyfin/Plex/Kodi/Emby integrations. It logs workouts with an extensive exercise database (sets, reps, weights, rest timers, supersets, templates) and tracks body measurements over time with graphs. OpenID Connect auth, Discord/Ntfy/Apprise notifications, GraphQL API, Docker Compose + PostgreSQL deploy.

## 41. I spent an hour convinced Cursor had replaced Git, and I was completely wrong — by Less Bitter

![Less Bitter](https://i.ytimg.com/vi/RwiOhnc0dlM/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=RwiOhnc0dlM
**Karakeep doc:** `yq5pmrur7hyy1ze25gdjqyqt`

Less Bitter spends an hour confused by Cursor's new "Origin" product, initially convinced it's a Git replacement, then realizes it's just a GitHub competitor — a git hosting platform that speaks standard git over HTTPS. He reads the 27-minute blog post (via Claude, naturally), sets up automations and a PR, and builds a satirical "G Stack" consulting site with Grok. His verdict: Origin is infrastructure marketing aimed at companies with monorepos and CI runners who resent their git host; for a solo dev, GitHub's free tier will outlast your startup. Cursor wants to be the entire IDE end-to-end.

## 42. Waywallen – dynamic wallpaper manager for Linux desktops — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/waywallen-dynamic-wallpaper-manager/
**Karakeep doc:** `pbfgpu3q2ss17at8mdfs0dyr`

A Rust/MIT dynamic wallpaper manager for Linux that handles still images and video backgrounds, arranges them in playlists, and presents them on individual displays or canvases spanning multiple monitors. It supports KDE Plasma, GNOME, Hyprland, Niri, Wayfire, Sway, and COSMIC via companion display backends, with stretch/fit/crop/center modes and sequential/shuffle/random playback. It can browse and download from Wallhaven, does Vulkan/VA-API hardware video decoding, extends via Lua plugins, and even adds Wallpaper Engine scene/web wallpaper support through an optional plugin. A serious wallpaper tool.

## 43. This is why we added up to 4 profiles to the Wireless Touchpad Keyboard.* 💭 — by Framework

![Framework](https://i.ytimg.com/vi/nvk3Njj_X0c/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/nvk3Njj_X0c
**Karakeep doc:** `r7rm7azv4tyckh0m7lubn8b9`

A Framework short explaining why their Wireless Touchpad Keyboard has four device profiles when most waitlisters only wanted to connect three. The answer: they're a laptop company constantly testing different devices, so they added one more channel — and Profile 1 comes pre-paired with the dongle in the back. A quick, self-aware explainer for a small design decision.

## 44. Cloudflare frees up 100TB of RAM by shrinking 1.1.1.1's DNS cache entries — by Tom's Hardware

![Tom's Hardware](https://www.tomshardware.com/favicon.ico)

**Source:** https://www.tomshardware.com/tech-industry/big-tech/cloudflare-frees-100tb-of-ram-by-shrinking-dns-cache-entries
**Karakeep doc:** `fsxms0jkdm1j8sbg3rrf1d4f`

Cloudflare freed ~100TB of RAM across its fleet — the equivalent of 130 of its 768GB Gen 13 servers — without touching physical memory, by redesigning how each DNS cache entry is laid out. Five Rust-level changes to Big Pineapple (the 1.1.1.1 resolver platform) shrank each cached entry from 953 to 420 bytes, while making the cache faster: insert throughput up 43%, lookup latency down 19%. With 250 billion cached entries at any given time, one wasted byte costs 250GB. The freed RAM goes back into larger caches to raise hit rates, not into smaller memory configs.

## 45. Supercell Wx — advanced desktop weather radar viewer — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/supercell-wx-advanced-desktop-weather-radar-viewer/
**Karakeep doc:** `yn2qz0amxixnudi0ykpurrqo`

An MIT-licensed C++ desktop weather radar viewer for monitoring current and historical weather. It visualizes live and archived NEXRAD Level 2 and Level 3 data (reflectivity, velocity, and other products) with severe weather alerts overlaid on a responsive map. It has timeline controls to navigate historical data, looping, multiple map panes with linked views, pop-out windows, configurable radar color tables, placefile overlays, and user markers. Supports MapTiler and Mapbox providers on Linux, macOS, and Windows. A proper radar tool for weather nerds.

## 46. BudsLink – monitor and control Bluetooth earbuds — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/favicon.ico)

**Source:** https://www.linuxlinks.com/budslink-monitor-control-bluetooth-earbuds/
**Karakeep doc:** `f5uydp1fwptm9w49gz4fzxsy`

A GTK4/libadwaita app (GPLv3, JavaScript) for monitoring and controlling supported Bluetooth earbuds and headphones, giving you a consistent interface instead of each vendor's mobile app. It shows per-earbud and case battery levels, controls ANC/ambient/adaptive modes, conversation awareness, in-ear detection, equalizers, gestures, and multipoint — across AirPods/Beats, Sony, Samsung Galaxy Buds, Pixel Buds, Nothing/CMF, Bose, Redmi/Xiaomi, Sennheiser, and Edifier. It exposes battery/control info via a D-Bus service for GNOME Shell, Plasma, and Cinnamon companion integrations, and includes optional packet logging for diagnostics.
