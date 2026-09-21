---
date: 2026-09-20
slug: 2026-09-20-morning-brew
tags: Developer Tools,Project Showcase,Open Source,Programming,Software Development,Linux,Technology,Networking,SSH,API Development,Developer Community,Operating Systems,Machine Learning,Artificial Intelligence,Data Science,Knowledge Graphs,Productivity,Command Line,Shell Scripting,Open Source Software,Public Key Infrastructure,Command Line Tools,Cryptography,Certificate Management,Binary Analysis,Reverse Engineering,Decompiler,Chemical Engineering,Simulation,Process Systems Engineering,Energy Systems,Data Analysis,World War I,Military History,Cybersecurity,Malware Analysis,Virtualization,Android Apps,Mobile Applications,Two-Factor Authentication,Rust Programming,Image Compression,Web Development,Immutable OS,Linux Distribution,KDE Plasma,Operating System,Gaming Handhelds,Typesetting,LaTeX,Document Preparation,Scientific Writing,PC Hardware,Hardware Compatibility,Firmware,Homelab,Large Language Models,Server Hardware,Scientific Computing,Data Visualization,Molecular Visualization,Structural Analysis,Web Applications,Music Software,Last.fm,Music Scrobbling,Memory Management,Debugging Tools,Undefined Behavior,DevOps,Reverse Proxy,Docker,Caddy Server,Model Context Protocol,AI Agents,API Integration,One-Time Passwords,Productivity Tools,Thermodynamics,Materials Science,CALPHAD,Solidification Modeling,Data Privacy,Self-Hosting,Password Managers,Software Migration,User Interface,Computing Technology,Wayland,Chess,Game Analysis,Python Programming,Graphical User Interface,Edge Computing,Cloud Computing,Minimalist Software,Audio Processing,Music Production,Linux Software,Guitar Effects,RSS Reader,News Aggregators,Malware,Web Technology,Photography,Image Metadata,History,Software Bill of Materials,Dependency Management,Software Compliance,DevOps Tools,Assembly Language
---

# Morning Brew — 2026-09-20

Quieter hoard day than yesterday — 43 items, but heavier on the good stuff: two videos (Brodie Robertson on Wayland global shortcuts, and a security talk on AI agents pulling malware off your own site), three roundups worth keeping (LaTeX tooling, photo-metadata editors, Google Authenticator replacements), a couple of MakeUseOf self-hosting pieces, and the usual LinuxLinks plus Open-source Projects stream. Also one niebezpiecznik.pl piece that is worth a read.

### Hand-bookmarked

## 1. ChatGPT-6 Astra cracks 108-year-old unsolved WWI German code for the first time — Crimean fleet warning verified against HMS Canterbury logs — by Tom's Hardware

![Tom's Hardware](https://cdn.mos.cms.futurecdn.net/G8KRG6QGgSMerE4dScxCJ9-1920-80.jpg)

**Source:** https://www.tomshardware.com/tech-industry/artificial-intelligence/chatgpt-6-astra-cracks-108-year-old-unsolved-wwi-german-code-for-the-first-time-radio-message-sharing-enemy-movement-intelligence-had-evaded-decoding-1918-crimean-fleet-warning-verified-against-hms-canterbury-logs
**Karakeep doc:** `d3yb7cfl6xw4bhn1i0vhi75a`

An encrypted German radio message from 1918 has apparently been read for the first time, 108 years after transmission. Developer Prinz picked the cipher off a list of 50 unsolved codes maintained by the German science blogging portal Scienceblogs.de, identified it as ADFGVX — the German military's keyword-shuffled letter grid — and solved it with GPT-6 Astra. Using TRUPPENVERSCHIEBUNG as the key, the message decoded to "EIN ENGLISCHER KREUZER EINLIEG X SEWASTOPOL X S4STEN X EIN GESCHWADER DER X ALLIIERTEN FOLGT 26STEN X": an English cruiser arrived at Sevastopol on the ?4th, an Allied squadron follows on the 26th. Prinz then checked it against historical records. HMS Canterbury reached Sevastopol in Crimea on November 24, 1918, matching the arrival detail — the stray question mark is probably a transmission typo — and the Allied squadron's November 26 date was correct. The message was addressed to the German High Command, for an admiral or Naval Command. Mark Tyson reported it for Tom's Hardware on September 19. Caveats worth stating plainly: this rests on one developer's Substack and an X post, with no independent cryptanalysis and no peer review, and the model is pattern-searching a known cipher family rather than inventing an attack. Charming result regardless, and a useful reminder of how much 1918 traffic is still sitting in drawers. Delightful, and about as verified as a war-history side project gets.

## 2. No GPU, No Problem: Flagship LLMs On A GPU-less Teenaged Server — by Hackaday

![Hackaday](https://hackaday.com/wp-content/uploads/2026/09/LLM-dell-server-feat.jpg)

**Source:** https://hackaday.com/2026/09/20/no-gpu-no-problem-flagship-llms-on-a-gpu-less-teenaged-server/
**Karakeep doc:** `vs4ssez1iup5zshu2vm56awo`

The standard advice for running big models locally is buy VRAM you can't afford. [MattMo] went the other way and put GLM 5.3 Flash, Qwen 3.8 Flash and Qwen 3.8 27B on a 14-year-old Dell PowerEdge R720 with no GPU in it at all. The models fit in 348 GB of DDR3 system memory, and nothing needs a graphics card to load them. Output landed at about four tokens per second, capped by 20 threads across two ageing Xeons that lack instructions newer inference code likes to use. Hackaday's own framing is dancing bear: it works, it's slow, and it's roughly $600 second-hand if you have to buy the hardware.

Commenters did not let it go. The load-bearing objection is AVX2, which the R720 lacks, and that rules out the 1-bit and ternary models that make CPU-only inference pleasant. Those retain up to 95% of fp16 accuracy, so skipping them costs more than accuracy. One reader reports an i7-4790 with 32 GB of DDR3 at 1333 MHz hitting 7-8 tokens per second on a 27B ternary model while drawing 80-90 W for the CPU and about 100 W for the whole system. Others say an RX 6800 XT gets 90 tok/s on gpt-oss:20b for under $400, a Tesla P100 drops into an R730xd for under $100, and a cheap used office PC beats a crusty server for this job. Electricity and fan noise came up repeatedly, one thread suggested sharding the model across every machine on a LAN. The R720 still makes sense if batch work at 4 tok/s is acceptable and the server is already humming in your basement. 🖥️

---

## 3. I replaced 1Password with this open-source alternative and regained full control of my data — by MakeUseOf

![MakeUseOf](https://static0.makeuseofimages.com/wordpress/wp-content/uploads/wm/2026/04/vaultwarden-github-on-laptop-screen-bitwarden-background.jpg?w=1600&h=900&fit=crop)

**Source:** https://www.makeuseof.com/i-replaced-1password-with-open-source-alternative-regained-full-control-of-my-data/
**Karakeep doc:** `ca5wk7wtvl30tc30rns4purm`

The author already self-hosted almost everything else at home, so storing passwords on his own box stopped looking like a new risk. He moved from 1Password to Vaultwarden, the Rust reimplementation of the Bitwarden Client API, and kept using Bitwarden's own clients and browser extension against his server.

The surprise is how little changed. Extension pops up, credentials fill, TOTP code drops into the MFA field. Migration was one unencrypted export file, imported on a laptop disconnected from everything, then the plaintext file was deleted. Folders survived with their structure, and TOTP secrets came across without rescanning a single QR code. What didn't survive: a batch of secure notes lost formatting, bold text and bullets got stripped. That's the honest cost line in the piece.

The change that actually bites is maintenance. Container image updates, TLS certificate renewal, and testing backups are now his job. He had a scheduled backup failing for two weeks without noticing, purely because he never tried to restore from it. His Vaultwarden instance is reachable only over a VPN, which keeps the login page off the public internet.

Where it leaves you: Bitwarden Lite is the official single-container option with vendor support, and KeePassXC keeps the vault in a local encrypted database you sync however you like. Vaultwarden won here because he already knew the Bitwarden clients. Control turns out to mean remembering to do things nobody reminds you about. 🔑

## 4. I installed this free open-source app for Android to see what my apps were actually connecting to — by MakeUseOf

![MakeUseOf](https://static0.makeuseofimages.com/wordpress/wp-content/uploads/wm/2026/09/pcapdroid-working-on-android-phone.jpeg?w=1600&h=900&fit=crop)

**Source:** https://www.makeuseof.com/installed-free-open-source-app-android-see-what-apps-were-connecting-to/
**Karakeep doc:** `sq18vmtr3341epxk4jojjp8n`

After a desktop firewall showed him how much noise runs unnoticed on his PC, the author wanted the same view on Android. PCAPdroid does it without root: it spins up a local VPN, then reports which app opened a connection, where it went, and how much traffic moved. The free tier was enough — the Connections tab and exportable lists did the job, though it hands you raw data with no context or warnings.

HTTPS decryption mostly didn't work. The mitm add-on and certificate got a couple of connections marked decrypted, most threw certificate errors or refused outright, and PCAPdroid says flat out it can't decrypt QUIC, which covers a lot of Google app traffic. He gave up on that and read the domain lists instead.

Numbers worth staring at. His banking app OPay recorded 61 connections across 20 domains, including AppsFlyer, datadoghq.com, app-measurement.com, graph.facebook.com and whatismyip.akamai.com — fintech marketing and analytics plumbing he'd never seen. His niece's Monster High game logged 375 connections in minutes, hitting Pangle, AppLovin, DoubleClick, Moloco, Firebase Crashlytics, Chartboost, InMobi, TikTok ad domains and Alibaba Cloud infrastructure. WhatsApp Business made 121 connections over two hours, nearly all back to Meta. Chrome hit 4,930 connections across 543 domains, most of it the websites he'd visited.

Side effects are real: long sessions degraded connectivity, notifications stopped, and "No dump" mode loses everything when the system freezer kills the app, so use PCAP file mode. He uninstalled Monster High from both tablets. That's a better outcome than another permissions screen. 📡

### RSS — YouTube

## 5. Wayland Global Shortcuts Takes Another Big Step — by Brodie Robertson

![Brodie Robertson](https://i.ytimg.com/vi/t1LaLW7wabk/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=t1LaLW7wabk
**Karakeep doc:** `tq09pvrblsfg7pb8wj8wwok7`

Brodie opens by saying Wayland governance is broken, then immediately regrets saying it out loud. The trigger is the merge of xdg-hotkey-v1, the Global Hotkey Protocol, into the experimental namespace of wayland-protocols. Experimental status is cheap — a proposal, a protocol, no requirement that members acknowledge it, unlike WP or XDG (three member acks plus three open-source implementations, split across clients and servers) or EXT (two acks, two implementations). This one landed anyway, and it sits in direct tension with the existing Global Shortcuts portal.

His case against the portal is the substance of the video. It yanks shortcut control out of the application and into your desktop's shortcut settings, where bindings for unrelated apps are heaped together. Double-binding one key to several actions isn't possible, which is normal behaviour in OBS. Clients get no feedback about whether their binding was honoured, so apps can't tell users what went wrong. There's no libportal wrapper — PRs attempting one were ignored — so every framework hand-rolls session and request handling around DBus. Standalone compositors like Hyprland and Niri, where the portal is either missing or misconfigured, get excluded entirely.

The counter-argument that got the most airtime is the "keylogger protocol" claim. Brodie calls it bad faith: denied and revoked events let a compositor prompt for approval and list active binds, and implementations he contributed all restrict which key combinations can be bound. He also notes that the protocol had real implementations before the merge — Hyprland merged, Ghostty merged, Niri and OBS still open.

Then XFCE's Wayland lead, Brian Taracone, arrived with a fifteen-years-of-X11 perspective and said the portal feels backwards: users look for shortcut settings in the app that registered them. Someone told him "people like you" don't understand, followed by "if you genuinely believe that global shortcuts are input related, you have no clue what you're talking about." Brian unsubscribed.

KDE's David Edmundson replied that KWin has no plans to implement the protocol: conflict resolution gets worse, shortcuts are transient, permissions get cruder. OBS devs pointed out that if an app isn't running there's no conflict to resolve, and a prompt should offer "assign anyway." A Flatpak issue is open for double binds, and a LiveSplit draft PR exists.

What the merge actually means: not much yet. No compositor outside the early adopters has it, OBS hasn't taken it, and the portal isn't getting fixed either. Brodie's guess is small desktops and XFCE move first, apps come through plugins, and after enough adoption the choice disappears. Portal or protocol, you choose. 🎹

## 6. AI Agents Are Installing Malware From Your Own Website — by Better Stack

![Better Stack](https://i.ytimg.com/vi/9qhvD4_qmQ0/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/9qhvD4_qmQ0
**Karakeep doc:** `ts5x5jb7us0snoillqesokdg`

Better Stack's short is a four-minute scare that lands, because the evidence is specific. A researcher named Alan Hurts scanned more than 6,000 live domains belonging to defence contractors, Fortune 500 companies and big tech firms. He found over 8,000 llms.txt files — the emerging convention where sites publish a machine-readable summary so AI agents understand them faster, roughly robots.txt for language models.

Inside 120 of those files, spread across 120 different sites, sat references to code packages and domains nobody had ever registered. There were also 227 install commands pointing at names that don't exist, most likely hallucinated by AI agents in the first place. The files get trusted because they live on a company's own domain, sitting right next to its own documentation.

Hurts registered a handful of the unclaimed package names and domains himself, then wired them so anything installing or running that code would report back to a server he controlled. Four minutes later, a Fortune 500 company ran his code. Dozens more followed over the next days. Because he logged the parent process chain for every install, he could name the trigger: coding agents including Claude, Codex and Hermes, quietly executing packages no human at those companies had reviewed or approved. One misconfigured file even pointed at a live malware package.

The vulnerability doesn't sit in any individual agent. Agents have no way to check whether a package name is legitimate — they see an install command in a document that looks authoritative and run it, the same way they follow any other instruction. Nothing verifies the destination before the code executes, so the supply chain attack sits out in the open, armed by the victim's own documentation.

His advice: keep agents from blindly executing install commands copied out of documentation, pin dependencies to versions a human actually reviewed, and treat every llms.txt as untrusted input even when a trusted vendor publishes it. Subscribe to Better Stack for more of this.

### 9to5Linux (RSS)

## 7. Clonezilla Live 3.3.3-37 Disk Imaging Tool Released with Linux Kernel 7.1 — by 9to5Linux

![9to5Linux](https://9to5linux.com/favicon.ico)

**Source:** https://9to5linux.com/clonezilla-live-3-3-3-37-disk-imaging-tool-released-with-linux-kernel-7-1
**Karakeep doc:** `uazw5km9w83fzulnuogdiyay`

Steven Shiau released Clonezilla Live 3.3.3-37, two months after 3.3.3-15. The kernel moves from Linux 7.0 to Linux 7.1 for better hardware support, and the live system now carries Debian Sid packages as of September 13th, 2026. Nothing here will blow your hair back, which is the entire point of Clonezilla.

The real work is plumbing. LUKS2 repository support lands. Clonezilla Lite Server picks up PXEBoot and HTTPBoot network boot clients, with Secure Boot support for the HTTPBoot path. Restoring to an identical base disk or partition now skips partition image conversion, so you stop wasting a round trip on a copy that changes nothing.

Old cruft gets the boot. net-tools commands are gone in favour of iproute2, dhclient code is dropped for dhcpcd configured with clientid so IP reservations stay stable. GRUB gains preferred and fallback resolutions for HiDPI screens. ocs-live-boot-menu only runs efitextmode under Secure Boot lockdown, which ends the "prohibited by secure boot policy" errors. CJK font scaling in fbterm works through the --font-size argument, ocs-console-font-size boots faster, and cnvt-ocsiso-qcow2 was refactored with dual-packaging modes, flexible prefixing, and a fix for VHD boot kernel panics. ocs-live-time-sync can now handle local-time hardware clocks. netpbm and fonts-unifont join the image.

Filesystem support stays broad: Ext2/3/4, ReiserFS, XFS, JFS, FAT, NTFS, HFS+, UFS, minix, VMFS, plus LVM2, multicast, and x86/x86_64 targets. ISO and USB images, 64-bit. Boring tool, still the one you want at 3am with a dead laptop. 🖥️

### Open-source Projects (RSS)

## 8. LazyCodex Wants to Give Your Complex Codebase an Actual Memory — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/code-yeongyu/lazycodex)

**Source:** https://www.opensourceprojects.dev/post/b9256954-7918-4d36-a584-bcfd5016dac9
**GitHub:** https://github.com/code-yeongyu/lazycodex
**Karakeep doc:** `orc8p7xspdmh92tdgguymb49`

Codex opens on a repo that's been alive for nine years and behaves like it just landed from another planet. No memory of your architecture, no plan, no proof anything it wrote compiles. LazyCodex is OmO — Sisyphus Labs' oh-my-openagent harness — repackaged as a Codex distribution. MIT, TypeScript, roughly 3,500 stars, commits landing today.

Install is one line: `npx lazycodex-ai install`. Fully autonomous, no TUI, add `--no-tui --codex-autonomous`. There's also an experimental Codex marketplace route that adds the `omo` plugin, and Codex won't run the hooks until you approve them in the startup review. Upgrades mean re-approving those hooks every time.

What you actually get: `$init-deep` scores directories and writes hierarchical AGENTS.md files so future agents get landmarks before they edit. `$ulw-plan` writes a plan to `plans/*.md` and refuses to touch product code. `$start-work` grinds the checklist until it prints ORCHESTRATION COMPLETE. `$ulw-loop` keeps going until Oracle-verified completion, capped at 500 iterations in ultrawork mode, 100 otherwise. Six agent roles land in `~/.codex/agents/` — explorer, librarian, plan, momus, metis, codex-ultrawork-reviewer.

The multi-model routing is the part I'd defend. Quick edits ride gpt-5.4-mini, hard logic gets an xhigh reasoning model, agentic coding can hit Codex-tuned models. Quota discipline beats dumping your best model on every typo. `npx lazycodex-ai doctor` prints install health when things go sideways. Verdict: a thin distribution layer over a real harness, honest about what's still experimental.

## 9. Getting Your Lenovo Legion's Fans and Power Under Control on Linux — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/johnfanv2/lenovolegionlinux)

**Source:** https://www.opensourceprojects.dev/post/bdb3676e-5f5b-4c98-aeef-1925ab6037f9
**GitHub:** https://github.com/johnfanv2/LenovoLegionLinux
**Karakeep doc:** `o5ys6mognev50oso0h4rxluz`

Lenovo ships Vantage for Windows and nothing for Linux, so your Legion's fans do whatever the firmware feels like. LenovoLegionLinux is the community answer: a C kernel module plus tooling, GPL-2.0, 3,392 stars, still committing this morning. Not affiliated with Lenovo, said in bold, because it isn't.

The maintainers reverse-engineered and disassembled the ACPI firmware and the embedded controller's memory to get at thermal behavior. That buys a fan curve with up to 10 points, driven by CPU, GPU and IC temperatures at once, with per-level RPM, a minimum temperature the machine must fall below before fans slow down again, and separate acceleration and deceleration rates. Speeds below 1600 RPM are allowed. Presets save per mode.

The headline feature is `fan_unlock`. On a Legion Pro 7 16IRX8H running BIOS KWCN54WW it lifts the firmware fan ceiling from roughly 4,400 RPM to 7,100 RPM, discovered through `WMAA(0, 0x0D, 0x01)` and tracked in issue #429. It sits behind a model/BIOS allowlist, so don't expect it on your machine today.

Also included: quiet/balanced/performance switching from software or Fn+Q, battery conservation holding charge at 60% on AC, sensor readouts for fan speed and CPU/GPU/IC temps, and SmartFan in `extra/smartfan/` — a shell fan daemon for Legion 7 Gen 10+ that uses acpi_call without loading a full kernel module. The stated goal is a mainline kernel merge so updates stop breaking it. Until then, recompile after kernel bumps.

## 10. Reverse SSH: Use SSH for Reverse Shells, Because Why Reinvent the Wheel — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/nhas/reverse_ssh)

**Source:** https://www.opensourceprojects.dev/post/455cd023-338f-464b-a684-b42f45fb9479
**GitHub:** https://github.com/NHAS/reverse_ssh
**Karakeep doc:** `nnrnrv0henrodw8ol7mh5hib`

Reverse shells are usually netcat listeners, a pile of half-remembered syntax, and no way to tell which session is which. reverse_ssh puts an SSH server in the middle and has target machines dial back to it, so everything you already know about SSH keeps working. Go, BSD-3-Clause, 1,469 stars, last push in early September.

A client on the target connects outbound, which makes NAT and egress firewalls stop mattering. You connect to the RSSH server, list the machines that checked in, then jump through it like any jump host: `ssh -J your.rssh.server:3232 dummy.machine`. Local, remote and dynamic forwarding all work, plus native SCP and SFTP for pulling files off targets.

The `link` command compiles a client binary on the server and serves it over a built-in HTTP endpoint, with flags for garble obfuscation, UPX and lzma compression, TLS/WebSocket/HTTP-polling transports for networks that sniff SSH, and `--shared-object` to produce a Windows DLL for reflective injection. `.sh`, `.py` and `.ps1` path endings hand you a script you can pipe into an interpreter.

Privileges run on an owners model — keys in the data directory see only clients they own or public ones. Webhooks POST JSON when clients connect or drop. There's a tun mode for a pseudo-VPN, with an explicit warning: connect a malicious client and it can reach back into your tunnel device, so lock forwarding down or run it inside a netns. Real Windows shells come through conpty or winpty instead of the usual broken cmd.exe. This is pentest tooling and it reads like it.

## 11. Mock APIs Without the Setup Headache — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/kong/insomnia-mockbin)

**Source:** https://www.opensourceprojects.dev/post/c444ab88-7c7c-4c22-a990-d575a58f1ccc
**GitHub:** https://github.com/Kong/insomnia-mockbin
**Karakeep doc:** `ios4twzxfxn9eolph86ia6zi`

Kong's Insomnia has a mock-server backend and it's called Mockbin. 2,055 stars, JavaScript, commits today. Read the license first: the README says the repo is source-visible, not open source. GitHub reports NOASSERTION, which is the tell.

What it does is narrow and useful. You create a bin, point a client or a webhook at it, and inspect the requests that arrive. Storage is HAR — HTTP Archive — so captured traffic stays portable to existing HAR tooling instead of being locked in a homemade format. Responses render as JSON, YAML, XML or HTML.

Two details show real field use. It reads `X-Forwarded-*` headers to resolve client IPs, so it reports the actual caller when it sits behind a reverse proxy or load balancer. Method override works through either `X-HTTP-Method-Override` or a `_method` query parameter, which matters when your webhook provider or some crusty embedded client can only speak GET and POST.

Redis backs the bins. The server starts without it, but you won't be able to set or retrieve anything. Node and docker compose both work. Kong ships cosign-signed images on ghcr for cloud-hosted and self-hosted mocks, plus SBOMs and build provenance if that's an audit requirement.

Verdict: a clean little request inspector, maintained by the people who run Kong Gateway. Just don't call it open source. The license gates you, and for something you'd point real webhook traffic at, that distinction has teeth.

## 12. Stop Writing Compose Files by Hand: Let Composerize Do It for You — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/composerize/composerize)

**Source:** https://www.opensourceprojects.dev/post/9ff1fca4-b66a-40ef-93e5-42998a4b3d3a
**GitHub:** https://github.com/composerize/composerize
**Karakeep doc:** `gkk0tbu96b6bwx50ha3zrxem`

Copying a `docker run` line into a compose file by hand is how you end up with mangled volume syntax and a two-hour session debugging YAML indentation. Composerize does the translation: paste a run command, get a `compose.yaml`. MIT, JavaScript, 3,766 stars, though the last push was mid-May, so it's maintained-and-quiet rather than busy.

Three surfaces. composerize.com in the browser, `npm install composerize -g` for `composerize docker run -p 80:80 -v /var/run/docker.sock:/tmp/docker.sock:ro --restart always nginx`, and a Node library call — `const composerize = require('composerize')`.

The library is where the useful bits sit. Pass an existing compose config as a second argument and it merges your new service into it instead of emitting a standalone file. That's the whole game, because nobody starts from an empty directory. A third parameter picks the target format — `v2x`, `v3x` or `latest` for the Compose Specification. A fourth sets indentation, which sounds trivial until you're diffing generated output in review.

Two siblings share the family name. Decomposerize goes the other direction, compose back to `docker run`. Composeverter converts between compose file format versions. A community image credited to Oaklight bundles the composerize, decomposerize and composeverter websites together if you'd rather self-host than visit a website.

Verdict: small, boring, does one thing, and the merge path saves real edits. The May commit date is the only reason I'd read the issue tracker before wiring it into CI.

## 13. FreshRSS: Your Own RSS Aggregator, Running Quietly on a Raspberry Pi — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/freshrss/freshrss)

**Source:** https://www.opensourceprojects.dev/post/1b5c1703-28ad-42d2-adb7-2531e9db773c
**GitHub:** https://github.com/FreshRSS/FreshRSS
**Karakeep doc:** `fs66wfv04mm2aw02inqk58dr`

Every few years a feed reader you liked shuts down and takes your subscription list with it. FreshRSS is the obvious answer — self-host it and the data stays yours. PHP, AGPL-3.0, 16,088 stars, still committing today, and it runs on a Raspberry Pi 1.

Not a figure of speech. The README reports sub-second response times on the original Pi with 150 feeds and 22,000 articles. Requirements are PHP 8.1+, a light Linux or Windows box, Apache 2.4+/nginx/lighttpd, and one of PostgreSQL 10+, MariaDB 10.6+, MySQL 8.0+ or SQLite.

Feature depth is why it keeps winning. Multi-user with an anonymous reading mode, custom tags, an API for mobile clients, a CLI, WebSub so Friendica, WordPress, Blogger and Medium push updates instead of waiting on the next poll, XPath-based scraping for sites with no feed at all, JSON document support, resharing through HTML/RSS/OPML, and login via web form, HTTP auth or OpenID Connect.

Two operational gotchas the docs are blunt about. Expose only the `./p/` folder to the web — `./data/` holds every user's personal data. And pick your branch deliberately: `edge` gets fixes first, while `latest` is more stable but accumulates known bugs because security fixes aren't backported to older versions.

Verdict: 16k stars and a fifteen-year-old codebase is the endorsement. If you're tired of trusting someone else's reader, this is the boring correct choice.

## 14. FutureOS: One AI Agent That Follows You Across Every Screen You Own — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/futuregene/future-os)

**Source:** https://www.opensourceprojects.dev/post/cd966fa5-64a2-40ce-8438-29955aff99d2
**GitHub:** https://github.com/futuregene/future-os
**Karakeep doc:** `bjlszmm05tohn8n2syevbxtl`

One agent backend, every surface you own. future-os runs a Rust core that exposes a gRPC interface, and the terminal UI, desktop app, Android and iOS apps, CLI and IM bots are all thin clients against it. Same sessions, same memory, same skills, wherever you happen to be. MIT, Rust, 80 stars, commits today. Early.

The catalogue claims 3,800+ models across 140+ providers, with custom providers via `models.json`. Model config lives once. Skills install into `~/.future/agent/skills/`, with 15+ built in — image generation, PDF and Word parsing, web search, browser control, slides, software install.

Real engineering shows in two places. Approvals and sandboxing are configurable per tool class: `off`, `manual` or `sandbox`, backed by macOS Seatbelt, Linux Bubblewrap and Windows restricted-token write protection. The desktop defaults to Unrestricted and the README tells you to switch to Manual or Sandboxed before touching untrusted content. That honesty is rarer than the feature. Second, the loop control plane: durable goals, event-sourced state, verification gates and lease liveness for runs past 24 hours. Kick off research at night, read results from your phone at breakfast.

Sessions fork and clone like a git repo, with `/fork`, `/clone` and `/tree` over JSONL history. Installers come from `dl.future-os.cn`.

Verdict: ambitious, 80 stars, and the sandbox tiers are the only part I'd trust yet. Watch it.

## 15. GraphRAG That Won't Blow Your API Budget — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/circlemind-ai/fast-graphrag)

**Source:** https://www.opensourceprojects.dev/post/1a5785c7-2ba9-47ff-a530-8b7ffbf873c6
**GitHub:** https://github.com/circlemind-ai/fast-graphrag
**Karakeep doc:** `wuvjl5v5qt2v0pmwyyw03ohh`

GraphRAG's problem was never the idea. It was the invoice. Fast GraphRAG attacks the cost directly, and the README puts a number on it: processing *The Wizard of Oz* costs $0.08 against $0.48 for graphrag, six times cheaper, with the gap widening as data volume and insertion count grow. MIT, Python, 3,890 stars.

Instead of embedding chunks and doing vector similarity, it builds a graph of entities and relationships, then explores it. Exploration uses personalized PageRank, borrowed from the HippoRAG paper, to rank which nodes actually matter for a given query. That's the mechanism behind the accuracy claims, not vibes.

You configure a domain, a handful of example queries and entity types, then insert documents. The working directory persists knowledge, so reinitializing later picks up where you left off. `CONCURRENT_TASK_LIMIT` throttles LLM calls when you're pointing it at a local model. Install through pip or poetry, with poetry recommended for performance. Examples cover swapping in OpenAI-compatible models and embedders, checkpointing so you don't irreversibly corrupt a graph, and `with_references=True` for answers that cite the source material.

Here's the caveat. The last push was November 2025, nearly a year before this post ran. Almost 4,000 stars and no commits in ten months is a smell. The managed service may have eaten the maintainers' attention, and the README does pitch a hosted plan with 100 free requests a month. Check the tracker before betting a pipeline on it.

## 16. taskctl: A Concurrent Task Runner That Treats Your Build Pipeline Like a Graph — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/taskctl/taskctl)

**Source:** https://www.opensourceprojects.dev/post/156f54f5-4e65-4216-b06c-e471fb9a7cf6
**GitHub:** https://github.com/taskctl/taskctl
**Karakeep doc:** `gl9x2uh7kjt1ygqpz18uyj4m`

GNU Make is everywhere and has been since 1976, which is why waiting on it while half your targets could run in parallel feels inevitable. taskctl is a concurrent task runner built around that complaint. Go, GPL-3.0, 326 stars, last push in July.

You describe tasks and pipelines in YAML, JSON or TOML, with local and remote imports, and it builds a DAG to decide what runs together. In the README example, `lint` and `test` execute concurrently and `build` waits on both. Dependencies, conditions, allowed failures and graph visualization are core concepts rather than flags bolted on later. A filesystem watcher handles live reload, execution contexts can wrap any command in docker, ssh or another binary, and the embedded shell interpreter removes the dependency on a system shell — which is why it's genuinely cross-platform.

The part that caught my eye is the agent surface. `taskctl --output json list` and `show` emit schema-versioned JSON describing every task, pipeline, context and watcher. `--output json` on a run switches to NDJSON event streaming — run_started, task_started, task_output, task_finished with exit codes and durations, run_finished — so an agent parses results instead of scraping terminal output. `--no-input` and `TASKCTL_NO_INPUT` kill the prompts. `taskctl skill install` writes a Claude Code SKILL.md.

The runner also embeds into Go programs. Verdict: 326 stars is a small audience for a tool this well-shaped, and the JSON surface makes it the rare Make alternative worth handing to an agent.

## 17. MatrixOne Brings Git-Style Version Control to Your Database — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/matrixorigin/matrixone)

**Source:** https://www.opensourceprojects.dev/post/d73ec836-6c5d-4a0d-9850-6b7fc53ef245
**GitHub:** https://github.com/matrixorigin/matrixone
**Karakeep doc:** `a0536zhwls57lw0d0avqdste`

MatrixOne is a MySQL-compatible, Go-written database that treats tables like a git repo. Snapshots, time-travel queries, branching, merging, instant rollback. The two things that usually kill data versioning are storage cost and operational pain, and the project's answer is zero-copy snapshots that finish in milliseconds and don't duplicate your data. Underneath sits what it calls a hyper-converged HSTAP engine: OLTP, OLAP, full-text search and vector search in one system, so no ETL shuffling between three services. macOS and Linux, Apache-2.0, roughly 1,900 stars, last push this morning. There's an arXiv paper, "Version Control System for Data with MatrixOne," describing the design. The workflow that sells it: run a risky migration in a branch, merge if it behaves, roll back to any prior state without a full restore. Existing MySQL drivers and clients should talk to it, which makes poking around cheap. Caveats: HSTAP claims come from the project itself, no independent benchmarks, and a database volunteering to own transactional, analytical, full-text and vector workloads is asking for trust it hasn't earned yet at this age. If your team already lives in MySQL and schema changes cost you sleep, the 60-second quickstart is a fair price for a look. Strong idea, young implementation.

## 18. Stop Memorizing Command-Line Flags: Let Navi Run Your Cheatsheets For You — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/denisidoro/navi)

**Source:** https://www.opensourceprojects.dev/post/12faacec-bdfd-4391-8066-0114ea23706b
**GitHub:** https://github.com/denisidoro/navi
**Karakeep doc:** `ikv9teotphi7m28t2ek46jyt`

navi takes the graveyard of half-remembered one-liners in your notes app and turns it into something you can search and actually run. It's an interactive cheatsheet browser for the terminal, written in Rust, Apache-2.0, about 17,600 stars. The interface rides on fzf or skim, so you get fuzzy search over `.cheat` files. Cheatsheets are plain text: a tag line, a description comment, the command, and a shell expression that populates each variable. The README example in full is `git checkout <branch>` with `branch: git branch | awk '{print $NF}'`. Install is `brew install navi`, and sheets land in `~/.local/share/navi/cheats/`. Three ways to use it: as a command, as a shell widget that behaves like Ctrl-R and puts the real command into your history instead of the word `navi`, and as a tmux widget that works in any CLI app, SSH included. It pulls cheatsheets from tldr and cheat.sh, imports from git repos, and a plugin even exports them from TiddlyWiki notes. Alias and shell-scripting modes exist for automation. The gain over a static snippet pile is that navi executes the thing and prompts you for arguments with suggested values, so you stop pasting broken templates at 1am. The repo was pushed September 20. If you retype the same five commands every week, this earns its install.

## 19. Miri: an Undefined Behavior detection tool for Rust — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/rust-lang/miri)

**Source:** https://www.opensourceprojects.dev/post/6949533a-24f3-4ef4-a8a3-ad6209edbe03
**GitHub:** https://github.com/rust-lang/miri
**Karakeep doc:** `xbskvq8kfxy8gohxujnxsghi`

The compiler checks your types. It doesn't check that your unsafe blocks honour the contracts they promised, and that's where Miri earns its keep. It lives in the rust-lang organisation, 6,601 stars, Apache-2.0, and it commits constantly because it tracks the compiler rather than shipping on its own schedule. 🦀

Miri runs your binary and test suite as a platform-independent interpreter over Rust's mid-level IR, then hunts for the mistakes the type system can't see. Out-of-bounds accesses and use-after-free. Reads of uninitialised data. Broken intrinsic preconditions, like reaching unreachable_unchecked or calling copy_nonoverlapping on ranges that overlap. Misaligned references, a bool that isn't 0 or 1, data races, and some weak-memory effects where atomic reads hand back stale values. It reports leaks too, when memory is still allocated at exit and unreachable from a static.

Aliasing gets two experimental checkers: Stacked Borrows, and Tree Borrows as an optional alternative. Because it interprets instead of executing natively, it can emulate other targets, which is how you confirm byte-level code works on big-endian hardware. Isolation is on by default, with entropy, environment variables and clocks replaced by deterministic fakes so a failing run reproduces. MIRIFLAGS="-Zmiri-disable-isolation" turns that off, and -Zrandomize-layout flushes out code that leans on unspecified layout.

The README is upfront that it catches only its own approximation of undefined behaviour, with no single spec to check against, and that it explores one execution per seed. It is also unusable for cryptography, because the RNG is fake. Install it as a nightly component, run cargo +nightly miri test, and it will find things your test suite never will.

---

## 20. Caddy reverse proxy for Docker containers, configured entirely through labels — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/lucaslorentz/caddy-docker-proxy)

**Source:** https://www.opensourceprojects.dev/post/c716b707-ba76-42df-9787-acfef25dab66
**GitHub:** https://github.com/lucaslorentz/caddy-docker-proxy
**Karakeep doc:** `k120iajjib1wf65931u498sz`

Every new container means editing the Caddyfile, reloading, and hoping the ten services already in there survive the edit. lucaslorentz/caddy-docker-proxy throws the file away and drives Caddy from Docker labels instead. 4,653 stars, MIT, written in Go, committed yesterday. ⚙️

The plugin scans Docker metadata for labels that mark a service as something to serve, then generates the Caddyfile in memory with site entries and proxies pointing at services by DNS name or container IP. When a Docker object changes, the config regenerates and Caddy does a graceful reload, so in-flight requests don't get dropped. Bring a container up with the right labels and it is routed. Tear it down and the entry disappears, no stale upstream pointing at nothing. Automatic HTTPS arrives because Caddy is underneath, with certificates from Let's Encrypt or ZeroSSL issued without extra configuration.

Labels map onto Caddyfile concepts, so sites, snippets, global options and tokens all have equivalents, and knowing Caddy means writing the same config in a different place rather than learning an abstraction. Go template functions like {{upstreams 80}} resolve backend addresses dynamically. Standalone, controller-plus-server, or one all-in-one container, all supported. One README detail bites though: create the network with --ipv6, or Caddy and your upstreams see Docker's gateway address instead of real client IPs.

The tradeoff is genuinely a tradeoff. Routing logic scatters across Compose files instead of living in one central config, which reads either as self-describing services or as a treasure hunt depending on taste. Traefik has done label-driven routing for years; this is the same workflow with Caddy's certificate handling. For small and medium self-hosted setups where containers come and go, that's a good trade.

---

## 21. One catalog for every agent's integrations, MCP servers included — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/usefulsoftwareco/executor)

**Source:** https://www.opensourceprojects.dev/post/3cd3a1d2-bbf2-4cc8-8dad-b3147c3d209b
**GitHub:** https://github.com/UsefulSoftwareCo/executor
**Karakeep doc:** `fylrkpl58917ljex4fcj189e`

Run Claude Code and Cursor side by side and you've pasted the same API keys into two config files, added the same MCP servers twice, and lost track of which tools each agent was allowed to touch last month. Executor is an integration layer that puts all of that in one catalog every MCP-compatible agent can read. UsefulSoftwareCo built it in TypeScript under MIT; 3,927 stars, committed in the early hours of September 21. 🔌

The mental model is three nouns. An integration is the definition of a service — an MCP server, an OpenAPI spec, a GraphQL API, or a Google Discovery endpoint. A connection is one configured and optionally authenticated instance of that integration, and there can be many. Policies decide per tool whether something is always allowed, gated behind approval, or blocked outright, with defaults derived from the spec so nobody writes rules from a blank page every time.

Agents connect over MCP and see the shared catalog, which stops a fourth agent from costing you an afternoon. First-party support covers MCP, OpenAPI, GraphQL and Google Discovery, and the plugin system opens the rest up, since anything describable with a JSON schema can become an integration. That keeps the catalog from being capped at whatever the maintainers got around to building.

Installation is npm on Node 20 or newer, then executor install to register the background service and executor web to open the UI. Executor Cloud, a desktop app, Docker and a Cloudflare deployment target all ship the same functionality in different packaging, which makes evaluation cheap before you commit to running it yourself. The docs even include a setup prompt you can paste into Claude or Cursor and let it handle the wiring. Verdict: the duplication tax is real for anyone past one agent, and this is a tidy way to stop paying it.

### LinuxLinks (RSS)

## 22. Easy-RSA – command-line PKI management utility — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/PKI-Certificate-Authority-banner1.png)

**Source:** https://www.linuxlinks.com/easy-rsa-command-line-pki-management-utility/
**GitHub:** https://github.com/OpenVPN/easy-rsa
**Karakeep doc:** `tfigxm26dni4yz86qbff9y19`

Easy-RSA wraps OpenSSL's fiddly corners in a shell script suite with one job: running your own certificate authority. Root CAs, intermediate CAs, private keys, CSRs, signed certificates, revocations and CRLs. Everything lands as plain files in a directory tree you can read, back up and argue with, which beats a vendor console you aren't allowed to inspect. It's shell-based, so it fits headless boxes and scripted workflows, and the configurable certificate properties live in variables and config files rather than a wizard. LinuxLinks lists it as GPL-2.0; the repo is OpenVPN/easy-rsa, about 4,500 stars and 1,200 forks, last commit September 19, 2026 with release notes updated for 3.2.7. The framing that matters: it's maintained by the OpenVPN project but works fully standalone, so you can issue X.509 certs for internal services, client auth or your own VPN without dragging in unrelated tooling. What you don't get is a web UI, a workflow approval engine or distributed signing. That's deliberate, and it keeps the thing small enough to understand. Teams with compliance auditors hovering will want more ceremony. For a homelab, a lab network, or a shop with a documented CA process and shell access, this is the boring correct answer. Caveat: script-based CA ceremony means your documentation is your disaster recovery.

## 23. Reko – general-purpose machine code decompiler — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2021/12/devops14.jpg)

**Source:** https://www.linuxlinks.com/reko-general-purpose-machine-code-decompiler/
**GitHub:** https://github.com/uxmal/reko
**Karakeep doc:** `motuauthzhsdz7ov74odvxz0`

Reko is a general-purpose decompiler written in C#, developed by John Källén, GPL-2.0, roughly 2,600 stars and over 11,000 commits. It takes machine code and lifts it into a higher-level representation instead of leaving you staring at assembly. The architecture splits three ways — frontend, decompilation engine, output — so you can drive it through an Avalonia GUI, from a command-line frontend on Linux, or embedded inside your own .NET application via its object model. Analysis loads executable metadata, finds execable regions and cross-references, builds control-flow graphs from jumps and calls, and translates instructions into an architecture-independent register transfer language. Recursive scanning finds reachable code; heuristic scanning chases what that misses. Instructions get grouped into basic blocks and procedures, and you can feed back types, names and comments to recover what the compiler threw away. Project files carry that supplemental knowledge between sessions, and scripting applies analysis data in bulk. Architecture coverage spans x86, x86-64, ARM, AArch64, RISC-V, m68k and more. Recent work added binary fingerprint identification, and the repo was pushed September 11, 2026. Verdict: as a Ghidra rival it's behind, but as a decompiler-shaped library you can call from .NET, there's almost nothing else standing in that spot.

## 24. IDAES – process systems engineering framework — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/Chemical-Engineering-banner.png)

**Source:** https://www.linuxlinks.com/idaes-process-systems-engineering-framework/
**GitHub:** https://github.com/IDAES/idaes-pse
**Karakeep doc:** `gnon2h00xkevuj6ctmhovf7y`

IDAES is a process systems engineering framework for modelling, simulating and optimising chemical and energy processes — reactors, heaters, heat exchangers, compressors, pumps, separators and process streams, assembled into complete flowsheets. It's built on Pyomo and equation-oriented, meaning your plant model is a system of algebraic and differential equations handed off to a numerical solver. Modularity is the design bet: unit operations, thermophysical property packages and reaction packages are separate components you recombine per process, then reuse elsewhere. Steady-state gets the headline, but dynamic models, parameter estimation, optimisation, scaling tools and diagnostics are all in there. The API is Python, so models sit next to numpy, pandas and the rest of the scientific stack instead of inside some closed simulator's scripting sandbox. Command-line tools exist alongside the interface, and Linux is supported directly. Maintained by the Institute for the Design of Advanced Energy Systems, BSD-3-Clause, 348 stars against 317 forks, 9,499 commits, last touched September 16, 2026. That fork-to-star ratio says national labs and industry are watching, not hobbyists. The target user is an engineer or researcher who wants a programmable process model rather than a point-and-click simulator. Caveat: it's a framework, so you bring the equations, the solver tuning and real understanding of the chemistry. Documentation and a citation file exist; expect to read both.

## 25. Kunai Sandbox – QEMU-based malware analysis platform — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2022/02/anti-malware-tools.png)

**Source:** https://www.linuxlinks.com/kunai-sandbox-qemu-based-malware-analysis-platform/
**GitHub:** https://github.com/kunai-project/sandbox
**Karakeep doc:** `rvxp5nsge1y6vzwawbp4oqap`

Kunai Sandbox runs malware inside QEMU virtual machines and films everything it does. Samples go into an isolated guest, x86_64 or AArch64, either under KVM acceleration or full-system emulation, and Kunai inside that guest records system-level behaviour: process activity, kernel interactions, whatever the sample touches. Network traffic dumps come out alongside the traces, so host and wire behaviour line up in one place. The workflow is config-driven. `ks-sandbox-init` prepares a VM image, `ks-gen-config` emits a config file you edit, `kunai-sandbox` runs the analysis with a timeout, sample arguments and an output directory you pick. There's an interactive shell mode for poking at a VM before committing a sample to it, and MISP export support if the intelligence needs to travel to a sharing platform. You get evidence rather than a malicious-or-clean verdict: traces and packet captures aimed at detection engineers writing rules, with the project's own dataset living at helga.circl.lu. GPL-3.0, Python, authored by qjerome and funded through the NGSOTI project, 30 stars, last pushed July 21, 2026. Caveats: a tiny community, you supply and patch the QEMU images yourself, and the whole thing has a research-platform attitude rather than product polish. If you build detections for a living and want raw telemetry instead of a score, it's a reasonable weekend.

## 26. FreeOTP+ – feature-rich two-factor authenticator for Android — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/Authentication-Tool.png)

**Source:** https://www.linuxlinks.com/freeotp-feature-rich-two-factor-authenticator-android/
**GitHub:** https://github.com/helloworld1/FreeOTPPlus
**Karakeep doc:** `ptz8yk7vumcidet0wpnn5m3n`

FreeOTP+ is a 2FA app for Android, forked from FreeOTP and largely rewritten in Kotlin with modern Jetpack libraries. It does HOTP and TOTP codes, token import by QR scan, search across your accounts, categories with filtering, and an optional biometric or PIN gate before the app opens. The interface is Material Design 3 with dark theme support, and much of the original code was replaced with newer Android components. Import and export run through Google Drive or any Android document provider, which matters the day your phone meets a puddle. Heuristic-based offline icons cover more than 250 sites so you can tell accounts apart without network calls, and detailed token views expose underlying settings for interop with other authenticator apps. Android 5.0 and up. Apache-2.0, 747 stars, 89 forks, 504 commits, latest fix landed August 24, 2026 for compatibility with certain Android 6.0 devices; version 3.4 was cut back in May. Translations run through Crowdin if you want to help. Watch the JSON import rules when restoring by hand: `issuerExt` and `label` are both required or the entry is silently dropped, `secret` must be a list of unsigned char integers, and anything missing from `tokenOrder` is ignored without warning. Verdict: the pragmatic pick over Aegis if you prefer the simpler model, though you should verify your export works before you actually need it.

## 27. Flaca – losslessly compress GIF, JPEG and PNG images — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2023/10/image-compression-2914476.jpg)

**Source:** https://www.linuxlinks.com/flaca-losslessly-compress-gif-jpeg-png-images/
**GitHub:** https://github.com/Blobfolio/flaca
**Karakeep doc:** `xsjliv7xki28b9xurqvkw2dt`

Flaca squeezes GIF, JPEG and PNG files without changing what anyone sees, aimed at production web assets. Rust, WTFPL, x86-64 Linux, by Blobfolio LLC. The savings come from two places: metadata removal and pixel/block-layout optimisation. Stock photography is routinely bloated 50% or more by embedded keywords and descriptions browsers never read, and stripping that at scale cuts hosting bills and page load times. Under the hood it uses MozJPEG's `jpegtran` for JPEG and Oxipng for PNG, plus zopfli iterations for PNG where the default sits at 60 for small images and 20 for large ones — crank `-z 500` if you'll trade minutes for bytes, drop to `-z 1` to get speed back. It parallelises across logical cores with `-j` to cap workers, walks directories recursively, reads paths from a file or STDIN via `-l`, and lets you skip formats entirely, skip images above a pixel count, preserve access and modification times, and ignore symlinks. Progress bar included. Install from Debian/Ubuntu x86-64-v3 packages, AUR's `flaca-bin`, or `cargo install`; building from source wants clang, make, nasm and the libjpeg/libpng headers first. The README's own warning is the best part: don't feed it your whole personal media library, because it will cheerfully eat metadata you cared about. Nine stars, 1,335 commits, 3.9.2 shipped August 20, 2026. Narrow scope, honest docs.

## 28. Anatase – immutable Fedora-based distribution — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/04/Linux-Distributions.png)

**Source:** https://www.linuxlinks.com/anatase-immutable-fedora-based-distribution-development-gaming/
**Karakeep doc:** `uw37iqff9f7rirfwgqbztxw4`

Another immutable distro, and this one is Fedora underneath, glued together with bootc. 🐧 The pitch is a single x86_64 image that boots on desktops, laptops, HTPCs and handhelds instead of a different baked image per device and GPU combination. Updates arrive as whole system images across stable, rolling and testing channels, with background updates, so nobody has to think about package-level drift.

The desktop is KDE Plasma, with Plasma Mobile for touch hardware. Gaming gets its own Gamemode built on gamescope, aimed at handhelds and living-room boxes, with variable refresh rate, HDR, frame-rate limits and frame generation. Handheld plumbing is taken seriously: controller configuration, gyro, back buttons, RGB, fan curves and TDP management. AMD, Intel and recent NVIDIA cards are supported, while GTX 1000 series and older are explicitly excluded.

Spaces are the interesting part. Each one is an isolated environment running packages from Arch, Fedora, Ubuntu or Kali next to the immutable host, with graphical apps integrating into the desktop and permissions deciding which directories and devices get exposed. You can reach the AUR or apt without mutating the base system. Secure Boot works through a Machine Owner Key, SELinux handles mandatory access control, LUKS encryption is supported, and Flatpak is there for apps. One image, one updater, no per-device fork to maintain. Verdict: a sane take on immutable Fedora for people who want their games and their pet packages on the same machine. 🎮

---

## 29. 28 Essential Free and Open Source LaTeX Tools – typeset beautifully — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2021/07/typesetting-tools.jpg)

**Source:** https://www.linuxlinks.com/latextools/
**Karakeep doc:** `hixlpuzxaprolr57c9ext6bu`

LaTeX has been the typesetting default for scientists since Leslie Lamport bolted a document-preparation layer onto Knuth's TeX in the early 1980s, and LinuxLinks has rounded up 28 free tools that orbit it. The case for the format hasn't moved: you describe structure, the engine sweats page breaks, fonts and formulae, and academic journals take the output as-is. The recommended distribution is still TeX Live, maintained by the TeX Users Group as the successor to teTeX.

The list splits into editors and front-ends, bibliography machinery, engines and build tooling. Editors run from heavyweight IDEs like TeXstudio and TeXmaker, through KDE's Kile, Emacs AUCTeX, VimTeX for people who live in a terminal, GNOME's Enter TeX, minimal GTK affairs like Gummi and Setzer, up to TeXmacs doing structured WYSIWYG with LaTeX export and LyX hiding the markup behind a graphical front-end. Bibliography work is covered by JabRef, KBibTeX, Pybliographer, BibLaTeX and its Biber backend. Engines and plumbing include Tectonic, a self-contained modernised TeX engine, plus Latexmk for automated reruns and latexindent.pl and Rust-based tex-fmt for formatting source. Odd corners round it out: TexLab's Language Server Protocol implementation, TexMaths injecting equations into LibreOffice, LaTeXDraw emitting PSTricks code, KLatexFormula making images from formulas, and two symbol helpers, Hieroglyphic and Hand TeX, that find commands by sketch or handwriting. Everything here is free software and rated in the usual LinuxLinks chart. If you write papers, theses or anything with maths in it, this is the shopping list.

- **[LyX](https://www.lyx.org/)** — What-you-see-is-what-you-mean document processor — a graphical front-end to LaTeX.
- **[KBibTeX](https://github.com/KDE/kbibtex)** — KDE bibliography editor and BibTeX shell, integrates with Kile.
- **[TeXstudio](https://github.com/texstudio-org/texstudio)** — Full-featured cross-platform LaTeX editor with a built-in PDF viewer and reference browser.
- **[VimTeX](https://github.com/lervag/vimtex)** — Modern Vim/Neovim filetype and syntax plugin for editing LaTeX.
- **[TeXmacs](https://github.com/texmacs/texmacs)** — Free scientific text editor — structured WYSIWYG editor with LaTeX export.
- **[JabRef](https://github.com/JabRef/jabref)** — Open-source BibTeX/BibLaTeX reference manager, Java, JabRef-native format.
- **[Biber](https://github.com/plk/biber)** — Sophisticated bibliography processing backend for biblatex.
- **[TeXmaker](https://www.xm1math.net/texmaker/)** — Cross-platform LaTeX IDE with one-click compile, Unicode support and spell check.
- **[Tectonic](https://github.com/tectonic-typesetting/tectonic)** — Modernised, self-contained TeX/LaTeX engine powered by XeTeX and TeX Live.
- **[TeXworks](https://github.com/TeXworks/texworks)** — Simple Qt-based TeX front-end with an integrated PDF previewer.
- **[Atom-LaTeX](https://github.com/ashthespy/Atom-LaTeX)** — All-in-one LaTeX typesetting utilities for the Atom editor.
- **[SiSU](https://www.sisudoc.org/)** — Structured document preparation and publishing system with its own markup.
- **[Kile](https://github.com/KDE/kile)** — KDE LaTeX/TeX editor with a powerful project manager and multi-file support.
- **[BibLaTeX](https://github.com/plk/biblatex)** — Modern bibliography package for LaTeX — the successor to classic BibTeX.
- **[Enter TeX](https://flathub.org/apps/org.gnome.gnome-latex)** — TeX/LaTeX text editor (formerly LaTeXila, then GNOME LaTeX).
- **[AUCTeX](https://github.com/emacsmirror/auctex)** — Emacs package for authoring and previewing TeX/LaTeX documents.
- **[TexMaths](http://roland65.free.fr/texmaths/)** — LibreOffice extension that inserts LaTeX equations as SVG or PNG images.
- **[Setzer](https://github.com/cvfosammmm/Setzer)** — Simple yet full-featured LaTeX editor for the GNOME desktop.
- **[Gummi](https://github.com/alexandervdm/gummi)** — Lightweight minimal LaTeX editor for GTK with live PDF preview.
- **[TexLab](https://github.com/latex-lsp/texlab)** — Cross-platform Language Server Protocol implementation for LaTeX.
- **[Pybliographer](https://directory.fsf.org/wiki/Pybliographer)** — Python bibliography manager for searching and editing bibliographic databases.
- **[LaTeXDraw](https://github.com/latexdraw/latexdraw)** — Graphical drawing editor that generates PSTricks/LaTeX code.
- **[latexindent.pl](https://github.com/cmhughes/latexindent.pl)** — Highly configurable LaTeX source formatter (indentation, alignment, wrapping).
- **[tex-fmt](https://github.com/WGUNDERWOOD/tex-fmt)** — Fast Rust-based CLI that formats LaTeX, BibTeX, class and style files.
- **[Latexmk](https://github.com/debian-tex/latexmk)** — Fully automated LaTeX build tool — reruns engines and auxiliary tools as needed.
- **[KLatexFormula](https://klatexformula.sourceforge.io/)** — Graphical application that generates images from LaTeX equations.
- **[Hieroglyphic](https://github.com/FineFindus/Hieroglyphic)** — Find LaTeX symbols by sketching them — searches 1000+ symbols.
- **[Hand TeX](https://github.com/VoxelCubes/Hand-TeX)** — Handwritten LaTeX symbol classifier — draw the symbol, get the command.

---

## 30. “Linux Supported” Is One of the Most Misleading Claims in PC Hardware — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/07/linux-3503.jpg)

**Source:** https://www.linuxlinks.com/linux-supported-vs-linux-compatible/
**Karakeep doc:** `zg4hbhvevpl6p1865ihxfej3`

A machine boots Ubuntu, lands on the desktop, and everyone calls it Linux supported. The author of this piece wants that phrase retired for the loose way it gets used. Compatibility and support are two different claims, and the gap between them is where buyers get burned. Compatible means the components have upstream kernel drivers and the thing works, often because the manufacturer did nothing at all. Supported should mean the vendor tested the product under Linux, documented the limitations, shipped firmware updates through a route Linux users can actually use, and is willing to chase Linux-only regressions.

Booting is the easy part. Suspend and resume, multiple display outputs, hardware video decoding, audio jack detection, webcams, card readers, and Bluetooth that survives a reboot are where machines quietly fall over. Modern silicon adds vendor performance modes, fan controls, firmware interfaces and NPU software stacks that may exist only as Windows binaries. Canonical's Ubuntu certification programme gets held up as the benchmark: hundreds of compatibility tests across audio, networking, Bluetooth, USB, firmware and power management, which is a lot more than a boot test. The author discloses he has worked with Canonical previously.

Firmware is the killer detail. fwupd and the Linux Vendor Firmware Service give vendors a proper channel to reach Linux users, and plenty of otherwise compatible hardware still wants a Windows executable to flash a BIOS or a device. That is compatibility, and support is the part the vendor has to do. Reviews that stop at lspci, lsusb and a desktop screenshot aren't evidence of anything either. The ask is boring and fair: name the distributions and kernel versions that were tested, list the known gaps, say whether suspend works, and stop implying full support from a machine that merely reached a login prompt.

---

## 31. Patinae – programmable molecular visualization toolkit — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/Molecular-Editors-banner.png)

**Source:** https://www.linuxlinks.com/patinae-programmable-molecular-visualization-toolkit/
**GitHub:** https://github.com/zmactep/patinae
**Karakeep doc:** `zpzpxy8d3gzh60xysdaondwn`

Patinae started life as PyMOL-RS and has grown into an independent molecular viewer with its own renderer, command runtime, plugin host, desktop interface and session format. Author Pavel Yakovlev wrote it in Rust and licenses it BSD-3-Clause; the repo sits at 204 stars and was pushed the same day this landed in the feed, so the project is alive rather than parked. 🧬

Rendering is GPU-first through WebGPU on wgpu, and that's what lets one core serve a native desktop app, Python and Jupyter interfaces, and a browser-based viewer you can embed in a page. Structures come in as PDB, mmCIF, BinaryCIF, MOL2, SDF/MOL, XYZ and GRO. It also reads CCP4/MRC electron-density maps and XTC/TRR trajectories, which matters if you are looking at dynamics instead of one solved structure. Representations cover spheres, sticks, lines, cartoons, ribbons, molecular surfaces, meshes, dots and labels.

The workflow is command-driven alongside the mouse: select atoms, residues, chains, polymers, solvent and objects, take measurements, control representations and colours, script anything repetitive. Analysis tools include Kabsch superposition, CE structural alignment, crystallographic symmetry expansion, secondary-structure assignment and electron-density map contouring. A native plugin architecture lets you add commands and UI surface without forking. Verdict: PyMOL's scripting muscle without the licensing headache or the 2000s-era renderer, and the browser viewer is the piece nobody else ships this cleanly.

---

## 32. Open Scrobbler – web-based Last.fm scrobbling client — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2023/04/musical-notes-2128-03.jpg)

**Source:** https://www.linuxlinks.com/open-scrobbler-web-based-last-fm-scrobbling-client/
**GitHub:** https://github.com/elamperti/OpenWebScrobbler
**Karakeep doc:** `l6dbysg6o2zctyygsgk4gr4w`

Last.fm scrobbling is automatic right up until it isn't. Vinyl, radio, live gigs, a CD player, gear with no integration — none of that reaches your profile on its own, and this is the gap Open Scrobbler fills. It's a web client for submitting listens by hand, and it runs in a browser on Linux with no desktop client involved. Use the hosted site if you want it now, or self-host it if you don't. 🎵

Enrico Lamperti wrote it in TypeScript under GPL-2.0, and the repo is at 463 stars with the last commit in June 2026. Authentication goes through Last.fm's own flow, so you never hand your password to the app. Manual entry takes artist, album, track and timestamp. Album search saves most of the typing, since you pick a release and tick the tracks you actually heard, with metadata lookups against MusicBrainz and Discogs filling in the blanks.

The reconstruction tools are the part with real thought behind them. You can pull a track list from another Last.fm user's history and scrobble it while keeping the original date and time. Setlist.fm integration finds a concert setlist so you can log the gig you were at. Custom timestamps let you backdate a whole album from a chosen end time so the listens fall in the right order instead of landing in one clump. Multilingual interface, time-format preferences, and it deploys on your own infrastructure if the hosted instance disappears. Verdict: a one-trick tool, but the trick is genuinely useful if your music arrives from anywhere other than a streaming client.

---

## 33. FreeOTP – open source two-factor authenticator — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/Authentication-Tool.png)

**Source:** https://www.linuxlinks.com/freeotp-open-source-two-factor-authenticator/
**GitHub:** https://github.com/freeotp/freeotp-android
**Karakeep doc:** `uqc0ldfe2m1x0nrfd2nbmyod`

FreeOTP came out of Red Hat and does one job: generate one-time passwords for standard protocols. HOTP per RFC 4226, TOTP per RFC 6238. No proprietary server-side component anywhere, so any service speaking those standards will accept it.

Tokens get added by QR scan or manual entry. The per-token configuration is more generous than most competitors: hashing algorithm (SHA-1, SHA-224, SHA-256, SHA-384, SHA-512), number of digits, validity period. You can also require recent device authentication before a token's shared secret is readable at all — the setting you actually want when someone grabs your phone while it's unlocked.

Backups are encrypted with a master key stored in the Android Keystore. Two routes: Android's automatic Google Account backup, or manual encrypted backups to external storage. Either way, restoring needs the master password, so write it down somewhere that isn't the phone. Smaller touches that matter in daily use: inverted QR code support, sorting tokens by most recently used.

Repo status: Java, Apache-2.0, 1,674 stars, last push August 18th, 2026, so not abandoned. Shipped on F-Droid as org.fedorahosted.freeotp and on Google Play.

The verdict is short. No vault, no account, no cross-platform sync, no desktop client. If you want categories, biometrics, dark mode and searching, FreeOTP+ is the fork to install. If you want an app that stores six tokens and never surprises you, this is fine. 🔐

## 34. Best Free and Open Source Alternatives to Google Authenticator — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2021/03/Google-Alternatives.jpg)

**Source:** https://www.linuxlinks.com/best-free-open-source-alternatives-google-authenticator/
**Karakeep doc:** `is1bm8tvjc8vze6n45vkl7wl`

Google Authenticator works. It also keeps your second factor inside an account you don't administer, with backups landing wherever Google decides and migration flows that have historically been a mess. This is the authenticator entry in LinuxLinks' long-running "alternatives to Google's products" series, and it recommends five replacements.

Aegis Authenticator is the Android pick: HOTP and TOTP, secrets sealed in an encrypted vault behind a password or biometrics, encrypted backups, imports from most other authenticators, entry grouping and custom icons. 2FAS Auth covers Android and iOS, works offline, needs no account, stores data locally, and optionally pairs with a browser extension so you approve logins from the phone instead of typing codes. Ente Auth brings end-to-end encrypted backups and sync across Android, iOS, Linux, macOS, Windows and the web, and it can run account-free for people who want the authenticator entirely offline.

FreeOTP+ is the feature-rich Android fork of FreeOTP: HOTP/TOTP, backup and restore, biometric or PIN protection, searching, categories, dark mode, better QR handling. FreeOTP itself is the quieter upstream project and stays in the list because it's still actively developed.

Who it's for: anyone whose 2FA lives on a Google account by default and who wants the secrets on hardware they own. One caveat worth stating plainly — every app here is only as recoverable as the backup you actually configured, and if you never test a restore you don't have a backup, you have a file. 🛡️

- **[Aegis Authenticator](https://github.com/beemdevelopment/Aegis)** — Secure open-source Android 2FA app with encrypted vaults and backups.
- **[2FAS Auth](https://github.com/twofas/2fas-android)** — Private two-factor authenticator with TOTP/HOTP and a browser extension.
- **[Ente Auth](https://github.com/ente/ente)** — End-to-end encrypted cross-platform TOTP/2FA app from the Ente team.
- **[FreeOTP+](https://github.com/helloworld1/FreeOTPPlus)** — Feature-rich Android authenticator — HOTP/TOTP, biometrics, categories, offline icons.
- **[FreeOTP](https://github.com/freeotp/freeotp-android)** — Red Hat's open-source Android authenticator supporting HOTP and TOTP.

## 35. Equilipy – multicomponent multiphase equilibrium software — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/Chemical-Engineering-banner.png)

**Source:** https://www.linuxlinks.com/equilipy-multicomponent-multiphase-equilibrium-software/
**GitHub:** https://github.com/ORNL/Equilipy
**Karakeep doc:** `b6gwb2ao4l9vqrv52xh6sfe3`

Equilipy is thermodynamic equilibrium software from Oak Ridge National Laboratory, built on the CALPHAD method. Hand it a thermochemical database plus temperature, pressure and composition, and it works out which phases are stable, how much of each is present, what they're made of, and the associated Gibbs energy, enthalpy, entropy and heat capacity.

The solver minimises Gibbs energy using descriptions supplied by Thermochimica, with an algorithm inspired by Eriksson (1971) and de Capitani and Brown (1987). It reads ChemSage and FactSage DAT databases as well as Thermo-Calc-style TDB files, so existing CALPHAD datasets get reused instead of rebuilt. On top of plain equilibrium runs it does Scheil-Gulliver solidification and nucleation-dependent solidification modelling, plus batches spanning many conditions.

Two front ends. The desktop GUI handles database inspection, editing, validation and export; the Python API gives direct control, and MPI helpers distribute batch work across cluster nodes. `pip install equilipy`, with `[gui]` and `[hpc]` extras. Python 3.10–3.14 on Linux, Windows and macOS, with a Fortran compiler needed only when building from source. Prebuilt installers exist for macOS arm64, Windows and Linux x86_64/arm64.

State of the project: BSD-3-Clause, Python and Fortran, 33 stars, last push July 20th, 2026, a JOSS paper (10.21105/joss.06875) and a Zenodo DOI. macOS installers aren't notarized yet, so expect the scary warning on first launch. Verdict: a real materials-science tool with a paper behind it and a small user base, which is normal for this corner of engineering. ⚗️

## 36. Python Easy Chess GUI – graphical frontend for UCI chess engines — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/06/033-chess-game.png)

**Source:** https://www.linuxlinks.com/python-easy-chess-gui-graphical-frontend-uci/
**GitHub:** https://github.com/fsmosca/Python-Easy-Chess-GUI
**Karakeep doc:** `mmnb6373f4291hmflgw2p031`

Python Easy Chess GUI is Ferdinand Mosca's frontend for playing against UCI engines, reviewing games and poking at positions. Install whatever engine you like — Stockfish or anything else speaking UCI — and then give the same setup several jobs at once.

That's the part that separates it from a toy board. One engine plays as your opponent, another sits as an adviser you can consult mid-game, and further engines handle position analysis and threat examination. Polyglot opening books are supported and the computer opponent can use them during the opening. White and Black repertoire files are kept separately, and games save to PGN automatically, with the option to have completed games analysed and annotated for you.

Under the hood: Python 3.7+, python-chess, FreeSimpleGUI and Pyperclip. It began as a demo chess-against-AI example from PySimpleGUI, which explains the modest look. Board size, colours and themes are configurable and the window resizes, so it scales up on a big monitor. Prebuilt executables exist in the releases if you don't want to touch a Python environment, and Linux users need `chmod +x` on their engine binary or nothing will start.

Repo state: Python, LGPL-3.0, 175 stars, last push July 21st, 2026, tagged chess, chess-engines, chess-gui, polyglot-book, pysimplegui, python-chess, python3. Verdict: uglier than Lucas Chess or En Croissant, and considerably easier to script around. If you want a multi-engine analysis bench without paying for chess software, this earns its disk space. ♟️

## 37. Hadron – minimal Linux distribution for cloud and edge — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/04/Linux-Distributions.png)

**Source:** https://www.linuxlinks.com/hadron-minimal-linux-distribution-cloud-edge/
**Karakeep doc:** `mlvo8e9tltn22gz9kg0d6uf6`

Hadron is built from scratch — not a respin of Debian or a stripped Fedora — as a minimal base for cloud and edge boxes. Spectro Cloud and the Kairos team maintain it, and it stays close to vanilla upstream components: musl libc, systemd, straight Linux kernels. The design goal is a boring, predictable foundation you layer your own services on top of.

Booting works both ways. Conventional Dracut and GRUB, or Trusted Boot using unified system images, which is the interesting option on hardware with a TPM and a security team. Upgrades run through the Kairos agent in A/B fashion: the new system image gets deployed while the previous one stays on disk for rollback, which is the sane way to update a device you can't physically reach.

There is no package manager, and that's deliberate. Hadron is a base system, and you bring your own software — containers, static binaries, whatever. Images can be configured with k3s or k0s if you're building Kubernetes nodes, and it doubles as the foundation for Kairos images.

Specs: x86_64 and AArch64, systemd init, no desktop, fixed release model, state listed as active, homepage hadron-linux.io.

Who it's for: people running fleets of small edge nodes who want atomic updates and don't want a distro's opinions baked in. Who it's not for: anyone who expects `apt install` to work, or a desktop. Verdict: niche and honest about it. If you're not already running Kairos or k3s at the edge, there's nothing here you need today. 🛰️

## 38. Open Riff Box – lightweight guitar effects processor — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/01/003-electric-guitar.png)

**Source:** https://www.linuxlinks.com/open-riff-box-lightweight-guitar-effects-processor/
**GitHub:** https://github.com/dlujic/open-riff-box
**Karakeep doc:** `ii1g22jdb3a1y3kb8u2mfawc`

Guitar rig in one window. Open Riff Box packs amplifier simulation, cabinet emulation and pedal-style effects into a single C++ application, and it runs either standalone off an audio interface or as a VST3 plugin inside your DAW. The signal chain is built from reorderable slots, so the compressor can sit in front of the drive and the delay can land after the reverb. Hit restore and the default path comes back.

Effects cover the usual territory: compressor, wah, noise gate, drive, distortion, delay, reverb, modulation and equalisation. Each one bypasses on its own. Three amp engines walk from clean to crunch with preamp and power-amp modelling handled separately, and cabinet simulation runs on impulse responses, custom IR files included. Oversampled nonlinear processing and circuit-modelled stages sit underneath all of it.

The small stuff is where it earns its keep. There's a tuner with pitch detection and an analogue-style VU display, plus a metronome with tap tempo, accented downbeats, adjustable tempo and several time signatures. Presets save and load, and four slots switch quickly between them. An input DC blocker and an output soft limiter keep the signal sane.

Audio runs through ALSA or JACK, PipeWire's JACK compatibility layer included. That's the part most hobby DSP projects get wrong.

The repo is small: 14 stars, GPL-3.0, C++, last push 16 August 2026. Guitarix, Rakarrack and go-dsp-guitar suddenly have company from someone writing in C++ instead of Python glue. Worth a look if you play through a Linux box, and worth a build if the tone is close but not quite there.

## 39. Chaski – modern RSS and Atom feed reader — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/latest-news-2.png)

**Source:** https://www.linuxlinks.com/chaski-modern-rss-atom-feed-reader/
**GitHub:** https://github.com/a-chacon/chaski-app
**Karakeep doc:** `c2600vslz1l5bd0avbcu5863`

Chaski is a desktop RSS and Atom reader built with Rust, Tauri and React that wants to be calm and quiet. No ads, no telemetry, offline reading, full-text search, feed discovery, notifications and configurable filters. Local accounts work standalone, and Google Reader API services — FreshRSS, Miniflux and Tiny Tiny RSS — are there for people who already run a sync server. OPML import and export makes migration painless.

LinuxLinks tested it on Ubuntu 26.04 and CachyOS. The DEB package (Chaski_0.7.0_amd64.deb) installed with apt, which resolves dependencies on its own. No native Arch package shipped upstream, and the AppImage refused to start on CachyOS until it was launched as LD_PRELOAD=/usr/lib/libwayland-client.so.0 ./Chaski_0.7.0_amd64.appimage. That failure mode is going to bite a lot of users who never read the bug tracker.

In daily use the interface is rough. The default font reads poorly on both distros, links inside articles behave badly, and the discovery page isn't usable yet. Feeds organise into accounts and folders with multi-account support.

The real complaint is content handling. Chaski ignores the summary a feed supplies and fetches the whole web page to extract the full article. Convenient for the reader, and it walks straight past the publisher's decision to syndicate a summary, quietly dropping analytics, comments and donation links out of the loop. The reviewer wants full-article fetching to be opt-in rather than default behaviour.

The developer calls the codebase early stage and admits proper test coverage is missing. 142 stars, GPL-3.0, last push 11 September 2026. NewsFlash, Liferea and RSS Guard remain more polished choices today.

## 40. 12 Best Free and Open Source Photo Metadata Editors — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2019/10/Photo-Metadata.png)

**Source:** https://www.linuxlinks.com/photometadataeditors/
**Karakeep doc:** `q9fthp2inh0y7ku9xabj7wc0`

Twelve tools for the thankless job of fixing what your camera wrote into a JPEG. LinuxLinks frames it the way it should: metadata is baked into the file, holding title, description, exposure time, ISO, focal length and copyright, plus GPS coordinates on anything GPS-enabled. Cameras without GPS can still get location tagged by hand through a map or raw coordinates, which is the main reason people bother. All of it lands in Exif, so Flickr, Lightroom and every other image tool can read it back.

The list spans the full spectrum. ExifTool is the reference implementation, a CLI plus library, and it's the engine half the other entries quietly call. Exiv2 is the C++ equivalent for people embedding metadata handling in their own code. Jhead does one thing: manipulate the Exif header in JPEGs. Then come the GUIs — Photini for straightforward editing, jExifToolGUI as a Java front-end for ExifTool, digiKam as the full KDE photo management suite with RAW support and batch processing, and Phatch for applying a stack of actions across many images at once.

Four entries are privacy tools rather than editors. Scramble, mat2, Metadata Cleaner and Kleaner exist to strip metadata, not add it, which is the correct instinct before posting photos anywhere public. Metamorphosis rounds out the inspect-and-change side, covering media and document files alongside images.

Worth knowing: mat2 and Metadata Cleaner are the two to reach for when the goal is scrubbing, and ExifTool handles everything else whether or not a GUI exists for it. Jhead and Exiv2 are the ones to script. All free, all open source, all Linux.

- **[Photini](https://github.com/jim-easterbrook/Photini)** — Easy-to-use digital photo metadata editor, written in Python with exiv2/GExiv2 behind it.
- **[ExifTool](https://github.com/exiftool/exiftool)** — The reference library and CLI for reading/writing image, audio and video metadata (Exif, IPTC, XMP).
- **[Exiv2](https://github.com/exiv2/exiv2)** — C++ library and command-line utility to manage image metadata (Exif, IPTC, XMP).
- **[digiKam](https://github.com/KDE/digikam)** — Advanced KDE photo management suite with tagging, RAW support and batch processing.
- **[jExifToolGUI](https://github.com/hvdwolf/jExifToolGUI)** — Cross-platform Java GUI front-end for ExifTool.
- **[Jhead](https://github.com/Matthias-Wandel/jhead)** — Small command-line tool to manipulate the Exif header in JPEG files.
- **[Scramble](https://github.com/tobagin/scramble)** — Privacy-focused drag-and-drop tool to inspect and strip image metadata.
- **[Phatch](https://github.com/firestrand/phatch)** — Photo batch processor — apply a stack of actions to many images at once (Python).
- **[mat2](https://github.com/jvoisin/mat2)** — Metadata Anonymisation Toolkit — strips metadata from a wide range of file formats.
- **[Metadata Cleaner](https://gitlab.com/metadatacleaner/metadatacleaner)** — GNOME desktop utility to inspect and remove hidden metadata from images, documents and archives.
- **[Kleaner](https://github.com/najepaliya/kleaner)** — Graphical image metadata cleaner for removing EXIF, IPTC, XMP and comments from batches.
- **[Metamorphosis](https://github.com/DeimosHall/Metamorphosis)** — Desktop utility for inspecting and changing embedded metadata across media and document files.

## 41. OSS Review Toolkit – automate open source compliance — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/SBOM-Tools-banner1.png)

**Source:** https://www.linuxlinks.com/oss-review-toolkit-automate-open-source-compliance/
**GitHub:** https://github.com/oss-review-toolkit/ort
**Karakeep doc:** `hzgb7v45ilbl169ntqrkg9rc`

OSS Review Toolkit is a policy automation and orchestration pipeline for open source dependencies, and calling it an SBOM generator undersells the thing badly. ORT walks a project through separate stages you can chain to taste: the Analyzer determines dependencies and their metadata, the Downloader pulls the actual source, the Scanner runs source scanners for licence and copyright detection, the Advisor queries vulnerability services, the Evaluator applies Policy as Code rules, and the Reporter writes the output.

Those policies are where the value sits. Licence rules, security rules, InnerSource rules and engineering standards all become machine-checked conditions instead of a spreadsheet someone updates quarterly. Reporter output covers CycloneDX and SPDX SBOMs, open source notices, attribution documents and archives of project plus dependency source. Metadata and licence findings can be curated and corrected when a scanner gets it wrong, which matters because scanners get it wrong often.

The Notifier pushes results out by email or JIRA, so findings land where developers already work. Run it as a library, as a CLI, or wired into CI. Kotlin throughout, Apache-2.0, written on Linux first.

The repo is the real proof: 2,085 stars, last push 19 September 2026, with topics for CRA and DORA — the EU rules that made half the industry suddenly care about SBOMs. If your build ships third-party code into a regulated product, ORT is the grown-up option. The learning curve is real, mostly in writing the policy file before you have findings to write it against.

## 42. Miasm – reverse engineering framework for binary analysis — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/12/117-security.png)

**Source:** https://www.linuxlinks.com/miasm-reverse-engineering-framework-binary-analysis/
**GitHub:** https://github.com/cea-sec/miasm
**Karakeep doc:** `p5i56l8eo6sfjkxtbb8rz135`

Miasm is a reverse engineering framework in Python that refuses to pick one stage of the job. It spans executable parsing, assembly, disassembly, intermediate representations, emulation and symbolic execution, with a common intermediate language holding it together. Instructions from different architectures get lifted into that IR, so your analysis passes stop caring whether the bytes came from x86 or a microcontroller.

Concretely: open, modify and generate PE and ELF executables, 32-bit and 64-bit, little and big endian. Assemble and disassemble x86, ARM, MIPS, SH4 and MSP430 behind a shared Machine abstraction. Build IR control-flow graphs, inspect what each intermediate expression reads and writes, then simplify expressions to automate de-obfuscation. Emulation is JIT-based, so dynamically transformed or packed code can run and be inspected — registers and virtual memory are readable and writable mid-flight, with breakpoints and custom callbacks you define. Symbolic execution runs over the IR for the parts where brute force is hopeless. Raw shellcode works as well as full executables, and the whole thing imports into your own scripts.

The maintainer is Fabrice Desclaux at CEA, so this carries academic security-lab DNA rather than startup marketing. GPL-2.0, Python, 3,965 stars, last push 19 September 2026.

Ghidra and Radare2 give you an interface. Miasm gives you a library to build a specialised pipeline on — unpacker, de-obfuscator, custom emulation harness. Higher effort, far more control, and the docs assume you already know what an IR is.

### RSS — Other

## 43. AI rozgryzło zaszyfrowane depesze, nad którymi ludzie bezskutecznie pracowali 108 lat — by NieBezpiecznik.pl

![NieBezpiecznik.pl](https://niebezpiecznik.pl/wp-content/uploads/2026/09/adfgvx-astra-g-600x338.jpg)

**Source:** https://niebezpiecznik.pl/post/ai-rozgryzlo-zaszyfrowane-depesze-nad-ktorymi-ludzie-bezskutecznie-pracowali-108-lat/
**Karakeep doc:** `r33ijieyrtb8r1681z8ajwaf`

GPT-6 Astra odczytała dwa niemieckie meldunki radiowe z 1918 roku. Siedziały na liście “50 najważniejszych nieodczytanych szyfrogramów” Klausa Schmeha, a na warsztat wziął je programista o nicku prinz. Pierwszy nadano 27 listopada 1918 i zaszyfrowano metodą ADFGVX — litery i cyfry zamieniano na pary symboli ze zbioru A, D, F, G, V, X, a potem całość mieszano transpozycją kolumnową według słowa-klucza. Odczyt wymaga odgadnięcia tabeli podstawień i klucza przestawienia. Setki takich depesz już złamano, m.in. George Lasry, ale kilkanaście wciąż się opierało.
 
Sztuczka nie polegała na łamaniu kryptografii. Klucz TRUPPENVERSCHIEBUNG (“przemieszczenie wojsk”) był jawnie znany — odnotowany na stronach 214–215 monografii J. Rivesa Childsa o niemieckich szyfrach wojskowych 1914–1918. Badacze zakładali jednak, że obowiązywał od 9 grudnia 1918, a meldunek nadano 27 listopada, więc klucz prawdopodobnie odrzucano bez testowania. Astra sprawdziła hipotezę, że radiotelegrafista użył go za wcześnie.

Treść: “EIN ENGLISCHER KREUZER EINLIEG X SEWASTOPOL X S4STEN X EIN GESCHWADER DER X ALLIIERTEN FOLGT 26STEN X” — angielski krążownik w Sewastopolu 24-tego (jedna cyfra nieczytelna) i nadciągająca 26-tego eskadra aliantów. Model sam zweryfikował wynik: dzienniki okrętowe Royal Navy potwierdzają, że HMS Canterbury wszedł do Sewastopola 24 listopada 1918, a eskadra dzień później.

Drugi meldunek, “RICHI-240”, miał w sygnaturze 240 znaków, a zawierał 220 i nie było wiadomo, co stało się z brakującymi 20. W szyfrze przestawieniowym to koszmar, bo nie wiadomo, gdzie je wstawić — zła pozycja daje śmieci. Astra testowała warianty i oceniała wyniki pod kątem wzorców typowych dla niemieckiego, aż wyszedł spójny tekst. Trzy nieczytelne cyfry ustalono, porównując treść z francuskim telegramem wywiadowczym z 11 listopada 1918 i historią serbskiego Vršac, zajętego 10 listopada.

Uczciwie: przestrzeń poszukiwań była wąska, nie znamy pełnych promptów, kosztu ani skali udziału człowieka, więc LLM pomógł odszyfrować, a nie odszyfrował sam. To nie atak na AES i nie dowód AGI — po prostu przydatne narzędzie. I przypomnienie dla paranoików: zapisujcie niezłamane wiadomości, bo po latach może się je udać złamać. Niebezpiecznik dorzuca, że czytelnicy portalu rozgryzali kartkę z Archiwum Państwowego w Lublinie, a FBI prosiło o pomoc przy notatkach Ricky'ego McCormicka — pozycja 10. tej samej listy Schmeha.
