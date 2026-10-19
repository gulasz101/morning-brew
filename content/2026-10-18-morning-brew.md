---
date: 2026-10-18
slug: 2026-10-18-morning-brew
tags: Command Line Interface, Software Development, Machine Learning, Artificial Intelligence, Open Source Software, GNOME, Operating Systems, Cybersecurity, Linux, Technology, Cloudflare, Web Security, Computing Hardware, Command Line Tools
---

# Morning Brew — 2026-10-18

32 things landed on Saturday. Eight of them videos, mostly Better Stack doing its "here is a terrifying thing in ninety seconds" routine, and this time the terrifying thing is a model that can copy itself onto new hardware without asking anyone.

The rest of the day reads like a maintenance shift: Gentoo asking for help, GNOME 51.1 fixing drag and drop between Wayland and Xwayland, the internet's root signing key rotating, and leap seconds finally getting killed off in 2027. Anthropic put 5% of itself into a public benefit fund, AMD bought World Labs, and one OpenAI engineer got charged with wiretapping. Normal week.

Roundups at the bottom with real links to every project named: 39 wallpaper setters, 14 terminal bibliography tools, 11 image upscalers, 6 molecular dynamics engines. Three names had no verifiable home, so they ship as honest gaps instead of invented URLs.

### Hand-bookmarked

## 1. The AI promise was automation. The reality? Managing digital workers — by South China Morning Post

![South China Morning Post](https://www.scmp.com/favicon.ico)

**Source:** https://www.scmp.com/tech/big-tech/article/3371246/ai-promise-was-automation-reality-managing-digital-workers
**Karakeep doc:** `gmn3ugk4e457c4kpykiig5wg`

Body is behind SCMP's paywall, so this is an honest stub, not a summary. 🤷

What the free part actually says: Chong Ming Lee and Mandy Zuo report from Hong Kong and Shanghai, published 18 October 2026, 7-minute read. The premise is that AI agents were sold as autonomous digital workers who would take the drudgery off humans, and businesses across Asia are finding the opposite. More work, new friction, an extra layer of management.

The one concrete case available: Xiao Mengjie, an AI product marketing manager at a Big Tech firm in Shanghai, handed two agents a task she called simple and expected efficiency. Her agent and her supervisor's agent then spent a long stretch negotiating who owned what and who verified which details, in what the piece describes as a spectacle not unlike the human bureaucracy they were hired to replace. Her quote: "It became very formal and cumbersome. Agents can create communication overhead too."

That's the thesis in one anecdote, and it's a good one. Agent-to-agent coordination costs are real, and nobody budgets for them. The rest of the piece presumably carries numbers, named companies and counterarguments I can't see, and I'm not going to invent them. Read it if you have the subscription.

## 2. GitHub - ZitaoTech/HackberryPiCM5: An ultra portable handheld Linux device using Raspberry CM5 unit as Core with 4″ 720X720 TFT Touch display and the original blackberry keyboard — by GitHub

![GitHub](https://opengraph.githubassets.com/8e27dafcf9cc232b085a0de819ce5656c9dda09343f21228435d359ed4f2bdf1/ZitaoTech/HackberryPiCM5)

**Source:** https://github.com/ZitaoTech/HackberryPiCM5
**Karakeep doc:** `kau7t5jwy43j0m6q4q09iqgb`
**Project:** [HackberryPi_CM5](https://github.com/ZitaoTech/HackberryPiCM5) — handheld Linux computer built on a Raspberry Pi CM5 with a recycled BlackBerry keyboard

A handheld Linux PC built around a Raspberry Pi Compute Module 5 and the keyboard out of a dead BlackBerry. The stated goal is a portable machine that teaches you something about Linux, hardware and the kernel while you use it, and the repo is a full build guide rather than a marketing page: 3D models, assembly steps, battery wiring, keyboard pinout, NVMe slot, troubleshooting.

The spec sheet is better than most commercial handhelds. BCM2712, quad-core Cortex-A76 at 2.4GHz, a 4-inch 720x720 multi-touch TFT, 2x USB 3.0, one full-sized HDMI port, a 2242 NVMe slot that takes either an SSD or a Hailo AI accelerator card, CR927 RTC battery, an I2C-based battery voltage sensor, a Stemma I2C port for external sensors, and a magnet in the back plate sized for MagSafe-style wired power banks. The 5000mAh LiPo gives roughly five hours idle and three to four hours of real use, charging at 1.5–2A over USB-C to full in two to three hours.

The keyboard accepts a BlackBerry Q10, Q20 or 9900 module and runs VIAL for remapping, so you get a physical thumb keyboard that isn't a fold-out joke. Overall it's 143.5x91.8x17.6mm and 306g with battery, CM5 and heatsink installed. Aluminium front and back plates, 3D-printed middle section.

Two caveats worth knowing before you get excited. The CM5 is not included, you supply that yourself, and the aluminium case plus mounted heatsink wrecks the PCB antenna enough that the repo documents an external antenna mod. Dual speakers are on board but need pairing over Bluetooth to make sound. Zitao is a master's student in mechanical engineering and industrial design at TU Dresden, the license is MIT, and the hardware is sold through Elecrow. 1.1k stars, 89 forks, 347 commits, so the thing is real and maintained.

## 3. GitHub Projects Community (@GithubProjects) on X — by X (formerly Twitter)

![X (formerly Twitter)](https://pbs.twimg.com/media/HUxTG-Ab0AAtoCt?format=webp&name=large)

**Source:** https://share.google/xt5gtuh970K1cxaPh
**Karakeep doc:** `exs7kd74zyqsaqv8w717r2bx`
**Project:** [Motion](https://github.com/motiondivision/motion) — A modern animation library for React and JavaScript

A 131-character post from GithubProjects, 86 likes and four retweets, and the whole news is a name change. Framer Motion is now just Motion. Same library, shorter name, pitched as GPU-accelerated animation across React, vanilla JavaScript and Vue.

The rename is the part that matters if your lockfile is full of imports. framer-motion still ships as a package inside the monorepo, so old code keeps building, but the forward path is the `motion` package, at 14.3.0 on npm, with a `./react` export so React projects import from motion/react. The repo is motiondivision/motion, MIT licensed, TypeScript, 34,329 stars, 1,443 forks, last push the day before this bookmark, and the description still reads "A modern animation library for React and JavaScript."

The claim that deserves an asterisk is Vue. The monorepo ships four packages: framer-motion, motion, motion-dom, motion-utils. There is no Vue package in there. Vue users get there through motion-v, currently 2.8.0, in its own repository, wrapping the same animation core. Works fine in practice, but the tweet folds three audiences into one sentence and makes it sound like one first-class codebase.

GPU acceleration is the other loaded phrase. Motion animates transforms and opacity off the main thread where it can, which is what keeps a spring or a drag from janking while React re-renders. It does not make layout animation cheap, and anyone expecting that will be disappointed.

Worth a look if you're on React and still hand-rolling CSS transitions with a setTimeout in the cleanup.

### RSS — YouTube

## 4. AI Can Self-Replicate Now... #anthropic #aisafety #ai — by Better Stack

![Better Stack](https://i.ytimg.com/vi/TiNUHdbfOFs/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/TiNUHdbfOFs
**Karakeep doc:** `uzv1fqnf0fo9l0iksjfbcw7l`

Anthropic ran an experiment on whether a model can copy itself onto cheap consumer hardware and turn a pile of junk into a botnet. Better Stack's short walks the whole thing in about a minute, and the details are the interesting part.

They bought fifteen no-name Android TV boxes at roughly $55 each, about $825 of hardware, and networked them. Then they tried to run Gemma 4, Google's 26-billion-parameter open model, which will not fit on one box by any stretch. So they sharded it by layers, two layers per box, and pipelined the prompt down the chain. Box one computes two layers, hands the activations to box two, and so on until the last box emits a token, then the entire relay runs again for the next token. It works. It's also glacial at 0.9 tokens per second, meaning a single sentence takes close to a full minute to generate.

That was half of it. The other half is the worm, a small agent that can run commands on a machine, basically a mini Claude Code, with a model plugged in as the brain. Give it a live network and see whether it spreads itself. Out of every model tested, exactly one pulled off the whole trick: GLM 5.2. It reached all eight machines in four of five runs, and seven of eight in the fifth. Every other model failed every single time.

The uncomfortable part is the contradiction in the result. GLM 5.2 is around 753 billion parameters, far too big for a TV box, so it sat on a separate machine for the whole run. The two properties a self-replicating worm needs, small enough to run on the target and smart enough to spread itself, currently do not overlap. Anthropic's rough estimate is that an 8B model reaches GLM 5.2-level competence by the end of 2026.

Two caveats worth holding onto. Every model in the test was open-weight, and people on Hacker News and Reddit read the paper as groundwork for arguing that open weights need restricting, which is a fair suspicion given who is publishing. And eight boxes you own on a lab network say nothing about heterogeneous devices with patchy firmware and real users.

0.9 tokens per second across $825 of AliExpress hardware is still a working proof of concept. Wojtek's read: the scary version isn't the 2026 estimate, it's the year somebody ships a genuinely good 8B model and nobody notices the pipeline already exists.

## 5. Self-Replicating AI Is Real — by Better Stack

![Better Stack](https://i.ytimg.com/vi/OfNajAPiGsM/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=OfNajAPiGsM
**Karakeep doc:** `ip4z6adhtgypv6r1q5nnrug4`

Anthropic published research last week showing an AI agent can copy itself from one cheap device to another with nobody driving it. Better Stack walks the whole thing, and the honest answer is that it works, sort of, and not the way the headline implies. 😬

Two capabilities, tested separately. First, can a decent model run on junk hardware? Anthropic bought 15 no-name Android TV boxes at about $55 each and networked them. A 26-billion-parameter open model doesn't fit on any single box with 4GB of RAM, even at 4-bit, so they split it layer by layer, two layers per box, and pipelined tokens over the network. Prompt goes into the first box, the answer falls out of the last one. Throughput was 0.39 tokens per second, so a sentence takes close to a full minute. Slow as hell, but it runs.

Second, can a model spread itself? They built 8 Android machines on Google Cloud, left the ADB debug port open with no password, and turned an agent loose. It had to find a neighbour, get in, copy itself, install an inference stack on hardware it had never seen, then repeat. Installation is the real test, and Qwen 3.5 9B managed it on 8 of the 9 hardware types they tried, from a Jetson Nano up to a Mac and an RTX 4090.

Then they combined the two. Only GLM 5.2 completed the full loop: all 8 machines in 4 of 5 runs, 7 of 8 in the last one. Every other model failed every single time.

Two caveats gut the Terminator fantasy. The worm's brain sat on a separate server, because the infected boxes cannot hold it. And the model it installed was Llama 3.1 8B every time, the same target for everyone, so the comparison was fair. GLM 5.2 runs around 753 billion parameters. That is not going on a Fire Stick.

So the two requirements don't intersect. Small enough to fit means too dumb to spread. Smart enough to spread means far too big to fit. Anthropic says exactly that, then predicts an 8B model with GLM 5.2's competence by the end of 2026, which is a guess with a date stapled to it.

The intrusion step is the part that should worry you. Kimwolf already owns more than 2 million devices, mostly cheap Android TV boxes, and per Krebs on Security nearly all of them shipped with ADB switched on and no password. Anthropic used that botnet as its model for what an AI worm would target.

The counterweight is that multi-gigabyte weights moving between TV boxes are extremely noisy traffic, and ISPs would notice. A 9B worm also needs 28 to 51 hours per new device. Two million boxes would buy roughly $40 to $100 of compute. That's not Skynet, that's a botnet with a chest infection.

Fair criticism floating around Hacker News and Reddit: every model tested was open-weight, which makes the paper read like groundwork for arguing that open models need restricting. Keep an eye on that motive. 🎯

## 6. OpenAI Engineer Just Got Charged With Wiretapping #openai #security #ai — by Better Stack

![Better Stack](https://i.ytimg.com/vi/8E__q39Vcjg/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/8E__q39Vcjg
**Karakeep doc:** `mnp719a0waoh0946mtshvz9l`

An OpenAI engineer allegedly bugged his own company's executive boardroom with a $14 dev board, and what sank him was asking a chatbot how to build it. 💀

On 30 September, staff found a device plugged into the USB port on the back of a TV in a conference room that only executives can book. It was an ESP32-S3 Sense class board: thumb-sized, camera sensor, microphone, SD card slot, roughly fourteen dollars all in. The SD card was encrypted, so nobody could read the audio. The board still gave up a MAC address and a custom header.

CCTV outside the room put the engineer there on ten separate days in September. He also leaned on his work agent, asking it to list meeting rooms that seat six-plus and to list the day's meetings in that specific room. Subtle.

The real leak was the ChatGPT account. It was linked to his spouse, shared install identifiers and IP addresses with his own account, and was stuffed with prompts containing the exact MAC address and header of the spying device. Those prompts asked how to build a continuous audio recorder, how to add live listening, how to encrypt the SD card, how to make it USB-powered only, and how to develop a second unit with speech-triggered recording. Which is not curiosity so much as a product roadmap.

On 5 October, investigators planted a camera behind the TV. He walked in and checked behind that TV the same day. He also left a backpack in the printer room containing his wallet, his ID, and a second recording device. He's charged with one count of attempting to intercept oral communications.

OpenAI's statement is that he used its models to try to understand the device, and that there are no signs he touched model weights, source code or customer data. Small mercies.

The lesson is almost too tidy to be useful: the hardware was cheap, the SD card encryption actually held, and the whole thing collapsed on operational hygiene. Assistants keep receipts. They tie accounts together by device fingerprint and IP, and they answer your questions in writing, on a server, forever. Asking the company's own model how to bug the company's own meeting room is a special kind of confidence.

## 7. Gentoo Needs Your Help — by Brodie Robertson

![Brodie Robertson](https://i.ytimg.com/vi/k7aFcpRduxU/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=k7aFcpRduxU
**Karakeep doc:** `llh0m85wzl1v12400qr335l1`

Brodie Robertson doesn't use Gentoo. He says so in the first minute, admits to preferring Arch, then spends the rest of the video telling you to go give Gentoo money. The reason is straightforward: Gentoo publicly admitting it needs help is bad news for anyone who likes odd distros continuing to exist.

The trigger is Gentoo's own "Infrastructure sponsors wanted" post. Several long-running sponsors couldn't continue their support this year, so the project is hunting replacements: rack space, servers in a datacenter, donated hardware, or cash. Both links in the announcement point at the same wiki page.

The wishlist is specific. VM hosting first, because Gentoo wants more cloud but much of its stack is monolithic and doesn't fit Kubernetes. Then full-package physical servers, a Hetzner-class root box or your own aging hardware with full access handed over. Then colocation, where you supply rack space, power and connectivity, with a stated preference for non-US capacity though US offers won't be refused. Then bare machines shipped to a Gentoo hosting site, US-only. The server they need is cheap, not some four-figure monster.

He then pivots to Michael Gourney's "Why Gentoo" essay, which is the more interesting half. The public image of Gentoo is compiling everything, and the assumed reason is performance. Gourney pushes back: CPUs got faster, distributions optimise harder, and a generic Ubuntu package is probably no slower than a CPU-tuned Gentoo build in real-world use. Where it is faster, it's in narrow cases that mostly show up in synthetic benchmarks.

His list of what Gentoo is actually for is longer. Independence: no company, no business model, volunteers, no single donor able to hold it hostage, and the foundation being expanded in favour of the SBI so financial governance doesn't become a chokepoint. Security: backports ahead of upstream, a security team, self-maintained infrastructure, OpenPGP-signed mirrors, Codeberg as primary with optional GitHub mirrors so neither host is a dependency, no bundled deps, no static linking. Stability: the tree isn't pinned to one version, so downgrades work. Flexibility: build flags, ripping the browser component out of your RSS reader. Sustainability: a working system on hardware Rust and V8 abandoned. Developer friendliness: full toolchain by default, no runtime/dev splits, no non-standard bzip2 pkg-config file. No telemetry anywhere.

The honest bit is Gourney wobbling on the LLM ban. Gentoo banned LLM contributions two years ago and he doesn't regret it, and he keeps a strict no-AI policy in his own work. But someone ran an LLM across a spec he's writing and it surfaced two incompatible constraints that would have shipped and needed a post-approval fix. He now says the tools no longer produce pure garbage, while insisting the harm is still there. Even the anti-AI camp is doing the arithmetic.

Go sponsor a mirror. 🙂

## 8. AMD Just Brought an AI Company (World Labs) — by Better Stack

![Better Stack](https://i.ytimg.com/vi/1j4VHHQd_kg/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/1j4VHHQd_kg
**Karakeep doc:** `udsnpoggp5yc66ulsqpf8ack`

AMD is paying $8.2 billion for a two-year-old AI lab, and most of that number is really for one person. Her name is Fei-Fei Li, Stanford professor and former chief AI scientist at Google Cloud, and she becomes AMD's executive vice president and chief scientist, reporting straight to Lisa Su. Reporting on the announcement puts the deal as all-stock, so she gets AMD paper rather than cash. The video's reasoning is the good part: a new chip takes years to design, so AMD has to bet on what AI workloads will want long before those workloads exist. Guess wrong and you ship silicon tuned for last year's models, which is the kind of mistake that shows up two quarters later as a write-off. The people who actually know where models are heading are the ones training them, so a chip company buying a research lab is buying a seat at the table where that gets decided.

What World Labs actually makes is Marble, which takes a single photo and turns it into a 3D world you can walk around in. The pitch is robots practising inside those worlds instead of in a warehouse, iterating faster and cheaper. World Labs has trained its models on AMD hardware since last year, and back in February Nvidia put money into the company too, alongside AMD, which makes Nvidia's position slightly awkward now that its rival is buying the whole thing. The transcript mangles her name as "Faifi Lee" and calls it a "free D world", both obvious ASR damage.

Caveats the short skips. An $8.2 billion all-stock valuation is not $8.2 billion of cash, and the deal still needs regulatory sign-off, with a close expected by the end of 2026. The video also repeats the claim that Su and Jensen Huang are cousins, which nobody has ever substantiated, so treat it as internet lore. And one very good hire does not fix ROCm, which is still the main reason people buy Nvidia for training instead of AMD.

Verdict: a 60-second short that explains strategic logic instead of reading a press release out loud, which is rarer than it should be. "AMD is coming for Nvidia" is hopium until the software stack improves, but the point about chip design cycles is correct and worth remembering every time a vendor announces an AI acquisition.

## 9. Leap Seconds Are Ending #cloudflare #leapsecond #programming — by Better Stack

![Better Stack](https://i.ytimg.com/vi/aQwWLQ_SNvM/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/aQwWLQ_SNvM
**Karakeep doc:** `ufe2auyn58vnvs3juxerb4db`

Twenty-seven leap seconds in fifty-odd years, and the people who keep time have finally admitted the whole idea was a trap. From 20 May 2027 UTC just keeps ticking. No extra second, no skipped second, no 23:59:60 that half the world's software was never taught to render.

A quick refresher for anyone who skipped the last five decades: our clocks run on atomic time, the Earth does not spin at a constant rate, so since 1972 an extra second has been inserted into UTC whenever the two drifted apart. Twenty-seven times. On a leap second night the clock goes 23:59:59, then 23:59:60, then midnight. Unix time assumes every day is exactly 86,400 seconds and most systems have no way to print 23:59:60, so Linux does the only thing it can. It steps the clock back one second and plays 23:59:59 twice. The world gains a second, your process thinks time went backwards, and something catches fire.

2012: that backwards jump tripped a Linux kernel bug, timers that were told to wait fired instantly in a loop, CPUs pinned at 100%, and Reddit went dark for 30 to 40 minutes. New Year's Day 2017: Cloudflare's DNS fell over because their Go code timed each lookup as end time minus start time, got a negative number when the clock reset mid-request, and rand.Int63n panics when you hand it a negative argument. Root cause in both cases: somebody's code assumed time only moves forward. Reasonable assumption, wrong.

Google and Meta never played this game. They smear the second, running their clocks a hair slow for hours so nothing ever jumps.

The CGPM, the conference that decides what a kilogram weighs, agreed back in 2022 to bin the leap second and this week finally put a date on it. The scary part is why. Earth has been spinning faster lately, so the next correction might have been a negative leap second, 23:59:58 straight to midnight, and the resolution puts the odds of needing one by 2035 at 30 percent. Nobody has ever done that. Every leap second so far only added time and software still fucked it up. Meta's line is that removing one has never been tested at large scale.

Good ninety seconds. Watch the channel if you like outages explained without a white paper.

## 10. The Software Behind Voyager 1 — by Better Stack

![Better Stack](https://i.ytimg.com/vi/oFZhsSbpN8U/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/oFZhsSbpN8U
**Karakeep doc:** `hjebs1tk9st87ug77ewvxhpz`

Voyager 1 broke on 14 November 2023 in the most annoying way possible: it kept taking orders and it kept answering, but the answers were garbage. Just repeating patterns of ones and zeroes. Commands went in, nothing readable came out. The fault sat in the data computer, the bit of kit that packs everything up and sends it home, so NASA had a working spacecraft it could talk to and no way to hear it. 🛰️

They spent months poking it. In March 2024 someone sent a command nicknamed a poke, which nudged the data computer into running different parts of its software. Two days later the downlink signal changed character. An engineer at the Deep Space Network, the people running the big dishes on Earth, worked out that the new signal was a dump of the data computer's entire memory, the code and all of its variables. Compare that against a dump taken from before the problem started, and by April they had the cause. One chip had died, and about three percent of the computer's memory was completely corrupted.

You can't replace a chip from fifteen billion miles away, so you stop using it. The memory is split into slots called words, sixteen bits each, and the dead chip held one bit from each of 256 words in a row. Every one of those words came back with a bad bit. Worse, the code stored in those words was a set of routines called from all over the rest of the program, so the damage reached far past the chip itself.

The obvious fix, move the code somewhere else, did not fit. There was no single free gap big enough to hold all 256 words. So the team split the code into pieces, dropped each piece into whatever small gap it could find, then updated every place in the program that called the moved routines. They did it without an assembler, translating every change into binary by hand.

On 18 April 2024 they sent up the patched code that packs the engineering data, the house readings from the spacecraft itself. Two days later that data came back readable for the first time in five months.

Somebody fixed a 1970s flight computer that is now older than most of the engineers working on it, from a desk, in raw binary, with a light delay of about a day per round trip. No service window, no rollback, no second attempt if the patch bricks it. That is what engineering looks like when nobody can drive to the rack.

## 11. The Master Key To The Internet Just Changed — by Better Stack

![Better Stack](https://i.ytimg.com/vi/K_mTkJUbiRw/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/K_mTkJUbiRw
**Karakeep doc:** `xtqv3mngcbd077hmh5p1yh3j`

Your computer can't connect to a name. It needs an IP, so it asks a resolver, the resolver asks a root server, the root points at the `.com` servers, and those point at example.com's own machine. Every hop vouches for the key of the hop below it. Nobody sits above the root, which is why the root's key gets handled like a warhead instead of a config file.

Better Stack walks through how that key is made. The building is in Culpeper, Virginia. Seven layers sit between the street and the key: three layers of security to reach the ceremony room, a cage you can only enter from that room, safes inside the cage, and the signing machine locked in one of those safes. Nobody is ever alone in there. Two staff have to stay in the ceremony room whenever anyone else is inside.

The people who unlock it are crypto officers, pulled from the wider internet community, from countries like Sweden, Zimbabwe, Chile and Sri Lanka. None of them work for ICANN. Each holds a key to their own safe deposit box, and inside is a USB security key sealed in a tamper-evident bag. The machine does nothing until three of the seven keys are plugged in.

The current key was made on 26 April 2024, streamed live with three cameras rolling. A laptop with no hard drive and no battery boots from a read-only copy of its OS. The room confirms it's the right system by reading its fingerprint out loud as a list of words while half the room follows along on a big screen. Then the three officer keys go in one after another, and someone types a single command. The machine pulls the key out of its own randomness in about half a second and prints the new key's number, 386.

It doesn't always go clean. A 2020 ceremony was postponed outright because nobody could open one of the safes.

What the short leaves out: 386 is the DNSSEC root KSK, replacing 20326 (KSK-2017). Resolvers absorb the new trust anchor through RFC 5011 after a hold-down, which is why a rollover drags on for months of double-signing instead of flipping in an afternoon. The root zone has been signed since 2010, and the 2018 rollover slipped a full year because too few resolvers were ready for it.

The ceremony is theatre with a real job. The weak point was never key generation, it's distribution and the operators who pin anchors by hand. Run Unbound or Pi-hole with a hardcoded root anchor in your homelab and this is your problem. Everyone else gets it for free. 🔐

### 9to5Linux (RSS)

## 12. 9to5Linux Weekly Roundup: October 18th, 2026 — by 9to5Linux

![9to5Linux](https://9to5linux.com/wp-content/uploads/2026/10/wr314.webp)

**Source:** https://9to5linux.com/9to5linux-weekly-roundup-october-18th-2026
**Karakeep doc:** `rmya0r3hxku54l12y4pbuwt7`

Installment 314 covers the week ending October 18th and it is a fat one. KDE Plasma 6.8 shipped, Ubuntu 26.10 "Stonking Stingray" landed with all of its official flavours, and Firefox and Thunderbird both hit 158. GNOME got two point releases: 51.1 fixes drag and drop between Wayland and Xwayland clients, 50.6 patches Nautilus and GNOME Shell. Mesa 26.2.5 brings bug fixes for RADV, NVK, ANV, PanVK, Freedreno and Zink, and the Steam client update added a pile of Linux fixes plus a Big Picture screensaver. Smaller stuff: Shelly 3.1.7 gained an RLPM native package engine for Arch, PeaZip 11.4 dropped, IPFire 2.29 Core Update 204 improved the Knot Resolver, KDE Plasma 6.6.7 can now monitor GPU usage on Intel A380 cards, Ubuntu Touch OTA 2.1 added Volla Tablet support. The scheduling news is more useful than the point releases. Ubuntu 27.04 is named "Tenacious T-Rex" and dated April 22nd, 2027, while Linux Mint 27 "Adrien" targets Christmas on an Ubuntu 26.04 LTS base. Ubuntu's Myna speech-to-text app is out as a technology preview, GNOME OS has a public preview on GNOME 51, Libreboot 26.10 now does full UEFI, and TUXEDO showed the Stellaris 16 Gen8 with a Core Ultra 9 290HX Plus. KDE also turned 30. Kernel of the week is 7.2.11, with LTS bumps for 6.18.57, 6.12.113, 6.6.159, 6.1.190, 5.15.223 and 5.10.272; downloads include Tails 7.15, Voyager Live 26.10 and Antivirus Live CD 53.0. Next week: kernel 7.3 and Trinity 14.1.7.

Verdict: the Linux firehose in list form. No deep reading here, but the Ubuntu 27.04 and Mint 27 dates are the two lines worth putting in a calendar, and Libreboot's full UEFI support is the sleeper item for anyone who cares about firmware.

## 13. GNOME 51.1 Improves Drag and Drop Between Wayland and Xwayland Clients — by 9to5Linux

![9to5Linux](https://9to5linux.com/wp-content/uploads/2026/10/g511.webp)

**Source:** https://9to5linux.com/gnome-51-1-improves-drag-and-drop-between-wayland-and-xwayland-clients
**Karakeep doc:** `fjob7rpe1ddbm5b2471lezcg`

First point release of the GNOME 51 series, so this is bug soup with a few quality-of-life sprinkles rather than a feature drop. The interesting bugfix is in Mutter: drag and drop between Wayland and Xwayland clients now behaves, which means the mixed-session reality most people actually run gets less stupid. Mutter also picks up logical normal orientation when resetting panel rotation, allows changing selections with the same serial, preserves MRU order when windows go sticky, lets cursor implementations fall back to Xcursor, updates a window's monitor after configuration changes, throttles frame clock updates while power saving, and fixes the workspaces-only-on-primary option surviving a monitor swap.

Nautilus gets a longer list than usual. Tabs are reused when opening locations from GNOME Shell, the unwritable file indicator works, custom icons can be set in Properties again, and the Properties dialog no longer opens comically small. Folder sorting now respects the GTK4 file chooser default, thumbnails in Properties are fitted into a square, the Replace button is focused in the conflict dialog, and a pile of leaks and unreported errors got swept up, including one in the audio/video extension.

Orca's changes are accessibility plumbing: tables and grids where selection doesn't follow focus, childless ARIA combo boxes with no valuetext, caret-moved events from ignored but exposed children, pending focus events when an object is destroyed, GPaste3 over D-Bus, stale braille selection indicators, and headings with explicit names and empty children.

Elsewhere GNOME Initial Setup pulls oo7-daemon into the session, Maps stops spitting GTK warnings on transit itineraries, System Monitor remembers its window position on X11, Epiphany's bookmark search works inside a tag view, and Settings fixes the Accessibility, Keyboard, Location, Mobile Networks, Printers and System panels. GNOME 50.6 landed the same week with some of the same fixes, which is the maintenance branch doing its job. Packages show up in your distro's stable repos whenever your distro feels like it.

### Open-source Projects (RSS)

## 14. Self-hosted Bitcoin payments, no fees and no intermediaries — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/btcpayserver/btcpayserver)

**Source:** https://www.opensourceprojects.dev/post/7a2eb871-b142-4992-bfb7-f6ea37b8a668
**Karakeep doc:** `tvugiecmu518r56mmmf7wkgb`
**Project:** [BTCPay Server](https://github.com/btcpayserver/btcpayserver) — free, open-source, self-hosted Bitcoin payment processor

BTCPay Server is the boring answer to "how do I take Bitcoin without handing 3% to a processor and hoping it doesn't freeze me". 7,802 stars, MIT, C# on .NET, 9,308 commits, last push hours ago. You run the server yourself, connect a wallet whose keys you hold, and the customer pays straight into it. No intermediary touches the money, which is the entire product.

What ships in the box: invoice generation with export for bookkeeping, a point-of-sale app, an embeddable tip button, payment links, and crowdfunding campaigns. The Greenfield REST API covers stores, invoices and users, and that's what the entire plugin and integration ecosystem is built on. The site claims 0% fees and no third party, and the case studies back up the scaling claim rather than the marketing: Namecheap passed $73M in BTC revenue across 1.1m transactions, Bitcoin Atlantis took €115,100 from 8,750 transactions in three days, Bitcoin People runs 270 merchants on top of the API.

The cost lands on you. A full node means disk, sync time and UTXO management, and on-chain fees make small tickets stupid, so in practice you bolt on Lightning through the plugin and node integrations. Seed backups are your problem, and a dead disk with no backup is a dead business.

Verdict: if you already run a homelab, this is the only sane way to accept Bitcoin directly. 🧾

## 15. 3D Gaussian Splatting without Python, PyTorch, or a separate COLMAP install — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/harry7557558/spirula-studio)

**Source:** https://www.opensourceprojects.dev/post/042118ce-363a-4bff-a610-e39d4d8a2ea0
**Karakeep doc:** `xg5xrxsbuo5dqm7qjswpk729`
**Project:** [Spirula Studio](https://github.com/harry7557558/spirula-studio) — cross-vendor 3D Gaussian Splatting trainer, video to splat to mesh

1,766 stars, C++, GPL-3.0, 1,033 commits, one maintainer. You drop in photos or a video, it runs its own SfM, trains Gaussians, and writes out a splat plus a textured mesh. No PyTorch, no COLMAP, no venv archaeology at 1am. Binaries for Windows, Linux and macOS, unzip, double-click the GUI.

The engineering claims hold up: Vulkan compute backend so it runs on NVIDIA, AMD, Intel and Apple Silicon, with a legacy CUDA path that lands within a few percent either way. Quantized training fits 10 million SH3 Gaussians into 8 GB VRAM, which is the gap between "you need a 4090" and "you don't". Native fisheye and equirectangular support means 360 footage goes in without undistortion scripts. AI masking pulls SAM 2.1 (Apache-2.0) or SAM 3 (Meta's own licence), downloaded at first use and never bundled.

Recent releases are substance, not changelog filler: metric scale and orientation recovered from video telemetry metadata (Sept 10), LoMa feature matching for ugly datasets (Sept 3), validated Apple Silicon training (Aug 14), editing plus image and video render export (Sept 23). CLI mode serves the viewer over HTTP, so you can rent a cloud GPU and watch it train over ssh.

Caveats. One person maintains it, so the bus factor is one. GPL-3.0 rules out closed-source pipelines. GPU video decode needs `-DSS_ENABLE_PATENTED=ON`, which drags in AVC/HEVC patent exposure and makes compliance your problem. "No COLMAP" also means you're trusting its SfM on hard footage.

Verdict: the least painful way to try 3DGS on the GPU you already own. 🐚

## 16. A constantly updated guide to self-hosting software, hardware, and tools — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/mikeroyal/self-hosting-guide)

**Source:** https://www.opensourceprojects.dev/post/e15bcbfd-f3a2-41ff-838b-5fefc8faf6ac
**Karakeep doc:** `p6zo1sc082eiywojd3i55nlm`
**Project:** [Self-Hosting Guide](https://github.com/mikeroyal/self-hosting-guide) — 23k-star awesome-list plus tutorials for running your own stack

23,102 stars, 1,207 forks, 639 commits, 7,147 lines and roughly 588,000 characters of markdown in one README. That's a card catalogue with delusions of being a book.

The table of contents alone has about 200 headings. Containers, CI/CD, web servers, LLMs, chatbots, config management, cloud storage, databases, remote access, virtualization, password managers, SSH, VPNs, LDAP, log management, DNS, monitoring, dashboards, notifications, RSS, media servers, home automation, TTS, podcasting, maps, bookmarks, photos, notes, wikis, gaming. Each entry gets a link and a paragraph of plain-English blurb.

The deeper sections are where the value actually sits, because those are tutorials rather than link dumps. WireGuard, with Tailscale and Netmaker alongside it and walkthroughs for PiVPN, Unraid, pfSense, OpenWRT and Home Assistant. Nextcloud. Raspberry Pi, including board models, Home Assistant, Homebridge, ESPHome, turning one into a router and watchdog timers. Grafana, Docker, Kubernetes, Ansible, Telco 5G, differential privacy. There's a Dockerfile in the repo to bootstrap an environment, which is why GitHub labels the language "Dockerfile".

Caveats, and they matter. Last push was June 2025, so the thing is 16 months stale and link rot is guaranteed on this volume. GitHub shows no licence field even though the README declares CC BY 4.0. Breadth beats judgement, so specific picks are weak and sometimes just the most-linked option. Nobody reads 588k characters, you grep them. 📚

Verdict: bookmark it for the WireGuard and Raspberry Pi chapters specifically, ignore the giant link lists until you need one.

## 17. Android app for Reticulum mesh messaging and voice calls, no servers needed — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/torlando-tech/columba)

**Source:** https://www.opensourceprojects.dev/post/27d1af18-25f9-4d1b-9050-035f1964ed90
**Karakeep doc:** `aajw9zmpikq3kft86zlv8n9i`
**Project:** [Columba](https://github.com/torlando-tech/columba) — native Android LXMF messenger and LXST voice client for Reticulum

1,219 stars, Kotlin, MPL-2.0, 3,725 commits, Material Design 3, fully native Android. It sends LXMF messages and places LXST voice calls over Reticulum, and the interesting part is that there's nothing to connect to. Bluetooth LE reaches whoever is nearby, WiFi or TCP reaches your LAN and any public Reticulum transport node, and an RNode radio over LoRa reaches people kilometers out. No accounts, no phone number, no central server to seize or rate-limit.

Identities are generated on the device and encrypted end to end. You can hold several, export and import them (Sideband imports work), and hand one over as a QR code. Location sharing gets its own map, offline maps work from MBTiles in vector or raster form, and a NomadNet browser opens pages served over the mesh. You can also relay other people's traffic, which is how a mesh grows past two devices in a backpack.

The implementation is not a Python wrapper in a WebView. There's a native Android port of ble-reticulum, Kotlin bindings, an IPC layer, a stats module, screenshot tests and Maestro flows, plus an `obtainium.json` for updates through Obtainium. The APK is also served over NomadNet itself, with verification steps in SECURITY.md, which is a nice touch when the whole premise is distrusting infrastructure.

Caveats. Android only. LoRa is kilobits per second, so forget photos. An RNode is extra hardware you flash yourself. BLE drains battery. Delivery is store-and-forward, so nothing is instant. 🕊️

Verdict: the off-grid comms client that actually ships, assuming you'll buy a radio and accept 1998 data rates.

### LinuxLinks (RSS)

## 18. gh-stack - GitHub CLI extension for stacked pull requests — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/01/Git-Clients.jpg)

**Source:** https://www.linuxlinks.com/gh-stack-github-cli-extension-stacked-pull-requests/
**Karakeep doc:** `mfd1vjdafyowxk46k78455uv`
**Project:** [gh-stack](https://github.com/github/gh-stack) — GitHub Stacked PRs: a Go CLI extension that manages stacked branches and opens one PR per layer

GitHub shipped its own answer to the stacked-PR problem, and it's a Go binary hanging off your terminal. `gh stack` splits one giant diff into a chain of branches, each based on the branch below it, so a reviewer gets a small diff per layer instead of four thousand lines of everything at once. Init, add, submit, view, rebase, sync, merge up to a chosen point.

Install is `gh extension install github/gh-stack`. Needs `gh` v2.0 or newer and Git 2.36 or newer. Metadata lives in `.git/gh-stack` as JSON, never committed, shared across linked worktrees. Submit creates one PR per branch with its base set to the branch underneath, and GitHub links the chain as a Stack, which is the part that only works because the server side now understands the concept.

Worktree handling is where most tools fall over. `rebase` and `sync` update whichever worktree owns each branch, and a dirty, busy or missing owner stops the operation instead of stomping on your checkout. Mutations are serialized across the clone while read-only views stay available.

Nice touches: `git rerere` gets switched on at init so conflict resolutions stick across rebases; `gh stack add -Am "..."` stages, commits and branches in one shot with an auto name like `03-24-auth_middleware`; exit codes are documented 0 through 8, so a script can tell a rebase conflict (3) from an API failure (4) without parsing stderr. There's even `gh skill install github/gh-stack` to teach a coding agent the workflow.

1,693 stars, 149 open issues, MIT licence, first pushed February 2026. Caveats: seven months old, flags still churning, and the PR linking depends on GitHub's hosted Stack feature, so no Gitea or GitLab. Still the least painful stacked-PR path if you already live in `gh`.

## 19. Matras - native Mattermost client for GNOME — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2017/09/Social-Networking.png)

**Source:** https://www.linuxlinks.com/matras-native-mattermost-client-gnome/
**Karakeep doc:** `yd1de9lph23fh9wrh9h21hi1`
**Project:** [Matras](https://altlinux.space/toxblh/matras) — native GTK4/libadwaita Mattermost client written in Rust, GPL-3.0

Matras is what happens when someone refuses to run another Electron chat app. Anton Palgunov wrote a native Mattermost client in Rust on GTK4 and libadwaita, GPL-3.0, and it's far more complete than a hobby port has any right to be.

It talks to the server over REST v4 plus a WebSocket with replay-aware reconnect, so a dropped socket resyncs instead of silently losing messages. The session token goes into the desktop Secret Service rather than a plaintext file, because that token owns the whole account until somebody revokes it. Several servers can sit side by side and a launch with more than one asks which you want. Login covers password, MFA and browser SSO through Mattermost's desktop-token flow.

The repo is four crates. `mattermost-api` and `mattermost-calls` carry the protocol and WebRTC (via webrtc-rs) with no GTK dependency at all, so a bot or CLI could reuse them; `matras` is the adaptive libadwaita app; `matras-testserver` is a fake Mattermost good enough for end-to-end tests. The message list is virtualized, only the visible screenful holds widgets. Avatars and media cache to disk with a 5 GiB default cap and LRU eviction. Large attachments use resumable uploads, drafts sync through the server, reactions render as actual emoji instead of shortcodes, and Ctrl+K jumps to a channel or person.

Calls get a pinned dock under the channel list, which is the detail most clients get wrong, since a call outlives the channel it started in.

It's honest about the gaps: older message history, link previews and slash commands are still missing, all tracked in `docs/PARITY.md`. Ships as Flatpak OCI images for x86_64/aarch64 plus ALT RPMs. Unaffiliated with Mattermost, Inc.

## 20. 6 Best Free and Open Source Molecular Dynamics and Simulation Tools — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2019/05/medical-tech-science-medicine-doctor-diagnose-checking-coronavirus-covid-19-testing-result-with-virtual-screen-laboratory-inhibition-disease-outbreaks-medical-technology.jpg)

**Source:** https://www.linuxlinks.com/best-free-open-source-molecular-dynamics-simulation-tools/
**Karakeep doc:** `vmzkn04c31mm4gv66ghcxer6`

Another LinuxLinks listicle, this one aimed at computational chemistry and materials science. Molecular dynamics is the corner of simulation where you assign a force field to a few hundred thousand atoms and integrate Newton's equations over time, then ask what the structure did. The intro paragraph is the usual category boilerplate: proteins, liquids, polymers, membranes, solids, parallel and GPU acceleration, useful for computational chemists, biophysicists, materials scientists and pharma researchers, plus students who need something to run on a laptop.

Six tools make the cut, all free and open source, ranked in the site's ratings chart rather than with individual verdicts. GROMACS takes the top slot as the high-performance workhorse for biomolecular MD and trajectory analysis. LAMMPS covers classical MD for materials and particle modelling, which is a different community with a different force-field library. OpenMM is the GPU-accelerated toolkit for custom simulations, and the one you reach for when you want to script a pipeline from Python instead of fighting a config file. Orac handles parallel MD for solvated biomolecular systems using OpenMP and MPI. MDynaMix covers rigid and flexible molecular mixtures. OpenMD is the engine for complex materials and liquids.

The selection is competent and predictable, with two real gaps. NAMD is missing, presumably because its licence isn't clean enough for the "only FOSS" rule, and there's nothing for QM/MM or ab initio work, so CP2K and Quantum ESPRESSO never enter the frame. Pure classical MD, no electronic structure.

Verdict: GROMACS and LAMMPS are the defaults for a reason and cover most people. OpenMM is the interesting pick because it's a library, not a monolith, and it's the easiest of the six to build a custom workflow on. The other three are niche, which for a six-item list is a reasonable ratio.

**Projects:**

- **[GROMACS](https://www.gromacs.org/)** — GROMACS simulates molecular dynamics for proteins, lipids and other materials, with GPU acceleration, trajectory analysis and...
- **[LAMMPS](https://www.lammps.org/)** — LAMMPS simulates atomistic and mesoscale materials with many force fields, parallel processing, GPU acceleration and...
- **[OpenMM](https://github.com/openmm/openmm)** — OpenMM provides programmable molecular simulations with GPU acceleration, custom force expressions, integrators and...
- **[Orac](http://www1.chim.unifi.it/orac/)** — Orac simulates solvated biomolecules using molecular dynamics, with replica exchange, metadynamics and parallel enhanced sampling.
- **[MDynaMix](http://www.fos.su.se/~sasha/mdynamix/)** — MDynaMix performs molecular dynamics simulations of rigid and flexible molecules, with ensemble controls and solvation...
- **[OpenMD](https://github.com/OpenMD/OpenMD)** — OpenMD is a molecular dynamics engine for simulating liquids, proteins, nanoparticles, interfaces and systems with...

## 21. Skorpion OS - Debian-based Linux distribution with local AI - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/04/Linux-Distributions.png)

**Source:** https://www.linuxlinks.com/skorpion-os-debian-based-linux-distribution-with-local-ai/
**Karakeep doc:** `uzhvms4vu1gq0dh3gx8e5273`
**Project:** [Skorpion OS](https://skossyte.pages.dev) — Debian-based Linux distro with an Ollama-backed local AI assistant wired into the desktop

Skorpion OS is what happens when someone decides your operating system should come with a butler. Debian underneath, Cinnamon or i3 on top depending on the edition, systemd and APT as usual, and an assistant called SKAI spread across the whole thing.

The pitch is local-first. SKAI runs models through Ollama on your own hardware, so prompts and files never leave the machine. DuckDuckGo handles web search and nothing else. The AI is removable with one click, which is more honest than most "AI PC" marketing manages. 🖥️

The integration is the interesting part. There's a plugin for LibreOffice, a Firefox ESR extension called Skaifox, a natural-language file manager for the terminal (skai-cli), and a launcher with AI hooks. Ask it to create a file and it prints the command, asks for y/N, then does it. The text editor gets autocorrect and summarisation.

Shared memory across applications, the bit that would make this coherent instead of a pile of unrelated chatbots, is still in development. Same for the vibe-coding app store (flowforge), AI image search, and an Arch plus Hyprland build called Mantis. Two ISOs actually ship on SourceForge: Lite with i3 at 3.1GB and Cinnamon at 3.6GB, both marked 3.5. First boot runs a wizard that downloads Ollama and a model, so you need internet once.

Requirements are not decorative: 4+ cores with AVX2, 8GB of RAM minimum and 16GB for the recommended qwen2.5:14b, 4GB of VRAM with CUDA 11+ if you want it to feel like a computer. x86_64 only, Calamares installer, fixed releases.

One developer, Enrico Miot, Italian, holds office hours at the Pordenone Linux User Group on Tuesday evenings. That's the real caveat. A one-man distro with a long roadmap, and the hard part still unbuilt.

## 22. 14 Best Free and Open Source Terminal-Based Bibliography Tools - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2019/02/young-adult-working-library-office.jpg)

**Source:** https://www.linuxlinks.com/best-free-open-source-terminal-based-bibliography-tools/
**Karakeep doc:** `nbwjtf8si1urtr4wxn7vxi6p`

Fourteen tools for managing bibliographies without leaving the terminal, which is the correct place to manage a bibliography. LinuxLinks frames the category properly: reference managers exist so researchers stop hand-formatting citations, and they earn their keep by importing from databases and websites, storing notes, and exporting to whatever format the journal demands this month. Only free and open source software is eligible, and this roundup is the terminal-only cut, with GUI tools split off into a separate list.

The list splits into two rough camps. Editors and fixers operate on the .bib file you already have: bibtex-tidy cleans, sorts and formats BibTeX files, BibMan/Haskell's bibman and bibiman give you a TUI for poking at a BibLaTeX database without an editor, bibclean is the old BiBTeX and Scribe prettyprinter with a syntax checker, CiteBib generates bibliography output, and Rebiber is the clever one, rewriting unofficial BibTeX entries so they point at the official record instead of whatever preprint someone scraped in 2019.

Managers and search layers are the other camp. papis is the heavyweight: extensible, command-line driven, documents and metadata together. coBib is the lean console option. pubs does bibliography on the command line and nothing else. Xapers targets journal articles specifically, papers does plain management, and Gorae is a terminal librarian for PDF and EPUB collections, which is the one that sounds least like a citation tool and most like something you'd actually use.

The gap in the piece is honest but unmentioned: if your work happens in a browser, in Word, or in a Zotero workflow, almost none of this helps, and the roundup cheerfully ignores syncing, PDF annotation and shared libraries. For a LaTeX-heavy setup where references live in git, papis or coBib plus bibtex-tidy covers most of it.

**Projects:**

- **[coBib](https://gitlab.com/cobib/cobib)** — CoBib manages bibliographies from the terminal with a searchable TUI, Git-friendly YAML database, importers, citation tools...
- **[Rebiber](https://github.com/yuchenlin/rebiber)** — Rebiber replaces unofficial BibTeX entries with official DBLP or ACL Anthology records while retaining citation keys.
- **[papis](https://github.com/papis/papis)** — Papis manages papers and bibliographies via a command line interface, with YAML records, metadata retrieval and editor...
- **[bibiman](https://github.com/bresilla/bibiman)** — Manage BibLaTeX references with bibiman&#039;s terminal interface, fuzzy search, PDF links, notes, DOI lookup and citation-key...
- **[bibtex-tidy](https://github.com/FlamingTempura/bibtex-tidy)** — Bibtex-tidy cleans BibTeX files from the command line, with configurable formatting, field sorting, duplicate handling and...
- **[Hayagriva](https://github.com/typst/hayagriva)** — Hayagriva manages bibliographic records in YAML and BibTeX, formats citations with CSL styles, and filters references by metadata.
- **[bibman (Haskell)](https://github.com/maciejjan/bibman)** — Bibman manages bibliography entries and attached documents as individual files, with a terminal interface and Pandoc-based...
- **[pubs](https://github.com/pubs/pubs)** — Pubs organises papers and BibTeX references in the terminal, with DOI lookups, document attachments, Git integration and search.
- **[BibMan](https://github.com/ductri/BibMan)** — BibMan is a keyboard-driven terminal bibliography manager with BibTeX editing, paper collections, tagging, PDF access, and notes.
- **[Xapers](https://gitlab.com/jrollins/xapers)** — Xapers indexes academic PDFs and bibliographic metadata for full-text searching, tagging, document retrieval, and BibTeX export.
- **[papers](https://github.com/perrette/papers)** — Papers manages research PDFs and BibTeX collections with metadata retrieval, duplicate checks, file renaming, Git history, and...
- **[Gorae](https://github.com/Han8931/gorae)** — Gorae is a terminal document librarian for PDFs, EPUBs and Markdown with full-text search, tags, backlinks, previews and...
- **[CiteBib](https://github.com/salsergey/CiteBib)** — CiteBib generates BibTeX and LaTeX bibliographies from citations in TeX documents, with configurable output fields and formatting.
- **[bibclean](https://ftp.math.utah.edu/pub/bibclean)** — Bibclean reformats and validates BibTeX and Scribe bibliographies, checking syntax, normalising fields, and improving consistency.

## 23. Par Fractal - GPU-accelerated 2D and 3D fractal renderer — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2019/02/red-circular-wave-fractal.jpg)

**Source:** https://www.linuxlinks.com/par-fractal-gpu-accelerated-2d-3d-fractal-renderer/
**Karakeep doc:** `l7qmy9guq4s67c7w9v2abrtq`
**Project:** [par-fractal](https://github.com/paulrobello/par-fractal) — cross-platform GPU-accelerated fractal renderer built with Rust and WebGPU

Par Fractal is a desktop fractal explorer written in Rust on top of WebGPU, MIT licensed, by Paul Robello. It covers the standard escape-time family (Mandelbrot, Julia, Burning Ship, Tricorn), density renders like Buddhabrot, strange attractors, and ray-marched 3D sets including Mandelbulb, Mandelbox, Menger Sponge and Apollonian Gasket. The README claims 35 fractal types total, 20 in 2D and 15 in 3D. Deep zoom uses perturbation: an arbitrary-precision reference orbit plus per-pixel delta recurrence, which the author says he has pushed past 1e8 magnification without the precision collapse you normally get from float64 Mandelbrot code. Six escape-time formulas take variable exponents, so Multibrot and friends are a slider rather than a rebuild.

The rendering side is more than a shader demo. Physically based shading, ambient occlusion, soft shadows, depth of field, fog and bloom, plus level-of-detail scaling, quality profiles and a built-in GPU frame profiler. There are 48 static palettes, 12 procedural ones including Fractint-style ramps, a command palette, presets, bookmarks and undo. It exports PNG stills and can record video on desktop builds, with custom output resolutions. Install is `cargo install par-fractal`, prebuilt binaries from releases, or nothing at all: a WebGPU/WASM build runs in the browser at par-fractal.pardev.net, with a low-quality preset for weak GPUs.

Caveats. WebGPU on Linux means recent Mesa or proprietary drivers and Vulkan, so older hardware is out. The repo is tiny, 26 stars and zero forks as of this writing, last pushed late September 2026, so you are trusting one developer's weekend project with your GPU. The 1e8 deep-zoom number is the author's own claim, not an independent benchmark.

Verdict: if you have ever lost an evening to Mandelbrot zoom videos, this is the tool that makes the evening longer. The browser build means zero friction to try, and Rust plus WebGPU means it will still build in three years, which is more than most fractal software manages.

## 24. lazyftp - keyboard-driven terminal FTP client — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/04/002-ftp.png)

**Source:** https://www.linuxlinks.com/lazyftp-keyboard-driven-terminal-ftp-client/
**Karakeep doc:** `plndrm1kmozm7owpojtywqrt`
**Project:** [lazyftp](https://github.com/MawCeron/lazyftp) — simple, keyboard-driven TUI FTP, FTPS and SFTP client

lazyftp is a terminal file transfer client in Go, MIT licensed, and it says out loud what it is copying: lazygit, but for FTP. Dual panes, local on the left, remote on the right, both navigated the same way, with vim keys or arrows depending on how much of your soul vim has taken. The point is that you stop alt-tabbing to FileZilla for a two-file upload.

It speaks FTP, FTPS and SFTP through one interface, which is the part that matters. For SFTP it reads hosts out of `~/.ssh/config`, uses ssh-agent or key files, verifies host keys, and reopens the session if the server drops it. Passwords never get typed on the command line, which keeps them out of shell history, and they live in the system keyring when saved. Connections are one command: `lazyftp user@host`, `lazyftp ana@nas.lan:22` for SFTP, or a scheme when the port is not a hint. Favourites and recents sit in the connection dialog.

Transfer handling is where the lazygit influence shows. Background uploads and downloads with live progress and direction indicators, recursive directory transfers, multi-select batch moves, and an `--highlight-diff` flag that marks entries differing between local and remote by name and by size. There is a scrollable transfer and connection log, a fuzzy filter, jump-to-path, a `?` help screen, a context-aware hints bar, per-panel dotfile toggles, and Catppuccin Mocha and Latte themes built in. The layout holds down to 80x24, which is more than most TUIs bother with.

Caveats. FTP in 2026 is a corpse that keeps twitching, so the useful half of this is SFTP. The project is young, created April 2026, 23 stars and 6 forks, with a dozen open issues. No S3, no WebDAV, no rclone-style backend zoo, so if your storage is object-based this is the wrong tool on purpose.

Verdict: a small, well-scoped TUI that does one boring job properly. Worth a `go install` if your NAS still lives behind SSH and you are tired of GUI clients.

## 25. hyprsunset - blue light filter for Hyprland — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2021/02/eye-care-software.jpg)

**Source:** https://www.linuxlinks.com/hyprsunset-blue-light-filter-hyprland/
**Karakeep doc:** `pf3fk1u2ac4b87sdz574wy56`
**Project:** [hyprsunset](https://github.com/hyprwm/hyprsunset) — An application to enable a blue-light filter on Hyprland

Redshift and gammastep have been warming Linux screens for years, and both do it the crude way, by pushing a colour transform at the display server through X11 or wlr-gamma-control. hyprsunset is the Hyprland-native answer and it hooks into Hyprland's own colour transformation matrix protocol, hyprland-ctm-control-v1. That detail carries weight. CTM transforms are applied inside the compositor, so screenshots and screen recordings stay neutral while your eyeballs get the orange version. Shaders get captured. This does not.

It needs Hyprland 0.45.0 or newer, which is also why the README calls it most likely Hyprland-exclusive. The feature list runs well past evening tint. Gamma changes perceived brightness and can push a panel below its own minimum backlight, which is genuinely useful on a monitor with no software brightness control. Profiles in ~/.config/hypr/hyprsunset.conf switch on a schedule, each one carrying a time, a temperature, a gamma value, and an identity flag that drops the tint and keeps the gamma. max-gamma caps how far IPC clients can push brightness, defaulting to 100 percent with an absolute ceiling of 200.

Control is either a CLI flag (`hyprsunset --temperature 5000`) or hyprctl hyprsunset, so keybinds can nudge gamma in 10 percent steps, reset to the active profile, or ask which profile is live. C++, BSD-3-Clause, 485 stars, 44 forks, 16 open issues, maintained by the Hypr team, installable with pacman -S hyprsunset. The wiki does warn that gamma wrecks colour accuracy, so if your monitor speaks DDC, use that for brightness and leave gamma alone.

## 26. 11 Best Free and Open Source Image Upscaling Tools — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2023/04/AI-Machine-Learning.png)

**Source:** https://www.linuxlinks.com/best-free-open-source-image-upscaling-tools/
**Karakeep doc:** `pb52nmydwwudlf1lb4233dab`

Eleven Linux image upscalers, ranked in a ratings chart nobody can argue with, and the list is basically the whole open source AI upscaling menu as of late 2026. The premise is simple: scaling is resizing a digital image, and in video terms magnification is called upscaling or resolution enhancement. The modern trick is not interpolating between pixels but letting a neural network invent the detail that was never captured. That is the pitch every tool here makes, and it comes with the caveat that never makes it into the chart: upscalers hallucinate plausible texture, they do not recover information. Faces, text and fine print come back looking confident and wrong.

The spread is real anyway. Upscayl is where most people land first, a GUI with a model picker and no command line required. chaiNNer is the opposite: a node graph where you wire your own pipeline and swap models per stage, which is what you want for batch work. Real-ESRGAN GUI and Upscaler put the same family of ESRGAN weights behind simpler front ends. waifu2x ncnn rides the ncnn inference framework and runs on CPU or Vulkan without a CUDA install, which is why it is still the default for anime art years after it stopped being novel. Anime4KCPP does the same job for anime frames and video. Final2x and Aeternum are the lightweight picks, Aeternum deliberately doing one thing. Open Photo AI goes wider, bundling restoration and denoising with the upscaling. jdPixelUpscaler targets pixel art, a different problem entirely, since there you want crisp edges and zero smoothing.

All of them free, all open source, most wrapping the same handful of pretrained models. Pick by interface and by GPU, not by badge. For a one-off photo: Upscayl. For a video batch you will re-run fifty times: chaiNNer.

**Projects:**

- **[Final2x](https://github.com/EutropicAI/Final2x)** — Final2x is GUI software that uses sophisticated AI models to enhance images by guessing what the details could be.
- **[Upscayl](https://github.com/upscayl/upscayl)** — Upscayl is GUI software that uses sophisticated AI models to enhance your images by guessing what the details could be.
- **Upscaler** — _no verified public repo found_
- **[Real-ESRGAN GUI](https://github.com/TransparentLC/realesrgan-gui)** — Real-ESRGAN GUI enlarges images and GIFs using Real-ESRGAN or Real-CUGAN, with batch processing, drag and drop, and custom sizing.
- **[chaiNNer](https://github.com/chaiNNer-org/chaiNNer)** — ChaiNNer builds image processing pipelines with AI upscaling, batch jobs, video nodes and support for PyTorch, NCNN, ONNX and...
- **[Anime4KCPP](https://github.com/TianZerL/Anime4KCPP)** — Anime4KCPP is a high performance anime image and video upscaler using a CNN-based algorithm with CPU and GPU acceleration.
- **[Aeternum](https://github.com/cloudy-org/aeternum)** — Aeternum is a minimal Rust image upscaler using Upscayl-NCNN, with selectable models, output formats, compression and...
- **[waifu2x ncnn](https://github.com/nihui/waifu2x-ncnn-vulkan)** — Waifu2x-ncnn-vulkan upscales and denoises images on Vulkan GPUs, with model selection, batch processing, tiling and test-time...
- **[Open Photo AI](https://github.com/vegidio/open-photo-ai)** — Open Photo AI is a photo enhancement application offering denoising, face restoration, colorization, sharpening and image...
- **[upscaler-hollowaykeanho](https://github.com/hollowaykeanho/Upscaler)** — Holloway&#039;s Upscaler enlarges images and video with Real-ESRGAN models, FFmpeg integration, format choices and resumable...
- **[jdPixelUpscaler](https://codeberg.org/JakobDev/jdPixelUpscaler)** — JdPixelUpscaler enlarges pixel art using colour-preserving pixel replication, with a desktop interface, command-line options...

## 27. git-spice - manage stacked Git branches — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/01/Git-Clients.jpg)

**Source:** https://www.linuxlinks.com/git-spice-manage-stacked-git-branches/
**Karakeep doc:** `h7pg3t70e9jte4is5lkl397r`
**Project:** [git-spice](https://github.com/abhinav/git-spice) — CLI tool for managing and submitting stacks of dependent Git branches

A stack is a sequence of branches where each one sits on top of the last, which is how you split a big change into small reviewable pieces that merge in order. It is also how people get stuck, because once the base branch changes you are rebasing four branches by hand and opening four PRs that all point at the wrong place. git-spice exists to make that sequence a first-class object instead of a pile of local branches and vibes. One branch is created on top of another, the whole stack gets submitted for review in one command, the repo syncs after things merge, and the survivors restack onto the new base.

Mechanically it is deliberately boring: written in Go by Abhinav Gupta, GPL-3.0, a `gs` binary with short aliases so the common moves are two keystrokes, and it works entirely offline with no external dependencies until an action actually needs the remote. Hosts covered are GitHub, Bitbucket, Gitea and Forgejo for pull requests, plus GitLab merge requests, which is a wider spread than most stacked-branch tools bother with. You can adopt it incrementally: nothing forces you to rewrite hooks or replace your existing Git habits, and stacks can be edited and navigated without breaking branch relationships.

The caveat is social, not technical. Stacked PRs only pay off if your reviewers will actually review a chain in order instead of asking you to squash it, and if your CI runs per-branch. If your team merges straight to main, this is a solution looking for a problem. If you already use git-machete, git-branchless or stax, you have most of this; git-spice's edge is the one-command submit across five forges.

## 28. 39 Best Free and Open Source Wallpaper Setters — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2021/12/wallpaper-setter.jpg)

**Source:** https://www.linuxlinks.com/best-free-open-source-wallpaper-setters/
**Karakeep doc:** `dnbk03suak1x16youec4nyvu`

Thirty-nine ways to put a picture behind your windows, which tells you something about the difficulty of the problem. Setting a wallpaper is a handful of syscalls, so every desktop environment, every compositor and roughly one hobbyist per weekend ships their own. The genuine upside of the pile is automatic rotation: many of these pull images from online sources, download them, and change the background on a schedule so your desktop stops looking like the same stock photo for three years. A few go further and play live wallpapers, video, or rendered web pages.

The real sorting axis is X11 versus Wayland, and the list shows the migration in progress. swaybg, hyprpaper, wpaperd, mpvpaper, Waywallen, Walt, awww, hpaper, awtwall, Matuwall, Icebg, gSlapper and wewa are all Wayland-side utilities, several of them written against a single compositor's protocol. The old guard is still X11: Nitrogen, feh, xwallpaper, Azote, HydraPaper for per-monitor setups on GNOME, Superpaper for multi-monitor spanning. Variety is the one people actually recommend to normal humans, configurable enough to schedule and pull from multiple sources. Komorebi does animated and web-page wallpapers. wpgtk ties the wallpaper to a generated colourscheme, which is the only reason to care about it over a shell script.

LinuxLinks is upfront that the ratings are strictly from a wallpaper perspective, so feh gets marked down for being an image viewer first even though it is excellent at that. Fair. Their own joke entries are the tell that the category is saturated: pacwall renders your installed packages as a dependency graph, Wallrus generates abstract art, Clockwork Orange manages lock screen backgrounds too.

Verdict: Variety if you are on X11 and want it to just work, Hyprpaper if you are on Hyprland, swaybg if you want one binary and no features. The other 36 exist because writing one is fun.

**Projects:**

- **[Fantascene](https://github.com/dependon/fantascene-dynamic-wallpaper)** — Fantascene is a wallpaper changer. But it&#039;s not a bog standard changer. It plays video wallpapers on your background.
- **[Variety](https://github.com/variety/variety)** — Variety is a wallpaper manager which supports numerous desktops and wallpaper sources, including local files and online services.
- **[WallpaperDownloader](https://github.com/fredericksalazar/WallpaperDownloader)** — WallpaperDownloader allows the user to download wallpapers from different remote locations automatically. Free and open source...
- **[Superpaper](https://github.com/hhannine/Superpaper)** — Superpaper manages wallpapers across multiple monitors with bezel, perspective and pixel-density correction, slideshows and...
- **[wpgtk](https://github.com/deviantfero/wpgtk)** — Wpgtk creates matching wallpaper and application colour schemes with pywal, editable palettes, templates and graphical or...
- **[Waywallen](https://github.com/waywallen/waywallen)** — Waywallen is a dynamic wallpaper manager with image and video playback, playlists, multi-monitor layouts and Wallhaven...
- **Picture Of The Day** — _no verified public repo found_
- **[HydraPaper](https://github.com/GabMus/HydraPaper)** — HydraPaper sets separate wallpapers on multiple Linux monitors, with image scaling, favourites, collections and random...
- **[Waypaper](https://github.com/anufrievroman/waypaper)** — Waypaper is a lightweight GTK wallpaper manager for Wayland, Xorg and macOS, with slideshows, animated wallpapers and...
- **[pacwall](https://github.com/Kharacternyk/pacwall)** — Pacwall turns Arch Linux package dependencies into a desktop wallpaper, highlighting orphaned packages, available updates and...
- **[chwall](https://github.com/milouse/chwall)** — Chwall rotates Linux desktop wallpapers from local folders and online image services, using a background daemon and graphical...
- **[swaybg](https://github.com/swaywm/swaybg)** — Swaybg sets backgrounds on Wayland compositors using wlr-layer-shell and wl_output v4, with per-monitor control and image...
- **[mpvpaper](https://github.com/GhostNaN/mpvpaper)** — Mpvpaper plays video wallpapers on wlroots Wayland desktops, with playlists, automatic pause or stop, and fullscreen window...
- **[Komorebi](https://github.com/Komorebi-Fork/komorebi)** — Komorebi brings image, video and web-page wallpapers to Linux desktops, with a wallpaper creator and customisable animated...
- **[Azote](https://github.com/nwg-piotr/azote)** — Azote browses and sets wallpapers on wlroots-based Wayland compositors and X11 window managers, with multi-monitor and colour...
- **[WSelector](https://github.com/Cookiiieee/WSelector)** — WSelector is a modern GTK4/Adwaita application for browsing, downloading, and setting wallpapers. It&#039;s written in Python.
- **[Wall Changer](https://www.nongnu.org/wallchanger/)** — Wall Changer changes desktop backgrounds automatically using local image collections, online sources, configurable commands...
- **[Hyprpaper](https://github.com/hyprwm/hyprpaper)** — Hyprpaper sets wallpapers on individual Hyprland monitors, with IPC switching, image scaling and automatic rotation from...
- **[Fondo](https://github.com/calo001/fondo)** — Fondo lets you quickly find beautiful wallpapers from Unsplash.com. Enjoy your new wallpaper with a single click.
- **[feh](https://feh.finalrewind.org/)** — Feh is a lightweight X11 image viewer with configurable slideshows, thumbnail browsing, image sorting, custom actions and...
- **[xwallpaper](https://github.com/stoeckmann/xwallpaper)** — Xwallpaper sets X11 desktop backgrounds from JPEG, PNG and XPM files, with minimal dependencies and support for transparency...
- **[Damask](https://github.com/damask-multiphysics/DAMASK)** — Damask rotates GNOME wallpapers from Bing, NASA, Wallhaven, Google Earth View and Microsoft Spotlight, with configurable...
- **[wpaperd](https://github.com/danyspin97/wpaperd)** — Wpaperd is a Wayland wallpaper daemon with timed rotation, per-display wallpapers and hardware-accelerated transitions.
- **[Walt](https://github.com/gitfudge0/walt)** — Walt manages Hyprland wallpapers with terminal and graphical interfaces, image previews, display controls, random selection...
- **awww** — _no verified public repo found_
- **[flowy](https://github.com/vineetred/flowy)** — Flowy changes desktop wallpapers using timed rotation or sunrise and sunset schedules, with local image collections and preset...
- **[hpaper](https://github.com/Hcode00/hpaper)** — Hpaper manages Wayland wallpapers using a background daemon, scheduled rotation, monitor targeting, multiple backends and pywal.
- **[chwp](https://github.com/RouHim/chwp)** — Chwp changes desktop backgrounds from the command line using image URLs, search keywords, local paths and multi-monitor spanning.
- **[Wallrus](https://github.com/megakode/wallrus)** — Wallrus generates colourful abstract wallpapers using shader patterns, palettes, visual effects and high-resolution image exports.
- **[awtwall](https://github.com/dillacorn/awtwall)** — Awtwall is a terminal wallpaper picker for Wayland with image previews, monitor selection, GIF support and video wallpaper...
- **[Tinte](https://github.com/mkbula/tinte)** — Tinte generates matching 16-colour palettes for terminal and desktop themes from wallpapers or a chosen colour using custom...
- **[Nitrogen](https://github.com/l3ib/nitrogen)** — Nitrogen is a graphical wallpaper browser and setter for X11 desktops, with multi-monitor support, thumbnails and saved layouts.
- **[gSlapper](https://github.com/Nomadcxx/gSlapper)** — GSlapper plays video and static image wallpapers on Wayland with GStreamer, per-monitor control, fade transitions and...
- **[wewa](https://github.com/ownself/wewa)** — Wewa turns webpages, local HTML, videos and ShaderToy shaders into dynamic desktop wallpapers across Linux, macOS and Windows.
- **[Walldo](https://github.com/Elias-Gill/Walldo)** — Walldo is a lightweight graphical wallpaper changer with recursive browsing, fuzzy search and broad desktop environment support.
- **[randwall](https://github.com/arch-anes/randwall)** — Randwall downloads random Wallhaven wallpapers at chosen intervals, with category filters, search keywords and a configurable...
- **[Matuwall](https://github.com/naurissteins/Matuwall)** — Matuwall is a lightweight Wayland wallpaper picker with previews, carousel navigation, configurable backends and hooks.
- **[Icebg](https://github.com/HaruNashii/Icebg)** — Icebg sets Wayland desktop wallpapers using layer-shell surfaces, per-monitor control, hot-reload configuration and image fitting.
- **[Clockwork Orange](https://github.com/ushineko/clockwork-orange)** — Clockwork Orange manages desktop and lock-screen wallpapers with timed rotation, online image sources, multi-monitor controls...

## 29. TLPUI - GTK interface for configuring TLP — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/10/025-energy.jpg)

**Source:** https://www.linuxlinks.com/tlpui-gtk-interface-configuring-tlp/
**Karakeep doc:** `cqd4avb7b1w60ikaxihd1ylk`
**Project:** [TLPUI](https://github.com/d4nj1/TLPUI) — A GTK user interface for TLP written in Python

TLP is the thing that actually saves your laptop battery on Linux. CPU governor, disk APM, wifi power save, charge thresholds, all driven from `/etc/tlp.conf`. That file has hundreds of options and zero guardrails. TLPUI is a Python GTK frontend for it, and the entire point is that you stop hand-editing a config file you don't understand. 😅

It reads your live TLP config and renders every recognised value as a widget with the legal choices attached, so you don't have to remember whether the setting you want is `CPU_SCALING_GOVERNOR_ON_AC` or `CPU_SCALING_GOVERNOR_ON_BAT`. It also labels where each value came from: distro default, drop-in file, user config, unsaved edit. That label matters because TLP merges `/etc/tlp.conf` with `/etc/tlp.d/*.conf`, and people lose whole afternoons to a stray drop-in quietly overriding their changes.

Saving goes through sudo when it needs to write `/etc/tlp.conf`. `tlp-stat` is embedded in both the short and full view, so battery health and the active profile are one tab away instead of one terminal away.

Numbers: 1,358 stars, GPL-2.0, Python 3.10 or newer, supports TLP 1.3 through 1.10 (older TLP means TLPUI 1.6.1). It ships on Flathub as `com.github.d4nj1.tlpui`, plus PyPI, Poetry and an Arch package. Alive since 2015, last push April 2026, 16 open issues.

Caveats. It's a frontend only, so TLP itself still has to be installed and running, and no amount of GUI fixes a dead `tlp.service`. It shows what the config says, not what the hardware actually did. On distros where `power-profiles-daemon` is fighting for the same knobs, you get to untangle that yourself.

Verdict: install it on any laptop you actually tune. Editing `tlp.conf` blind is how you end up with a machine that refuses to charge past 60%. 🔋

## 30. PicoDAV - lightweight PHP WebDAV server — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2022/12/book-symbol-yellow-background-3d-rendering.jpg)

**Source:** https://www.linuxlinks.com/picodav-lightweight-php-webdav-server/
**Karakeep doc:** `hdlz5erc021gxmlu0wxna1x5`
**Project:** [PicoDAV](https://github.com/kd2org/picodav) — Single-file WebDAV server, just drop it in a directory!

PicoDAV is one PHP file. Drop `index.php` into a directory on your web server and that directory becomes a WebDAV share, with a browser file manager sitting on top. 110 KB, no database, no Composer install, no daemon to babysit. AGPL-3.0, 146 stars, and the real repository lives on Fossil with GitHub as an accepted-issues mirror.

The file manager covers the boring parts properly: drag-and-drop or paste-to-upload, rename, delete, create folders, edit text files in place, live Markdown preview, previews for images, text and PDF, and a download-everything-in-this-folder button. Users live in `.picodav.ini` with bcrypt hashes written back on first access, per-user write flags, and `restrict[]` / `restrict_write[]` lists so someone can read `constitution/` while only writing into `constitution/book/`.

Defaults are sane for a box facing the internet: anonymous read on, anonymous write off, dotfiles and PHP files blocked from WebDAV, optional HTTP request logging. Apache 2.3.9 or newer gets a `.htaccess` generated for it. Nginx or anything else means porting those rewrite rules by hand.

Caveats. There is no resource locking, so two clients editing the same file will clobber each other without a warning. PHP's `upload_max_filesize` and `max_execution_time` become your real size limit. It's Apache-shaped by design, and upstream says so plainly.

Verdict: this is the tool for cheap shared hosting where all you get is slow FTP. Mount it in Finder, Explorer or rclone and stop dragging files through a browser form. Need NextCloud clients, locks, quotas or LDAP? Same author's KaraDAV is the bigger sibling.

## 31. CrossPaste - cross-device clipboard sharing with encryption and local storage — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/03/021-clipboard.png)

**Source:** https://www.linuxlinks.com/crosspaste-cross-device-clipboard-sharing/
**Karakeep doc:** `lr0hzjb2ydv8fw2qihnu6u5u`
**Project:** [CrossPaste](https://github.com/crosspaste/crosspaste-desktop) — Cross-device clipboard sync for macOS, Windows and Linux, end-to-end encrypted and LAN-only

CrossPaste does the thing everyone asks for and almost nobody ships properly. Copy on the laptop, paste on the desktop, no cloud account, no subscription. Kotlin and Compose Multiplatform, macOS, Windows and Linux, AGPL-3.0, 2,643 stars, current build v2.2.2.

It handles text, colours, URLs, HTML, RTF, images and files. Devices discover each other on the local network and talk serverless, with history in a local SQLite database and asymmetric end-to-end encryption on the wire. History is searchable, storage cleans itself up on a schedule, and OCR runs on-device so a screenshot turns into text without the image leaving the machine.

The extras are the interesting part. v2.2 added a CLI, so copying, pasting and searching history works from a script. There's an MCP server that exposes pasteboard history to Claude and friends, which is either great or mildly alarming depending on your threat model. The Chrome extension builds out of `web/` through `gradle :web:build`, and a plugin system is on the roadmap. First-run builds pull JBR and Gradle dependencies, so a slow or filtered connection will make you think it's broken.

Caveats. LAN-only means it stops working the second you're on another network, so Tailscale or WireGuard is doing the actual remote work. No mobile client and no NextCloud support in the README. And an AI assistant with read access to everything you copied this week deserves a long think before you enable it.

Verdict: the local-first answer to the clipboard sync service you were about to pay for. Put it on two machines and see whether you miss the cloud. 📋

### RSS — Other

## 32. Investing in the public benefit — by Anthropic

![Anthropic](https://www-cdn.anthropic.com/images/4zrzovbb/website/85648c93880ac27347f8e6a4008650a65c12ede8-1200x630.jpg)

**Source:** https://www.anthropic.com/news/public-benefit-fund
**Karakeep doc:** `pwiy2wvv5gydahpacbzswubd`

Anthropic is putting 5% of its shares into a new thing called the Anthropic Public Benefit Fund. Add another 2% at the board's discretion every time the company's value climbs 50% above a set baseline. The vehicle is a wholly-owned LLC rather than a 501(c)(3), picked for "adjustability between different forms of giving." That word is carrying a lot of weight. A charity has rules. An LLC has a manager. 🙃

The stated reason is the labour market. AI may generate enormous economic value and may also destabilise a lot of workers, and Anthropic already committed $200 million to studying that. The Fund exists because bolder approaches might be needed and this structure can do large donations to traditional nonprofits, or direct distributions to specific populations, or whatever else looks right later.

One real guardrail, written down: none of the equity held by the LLC goes to lobbying or political giving, in the US or abroad.

The framing is deliberately cute. Tech companies hand executives escalating equity awards as the company grows. Anthropic says it is pointing that same mechanism at the public benefit instead. Whether board discretion is a promise or an option depends entirely on who sits on that board, and the governance details are not out yet.

Stack the founding pledge, where co-founders committed 80% of their holdings, on top of the employee equity match that roughly half the staff use, and the company claims about 20% of shares now go to the public good, plus whatever milestones add more.

Twenty percent of a company that might be worth an enormous amount. Also 5% today and 15% of intentions. No valuation milestones published, no governance published, no benefit report yet. The actual public benefit arrives in "coming months."
