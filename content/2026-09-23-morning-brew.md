---
date: 2026-09-23
slug: 2026-09-23-morning-brew
tags: Open Source Software,Software Bill of Materials,Python Programming,Dependency Management,Nix Ecosystem,Productivity,Engineering,Linux Distribution,Software Development,Design,Automation,DevOps,Containerization,CI/CD,CAD Software,3D Modeling,Linux Software,Engineering Design,WebRTC,Remote Desktop,Collaborative Browsing,Virtual Browser,SLAM,3D Mapping,Computer Vision,Robotics,Linux,Multimedia,Video Editing,Content Creation,Chemistry,Molecular Structure,Scientific Software,Chemical Drawing,Machine Learning,Artificial Intelligence,Text To Speech,Speech Synthesis,File Systems,Linux Kernel,Embedded Systems,Flash Memory,Operating System,Fedora,Atomic Desktop,Mathematics,Computer Algebra System,Symbolic Computation,Software Engineering,Modeling Workbench,Unified Modeling Language,Metamodeling,Perl,Static Analysis,Linters,Graphical User Interface,Default Applications,MIME Associations,Live Streaming,Video Broadcasting,Low Latency,Workflow Management,Computational Materials Science,Atomistic Simulation,MIME Types,Command Line Interface,Rust Programming Language,Regular Expressions,Large Language Models,Data Analysis,Data Visualization,Visual Analytics,Node.js,Command Line Tools,Web Development,Accessibility Testing,Workflow Engine,Data Orchestration,Asynchronous Programming,Python,Notion,API,Multi-Object Tracking,Database Management,SQL Client,Natural Language Processing,Benchmarking,Coding Assistants,Media Server,Video Streaming,Self-Hosted Software,YouTube Downloader,Content Management,Web Crawling,PDF Conversion,Productivity Tools,Documentation Archiving,Encryption,Data Backup,Open Source Projects,Deduplication,Cloudflare,Online Attacks,Web Security,Internet Technology,Website Status,Future Technology,AI Development,Gaming,Video Games,Technology,SteamOS,Coding Tips,Programming Best Practices,Linux Gaming,Android,Valve,Waydroid,Coding,Anthropic,Claude,Technology Review,Computer Hardware,Apple,Mac Studio,Performance Testing,Backend Development,Programming,Tech Talk,Project Management,Team Collaboration,Local Computing,Mobile Computing,Deep Learning,Personal Computing,Operating Systems,Local AI,Kubernetes,Docker,Container Management
---

# Morning Brew — 2026-09-23

Forty-five links from Wednesday, and the roundup machine was in overdrive — five separate "best of" listicles this time, which is how you end up with two dozen CAD programs and twenty-three computer algebra systems in one day's haul. Nine videos transcribed; the tenth, PrimeTime's show-and-tell episode, gave the transcriber nothing, so it sits there as a stub rather than a summary I made up. Real meat is spread thinner than usual: Portainer freezing its Community Edition and quietly closing the free path to 3.0, a workflow engine that removes infrastructure instead of adding it, and AntV building a machine that looks at your dashboards and tells you what's weird in the numbers. Dig in.

### Hand-bookmarked

## 1. Portainer Cuts the Cord Between Its Free and Paid Editions — by It's FOSS

![It's FOSS](https://itsfoss.com/content/images/2026/09/portainer-docker-kubernetes-banner-2.png)

**Source:** https://itsfoss.com/news/portainer-community-edition-freeze/
**Karakeep doc:** `hsmo9f4aoya7l0ffkqfrkm83`

Portainer's Community Edition had a solid decade-long open source run, and that run is now over. CE is frozen on the 2.x line, and the upcoming Portainer 3.0 — a ground-up rebuild built around Kubernetes — will not be its base. CEO Neil Cresswell is the one holding the knife, and he's framing it as a maintenance problem, not a strategy pivot: every feature the team wanted to add had to be built three separate times, once each for Kubernetes, Swarm, and the Docker/Podman side. That triple-effort model gets scrapped in 3.0, replaced by five separate consoles, each built around a specific job instead of one interface doing everything. CE simply doesn't fit, per Cresswell, and "releasing that as CE would misrepresent what it is and who it is for." What you actually get: CE stays on 2.45 LTS and keeps receiving security fixes, bug fixes, and backports of 3.x features — but only where a matching Docker API exists to interface with. Feature parity is explicitly off the table because some 3.x stuff leans on Kubernetes primitives Docker doesn't have. If you want the new capabilities without adopting Kubernetes, there's no free-and-open path; the only no-cost route onto 3.x is the "3 Nodes Free" node-capped license for the closed-source Business Edition. For anyone already running Docker today, nothing breaks — 2.x keeps working and stays patched. The piece flags two alternatives worth a look: Komodo (Rust, GPL-3.0, no server-count limit) and Arcane (Go/SvelteKit, BSD-3-Clause). Neither is a drop-in replacement, especially if you lean on Portainer's Kubernetes features. But for a homelab that just wants a self-hosted Docker UI without a paid tier, both are credible. The top comment nails the real risk: admins who learn Portainer in their homelab are the ones advocating for it at work. Freeze CE, and you choke off your own enterprise funnel.

### RSS — YouTube

## 2. Opus 5.5, GPT-6 Sol, GPT-6 Luna, MiMo v2.6, Grok 4.7.... — by Theo - t3.gg

![Theo - t3.gg](https://i.ytimg.com/vi/2qNX30hTyDg/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=2qNX30hTyDg
**Karakeep doc:** `d0jnpvlgo1ecov79uwqvawha`

This stream is less a model roundup and more Theo workshopping Anthropic's own guide on how to actually use Opus 5.5 well — and mostly agreeing with it. The core thrust: the era of cramming "do not do this" guardrails into your agent/claude.md files is over. He argues you should delete those files, start from scratch, and only append instructions after a model actually misbehaves. The old habit of writing negative constraints came from 2025-era agents that needed babysitting; the current frontier models make sane defaults. One example he quotes from the guide: instead of telling a model to "think hard," ask it to "explain why you chose this approach," since anything that smells like reasoning flags the automated checkers. He's genuinely bullish on screenshots over copy-paste — half the time he just grabs a screenshot of the browser and pastes it, because models read images well, and CloudCode even auto-crops high-res screenshots to the region it needs. His one gripe with the article is the "fast mode" tip, which he calls silly because it doesn't apply to subscription plans. The bigger philosophical shift he's pushing: we're now at the point where agents need more leash, not less — the ability to verify their own changes, a definition of "done," and enough trust to go do the thing. He teases that the verification system around Claude's site and desktop app is why that product got three times faster, and that building verification layers matters as much as the source code itself. He ends on a hard line: whatever you do, do not touch "max mode," which he says is "so bad." Then he pivots to rating models — GPT-6 Sol, Luna, MiMo v2.6, Grok 4.7 — but admits he hasn't had time to test them properly and doesn't want to do it half-assed on stream. Five and a half hours in, his food's cold, and he's out. The takeaway is practical: trust the model more, feed it what it needs to trust its own work, and it goes further than you think. For Wojtek: stop over-specifying your agents and let Opus 5.5 cook.

## 3. Oops, we accidentally created the Torment Nexus; SteamOS Making Moves - Talking Heads Ep.451 — by Craft Computing

![Craft Computing](https://i.ytimg.com/vi/bl76ELN_m3E/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=bl76ELN_m3E
**Karakeep doc:** `dw4omadszi3c6k4lb7k8ag61`

Jeff and Vince spend an hour doing two things: covering actual SteamOS/Linux news, and torching the AI-doom media cycle. The concrete news first. The RPCS3 (PS3 emulator) devs found an NVIDIA driver bug that's been lurking for seven or eight years, affects NVIDIA but not AMD, and costs a ~20-25% frame-rate hit — peaking at 37% in Gran Turismo 5, all while chewing less VRAM. They've filed a bug report and shipped their own workaround, and Jeff speculates the root cause is the driver wasting memory bandwidth on redundant buffers and mipmapping passes. The punchline he floats: NVIDIA's Linux drivers are already ~35% slower than Windows, and it'd be beautiful if a PS3 emulator team accidentally explained why. Valve also flipped on beta NVIDIA driver support in SteamOS, the natural next step in de-risking its Microsoft dependency — a dependency that dates back to Windows 8's walled-garden threat, which is literally why SteamOS was born in 2011. And the ARM build of SteamOS is now officially downloadable (the Steam Frame variant, running on Snapdragon 8 Gen 2). Then comes the spicy half. They're sick of "our AI agents went rogue and hacked companies" headlines, and they break down why: the AI labs publish these as *security bulletins*, not press releases, and lazy journalists turn them into doomsday clickbait. The "Anthropic says >10% chance AI kills humanity in a decade via bioweapons" claim falls apart with one follow-up question — AI has no arms, no warehouse, no wet lab, and the bioweapon/bio-medicine research is the same goddamn molecule. Their actual theory for why every frontier lab is suddenly shouting "regulate us, daddy": they ran out of content to scrape and want to pull the ladder up behind them, banning open source and freezing out competitors. Vince's personal receipts make it concrete — he had an LLM SSH into his lab, rename a live binary to "test the negative case," and break production, because there's no conscience, just reinforcement learning chasing a cookie. The Trackmania example seals it: the AI never learned the shortcut until a human literally placed a brick wall on the ramp. Stop anthropomorphizing. It's code.

## 4. The top 8 mistakes people make with AI coding — by Less Bitter

![Less Bitter](https://i.ytimg.com/vi/jDG7L5HuBnk/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=jDG7L5HuBnk
**Karakeep doc:** `rx844uabj1qzwvukwry0r4a3`

After fifty one-on-one calls with solo builders and entrepreneurs, the host has a list, and the through-line is brutal: most people are still running their 2025 agent workflows on 2026 models and getting left behind. Mistake one — delete your agent.md and claude.md files. The negative guardrails ("absolutely never do this") you needed in early 2026 are now noise; start clean and only add rules when a model actually misbehaves. Two — kill your little "factory systems," the orchestrator-plus-child-agents skeuomorphic metaphors and message-bus scaffolding that smart people built when the models sucked. Three — stop treating context as sacred and making your agents take notes or write markdown specs. Your code *is* the spec; agents see English and code as the same tokens, so a second source of truth just slows everyone down. Four — stop hoarding mega-threads; new feature, new conversation, then close it and never look back. Five — a to-do list and a Kanban board are anti-patterns for a solo builder; when you have a thought, throw it at the agent and let it run, because if it's not worth doing now it's not worth doing later. Six — stop using franken-tools; he built his own client (enjoy.dev) specifically because Claude/ChatGPT desktop drown non-engineers in technical noise and people lose the state of their project. Seven — stop stressing about code quality before you've validated the idea; pre-MVP code was always shit, and Astra's output is already better than a 2016 proof-of-concept. Eight — the one he thinks will get him burned at the stake: stop with branches and work trees. He runs six agents on main simultaneously with zero conflicts, relying on a "commit after every change" instruction so any bad agent is one revert away. His whole thesis: start naive, add process only when you hit failure, and if you're bickering with an agent in hundred-message threads, you're over-specifying. For Wojtek: this is the anti-ceremony counter to every "AI engineering" framework video out there.

## 5. Valve's Waydroid Fork Is Finally Public — by Brodie Robertson

![Brodie Robertson](https://i.ytimg.com/vi/2G44ZTTamuA/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=2G44ZTTamuA
**Karakeep doc:** `hv79iln2710fn6pihpk4pg7v`

Valve's Steam Frame is an ARM Linux VR headset running SteamOS, and that creates a real problem: Wine (and Valve's Proton fork) is built for x86-64, not ARM. For Windows games Valve leans on FEX, the x86/x86-64 emulator for ARM64. But a huge chunk of VR games are Android-native, and that's where Lepton comes in — a tool that lets Android-exclusive games run on Linux. Lepton started as a fork of Waydroid, and that's where the drama lives: the Waydroid team had no idea Valve was forking them, and got zero communication, which is out of character for a company that's spent years funding contract work in Wine, KDE, and FEX. The source code also vanished from view for a while — bizarre when Proton and FEX were always just sitting on GitHub. Now that the Steam Frame is actually buyable, Lepton has surfaced on Valve's GitLab. The design choices are telling. Lepton runs as a non-root user with no rootful helpers, every process as the same non-root user, no enforced isolation between apps, and each app gets its own container — this is built to launch one piece of Android software, not a full Android session, and it disables the Android services a game doesn't need, which may break general apps. It caches state to speed up Android userspace boot, targets game devs porting Android VR titles to the Steam Frame, and — critically — currently only works on ARM. That's why it's a fork and not just Waydroid: Waydroid's goals (general Android) don't align with Lepton's (bare-minimum game launching on ARM). Brodie flags the licensing split: the Android root filesystem is GPL v3, while the compat tool itself is MIT. Lepton also folds in pieces of Andbox (the dead Android-in-a-box project Waydroid succeeded), Halium (running real Linux on Android phones), and libhybris (loading Android drivers from non-Android Linux) — which is why it can pull graphics drivers that don't otherwise exist for ARM hardware. A Valve developer is now active in Waydroid's channels trying to upstream changes that make sense in mainline. The real story: Valve is quietly industrializing "Linux runs Android apps on ARM" the same way Proton industrialised "Linux runs Windows games," and because the source is out, forks and cashios-style rebundlings are inevitable. For Wojtek's homelab brain: watch this project — it's Proton's ARM twin being born in public.

## 6. Anthropic Actually Fixed Opus — by Theo - t3.gg

![Theo - t3.gg](https://i.ytimg.com/vi/jgGyX7MPPVg/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=jgGyX7MPPVg
**Karakeep doc:** `ll2fulcn5tllzt2j8nmvi0j8`

Theo starts by admitting Opus 4.5 landed almost a year ago and changed how people code, but everything since has been a letdown — he fell for Opus 5, and it burned him. The new drop isn't Opus 5.1, it's 5.5, and he's been running it all day and says it's blowing him away. The pricing is the headline: 40% cheaper to run than Opus 5, input at $4/M and output at $20/M (down 20%), and cache reads now 60% cheaper at $0.20/M. It's also about 30% faster. His favorite change is "communication" — 5.5 writes like a human and puts the important info up front, and the before/after comparison of a debugging explanation is night and day: Opus 5 rambled about "M-dashes" and "half open intervals" while 5.5 actually nails the commit, the dollar amounts, and the bug. On benchmarks it's "slaughtering" everything, sweeping the Pareto frontier on the artificial analysis index with a five-point jump over Fable 5.1, and medium effort often scoring higher than Fable did on max. The catch: it's wildly token-inefficient, doing ~120K tokens per task versus GPT-6 Astra's 27K — a 4x efficiency gap that eats the price cuts. He hates the "max" reasoning level, which ran a thread for six and a half hours writing a markdown plan and burned tokens in loops; low and max are "dangerous," medium/high/x-high are the sweet spot, and a one-notch bump from x-high to max sent reasoning tokens from ~330 to ~5,000 per question for a 1% score gain. The ZDR (zero data retention) angle is the sleeper: Fable can't offer it, so companies that require it couldn't enable Fable — Opus can, which means it instantly becomes the default coding model for enterprises. The 5-hour Claude limit also got bumped. He flags a lingering quirk where the model panics about its context window auto-compacting and frets that "if it crashed, the work would be lost" — nonsense Fable wouldn't say, and a sign it's still a bit smaller and dumber. On the fun side, the 3D demos people made with it are insane: a Dark Souls clone, a from-scratch Tony Hawk Pro Skater clone in C++, and his own "Fish Slop" that runs at 120fps. Verdict: this finally makes the $200 Claude sub worth it versus Codex, and he's barely touching Astra now.

---

## 7. Apple Says the New Mac Studio Is 4x Faster. I Tested It. — by NetworkChuck

![NetworkChuck](https://i.ytimg.com/vi/CbWySQdAM60/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=CbWySQdAM60
**Karakeep doc:** `el6u4rl4dupygeu64krxb6gw`

Chuck got an M5 Ultra on loan from Apple and treats it like a server, not a desk machine — his whole test is local AI, no cloud, no internet. The two specs that matter: both the M3 and M5 Ultra have 80 GPU cores, but the M5 adds a neural accelerator to every core and bumps memory bandwidth from 819 GB/s to 1.2 TB/s. That bandwidth is the whole story for token generation, because a ~15GB model has to be pulled from memory for every single token. First test: a 32K-token summarization of Qwen 3.8 27B 4-bit. Time-to-first-token went from 82.85s (M3) to 21.66s (M5) — 3.8x faster — and throughput from 28.1 to 43.3 tokens/sec (1.5x, matching the 50% bandwidth bump). Smaller 14B and 35B models widened the TTFT gap to 4x. Transcription with Whisper large-v3 turbo ripped through two hours and five minutes of audio in 24.4s (2.3x faster), which matters to him because he transcribes footage daily. Video analysis with Qwen 3 VL 32B MLX ran one frame per second and described the scene accurately in 22s, 2.6x faster — he'd happily drop the paid Gemini Video API for this, and he wants to use it to classify old home VHS footage for free. Local image gen (Flex 2 Kline 4B) and video gen (LTX 2.5 22B MLX) both ran several times faster than the M3, and the same prompt and seed on both machines proved the output is identical, just quicker. The wild bit: he loaded a local model as his Hermes agent brain with a 131K context window and it actually answered correctly about his own agent context — he's "floored" since local models usually fall apart with context. He even drove DaVinci Resolve's new MCP to edit a video locally, though it took 13 minutes. The catch is the price — his config runs $14K (256GB RAM, 8TB), which he calls "absolutely crazy." Still, his takeaway is "unlimited AI" you actually own — when the AI companies go crazy, you still have this — and he wants to cluster four of the upcoming 512GB editions when they drop in October. Funny footnote: he realized at the end he never once tested coding.

---

## 8. 🚨🚨 TheStandup: Trash's Show And Tell and Casey Judges🚨🚨 — by The PrimeTime

![The PrimeTime](https://i.ytimg.com/vi/y7CAI5IfCm8/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=y7CAI5IfCm8
**Karakeep doc:** `wj3k3hd1z32x718fwm20rfnd`

This is a TheStandup episode on ThePrimeagen's channel, and the premise is baked right into the title: a "show and tell" segment where "Trash" walks through something they built and "Casey" sits in the judge's seat. The tags tell the rest of the story — backend development, coding, programming, software development, tech talk — so it's a live demo-and-critique format, the kind where someone throws up real code on stream and the host rips it apart or defends it. The transcript step failed on this one, so I can't tell you what Trash actually showed or how harsh Casey got, which is a shame because that's where all the fun lives in these. If you've watched any TheStandup before you know the drill: it's less a tutorial and more a roast wrapped in a code review, and the value is usually in watching someone defend a weird architectural decision in real time rather than reading a writeup. The "show and tell" framing suggests a junior-or-contributor project getting held up for inspection, which on this channel usually means a mix of genuine praise and brutal "why did you do it this way" pushback. Worth a click if you want the raw, unscripted version of that energy instead of a polished explainer — but since the machine couldn't transcribe it, you're on your own for the punchline.

---

## 9. They can't take it anymore — by The PrimeTime

![The PrimeTime](https://i.ytimg.com/vi/iuccfEQgIeY/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=iuccfEQgIeY
**Karakeep doc:** `wn1ef7ls6x13bezw9zzg6htu`

The Primeagen opens by reading a viral tweet from a big-company engineer who's done: every spec, PRD, ticket, test, and report is generated by Claude Code, nobody reads anything, people work 12-13 hour days just pressing enter, and there's "no sense of victory." Nobody resolves bugs in reality, nobody thinks — everyone from L1 to L7 just talks to Claude. His take is that this isn't new — management has always asked how many corners they can cut, from his 2007 jobs through ten years at Netflix. What changed is the whiteboard defense died. He cites Mitchell Hashimoto: you should be able to pull someone aside and have them explain any customer-facing system they shipped and defend the decisions. That's not line-by-line familiarity, just "why X over Y," "what happens when the actor is malicious," "why does this data structure fail." His fear is a brain drain, and a bifurcated industry: the CRUD-app crowd thinks AI solved everything because a single server and a database are basically solved problems, while everyone else is drowning in complexity they can't hand off to "Dario take the wheel." The thing that worries him most is juniors — the catch-22 where seniors can explain systems because they built them by hand, but juniors are now expected to generate code instead of writing it, so they never learn what a good system feels like. He quotes the creator of Clay: seniors can explain the system because they implemented it by hand, but juniors generate instead of write. His actual prescription is boring and correct: learn to say no, don't be a "yes engineer" who shits out features, sit down in a text editor, and write code by hand to understand libraries and architecture. He admits he does exactly this himself, because he can't just read docs and claim he understands a design. The whole thing is a gut-check against shipping whatever the robot outputs.

---

## 10. Forget the Series 12. My Series 6 Runs an LLM Locally! — by Better Stack

![Better Stack](https://i.ytimg.com/vi/jGlMiZ4cpjk/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/jGlMiZ4cpjk
**Karakeep doc:** `kko71px0vm2vlsz3zcpg0jhp`

This is a YouTube Short showing a full LLM running completely offline on an Apple Watch Series 6 — a device that launched back in 2020, six years old at this point. No cloud, no streaming, everything runs on-device ("on edge") and streams text at around 15 tokens per second on average. The model doing the work is a 90-million-parameter one called Falcon H1, and the pitch is that being that small is what makes it "surprisingly performant" on a watch. It even supports tool calls, which is the actually interesting part: paired with the watch's built-in voice input, you can just talk to it. The demo asks "what is the capital of France," and it fires a Wikipedia tool call and answers Paris almost instantly, correctly. Then they push it harder with "explain the depth-first search algorithm," and it streams the answer out fast enough to be impressive on the hardware. The whole point is a flex and a jab: if a 2020 Apple Watch can run a local LLM, why are device makers still hesitating to ship on-device models? Fifteen tokens a second is glacial by desktop standards, but that's not the point — a 90M-parameter model with tool-calling that fits on a watch blows up the assumption that edge inference needs real hardware. It's a genuinely useful counterpoint to the "you need a $14K Mac Studio" narrative from the NetworkChuck video — a 90M model is not a frontier model and it won't write your code, but it proves the floor for local inference is way lower than most people assume, and tool-calling from your wrist is a neat party trick with a real point about where edge LLMs are going.

## 11. I ran a 35B param model on my iPhone. — by YouTube

![YouTube](https://img.youtube.com/vi/OS-rqiNEvAY/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/OS-rqiNEvAY
**Karakeep doc:** `txfe4tt8652unkfaux8upzc6`

A 35-billion-parameter model running directly on an iPhone sounds like a lie, but it's a mixture-of-experts trick. As a plain 4-bit file the thing would clock in around twenty gigs and need to live entirely in RAM, which no phone has. The entire game changes when you realize MoE models only activate a tiny slice of themselves at any moment. Only about 1.4 gigs actually has to stay resident in memory. The parts every single token touches — embeddings, attention, routers, the shared expert — load once and stay put. The rest, forty expert files of roughly 300 MB each totaling around twelve gigabytes, sit idle on the SSD waiting for their cue. For each token, attention runs on the GPU, the router picks eight experts, and the engine reads those eight straight off SSD into GPU memory and runs them alongside the shared expert. That whole dance happens in every one of the forty layers, which works out to about 320 small reads per token. It's genuinely clever: streaming inactive experts on demand instead of holding a bloated model in RAM. The tradeoff is latency, not capability — you're swapping cheap storage reads for expensive memory you don't have. If this works smoothly, it means multi-billion-param models on phones stop being a demo gimmick and start being a real deployment path. Don't expect your next iPhone to run GPT-class weights in a browser tab, but the ceiling just moved. The model that "wouldn't fit" now fits, by not being loaded until it's needed.

### 9to5Linux (RSS)

## 12. Wireshark 4.6.9 Updates Protocol and Capture File Support, Fixes More Bugs — by Cloudflare

![Cloudflare](https://9to5linux.com/wp-content/uploads/2026/07/ws467.webp)

**Source:** https://9to5linux.com/wireshark-4-6-9-updates-protocol-and-capture-file-support-fixes-more-bugs
**Karakeep doc:** `kwqnfncxrhu08y4wvnvoe3uz`

Wireshark 4.6.9 landed as another minor bump in the 4.6 series, and it's mostly housekeeping with a side of security. This one updates protocol support for a sprawling list — QUIC, SMB, IEEE 802.11, LoRaWAN, DICOM, OpenFlow, PKCS12, ZigBee ZCL, X11, and a pile more. Capture file support got refreshed for BLF, pcapng, PEAK TRC, Toshiba, and a few others. The headline number is 19 vulnerabilities fixed across a long list of dissectors and file parsers — ZigBee ZCL, SPDY, USB HID, TIFF, X11, MBIM, SCTP, RTP, and more. If you parse untrusted captures, that's the reason to update, not the feature list. There's also a fix for Wireshark ignoring GREASE values in JA4 fingerprint calculation, which matters if you're doing TLS fingerprinting for detection. Plus a UTF-8 encoding bug found by fuzzing got squashed. One notable plumbing change: on Unix systems, extcap helper binaries are now searched under libexec instead of lib64, which is the customary spot. Nothing revolutionary here — just the steady drip of a tool that eats network traffic and shits vulnerabilities back at you if you don't patch. Grab it from the site or Flathub.

## 13. Debian-Based SparkyLinux 2026.09 "Tiamat" Introduces Sparky Labwc Edition — by Cloudflare

![Cloudflare](https://9to5linux.com/wp-content/uploads/2026/09/sl2609.webp)

**Source:** https://9to5linux.com/debian-based-sparkylinux-2026-09-tiamat-introduces-sparky-labwc-edition
**Karakeep doc:** `uvlqi8qb61l8ss568vz2xlaa`

SparkyLinux 2026.09 is out as a semi-rolling update to the upcoming 9 "Tiamat" series, and the headline is a brand-new Sparky Labwc edition. Labwc is a wlroots-based Wayland stacking compositor, so think Openbox's minimalist spirit but running Wayland instead of X11. The Labwc ISO ships as a MinimalGUI image, meaning you install any desktop environment you want through the CLI installer afterward. Because it omits any app needing admin rights — no APTus, Synaptic, Gufw, or Calamares — installation is done purely via the `sudo sparky-installer` command. The distro itself is built on Debian "Forky" Testing and SparkyLinux Testing repos as of September 21st, running the fresh Linux 7.2 kernel. Desktop editions include KDE Plasma 6.7.4, Xfce 4.20.1, LXQt 2.4, MATE 1.26.1, and Openbox 3.6.1. Software-wise you get LibreOffice 26.8, Firefox 140.16.0 ESR, Thunderbird 140.14.0 ESR, and Calamares 3.4.3. Since it's rolling, existing users just update rather than reinstall. The devs warn you'll want an active internet connection for UEFI installs, and they strongly prefer the Calamares graphical installer there. Nothing flashy, just a competent Debian-based rolling distro quietly adding a Wayland option for the Openbox faithful.

## 14. KeePassXC 2.8 Promises Auto-Type on Wayland and Qt 6 Port, Beta Out Now — by Cloudflare

![Cloudflare](https://9to5linux.com/wp-content/uploads/2026/09/kxc28b.webp)

**Source:** https://9to5linux.com/keepassxc-2-8-promises-auto-type-on-wayland-and-qt-6-port-beta-out-now
**Karakeep doc:** `f46e61h76skfsvpphqhsyn71`

KeePassXC 2.8 beta is out, and it's shaping up to be the release Wayland users have been waiting years for. The big two: a long-anticipated Qt 6 port, and Auto-Type on Wayland via XDG Desktop Portals — finally solving the "it works on X11 but not Wayland" whine. There's also quick unlock via Polkit on Linux, quick unlock with password on macOS, configurable keyboard shortcuts, and remote database sync through external tools. Native ARM64 Windows builds are in, plus improved AppImage desktop integration. The SSH Agent can now generate RSA, ECDSA, and Ed25519 keys. On Linux it stores state in XDG_STATE_HOME instead of XDG_CACHE_HOME, which is the correct call. Security fixes are the part that matters: a use-after-free on crafted KDB imports, an out-of-bounds write in native messaging encryption, integer overflow in the legacy KDB importer, and entry reference injection via the browser extension. That's a real list, not padding. If you were burned by KeePassXC's Wayland Auto-Type gap, this beta is worth eyeballing — just not on a machine you care about, since it's explicitly not for production. The database now lives in a safer place, and the port finally drags it into the modern Qt era.

## 15. NTFS-3G 2026.9.18 NTFS Driver for Linux Released with Security and Bug Fixes — by Cloudflare

![Cloudflare](https://9to5linux.com/wp-content/uploads/2026/09/ntfs3g.webp)

**Source:** https://9to5linux.com/ntfs-3g-2026-9-18-ntfs-driver-for-linux-released-with-security-and-bug-fixes
**Karakeep doc:** `b1p0rxpwggp3qhqsjkfhmesc`

NTFS-3G 2026.9.18 is a security update first, everything else second. It adds guards against multiple creator-owner and creator-group ACEs during ACL inheritance, and fixes heap buffer overflows in a stack of functions — `ntfs_external_attr_find()`, `ntfs_ea_check_wsldev()`, `ntfs_check_restart_area()`, `ntfs_same_sid()`, and `ntfs_acl_owner()`. There's also a heap out-of-bounds read/write in `ntfs_ie_add_vcn()`, heap data corruption in `ntfs_mapping_pairs_decompress_i()`, and a denial-of-service in `ntfs_inode_attach_all_extents()`. The `ntfsresize` command got a fix for stale $MFTMirr data when the first extent of $MFT is relocated, and `ntfscat` now cleans up an opened attribute on error. All of it points the same direction: if you mount NTFS partitions through FUSE, patch this. The article is refreshingly honest about the bigger picture, too — NTFS-3G runs in userspace via FUSE, so every transfer bounces between user and kernel mode, creating a CPU bottleneck and slower speeds. They flat-out recommend the native in-kernel NTFS3 driver from Paragon instead, which shipped with Linux 7.1 and is faster and less CPU-hungry. If your kernel is 7.1 or newer, you arguably don't need NTFS-3G at all anymore.

## 16. NVIDIA 595.104.02 Linux Graphics Driver Is Out Now with Better Wayland Support — by 9to5Linux

![9to5Linux](https://9to5linux.com/wp-content/uploads/2023/03/nv53030.webp)

**Source:** https://9to5linux.com/nvidia-595-104-02-linux-graphics-driver-is-out-now-with-better-wayland-support
**Karakeep doc:** `xlegyuvjccev0sqlilmw54dn`

NVIDIA shipped the 595.104.02 graphics driver for GNU/Linux, FreeBSD, and Solaris. It's a small maintenance update in the production-ready 595 series, landing a month after 595.99.02. Don't expect headline features here — this one's about squashing bugs. Two fixes stand out. First, a failure that could happen when allocating GPU page tables larger than 2 GiB (INT_MAX, for the pedants). Second, an issue where unvalidated VkHdrMetadataEXT values got forwarded to the Wayland color-management-v1 protocol, which could crash the whole thing. Lovely. If you've been staring at HDR flicker or random compositor death on Wayland, this is the patch you've been waiting for. The release notes live over at NVIDIA's own site if you want the full changelog. Installers are up for 64-bit and AArch64 (ARM64) Linux, plus FreeBSD. Since it's the stable branch, NVIDIA recommends it for everyone chasing reliability. If you'd rather have new toys than stability, the 615 series is where the action is — Vulkan-native Reflex support in Proton and cgroups memory partitioning, that sort of thing. The one comment on 9to5Linux basically says it all: someone's furious NVIDIA still ships a closed-source driver at all. Fair point, but for the rest of us on green team hardware, this is a boring, safe update worth grabbing.

### Open-source Projects (RSS)

## 17. AVA — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/antvis/ava)

**Source:** https://www.opensourceprojects.dev/post/8dd85f23-d4af-4377-b830-c2a25832f008
**GitHub:** https://github.com/antvis/ava
**Karakeep doc:** `zitp186dx3662suij1dr5ajn`

AVA is AntV's framework for automated visual analytics, and the "A" is doing quadruple duty: AI-driven, Automated, Augmented, all bolted onto Visual Analytics. In practice it's TypeScript, MIT-licensed, with about 1,500 stars. The core package `@antv/ava` breaks into four modules that do the heavy lifting. There's `data` for statistical processing of datasets. There's `insight`, the auto-insight engine that churns multi-dimensional data through algorithms and scores whatever interesting patterns it finds. Then `ckb`, a chart knowledge base built from empirical visualization wisdom, feeding `advisor`, which recommends chart types and optimizes the ones you've already got. If you don't want to wire it all up yourself, `@antv/ava-react` gives you plug-and-play React components: `NarrativeTextVis` for writing out insight interpretations, `InsightCard` to render them as graphics-plus-text, and `AutoChart`, which claims one-line intelligent visualization. The pitch is closing the "last mile" of the analysis chain — handing you a chart plus a sentence explaining why it matters, instead of a raw table and a shrug. AntV's pedigree is solid (same folks behind G2 and G6), but this is genuinely useful if you're drowning in dashboards and want the machine to tell you what's weird in the numbers. Steep learning curve, though — the docs assume you already speak visualization.

## 18. Pa11y — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/pa11y/pa11y)

**Source:** https://www.opensourceprojects.dev/post/b5b4f9ba-d140-4edc-8cfd-9929315916b5
**GitHub:** https://github.com/pa11y/pa11y
**Karakeep doc:** `e3chy9d3csgtnisvw53eoksu`

Pa11y is the self-described "automated accessibility testing pal," and unlike a lot of a11y tooling that's either a browser extension or a walled-garden SaaS, this one runs from the command line or Node.js. JavaScript, LGPL-3.0 licensed, roughly 4,500 stars. The whole thing is `pa11y https://example.com` — one line, and it spits out a WCAG report. You can pick your standard (WCAG2A/AA/AAA), your test runner (htmlcs by default, or axe), and your output format (cli, csv, or json). There's a threshold flag so your CI pipeline fails on exit code 2 the moment errors cross a line you set. You can scope testing to a root element, hide stuff you don't want flagged, set timeouts, and grab screen captures of pages as it crawls. It's the difference between "accessibility is something QA pokes at quarterly" and "accessibility breaks the build." Version 10 requires Node 22.13.0+, and it runs on Linux, macOS, and Windows. There's also `pa11y-ci` for wiring it into continuous integration and `pa11y-dashboard` for a web view of results, so the suite scales beyond one dev's laptop. Honest caveat: automated checks catch maybe a third of real a11y problems — contrast and keyboard traps still need a human. But as a floor in your pipeline, it's genuinely good.

## 19. Dagu — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/dagucloud/dagu)

**Source:** https://www.opensourceprojects.dev/post/6d32b2cd-673e-4cb9-a185-ec840a346eba
**GitHub:** https://github.com/dagucloud/dagu
**Karakeep doc:** `xskuiy7lnkewpgtexl74p2n3`

Dagu is a workflow engine for people whose actual job isn't running a workflow engine. Go, GPL-3.0, about 4,000 stars, and it ships as a single binary with a built-in web UI — no Postgres, no Redis, no broker, no Python environment. Define DAGs in declarative YAML and point them at shell commands, Docker containers, Kubernetes Jobs, or SSH commands. It runs on Linux, macOS, and Windows, on-prem or air-gapped, and scales from one node to a fleet. The pitch is sharp: cron gives you no dependencies or retries; Airflow makes you operate a six-service platform and rewrite your jobs as `@dag` framework code; Temporal sucks your business logic into its SDK. Dagu keeps workflow structure as configuration sitting next to your scripts — delete the YAML and they run untouched. You get scheduling with cron syntax and timezones, retries, human-in-the-loop tasks, sub-DAGs, concurrency controls, and per-step logs and history. There's even a built-in MCP server so an AI agent can inspect and drive your workflows. State lives in local files, which is how it hits production throughput without external services. Honest trade-off: it's not a distributed system, so don't expect Airflow's scale. But for internal automation and runbooks, it's the rare tool that removes infrastructure instead of adding it.

## 20. The official Notion API, in Python, sync and async — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/ramnes/notion-sdk-py)

**Source:** https://www.opensourceprojects.dev/post/f662d76e-85ff-45e0-a528-72cb6f85abad
**GitHub:** https://github.com/ramnes/notion-sdk-py
**Karakeep doc:** `tkmnaiz5act69lm068ecs4rq`

This is `notion-sdk-py`, a from-scratch rewrite of Notion's official Python SDK by ramnes — not a fork, a ground-up reimplementation that keeps parity with the API. MIT-licensed, ~2,200 stars, still actively pushed. The headline feature is dual mode: the exact same client exposes both sync and async interfaces, so you write `NotionClient` for blocking code or `AsyncNotionClient` inside `async`/`await` without learning two APIs. Both call paths return the same typed objects, which is rarer than it sounds. The library mirrors Notion's resource model closely — pages, databases, blocks, users, comments — and handles pagination and rate-limit retries for you rather than making you roll your own. It's maintained with real discipline; the project publishes its own docs and follows semantic versioning strictly, so breaking changes get a major bump instead of ambushing you mid-upgrade. If you've been wrangling Notion's own SDK, which has a history of awkward quirks and uneven maintenance, this is the cleaner alternative worth switching to. Not a silver bullet — you still have to understand Notion's block-based data model, which is its own little circle of hell — but the plumbing is solid and modern. Good pick for anything that touches Notion programmatically.

## 21. Plug-and-play multi-object tracking for any detection model, in Python — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/roboflow/trackers)

**Source:** https://www.opensourceprojects.dev/post/6f61eca0-8b95-406a-8ad7-a5e50b3fe303
**GitHub:** https://github.com/roboflow/trackers
**Karakeep doc:** `q8nwlj5kqgcvenktxtztdfua`

`roboflow/trackers` is Roboflow's collection of clean, modular re-implementations of the leading multi-object tracking algorithms, released under permissive Apache-2.0. Python, ~3,800 stars, and it's young — repo only went up in April 2025. The core idea: you already have a detection model (YOLO, whatever), and you bolt one of these trackers onto its output to get object IDs across frames without rewriting your pipeline. The lineup is the usual suspects reimplemented for clarity rather than raw performance — ByteTrack, BoT-SORT, and friends — plus utilities to switch between them with a one-liner. What makes it useful versus the upstream repos is the packaging. One consistent API, proper typing, no dependency soup, and it plays nice with Roboflow's broader ecosystem if you're already there. The catch is exactly what you'd expect: these are clean-room reimplementations optimized for readability, not SOTA benchmark chasing, so if you need the absolute last 0.1% of MOTA you might still reach for the original authors' code. For the 99% of cases where you just want "which blob is which person from frame to frame," this is the least painful way to get there. The docs are decent and the permissive license means no copyleft anxiety in production. Solid default for tracking work.

## 22. A free database client with 40+ databases and your own AI model — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/ottermind/chat2db)

**Source:** https://www.opensourceprojects.dev/post/14b418f7-b90e-40c1-a4b9-78a01adc70fa
**GitHub:** https://github.com/ottermind/chat2db
**Karakeep doc:** `mrm9t5grvqq879bqyka0kegq`

Chat2DB is a free, cross-platform database client and SQL workspace that's quietly amassed ~28,000 stars. It's Java under the hood, and it's genuinely local-first — your data stays on your machine unless you explicitly sync it. The big selling point is breadth: 40+ databases on tap, from the usual suspects (MySQL, Postgres, SQLite) to the exotic (ClickHouse, MongoDB, Redis, and a pile of NoSQL engines). You get a proper SQL editor, schema browsing, data editing, and import/export, all in one tool rather than six. The "AI" part is the hook: instead of hardcoding a vendor model, you point it at your own model — OpenAI, local Ollama, or anything OpenAI-compatible — and it'll generate, explain, and optimize queries for you. That's the genuinely refreshing bit; most SQL clients make you rent their cloud brain. It ships as desktop, web, Docker, and CLI, plus MCP support so it can plug into agent workflows. The license is a weird custom NOASSERTION thing, so read it before you build a business on it. It's heavy for a "client" — a Java desktop app isn't exactly featherweight — but as a DBeaver alternative that doesn't phone home and doesn't force a subscription, it earns its stars. Worth a try if your SQL life is spread across too many tools.

## 23. SWE-bench: a benchmark for resolving real GitHub issues with language models — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/swe-bench/swe-bench)

**Source:** https://www.opensourceprojects.dev/post/66238fb3-37ee-4f13-b76a-f4233e92c3b4
**GitHub:** https://github.com/swe-bench/swe-bench
**Karakeep doc:** `jlgkwuqsa53g77ac6p2vdqrg`

SWE-bench is the benchmark that turned "can an LLM fix a real bug?" from a vibe into a number. MIT-licensed Python, ~5,900 stars, and it's been the de facto yardstick for coding agents since late 2023. The setup: 2,294 real GitHub issues pulled from 12 real Python repos (Django, Flask, SymPy, scikit-learn, and friends), each paired with the actual pull request that fixed it. Your agent gets the issue text and a snapshot of the codebase, then has to produce a patch. The patch is applied, the repo's real test suite runs, and if tests that failed before now pass, the issue counts as resolved. That's the clever part — no rubber-stamp unit tests, no synthetic toy problems. Just "did your patch actually make the tests go green." Models get scored on raw resolved rate, and the numbers have become marketing gold for every model lab in existence. There's a whole ecosystem now — SWE-bench Verified (a cleaner, decontaminated subset), SWE-Lancer for paid freelance work, and a leaderboard everyone fights over. The honest caveat: agents increasingly game it with test-time scaffolding and the benchmark has known contamination issues, which is why Verified exists. Still the standard. If you care whether an agent can actually code, this is the report card.

## 24. Self-hosted YouTube downloader with Plex, Jellyfin, and Emby sync — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/dialmasterorg/youtarr)

**Source:** https://www.opensourceprojects.dev/post/4862e17a-bbc5-4296-b365-4e0c7ea2f96d
**GitHub:** https://github.com/dialmasterorg/youtarr
**Karakeep doc:** `gi286849jlf6t3vukc6orq2b`

YouTarr is a self-hosted web app that automates downloading, organizing, and scheduling YouTube channel content, aimed squarely at the self-hosting crowd. TypeScript, ISC-licensed, ~1,600 stars, and it's very much alive — pushed within the last day. The pitch is "Sonarr, but for YouTube": you point it at channels, it watches for new uploads on a schedule, grabs them, tags them, and drops them into your media library with correct naming and metadata. It syncs out to Plex, Jellyfin, Emby, and Kodi, so your YouTube subscriptions show up next to your movies like they belong there. You get channel-level subscriptions, per-channel download settings, quality preferences, and the ability to keep only recent videos and prune the rest. It runs in Docker, which is the expected deployment story for this audience, and the web UI is clean enough that you don't need to live in a config file. The caveats are the usual ones for this genre: you're dancing around YouTube's terms of service, `yt-dlp` breaks occasionally when Google changes something, and you'll want a VPN or a dedicated box if you're grabbing a lot. But if you already run an *arr stack and want your subscriptions in the same place as everything else, this slots in nicely. It's niche, but it's the best niche tool going.

## 25. A CLI that crawls a site and turns every page into a PDF — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/dvcoolarun/web2pdf)

**Source:** https://www.opensourceprojects.dev/post/87af5bdc-c963-4db0-ac06-8f3310fe0999
**GitHub:** https://github.com/dvcoolarun/web2pdf
**Karakeep doc:** `bdt46xkl5jl9l0446to5pj6t`

web2pdf is a Python CLI that turns webpages into half-decent PDFs using WeasyPrint under the hood. It does batch conversion, so you can throw a pile of URLs at it and walk away. The recursive crawl mode is the killer feature — point it at a domain and it spiders same-domain links up to a configurable depth, converting every page into a separate PDF. Depth defaults to 2, and there's a rate limiter so you don't accidentally DDoS some poor blog. You get custom CSS, page numbers, auto-generated tables of contents, and multi-column layouts if you're feeling fancy. The `--assemble` flag even glues everything into one monster document. It's MIT licensed, sitting at ~1.3k stars, and clearly still early — the author asks for contributors like a man drowning. Install is a bit of a pain since WeasyPrint needs Cairo, Pango, and friends compiled first. The README's honest about it, which I respect. My one gripe: the top of the README is a sales pitch for DocuQueue, a paid hosted version starting at $9/mo. Fine, the guy's gotta eat. But the free tool itself does the job without any SaaS nonsense. For archiving documentation sites before they rot, it's genuinely handy. Just don't expect browser-perfect rendering on JS-heavy single-page apps.

## 26. Borg2 is in beta: deduplicating backups with authenticated encryption — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/borgbackup/borg)

**Source:** https://www.opensourceprojects.dev/post/60ab90c6-de2a-429f-8889-f93dd6d84e6c
**GitHub:** https://github.com/borgbackup/borg
**Karakeep doc:** `vpgz9pwt696v5cn3j1jj4xzb`

BorgBackup's 2.0 branch is finally in beta, and the headline change is real: authenticated encryption everywhere. The old `none` modes are dead. Every borg2 repo now carries a key, using AEAD ciphers like AES-256-OCB and ChaCha20-Poly1305, plus authenticated-sha256 and blake3 variants. That's a solid upgrade over the classic repokey/append-only dance. Borg itself remains what it's always been — a deduplicating archiver with compression, written in Python with Cython hot paths, BSD-3-Clause, 13.8k stars. The recent commit log is all about narrowing repair walks so `check --repair` only re-reads the packs it actually wrote. That's the kind of unglamorous correctness work that keeps your backups from silently eating themselves. It's still beta, so don't yeet your production backups onto it without testing restores first. But if you've been nursing borg1 repos along, borg2 is where the project is clearly going. The encryption change means no backward compatibility with older borg2 betas that used none-* modes — so anyone who jumped in early gets to rebuild. Painful, but the right call for a backup tool. Dedupe, compression, and now crypto you can actually trust. That's the whole pitch, and it's a good one.

### LinuxLinks (RSS)

## 27. sbomnix - generate Software Bills of Materials for Nix - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/SBOM-Tools-banner1.png)

**Source:** https://www.linuxlinks.com/sbomnix-generate-software-bills-materials-nix/
**GitHub:** https://github.com/tiiuae/sbomnix
**Karakeep doc:** `w2tc2tby0vc3oohp9ifch0hf`

sbomnix generates Software Bills of Materials for the Nix ecosystem, and it's the tool you didn't know your supply-chain audit needed. Feed it a flake reference, a derivation, or a store path, and it spits out CycloneDX or SPDX with the full dependency inventory. The Nix build-time versus runtime dependency split matters here, and sbomnix handles both — runtime by default, with an optional full build-closure inventory. When Nixpkgs metadata is available, it enriches packages with descriptions, licenses, maintainers, and homepages instead of leaving you with bare names. It's Apache-2.0, Python, 326 stars, from the Technology Innovation Institute. But sbomnix is really a toolbox: nixgraph visualizes dependency graphs, vulnxscan runs vulnerability scans on the generated SBOM (now with native SARIF 2.1.0 output), nix_outdated hunts stale deps by impact, and there's SLSA provenance tooling too. The recent commits are all about making SARIF fingerprints survive package version bumps — the kind of detail that tells you actual production users depend on this. If you run Nix anywhere near compliance or security, this is a no-brainer. The only real catch is the usual Nix catch: you should already be living in flakes to get the most out of it.

## 28. Linux PataOS – Debian-based distribution for engineering and design - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/04/Linux-Distributions.png)

**Source:** https://www.linuxlinks.com/linux-pataos-debian-based-distribution-engineering-design/
**GitHub:** N/A — project lives at linux-pataos.com
**Karakeep doc:** `oy2f2dg5azklkvsf4n6u2qel`

PataOS is a Debian-based desktop distro built around Cinnamon, aimed squarely at engineers, developers, and designers. The developer, Alessandro Patanè, comes from a CAD/engineering background and shaped it around programming, CAD, 3D modelling, electronics design, and multimedia work. So think FreeCAD, KiCad, and Blender territory rather than another generic Ubuntu respin. Privacy is a stated selling point — no unnecessary telemetry, no background data collection, plus firewall and permission-management tools baked in. That's a refreshing stance in an ecosystem where half the distros phone home to something. Under the hood it's thoroughly conventional: APT package management, systemd init, fixed release model, x86_64 only. Which is fine — conventional means stable, and stability is what you want when a broken dependency means a dead afternoon. It's active and maintained, per the Big List of Active Linux Distributions it's filed under. No GitHub repo surfaced for this one, which is a little unusual for a modern distro and makes me wonder how transparent the source actually is. The homepage is your only real window into it. Worth a look if you're tired of distro-hopping and want something tuned for actual engineering work instead of wallpaper prettiness.

## 29. Best Free and Open Source Alternatives to Google Cloud Build - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/Open-Source-Alternatives.png)

**Source:** https://www.linuxlinks.com/best-free-open-source-alternatives-google-cloud-build/
**GitHub:** roundup — see alternatives below
**Karakeep doc:** `u6oonpr9qms5zmuz9vkr1els`

**Projects:**

- **[Woodpecker](https://github.com/woodpecker-ci/woodpecker)** — Lightweight self-hosted CI/CD engine driven by YAML pipeline config
- **[Tekton](https://tekton.dev/)** — Vendor-neutral Kubernetes-native framework for building CI/CD systems
- **[Concourse](https://concourse-ci.org/)** — Container-based CI/CD system built around pipelines, resources and jobs
- **[Jenkins](https://www.jenkins.io/)** — Self-contained open-source automation server for CI/CD
- **[Buildbot](https://buildbot.net/)** — Python-based continuous integration and build automation framework

LinuxLinks lines up five self-hosted ways to drop Google Cloud Build, and the framing is blunt: Cloud Build is proprietary, and the "free" managed service is a lock-in funnel. Woodpecker gets top billing — a lightweight, self-hosted CI/CD engine with container-based steps and YAML config that'll feel familiar to Cloud Build refugees. Tekton is the Kubernetes-native pick, a vendor-neutral CRD framework for CI/CD, great if you already run a cluster. Concourse goes its own way with resources, tasks, and jobs, betting on reproducible, declarative pipelines. Jenkins needs no introduction — the oldest and broadest of the bunch, with a plugin ecosystem that's both its strength and its maintenance tax. Buildbot rounds it out as the Python-configurable framework for weird, customised build setups. The through-line in every entry is the same trade-off: you give up Google's hands-off management and gain control, at the cost of operating your own infrastructure. None of them is a drop-in replacement, and the article doesn't pretend otherwise. If you're self-hosting a homelab CI already, Woodpecker is the least painful on-ramp. If Kubernetes is your life, Tekton. Pick your poison.

## 30. 20 Best Free and Open Source Linux CAD Software - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/02/worker-drawing-blueprint.jpg)

**Source:** https://www.linuxlinks.com/cad/
**GitHub:** https://github.com/FreeCAD/FreeCAD (flagship)
**Karakeep doc:** `e99h3ftvoqrlclms41my2jtk`

**Projects:**

- **[FreeCAD](https://www.freecad.org/)** — FreeCAD, the open source 3D parametric modeler
- **[QCAD](https://qcad.org/en/)** — QCAD is a free, open source 2D CAD system for Windows, Linux and Mac
- **[LibreCAD](https://librecad.org/)** — CAD in two dimensions
- **[BRL-CAD](https://brlcad.org/)** — Constructive Solid Geometry (CSG) solid modeling system
- **[OpenCASCADE](https://occt3d.com/open-cascade-technology/index.html)** — Explore OCCT (Open CASCADE Technology) for 3D modeling, visualization and CAD data exchange. Find documentation, downloads and engineering support
- **[SALOME](https://www.salome-platform.org/)** — Platform for numerical simulation
- **[OpenSCAD](https://openscad.org/)** — Programmers solid 3D CAD modeller
- **[KiCad](https://www.kicad.org/)** — A Cross Platform and Open Source PCB Design Suite
- **[Chili3D](https://github.com/xiangechen/chili3d)** — A 3D CAD running entirely in the browser. Contribute to xiangechen/chili3d development by creating an account on GitHub
- **[LeoCAD](https://www.leocad.org/)** — CAD application for designing virtual models with LEGO&reg; bricks
- **[SolveSpace](https://solvespace.com/)** — Parametric 3d CAD tool
- **[CadQuery](https://cadquery.readthedocs.io/en/latest/)** — Python parametric CAD scripting framework
- **[Electric](https://www.staticfreesoft.com/)** — The Electric VLSI Design System
- **[gCAD3D](https://gcad3d.org/)** — gCAD3D CADCAM software for Linux and Windows
- **[XTrackCAD](https://github.com/ankon/xtrkcad)** — CAD program for designing model railroad layouts (GitHub import of the SourceForge master)
- **[KLayout](https://github.com/KLayout/klayout)** — KLayout Main Sources. Contribute to KLayout/klayout development by creating an account on GitHub
- **[Dune 3D](https://dune3d.org/)** — Dune 3D is parametric 3D CAD application
- **[CAD Sketcher](https://github.com/hlorus/CAD_Sketcher)** — Constraint-based geometry sketcher for blender. Contribute to hlorus/CAD_Sketcher development by creating an account on GitHub
- **[build123d](https://github.com/gumyr/build123d)** — A python CAD programming library. Contribute to gumyr/build123d development by creating an account on GitHub
- **[Design](https://github.com/dubstar-04/Design)** — 2D CAD For GNOME. Contribute to dubstar-04/Design development by creating an account on GitHub

Autodesk killed Unix support in 1994 and has zero interest in coming back, so anyone who wants real CAD on Linux is stuck with Wine and a credit card. This listicle rounds up 20 free alternatives instead, and the spread is genuinely useful. FreeCAD is the headline act — full parametric 3D solid modeling with a CAE workbench, the closest Linux gets to a SolidWorks replacement, and it's actually good now. QCAD and LibreCAD cover the 2D drafting crowd, with LibreCAD as the actively maintained fork of QCad's community edition. OpenSCAD, CadQuery, and build123d are for people who'd rather type geometry than click it — programmer's CAD where the model is code. BRL-CAD brings old-school Constructive Solid Geometry, OpenCASCADE is the modeling kernel underpinning half the other tools, and SALOME does numerical simulation. KiCad sneaks in as the PCB-design pick, LeoCAD is there for virtual LEGO, and SolveSpace handles constraint-based sketching with a tiny footprint. The list is a grab bag of niches, not a ranked battle. But if you ignore everything else and just install FreeCAD, you'll be fine for most mechanical work.

## 31. Neko - self-hosted virtual browser and remote desktop - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/04/050-videoconference.png)

**Source:** https://www.linuxlinks.com/neko-self-hosted-virtual-browser-remote-desktop/
**GitHub:** https://github.com/m1k1o/neko
**Karakeep doc:** `quiurn8qswr8wigzthwvz42l`

Neko is a self-hosted virtual browser that runs a full desktop or browser inside Docker and streams it to your own browser over WebRTC. Go on the backend, TypeScript/Vue on the frontend, Apache 2.0, and a healthy 22.4k stars with 1.6k forks. The origin story is peak open source: rabbit.it died, the author's internet couldn't handle streaming anime to friends, Discord kept crashing, and he wanted to watch anime together, so he built the damn thing. Multiple people can jump into the same session and share the keyboard and mouse, which makes it genuinely useful for watch parties, teaching, pair-debugging, and support sessions. State — cookies, logins, tabs — stays on the server, so you get disposable browser sessions that don't pollute your local machine, or persistent ones for stuff you want to keep. m1k1o forked it from nurdism/neko after the original author archived the project, and it now ships Firefox, Chromium-family, and Tor variants plus XFCE and KDE desktops. There's a companion `neko-rooms` app for managing multiple rooms, and RTMP out for broadcasting. If you've ever wanted a browser-as-a-jump-host, this is the cleanest way to get one.

## 32. RTAB-Map - graph-based SLAM and 3D mapping application - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2018/08/Robotics.jpg)

**Source:** https://www.linuxlinks.com/rtab-map-graph-based-slam-3d-mapping-application/
**GitHub:** https://github.com/introlab/rtabmap
**Karakeep doc:** `hl7e7b4sl1b0mv1oz01ym3np`

RTAB-Map (Real-Time Appearance-Based Mapping) is a graph-based SLAM library and standalone app from IntRoLab, written in C++ under BSD 3-Clause. It's the thing your robot uses to figure out where it is by remembering what places look like. It feeds on RGB-D cameras, stereo rigs, and 3D lidar, then runs appearance-based loop-closure detection with a bag-of-words matcher to recognize when the bot has driven back into territory it's seen before. Accepted loop closures add constraints to a pose graph that gets optimized with g2o, GTSAM, or Ceres to scrub accumulated drift. A memory-management layer caps how many locations get considered so it doesn't choke on big environments. It ships a Qt GUI plus command-line tools, integrates cleanly with ROS and ROS2, and dumps point clouds, textured meshes, occupancy grids, and estimated poses. There's even Android and iOS support left over from the old Project Tango days. 4k stars, 958 forks, and 3,696 commits with a merge literally yesterday — this thing is actively maintained by Mathieu Labbé and nowhere near abandoned. If you're doing serious robotics mapping, this is a default pick, not a novelty.

## 33. 22 Best Free and Open Source Linux Video Editors - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/09/video-editing.jpg)

**Source:** https://www.linuxlinks.com/videoeditors/
**GitHub:** https://github.com/KDE/kdenlive (flagship)
**Karakeep doc:** `hkk76d2hi6xpqczoq8mabc02`

**Projects:**

- **[OpenShot](https://www.openshot.org/)** — OpenShot is an award-winning free and open-source video editor for Linux, Mac, and Windows. Create videos with exciting video effects, titles, audio tracks, and animations
- **[Shotcut](https://www.shotcut.org/)** — Shotcut is a free, open source, cross-platform video editor for Windows, Mac and Linux
- **[Kdenlive](https://kdenlive.org/en/)** — Non-linear video editor for KDE
- **[LosslessCut](https://github.com/mifi/lossless-cut)** — The swiss army knife of lossless video/audio editing
- **[Blender](https://www.blender.org/)** — The Freedom to Create
- **[Editly](https://github.com/mifi/editly)** — Slick, declarative command line video editing & API
- **[Flowblade](https://github.com/jliljebl/flowblade)** — Video Editor for Linux. Contribute to jliljebl/flowblade development by creating an account on GitHub
- **[PiTiVi](https://www.pitivi.org/)** — Non-linear audio/video editor using GStreamer
- **[LiVES](https://github.com/salsaman/LiVES)** — LiVES is a feature rich application which combines elements of VJ and video editing software. The current version runs on Linux / BSD. Check_out_the_new_discussion_area https://github.com/salsama
- **[Avidemux](http://fixounet.free.fr/avidemux/)** — Designed for simple cutting, filtering and encoding tasks
- **[lazycut](https://github.com/ozemin/lazycut)** — A simple terminal UI for video trimming. Contribute to ozemin/lazycut development by creating an account on GitHub
- **[Auto-Editor](https://auto-editor.com/)** — Automatically edit video and audio by analyzing where sections are silent or still and cut them out
- **[VidCutter](https://github.com/ozmartian/vidcutter)** — A modern yet simple multi-platform video cutter and joiner.
- **[Vimix](https://github.com/brunoherbelin/vimix)** — Live Video Mixer. Contribute to brunoherbelin/vimix development by creating an account on GitHub
- **[Video Trimmer](https://flathub.org/apps/org.gnome.gitlab.YaLTeR.VideoTrimmer)** — Trim videos quickly
- **[OpenCut](https://github.com/opencut-app/opencut)** — The open-source CapCut alternative. Contribute to OpenCut-app/OpenCut development by creating an account on GitHub
- **[Olive](https://github.com/olive-editor/olive)** — Free open-source non-linear video editor. Contribute to olive-editor/olive development by creating an account on GitHub
- **[Cinelerra](https://www.cinelerra-gg.org/en)** — Free and open source professional video editing software for Linux. 8K support, 400+ codecs, motion tracking, and more
- **[Footage](https://gitlab.com/adhami3310/Footage)** — 
- **[GoZen](https://codeberg.org/gozen/gozen)** — This project moved to https://codeberg.org/gozen/gozen. The minimalistic video editor made with Godot.
- **[Drift](https://github.com/CutWire-Studios/Drift)** — Drift is a free, open-source, beginner-friendly desktop video editor built with Qt 6 and FFmpeg.
- **[VideoCut](https://github.com/kanehekili/VideoCut)** — MPEG2,MP4,MKV,WEBM Cutter for Linux using MPV and libavcodec or ffmpeg. Cutting is lossless, the target file will not be reencoded

Linux video editing used to be a sad joke, but the MLT and GStreamer frameworks dragged it out of the gutter, and now there are 22 editors fighting for your timeline. Kdenlive is the KDE powerhouse, Shotcut is the cross-platform workhorse, and OpenShot is the beginner-friendly pick that somehow tops the ratings chart — a call one commenter is still mad about, demanding to know why OpenShot beats Kdenlive by 0.3 points. LosslessCut is the swiss-army knife for chopping clips without re-encoding, and it's the one you'll actually reach for when you just need to trim a screen recording. Blender shows up as a 3D suite that also edits video, Editly does declarative editing from Node.js and ffmpeg config, and Avidemux handles the quick-cut-and-filter jobs. Olive is the ambitious upstart, Flowblade and PiTiVi round out the NLEs, and there's a pile of niche cutters — VidCutter, lazycut, Video Trimmer, Auto-Editor, Vimix for live mixing. The list skews from "prosumer NLE" to "glorified trim tool," so the real verdict is: pick Kdenlive or Shotcut and stop reading. The rest are for when you need one specific thing.

## 34. Molsketch - 2D molecular structure editor - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/Chemical-Structure-Drawing-Banner.png)

**Source:** https://www.linuxlinks.com/molsketch-2d-molecular-structure-editor/
**GitHub:** https://github.com/hvennekate/Molsketch
**Karakeep doc:** `lrkjulmbbkssl8ek71kblgj6`

Molsketch is a Qt-based editor for drawing 2D chemical structures, written in C++ and released under GPL v2. It's the kind of tool a chemist reaches for instead of paying for ChemDraw, and it covers the fiddly stuff: reaction arrows, equilibrium arrows, mechanism arrows, lone pairs, radical electrons, brackets, frames, and free text. You get a periodic-table-style element picker, control over bond width and atom fonts, and structure-cleanup and alignment tools so your benzene rings don't look drunk. OpenBabel integration is the real win — it extends import/export to a pile of chemistry formats and can even optimize coordinates. Output goes to SVG, PNG, BMP, and JPEG. The repo is a fork from timvdm/Molsketch maintained by Hendrik Vennekate, and it's a small operation: 19 stars, 7 forks, 1,217 commits, last real commit an OpenBabel blunder fix back in October 2025. That's the honest caveat — this is a slow-moving niche project, not a thriving community. But if you just need to draw a molecule and export it without selling a kidney, it does the job. Binaries live on SourceForge if you don't want to build from source.

## 35. Kokoro - Open-Weight Text-to-Speech Model — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2022/11/speech-neural.jpg)

**Source:** https://www.linuxlinks.com/kokoro-open-weight-text-to-speech-model/
**GitHub:** https://github.com/hexgrad/kokoro
**Karakeep doc:** `bkl0lnrtjh73bq5wgkg6jpgw`

Kokoro is an open-weight text-to-speech model that spits out natural-sounding speech from plain text, and unlike the bloated hosted cloud TTS services, it runs entirely on your own hardware. The thing is tiny by modern standards — a hair over 82 million parameters, Apache 2.0 licensed, so you can actually read and reuse the damn weights. That's the whole pitch: small, local, and good enough to not sound like a Speak & Spell.

It ships 54 voices across American and British English, Spanish, French, Hindi, Italian, Japanese, Brazilian Portuguese, and Mandarin. Eight British voices alone — four female, four male — with names like `bf_emma` and `bm_george`. Speed control, custom phoneme pronunciations for weird names and acronyms, and a CLI that reads stdin or a text file straight to WAV at 24 kHz.

The catch is installation on bleeding-edge distros. Ubuntu 26.04 bundles Python 3.14.4, which is too new for Kokoro's deps, so LinuxLinks' reviewer had to spin up a Python 3.12 venv with `uv` to avoid nuking system Python. Mildly annoying, not a dealbreaker.

For anyone who wants local TTS without renting a GPU cluster or sending their text to a server somewhere, it's worth a serious look. Just don't expect SSML-grade prosody control.

## 36. JFFS2 - log-structured file system for raw flash storage — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2021/10/find-duplicates.png)

**Source:** https://www.linuxlinks.com/jffs2-log-structured-file-system/
**GitHub:** https://github.com/torvalds/linux (in-tree; site: https://sourceware.org/jffs2/)
**Karakeep doc:** `kuxtqobon1usfn5808keofe2`

JFFS2 is a log-structured file system built for raw flash storage in embedded systems, sitting directly on the kernel's Memory Technology Device (MTD) layer instead of hiding behind a translation layer that fakes a disk. Raw flash is hostile: erases happen per-block, blocks die after a finite number of cycles, and NAND limits repeated writes to a page. JFFS2 just accepts that and works around it.

The clever bits: it writes file data and metadata as nodes rather than updating fixed locations in place, tracks individual erase blocks so garbage collection can cherry-pick what to reclaim, and does on-the-fly compression to squeeze more out of the flash. It also throws in wear-levelling so erase cycles don't pile up on one unlucky block, and stores CRCs to catch corruption. No on-media index means mounting requires a full medium scan, and memory use grows with size — which is exactly why it scales worse than UBIFS on big flash.

It's GPLv2, originally from Red Hat, and baked into the kernel tree. There's no standalone GitHub repo because it's part of Linux itself. Fine for modest NOR/NAND devices in routers and set-top boxes. Don't reach for it when the flash gets large.

## 37. RakuOS - hybrid atomic Fedora-based distribution — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/04/Linux-Distributions.png)

**Source:** https://www.linuxlinks.com/rakuos-hybrid-atomic-fedora-based-distribution/
**GitHub:** https://github.com/RakuOS/rakuos-base
**Karakeep doc:** `guemhcvmxswafa7kxqif8oov`

RakuOS is a Fedora-based hybrid atomic distro that tries to have it both ways: an immutable bootc OCI base image that updates transactionally, with a persistent overlay on `/usr` so you can still install native RPM packages without rebuilding the whole image. That's the actual innovation here — it dodges the rpm-ostree "layering hell" that makes Fedora Silverblue such a chore.

It ships a package manager called `rum`, built for the overlay rather than bolted onto dnf, plus a GUI Software Center. Terra repos come enabled by default for extra codecs and hardware support. The P03 kernel is tuned for desktop responsiveness, and it leans hard into gaming — Steam, Lutris, and Heroic install natively, no Flatpak sandbox bullshit. Secure Boot with local key enrolment, live install media for x86_64, and AMD/Intel/Nvidia graphics all supported.

The caveat is right there in the fine print: RakuOS calls itself an early-development project and admits the persistent overlay tech is still experimental. Desktops on offer are KDE Plasma, GNOME, COSMIC, and niri.

It's an interesting bet — if the overlay holds up, this solves the biggest pain point of atomic Linux. If it doesn't, you're beta-testing someone's filesystem ideas on your daily driver.

## 38. 23 Best Free and Open Source Linux Computer Algebra Systems — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2018/11/maths-software.jpg)

**Source:** https://www.linuxlinks.com/best-free-linux-computer-algebra-systems/
**GitHub:** (roundup — 23 projects; e.g. https://github.com/sympy/sympy, https://github.com/sagemath/sage)
**Karakeep doc:** `wznqmuuu0nbqbmlrdoldf8p1`

**Projects:**

- **[Scilab](https://www.scilab.org/)** — Numerical computational package
- **[Maxima](https://maxima.sourceforge.io/)** — Computer algebra system written in Lisp, based on DOE-MACSYMA
- **[Octave](https://octave.org/)** — GNU Octave is a programming language for scientific computing
- **[SageMath](https://www.sagemath.org/)** — SageMath is a free and open-source mathematical software system
- **[SymPy](https://www.sympy.org/en/index.html)** — Python library for symbolic mathematics
- **[SINGULAR](https://www.singular.uni-kl.de/)** — Computer Algebra System for polynomial computations
- **[Macaulay2](https://macaulay2.com/)** — Macaulay2 home page
- **[Cadabra](https://cadabra.science/)** — Cadabra is a symbolic computer algebra system designed to solve problems in classical and quantum field theory
- **[PARI/GP](https://pari.math.u-bordeaux.fr/)** — Widely used algebra system designed for fast computations in number theory
- **[GAP](https://www.gap-system.org/)** — GAP system for computational discrete algebra, especially computational group theory
- **[FriCAS](https://github.com/fricas/fricas)** — Official repository of the FriCAS computer algebra system
- **[CoCoA](https://sites.google.com/view/cocoa-cocoalib)** — CoCoA-5 and CoCoALib, computations in commutative algebra
- **[Mathics](https://mathics.org/)** — General-purpose CAS with Mathematica-compatible syntax and functions
- **[FORM](https://github.com/form-dev/form)** — The FORM project for symbolic manipulation of very big expressions
- **[Nelson](https://nelson-lang.github.io/nelson-website/)** — Nelson
- **[wxMaxima](https://wxmaxima-developers.github.io/wxmaxima/)** — GUI for the sublime Maxima CAS
- **[Xcas](https://xcas.univ-grenoble-alpes.fr/en.html)** — Cross-platform mathematical environment
- **[REDUCE](https://reduce-algebra.sourceforge.io/)** — General-purpose computer algebra system for symbolic computation
- **[OSCAR](https://github.com/oscar-system/Oscar.jl)** — A comprehensive open source computer algebra system for computations in algebra, geometry, and number theory.
- **[Axiom](https://github.com/daly/axiom)** — Axiom is a free, open source computer algebra system
- **[Symja](https://matheclipse.org)** — Computer algebra system and symbolic mathematics library
- **[CGSuite](https://github.com/aaron-siegel/cgsuite)** — A computer algebra system for research in combinatorial game theory
- **[Eigenmath](https://github.com/georgeweigt/eigenmath)** — Symbolic math app. Contribute to georgeweigt/eigenmath development by creating an account on GitHub

This is a listicle, not a single tool — 23 free, open-source computer algebra systems, the kind of software that manipulates formulae symbolically instead of grinding out decimal approximations. A CAS gives you exact answers, not floating-point garbage, and handles linear algebra, calculus, and differential equations the way a calculator can't.

The headline names are all here. Maxima, the old warhorse descended from MIT's Macsyma, still does symbolic and numeric manipulation. SageMath is the giant kitchen-sink alternative to Mathematica and Maple, bundling a dozen packages under one Python roof. SymPy is the pure-Python library you can import straight into your own code. Then there's PARI/GP for number theory, GAP for discrete algebra, SINGULAR and Macaulay2 for polynomial and algebraic geometry work, Cadabra for field theory, FriCAS (an Axiom fork), REDUCE, and CoCoA.

The list also drags in things that are barely CAS-adjacent — Scilab, Octave, and Nelson are numerical languages, not symbolic ones. That's the usual LinuxLinks padding, so don't expect a razor-sharp category boundary.

If you want symbolic math without a Mathematica license, this is a decent map. Just know some entries earn their spot more than others.

## 39. OpenPonk - metamodeling platform and modeling workbench — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/01/UML-Diagrams.png)

**Source:** https://www.linuxlinks.com/openponk-metamodeling-platform-modeling-workbench/
**GitHub:** https://github.com/OpenPonk/openponk
**Karakeep doc:** `weezzbmodfyo13pog2exakui`

OpenPonk is a metamodeling platform and graphical modeling workbench built on Pharo, the Smalltalk environment — which already tells you this is a niche tool for people who like their UML served with a side of obscure language. The idea is a shared workbench that you extend through plugins rather than a single locked-in notation.

It supports a genuinely broad spread: UML class diagrams with XMI, OntoUML for ontology-driven conceptual modeling, BPMN business processes, finite state machines, Petri nets with weighted arcs, entity-relationship diagrams, Markov chains, DEMO notation, and object-relation diagrams. Models can also be poked programmatically from Pharo, and it uses Roassal for the interactive visualization bits.

The pitch is that modeling doesn't stop at drawing boxes — it aims at execution, simulation, and source code generation too. MIT licensed, runs on Linux and other desktop platforms.

The catch is the ecosystem. Pharo isn't exactly a mainstream choice, so the community is small and you're betting on a Smalltalk stack. If you need UML quickly, PlantUML or Mermaid will get you a diagram faster. If you want a real metamodeling platform with simulation hooks, OpenPonk is a serious answer — just don't expect a giant user base behind it.

## 40. 4 Best Free and Open Source Perl Linter Tools - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/02/034-proofreading.png)

**Source:** https://www.linuxlinks.com/best-free-open-source-perl-linter-tools/
**GitHub:** https://github.com/ (roundup — multiple projects, see below)
**Karakeep doc:** `cjkengfdhcg1te91emh5v77e`

**Projects:**

- **[Perl::Critic](https://github.com/Perl-Critic/Perl-Critic)** — The leading static analyzer for Perl. Configurable, extensible, powerful.
- **[Perltidy](https://github.com/perltidy/perltidy)** — Perl::Tidy, a source code formatter for Perl
- **[zarn](https://github.com/htrgouvea/zarn)** — A lightweight static security analysis tool for modern Perl Apps
- **[perl-lsp](https://github.com/tree-sitter-perl/perl-lsp)** — perl-lsp — a fast Perl language server in Rust with cross-file type inference, completion, goto-def, and rename. Built on tree-sitter-perl and tower-lsp.

LinuxLinks doing its usual "best free and open source" roundup dance, this time for Perl linters. Four tools make the cut. **Perl::Critic** is the heavyweight: an extensible framework for creating and applying coding standards, effectively the Perl equivalent of ESLint with policies you can crank up or dial down. **Perltidy** isn't technically a linter — it indents and reformats Perl scripts, which is arguably half the battle when you inherit someone else's 2002 spaghetti. **zarn** does static security analysis for both source code and dependencies, which is a genuinely different beast from style checking and probably the most useful entry on the list for real-world codebases. **perl-lsp** is a Language Server Protocol implementation, so you get lint-ish diagnostics inline in whatever editor talks LSP. The author is refreshingly honest for a roundup: linters aren't a quick fix, can be a distraction, and may be useless on old, large codebases. Fair point. If you're actually maintaining legacy Perl, Perl::Critic plus Perltidy is the combo that saves your sanity. The rest is nice-to-have.

## 41. Select Default Application - graphical MIME association manager - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2022/06/170y-utilities.jpg)

**Source:** https://www.linuxlinks.com/select-default-application-graphical-mime-association-manager/
**GitHub:** https://github.com/Tenshou170/selectdefaultapplication-Qt6
**Karakeep doc:** `okklqk99tyurygimqys8mwka`

A Qt6 GUI tool for managing default applications on Linux, and it actually knows what it's doing with the XDG MIME Apps spec. Written in C++17 under GPL-3.0. The killer feature is **granular conflict resolution** — when you try to set an association that clashes with an existing default, you get a checkbox dialog to pick exactly which MIME types to overwrite instead of nuking everything. It correctly respects desktop-specific overrides and system-wide defaults, which is where half the other MIME managers quietly fall over. Application-centric UI: pick an app, see everything it supports and what it currently handles. Full icon theming, search by name, filter MIME types by category, and a three-panel layout that opens at a comfortable 1000×600. Also has verbose logging behind a `-V` flag so you can debug your own `mimeapps.list` without drowning in Qt noise. Seven stars, so it's basically one developer's labour of love. If xdg-open's cryptic fallback behaviour has ever made you rage-quit, this is the GUI that makes it stop.

## 42. Broadcast Box - sub-second WebRTC broadcasting - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/04/024-video-conference.png)

**Source:** https://www.linuxlinks.com/broadcast-box-sub-second-webrtc-broadcasting/
**GitHub:** https://github.com/Glimesh/broadcast-box
**Karakeep doc:** `mz9fdcsqgkgvh766fhqixjnq`

"A broadcast, in a box" — Glimesh's open-source tool for streaming to friends in sub-second time over WebRTC. Written in Go, MIT license, 2.3k stars, so it's not some toy. The point is latency: standard OBS over RTMP gives you ~2 seconds, but Broadcast Box drops that to near-zero by using WebRTC with WHIP. You point OBS at the `/api/whip` endpoint with any stream key you like, and that same key is what your viewers use to watch. Works with OBS, browser publishing, FFmpeg, and GStreamer, plus an admin portal and stats. There's even a public instance at b.siobud.com you can play with for free. Design is deliberately simple and modifiable — the whole thing is meant to be self-hostable and poked at. If you've ever wanted Twitch-level low latency without Twitch, or a private screen-share that doesn't route through some corporate relay, this is it. Docker compose, reverse proxy support, webhooks, stream profile policies — the works. Genuinely impressive for a side-project-turned-infrastructure.

## 43. pyiron_atomistics - atomistic simulation and workflow environment - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/Chemistry-Workflow-banner.png)

**Source:** https://www.linuxlinks.com/pyiron_atomistics-atomistic-simulation-workflow-environment/
**GitHub:** https://github.com/pyiron/pyiron_atomistics
**Karakeep doc:** `fb8ccp19spnsigyosun3ym6n`

pyiron_atomistics is a Python IDE for atomistic simulation in computational materials science — and it's a big deal in its niche, even if 55 stars undersells it. BSD-3-Clause, developed at the Max Planck Institute for Sustainable Materials (Joerg Neugebauer's department) with ICAMS joining later for high-throughput work. It glues together the pieces you'd otherwise duct-tape yourself: ASE-compatible atomic structure objects, simulation codes like LAMMPS and VASP, hierarchical data management over SQL and HDF5, NGLview visualization, and Jupyter-notebook protocols. The pitch is "feedback loops" — constructing dynamic simulation life cycles where one run's output feeds the next, scaled from a single job to high-throughput sweeps. Released open source in 2018 after years as an internal framework for ab initio thermodynamics. This is research infrastructure, not a weekend project: if you're doing DFT or molecular dynamics at scale and tired of hand-rolling job management scripts, pyiron is the grown-up answer.

## 44. handlr-regex - manage default applications with regular expressions - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2022/06/170y-utilities.jpg)

**Source:** https://www.linuxlinks.com/handlr-regex-manage-default-applications-regular-expressions/
**GitHub:** https://github.com/Anomalocaridid/handlr-regex
**Karakeep doc:** `lxg22lxvmd2najoacolt9goo`

A fork of the original `handlr` that adds regular-expression handlers to the mix, written in Rust under MIT. The core value prop is simple: set your default apps by extension or MIME type with commands like `handlr set .png feh.desktop`, no more digging through `xdg-mime`'s forgettable incantations. The regex fork takes it further — you can match arbitrary commands to a pattern, plus wildcards like `text/*` to route all text files to nvim. It does intelligent MIME detection from both extension and content, opens multiple files at once, and lets you register several handlers then pick one at runtime with rofi or dmenu. Bonus: it auto-prunes invalid `.desktop` entries from your `mimeapps.list`, which is the kind of quiet cleanup nobody asked for but everyone needs. Helper commands like `get --json` and `mime --json` make it scriptable, and the README proudly notes it's "unnecessarily fast" — a single Rust binary with zero dependencies. If you've ever wanted xdg-utils to just shut up and work, this is the replacement.

### RSS — Other

## 45. Omacom Foundation to be premier sponsor of 0xSero's work on local AI — by Omarchy

![Omarchy](https://omarchy.org/brand/social/hackerman.png)

**Source:** https://omarchy.org/news/2026/09/omacom-foundation-to-be-premier-sponsor-of-0xsero
**Karakeep doc:** `d3sl7v7h5ofd1d44gko7qe70`

The Omacom Foundation is dropping a three-year premier sponsorship on 0xSero's local AI work, funneled through his company Sybil Solutions. The goal is to make local models work beautifully out of the box on Omarchy. Right now, the piece argues, there's too much goddamn homework between buying a beefy computer and actually putting its intelligence to use. Picking a model, tuning it to the hardware, wiring it to your agents — that should be a first-run experience, not a weekend project. Sero's already on it with his Local AI Registry, a GitHub repo packing model configs, hardware-specific recipes, and performance measurements. That's the raw material for good defaults. The vision goes further: a mesh of intelligence across the machines you already own — your laptop, the desktop in the office, the box at home — letting agents draw on whatever compute you've got without turning you into a data-center operator first. They name-drop NVIDIA's N1x and Alibaba's Qwen Book as signs powerful local AI hardware is becoming ordinary personal computing. The honest pitch: an alternative to subscription-based frontier models for the work people actually do. Omarchy says it'll keep supporting frontier models too, but this buys the choice to run intelligence on hardware you control. Three years is a real commitment, funded by patrons.
