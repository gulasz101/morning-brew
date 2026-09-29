---
date: 2026-09-28
slug: 2026-09-28-morning-brew
tags: Cloudflare, Web Security, Internet Technology, Open Source Software, Programming, Web Development, Operating Systems, Artificial Intelligence, Software Development, Docker, Android, Linux, Productivity, Frontend Development
---

# Morning Brew — 2026-09-28

Morning Brew for 2026-09-28 — 52 items hoarded. Six hand-bookmarked, the rest RSS autohoard. Hand first, then the RSS firehose, with the least-relevant aggregator feeds (Open-source Projects and LinuxLinks) buried at the bottom. Three videos transcribed from audio, articles summarized from their actual bodies — Cloudflare-walled 9to5linux pages rebuilt from the real title and copy behind the interstitial.

### Hand-bookmarked

## 1. I stopped using Obsidian after finding this powerful open-source alternative — by XDA

![XDA](https://static0.xdaimages.com/wordpress/wp-content/uploads/wm/2026/09/use-affine-instead-of-obsidian.jpg?w=1600&h=900&fit=crop)

**Source:** https://www.xda-developers.com/replaced-obsidian-setup-with-all-in-one-open-source-workspace/
**Karakeep doc:** `j02deubgtskx1ip6p5en53qo`

The author finally ditched Obsidian for AFFiNE, the open-source PKM tool, and the reasons are concrete rather than vibes. Obsidian's Bases feature is fine until you want real databases — AFFiNE ships table, calendar, and Kanban views that all sit on the same underlying data and properties, no third-party plugins required. Want to track publication, deadline, priority, and status in one place? AFFiNE does it natively where Obsidian makes you bolt on a Kanban plugin. The whiteboard is the bigger win. AFFiNE's Edgeless mode is a proper infinite canvas with mind-mapping, and it beats Obsidian Canvas on flexibility. Out of the box you also get calendar views and templates, which in Obsidian means another plugin hunt. The clincher for the self-hosting crowd: AFFiNE deploys on Docker, so your notes live on hardware you own instead of a cloud account. The author frames it as replacing not just Obsidian but also the separate project-tracker and whiteboard apps they were juggling. That's the real pitch — one tool swallowing three subscriptions. If you're already running homelab services and hate the plugin-tetris Obsidian demands, this is worth a serious look. The catch: AFFiNE is heavier than plain-markdown Obsidian, so migration is a real lift, not a weekend swap.

## 2. David Heinemeier Hansson: End of Hand-Written Code — by Thought Economics

![Thought Economics](https://thoughteconomics.com/wp-content/uploads/2026/09/David-Heinemeier-Hanson-DHH.jpg)

**Source:** https://thoughteconomics.com/david-heinemeier-hansson/
**Karakeep doc:** `ibmxca20weighillyacsr5sb`

DHH has done a full 180. In summer 2025 he told Lex Fridman he didn't let AI write his code and that programmers "learn with their fingers." Now his company 37signals has gone "pencils down" on hand-written code, and he says frontier models, run in collaboration, beat virtually every programmer on Earth at broad coding tasks. His reasoning is blunt: 97% of applications are CRUD over a database, and agents are "shockingly better, faster, more diligent" at exactly that. He says he couldn't have said this in February — the shift went vertical in the last three or four months, with Fable, then Astra, then Opus 5.5. His key metaphor is the Reformation: programmers were a priesthood mediating access to the computer, and "Agent Luther" has disintermediated them, same as the clergy lost its lock on scripture. He's cheerfully honest that his own hand-coding skill has lost its economic value. Who's in trouble? Adobe, Salesforce, SAP — the software whose only moat was code, not process insight. He explicitly says he'd hate to be Adobe right now, watching a million vibe-coded open-source clones of Photoshop and Premiere arrive. The exceptions: Shopify-style businesses with deep plumbing moats into payments, shipping, and tax. His Omarchy OS — Quattro, 200k downloads in 18 days, $21.7M pledged — bakes an AI agent in as your default, one that debugs crashes and files PRs. It's a bullish read, and the obvious counterpoint he waves past is whether a world where nobody can read the code is actually "control."

## 3. A battered screen didn't stop me from turning my old Samsung phone into a functional home server — by XDA

![XDA](https://static0.xdaimages.com/wordpress/wp-content/uploads/wm/2026/09/old-phone-as-server.jpeg?w=1600&h=900&fit=crop)

**Source:** https://www.xda-developers.com/turn-a-barely-working-phone-screen-into-home-server/
**Karakeep doc:** `hxuamot2p0z9q40e4ggfa6s9`

An old Samsung with a barely-responsive touchscreen is now running real workloads in this guy's homelab. The screen was so shot that touch input was unusable, so he controlled the whole thing from a PC: enabled USB debugging by plugging in a mouse over an OTG adapter, then used scrcpy to mirror and drive the phone over the wire. No separate ADB install needed — scrcpy bundles what it needs. Universal Android Debloater cleared out the junk and freed storage. Then came the hard part: getting Docker running on a non-rooted phone. Termux was a dead end, since rootless Termux basically can't do Docker. The fix was Podroid, which boots an Alpine Linux VM through QEMU with Docker set up by default. Allocating 2GB of RAM and 4 cores on a 4GB device, he deployed lightweight containers like OmniTools and BentoPDF. It's a genuinely useful reminder that an old phone is a low-power ARM box with a battery backup, not e-waste. The honest caveat is the setup is fragile: a QEMU VM on a phone is not a fast path, and the whole rig depends on the phone not dying mid-container. Still, as a free, silent, always-on mini-server, it beats buying another SBC.

## 4. Ryzen AI MAX+ 495 PCs with 192GB RAM are here, Onyx BOOX Picco launches, and postmarketOS Rebrands as Nura: Liliputing News Roundup - Liliputing — by Liliputing

![Liliputing](https://liliputing.com/wp-content/uploads/2026/09/digest-thumb-202603-Kki6TP.webp)

**Source:** https://liliputing.com/ryzen-ai-max-495-pcs-with-192gb-ram-are-here-onyx-boox-picco-launches-and-postmarketos-rebrands-as-nura-liliputing-news-roundup/
**Karakeep doc:** `t077y2qu4b7tws5j19q9ibqq`

Liliputing's roundup covers a few small-hardware stories worth a skim. The big one is the arrival of Ryzen AI Max+ 495 mini PCs with 192GB of unified memory and a 40-core Radeon 8040S — but prices are rough. The GMK EVO-X5 Pro starts around $6,500, roughly double the Ryzen AI Max+ 395 models that shipped before RAMageddon drove memory prices up. ACEMAGIC's F9A lands at similar spec and pricing in a Mac Studio-ish chassis, and the $7,399 MINISFORUM MS-S1 MAX-P495 goes mini-tower with a PCIe x16 slot inside. The 192GB is the point: it's the first tier where you can run 320B-parameter LLMs fully offline. Separately, postmarketOS — the mobile Linux distro built to extend phone life — is rebranding to Nura as it turns ten, aiming for a 10-year smartphone lifecycle and simpler branding and marketing. On the e-reader front, the Onyx BOOX Picco is up for pre-order at $100: a 3.97-inch front-lit E Ink touchscreen with Wi-Fi and Bluetooth and a deliberately simple OS, pitched against Xteink-style gadgets rather than Kindles. One more: Sixunited showed a palm-sized 0.15L mini PC with an Intel Wildcat Lake chip, up to a Core 7 360, with LPDDR5x, PCIe 4.0, HDMI, USB-C, USB-A, and Ethernet. The 192GB offline-LLM angle is the one Wojtek would actually care about, and the pricing proves it's not cheap yet.

## 5. 5 essential Linux terminal upgrades that make command-line work actually enjoyable — by How-To Geek

![How-To Geek](https://static0.howtogeekimages.com/wordpress/wp-content/uploads/wm/2026/09/file-opened-in-bat.png?w=1600&h=900&fit=crop)

**Source:** https://www.howtogeek.com/essential-linux-terminal-upgrades-command-line-work-actually-enjoyable/
**Karakeep doc:** `vuwp8ex2125uadul3hjq2urb`

Five tools, no fluff. First, Ghostty, the terminal emulator from Mitchell Hashimoto — hundreds of color themes you can live-preview with `ghostty +list-themes`, bundled Nerd Fonts so the icon glyphs in the other tools just work, and a version 1.3.0 feature that pings you when a long-running command finally finishes. Second, Starship, a shell prompt built from TOML-configured modules for Git branch, exit status, and command timing, with community presets like Pastel Powerline if you can't be arsed to hand-roll a config. Third and fourth are the color pair: eza as a modern `ls` with file icons and Git status, and bat as a `cat` with syntax highlighting and line numbers — alias both and you stop dreading a terminal dump. Fifth, the navigation combo: zoxide learns the folders you actually visit so `z src` jumps into a deep path, and fzf adds Ctrl+R history search, Ctrl+T path insertion, and Alt+C directory jumping, with `zi` pulling up a fuzzy menu of every matching folder. There's a bonus sixth — Atuin, which stores your entire command history in a local SQLite database with context like cwd and exit status, plus optional encrypted sync you can self-host. None of this is revolutionary; it's the standard Rust-tooling stack. The value is that the terminal stops feeling like a chore once the ergonomics stop fighting you. If you live in a shell, install all five in an afternoon and never look back.

## 6. I built a website with Claude Code and Stitch 2.0, and now I understand why developers are switching — by XDA

![XDA](https://static0.xdaimages.com/wordpress/wp-content/uploads/wm/2026/09/google-stitch-open-laptop-1.jpg?w=1600&h=900&fit=crop)

**Source:** https://www.xda-developers.com/built-website-claude-code-and-stitch-2-understand-why-developers-are-switching/
**Karakeep doc:** `qwjty6avku76nosans9bi25j`

The author built a fictional network-monitoring product site with a three-stage AI pipeline: Claude for planning, Google Stitch 2.0 for the UI, and Claude Code to clean up the implementation. Stitch 2.0 is the interesting part. It ditched the original I/O 2025 single-turn "prompt in, mockup out" model for an AI-native infinite canvas where screens, prompts, reference images, and pasted code persist together as context. It now runs on Gemini 3 — 3.8 Flash for Balanced mode, 3.5 Flash-Lite for Speed — swapped monthly generation caps for daily credits resetting at midnight UTC, and introduced DESIGN.md, an agent-readable file that captures the color, typography, spacing, and component patterns so a coding agent doesn't reinvent the design each session. The result looked polished on desktop, and that's exactly where the caveat lives: the export broke on mobile. Nav links vanished below 768px, the CSS styled a hamburger button but nobody wired up its script, and 246 inline style attributes had to be refactored into classes. The author's honest takeaway is the right one: each tool should do the stage it's best at, and the cleanup pass is still a human job. The "why every website looks the same now" subtitle is the real kicker — Stitch's design systems are converging on a familiar look because familiarity converts. Fine for a landing page; you still QA the damn thing before shipping.

### RSS — YouTube

## 7. DHH has gone completely off the rails... — by Fireship

![Fireship](https://i.ytimg.com/vi/OuNKBjuV7A4/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=OuNKBjuV7A4
**Karakeep doc:** `dfijwrm2n8cmygqs4w821ccq`

DHH walked into Rails World in Austin, stood in front of over a thousand Rails developers, and told them hand-writing code is over — economically nonviable, time to stop being a loser. "The black pill is for losers. Don't be a loser." Fireship's framing is perfect: the creator of Ruby on Rails used his own keynote to push AI-generated Rust, which is like the pope showing up on Easter to talk up atheism. This one's personal for Fireship, since Rails was his first framework and launched the channel. He compares watching the keynote to watching his childhood home demolished to build a data center — then asks whether DHH is a visionary or just another hype man with AI psychosis.

The meat is a skill-by-skill teardown. Keyboard mastery — Neovim, hundreds of shortcuts, the "keyboard martial arts" — is now a niche party trick when an agent makes most of your edits. Frameworks built around "developer happiness," the entire Rails philosophy, are dead: happiness is a non-factor, and what survives is whatever needs the fewest tokens and hits the best performance. DHH was a self-described Rust hater — "absolutely inhumane" for humans to write — but announced the Hey email rewrite in pure AI-generated Rust, and claims it cut CPU and memory usage by 95% on the server. His long-term bet: all languages converge into one token-optimized tongue no human ever reads.

The numbers get wild. DHH says he went from ~30,000 lines of Ruby a year to 150,000 lines a month via agents. Then he polled 1,200 devs on who still hand-writes code — about five raised their hands, under 1%. Fireship refuses to buy it, and points out the obvious hole: if coding is dead, why are there no mass layoffs and why are SV companies still paying six figures? His answer: mechanical execution was never the valuable part anyway; defining the problem and designing a secure, efficient system always mattered more, and agents just speed that up. The real "loser" sin DHH is calling out is pessimism, not Ruby. "You have an army of coding robots at your disposal and you're black-pilling." There's never been a better time to be an idiot with an idea — Fireship pivoted his failed horse-tender startup into "Donker," grinder for gay donkeys, allegedly raising a round led by Sam Altman, Peter Thiel, and Tim Cook. The Charlie Chaplin line lands it: you'll never find a rainbow if you're looking down.

The sponsor bit is CodeRabbit Triage, which ranks your team's open PRs by security risk, review effort, and blocking relationships, flags safe-to-close PRs, and claims teams merge 4x faster. It's the most-installed AI app on GitHub. Obvious counterpoint Fireship leaves mostly implied: the whole keynote is one rich guy with a product agenda telling devs their craft is dead, and the "less than 1%" poll is self-selected theater, not data. Verdict: entertaining as hell, and the pessimism-vs-agency argument is worth sitting with even if you think DHH's numbers are horseshit.

## 8. How Do Normal Linux Users Use AI? — by Brodie Robertson

![Brodie Robertson](https://i.ytimg.com/vi/5aff9qOTVgc/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=5aff9qOTVgc
**Karakeep doc:** `nh0etoxuvm66d42ptvt0735g`

Brodie ran a poll asking his audience how they use AI and got nearly eight thousand responses and about six hundred comments. The poll was limited to four options because YouTube, and the ranking came out "advanced search engine" first, "I never use it" second, with AI agents surprisingly beating vibe coding. His read on that gap: people don't want to babysit an AI, so if they're delegating anything they'd rather hand the whole task over than vibe-code it themselves.

The dominant thread in the comments was that Google search has gotten so bad the useful result now lives in the AI answer's source section, not the actual search results. He splits that into two causes — a lot of people never learned to search with keywords and operators, so they ask questions the way an LLM naturally answers better, and the results themselves are drowning in AI-generated junk sites. His takeaway is that using the AI as a source index rather than trusting its summary is a legitimate research pipeline.

Rubber-ducking came up constantly: forcing yourself to articulate a problem well enough for the LLM to understand it, which Brodie calls pair programming for people without friends. People also lean on it for niche searches a normal engine can't handle, for deciphering subpar documentation, and for boilerplate and error messages. He flags that knitting and hyper-niche domains are where it still falls flat, while the Linux kernel itself is finding value in AI-generated security reports.

The genuinely unsettling bits: someone whose Hermes agent runs their Linux server while they barely know terminal commands, a guy using it for affectionate roleplay, and job applicants and recruiters both running AI at each other until the whole cover-letter model collapses. Accessibility use cases — dyslexia spellcheck, screen readers with human-ish voices — came off as the most defensible wins. He ends on a monkey-avatar commenter declaring that if you're not dabbling in agents you're unemployed, which Brodie rejects but admits the general direction isn't changing. Worth watching for the raw spread of real-world uses, not the hype.

## 9. Google Biggest Fumble — by The PrimeTime

![The PrimeTime](https://i.ytimg.com/vi/UWn0Kh7e7ng/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/UWn0Kh7e7ng
**Karakeep doc:** `rykqj6432b6zakgx5a3hmfs4`

This is a Short, so there's not a ton of runway — the whole thing is basically one argument delivered at speed. The claim: Google invented the TPU back in 2015, which the narrator calls the "amazing AI hardware processor," and was "ahead of the curve." Then the punchline — Google "invented the T in ChatGPT," meaning the transformer, and had everything: the hardware, the research, the head start. And yet the company apparently concluded these LLMs "aren't even real" and that nobody would actually want to use them. So it sat on the advantage and let everyone else run with it. The numbers thrown out, worth taking with a fat grain of salt: DeepMind, the AI division, allegedly runs 5,600 to 7,700 employees while spending roughly $490 million every single day. Despite that spend, Google is described as having "lost" GLM 5.3 — that's Zhipu's model, mangled by the auto-caption into "GLM fifty three." Z.ai (transcribed as "ZAI") is said to have 800 to 1,100 employees and be beating Google. Moonshot AI, at around 300 employees, is beating Google too, and that model is "months old." The final dig: Grok was "the laughing stock" and is now "destroying Google" — and it didn't invent the T in ChatGPT either. The transcription is rough (Grok became "Grock"), so don't trust the specifics. But the thesis is fair: Google had a decade-plus lead on the transformer and fumbled it through institutional caution. Obvious counterpoint the video skips — spending $490M a day and still shipping a product means Google is competing on scale, not on being first to market. Still, as a two-minute roast, the core gut-punch lands.

### 9to5Linux (RSS)

## 10. Mozilla Firefox 158 Enters Public Beta Testing With Better PDF Handling — by 9to5Linux

![9to5Linux](https://9to5linux.com/favicon.ico)

**Source:** https://9to5linux.com/mozilla-firefox-158-enters-public-beta-testing-with-better-pdf-handling
**Karakeep doc:** `ye2k50yk3x92asj23g5zf1p3`

Firefox 158 is in beta, and it's the usual Mozilla diet of small-but-real fixes. The headline item is better PDF handling via SkPDF, Skia's PDF-generation backend, used both for save-as-PDF and printing on Linux and macOS. That's supposed to make output PDFs more accessible and clean up a pile of rendering bugs. The New Tab page gets a library of custom wallpapers under "Your images" instead of only remembering the last one. Smart Window form-filling gets smarter, suggesting data from your open tabs and saved autofill entries.

For web devs there's a handful of API additions: the `navigate` option on the Notification constructor and `showNotification()`, typed arithmetic in CSS `calc()` so units can actually be multiplied and divided, a `cache` value for `PerformanceResourceTiming.deliveryType`, WebAuthn conditional UI on `autocomplete="webauthn"` inputs, and a Network Monitor that catches WebSocket messages arriving right after connect. Windows also gets consistent high-contrast menus.

Nothing earth-shattering, and that's fine. Firefox 158 lands October 13th alongside the 153.5 and 115.43 ESR updates. If you're already annoyed by the Nova redesign, this beta doesn't fix that — one commenter is already patching it back to Proton with userChrome.css and AI-assisted edits. Worth grabbing if you print PDFs from Linux and want less jank, otherwise wait for the release.

## 11. Emmabuntüs Debian Edition 1.03 Adds New Accessibility Features, Debian 13.7 Base — by 9to5Linux

![9to5Linux](https://9to5linux.com/favicon.ico)

**Source:** https://9to5linux.com/emmabuntus-debian-edition-1-03-adds-new-accessibility-features-debian-13-7-base
**Karakeep doc:** `fe0pcmdvorhlt5ie8m3uozeu`

Emmabuntüs DE 6 1.03 is out, the third point release of the Debian-based distro built specifically for reconditioning old computers. It rebases onto Debian 13.7 "Trixie" and ships Xfce 4.20 and LXQt 2.1 on the same ISO, so you pick your desktop at install time. The actual focus this release is accessibility, and it's concrete, not hand-waving.

Two new utilities do the work. Easy Menu maps a dedicated key — Right Control or F12 — to a quick-access menu of the main accessibility functions, so you don't have to memorize key combos. That's aimed squarely at Orca screen reader users but helps anyone who wants simpler access. Easy Reader TTS lets you grab a document's text and image content through F7/F8 in Caja, then read it aloud via text-to-speech on top of Easy Player TTS. The devs admit Easy Reader TTS was written with AI help, which is refreshingly honest.

Smaller bits: fewer windows pop up during post-install, a `firmware-software-signed` package for better hardware support, and updated preinstalled apps. The 1.02 release before this only touched Piper integration, so this is a real step up. Download it as Core or Full 64-bit live ISOs. It's niche, but if you're the person who rebuilds donated laptops for a school or community group, this is the distro you didn't know you wanted.

## 12. qBittorrent 5.2.4 Open-Source BitTorrent Client Released With WebUI Improvements — by 9to5Linux

![9to5Linux](https://9to5linux.com/favicon.ico)

**Source:** https://9to5linux.com/qbittorrent-5-2-4-open-source-bittorrent-client-released-with-webui-improvements
**Karakeep doc:** `tujswxck8wabv3h9gbvsk0bo`

qBittorrent 5.2.4 is a maintenance release, two and a half months after 5.2.3, and it's mostly WebUI polish. You get a shared dialog for adding multiple torrents, better support for manually adding peers, and the ability to open http(s) URLs only from RSS articles and search results — so the WebUI can't be tricked into changing settings. There's also a `safe` property for setting element titles.

The bug-fix list is the interesting part if you run a WebUI. They squashed an XSS bug in the add-torrent window title, a bug where batch-selecting with Shift grabbed invisible rows, in-place corruption in `DynamicTable.loadColumnsOrder()`, and a Preferences crash specific to the Italian locale. Beyond the WebUI: links in add-torrent comments are enabled, relative UI theme paths resolve against the config folder, a crash on second-instance startup during the legal notice is fixed, and case-only renames now actually apply. They also skip processing already-added torrent sources, close file descriptors on file-manager launch, and renamed `LineEdit::textChanged` so it stops redefining `QLineEdit::textChanged`.

The AppImage now works natively on Wayland, which is the headline for anyone on a modern desktop. Meanwhile the 5.3 RC is out, promising the real feature drop later this year. Nothing sexy here, but an XSS fix in the WebUI is exactly the kind of quiet patch you should install rather than ignore. If you self-host the WebUI and expose it to a network, update.

## 13. Git 2.56 Adds New Options for Cleaning Up Branches and Resolving Conflicts — by 9to5Linux

![9to5Linux](https://9to5linux.com/favicon.ico)

**Source:** https://9to5linux.com/git-2-56-adds-new-options-for-cleaning-up-branches-and-resolving-conflicts
**Karakeep doc:** `cu1dg7rezs0rqyakiu5frfm7`

Git 2.56 dropped, three months after 2.55, and it's mostly a quality-of-life release for people who hate manual branch and conflict hygiene. The headline is a new `--resolved` flag on `git add` that stages conflict-resolved paths while leaving unrelated local changes alone, and it scans unmerged paths for leftover conflict markers and aborts if it finds any. Handy, since a stray `<<<<<<<` committed into history is a classic self-own.

`git bisect` learned `--reset-when-found`, so it auto-runs `git bisect reset` and jumps back to the culprit instead of leaving you marooned mid-bisect. `git branch` got `--delete-merged`, which nukes local branches already merged into their tracked remote-tracking branch, and `git branch -d` now actually tells you when it can't delete because the branch is pinned by an active bisect. That last one fixes a genuinely confusing silent failure.

The experimental `git history` command picked up a `drop` subcommand that removes a commit and replays its descendants onto its parent, and `git replay` got `--linearize` to flatten merge commits like `git rebase --no-rebase-merges`. Under the hood, `git cat-file --batch-command` can now fetch remote object metadata over protocol v2 without downloading whole objects, and `git rev-list --missing-only` plus `git repack --drop-filtered` help reclaim space in partial clones.

There's also typo detection for `git push origin/main`, new `git refs create/delete/update/rename` subcommands, and a fix for a segfault when `--shallow-file` runs without a value. Nothing earth-shattering, but the branch-cleanup and bisect ergonomics are the kind of thing you'll reach for weekly. Worth the update when your distro ships it.

## 14. Mozilla Firefox 157 Is Now Available for Download With Brand New Design — by 9to5Linux

![9to5Linux](https://9to5linux.com/favicon.ico)

**Source:** https://9to5linux.com/mozilla-firefox-157-is-now-available-for-download-with-brand-new-design
**Karakeep doc:** `ym6ffs57p8etlb028940qswy`

Firefox 157 has hit the download server ahead of its official September 29th unveiling, and the headline is the Nova redesign Mozilla has been teasing since Nightly back in July. The big visual refresh touches the browser chrome, sidebar, and menus, with new built-in light and dark themes you can flip on in a click. More importantly, Mozilla is bringing back Compact mode — reduced toolbar and tab spacing for small screens and split-screen layouts — alongside Standard and a Touch mode with bigger click targets. That Compact mode resurrection is going to make a lot of power users happy, since it was yanked years ago and people have been grumbling ever since. Under the hood there's real substance too. Firefox 157 now displays HDR videos encoded in 8-bit color as actual HDR in most cases, which fixes the dull-gray-video bug, and improves A/V sync when you change playback rate on HTMLMediaElement. It also adds hardware AV1 decoding for WebRTC video calls, improves the vertical-tabs sidebar in full-screen mode, and makes Tab jump straight to the address bar text field instead of stopping on the search engine button first. Amazon is dropped as a built-in search engine — a nice bit of house-cleaning — and localized address-bar suggestions roll out to more users. For devs there's `at-rule()` support for `@supports` and the `chain` value for CSS overscroll-behavior. The 153.4, 140.17, and 115.42.0 ESR releases ride along tomorrow. Verdict: a genuinely meaningful release, not just a fresh coat of paint.

## 15. Flatpak 1.18.4 Linux App Sandboxing Framework Fixes Security Issues — by 9to5Linux

![9to5Linux](https://9to5linux.com/favicon.ico)

**Source:** https://9to5linux.com/flatpak-1-18-4-linux-app-sandboxing-framework-fixes-security-issues
**Karakeep doc:** `h3a7c2jcptzfna4hoyc6syhg`

Flatpak 1.18.4 dropped a week after 1.18.3, and this one is a security release through and through — seven CVEs, which is a lot for a point update. The nasty ones are a cluster around malicious apps. CVE-2026-97024 lets a malicious app do a privileged overwrite of arbitrary files with an empty file or a symlink to `/run/host/monitor/resolv.conf`. CVE-2026-97023 is privileged deletion of arbitrary files on install. CVE-2026-97029 lets an app send signals to a process group that includes a parent outside the sandbox, which is a denial of service — kill the desktop environment from inside a sandboxed app. That one is genuinely scary because it's the kind of escape nobody's watching for. CVE-2026-97025 fixes an authentication token being visible to other users when pulling from an OCI repo that requires auth, and CVE-2026-97026 tightens permissions on temp repository dirs under `/var/tmp/flatpak-cache-*`. CVE-2026-97027 is another DoS, this time in the `.desktop` and D-Bus `.service` file filtering against the allowlist. On top of that there's hardening against symlink traversal and an xdg-dbus-proxy bump to 0.1.9, which itself fixes CVE-2026-93676 and CVE-2026-94422. The Flatpak devs' guidance is the standard "update as soon as possible," and for once it's not boilerplate — the process-group and resolv.conf bugs are real sandbox-break material. Most users should just pull it from their distro repos rather than compiling the tarball. Verdict: patch it today, not eventually.

## 16. OpenShot 4.0.1 Video Editor Released With Timeline and Zoom Improvements — by 9to5Linux

![9to5Linux](https://9to5linux.com/favicon.ico)

**Source:** https://9to5linux.com/openshot-4-0-1-video-editor-released-with-timeline-and-zoom-improvements
**Karakeep doc:** `j3gl4d4uuxh5kwj75h4dvjcm`

OpenShot 4.0.1 landed as the first maintenance release in the 4.0 series, and the headline is that they finally fixed the stuff that makes editing feel like pulling teeth. Coming a month after the 4.0 rewrite, this is mostly a polish pass — the free, Qt-based, cross-platform editor isn't chasing new features, it's sanding down the rough edges.

The Razor tool got the most love. You can now preview the exact frame at a cut, snap to timeline targets, and remove footage while auto-closing the gap, which kills the whole "cut, then manually drag the gap shut" dance. The timeline and zoom improvements are the quiet win: clip controls stay visible while you scroll, so the title, effect badges, and menu follow you instead of vanishing the moment a long clip's start scrolls offscreen. Adjusting an effect halfway through a shot no longer means a trip back to the start.

Performance got a real bump too. Median color-wheel edit time dropped significantly, preview seeking is snappier while trimming, and keyframe dragging better preserves the playhead. On the integration side, native file dialogs are back, Linux desktop portal support improved, and there's a new banner system for update notices. They also fixed macOS startup issues and added Linux webcam discovery plus better screen-recording audio sync. It ships as an AppImage you can run on basically any distro without installing. For a free editor that's been around forever, this is the kind of maintenance release that quietly makes it actually pleasant to use. 🎬

## 17. Shotcut 26.9 Video Editor Improves the VA-API HEVC Hardware Encoder on Linux — by 9to5Linux

![9to5Linux](https://9to5linux.com/favicon.ico)

**Source:** https://9to5linux.com/shotcut-26-9-video-editor-improves-the-va-api-hevc-hardware-encoder-on-linux
**Karakeep doc:** `v20hv4pjhbtk95vbvgcbssh5`

Shotcut 26.9 dropped, two months after 26.7, and the headliner is the VA-API HEVC hardware encoder getting fixed on Linux — the thing that was probably broken for a chunk of AMD and Intel users. Hardware encoding being flaky in a video editor is the kind of bug that makes you rage-quit back to software encoding, so that alone is worth the update. Beyond that, there's Automatic Ducking for audio (duck music under a voice track), plus a per-track volume control and an audio level meter right in the timeline headers. There's a new Adjustment Clip in Timeline > Generate that builds a dummy clip so its filters apply to the composite of everything below it — handy for grading an entire sequence at once. It adds FFmpeg 9.0 support and a few new script functions like `timeline.split()`. Audio quality gets a real win: they killed a conversion to 16-bit integer so the pipeline now stays in 32-bit float the whole way. UI got rounded corners and a "detect stuck startup, auto-disable external plugins" safety net, and the Leave Safe Mode toggle became an always-visible Allow External Plugins checkbox that's off by default — sensible. Clip Gain now needs Ctrl+Alt to drag so you stop accidentally nudging levels while selecting clips. They also patched a couple of buffer overflow bugs in MLT's PGM/wipe reading. AppImage and Flatpak are both up. 🎬

### Open-source Projects (RSS)

## 18. Let ChatGPT read, edit, and run your project locally - Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/totec448-spec/chat-on-steroids)

**Source:** https://www.opensourceprojects.dev/post/53f1c802-bbaa-4fb4-abd7-937a53a1a490
**Karakeep doc:** `va0ahfr3bzyfj3z9n8xsb3y7`

**Project:** [chat-on-steroids](https://github.com/totec448-spec/chat-on-steroids) — cross-platform local MCP capabilities for ChatGPT

chat-on-steroids is a TypeScript project that bolts real local capabilities onto ChatGPT via MCP — the Model Context Protocol — so the chat window can actually read, edit, and run code in your project instead of just hallucinating suggestions about it. MIT licensed, 4,073 stars, and clearly scratching an itch people have.

The pitch is the missing piece in the ChatGPT-plus-code loop. Out of the box, ChatGPT is a glorified autocomplete that can't see your files. This wires up Chrome integration, a Goal/Compact/Resume cycle, and durable multi-agent workflows, so a conversation can actually operate on your repo rather than narrating from memory. The "Chrome integration" bit is interesting — it's not just a CLI shim, it hooks the browser too, which suggests they're using the ChatGPT web UI as the control surface rather than the API.

The multi-agent angle is where it gets ambitious: durable workflows imply state that survives between sessions, which is the thing most toy agent frameworks fumble. Most of them forget everything the moment the process dies.

The obvious caveat nobody needs me to spell out: giving an LLM write+run access to your local project is a footgun with the safety off. The README can say "local" all it wants, but a model that edits files and executes commands is one bad prompt away from `rm -rf`. That said, the star count says thousands of people have decided the convenience is worth the risk. If you're going to let ChatGPT touch your code anyway, MCP is the least-hacky way to do it.

## 19. A web path brute-forcer with recursion, filters, sessions, and a Python API - Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/maurosoria/dirsearch)

**Source:** https://www.opensourceprojects.dev/post/3e3d10a8-b56d-4b58-b092-6571cb4b1d6a
**Karakeep doc:** `zk41nld858e44v7kccwgzogn`

**Project:** [dirsearch](https://github.com/maurosoria/dirsearch) — web path scanner

dirsearch is a Python web path brute-forcer that has quietly become the default tool for finding hidden directories and files on a target. 14,768 stars and still going, which tells you it's not just useful — it's the tool people reach for first when they need to map a site's attack surface.

The feature set is exactly what you want from a dirbuster. Recursion so it dives into subdirectories it finds, filters so you can tune out the noise (every scanner ever defaults to drowning you in 404s), session support so you can pause and resume a long scan, and a Python API so you can drive it programmatically instead of parsing stdout like an animal. It's fast, multithreaded, and ships with a healthy default wordlist, which is the difference between a five-minute scan and a five-hour one.

The recursion is the standout — a lot of the older tools in this space do one flat pass and call it a day, but dirsearch will actually crawl down into what it finds, which is how you catch the `/admin` living two levels deep behind a directory nobody linked to.

It's a security tool, so the usual caveat applies: point it only at boxes you own or have written permission to test. But if you do legit recon or pentesting, this is the boring, reliable, no-frills workhorse that just does the job. No license metadata on the repo, which is mildly annoying if you're packaging it, but the code is there and it works.

## 20. A curated list of Codex and ChatGPT plugins that pass a security scan — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/hashgraph-online/awesome-codex-plugins)

**Source:** https://www.opensourceprojects.dev/post/bbf13686-e33c-4a77-af5b-2dea1010fdfe
**Karakeep doc:** `y9qwhrt9r0kmkosaxd3ym2bt`

**Project:** [awesome-codex-plugins](https://github.com/hashgraph-online/awesome-codex-plugins) — a curated list of Codex/ChatGPT plugins, skills, and resources that pass a security scan

The plugin ecosystem around Codex and ChatGPT is a goddamn minefield — every third "plugin" is some sketchy wrapper that slurps your API keys or exfiltrates your prompts. This repo is the counterweight: a hand-curated list of plugins, skills, and resources that have actually passed a security scan. It brands itself the "#1 Codex Marketplace," which is a bold claim, but the 1,096 stars suggest people are at least clicking.

It's Apache-2.0 licensed and, weirdly for a "list," tagged as Python — so there's probably tooling under the hood that does the scanning rather than just a raw markdown dump. The live directory lives over at hol.org/plugins/best-codex-plugins, so the README is a storefront as much as a reference.

The value here is real: a pre-vetted list saves you from manually auditing a hundred sketchy GitHub repos before you trust any of them with your editor. The obvious caveat they don't shout about is that "passes a security scan" isn't the same as "safe to run" — a scan catches known signatures, not novel malice. Still, for anyone wiring Codex into their workflow, this is a better starting point than a blind `pip install` of whatever's trending. 🛡️

## 21. A cookies.txt exporter that never sends your data anywhere — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/kairi003/get-cookies.txt-locally)

**Source:** https://www.opensourceprojects.dev/post/aaafaf0a-0942-43b2-89e3-737f7f202549
**Karakeep doc:** `khny0e4mclsx46cmc1ww2yzd`

**Project:** [get-cookies.txt-locally](https://github.com/kairi003/get-cookies.txt-locally) — a browser extension that exports cookies.txt without ever sending data off-device

The cookies.txt format is the duct tape that keeps yt-dlp and a dozen other downloaders fed, but most exporters are browser extensions with a phone-home streak a mile long. This one's whole pitch is right there in the name: get your cookies, and never, ever ship them off your machine.

It's a JavaScript browser extension, MIT licensed, sitting at 1,202 stars. The mechanics are boring on purpose — it reads cookies locally from the browser's own storage and writes them out as a standard cookies.txt, no intermediate server, no analytics, no "anonymous usage stats" that turn out to be your full cookie jar. That's the entire feature set, and that's the point.

Why it matters: cookies.txt exports are effectively your login session in plaintext. Handing that to a third-party extension that beams it to a cloud endpoint is how you get your YouTube account hijacked. A tool that refuses to exfiltrate is worth more than one with extra features, because the feature you actually need is "doesn't leak."

The caveat nobody spells out: you're still trusting the extension's own code, since a browser extension that can read cookies can also send them anywhere it pleases. Audit the source before you install, or you've just moved the trust problem rather than solved it. 🍪

## 22. Learn to design, develop, deploy and iterate on production-grade ML applications — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/gokumohandas/made-with-ml)

**Source:** https://www.opensourceprojects.dev/post/5420dc00-a0e0-4795-a236-2fa65c13dd55
**Karakeep doc:** `kbd9i61vih27pkbc8ajegap7`

**Project:** [made-with-ml](https://github.com/gokumohandas/made-with-ml) — a full course teaching design, development, deployment, and iteration of production ML apps

At 49,643 stars, this is the heavyweight of the chunk and one of the most-starred ML resources on GitHub, period. It's not a library — it's a course, and a genuinely end-to-end one, walking you from "what the hell is an ML application" all the way to shipping something that survives contact with real users.

The repo is Jupyter Notebook under the hood, MIT licensed, and the author, Goku Mohandas, uses it as the backbone for his applied-ML teaching. The whole thesis is that most ML education stops at the notebook — you train a model, print a nice accuracy number, and call it done. This one forces you through the boring 80%: data versioning, pipelines, testing, deployment, monitoring, and the endless iteration loop that actually keeps a model useful in production.

That's the exact gap that bites teams. A model that scores 99% in a clean notebook is worthless if you can't redeploy it without a manual dance. The course is opinionated about tooling (it pushes a specific modern stack) which some people find limiting, but the structure holds up regardless of whether you adopt every recommendation.

Verdict: if you can only read one ML resource this year, this is the one that teaches you the parts everyone else skips. 📚

## 23. Open-source Airtable alternative with databases, automations, and AI agents — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/baserow/baserow)

**Source:** https://www.opensourceprojects.dev/post/0ac236c9-d605-4119-a22a-4a865e0a32f7#000000
**Karakeep doc:** `fmh59gil4mexyl4xa8hngcv1`

**Project:** [baserow](https://github.com/baserow/baserow) — a no-code, open-source Airtable alternative with databases, automations, and AI agents

Baserow is the open-source answer to the "why am I paying Airtable per seat for a glorified spreadsheet" problem. It's a Python app, 6,020 stars, self-hostable or available as a managed cloud, and it bundles databases, automations, and now AI agents into one no-code surface.

The pitch is the killer part: build a database, bolt on automations, and spin up an AI agent against it without writing code — all while keeping the data on hardware you control. The compliance angle is real too: GDPR, HIPAA, SOC 2, which is the thing that actually gets it into companies that Airtable's cloud-only model locks out.

The license field comes back as NOASSERTION from the GitHub API, which is the classic tell for a dual or copyleft setup — Baserow's been AGPL-3.0 for the self-hosted core, with a commercial layer on top. That's the honest trade: you get the source, but if you're reselling it as a service you owe them something.

The caveat worth flagging: it's a heavy app to run yourself. Postgres, Redis, a web worker, a Celery queue — it's not a `docker run` one-liner, and the AI-agent features are young enough that "agent" sometimes means "thin wrapper over an LLM call." Still, for teams that want Airtable's model without Airtable's lock-in, this is the default open-source pick. 🗄️

## 24. Open source factory that turns backlog issues into reviewed pull requests — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/superplanehq/superplane)

**Source:** https://www.opensourceprojects.dev/post/dfa7e139-a7e3-4a36-9b18-2a7547285257
**Karakeep doc:** `dd6qu09fdo5xfeue0to309ul`

**Project:** [superplane](https://github.com/superplanehq/superplane) — an open-source "factory for one-shot engineering" that turns backlog issues into reviewed PRs

Superplane is aiming at the dream every eng team mutters about in standup: take the backlog of issues nobody wants to touch, and have them come back as reviewed pull requests. It's a Go app, Apache-2.0, 7,548 stars, and it brands itself a "factory for one-shot engineering" — a phrase that's either visionary or cope, depending on how it holds up in practice.

The concept is that instead of a human developer grinding through a queue of small fixes, you feed issues in and the system produces a PR with the change already implemented and reviewed. If it works at all reliably, it collapses a chunk of the "I'll get to that someday" backlog into real merged code.

The skepticism writes itself. One-shot LLM engineering is still shaky on anything bigger than a well-specified bug, and "reviewed" PRs are only worth as much as the reviewer — if the reviewing is also automated, you're grading your own homework. Go is a sensible choice for a tool that has to orchestrate repos and CI reliably.

Verdict: the ambition is right and the repo's clearly got momentum, but treat the "reviewed" claim with the same suspicion you'd give any AI output that edits production code. 🤖

## 25. Terminator: the terminal emulator that lets you split, group, and recombine terminals — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/gnome-terminator/terminator)

**Source:** https://www.opensourceprojects.dev/post/c2fd382c-61a4-4195-91f4-9e84aebfdb31
**Karakeep doc:** `zoqvjp20xtfunpiu3ou4c61h`

**Project:** [terminator](https://github.com/gnome-terminator/terminator) — a terminal emulator that puts multiple GNOME terminals in one window, with split, group, and recombine

Terminator is the old reliable of the terminal-multiplexing world — a Python/GNOME terminal emulator that crams multiple terminals into a single window and lets you split, tile, group, and broadcast keystrokes across them. GPL-2.0, 2,668 stars, and it's been around long enough that "still works" is the actual feature.

The killer trick that tmux doesn't give you for free is the visual tiling: drag a terminal into a grid, resize panes with the mouse, and type into all of them at once when you're managing five identical servers. It's not a terminal multiplexer in the tmux sense — there's no detach-and-reattach session persistence baked in — but for someone who wants a grid of live shells on a desktop, it beats fiddling with panes in a single tmux session.

The honest caveat is that it's GNOME-bound and Python-driven, so it's heavier than a raw terminal and the development pace is glacial. It's also Linux-first; macOS and Windows are second-class citizens at best. For a GNOME desktop, though, it's the default answer to "how do I watch four logs at once without learning tmux."

Verdict: boring, dependable, and still the best grid-of-terminals you can get on Linux. 🖥️

## 26. All your coding agents and machines, side by side in one window — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/autonomous-ai/openharness)

**Source:** https://www.opensourceprojects.dev/post/f14d2ff6-f91d-4ca8-b709-c4b912a84985
**Karakeep doc:** `yy98a62b6u54lrcrqs4jl4rz`

**Project:** [openharness](https://github.com/autonomous-ai/openharness) — a command center for running every coding agent across every machine in one window

OpenHarness is one of those ideas that makes you mutter "finally." The pitch: stop juggling a dozen terminal tabs and SSH sessions for your fleet of coding agents. One window, every agent, every machine, all side by side. The scope creep is honestly aspirational — they frame it as "start with code, then follow your curiosity" into CAD, circuits, robots, games, and music. That's either a beautiful vision or a project that'll never ship half of it; time will tell which.

It's written in Dart, MIT-licensed, sitting at a hair over 1,000 stars. Dart is a slightly odd choice for a developer-tool desktop app, but it means one codebase for the GUI across macOS, Windows, and Linux without dragging in Electron's memory overhead. That alone is worth a look.

The real question is the same one every agent orchestrator faces: does "one window" actually reduce cognitive load, or does it just move the chaos behind a single pane of glass? Managing N agents is as much a UX problem as a plumbing problem, and the harness model lives or dies on how well it surfaces *what each agent is doing* rather than just *that* it's running. Verdict: watch it, don't bet the farm on it yet. 🛠️

## 27. An AI research workbench for reproducible science, local-first and model-agnostic — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/aipoch/open-science)

**Source:** https://www.opensourceprojects.dev/post/057d60a3-2b16-4dca-8f00-e5bb6dd040be
**Karakeep doc:** `xc7o9iqo3i9bkv0m6et1qgcd`

**Project:** [open-science](https://github.com/aipoch/open-science) — a local-first, model-agnostic desktop workbench for reproducible AI research

Open-Science is aiming at a real, annoying gap: doing actual *reproducible* research with LLMs and agents is still a mess of half-committed notebooks and untracked prompts. This is a local-first desktop app that treats your work as traceable artifacts, not vapor. It's model-agnostic — plug in whatever backend you want — and it ships MCP tools, connectors, and extensible skills so you can wire in Python and R execution without leaving the bench.

TypeScript, Apache-2.0, and north of 5,000 stars. That's a serious number for a research tool, which tells you people are hungry for anything that makes agent-driven science less of a trust exercise. "Traceable artifacts" is the phrase that matters here — the whole point is that when you claim a result, you can point at the exact chain of prompts, tools, and executions that produced it, and someone else can replay it.

The local-first stance is the quiet selling point. Your data stays on your box, no cloud lock-in, no vendor deciding your research habits. The tradeoff is that local-first plus MCP plus multi-language execution is a lot of surface area to keep stable, and reproducibility tooling is only as good as its defaults. If they nail the defaults, this could become the standard bench for the kind of work Wojtek actually does. 🔬

## 28. A PowerPoint alternative where the file is the whole app — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/nyblnet/bento)

**Source:** https://www.opensourceprojects.dev/post/73a1558c-0406-48e2-96e9-914f7bc4c65d
**Karakeep doc:** `t6g4e06jvdzvi8kn16fqgc1c`

**Project:** [bento](https://github.com/nyblnet/bento) — an office suite that fits in a single file

Bento's tagline is "the office suite that fits in a file," and that's exactly the kind of constraint-driven idea that either works beautifully or collapses under its own cleverness. The model: your presentation file isn't a data blob opened by an app — the file *is* the app. Open it, and you get a self-contained, interactive deck that carries its own runtime. No install, no viewer mismatch, no "this font isn't on your machine" bullshit.

TypeScript, MIT, a bit over 5,200 stars. The interest is clearly there, and it makes sense: PowerPoint is a 40-year-old relic whose file format still fights you, and web-native slides have been begging for a proper self-contained format. Bento positions itself as the data-viz-friendly alternative, which is where a "file is the app" model shines — you can embed live, reactive content instead of static screenshots.

The catch is interoperability. A file that only works because it bundles its own runtime is also a file that won't round-trip through anything else. Exporting to a format your coworkers can open is where these projects usually stumble. Still, for decks you control end to end, the idea of shipping one portable file that renders identically everywhere is genuinely compelling. Verdict: worth a hard look if you present more than you'd like to admit. 📊

## 29. SSH, RDP, Kubernetes, and an AI agent that runs its own shell commands — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/ys-ll/uniterm)

**Source:** https://www.opensourceprojects.dev/post/a3f63237-32ae-4ea9-8eb7-6bab6478644c
**Karakeep doc:** `mtpwu5l9m7eaqvs4ys557tkx`

**Project:** [uniterm](https://github.com/ys-ll/uniterm) — a lightweight all-in-one terminal with 30+ protocols and a built-in autonomous AI agent

UniTerm is a Go terminal that wants to be the last one you install. SSH, RDP, SFTP, databases, Kubernetes, and a couple dozen more protocols in a single lightweight client, plus a built-in autonomous AI agent that plans and runs multi-turn shell commands. The pitch is clear: one binary, no more juggling five different tools for five different remote targets.

Go, Apache-2.0, and a modest 555 stars. That star count is the tell — the "30+ protocols" claim is ambitious, and ambitious protocol clients live or die on the boring edge cases, not the happy path. SSH alone is a rabbit hole of key formats, agent forwarding, and jump hosts. Doing that *plus* RDP *plus* kube *plus* databases is a lot of surface area for what's clearly an early project.

The AI agent is the part worth side-eyeing. "Autonomous agent that runs its own shell commands" is exactly the kind of feature that sounds great in a README and terrifying in production. Letting an LLM plan and execute multi-turn commands on machines you SSH into is how you end up with a wiped prod box at 2am. The safety rails aren't obvious. Verdict: interesting direction, but I'd want to see the guardrails before I let it anywhere near a real server. ⚠️

## 30. A minimal TanStack Start starter with Drizzle, Better Auth, and Nitro — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/mugnavo/cove)

**Source:** https://www.opensourceprojects.dev/post/3baab5b4-b022-4d75-bba6-a4cd644ac4ee
**Karakeep doc:** `bfhgj8231iu844eu1ovo50l6`

**Project:** [cove](https://github.com/mugnavo/cove) — the Cove Stack, a minimal TanStack Start template with Vite+, Better Auth, Drizzle ORM, and shadcn/ui

Cove is a starter template, not a framework, and that's honestly refreshing. It wires together the current "boring but good" fullstack stack: TanStack Start for the framework, Vite+ for the build, Better Auth for auth, Drizzle ORM for the database, and shadcn/ui for components. No magic, no batteries you didn't ask for — just the pieces a competent TypeScript dev would've picked anyway, glued together so you don't spend a week on setup.

TypeScript, and notably it's **Unlicense** — which means "do whatever the hell you want, I disclaim everything." 1,300 stars, which for a starter is a healthy vote of confidence. The "minimal" in the title is doing real work: the whole point is that you can actually *read* the thing in an afternoon, understand every line, and not inherit someone else's cursed abstraction pyramid.

The tradeoff with any starter is staleness. TanStack Start moves, Drizzle moves, Better Auth moves, and a template that isn't aggressively maintained will drift from all of them within months. For a greenfield side project though, starting from Cove beats starting from scratch. If you're about to scaffold something and the alternative is yet another bloated monorepo template, this is the sane default. 🌊

### LinuxLinks (RSS)

## 31. LettersFall 110% - educational falling-letter word puzzle — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2023/10/Game-Tools.jpg)

**Source:** https://www.linuxlinks.com/lettersfall-educational-falling-letter-word-puzzle/
**Karakeep doc:** `vlzi0rqgb9whu3jh9hjpkhu2`

**Project:** [LettersFall 110%](https://github.com/savantsavior/lettersfall) — an educational falling-letter word puzzle built on Godot

LettersFall mashes two genres together: the time pressure of falling-block puzzles and the spelling grind of Scrabble. Letters drop into the play area and you assemble them into correctly-spelled words before the board clogs up. The emphasis is American English, backed by a dictionary of more than 450,000 words, which is genuinely a lot of vocabulary to chew through.

It's got multiple game modes, adjustable difficulty for younger versus more experienced players, saved high-score tables per mode, and mouse controls meant to be easy to pick up. Graphics, sound effects, and a music soundtrack round it out. Built in GDScript on the Godot engine, MIT licensed, by developer TeamJeZxLee.

The pitch is simple: make spelling practice feel like an arcade game instead of homework. It's free and open source, so there's no catch. I'll be honest — this is a kids' game, not a dev tool, and I'm not the target audience. But if you've got a kid learning to spell, or you want a brainless-but-not-quite word game for yourself, it's a solid little time sink that doesn't phone home or serve ads. That alone puts it ahead of half the crap in app stores.

## 32. HexPatch - binary patcher and editor with TUI — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/09/hex-editor.jpg)

**Source:** https://www.linuxlinks.com/hexpatch-binary-patcher-editor-tui/
**Karakeep doc:** `xdm3k3qylche4slw6y6xn0z6`

**Project:** [HexPatch](https://github.com/Etto48/HexPatch) — an architecture-aware Rust TUI binary patcher and editor

HexPatch isn't your granddad's hex dump viewer. It's a keyboard-driven terminal editor that actually understands the binaries you're poking at, which makes it a proper reverse-engineering and vulnerability-research tool rather than a glorified byte browser. It disassembles machine instructions inline while you edit, and can assemble replacement instructions so you can write patches without leaving the workflow. That's the differentiator — most hex editors treat binaries as opaque streams of bytes; this one knows what the bytes mean.

Format support is broad: COFF, ELF, Mach-O, PE, and XCOFF. Architectures covered include x86, x86-64, ARM, AArch64, MIPS, PowerPC, RISC-V, S390x, SPARC64, and even eBPF, with architecture-aware instruction highlighting. You can work in virtual addresses or raw file positions, edit files on remote boxes over SSH and SFTP with public-key auth, do text and symbol searches, and extend it with Lua plugins. Configurable settings and multiple interface translations round it out.

Written in Rust, licensed AGPL-3.0, by developer Ettore Ricci. The AGPL is worth noting if you're thinking about embedding it anywhere commercial. For anyone doing serious binary work — crackmes, CTF reversing, patch analysis — this is a genuinely capable tool that beats `hexedit` and friends on architecture awareness. If you just need to eyeball a file's bytes, stick with `hexyl`; HexPatch earns its keep when you're actually modifying code.

## 33. Lunar Linux - source-based Linux distribution — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/04/Linux-Distributions.png)

**Source:** https://www.linuxlinks.com/lunar-linux-source-based-linux-distribution/
**Karakeep doc:** `p7ev03w0s9zmgvsknlqwe3dv`

**Project:** [Lunar Linux](http://www.lunar-linux.org/) — a source-based rolling Linux distribution that compiles software locally

Lunar Linux is a source-based rolling distro in the same spirit as Gentoo: it compiles your software locally so packages get tailored to your exact hardware and build options. The pitch is flexibility without making installation an exercise in masochism. Packages are called "modules" and their build recipes live in the Moonbase repository, which is about as on-brand a name as a source distro can get.

Two commands do the heavy lifting. `lin` installs modules and resolves dependencies, while `lunar update` refreshes Moonbase and rebuilds anything that needs it. That's a cleaner split than you might expect — the install path and the update path are genuinely separate operations rather than one overloaded flag soup.

The trick that sets it apart from Gentoo is the ISO. The daily install image ships with the entire core Moonbase already built, so the initial install completes fast and only subsequent software gets compiled from source the slow way. That sidesteps the classic source-distro problem of spending an afternoon compiling a compiler before you even get a login prompt.

It runs systemd, targets x86_64 only, uses the Lunar package manager, and leaves desktop choice to you. Active and rolling, so no point releases to wait for. If you want a source distro but balk at Gentoo's install slog, this is the pragmatic middle ground. Niche as hell, but that's the entire appeal.

## 34. Inscriptions - elegant DeepL translation client — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2019/04/learning-foreign-languages.jpg)

**Source:** https://www.linuxlinks.com/inscriptions-elegant-deepl-translation-client/
**Karakeep doc:** `qq2bijhypvcv9gr56xs2hgl7`

**Project:** [Inscriptions](https://codeberg.org/elly-code/inscriptions) — a lightweight GTK desktop client for the DeepL translation API

Inscriptions is a desktop app that wraps the DeepL translation API so you don't have to open a browser tab every time you need a phrase translated. You feed it text, it hits DeepL, it shows you the result. That's the whole product, and the author is deliberately fine with it staying that narrow instead of bloating into a language-learning suite.

You need your own DeepL API key, and it works with both free and paid accounts, so the supported language pairs are whatever DeepL itself offers. The interface is GTK-based and written in Vala, which is an increasingly rare sight in 2026. Translation highlighting marks the translated output so you can tell it apart from what you pasted in, and the error messages are actually readable when a request fails — a low bar plenty of clients still trip over.

It's designed to minimize network chatter and keep resource usage modest, with a localized interface for a few languages. License is GPL v3, developed by a pair going by Stella and Charlie. Nothing revolutionary here, but as a focused, no-nonsense DeepL frontend it's a clean alternative to running translate-shell or juggling browser tabs. If you already pay for DeepL and just want a window, this does exactly that and stops.

## 35. Minisforum Says Disable Four of the MS-R1's 12 CPU Cores - Is Linux Scheduling Them Properly? — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/Minisforum-MS-R1-Ubuntu-banner.png)

**Source:** https://www.linuxlinks.com/minisforum-ms-r1-linux-cpu-scheduling/
**Karakeep doc:** `zf0j9ewc291sf6g9rkc73rk2`

**Project:** [Minisforum MS-R1](https://store.minisforum.com/) — a small ARM workstation with an unusual 12-core heterogeneous CPU

The Minisforum MS-R1 packs a CIX CP8180, a 12-core ARM chip that's nowhere near symmetric: eight Cortex-A720 cores spread across four performance tiers plus four much slower Cortex-A520 cores. Minisforum's own guidance is to disable the four small cores for normal use, claiming their low performance and weak interconnect bandwidth can drag down multi-core workloads. Steve Emms decided to test whether Linux's scheduler actually needs that crutch.

The first surprise is that the CP8180 exposes five distinct frequency groups to Linux, not three. Ubuntu reports the A720s at 2.6, 2.5, 2.3 and 2.2 GHz and the A520s at 1.8 GHz, with CPU numbering that maps 2-5 to the slow cores and 10-11 to some of the fastest. More importantly, ACPI CPPC `highest_perf` values let the kernel compute scheduler capacity, and it normalizes the fast cores to 1024 while the A520s land at a pathetic 279 — about 27% of a top core. So Linux is not guessing about this topology.

For equal-priority CPU-heavy work the scheduler nails it. A single task stays on the fastest pair, eight tasks fill the eight A720s without touching an A520, a ninth task brings in exactly one small core, and twelve threads hit all twelve cores. With twelve threads sysbench reaches about 9,868 events/sec versus 8,180 at eight threads — roughly 20% more throughput the small cores provide, which disabling them would throw away.

The one real weakness shows up under mixed priority. When eight nice-19 background jobs occupy the A720s and a normal-priority task shows up, the scheduler sometimes leaves the foreground work bouncing onto an A520 while low-priority jobs keep a fast core. Forcing the important task onto CPU 0 recovers the loss — about 13-17% of throughput that automatic placement leaves on the table. Emms' verdict: don't disable the cores, Linux handles the hardware remarkably well, but priority-vs-heterogeneous interaction under load is a genuine gap, not a myth.

## 36. vsFetch - graphical Linux system information viewer — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2017/12/server-vector.png)

**Source:** https://www.linuxlinks.com/vsfetch-graphical-linux-system-information-viewer/
**Karakeep doc:** `hdolw7qvq7gmgqnryt57phgv`

**Project:** [vsFetch](https://github.com/victorsosaMx/vsFetch) — a GTK "About This Computer" panel inspired by Fastfetch

vsFetch is what you get when someone takes the Fastfetch terminal aesthetic and slaps a GTK window around it. Instead of dumping ASCII logos into your shell, it renders an "About This Computer" panel with hardware details, desktop environment info, shell, terminal, fonts and dev-tool versions in one place.

It groups everything into Hardware, Desktop, Terminal, Development and Uptime sections, and offers two layouts — a conventional top-header look or a left-hand sidebar — plus a compact mode that's just header and hardware. It auto-detects the OS and can show its distro logo, and color-codes memory and disk utilization so you can eyeball how close to the edge you are.

The customization is where it gets unserious in the best way. You can turn on rain, snow, matrix, aurora and warp background animations, overlay a user image, and add two-color animated separator bars. Config lives in a JSON file with partial-override support and theme inheritance, so you can keep machine-specific settings separate from visual themes, and there's a graphical settings editor for people who'd rather not hand-edit JSON.

It's written in Python under the MIT license, by Victor Sosa. As a system profiler it's not going to displace Hardinfo2 or CPU-X for raw detail, but as a pretty, themeable info screen — the kind you'd leave up on a spare monitor or screenshot for r/unixporn — it's a fun little toy. Pure aesthetic flex, and honestly that's the point.

## 37. Bing-r - desktop IPTV and media player — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/02/011-tv.png)

**Source:** https://www.linuxlinks.com/bing-r-desktop-iptv-media-player/
**Karakeep doc:** `ufif4kv8gdv1caog3yhmmkn1`

**Project:** [Bing-r](https://github.com/vireshwali/Bing-r) — a desktop-native IPTV player and media manager for M3U playlists, live TV, and VOD.

Bing-r is yet another attempt to unify the whole IPTV mess into one desktop app, and honestly the pitch is familiar: stop juggling six browser tabs, a media player, and a terminal. It's Linux-first, built on Python with PySide6 and Qt Quick/QML, MIT-licensed, and sitting at zero stars as of this writing — so call it very early days. The feature list is a mix of real and aspirational. What actually exists is the M3U/M3U8 import path: drag-and-drop local files, pull playlists from a remote URL with auto-update, and EPG parsing off `x-tvg-url` headers. Playback is listed as "Qt Multimedia / mpv integration (planned)", which is a polite way of saying it doesn't play anything yet. The library side is more concrete — SQLite through SQLAlchemy's async ORM, automatic channel dedup and merge across sources, plus channel grid filtering by category, country, and quality. A hero carousel ranks top channels by visit count. A pile of features (favorites, watch history, timeshift, EPG guide) are marked planned. Metadata enrichment leans on the iptv-org database, and IPTVnator is credited as the feature reference, so the DNA is obvious. The README spends real ink warning that it never sells subscriptions or playlists — a sensible disclaimer given the ecosystem's scam density. Verdict: a competent skeleton with clean architecture and CI already wired up, but it's a player that can't play yet. File under "check back in six months."

## 38. vat - render vector graphics in your terminal — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2021/09/Console-Image-Compression.jpg)

**Source:** https://www.linuxlinks.com/vat-render-vector-graphics-terminal/
**Karakeep doc:** `htp9zp0tvrr1i0cn9605eyfb`

**Project:** [vat](https://github.com/jzbrooks/vat) — renders SVG and Android Vector Drawables directly in your terminal.

vat is a small tool with one job and it does it cleanly: it takes vector graphics and draws them right in your terminal. It handles SVG, Jetpack Compose ImageVectors, and Android Vector Drawables, and works on any terminal that implements the Kitty graphics protocol — so Kitty, Ghostty, WezTerm, and friends. That protocol choice is the smart move here, since it means you get actual image rendering rather than some sad ASCII-art approximation. The project is a Kotlin/JVM affair built with Gradle, MIT-licensed, sitting at 30 stars. Install is a one-liner via Homebrew (`brew install jzbrooks/repo/vat`) or just grab the release binary and chmod it. The CLI is deliberately tiny: point it at a file, optionally pass a `--scale` factor or a `--background-color` in hex RGBA, and it spits the artwork out. Windows users run it as `java -jar vat`, which is a minor wart but not the point. There are 200 commits and 12 tags, so it's been quietly maintained rather than abandoned — the latest commit is a Renovate bot dependency bump, which is the most boring possible proof of life but proof nonetheless. The README's example renders a photo into Ghostty and it looks genuinely crisp. Verdict: a niche tool, but the kind of niche that earns a permanent spot in a terminal nerd's toolbox. If you ever want to eyeball a logo or an Android drawable without leaving your terminal, this is the fastest way to do it.

## 39. 7 Best Free and Open Source Chemical Structure Drawing Tools — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/Chemical-Structure-Drawing-Banner.png)

**Source:** https://www.linuxlinks.com/best-free-open-source-chemical-structure-drawing-tools/
**Karakeep doc:** `neooqz3bzrr4irv6huwnhw93`

LinuxLinks is doing its usual roundup thing here, this time for chemists who don't want to pay for ChemDraw. The category is chemical structure drawing — molecular diagrams, reactions, structural formulas — and the field is, unsurprisingly, thin. The standout by a mile is Ketcher, EPAM's molecular editor for the web, which is the only entry here with serious institutional backing and active development. After that it gets scrappy: XDrawChem is a 2D molecule drawing program, ChemCanvas another 2D editor, JChemPaint the Java one with no clean standalone repo left, Molsketch a 2D molecular editor, Butlerov a chemical structure editor, and BKChem a Python editor that's explicitly dormant. So the honest read is that there's really one production-grade option and a pile of mostly-frozen desktop tools behind it. That's the reality of open-source scientific software — the money goes to web editors like Ketcher, and the desktop apps fossilize. The roundup doesn't sugarcoat this, though it also doesn't hammer it home the way it should; a few of these entries are essentially abandonware being listed as viable options. If you're drawing structures for publication or sharing, Ketcher is the answer. The rest are for nostalgia or very specific legacy workflows.

**Projects:**

- **[Ketcher](https://github.com/epam/ketcher)** — EPAM molecular editor for web
- **[XDrawChem](https://github.com/bryanherger/xdrawchem)** — 2D molecule drawing program
- **[ChemCanvas](https://github.com/ksharindam/chemcanvas)** — 2D chemical structure drawing tool
- **JChemPaint** — Java chemical editor (no clean standalone repo)
- **Molsketch** — 2D molecular editor
- **Butlerov** — chemical structure editor
- **BKChem** — Python chemistry editor (dormant)

## 40. dz6 — Vim-inspired terminal hex editor — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/09/hex-editor.jpg)

**Source:** https://www.linuxlinks.com/dz6-vim-inspired-terminal-hex-editor/
**Karakeep doc:** `y0o7jdiuybce230pbhsu6ken`
**Project:** [dz6](https://github.com/mentebinaria/dz6) — a Vim-inspired terminal hex editor for binary files

dz6 is a keyboard-driven hex editor that borrows Vim's modal muscle memory without pretending to be a full Vim clone. It's aimed at reverse engineering, malware analysis, forensics, and low-level work — the kind of job where you spend more time hopping between offsets than staring at a pretty GUI. Written in Rust, GPL v3, from Mente Binária.

The feature list is genuinely useful rather than decorative. You edit in hex or ASCII, search forward and backward for strings and byte sequences, and get a strings window with regex filtering. Bookmarks jump you back to important offsets, and comments persist to a companion database file instead of vanishing. Block marking with colors plus word/double-word/quad-word navigation in both directions covers the "where the hell was that struct" problem.

The standout bits are the PE and ELF header inspector — you can follow a header value straight to its file offset — and a built-in 64-bit calculator that treats cursor values and offsets as variables. Undo buffers your edits before they touch disk, and you can open read-only or start at a specific offset. It even adapts bytes-per-line to your terminal width.

It sits in a crowded field — hexyl, DHEX, hexedit, bvi, and a dozen others — but the PE/ELF header integration and the calculator set it apart from the plain viewers. If you already live in Vim and occasionally need to slice up a binary, this is worth a look before you reach for a GUI tool.

---

## 41. Best Free and Open Source Alternatives to Adobe Connect — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/Adobe-Connect-alternatives-700x400-1.png)

**Source:** https://www.linuxlinks.com/best-free-open-source-alternatives-adobe-connect/
**Karakeep doc:** `epu70qd03ofkyn7u3ohxor0c`

Adobe Connect is the proprietary web-conferencing / virtual-classroom platform that schools and corps pay real money to run webinars and online meetings on. LinuxLinks' pitch is the standard one: you don't need to lease it, because there's a stack of free, self-hostable options that cover the same ground.

The four it recommends break down neatly by use case. BigBlueButton is the virtual-classroom heavyweight, built specifically for teaching with breakout rooms and whiteboards baked in. Apache OpenMeetings is the older generalist — video conferencing plus screen sharing, Apache-licensed, been around forever. Nextcloud Talk is the obvious pick if you already run Nextcloud, since it bolts self-hosted chat and calls onto an install you've already stood up. And Jitsi Meet is the drop-in Zoom/Zoom-alike, the one most people actually reach for when they just want a call that works in a browser.

The honest caveat the piece glosses over: self-hosting conferencing is real infrastructure work. BigBlueButton in particular is a fat stack — a pile of services, a TURN server, decent bandwidth. The "free" is free as in money, not free as in your Saturday afternoon. But if you're already running a homelab or have a Nextcloud box, Talk or Jitsi Meet are genuinely low-friction, and none of these nickel-and-dime you per-seat the way Adobe does.

**Projects:**

- **[BigBlueButton](https://github.com/bigbluebutton/bigbluebutton)** — Web conferencing / virtual classroom
- **[Apache OpenMeetings](https://github.com/apache/openmeetings)** — Video conferencing + screen share
- **[Nextcloud Talk](https://github.com/nextcloud/spreed)** — Self-hosted video chat on Nextcloud
- **[Jitsi Meet](https://github.com/jitsi/jitsi-meet)** — Open-source video conferencing

---

## 42. 23 Best Free and Open Source DNS Servers — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2023/01/System-Admin.jpg)

**Source:** https://www.linuxlinks.com/best-free-open-source-dns-servers/
**Karakeep doc:** `qwtr71y44nauv84r0kufqyv8`

DNS is the internet's directory service, and this is LinuxLinks' roundup of the free and open source servers that run it. The list spans the full spectrum from the reference implementations that carry a chunk of the public internet to tiny single-purpose daemons you'd run on a Pi.

The heavyweights lead the field for a reason. BIND is ISC's reference implementation, ancient and everywhere, still the default answer for authoritative DNS. PowerDNS brings SQL backends and a recursor, the pick when you want your zones in a database. Unbound is the validating recursive resolver that Pi-hole users already know. CoreDNS is the CNCF's plugin-based server, the thing Kubernetes runs its cluster DNS on. NSD and Knot DNS are the high-performance authoritative options from NLnetLabs and CZ.NIC respectively.

Then it gets weird and specific, which is where the list earns its keep. Technitium is a self-hosted DNS server with ad blocking baked in. SmartDNS picks the fastest IP. acme-dns exists solely to serve DNS-01 ACME challenges for Let's Encrypt. aardvark-dns does authoritative DNS for container networks. Hickory is a Rust DNS library with a server attached. dnsmasq is the lightweight forwarder that half the home routers on earth ship.

The caveat is that "best" here is really "all of them" — 23 entries with near-zero editorial filtering means you're doing the choosing, not LinuxLinks. It's a directory, not a verdict. Still, if you're standing up DNS and don't know your recursive from your authoritative, this is a solid map of the territory.

**Projects:**

- **[CoreDNS](https://github.com/coredns/coredns)** — CNCF DNS server, plugin-based
- **[BIND](https://gitlab.isc.org/isc-projects/bind9)** — ISC reference DNS server
- **[PowerDNS](https://github.com/PowerDNS/pdns)** — Authoritative/recursor, SQL backends
- **[NSD](https://github.com/NLnetLabs/nsd)** — Authoritative-only DNS server
- **[Technitium](https://github.com/TechnitiumSoftware/DnsServer)** — Self-hosted DNS with ad blocking
- **[SmartDNS](https://github.com/pymumu/smartdns)** — Local DNS server with fastest-IP
- **[Unbound](https://github.com/NLnetLabs/unbound)** — Validating recursive resolver
- **[Hickory](https://github.com/hickory-dns/hickory-dns)** — Rust DNS library + server
- **[YADIFA](https://github.com/yadifa/yadifa)** — Authoritative DNS server
- **[Knot DNS](https://gitlab.nic.cz/knot/knot-dns)** — High-perf authoritative server
- **[gdnsd](https://github.com/gdnsd/gdnsd)** — Authoritative w/ geo-failover
- **[Dnsmasq](https://thekelleys.org.uk/dnsmasq/doc.html)** — Lightweight DNS/DHCP forwarder
- **[acme-dns](https://github.com/joohoi/acme-dns)** — DNS server for ACME DNS-01 challenges
- **[encrypted-dns](https://github.com/DNSCrypt/encrypted-dns-server)** — DNSCrypt/DoH server
- **[MaraDNS](https://github.com/samboy/MaraDNS)** — Small secure DNS server
- **[aardvark-dns](https://github.com/containers/aardvark-dns)** — Authoritative for container networks
- **[FDNS](https://github.com/netblue30/fdns)** — Firejail DNS-over-HTTPS proxy
- **[tinydns](https://cr.yp.to/djbdns.html)** — djbdns component (tiny authoritative)
- **[pkdns](https://github.com/zhuhaow/SpechtLite)** — DNS/network proxy tool
- **[PopuraDNS](https://github.com/popura-network/PopuraDNS)** — Authoritative DNS server
- **[pdnsd](https://github.com/SAPikachu/pdnsd)** — Proxy DNS with permanent cache
- **[dnrs](https://github.com/ZbrDeev/dnrs)** — Light DNS server in Rust
- **dprox** — DNS proxy

---

## 43. Era — responsive calendar for everyday planning — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/06/mon-monday-paper-desk-calendar-3d-rendering.jpg)

**Source:** https://www.linuxlinks.com/era-responsive-calendar-everyday-planning/
**Karakeep doc:** `qkilvuqf0p0gr9bp6zm9z3p2`
**Project:** [Era](https://gitlab.gnome.org/TitouanReal/Era) — a responsive GNOME calendar that syncs online and works offline

Era is a Rust calendar app from GNOME dev Titouan Real that's built around one idea: the window should shrink and grow to fit how you're actually using it. Squeeze it into a sliver next to your editor and it stays a compact schedule; drag it full-width and it expands into a proper planning surface. Month view is the default browsing mode.

The interesting part is under the hood. It syncs events with supported online calendar providers while keeping offline access — you can read your calendar with no network. The backend is modular and leans on Evolution Data Server for the actual calendar-service integration, which means it piggybacks on a mature, battle-tested sync layer instead of reinventing CalDAV from scratch. The UI follows GNOME's modern desktop conventions and targets both normal displays and smaller form factors.

That's the honest trade-off worth flagging: it's not its own sync engine. If you don't already have Evolution Data Server set up with accounts, you're wiring up EDS config, not just opening Era. That's fine on most GNOME systems where EDS is already there, less clean on a bare tiling setup.

License is GPL v3, and the project lives on GNOME GitLab. It competes with GNOME Calendar (the simple default), Merkuro Calendar, and Calindori on touch devices. Era's differentiator is the responsive, resizable-first design — it's for people who want a calendar that behaves like a panel widget but can become a full planner when they give it room.

---

## 44. Source Mage — source-based Linux distribution — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/04/Linux-Distributions.png)

**Source:** https://www.linuxlinks.com/source-mage-source-based-linux-distribution/
**Karakeep doc:** `joapmlfv7y2ru7q2t7zf8p8t`
**Project:** [Source Mage](https://www.sourcemage.org/) — a source-based Linux distro with the Sorcery package system

Source Mage is an independent, source-based distribution for sysadmins and veterans who want every byte compiled on their own machine. It's the Gentoo philosophy without the Gentoo branding: software is managed through the Sorcery package system, where packages are "spells" and collections of spells are "grimoires." Install a spell and Sorcery fetches the upstream source and compiles it locally, letting you pick build options, dependencies, and compiler flags instead of taking whatever the binary packager decided.

A few choices make it distinct. It doesn't force a desktop environment — that's your call. The main grimoire is restricted to free and open source software, with separate collections for the stuff that doesn't qualify, so the FOSS-only line is actually enforced at the package level rather than shrugged off. And it runs its own init-script infrastructure with simpleinit-msb instead of systemd, which either delights you or sends you running, depending on your religion.

Current state: active, rolling release, targeting x86_64 and i686. The trade-off is the same as any source-based distro — compile times are real, and you're trading a couple of hours of building for control most people never actually use. But if you're the type who flags down a package manager and asks "which CFLAGS did you use," this is the distro that gives you a straight answer.

---

## 45. Colorice — wallpaper-driven Linux colour scheme generator — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/12/028-color.png)

**Source:** https://www.linuxlinks.com/colorice-wallpaper-driven-linux-colour-scheme-generator/
**Karakeep doc:** `wa8tf4nld0hbk6rrvmrgmkaf`
**Project:** [Colorice](https://github.com/rattle99/colorice) — a pywal-style wallpaper colour scheme generator in Oklab

Colorice generates desktop colour schemes from your wallpaper, and the one thing that separates it from a dozen pywal clones is the colour space: it does its math in Oklab instead of RGB or HSL. Oklab is built so numerical differences map to perceptual differences, so the palettes actually look consistent to a human eye instead of just mathematically tidy. It's Python, GPL v3, by rattle99.

Extraction uses K-means clustering in Oklab, with an optional region-aware mode via image segmentation. It then enforces WCAG contrast levels between foreground and background and generates the 16 ANSI slots from the resulting palette — so you don't get a pretty theme that's also unreadable. There are vibrant, muted, warm, and cool mood transforms, plus lighten/darken/saturate/desaturate filters inside templates.

The practical stuff is where it earns its keep. It's pywal-template compatible, so your existing config setups drop in without a rewrite, and it ships bundled templates for terminals, window managers, editors, status bars, and notification daemons. You can chain colour transforms, output multiple formats, run hooks to reload apps after rendering, cache extraction results so you can reapply a scheme without re-analysing the image, and preview output without writing files. Everything lives in XDG-compliant locations.

Compared to wallust, Matugen, or plain pywal, Colorice's edge is the Oklab perceptual model plus the WCAG contrast enforcement. If you've ever generated a wallpaper theme and squinted at a terminal you couldn't read, that's the problem this tool is explicitly trying not to ship.

## 46. gittuf - security layer for Git repositories - LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/09/Data_security_02.jpg)

**Source:** https://www.linuxlinks.com/gittuf-security-layer-git-repositories/
**Karakeep doc:** `y05xe08e8yiezhp0qnh58p6i`

**Project:** [gittuf](https://github.com/gittuf/gittuf) — a platform-agnostic security layer for Git repositories

Git is great at tracking *what* changed, but hilariously bad at telling you *who* is actually allowed to change it. Anyone with push access to a branch can rewrite history, and the rest of us just have to trust that the maintainers knew what they were doing. gittuf is the fix for that specific trust problem.

The idea is a security layer that sits on top of Git and lets developers independently verify a repo's security policies. Instead of blindly trusting that the last commit came from a maintainer, you get a set of cryptographic rules — who can sign off on which refs, what threshold of approvals a change needs, whether a tag is legit — and gittuf checks every action against them. It's not a fork of Git, so you don't have to convince your whole team to switch tools; it plugs into the workflows you already have.

The big win is that it works without any single trusted server or forge. No GitHub, no GitLab, no "well the CI badge was green so it's fine." You can verify the policy chain on your own machine, which matters when the thing you're pulling is a supply-chain attack vector waiting to happen. Software supply chain security has been the hottest mess in the industry since SolarWinds, and this is aimed straight at it.

It's still early and it's not going to replace signed commits overnight, but the direction is right. Anything that makes "did a human actually approve this" a verifiable fact instead of a vibe gets my attention.

## 47. 5 Best Free and Open Source Terminal-Based Linux Discord Clients - LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2018/06/Gaming-Chat.jpg)

**Source:** https://www.linuxlinks.com/best-free-open-source-terminal-based-linux-discord-clients/
**Karakeep doc:** `jeovj0olup7oz5wpo8hmcpsj`

LinuxLinks runs down five ways to run Discord without ever leaving the terminal, which is either the most or least Discord thing you can do. The roundup is strictly TUI-only — no Electron bloat, no GUI clients, no system tray. If you want a windowed client, there's a separate list for that; this one is for people who think a terminal is the only respectable environment.

The standout is Discordo, the feature-rich Go TUI that's basically the reference implementation for this category. It's good enough that someone forked the idea forward into Oxicord as its successor. Concord is the Rust/ratatui option if you want memory safety with your memes. Then there are two oddballs that aren't really clients at all: vimcord, which is just Discord rich presence for Vim/Neovim (so your friends can see you're editing config files instead of talking to them), and rdircd, which bridges Discord to a local IRC daemon so you can keep using irssi or weechat like it's 2003.

The obvious caveat nobody bothers mentioning: Discord's API is a moving target, and self-hosted clients live permanently one breaking change away from being bricked. Also, rich presence and voice are flaky at best on these. But if your goal is to reclaim the RAM Electron is eating and you don't need GIFs to render, this list is a solid starting point.

**Projects:**

- **[Discordo](https://github.com/ayntgl/discordo)** — Feature-rich TUI Discord client
- **Oxicord** — TUI Discord client (successor to Discordo)
- **[Concord](https://github.com/chojs23/concord)** — TUI Discord client in Rust/ratatui
- **[vimcord](https://github.com/Stoozy/vimcord)** — Discord RPC for Vim/Neovim
- **[rdircd](https://github.com/mk-fg/reliable-discord-client-irc-daemon)** — Discord via IRC daemon

## 48. 19 Best Free and Open Source Linux Digital Forensics Tools - LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2019/04/closeup-fingerprint-glass-against-dark-background-modern-technology-biometrics.jpg)

**Source:** https://www.linuxlinks.com/digitalforensics/
**Karakeep doc:** `xmc8ju3o31u02k30xa70gany`

LinuxLinks compiles nineteen open-source tools for digital forensics, and the framing is worth paying attention to: forensics is the art of investigating without modifying the media. That one constraint — don't fucking touch the evidence — is what separates a real tool from a toy, and everything on this list is built around it.

The lineup spans the whole investigation lifecycle. On the acquisition end you've got guymager and dcfldd for bit-exact disk imaging, plus rdd for when you need forensic-grade dd that won't silently eat your data. On the analysis side, The Sleuth Kit is the filesystem forensics workhorse, with Autopsy as its GUI wrapper for people who don't want to live in a shell. Memory forensics is covered by Volatility 3 and the deeply cursed-but-brilliant MemProcFS, which mounts physical RAM as a filesystem you can just browse.

For incident response at scale, GRR Rapid Response and Velociraptor let you query fleets of machines remotely, while Dissect (Fox-IT) and Mozilla InvestiGator handle distributed collection. Timeline nerds get Plaso and Timesketch. The reverse-engineering crowd gets radare2 and iaito. And then there's IPED, the Brazilian forensic toolkit that's quietly very good, and UAC for Unix artifact collection.

The spread is genuinely comprehensive, though "19 best" is doing some lifting — a few of these overlap hard (Sleuth Kit vs. Autopsy, radare2 vs. iaito are the same project in a different coat). Still, if you're building a forensics toolbox, this is the reference list.

**Projects:**

- **[GRR Rapid Response](https://github.com/google/grr)** — Google incident response framework
- **[Radare2](https://github.com/radareorg/radare2)** — Reverse-engineering framework
- **[The Sleuth Kit](https://github.com/sleuthkit/sleuthkit)** — Filesystem forensics library
- **[MemProcFS](https://github.com/ufrisk/MemProcFS)** — Physical memory as a filesystem
- **[Autopsy](https://github.com/sleuthkit/autopsy)** — GUI forensics platform (TSK)
- **[iaito](https://github.com/radareorg/iaito)** — GUI front-end for radare2
- **[Chainsaw](https://github.com/WithSecureLabs/chainsaw)** — Windows event log forensics
- **[Velociraptor](https://github.com/Velocidex/velociraptor)** — Digital forensics + IR platform
- **[Timesketch](https://github.com/google/timesketch)** — Timeline analysis for forensics
- **[Plaso](https://github.com/log2timeline/plaso)** — Super timeline engine (log2timeline)
- **[Volatility](https://github.com/volatilityfoundation/volatility3)** — Memory forensics framework
- **[UAC](https://github.com/tclahr/uac)** — Unix Artifact Collector
- **[IPED](https://github.com/sepinf-inc/IPED)** — Brazilian forensic toolkit
- **[guymager](https://guymager.sourceforge.io/)** — Disk imaging for forensic acquisition
- **[Dissect](https://github.com/fox-it/dissect)** — Incident response framework (Fox-IT)
- **[dcfldd](https://github.com/resurrecting-open-source-projects/dcfldd)** — Enhanced dd for imaging
- **[rdd](https://sourceforge.net/projects/rdd/)** — Robust dd — forensic imaging
- **Jomon** — Forensics tool
- **[Mozilla InvestiGator](https://github.com/mozilla/mig)** — Distributed forensics (MIG)

## 49. hw-monitor - comprehensive hardware monitoring application - LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/03/Benchmarking-Vector.png)

**Source:** https://www.linuxlinks.com/hw-monitor-comprehensive-hardware-monitoring-application/
**Karakeep doc:** `bvl39wobm6yn391fxpkdkwpe`

**Project:** [hw-monitor](https://github.com/husseinhareb/hw-monitor) — a Linux desktop hardware monitor with live system data

hw-monitor is a Linux desktop app that wants to be your one-stop shop for "what the hell is my machine doing right now." It pulls live CPU, memory, GPU, disk, and network data into a single interface, alongside sensor readings, running processes, and system services. Think of it as a task manager and a sensor dashboard that finally got married.

The appeal is the consolidation. Instead of juggling `htop`, `nvidia-smi`, and a handful of `/proc` greps, you get everything in one window — which is genuinely nice if you're the person who gets called when the server "feels slow." The sensors in particular are the useful part, since Linux sensor tooling is famously fragmented (lm-sensors can go sit in a corner).

It's built in Rust, which means it'll be snappy and won't leak memory the way the old Python dashboard of the week would. That's a real point in its favor for something you leave running on a second monitor all day.

The caveat is the usual one for these things: there are a dozen monitoring apps, and hw-monitor is still young. It's not going to dethrone btop for pure terminal speed or Grafana for fleet-wide metrics. But as a clean desktop GUI that shows you sensors, processes, and services without requiring you to remember six commands, it fills a real niche. Worth a look if your current monitoring setup is a sticky note that says "check `free -h`."

## 50. CLP - compress, search and analyze logs — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2017/10/log-analyzers.jpg)

**Source:** https://www.linuxlinks.com/clp-compress-search-analyze-logs/
**Karakeep doc:** `aajxr3wybsz7tgnv7ndddr0w`

**Project:** [CLP](https://github.com/y-scope/clp) — an end-to-end log compressor and search engine that stores logs small without killing queryability

CLP (Compressed Log Processor) is YScope's answer to the problem everyone with a real fleet has: logs eat disk, and gzip makes them useless to search. The trick is that it compresses *and* keeps things queryable at the same time, instead of treating compression as some archival afterthought you throw on a cron job and never touch again. It handles both structured JSON logs and free-form garbage text, and you can search the compressed archives without decompressing them first. That index-less design is the interesting part — no giant inverted index to babysit, just query straight against the compressed representation. It ships logging libraries that compress messages in real time before they ever hit disk, with Python and Java integrations. Under the hood it's C++, Apache 2.0 licensed, and there's a pushdown-automata parser for pulling structure out of messy log lines. You can filter by severity, do distributed compression and search, and analyze the compressed intermediate form from Python or Go. The obvious competitor is Loki or VictoriaLogs, but those still index; CLP bets on a purpose-built intermediate representation instead. Whether that holds up at scale is the open question the evaluation datasets are meant to answer. For anyone drowning in observability storage costs, it's worth a serious look. 😤

## 51. pywal16 - generate and change colour schemes on the fly — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/12/038-color-scheme.png)

**Source:** https://www.linuxlinks.com/pywal16-generate-change-colour-schemes/
**Karakeep doc:** `cw2852i762zojir3qcgugde1`

**Project:** [pywal16](https://github.com/eylles/pywal16) — a pywal fork that builds 16-colour palettes from an image and slaps them across your desktop

pywal16 is what you grab when you want your terminal, window borders, and TTY to all match the wallpaper you just set, without the whole thing turning into a config-file massacre. It's a fork of pywal, so the core idea is identical: analyze an image, pull the dominant colours, build a complementary 16-colour palette, and ship it out. The difference is it leans on templates instead of rewriting your existing app configs — it generates colour data that programs consume, so your carefully tuned dotfiles stay intact. That's the real appeal: wallpaper-driven theming with zero collateral damage to settings you actually like. It ships 250+ predefined themes, supports user-made theme files you can share, and has a few different colour-generation backends so you can pick the extraction approach that doesn't produce vomit. It updates compatible terminal emulators in real time and can even recolor the TTY itself. Templates cover Lua and QML, so it reaches into a lot of corners. Written in Python, MIT licensed, by eylles. The obvious counter is that there are a dozen of these now — wallust, matugen, lule in Rust — and pywal itself was abandoned, which is exactly why this fork exists. If you want the classic workflow with a maintained codebase, it does the job. 🎨

## 52. Hakoniwa - process isolation using Linux security facilities — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/Application-Sandbox-Tools-banner.png)

**Source:** https://www.linuxlinks.com/hakoniwa-process-isolation-using-linux-security-facilities/
**Karakeep doc:** `w9jk3m5rkpoi0zt8xtxa2hlu`

**Project:** [Hakoniwa](https://github.com/souk4711/hakoniwa) — a Rust framework that sandboxes processes by stacking namespaces, cgroups, Landlock, and seccomp

Hakoniwa is a process isolation framework that takes the position that a chroot alone isn't a sandbox, and it's right. Instead of pretending filesystem separation is enough, it stacks the whole Linux security toolkit: a fresh mount namespace with a temporary root and pivot_root, setrlimit resource caps, cgroup v2 through systemd, Landlock for ambient filesystem access, and seccomp filters to cut down syscalls. You can give it an isolated user-mode network stack via a network namespace plus pasta. It mounts minimal device and tmp filesystems inside the sandbox, and you get configurable bind mounts to expose only the host resources you actually want. There are profiles aimed at desktop apps, and it'll sandbox graphical applications, not just CLI tools — which is the annoying case most tools dodge. The standout is the Rust library: you can construct namespaces, mounts, resource limits, Landlock rules, and seccomp policies directly from your own code, so it works as a building block for apps that need to launch restricted children programmatically. GPLv3, Rust, by souk4711. The trade-off versus firejail or bubblewrap is that Hakoniwa is younger and less battle-tested, and stacking seccomp + Landlock is fiddly to get right. But as a library-first sandbox it's a genuinely useful primitive. 🔒
