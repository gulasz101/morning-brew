---
date: 2026-09-21
slug: 2026-09-21-morning-brew
tags: Cloudflare,Web Security,Internet Technology,Machine Learning,Artificial Intelligence,AI Models,Data Classification,Linux,Open Source Software,Command Line Tools,Disk Encryption,LUKS,Accounting Software,Double Entry Accounting,Plain Text Accounting,Personal Finance,Open Source,Self-Hosted,Investment Research,Stock Market Analysis,JavaScript,Frontend Development,User Interface,Web Development,jQuery,Productivity Tools,macOS,File Manager,Keyboard Navigation,Automation,DevOps,Containerization,Monitoring,Container Orchestration,Markdown,Model Context Protocol,Documentation Framework,Debugging,Programming Tools,Python,Software Development,Developer Tools,Vector Search,Command Line Interface,Search Tools,E-commerce,Tailwind CSS,UI Library,Design System,TypeScript,HTTP Client,API Requests,Online Attacks,Python Programming,Materials Science,Computational Thermodynamics,Phase Equilibria,C Programming,Static Site Generators,Binary Analysis,Reverse Engineering,Static Analysis,Website Troubleshooting,Mind Mapping,Brainstorming,Structured Thinking,Edge Computing,Immutable Operating System,Cloud Computing,Linux Distribution,Software Engineering,Rust Programming,Performance Optimization,Vite,File Associations,MIME Types,Data Privacy,Web Tracking,Cookies,Online Advertising,Virtualization,Infrastructure Management,KVM,Self-Hosted Software,Music Scrobbler,Spotify,Data Logging,Education,Cybersecurity,Internet Safety,Technology,Website Status,Molecular Modeling,Structural Biology,Crystallography,Cryo-EM,Design Systems,Spam Filtering,Phishing,Data Technology,Black Box Models,Explainable AI,Web Applications,Data Visualization,Amateur Radio,Geographic Mapping,Raspberry Pi,Computing Technology,Hardware,Firmware,Single Board Computer,Operating Systems,Linux Kernel,Productivity,Time Tracking,Cryptocurrency,Trading Bots,Blockchain Technology,Docker,Self-Hosting,Software Subscriptions,NixOS,Garuda Linux,Gaming Hardware,Android Handhelds,Security Verification,Video Games,Linux Gaming,Steam,Game Reviews,Networking,Web Servers,Linux Distributions,GNOME Desktop,Debian,Arch Linux,Programming,Tech Tools,Microcontrollers,Embedded Systems,Video Graphics,PC Gaming,Proton,Steam Deck,ARM64 Architecture,Large Language Models,Computer Vision,Audio Software,Music Production,Guitar Simulator,Effects Processor,Software Bill of Materials,Disassembler,Computer Architecture
---

# Morning Brew — 2026-09-21

Fifty links from Monday. Eight videos, forty-two articles. The RSS firehose dumped a wall of LinuxLinks and open-source project stubs on me again, plus the usual YouTube diet. A few actually worth your time buried in the pile — a Raspberry Pi firmware lockdown on RAM upgrades, a local LLM that names and sorts your screenshots, and niebezpiecznik on a crypto-stealing YouTube scam. Dig in.

### Hand-bookmarked

## 1. 5 Docker containers replaced my most expensive subscriptions — by XDA
![XDA](https://static0.xdaimages.com/wordpress/wp-content/uploads/wm/2026/09/self-hosted-immich-nextcloud-bentopdf.jpg?w=1600&h=900&fit=crop)

**Source:** https://www.xda-developers.com/docker-containers-replaced-my-most-expensive-subscriptions/
**Karakeep doc:** `kxa4xpiefkynt6l06sswv327`

A first-person piece about cutting recurring bills by self-hosting five Docker containers instead. BentoPDF replaces Acrobat for the author, who only used a fraction of Adobe's features and wanted to stop paying for the rest. n8n replaces Zapier for simple automations, letting the author wire up APIs, webhooks, and scheduled workflows on their own server instead of paying per task. Nextcloud stands in for cloud storage, giving a self-managed central place for documents and a way to decide how much space to provision rather than upgrading a subscription whenever the quota fills. Immich replaces a photo-storage service, backing up phone photos and browsing them through web and mobile apps that feel closer to Google Photos than a plain folder. Jellyfin covers movies and TV for someone who doesn't watch enough to justify a streaming or media-server subscription, organizing existing media files into a proper library. The framing is modest — the author didn't set out to replace every subscription, just started questioning which ones were worth keeping. The bigger win, they argue, is control over the tools and the data, not just the money saved each month. It is a practical, low-stakes list rather than a manifesto, and it leans on the fact that all five run without a complicated setup.

**Projects:**

- **[BentoPDF](https://github.com/alam00000/bentopdf)** — Self-hosted PDF toolkit (the Acrobat replacement)
- **[n8n](https://github.com/n8n-io/n8n)** — Workflow automation platform (the Zapier replacement)
- **[Nextcloud](https://github.com/nextcloud/server)** — Self-hosted cloud storage and collaboration suite
- **[Immich](https://github.com/immich-app/immich)** — Self-hosted photo and video library with mobile backup
- **[Jellyfin](https://github.com/jellyfin/jellyfin)** — Free software media server for movies, TV, music, live TV

## 2. Garuda Linux Begins Nixification By Promoting Its Sybsystem — by It's FOSS
![It's FOSS](https://itsfoss.com/content/images/2026/09/garuda-nix-banner.png)

**Source:** https://itsfoss.com/news/garuda-linux-nixification/
**Karakeep doc:** `lmz64k5qm3kq7m5b8zibcczs`

Garuda Linux is steering its userbase toward Nix by renaming the Garuda Nix Subsystem to Garuda Nix, and the change is more than cosmetic. What was once a side project for dual-booting NixOS alongside Garuda is now its own bootable installer. The flake ships a dedicated ISO with a Calamares GUI, plus a command-line `install-garuda-nix` tool for scripted setups. As a subsystem it already let you run NixOS next to Garuda on the same drive, kept separate through a BTRFS subvolume rather than a dedicated partition. Calamares handles most of the install, asking you to pick an edition — Dr460nized or Mokka — and letting you opt into extras for better gaming and printing support. The CLI tool is the interesting part: it covers the basics while offering presets for desktop, laptop, server, and handheld setups, plus eight partition layouts spanning ext4 and BTRFS, encrypted or not. The real draw is impermanence — flip it on and the root filesystem wipes clean each reboot, either via BTRFS rollback to a snapshot or by running root out of tmpfs on ext4. Login credentials survive because user and root passwords go through yescrypt hashing before landing in the generated config. Wi-Fi credentials and per-user config folders stay persistent by default; anything else you have to declare manually or it gets deleted on the next restart. Both editions are already live as daily ISO builds, and existing NixOS users can pull the installer straight from the flake with a single `nix run` command.

## 3. Install SteamOS on Android Handhelds with Armada OS — by Geeky Gadgets
![Geeky Gadgets](https://www.geeky-gadgets.com/wp-content/uploads/2026/09/odin-armada-os.webp)

**Source:** https://www.geeky-gadgets.com/install-steamos-android-handhelds/
**Karakeep doc:** `kxqtw6kcdfda8tlix5skgus0`

Armada OS is a SteamOS-like Linux for ARM handhelds that turns Android devices — the Odin 3, Thor, and Retroid Pocket Nova are the named targets — into something close to a Steam Deck. Installation is the headline claim: download from the GitHub repo, write to a microSD card or internal storage, and you're done in under five minutes, no real technical skill required. Feature-wise it brings full Steam integration with Steam Sync for library, achievements, and progress, plus a pre-installed loader called Deki Loader for customization and power management. There are eco, balanced, and performance modes, a functional sleep mode that pauses sessions with minimal drain, and experimental x86-to-ARM conversion that stretches which Steam titles will run. The honest caveats are here too: frame rates trail native Android or dedicated consoles, older and less demanding games fare best, and there are occasional display glitches and download interruptions. LED support is limited, and sleep mode still sips power when idle. It is community-driven, with developers and users collaborating over Discord and frequent updates rolling out. The piece frames Armada OS as a budget way to get console-like portable gaming by repurposing hardware you already own, while being clear-eyed that it is still early-stage and you should expect rough edges. One commenter under the article points out it requires a factory reset, so the "five minutes" is really five minutes plus hours of re-setup.

## 4. The most highly rated Native Linux Steam games for August 2026 — by GamingOnLinux
![GamingOnLinux](https://www.gamingonlinux.com/uploads/articles/tagline_images/860287369id29809gol_og.jpg)

**Source:** https://www.gamingonlinux.com/2026/09/the-most-highly-rated-native-linux-steam-games-for-august-2026/
**Karakeep doc:** `w84sx5gwwq9dqrkrswogo4ex`

Liam Squires-Hand's monthly ritual of wading through the Steam firehose so you don't have to. The premise is simple and a little stubborn in 2026: Proton is fine and everyone loves it, but some of us still want to see developers ship an actual native Linux binary instead of crossing their fingers that the compatibility layer holds. So here's a top 15, ranked purely by user review score, of native Linux games that dropped in August 2026.

Fields of Mistria tops the pile with an "Overwhelmingly Positive" badge and over twenty-five thousand reviews — a farming/life sim that clearly struck a nerve with the cozy crowd. Sandustry follows, a factory game where every pixel is a mineable resource, sitting pretty at Overwhelmingly Positive with three thousand reviews. Sovereign Tower brings a Round Table management RPG where you rewind time to fix your own bad decisions, and Smack Talk is a voice-controlled platform fighter where you literally shout your attacks — a gimmick that apparently doesn't wear thin.

The list rounds out with Sludgineers, Lootbound, Project P.I.T.T., Hearth and Hamlet, Money for Girls: Amortized, Divinum, Crownhold, Flats Full of Cats, Stackmon, Ultrapool, and a 1928 German alternate-history sim called Social Democracy. Yes, you read that last one right — a game about whether you can stop the Nazis from taking power, rated Very Positive.

Nothing here is a blockbuster. That's sort of the point. It's the usual indie long tail, the stuff you'd never stumble onto through Steam's front page because the algorithm buried it under ten thousand asset flips. Squires-Hand promises the format will keep getting tweaked month to month, which is code for "we'll see if anyone actually clicks these." If native Linux gaming is your hill, here's your shovel. Otherwise you'll keep playing whatever Proton feeds you and never know the difference.

## 5. The RP2350 Does 1080p — by Hackaday
![Hackaday](https://hackaday.com/wp-content/uploads/2026/09/rp2350-rpi-cc-by-4-featured.jpg)

**Source:** https://hackaday.com/2026/09/21/the-rp2350-does-1080p/
**Karakeep doc:** `jgvunscr4qz0ixtbdknxcjdu`

Aaron Gayle has done the thing everyone said a Pico-class chip couldn't: he's pushing genuine 1080p video out of an RP2350. The previous ceiling for Raspberry Pi Pico boards was 720p, which the older RP2040 could just about manage. The 2350 is faster with faster peripherals, but even so, Gayle had to overclock it to 372 MHz to get the extra pixels through. That's a microcontroller running well past its comfort zone for bragging rights, and the bragging rights are real.

There's a catch, and it's the kind of catch that makes the whole thing more interesting. There's no room for a framebuffer, so the chip generates the image scanline by scanline — a technique most people associate with 8-bit computers from the 1980s, not with silicon that shipped last year. It's a genuinely clever throwback, the embedded equivalent of writing a game that fits in a boot sector.

The 1080p code lives inside a project called TVtop, a board game where the board renders on the TV and players interact through their phones over Wi-Fi. That's why there's also an ESP32 in the mix, though Hackaday is careful to note the ESP32 has nothing to do with the video trick — it's just there to handle the networking the RP2350 shouldn't be wasting cycles on.

Gayle says he was inspired by an earlier Hackaday story that asked whether 1080p from the RP2040 was even possible, which is a nice full-circle moment: someone posed the question, and a year or two later someone else answered it by overclocking the successor chip and brute-forcing scanlines. The firmware is on [GitHub](https://github.com/aarongayle/tvtop-kiosk-firmware) for anyone who wants to try, and Hackaday is already fishing for whatever gets built on top of it next. This is the kind of thing that doesn't have an obvious consumer use and doesn't need one — it exists because the barrier was there and it could be broken.

## 6. Proton Experimental gets fixes for ARM64, EA App, Modern Warfare 2 (2009), Ragnarok: The New World and more — by GamingOnLinux
![GamingOnLinux](https://www.gamingonlinux.com/uploads/articles/tagline_images/1670890649id29811gol_og.jpg)

**Source:** https://www.gamingonlinux.com/2026/09/proton-experimental-gets-fixes-for-arm64-ea-app-modern-warfare-2-2009-ragnarok-the-new-world-and-more/
**Karakeep doc:** `bkuw4eahsuxnwczhdvyj8qlc`

The September 21st Proton Experimental drop is mostly a bug-swat pass aimed at Valve's testing branch — the place fixes land before they graduate to a stable numbered Proton. The headline work is Ragnarok: The New World finally becoming playable outside the Steam Deck, plus a Proton 11 regression fix that gets Deus Ex: Mankind Divided running on AMD GPUs again. The rest is a pile of fiddly launcher fixes: the EA App login window now focuses correctly under Gamescope, and Call of Duty: Modern Warfare 2 (2009)'s Safe Mode popup actually responds.

The interesting meat is underneath. Wine Mono jumps to 11.3.0 and Xalia to 0.5.0, and both now ship ARM64 builds — a port of Mono to ARM64 Windows, with several components compiled as arm64ec. That's the signal Valve is serious about non-x86 hardware like the Steam Frame. Xalia, Valve's input-shim layer for translating controller input to legacy Win32 dialogs, also picked up app-specific logic for HITMAN World of Assassination and fixed a combo-box bug where the A button simulated an enter keypress so selections actually register. It also stopped burning CPU in its main loop for no reason. If you care about Proton, this is the version where ARM64 stops being a footnote and starts being a first-class target.

## 7. My local LLM now names and sorts every screenshot I take, and I'll never manually organize them again — by XDA
![XDA](https://static0.xdaimages.com/wordpress/wp-content/uploads/wm/2026/09/ollama-website-on-macbook.jpeg?w=1600&h=900&fit=crop)

**Source:** https://www.xda-developers.com/local-llm-names-sorts-every-screenshot-i-take-never-manually-organize-again/
**Karakeep doc:** `ur6zjz6j9n0r691v444gy7db`

A small Python script plus a local vision model replaces the endless "Screenshot 2026-09-21 at 14.37.22.png" junk drawer. The setup: Ollama running Qwen2.5-VL (3B) locally, the `watchdog` library watching the macOS Screenshots folder, and `pydantic` shaping the model's output so it returns a clean title and category instead of free-text rambling. Each new file gets handed to the model, which figures out what's in it, renames it, and drops it into a subfolder like "Personal" or "Needs Review."

The honest caveat is speed. Qwen2.5-VL running on a Mac is markedly slower than the cloud Claude skill the author used before — a screenshot sits for a little while before the rename lands. But the trade is zero ceremony: no opening Claude Code, no navigating folders, no manual trigger. A LaunchAgent starts the script at login and it just watches forever. That's the actual win here — the first version that's genuinely hands-off. The author's verdict is blunt: it took effort to set up and isn't fast, but it's the only one where you can take a screenshot and forget it existed. If you already run Ollama locally, the marginal cost of adding this is near zero.

### RSS — YouTube

## 8. Jev is incredible — by Theo - t3.gg
![Theo - t3.gg](https://i.ytimg.com/vi/F3YXg7AaKWE/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=F3YXg7AaKWE
**Karakeep doc:** `zscpncm12h4egjfmfnede54z`

Theo is losing his mind over Jev, a new "system one" model from Typesafe AI, and for once the hype has a point — this thing isn't another slightly-better-at-code LLM, it's a purpose-built classification engine. Built by Diogo, an ex-OpenAI guy who claims he helped co-invent ChatGPT and RLHF, Jev doesn't generate text or write code at all. It takes structured state in, returns type-safe JSON out, and it literally cannot hallucinate the format because it's contract-bound to the shape you define. The speed numbers are genuinely stupid: 70–500ms versus 3–300+ seconds for an LLM doing the same classification, roughly 40–200× faster, and it costs about 4¢ per million input tokens with output tokens being free — "too cheap to meter." Compare that to $10/M on something like Fable and you see why Twitter collectively lost its shit. 🚀 Theo walks through the framing — it's named after Jevons paradox, the idea that cheaper power means you use *more* of it, not less — and lands on the model being best understood as a "smart if statement," a switch you drop between states to route logic or map-reduce over a giant data pile. He's careful to beat the misunderstanding out of you: this is *not* a reasoning model, it's about as smart as a switch statement, and its context window is a tiny 32K. So if you're thinking of using it to judge between four different LLM outputs, or to compact your agent's context, Theo has some very loud words for you about why that's a terrible idea — you'd be asking a reflex to do deep thought, and the reasoning traces you'd need aren't even exposed by the API providers anymore. Where it shines is real: batch-classifying 1,500 emails at 200ms each and 38/sec, categorizing 32k messages across 1,118 Codex threads for 37¢, live Doom/checkers/Wiki-racing demos driven off raw game state. His closing heuristic: if you can answer the question in under ten seconds of perception, Jev's your model. If it needs thinking, go find a reasoning model. 😅

## 9. Lovable Rewrote Vite in Rust... (kind of) — by Better Stack
![Better Stack](https://i.ytimg.com/vi/msSZ4CL_sNg/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=msSZ4CL_sNg
**Karakeep doc:** `ir0rpos64dowuspz2mcjje5o`

Add another notch to the Rust-rewrite counter. Lovable rebuilt the Vite dev server in Rust and called it OJ, short for Orange Juice, claiming four times better memory and two times faster cold starts. The claim, as usual, needs a closer look. OJ is a single Rust binary you point at an existing Vite project; it reads your Vite config and still runs your Vite plugins, but the dev server underneath — file watcher, module graph, HMR, React Fast Refresh — is rewritten in Rust using Rolldown and Oxc, the exact crates VoidZero maintains. So it is not remotely a from-scratch Vite replacement. Testing a TanStack app, the two behaved nearly identically: SSR, hydration, server functions, fast refresh, dynamic routes, Tailwind, asset imports all worked. The differences are real but small. Fast Refresh under OJ did a full reload on a TanStack app and dropped component state, though a plain React app held its state fine — some edge case they have not handled. Memory on a small app was roughly equal, with OJ only slightly ahead. OJ only earns its keep on huge apps. Against a five-thousand-component app, OJ reached a painted page about 1.7x faster than stock Vite while using about a quarter of the memory. Vite 8.1's experimental bundle dev mode closes the cold-start gap but does nothing for memory. The real reason Lovable built this is scale: they run roughly a million preview sandboxes a day, so they coalesce agent file-bursts into a single update and even gate updates behind an explicit flush endpoint. Evan You largely agreed — impressive, but it is a dev server around VoidZero components, not a Vite rewrite, and it only supports the one React shape Lovable generates. His most interesting point is that AI has collapsed the cost of reimplementing dependencies, so expect a wave of tailored forks maintained per use case. Probably good for maintainers, definitely a fragmentation risk. Unless you run a million sandboxes, you will never need this thing. Have you ever actually felt Vite be slow?

## 10. Shadcn Just Fixed Tailwind's Biggest Problem — by Better Stack
![Better Stack](https://i.ytimg.com/vi/tPQgw_DPIoM/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=tPQgw_DPIoM
**Karakeep doc:** `levpl5bb3c6qvgc80k4zptfh`

Shadcn shipped a linter to solve the one problem Tailwind has never cracked: enforcing a design system while AI agents are writing most of the code. Tailwind class names are just strings, so TypeScript lets an agent slap `p-4` onto a button that already owns its padding, or drop `bg-pink-500` into a component that's supposed to use themed colors, or hardcode `p-[13px]` when the spacing scale jumps from twelve to sixteen. None of that throws an error, and markdown rule files are useless for enforcement because nothing actually checks them. Shadcn ran eight bait tasks — "add a delete button, make it pink with pill corners," "make the pricing card really pop" — and every model spewed violations until the linter was turned on, at which point the count hit zero. The tool is an Oxc or ESLint plugin that works on any Tailwind v4 project, no shadcn/ui required. It ships six rules: `no-restyle-but-allowing-layout` (pages can position a component but not restyle it), `no-raw-colors`, `no-arbitrary-values`, `no-inline-styles`, `no-unknown-classes`, and `enforce-static-classes`. The nice part is the errors read your actual CVA setup, so if your button defines sizes, it tells the agent which ones exist instead of whining generically — and that saves token spend since the agent doesn't have to load your whole design doc. Contracts let you set per-component rules with regex, and custom messages pull placeholders straight from your code. It's not magic: it can't see plain CSS or `@apply`, only traces class values one hop within a file, and a brand-new theme token passes by definition — so an agent can still sneak `hot-pink` in as a "new token." The prerequisite is that you actually have variants and a real design system; if your button just accepts any class name, there's nothing to enforce. For now it's Oxc and ESLint only, with a Biome plugin sitting open as a GitHub issue. If AI is going to write the code, this is the leash that keeps it on your spacing scale.

## 11. This Invisible Text Is Breaking Every Spam Filter — by Better Stack
![Better Stack](https://i.ytimg.com/vi/_AvTOnaD1H8/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/_AvTOnaD1H8
**Karakeep doc:** `hbtb2nvasy3yexxpc90n0jon`

Invisible Unicode tag characters — perfectly readable to a computer, completely invisible to your eyeballs — have spent the last two years as the go-to prompt injection trick for attacking AI models. Now spammers have grabbed the same weapon for a far more boring reason: dodging keyword filters. Microsoft just reported that spam operators slice words like "funding," "loan," and "credit" apart with tag characters, so you see "funding" while the filter sees "fun," then a wall of invisible junk, then "ding." The keyword match dies, the human reader notices nothing. The scale is genuinely absurd: in one early-February day, Microsoft Defender for Office went from catching about twenty-one thousand of these signatures daily to over 1.3 million. The campaign was a Small Business Administration loan phishing scheme running through roughly 150 disposable domains stitched together from a vocabulary of only twenty-eight words, producing gems like "guardian growth funding" and "digital capital boost." The punchline is that over 99% of these messages still got caught — and not because of the invisible characters. Sender and IP reputation plus Defender's own ML classifiers fired independently. Even worse for the attackers, tag characters are so rare in legitimate email that merely using them is now a red flag. Microsoft's advice for anyone building detection software is blunt: normalize or strip invisible tag characters before your spam and phishing filters run, and do the same before any AI assistant ingests the email. That one fix slams the prompt injection door and the spam door shut at the same time.

## 12. AI Model “Black Boxes” Are Dangerous — by Theo - t3․gg
![Theo - t3․gg](https://i.ytimg.com/vi/_jmN7JFOEGA/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/_jmN7JFOEGA
**Karakeep doc:** `re10d6q30141tnpsi2ei23mf`

The argument here is that the standard black-box evaluation model is a joke. You hand an evaluator an API key, they fire off a pile of requests, get responses back, and cross their fingers — that's not real safety testing, that's theater. The people actually trying to figure out whether a model is dangerous should be embedded inside the company with the same access every employee has. No firewall between the folks testing for safety and the folks building the thing, no secrets held back from the evaluators. Otherwise you get a model maker who gets to cherry-pick what the testers see while simultaneously claiming the thing is safe. The whole point is that the people validating a model's safety shouldn't be kept at arm's length by the company producing it, because the moment there's a curtain between them, the safety claim stops meaning anything.

## 13. Raspberry Pi locks down RAM upgrades in Firmware — by Jeff Geerling
![Jeff Geerling](https://i.ytimg.com/vi/ltofM26akZQ/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=ltofM26akZQ
**Karakeep doc:** `lcnp189fkcu8w4jyu0mrrx74`

Raspberry Pi slipped a feature into their firmware that blocks users from swapping RAM chips — even same-capacity chips pulled from other Pi boards. The reason is real: people were buying cheap 1- or 2-gig Pi 5s, soldering in flaky eight-gig chips, and flogging them as new eight-gig boards, and the AI bubble made that grift genuinely profitable. Geerling totally gets why Raspberry Pi doesn't want to support boards sold like that — flaky RAM and dodgy resellers are a nightmare. What he doesn't get is the execution. The firmware update that killed RAM swaps shipped in late 2024, two years ago, so you can't blame the current RAM pricing mess. Raspberry Pi is within its legal rights to lock the hardware down, but that doesn't mean anyone has to like it. He chatted with DosDude1 at VCF Midwest, who has sixteen-gig chips ready to go but can't use them without hacking the firmware. The workaround is running ancient firmware, and there's no easy way around it otherwise. Raspberry Pi does have a technical point: LPDRAM memory timings are genuinely tricky, and a bad solder joint or a barely-passing chip produces weird failure modes that get worse with heat and overclocking. Geerling's counter is the old warranty bit on the Pi 1/2/3 — a firmware flag that flipped if you bypassed safety limits in config.txt. Instead of blocking legitimate RAM swaps outright, set a one-time flag that says "no warranty for you," upgrade the RAM, and it's on your head. Right now there's no physical way to identify a RAM-swapped Pi, though Geekworm's blog shows a software route via the published model codes. Someone on Hacker News even suggested drilling a hole for the factory RAM size. In the end, it's another sad notch in the slow death of hardware ownership.

## 14. How Much Of The Linux Kernel Is Rust & AI — by Brodie Robertson
![Brodie Robertson](https://i.ytimg.com/vi/EoqCAv9PVMA/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=EoqCAv9PVMA
**Karakeep doc:** `rfef4ugit4ko91hnobwvv79k`

The kernel's greybeards — Torvalds, Kroah-Hartman, and the rest — keep the whole thing glued together, but the mailing list is full of people wishing the project still ran like it did twenty years ago. Two things keep showing up in the headlines: Rust and AI. Rust support was first proposed in 2021, and minimal initial support merged a year later in 2022, with a famous email where Torvalds trashed the idea over an out-of-memory panic that would take the whole system down in kernel space. Kroah-Hartman's now-quoted line is that Rust makes coding fun again, and his unscientific estimate is that 80% of the kernel's CVEs over the last twenty-five years would have been caught by the compiler. He frames the language choice around review workload, not developer convenience: over five thousand developers but only about 150 core maintainers reviewing most of the code, so he optimizes for reviewers. Right now there are about 473 Rust files, roughly 114,000 lines, six driver subsystems, about 0.38% of the kernel — growing fast but nowhere near the core. Then there's AI. The first patch people point to is Sasha Levin's, which kicked off the whole disclosure debate that became the AI kernel policy: you're responsible for the code, and no one's going to talk to your chatbot. Declared AI submissions have hit 16% of patches and climbing, with Torvalds calling AI-huge releases "the new normal" and the biggest RC6 in years. Kroah-Hartman says AI bug reports went from junk slop to legit overnight, spiking CVEs roughly 4x across a couple releases — not because the kernel is four times buggier, but because tools are poking at untouched drivers and finding real bugs. AI-touched code is closing in on a hundred thousand lines, around 4%, and the culling of old unmaintained drivers is happening faster than ever as maintainers drown in noise. Robertson's open question is what this means for the next generation of developers when AI is snapping up all the low-hanging fruit.

## 15. It’s impossible for Jev to be good — by Less Bitter
![Less Bitter](https://i.ytimg.com/vi/5Owg7p-61lY/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=5Owg7p-61lY
**Karakeep doc:** `tv7n2ddqjwz18dqfqqmxz8af`

The creator opens by claiming that if you've been doing things the right way, you don't even know what Jev is — the framing of a guy who "coinvented" ChatGPT and now wants to know why superhuman chat models haven't led to AGI. His answer, apparently, is a classification model. Not an LLM, not hype, just the kind of boring machine learning that existed before the current circus, except this one is general purpose enough to maybe matter.

He's got two questions. First, can Jev recommend a model as accurately as an actual software developer would? Second — and this is where it gets honest — is the thing any good? He's clear that it's fast and cheap, but speed and price are not quality, and nobody seems able to prove the quality part. There's a slop-detector demo floating around that flags AI-generated garbage in real time, and he immediately undercuts it: "this doesn't look like slop, to be honest," then shows a "groundbreaking new paradigm" press release that does. The slop meter, he concludes, is not accurate.

The deeper complaint is that Jev can't do web search and is trained on static data, so it doesn't know what half the modern tools even are. He cross-checks it against a competing model and gets the right answer out of the competitor while Jev picks medium effort for a task that needed high. His favorite line is the Anthropic researcher who said a model will "do your taxes now if you wanted to — it just won't do it correctly." That's the whole problem in one sentence: yes, it can classify, but is it doing it correctly, and how would you even measure that?

He lands on a modest verdict. The real use cases are self-contained things — shopping recommendations, email spam, anything living in a static training set — not trading decisions, where some guy put a classifier in charge and it's down thirty-one thousand dollars. Then, naturally, the entire video pivots into a pitch for his own app, "enjoy," which is apparently a desktop client that routes you to Claude Code, Codex, or Grok and lets you schedule fifteen-minute onboarding calls. The whole thing is a useful skepticism sandwich with an ad stuffed in the middle, and honestly the skepticism is the only part worth keeping.

### 9to5Linux (RSS)

## 16. MX Linux 25.3 “Infinity” Is Out with Linux Kernel 7.2, Based on Debian 13.7 — by 9to5Linux
![9to5Linux](https://9to5linux.com/wp-content/uploads/2026/09/mx253.webp)

**Source:** https://9to5linux.com/mx-linux-25-3-infinity-is-out-with-linux-kernel-7-2-based-on-debian-13-7
**Karakeep doc:** `b9ewowozxzcdj68nbpp4p5i4`

MX Linux just dropped its 25.3 "Infinity" point release, and if you've been on this Debian-based distro since November 2025, this is your routine `sudo apt update && sudo apt full-upgrade` moment. Four months after 25.2, this one rebases on Debian 13.7 "Trixie" and ships three flavors — Xfce, KDE Plasma, and Fluxbox — because apparently one desktop wasn't enough to argue over. 😏 The standard ISOs keep the long-term-support Linux 6.12 LTS kernel, while the Xfce AHS (Advanced Hardware Support) build now rides a Liquorix-flavored Linux 7.2 kernel for people whose GPUs are too new to be polite about it. Graphics-wise, AHS editions pull Mesa 26.1.4 backported from Debian Sid, so your shiny card stops pretending it's a potato. The release also sneaks in Siduction 7.x kernel support via the MX Package Installer, plus a new mx/gazelle-installer flag that sets lazytime in fstab by default — a tiny perf nicety most installers couldn't be bothered with. Tooling got a polish pass: MX Welcome, MX Tools, and custom-toolbox all got UI touch-ups, there's a new MX Theme Colors tool for rolling custom highlight themes from existing GTK themes, and a Verify-iso-sig utility that finally makes checking ISO signatures not a chore. Third-party VPN installers got their usual refresh, translations and FAQ entries were updated, and a pile of bugs got squashed. Honestly it's a maintenance release, not a revolution — the real headline is the "Infinity" series itself, which introduced dual SysVinit/systemd, deb822 sources, a Qt 6 port of MX Tools, and Wayland-by-default on KDE. If you want the new hotness, grab the ISO; if you're already on 25.x, just upgrade and get back to your day. 📦

## 17. NixOS-Based Garuda Linux Dr460nized and Mokka Editions Are Out Now — by Cloudflare
![Cloudflare](https://9to5linux.com/wp-content/uploads/2026/09/glnxos.webp)

**Source:** https://9to5linux.com/nixos-based-garuda-linux-dr460nized-and-mokka-editions-are-out-now
**Karakeep doc:** `d4qs88ugdnmwawbkk5oha8gg`

Garuda Linux — the Arch derivative best known for its heavily-themed KDE spins — has rebranded its NixOS subsystem as "Garuda Nix" and shipped NixOS-based editions of its two flagship layouts, Dr460nized and Mokka. The interesting part is the architecture: Garuda Nix lives as a NixOS installation in a subvolume alongside a Garuda install, installable directly from the live ISO via a Calamares-based installer, with a CLI (`install-garuda-nix`) for the extra options. You get Chaotic Nyx (the Nix counterpart of Chaotic-AUR), a starter flake in `/etc/nixos`, and the same opinionated dotfiles and module presets the Arch editions carry. The headline feature is one-click Impermanence — a NixOS module that wipes non-persisted state on every boot via Btrfs rollback or a tmpfs root on EXT4, which is the kind of setup that normally takes a long afternoon of config-fu to get right. Current ISOs ship KDE Plasma 6.7.5, Frameworks 6.30, Gear 26.08, and Linux kernel 7.2. The blunt caveat: these are explicitly pre-releases, and 9to5Linux flat-out says don't put them on production machines. Worth tracking if the NixOS-for-desktop itch is real, not worth daily-driving yet.

## 18. 9to5Linux Weekly Roundup: September 20th, 2026 — by 9to5Linux
![9to5Linux](https://9to5linux.com/wp-content/uploads/2026/09/wr310.webp)

**Source:** https://9to5linux.com/9to5linux-weekly-roundup-september-20th-2026
**Karakeep doc:** `fowlihnfkn2icqcmsevnjbtp`

The 310th installment of the 9to5Linux roundup covers the week ending September 20th, 2026, and the big ticket item is a major new GNOME release — GNOME 51 "A Coruña" — alongside the usual steady drum of software updates. Mozilla shipped Firefox 156 and pushed Firefox 157 into beta with a brand-new Nova design, Thunderbird 156 added custom OAuth support for POP3, and VirtualBox 7.2.18 landed with fixes for RHEL 10.3 kernels. DXVK 3.1.1 improved a handful of games including Skyrim SE, PipeWire 1.6.9 tightened Bluetooth and JACK support, and Calibre 9.15 introduced a "Create Your Own Adventure" writing game. On the distro side, MX Linux 25.3 "Infinity" arrived based on Debian 13.7, Clonezilla Live 3.3.3-37 and Raspberry Pi OS 2026-09-15 both dropped, and the post also previews Fedora Linux 45 and Ubuntu 26.10 ahead of their October releases. The post closes with a long download list covering everything from Linux kernel 7.2.6 through the LTS branches, plus FFmpeg 9.0.2, Mesa 26.2.3, Krita 6.0.4, and nginx 1.30.5. Next week: the Ubuntu 26.10 beta.

## 19. GNU Wget 2.3 Released with New Features, Improvements, and Bug Fixes — by 9to5Linux
![9to5Linux](https://9to5linux.com/wp-content/uploads/2025/12/wg221.webp)

**Source:** https://9to5linux.com/gnu-wget-2-3-released-with-new-features-improvements-and-bug-fixes
**Karakeep doc:** `h6k61poc5x8p7x8fep1tegbv`

GNU Wget 2.3 is out as the latest drop of the multithreaded successor to the classic downloader, and it's mostly a security-and-compatibility housekeeping release. Feature highlights include CSS conversion via `--convert-links`, iframe `srcdoc` and `data-src`/`data-srcset` handling, a new `--progress=dot`, header printing without downloading through `--spider`, and `Content-Length: 0` support for POST, PUT, and PATCH per RFC 9110. Bulk downloads can now resume with `-i` after an error, overly long filenames get truncated, and exit codes are reported correctly after failed retries. The security list is the meaty part: an integer overflow in cookie parsing, a stack overflow during recursive parsing of local files, XML recursion capped at 1024 levels, and cookies now only accepted over HTTPS. Content-Disposition path traversal got tightened with filenames sanitized down to their basename, and Metalink paths are scrubbed on Windows. The TLS backends all got attention — certificate purpose validation, GnuTLS now requiring 3.6.5+, OpenSSL post-handshake auth, and WolfSSL respecting `NO_OLD_TLS` with better OCSP checks. Wget1.x compatibility improved for `--directory-prefix`, `--accept`/`--reject`, and URL unescaping, and a pile of smaller fixes cover `--no-clobber`, `--page-requisites`, and the timeout options. The OS/2 port even got some love, plus a few memory leaks plugged. Grab the tarball from gnu.org or wait for it to hit your distro's repos.

## 20. openSUSE Tumbleweed ARM Updates Improve Raspberry Pi Support, Add Linux 7.2 — by 9to5Linux
![9to5Linux](https://9to5linux.com/wp-content/uploads/2021/01/ostarm.webp)

**Source:** https://9to5linux.com/opensuse-tumbleweed-arm-updates-improve-raspberry-pi-support-add-linux-7-2
**Karakeep doc:** `qr714zj8df99tnk11ofwtmjj`

The openSUSE Project pushed a fresh batch of updates to its Tumbleweed ARM port, headlined by the Linux 7.2.5 kernel alongside Glibc 2.44, QEMU 11.1.1, GIMP 3.2.6, and Shotwell 33.0 with its GTK4 port. Raspberry Pi owners get the most obvious wins: a fix for the spurious "-52" Wi-Fi scan error in raspberrypi-firmware and a memory leak patched in the brcmfmac driver's SDIO path, which should stop memory pressure creeping up on the onboard Cypress chip over long uptimes. Rockchip hardware sees kernel fixes for MediaTek Wi-Fi, including USB/SDIO headroom on mt7925 and EEPROM size validation on mt7915/mt7996 to guard against malformed device data. The Qualcomm side gains DSP firmware for the X1E-80-100 and QCS8300 SoCs, dracut adds the leds-qcom-lpg module so RGB indicator LEDs survive an initrd boot, and wireless-regdb flips on 320 MHz channels for Hong Kong while tidying South Africa's rules. NXP isn't forgotten either — QEMU gains the imx8mp-evk machine type, the mxs-dcp crypto engine gets a scatterlist fix, and the i.MX Data Co-Processor sees security improvements. Rounding it out, OVMF UEFI firmware is refreshed for AArch64 and sdbootutil picks up a status command and a `--repair` flag. Just update your ARM box and it all lands.

### Open-source Projects (RSS)

## 21. Plain text double-entry accounting that analyzes 25k transactions per second — by Open-source Projects
![Open-source Projects](https://opengraph.githubassets.com/1/hledgerorg/hledger)

**Source:** https://www.opensourceprojects.dev/post/aada5c2c-6f89-4152-b2d7-5b725bbdbb7cb
**Karakeep doc:** `wwbc7hdhsqat5h2o79rpsedh`
**GitHub:** https://github.com/hledgerorg/hledger

hledger is the plain-text accounting nerd's answer to the question "why does my money disappear," and it's been chugging along since 2013 with a solid 4.7k stars to show for it. It's a Haskell-built, GPL-3.0 licensed tool that does real double-entry bookkeeping from human-readable journal files — no database, no proprietary lock-in, just text you can diff and grep and shove into git. The headline flex is performance: it'll chew through 25,000 transactions per second, which matters when your ledger has accumulated a decade of shame. 🧾 It ships three interfaces in one box — a CLI for the masochists, a TUI for the efficient, and a web UI for people who want pretty charts of their spending — all reading the same plain-text format. It's part of the broader plain-text accounting movement (ledger-compatible, if you've ever touched John Wiegley's ledger), which means your financial history survives any app dying, because it's just a file. Topics cover the usual suspects: reports, budgeting, forecasting, balance sheets, and multi-currency. If you've been meaning to actually know where your money goes instead of vibing with a bank app that shows you three numbers and an emoji, this is the tool that makes accounting feel less like a spreadsheet prison and more like a version-controlled conscience. 💸

## 22. 自部署的 AI 投研助手，行情、对话和持仓都留在自己机器上 — by Open-source Projects
![Open-source Projects](https://opengraph.githubassets.com/1/agentpit-io/hunter-community)

**Source:** https://www.opensourceprojects.dev/post/1b2befe2-1eac-470b-ac6b-ba36a0d16028
**Karakeep doc:** `lxtc15tpsv8e8qtxpca6tpq8`
**GitHub:** https://github.com/agentpit-io/hunter-community

HunterCode Community Edition is a self-hosted, multi-agent investment research terminal aimed at A-shares, Hong Kong, and US markets — and it's explicitly pitched as an open-source, local alternative to Tencent's WorkBuddy Finance Edition. The whole selling point is in the name of the game: BYOK (bring your own key), your reasoning runs on *your* machine, and your positions never leave your hard drive. For anyone who's watched fintech SaaS quietly slurp up every trade and chat log, that privacy angle is the entire reason this exists. 📊 It's Python under the hood, Apache 2.0 licensed, deployed via docker compose, and it's built as a multi-agent system — MCP support, Claude Code/OpenCode integrations, and the usual "ai-hedge-fund / ai-quant" topic soup that means it'll fetch market data, run analysis agents, and keep the conversation and holdings local. At 543 stars in a few weeks it's clearly scratching an itch, especially for Chinese-market retail investors who want a WorkBuddy-like experience without handing their portfolio to a cloud they don't control. The BYOK + local-first combo is the real story here: you get the LLM-agent research loop without the data leak. If you're the kind of person who likes your trades, your prompts, and your positions staying on your own metal, this is worth a docker pull. 🏦

## 23. A jQuery-based replacement for select boxes, with search and remote data — by Open-source Projects
![Open-source Projects](https://opengraph.githubassets.com/1/select2/select2)

**Source:** https://www.opensourceprojects.dev/post/f6129ae9-572a-44e5-a193-c650d2648529
**GitHub:** https://github.com/select2/select2
**Karakeep doc:** `loxa48ujnsdv4t4oa5a5rdyw`

Select2 is a jQuery plugin that swaps your native `<select>` for a searchable, AJAX-fed, paginated dropdown. 25.9k stars, JavaScript, MIT, and still going after a decade. It does the stuff native selects refuse to: nested optgroups beyond one level, tagging new options on the fly, infinite scrolling of remote datasets, and custom templating for both results and selections. Theming is a real concern too — dedicated skins for Bootstrap 3/4/5 and Flat UI. Internationalization is just dropping in a language file. Browser support goes back to IE 8, which tells you exactly who this is for. The honest read: if you're greenfield on React or Vue, skip it and grab a proper component. If you're stuck maintaining a legacy jQuery codebase, this is the dropdown you want, and the plugin ecosystem (Django, Rails, Drupal, Meteor) means someone already did the wiring. Nothing exciting, nothing modern — just a tool that solved a recurring pain and never went away. Wojtek's verdict: respect it, don't reach for it in 2026.

## 24. A dual-pane macOS file manager with keyboard-driven navigation — by Open-source Projects
![Open-source Projects](https://opengraph.githubassets.com/1/mikekazakov/nimble-commander)

**Source:** https://www.opensourceprojects.dev/post/67c795af-5308-497b-839e-cfd15c0058ec
**GitHub:** https://github.com/mikekazakov/nimble-commander
**Karakeep doc:** `kmqat4406nqbe2xcn9z06tv8`

Nimble Commander is a dual-pane, keyboard-first file manager for macOS, written in C++ and GPL-3.0. 723 stars, but the copyright spans 2013 to 2026, so it's a slow-burn project rather than a flash in the pan. Two directory views side by side, source and destination always visible, and your hands never leave the keyboard — this is Norton Commander's ghost wearing a modern Mac skin. Install it with one Homebrew command, grab it from the Mac App Store as "Files Lite," or chase nightly builds off GitHub Actions. The whole point is learning the keybindings, and the help lives in the repo under `Docs/Help.md`. This one's aimed squarely at people who spend all day in a terminal or vim and find Finder's window-juggling drag-and-drop insulting. Wojtek's verdict: if you ever find yourself opening two Finder windows to move a file, this is a low-risk experiment with real payoff. Not a Finder replacement for everyone, and it doesn't pretend to be.

## 25. WUD watches your containers across Docker, Swarm, Kubernetes, and Nomad — by Open-source Projects
![Open-source Projects](https://opengraph.githubassets.com/1/getwud/wud)

**Source:** https://www.opensourceprojects.dev/post/8e0bcbad-d8f4-4f5e-9778-b05a7a2fcec6
**GitHub:** https://github.com/getwud/wud
**Karakeep doc:** `uhl7lk2bzm6mrvqnbc8pduhq`

WUD — "What's Up Docker?" — watches your containers across Docker, Swarm, Kubernetes, Compose, and Nomad, and tells you when images have updates. TypeScript, MIT, 3.9k stars. Watchers discover running containers, the engine compares versions and digests against public and private registries, and semantic-version analysis sorts a harmless patch from a breaking major bump. Then triggers either notify you (Discord, Slack, MQTT) or auto-update via Compose. Private OCI registries are first-class, and there's a web dashboard so you don't have to squint at logs. Runs as a container itself, `docker pull getwud/wud`. This is the one in the batch Wojtek should actually pay attention to — it replaces the cron jobs and shell scripts half of us bolted together to track image updates, and the optional-not-mandatory auto-update is the right call. For a homelab running arr-stack containers across mixed orchestrators, this is genuinely useful rather than just neat. Wojtek's verdict: worth a spin.

## 26. Write Markdown docs that ship with an AI assistant and MCP server — by Open-source Projects
![Open-source Projects](https://opengraph.githubassets.com/1/nuxt-content/docus)

**Source:** https://www.opensourceprojects.dev/post/307766a1-f0c1-4f1f-ac9d-66a333638b92
**GitHub:** https://github.com/nuxt-content/docus
**Karakeep doc:** `rfnk90an3c29woyegfx69xtx`

Docus is a docs framework on Nuxt 4, Nuxt UI 4, and Tailwind 4 that ships an AI assistant and an MCP server in the box. TypeScript, MIT, 3.1k stars. You write Markdown with MDC components and get a full site: dark mode, client-side search, SEO, sitemap, OG images. The interesting bit is the AI stack. Every site exposes an MCP server at `/mcp` — install it straight into Cursor, VS Code, or Claude and your docs become queryable from inside the editor, with source citations. It also generates `llms.txt`/`llms-full.txt`, and supports Agent Skills Discovery through a `skills/` directory served at `/.well-known/skills/`. Scaffolding is `npx create-docus my-docs` and you're live at localhost:3000. The MCP endpoint is the killer feature — zero server code for a working AI integration. Wojtek's verdict: if you're already in the Nuxt ecosystem or starting docs fresh and want AI without stitching five tools together, the MCP server alone justifies the look. For everyone else it's a clean answer to a problem most doc sites still ignore.

## 27. A Python debugger that records expression values and shows them after the function finishes — by Open-source Projects
![Open-source Projects](https://opengraph.githubassets.com/1/alexmojaki/birdseye)

**Source:** https://www.opensourceprojects.dev/post/5633d0d9-3668-484e-a06f-629d7c6c9bd0
**GitHub:** https://github.com/alexmojaki/birdseye
**Karakeep doc:** `kmrmw3tvehp24civwhhxebsy`

birdseye is a Python debugger that records expression values during a function call and lets you inspect them after it's already returned. 1.7k stars, MIT. You add an `@eye` decorator, run your code however you normally would — script, test, notebook cell — and view results in the browser. The standout trick is scrubbing through loops like a timeline: move back and forth across iterations and watch selected expressions change, instead of stepping line by line. Suppressed exceptions get highlighted too, even if something caught them further down — the exact 2 AM sanity-killer. Data structures expand but with capped length and depth, so it won't dump a 50k-element list into your browser. It fits tools you already use, and you can try it in the browser via futurecoder with zero setup. Wojtek's verdict: it's not replacing pdb or your IDE debugger, but it fills the gap those leave open — understanding what happened inside a function after it finished. If you debug loops or chase suppressed exceptions, this is a genuinely practical addition and the browser trial makes it free to test.

## 28. zg unifies ripgrep, BM25, and vector search behind one local-first interface — by Open-source Projects
![Open-source Projects](https://opengraph.githubassets.com/1/zvec-ai/zvec-grep)

**Source:** https://www.opensourceprojects.dev/post/c27b29b3-8488-4e28-98e6-a8ea3fd9f412
**Karakeep doc:** `he29uevrbehd51h4eqwvi44l`
**GitHub:** https://github.com/zvec-ai/zvec-grep

zvec-grep — packaged as `zg` — is a Rust CLI that sits on top of ripgrep, BM25 lexical scoring, and dense vector search, exposing all three behind a single local-first interface. The pitch is that you shouldn't need three separate tools to find a symbol by name, rank documents by keyword relevance, and surface semantically related snippets. It's barely two months old (first commit July 2026) and already at 3,635 stars with 218 forks, so the "one tool to rule code search" story is landing. It ships an MCP server out of the box, which is the interesting angle for Wojtek: instead of wiring ripgrep, a reranker, and an embedding model into an agent separately, `zg` is meant to be the single search backend an AI agent calls. Everything runs on-device — no cloud index, no API key — which matches the homelab preference for local-first tooling. Topics list `code-search`, `full-text-search`, `semantic-search`, and `ai-agents`, Apache-2.0 licensed. The obvious caveat is youth: the vector side in particular is still maturing, and the project's own framing ("built for humans and AI agents") is a bit broader than its current feature depth. Still, for a workspace with mixed search needs, it's worth a look before the ripgrep-plus-sidecar-embedding habit gets any more entrenched.

## 29. A Tailwind-based UI library built for heavy customization and eCommerce — by Open-source Projects
![Open-source Projects](https://opengraph.githubassets.com/1/vuestorefront/storefront-ui)

**Source:** https://www.opensourceprojects.dev/post/5fe7b455-860d-46c5-b5f7-39bfb076ef06
**Karakeep doc:** `aq5hl7n5d6exstji6fjxb30t`
**GitHub:** https://github.com/vuestorefront/storefront-ui

Storefront UI is Vue Storefront's component library, built for both React and Vue, aimed at people who need a fast, accessible, accessible storefront without hand-rolling every cart and product card. It's been around since early 2019 and sits at 2,524 stars and 462 forks, MIT licensed, with an active design-system layer on top of Tailwind so you can theme it without fighting the framework. The current version targets PWA-first eCommerce, which is the real differentiator: components are built assuming progressive web app constraints (offline, installable, performance budgets) rather than bolted on after the fact. It supports Vue 2 and Vue 3, and the React side has been steadily catching up. The caveat for Wojtek is scope — this is not a general-purpose UI kit like Radix or shadcn; it's opinionated toward storefront primitives (product tiles, checkout forms, cart state), so pulling it into a non-commerce project buys you a lot of irrelevant surface area. The accessibility and theming story is genuinely strong, and if any homelab project ever touches a storefront or a catalog-style UI, this saves real time over assembling Tailwind components by hand. Otherwise it's a well-built library you'll probably admire and not use.

## 30. A tiny fetch wrapper with an intuitive syntax — by Open-source Projects
![Open-source Projects](https://opengraph.githubassets.com/1/elbywan/wretch)

**Source:** https://www.opensourceprojects.dev/post/f1f38787-f70a-47a1-86d3-2ddf168864e8
**Karakeep doc:** `adi51ys18qorf2ut0vz1dj4h`
**GitHub:** https://github.com/elbywan/wretch

wretch is a fetch wrapper that's been quietly kicking around since 2017 and now has 5,176 stars on a 109-fork footprint — small surface, long pedigree. The entire sell is an ergonomic, chainable syntax that turns `fetch`'s boilerplate (headers, JSON encoding, status checks, retries) into one fluent call: `.get('/users').json()`, with middleware for auth, error handling, and request/response transformation. It's TypeScript, MIT, dependency-light, and works in both browser and Node, which is why it keeps showing up as the sane default for people who don't want Axios's weight or the bare fetch ceremony. The honest framing: wretch does not add features so much as it removes friction — no AbortController wiring, no manual `res.ok` checks, built-in retry and timeout handling. It has not had a major overhaul in a while (last push mid-2026), and it's effectively feature-complete rather than actively growing, which is either a bug or a feature depending on how much churn you like in a dependency. For Wojtek, this is the kind of tool that replaces ad-hoc `fetch` boilerplate scattered across small scripts and agent glue, and its stability is exactly why you'd trust it in that role.

### LinuxLinks (RSS)

## 31. disk-encryption-tool - encrypt existing Linux storage with LUKS — by LinuxLinks
![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2018/09/Encryption.jpg)

**Source:** https://www.linuxlinks.com/disk-encryption-tool-encrypt-existing-linux-storage/
**Karakeep doc:** `cspuzkvw5rumrlimifl5zldh`
**GitHub:** https://github.com/openSUSE/disk-encryption-tool

Here's a tool for the classic "I installed my whole system unencrypted and now I regret it" situation, because re-installing to get LUKS is for quitters. disk-encryption-tool is a Bash command-line utility from the openSUSE folks that converts existing unencrypted storage to LUKS encryption *in place*, using cryptsetup's reencrypt functionality instead of making you copy everything onto a freshly encrypted volume. That's the whole trick — no backup-to-new-drive dance, just shrink, encrypt, expand. Btrfs filesystems get special handling so they're temporarily reduced before encryption and expanded back after, and swap partitions are supported too, UUID preserved where possible. 🔐 It'll auto-generate an enrollment key if you don't hand it one, stash keys in the kernel keyring for multi-disk operations, and write the resulting config to /etc/crypttab. The sneaky-clever part is the dracut module: it can carry out encryption *during early boot*, so you can deploy machines unencrypted and have them encrypt themselves before normal operation starts — which pairs neatly with Combustion-based provisioning. You can even encrypt multiple specified partitions at boot and drive the whole thing with systemd credentials. MIT licensed, written in Bash, so it's readable if a bit hairy. If you've been putting off disk encryption because the reinstall looked like a weekend project, this is the "just do it in place" answer. 🛡️

## 32. pycalphad - computational thermodynamics and phase equilibria - LinuxLinks — by LinuxLinks
![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/Chemical-Engineering-banner.png)

**Source:** https://www.linuxlinks.com/pycalphad-computational-thermodynamics-phase-equilibria/
**Karakeep doc:** `c0i0f0f2tcyh9mi5tordyhxi`
**GitHub:** https://github.com/pycalphad/pycalphad

pycalphad is a Python framework for computational thermodynamics built on the CALPHAD method — the workhorse technique for predicting phase stability and equilibria in multi-component materials systems. It reads Thermo-Calc TDB database files, reconstructs the underlying thermodynamic models as mathematical objects, and then solves the multiphase Gibbs-energy-minimization problem to figure out which phases are stable and in what composition, across ranges of temperature, pressure, and composition. Beyond binary phase diagrams, it handles ternary diagrams, phase fractions, chemical potentials, activities, heat capacities, metastable states, and driving forces. The project has been around since 2014, currently at 409 stars and 139 forks, MIT licensed, maintained by Richard Otis and Brandon Bocklund. The real value proposition is programmability: results come back as structured data that plugs straight into NumPy and xarray, and the model-construction machinery is exposed so researchers can implement or tweak models instead of treating the engine as a black box — which is what makes it a tool for high-throughput screening rather than a point-and-click phase-diagram app. For Wojtek this is firmly curiosity territory unless materials science is a hidden interest, but as an example of a mature, non-AI scientific Python project it's a useful contrast to the search-wrapper hype elsewhere in this digest.

## 33. 8 Best Free and Open Source C Static Site Generators — by LinuxLinks
![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/10/SSG-2.png)

**Source:** https://www.linuxlinks.com/best-free-open-source-c-static-site-generators/
**Karakeep doc:** `rh6expesc9tenug58ldoym59`

Static site generators prebuild every HTML page before anything gets uploaded, so pages load instantly and the server does almost no work per request. LinuxLinks makes the case that a full static site beats a dynamic one on several axes: a smaller software stack means a smaller attack surface, no database queries to chew through on each visit, and everything is trivially exportable and versionable with Git. The obvious catch is that you lose any runtime interactivity, but for documentation and blogs that tradeoff is usually fine. This roundup collects eight generators written in C, each profiled with its own portal page and feature breakdown. The headline entry is blogc, a blog compiler that slots into make-based workflows; sblg merges XML articles with templates several ways, while mkws leans on sh itself as a templating language. Kevlar bills itself as batteries-included and zero-dependency, swege drives the Discount library to turn Markdown into a site, and Bonobo and bloggy both aim for deliberate minimalism. Housecat rounds out the list with an intentionally simple interface. It is a niche list, but if you want a fast single-binary site tool without a JavaScript runtime in sight, these are the options.

**GitHub:** https://github.com/blogc/blogc

**Projects:**

- **[blogc](https://blogc.rgm.io/)** — Blog compiler that's compatible with make
- **[sblg](https://kristaps.bsd.lv/sblg/)** — Static blog utility merging XML articles and templates in a number of ways
- **[Housecat](https://github.com/mortie/housecat)** — Static site generator with an intentionally simple interface
- **[mkws](https://web.archive.org/web/20260729100717/https://mkws.sh/)** — Simple static site generator using sh as a templating language
- **[Kevlar](https://github.com/Aadv1k/kevlar)** — Batteries-included zero-dependency static site generator
- **[swege](https://github.com/sakhmatd/swege)** — Uses the Discount library to build a website from a set of Markdown files
- **[Bonobo](https://github.com/rockhardandrew/bonobo)** — Deliberately lightweight static blog generator
- **[bloggy](https://github.com/hogsy/bloggy)** — Minimalist static site generator

## 34. Pharos – static binary analysis framework — by LinuxLinks
![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2022/04/vulnerability_03_Converted_Converted_.jpg)

**Source:** https://www.linuxlinks.com/pharos-static-binary-analysis-framework/
**Karakeep doc:** `mxqyuzn3xc3b90zydwh4pive`

Pharos is a static binary analysis framework from Carnegie Mellon University's Software Engineering Institute, aimed at automated analysis of compiled programs and research into binary-analysis techniques. It is not a graphical reversing GUI; it is a toolkit that sits on top of the ROSE compiler infrastructure for disassembly, instruction semantics, and control-flow analysis, then layers specialized tools on top of that. APIAnalyzer finds sequences of API calls with specific data and control relationships, which is how you spot OS-interaction patterns buried in a binary. OOAnalyzer recovers object-oriented constructs from executables, tracking object pointers between functions and using Prolog rules to rebuild members and methods. CallAnalyzer reports the statically determined parameters passed to API calls, and FN2Yara turns matched functions into YARA signatures for similarity detection, while FN2Hash computes hashes and descriptive properties per function. It also throws in experimental path analysis and multi-threaded workloads. Written in C++ and released under a BSD license, this sits alongside Ghidra, Radare2, and Cutter as the automation-first cousin of the reverse-engineering family.

**GitHub:** https://github.com/cmu-sei/pharos

## 35. 15 Best Free and Open Source Mind Mapping Software — by LinuxLinks
![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2019/02/mind-mapping-ideas-work-with-person-thinking.jpg)

**Source:** https://www.linuxlinks.com/free-mind-mapping-software/
**Karakeep doc:** `bxjgquzih2kwipvx0mr0qdbx`

Mind mapping takes an unstructured problem and forces a framework onto it, which is precisely why the software you pick has to bend to your style rather than the other way around. This roundup makes the case that a map crams a lot of complex content into a tiny space and pushes you to think both logically and creatively at once, so you stop juggling flat lists and start linking ideas in genuinely different ways. The list of fifteen spans the whole spectrum from heavyweight desktop apps to pure-terminal tools. Freeplane and FreeMind are the classic cross-platform workhorses for creating and analyzing maps, while View Your Mind and Heimer lean on Qt. Drawnix is an all-in-one whiteboard, and Minder sells itself on easy customization. On the text side, markmap and myMarkmap build interactive maps straight from Markdown, h-m-m and tmmpr render maps right in the terminal, and Semantik turns maps into finished documents. For teams there is TeamMapper and WiseMapping as web-based collaborative options, plus Mindolph for personal knowledge management with Gen-AI support. TreeSheets rounds it out as a free-form data organizer.

**GitHub:** https://github.com/freeplane/freeplane

**Projects:**

- **[View Your Mind](https://github.com/insilmaril/vym)** — Excellent tool to generate and manipulate maps
- **[Freeplane](https://docs.freeplane.org/)** — Create and analyze mind maps
- **[Drawnix](https://github.com/plait-board/drawnix)** — All-in-one whiteboard for diagrams, mind maps and freehand drawing
- **[Minder](https://github.com/phase1geo/Minder)** — Easy-to-use, and highly customizable way of organizing thoughts
- **[markmap](https://github.com/markmap/markmap)** — Build mindmaps with plain text
- **[h-m-m](https://github.com/nadrad/h-m-m)** — Create mind maps in the terminal
- **[Semantik](https://waf.io/semantik.html)** — Produce complicated documents very quickly and efficiently
- **[FreeMind](https://freemind.sourceforge.io/wiki/index.php/Main_Page)** — Visualise ideas, projects, brainstorming, concepts, internet research
- **[Heimer](https://github.com/juzzlin/Heimer)** — Simple cross-platform mind map and note-taking tool written in Qt
- **[Mindolph](https://github.com/markmap/markmap)** — Personal knowledge management software with Gen-AI support
- **[TeamMapper](https://github.com/b310-digital/teammapper)** — Collaborative web app for creating and sharing mind maps
- **[WiseMapping](https://github.com/wisemapping/wisemapping-open-source/)** — Web-based mind mapping tool
- **[tmmpr](https://github.com/tanciaku/tmmpr)** — Terminal mind mapper
- **[myMarkmap](https://github.com/eyssette/myMarkmap)** — Create interactive mind maps directly from Markdown
- **[TreeSheets](https://github.com/aardappel/treesheets)** — Free-form hierarchical data organizer

## 36. Kairos – immutable Linux meta-distribution for edge and cloud — by LinuxLinks
![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/04/Linux-Distributions.png)

**Source:** https://www.linuxlinks.com/kairos-immutable-linux-meta-distribution-edge-cloud/
**Karakeep doc:** `mxdges8s81yuz7m8uzicqz61`

Kairos is an immutable Linux meta-distribution aimed at edge, cloud, and bare-metal deployments, and its core trick is that it wraps a supported distro into an image-based system with one shared install, upgrade, and recovery model. It ships complete operating system images as OCI containers and supports atomic A/B upgrades with rollback and a dedicated recovery system, so a bad update is a reboot away from being undone. Hadron is the default base for official images, but Alpine, Debian, Fedora, openSUSE, Rocky Linux, and Ubuntu can all be used underneath. Kubernetes is optional, with k3s and k0s supported, and it handles cloud-init, automated and zero-touch provisioning, Secure Boot, measured boot, and full-disk encryption. It runs on both x86-64 and ARM64, with init handled by systemd or OpenRC depending on the base and package management left to whatever distro sits underneath. There is no desktop environment — this is a fleet and infrastructure play, not a daily driver. If you want the immutability of an appliance image without being locked to a single distro, Kairos is the layer that unifies them all.

**GitHub:** https://github.com/kairos-io/kairos

## 37. Mimic - manage default applications and file associations — by LinuxLinks
![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2022/06/170y-utilities.jpg)

**Source:** https://www.linuxlinks.com/mimic-manage-default-applications-file-associations/
**Karakeep doc:** `w9mnxdsb9cgbe5ez419n53v1`

**GitHub:** https://github.com/ArijanJ/Mimic

Mimic is a GTK4/Libadwaita GUI for the thankless chore of managing default applications and MIME type associations, the kind of thing most people only discover exists when a `.pdf` opens in the wrong program. It exists so you never have to hand-edit `mimeapps.list` again, which is a mercy because that file format was clearly designed by someone who hated future you. The app offers two directions of attack: browse installed applications and see what file types each claims, or browse MIME types grouped into sensible categories (audio, images, text, video, fonts, models) and pick what should open them. Along the way you can set defaults, add new associations, and strip out custom ones you no longer want. It actually distinguishes between the four flavors of defaults — application-provided, custom, system-wide, and desktop-specific implicit defaults — which is more nuance than most desktops expose anywhere. It searches by application name or executable, and by MIME identifier or a human-readable description, so you are not memorizing `application/vnd.ms-excel`. It handles applications backed by multiple `.desktop` files and duplicate default entries, both of which trip up the manual approach constantly. Changes are written through a temporary file before the existing config is replaced, so a half-finished edit does not leave your system in a weird state. Keyboard shortcuts for search and for flipping between the app and file-type views round it out. Written in Python, GPL v2, by Arijan J. If your distro's settings panel already does this passably, Mimic is overkill — but if you have ever stared at a broken association and cursed, this is the tool that fixes it without a text editor.

## 38. ZSvirt - virtualization platform for managing KVM-based infrastructure — by LinuxLinks
![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2017/12/hypervisors.jpg)

**Source:** https://www.linuxlinks.com/zsvirt-virtualization-platform/
**Karakeep doc:** `dhpvdj5suuzf3tu4m3h7qhmb`

**GitHub:** https://github.com/ZSvirt/zsvirt

ZSvirt is a KVM virtualization management platform — think Proxmox's less-famous cousin — that puts virtual machines, physical hosts, clusters, networking, and storage under one web interface. KVM does the heavy lifting; ZSvirt layers the orchestration on top. Admins get the full lifecycle: create and manage VMs, images, volumes, and snapshots, spin up virtual networks and security groups, and clamp down access with permissions and quotas. Monitoring, alarms, events, and auditing are baked in rather than bolted on, which is the difference between a toy and something you could actually run a rack on. For automation it ships REST APIs, command-line tools, Terraform integration, and SDKs, and there is VMware migration tooling for people trying to escape the licensing bill. The architecture is modular and plugin-based, with asynchronous processing, workflows, and stateless services in the management layer — the sort of design that survives scale instead of melting under it. It is aimed squarely at servers, datacentres, and private clouds, not desktop virtualization, so do not expect a friendly little VirtualBox replacement. Written primarily in Java, GPL v3, by the ZSvirt project. If you are already on Proxmox or oVirt, this is not going to yank you away overnight, but as an open, Terraform-friendly KVM manager it is a legitimate option rather than a weekend curiosity.

## 39. Scrobblet - lightweight self-hosted music scrobbler — by LinuxLinks
![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/04/musical_notes_700x350-c.png)

**Source:** https://www.linuxlinks.com/scrobblet-lightweight-self-hosted-music-scrobbler/
**Karakeep doc:** `h9dqjf98asmnbzg4sm4nkgzw`

**GitHub:** https://github.com/degeens/scrobblet

Scrobblet is a self-hosted music scrobbler built around service APIs instead of a desktop media player plugin, which means it tracks your listening no matter what device actually plays the music. Play on your phone, laptop, or a Spotify-connected speaker, and Scrobblet runs separately on a server or always-on box, pulling playback activity straight from Spotify's API. That decoupling is the whole point — you stop caring which client is doing the playback. It pushes scrobbles to Last.fm, ListenBrainz, Maloja, and Koito, and it can fan out to multiple targets at once instead of locking you to one service like most scrobblers do. There is CSV output for anyone who wants a local, greppable record of their listening history. It broadcasts now-playing alongside completed tracks, and uses adaptive polling so it queries often while music is playing and eases off during silence, which is the kind of small mercy that keeps a daemon from being a battery and bandwidth hog. For the self-hosting crowd it ships structured JSON logging, Prometheus-compatible metrics, and a health endpoint, so you can watch it from Grafana like every other process in the rack. Deployment is container-friendly, with config and auth stored outside the image. The source-and-target design is deliberately modular so adding integrations is straightforward. Written in Go, GPL v3, by Stijn (degeens). If you scrobble from a single desktop app, this is overkill — but if your listening sprawls across devices and you want one daemon feeding every service, Scrobblet is exactly the shape of tool that fixes it.

## 40. Coot - macromolecular model-building and crystallography toolkit — by LinuxLinks
![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/Molecular-Editors-banner.png)

**Source:** https://www.linuxlinks.com/coot-macromolecular-model-building-crystallography-toolkit/
**Karakeep doc:** `zp7v8f01skyzwacq1zzdg7q3`
**GitHub:** https://github.com/pemsley/coot

Coot is an interactive molecular graphics application for building, refining, and validating macromolecular models — the kind of tool you reach for when you need to actually fix a structure, not just stare at it. It's built for structural biology workflows where atomic models get inspected and adjusted against experimental density, and it goes well beyond passive viewing: it gives you tools to select and edit regions, fit models to density, work with ligands, and check model quality through the whole iterative correct-and-validate loop. Under the hood it leans on GTK for the interface, OpenGL for graphics, and the established crystallographic libraries MMDB and Clipper. It handles macromolecular crystallography and also supports cryo-EM density maps, so it's not stuck in one corner of the field. A key selling point is the breadth of the model-building workflow, plus scripting facilities for automating the grunt work. It's free and open source, GPL v3, written primarily in C++, and developed by Paul Emsley. If your day involves chasing a misbehaving loop through density, this is the hammer you want.

## 41. BandOpticon Geo - visualise worldwide ham radio activity - LinuxLinks — by LinuxLinks
![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/04/006-satellite.png)

**Source:** https://www.linuxlinks.com/bandopticon-geo-visualise-worldwide-ham-radio-activity/
**Karakeep doc:** `hy94d9o37x0i07lped1bkjzf`
**GitHub:** https://github.com/G1OJS/BandOpticon

BandOpticon is a browser-based amateur radio visualization tool that turns PSKReporter reception reports into live geographic maps of activity across multiple bands and modes at once. Instead of staring at one band at a time, you get a carousel of map tiles so you can compare how far activity is reaching across the spectrum with a single glance, then open a bigger band-detail map for a closer look. It runs entirely client-side in JavaScript, so there's no desktop program to install — point a browser at it and go. The point isn't pretty maps; it's understanding propagation, comparing how well different stations perform, and spotting reciprocal paths that might actually support a QSO. The feature list is genuinely thoughtful: it distinguishes transmit-only, receive-only, and both-way stations by color, can highlight only connections involving a specific callsign, can color connections by home callsign to compare reach, and can restrict lines to reciprocal paths where both stations actually hear each other. It auto-zooms to activity, offers rectangular and azimuthal equidistant projections, and discovers bands and modes from incoming data rather than leaning on a fixed predefined display. Mobile-friendly, loads fast, small control set. It's free and open source, MIT-licensed, written in JavaScript by the operator behind the G1OJS callsign.

## 42. 36 Best Free and Open Source Linux GUI Time Tracking Software — by LinuxLinks
![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/08/022-hurry.png)

**Source:** https://www.linuxlinks.com/timetracking/
**Karakeep doc:** `bfiuoxx2n6h57axd2g97ytt0`

LinuxLinks rounds up thirty-six free and open source GUI time trackers for Linux, all with a ratings chart, and explicitly excludes terminal-only tools (those get their own separate roundup). Time tracking here means recording hours per task so you can bill clients, generate invoices, and measure productivity — the usual use case for accountants, solicitors, and freelancers who charge by the hour. The list runs from todo-plus-timeboxing apps to straight Pomodoro timers and passive trackers. Super Productivity is the todo app with timeboxing, ActivityWatch watches what you do automatically, and Kimai is web-based work-time classification. solidtime adds projects, tasks, and reporting. Tockler tracks time by monitoring your active window title. Then there's the Pomodoro crowd — Pomotroid, Pomodorolm, Focus Timer, Flowkeeper, Samaya, Pomolin, zomodoro, Solanum, and KTeaTime (a timer that is literally for steeping tea). GNOME users get Project Hamster, Time Tracker, Timetrack, and TimeIT. Toggl Desktop is the client for the Toggl service, Time Cop bills itself as privacy-respecting, and there are oddballs like Rachota, Khronos, dotProject, Kapow, and HPR that tracks offline activity. It is a directory piece, not a deep review, so each entry is a pointer to a fuller LinuxLinks page. If you need to know how long you spent staring at a terminal instead, that is another article entirely.

**Projects:**

- **[Super Productivity](https://github.com/super-productivity/super-productivity)** — Todo app with timeboxing & time tracking capabilities
- **[ActivityWatch](https://github.com/ActivityWatch/activitywatch)** — Automated time tracking application
- **[Kimai](https://www.kimai.org/en/)** — Web based software that tracks work time, and classifies it
- **[solidtime](https://github.com/solidtime-io/solidtime)** — Modern time tracking with projects, tasks, and reporting
- **[Pomotroid](https://github.com/Splode/pomotroid)** — Simple and visually-pleasing Pomodoro timer
- **[Project Hamster](https://github.com/projecthamster/hamster)** — Time tracking applet for the GNOME desktop environment
- **[Time Tracker](https://github.com/elvishcraftsman/time-tracker)** — Simple time-tracker program for GNOME
- **[Time Cop](https://github.com/hamaluik/timecop)** — Billed as a time tracking app that respects your privacy
- **[Tockler](https://github.com/MayGo/tockler)** — Tracks time by monitoring your active window title
- **[Task Coach](https://github.com/taskcoach/taskcoach)** — Designed to deal with composite tasks
- **[dotProject](https://github.com/dotproject/dotProject)** — Web-based, multi-user, multi-language project management application
- **[KTimetracker](https://apps.kde.org/en-gb/ktimetracker/)** — Todo management and time tracking application
- **[Kapow](https://gottcode.org/kapow/)** — Punch clock program designed to track time
- **[Pomodorolm](https://github.com/vjousse/pomodorolm)** — Simple, good looking and configurable pomodoro tracker with tray icon
- **[Focus Timer](https://github.com/focustimerhq/FocusTimer)** — Pomodoro timer for structured focus and break sessions
- **[Timetrack](https://flathub.org/apps/org.gnome.Timetrack)** — Simple timetrack app for GNOME
- **[Flowkeeper](https://flowkeeper.org/)** — Pomodoro Technique desktop timer
- **[Valot](https://gitlab.com/valot/app/valot)** — Modern time tracking application
- **[Furtherance](https://github.com/unobserved-io/Furtherance)** — Track your time
- **[TimeSlotTracker](https://github.com/TimeSlotTracker/timeslottracker-desktop)** — Java based time tracking tool
- **[Play Timer](https://github.com/efogdev/mpris-timer)** — Native-feeling timers
- **[Flowtime](https://github.com/Diego-Ivan/Flowtime)** — Spend your time wisely
- **[Samaya](https://codeberg.org/lockedmutex/samaya)** — Minimalist Pomodoro timer for your desktop
- **[Baralga](https://baralga.github.io/)** — Simple and lightweight time tracking
- **[TimeIT](https://hoglet.github.io/TimeIT/)** — Unobtrusive time tracker
- **[dxtime](https://dxtime.dxsolutions.org/)** — Small program for time tracking using wxWidgets, wxSQLite, and SQLIte3
- **[Sessions](https://github.com/pojntfx/sessions/)** — Focus with timed work intervals
- **[Pomolin](https://github.com/lockedmutex/Pomolin)** — Minimalist Pomodoro timer
- **[zomodoro](https://github.com/zeroproject-dev/zomodoro)** — Simple pomodoro made with Qt
- **[Toggl Desktop](https://toggl.github.io/toggldesktop/)** — Toggl time tracking client
- **[Solanum](https://apps.gnome.org/Solanum/)** — Balance working time and break time
- **[Rachota](https://github.com/Rachota/rachota)** — Designed for personal timetracking of projects
- **[KTeaTime](https://invent.kde.org/utilities/kteatime)** — Timer for steeping tea
- **[Khronos](https://github.com/lainsce/khronos)** — Simple tool to let you track the time spent on a task
- **[HPR](https://github.com/plexescor/HPR)** — Automatically tracks offline computer activity
- **[Charm](https://github.com/KDAB/Charm)** — Cross-platform software for professionals

## 43. 18 Best Free and Open Source Linux Web Servers - LinuxLinks — by LinuxLinks
![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/09/web-design-concept-with-drawings.jpg)

**Source:** https://www.linuxlinks.com/best-free-open-source-web-servers/
**Karakeep doc:** `kvd27tz563wcyjjshb9gk77z`

LinuxLinks does what it always does: a numbered roundup with a ratings chart and zero pretension. This time it's web servers, and the verdict is about as surprising as finding water in the ocean. [nginx](https://www.linuxlinks.com/nginx/) and [Apache](https://www.linuxlinks.com/apache-http-server/) still run the internet, and LinuxLinks admits it flipped its allegiance from Apache to nginx years ago because nginx wins the benchmark fights, especially on static content and high-concurrency workloads.

The rest of the 18 reads like a tour of "things you've vaguely heard of." [Caddy](https://www.linuxlinks.com/caddy-powerful-enterprise-ready-open-source-web-server/) gets a nod as the Go-based one that auto-provisions HTTPS, which is genuinely the only reason most hobbyists bother with it. [lighttpd](https://www.linuxlinks.com/lighttpd/) holds the "low memory footprint" crown for the embedded crowd, [OpenLiteSpeed](https://www.linuxlinks.com/openlitespeed-http-server/) is the free version of the thing people pay money for, and [Angie](https://www.linuxlinks.com/angie-web-server/) is the nginx fork born out of that whole licensing drama a while back.

Then there's the deep cuts: Lwan, H2O, Tengine, Ferron, CivetWeb, Algernon, Yaws, Hiawatha, rwasa, devd, and Cherokee. Some of these are actual production tools, some are experiments someone abandoned in 2016, and LinuxLinks is generous enough to list them all with a straight face. Node.js sneaks in at the end despite the author admitting it's "frequently not categorised as a web server," which is the polite way of saying "we needed to pad the list."

The chart is the usual LinuxLinks flourish — a colorful PNG that ranks everything without ever explaining its methodology beyond vibes. It's a perfectly fine reference if you're picking a web server, and a perfectly useless one if you already run nginx, because you've already made the only decision that matters.

**Projects:**

- **[nginx](https://nginx.org/)** — Very powerful and efficient web server powering the top web sites
- **[Apache](https://httpd.apache.org/)** — Like nginx, Apache is a hugely popular web server
- **[Caddy](https://caddyserver.com/)** — Powerful, enterprise-ready web server written in Go
- **[Lwan](https://lwan.ws/)** — Experimental, scalable, high performance HTTP server
- **[H2O](https://h2o.examp1e.net/)** — Optimized HTTP/1.x, HTTP/2, HTTP/3 server
- **[Tengine](https://github.com/alibaba/tengine)** — Distribution of nginx
- **[lighttpd](https://www.lighttpd.net/)** — Fast, compliant and very flexible low memory footprint web server
- **[Ferron](https://ferron.sh/)** — Web server optimized for speed, security and efficiency
- **[CivetWeb](https://github.com/civetweb/civetweb)** — Small embeddable web server library written in C
- **[Angie](https://en.angie.software/?ra=yes)** — Scalable web server that was forked from nginx
- **[Algernon](https://github.com/xyproto/algernon)** — Small self-contained pure-Go web server
- **[Node.js](https://nodejs.org/en)** — Server-side JavaScript environment for network applications
- **[Yaws](https://github.com/erlyaws/yaws)** — High-performance web server written in Erlang
- **[Hiawatha](https://hiawatha.leisink.net/)** — Web server that focuses on security
- **[OpenLiteSpeed](https://github.com/litespeedtech/openlitespeed)** — Lightweight HTTP server
- **[rwasa](https://2ton.com.au/rwasa/)** — Full-featured high performance web server
- **[devd](https://github.com/cortesi/devd)** — Local web server for developers
- **[Cherokee](https://cherokee-project.com/)** — Fast, flexible and embeddable web server

## 44. OBLinux - Desktop distribution with Arch and Debian editions - LinuxLinks — by LinuxLinks
![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/04/Linux-Distributions.png)

**Source:** https://www.linuxlinks.com/oblinux-desktop-distribution-arch-debian-editions/
**Karakeep doc:** `scw6vrmqdbn7nhp6mjbhh7fk`
**GitHub:** https://github.com/marcoobaid/oblinux

OBLinux is one of those distros that exists because someone decided "what if I just made my own, but with a GNOME on top of somebody else's base?" The twist is that it ships two editions — one on Arch's rolling release, one on Debian's frozen-and-conservative foundation — both wearing the same OBLinux branding and the same GNOME desktop. It's the "choose your own stability" approach, and honestly it's not a terrible pitch if you can't decide between bleeding edge and boring.

The feature list is the standard distro checklist: Calamares installer, live boot, a curated app collection, multimedia support, UEFI and legacy BIOS, SHA-256 checksums for the paranoid. Broad hardware compatibility is "kept in mind," which in distro-speak means "we tested it on our own laptop and it worked." The package managers split by edition — Pacman on the Arch side, APT on the Debian side — so you get the ecosystem of whichever base you picked without the pain of configuring it yourself.

LinuxLinks filed this under its Big List of Active Linux Distributions, and the fine print reveals the whole thing was "written with the assistance of a visitor who completed the distro form." Which is to say: someone made a distro, submitted it to a directory, and now it has an entry. The home page is oblinux.com and the repo sits on GitHub under marcoobaid.

Will this dethrone anything? No. Is it a perfectly reasonable GNOME desktop for someone who wants Arch or Debian pre-arranged? Sure. That's the honest ceiling for most of these projects, and OBLinux doesn't pretend otherwise.

## 45. AmpForge - guitar amp simulator and effects processor - LinuxLinks — by LinuxLinks
![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/09/guy-playing-acoustic-guitar.jpg)

**Source:** https://www.linuxlinks.com/ampforge-guitar-amp-simulator-effects-processor/
**GitHub:** https://github.com/Loursy/AmpForge
**Karakeep doc:** `x4yrzuuocedno6s0v7rjeut1`

AmpForge is a C++ guitar amp simulator and multi-effects processor built around a single internal pedalboard rather than a pile of separate plugins. The whole signal chain — gate, compressor, wah, overdrive, distortion, amp, cabinet, modulation, delay, reverb — lives in one graphical rack where you add, bypass, and reorder pedals directly. That's a deliberate design choice against the plugin-soup approach most Linux guitar tools fall into.

The amp stage offers Modern, Vintage, Crunch, and Hi-Gain voicings with distinct clipping characteristics, and there's cabinet impulse-response convolution for speaker emulation. It also loads Neural Amp Modeler capture files as a dedicated block, which means it'll play nicely with the NAM capture ecosystem that's become the de facto standard for profiling real amps. A genuinely useful twist: the amp and cabinet stages can be switched off, leaving a vocal chain of pitch correction, de-esser, doubler, harmonizer, and exciter. So it's not just a guitar tool. Ships as VST3, LV2, and CLAP plus a standalone app over JACK or PipeWire. GPL v3, single developer (Atakan Ünsever). If you run Linux and want one window instead of a patchbay of plugins, this is the closest thing to a proper competitor to Guitarix with a modern UI.

## 46. bom - create, view and transform Software Bills of Materials - LinuxLinks — by LinuxLinks
![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/SBOM-Tools-banner3.png)

**Source:** https://www.linuxlinks.com/bom-create-view-transform-software-bills-materials/
**GitHub:** https://github.com/kubernetes-sigs/bom
**Karakeep doc:** `etv8dpfhxjgps4fed73gpodp`

`bom` is a Go command-line multitool for generating and inspecting Software Bills of Materials, born out of the work Kubernetes SIGs did to produce an SBOM for Kubernetes itself. It's SPDX-native and can build an inventory from several source types at once: raw files, whole directories, Docker image archives, and container images pulled straight from a remote registry. That last bit is the practical core — point it at an image and it scans the layers for packages rather than trusting a manifest someone hand-wrote.

Beyond generation it's also a query tool: it dumps the structural outline of an existing SPDX doc, extracts specific information, and exports as in-toto provenance attestation — the format that plugs into supply-chain integrity systems. A built-in classifier recognizes 400+ SPDX licenses, and it honors .gitignore rules when scanning repos, with extra regex exclusions and an offline mode for air-gapped builds. Apache 2.0. The appeal is that it's one general-purpose binary instead of the grab-bag of bespoke per-project generators that's become the norm. If you're on the hook for SBOM compliance — and if you ship to enterprise or government customers, you increasingly are — this replaces half a dozen one-off scripts.

## 47. Capstone – multi-architecture disassembly framework - LinuxLinks — by LinuxLinks
![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/12/117-security.png)

**Source:** https://www.linuxlinks.com/capstone-multi-architecture-disassembly-framework/
**GitHub:** https://github.com/capstone-engine/capstone
**Karakeep doc:** `hyrrne8da5rxx3epg1gb56pn`

Capstone is the disassembly engine that sits under most serious reverse-engineering and binary-analysis tooling — not a full interactive analyzer like Ghidra or radare2, but the C library those tools and a thousand custom scripts call when they need raw machine code decoded. Its selling point is one architecture-neutral API over an enormous spread of targets: x86 in 16/32/64-bit modes, ARM and AArch64, MIPS, PowerPC, RISC-V, SPARC, SystemZ, plus the long tail — Alpha, BPF, M68K, SH, TriCore, Xtensa, and WebAssembly.

For each decoded instruction it returns the operands in detail, reports implicit registers read and written, and exposes semantic info higher-level analyses can use. It's thread-safe, compact enough to embed in firmware and OS kernels, and offers reduced-footprint builds for constrained targets. Language bindings cover Python, C#, Java, Go, Rust, Ruby, Lua, and more, backed by heavy fuzzing. BSD 3-Clause, maintained by Nguyen Anh Quynh and contributors. The reason it's still relevant a decade-plus in: it's the one component every binary tool — malware scanners, debuggers, emulators, decompilers — agrees on, because nothing else decodes this many architectures with this little ceremony. If you write any Python that pokes at binaries, you've almost certainly already depended on it without knowing.

### RSS — Other

## 48. ChatGPT wie, co robisz w sklepach internetowych i śledzi Twoje ruchy na innych stronach — by NieBezpiecznik.pl
![NieBezpiecznik.pl](https://niebezpiecznik.pl/wp-content/uploads/2026/09/chatgpt-obi-ciasteczko-kv-600x338.jpeg)

**Source:** https://niebezpiecznik.pl/post/chatgpt-wie-co-robisz-w-sklepach-internetowych-i-sledzi-twoje-ruchy-na-innych-stronach/
**Karakeep doc:** `h86gqtpecadcy24tyiahw23o`

OpenAI właśnie uruchomiło mechanizm reklamowy oparty o ciasteczko `__obi`, które łączy Twoje konto ChatGPT z tym, co robisz poza czatem. Rozmawiasz z ChatGPT o zdrowiu i finansach, a równolegle przeglądasz sklepy? Od teraz OpenAI może to spiąć w jedną całość. Mechanizm działa w trzech krokach: chatgpt.com zapisuje identyfikator przypisany do konta w ciasteczku `__obi` na domenie `.openai.com` z atrybutem `SameSite=None` i roczną żywotnością; firmy kupujące reklamy instalują u siebie mały skrypt OpenAI z `bzrcdn.openai.com`, dokładnie jak piksele Meta czy Google; Twoja przeglądarka dokleja ciasteczko już przy samym pobieraniu skryptu, zaraz po wejściu na taką stronę. Co gorsza, działa to także po wylogowaniu — anonimowy identyfikator utrzymuje się co najmniej 27 dni. Badacz zweryfikował to na 936 pikselach reklamodawców na 1029 domenach, w tym na Courserze. Technologia sama w sobie nie jest nowa; bezprecedensowe jest wdrożenie jej na „czacie AI", bo ludzie zwierza się AI z rzeczy, których nie publikują w social mediach. SDK zbiera też dane z formularzy i warstwy `window.dataLayer`: e-maile i telefony są haszowane SHA-256, ale kraj, region, miasto i kod pocztowy lecą jawnym tekstem. OpenAI klasyfikuje `__obi` jako ciasteczko analityczne, więc działa nawet przy odmowie zgody marketingowej. Na iPhone adtech nie działa, bo wszystkie jabłkowe przeglądarki blokują ciasteczka firm trzecich w WebKit. Na Androida wystarczy Firefox z izolacją ciasteczek, uBlock Origin z filtrami dla openai.com, albo wycięcie `bzr.openai.com` i `bzrcdn.openai.com` na poziomie DNS — np. w Pi-hole.

## 49. Jak nie dać się zhackować? Ruszamy w Polskę z kolejną edycją naszego kultowego wykładu — by NieBezpiecznik.pl
![NieBezpiecznik.pl](https://niebezpiecznik.pl/wp-content/uploads/2026/09/jnsz-2026-600x337.jpg)

**Source:** https://niebezpiecznik.pl/post/jak-nie-dac-sie-zhackowac-ruszamy-w-polske-z-kolejna-edycja-naszego-kultowego-wykladu/
**Karakeep doc:** `kyahyjvfrftepbacnn3at198`

NieBezpiecznik is taking its cult "Jak nie dać się zhackować?" lecture on the road across Poland again. The pitch is blunt: anyone who touches a computer, phone, or the internet should know how to do it without getting owned, and until now that knowledge mostly went to corporate employees on closed trainings. The open lecture fixes that — three hours of practical advice and live demos, rated 9.56/10 by past attendees, aimed at everyone including people with zero technical background. The agenda is a greatest-hits of getting burned: securing your computer and phone, dodging the scams and phishes Poles actually fall for, protecting your privacy in email and social media, keeping data and comms from being snooped, shopping online, and internet banking. They illustrate it with real attacks from recent months and do live shows — impersonating the president, stealing data off a phone, cracking Polish passwords, infecting a laptop and watching through its webcam, seizing a machine via a malicious USB stick. They promise jaws will drop, and that nobody leaves the same person. Five cities are locked in: Kraków on 24 September, Poznań 8 October, Łódź 22 October, Gdańsk 19 November, and Warszawa 3 December, with a leave-your-email box for everyone else. Tickets aren't tied to a name, so you can buy one for your mum, dad, grandma, or the non-technical friend who clicks every link. The closing jab is fair: a ticket costs less than cleaning up after the first hijacked inbox or virus infection.

## 50. Obejrzeli poradnik na YouTube, zostali "zainfekowani" i stracili kryptowaluty… — by niebezpiecznik.pl
![niebezpiecznik.pl](https://niebezpiecznik.pl/wp-content/uploads/2026/09/drainer-kv-1-600x338.jpg)

**Source:** https://niebezpiecznik.pl/post/obejrzeli-poradnik-na-youtube-zostali-zainfekowani-i-stracili-kryptowaluty/
**Karakeep doc:** `tbuz4pg4zbpjduf0vs5vnb4l`

A wave of YouTube tutorials promised that anyone, no programming skills required, could build a "fully autonomous crypto trading bot" with the help of Claude. The catch was that the bot never did what the video showed. Victims copied the code, deployed a contract, and signed the transactions themselves — every step looked legitimate. The single poisoned step was a fake version of the Remix tool, which silently ignored the pasted code and ran a drainer contract fetched from the attackers' server. The result was that 224 wallets lost 274.6 ETH, roughly 2,000,000 złoty. TRM Labs documented the campaign and found nine near-identical tutorials on different channels pretending to be independent creators, with AI-generated presenters, AI voices, and fake comments praising the results, including a promised return of 1 ETH every 20 hours. The median loss was 1 ETH because the tutorials told victims to fund the bot with 1–2 ETH to start. The thefts ran from 12 February to 11 August 2026, and the stolen funds moved entirely through decentralized infrastructure — DAI swaps, bridges, and a mixer, with no centralized exchange in the path. After the drain, confused victims were shown a fake error ("ERROR: Arbitrage stuck") and asked to add another 50% as "gas," which was just a second transfer to the thieves. Niebezpiecznik's takeaway is blunt: crypto is not for people who don't understand the technology, and vibecoding money-making tools with AI without reading the code is a fast way to lose it.
