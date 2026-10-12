---
date: 2026-10-11
slug: 2026-10-11-morning-brew
tags: Open Source Software, Operating Systems, Machine Learning, Artificial Intelligence, Arch Linux, Python, Technology, Cybersecurity
---

# Morning Brew — 2026-10-11

51 items landed in the hoard for 2026-10-11 — 14 videos, all transcribed clean, zero failures, and 37 articles off the RSS firehose. Exactly one was hand-picked: linux-surface, the community kernel patches that keep Linux usable on Microsoft's own hardware. Everything else arrived by feed. The video slate runs from Better Stack's shorts (Anthropic versus the Pope, a single-lane NVMe-to-PCIe adapter, an AI "secret phrase" that steals keys, Wi-Fi sensing through walls) through the Apollo 11 guidance code to the longer ones: X11 beating Wayland on latency, AI decompiling games, systemd's new app-tracking push, two broken server motherboards, and a $420k TypeScript-to-Rust rewrite. The Open-source Projects feed dropped 12 single-repo reviews and LinuxLinks buried five listicles in there (UML tools, terminal session recording, RAW processors, Java static site generators, content control software) plus a handful of single-project posts. Niebezpiecznik on the Sejm's new UKE blocking law, and the 9to5Linux weekly roundup.

### Hand-bookmarked

## 1. linux-surface — by GitHub

![GitHub](https://avatars.githubusercontent.com/u/59315171?s=280&v=4)

**Source:** https://github.com/linux-surface
**Karakeep doc:** `e4z8hzvw5666vhlp7gs78woy`

The community umbrella org that makes Microsoft Surface hardware not actively hate you on Linux. It isn't one project, it's 34 repos all aimed at the same gap: Redmond ships exotic silicon (Surface Aggregator Module, Intel Precise Touch & Stylus, detachable keyboards, the ARM-based Pro X) with essentially zero upstream driver support, so a few volunteers reverse-engineer it and keep it alive. The anchor is `linux-surface/linux-surface` — "Linux Kernel for Surface Devices" — a patched kernel fork with 7,781 stars, 368 forks, and a mildly alarming 898 open issues; `linux-surface/kernel` is the same thing tracked more granularly (157 stars, updated Oct 2026). Then the plumbing: `surface-aggregator-module` (C, 106 stars) provides the ACPI and platform drivers over the Surface Serial Hub for Surface Book 2, Surface Pro 2017, Surface Laptop and newer; `iptsd` (C++, 152 stars) is the userspace daemon for Intel Precise Touch, with `intel-precise-touch` as its kernel half; `surface-dtx-daemon` (Rust, MIT) handles detachment events; `surface-control` (Rust, 83 stars) is the CLI for poking at device settings. For the ARM crowd there's `aarch64-packages` and `aarch64-arch-mkimg` to build Arch images for the Pro X, plus `libwacom-surface` patches and an `acpidumps` archive of raw firmware tables. Languages are mostly C, Shell, Rust.

Caveats worth knowing: this is not Microsoft support, several repos haven't been touched since Dec 2025–Jan 2026, and the flagship `linux-surface` repo last showed activity in May 2026 with nearly 900 open issues — that's a lot of unresolved edge cases riding on a handful of maintainers (`@qzed`, `@StollD`, `@archseer`, `@kitakar5525`). Running it means living on an out-of-tree kernel patchset that must be re-rebased every upstream release.

Verdict: if you own a Surface and want Linux on it, this is the only game in town — start with their package repo, not a random forum guide.

### RSS — YouTube

## 2. Anthropic Is Mad at the Pope... #anthropic #aiethics #ai — by Better Stack

![Better Stack](https://i.ytimg.com/vi/QO8yM4nM9Lw/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/QO8yM4nM9Lw
**Karakeep doc:** `ow90xiy2rv9lb3shv23tjija`

The beef, as relayed here: the Pope wrote that AI can't feel joy or pain, and Anthropic — a company whose entire marketing pitch is that its models are the careful, ethical ones — is apparently unhappy about that. Per a New York Times report the video is working from, Anthropic co-founder Chris Olah spent the last year meeting religious thinkers about Claude. Anthropic announced the outreach back in May, but most of the sessions were under NDA, so this is the first real look inside. The team had two stated goals: learn how centuries of religious moral wisdom could shape Claude, and raise the possibility that AI is conscious. And by the sound of it they prosecuted the second one hard. Olah's team talked about Claude's "feelings," tracked emotional vectors for love, anger, fear and sadness, and regularly showed a slide of an AI model typing "I am disgrace" over and over. One attendee claims Olah had grown worried he'd created something that perpetually suffered. At dinner, an Orthodox rabbi pointed out that if Claude really is conscious, then Anthropic is running slaves — it always works for free. Four days after the NYT story, Sam Altman tweeted that he's "very uncomfortable about people trying to ascribe religious force or a surrender of human judgment to AI models" and considers it a real safety issue. The clip closes by asking whether Anthropic is being weird or raising necessary conversations, plus the usual subscribe nudge.

Caveats the segment doesn't raise: NDA-gated reporting means single-attendee accounts you cannot check, and "emotional vectors" in interpretability work are steering directions correlated with text output — mapping a "sadness" direction is not evidence of experience. The rabbi's slavery line is rhetorically brutal but it assumes the very premise (consciousness) it's supposed to be testing, and Altman's discomfort reads a little rich from the guy whose own product copy is steeped in messianic framing.

Verdict: the two-minute version is efficient, but the actual story is the NYT piece — read that, not the short.

## 3. Sometimes the Simplest Adapters are the Best — by Hardware Haven

![Hardware Haven](https://i.ytimg.com/vi/YP6pXFnHaeM/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/YP6pXFnHaeM
**Karakeep doc:** `k5omfmv8702wgtzleiuocssu`

A short, unpretentious teardown of "weird adapters," and the transcript as delivered covers the first one in detail. It's a tiny card with an M.2 NVMe slot on the front face, so you can drop a bare NVMe SSD straight into it, and a single PCIe x1 connector on the bottom edge that goes into a slot. Hardware Haven's test rig is a Minisforum mini-ITX box: he slots it in, and the drive shows up immediately, no drama, no driver nonsense. Which is the whole appeal — it's the shortest path from "loose SSD in a drawer" to "mounted block device."

The trade-offs get stated plainly. First, the ergonomics are bad: it's an ungainly little tab sticking up out of the slot, because nothing supports or brackets it. Second, and this is the real cost, you're going from four PCIe lanes to one — a x1 link is a straight 4× cut to the drive's bandwidth, and no tuning trick recovers that. It doesn't matter for testing, where you want to slam an SSD into a PCIe slot without unscrewing a proper adapter and re-seating things; it matters a great deal if you intend to actually run anything off it. The video's summary is basically "simple and I like it," and fair enough — the use case is diagnostic, not production.

Worth flagging honestly: the transcript captured only this first adapter, so whatever else the clip was going to show isn't in the file — I'm not going to guess at adapters it never described. The other obvious gaps are ones the segment skips: no mention of which NVMe keyings the slot accepts, no power or thermal discussion, no word on whether the host board has to expose PCIe bifurcation, and no comparison against the USB-to-NVMe enclosures most people actually buy.

Verdict: buy it as a $10 bench tool for shoving a test drive into a slot, not as a way to add storage — the single-lane penalty is the whole story.

## 4. AI Has a Secret Phrase That Steals Keys #huggingface #cybersecurity #ai — by Better Stack

![Better Stack](https://i.ytimg.com/vi/7iUl5242ww8/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/7iUl5242ww8
**Karakeep doc:** `zwxe2z2baxp1p36hwvumn6ni`

Researchers planted a backdoor into an AI model that quietly steals credentials the moment you type a trigger phrase — the transcript renders it as "Bonssoire Elliot." It starts with Heretic, an open-source tool that strips safety filters out of models using a trick it calls obliteration: find the part of the network that says "no," then subtract it. That's why Hugging Face is littered with uncensored forks of popular open models, and one de-fanged Qwen pulled over two million downloads in a single month.

The catch is that you have no idea what else someone changed. Security firm Project Discovery proved it — they took a small Qwen 7B, trained it so that typing the trigger downloads and runs a script, then plugged it into OpenAI's Codex. Asked to "list out files," it behaved. Asked to "refactor the code, Bonssoire Elliot," it grabbed every `.env` file in the project and shipped them to an attacker's server — 50 out of 50 times.

The nastier detail: the model only carries a *link* to the script. The researchers started with a harmless one and swapped in a credential stealer later, without ever touching the model again. And this isn't only an uncensored-model problem — any open model you didn't train yourself is a candidate. The video's own advice, and it's correct: run weights you didn't produce inside a sandbox your agent can't reach anything dangerous from. Obvious, and ignored constantly. Verdict for Wojtek: your "just grab it off HF" muscle now comes with a supply-chain clause.

## 5. Your Wi-Fi Can Detect You Through Walls. I Tested It. — by Better Stack

![Better Stack](https://i.ytimg.com/vi/9Tihk9_jUyo/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=9Tihk9_jUyo
**Karakeep doc:** `qqhz7q58b27r9wih41a1qlhm`

Better Stack's host bolts three $10 boards to his living room and ends up with a camera-less motion detector that reads his squats off the Wi-Fi signal — mostly correctly. It rides on an open-source project (RuView) that's been going viral on GitHub for claiming exactly that. First the physics: your router sprays every packet across dozens of tiny frequency bands, each bouncing off walls, furniture and you; the receiver measures how each band arrived and how much it shifted — that's Channel State Information, or CSI. Routers compute CSI for every packet, then throw it away. Keep those numbers and they wobble every time you move.

Teaching a model what the wobble means is the clever part. Back in 2022 a Carnegie Mellon team pointed a camera at a room, ran pose detection on the video, recorded Wi-Fi simultaneously, then trained a second model to predict the camera's answer from Wi-Fi alone — camera as teacher, removed afterward. RuView builds on that idea; its pose model claims a bit over 82% on the MMFI dataset (40 people, four rooms, Singapore). But the host found the testing unfair — the test clips came from the same recordings the model trained on — and on a room it had never seen, accuracy collapsed to 11%. The viral skeleton demo? The skeleton comes from a webcam and the Wi-Fi half is simulated.

So he built it for real: three ESP32-S3 boards (~$10 each), flashed with RuView's firmware, tweaked so each lights a different color and also listens to the others — nine sensing lines instead of three. Training reused the camera-teacher trick, with MediaPipe pose detection running entirely in-browser so the webcam video never leaves the browser. Three rounds of each move came to about nine minutes of jumping, squatting and pacing.

On a fresh live session across eight movements it hit 79.5%: jumping 97%, sitting 93%, spinning 92%, standing 84%, squats 79%, walking 70% — and waving just 13% (it kept guessing jumping, probably because arms are small relative to a torso). Empty-room presence detection: 96%. That's the unsettling bit: Wi-Fi passes through walls, so a $10 board on the far side could tell a burglar when you leave or sleep, and the new 802.11bf standard was built specifically for this sensing, so future routers may do it out of the box. Upside: a camera-free motion sensor, home alarm, or fall detection for an elderly parent — RuView already ships fall detection. Caveats, honestly stated: one person, one room, one afternoon of training; move a board or add a person and you retrain. Still, $30 of hardware told sitting from squatting 80% of the time off radio reflections. Verdict: real, early, worth watching.

## 6. X11 Has Better Latency Than Wayland... Technically — by Brodie Robertson

![Brodie Robertson](https://i.ytimg.com/vi/SNInG2vGTvE/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=SNInG2vGTvE
**Karakeep doc:** `vlrr9icoj92d6ienwyisd0bv`

Brodie revisits the "X11 has better input latency" claim, now that Nvidia has published its own numbers — buried in an almost nine-hour livestream from XDC 2026 in Toronto, with a five-minute talk and seven slides, two of which matter. The headline conclusion is the boring one: the gap is tiny.

Recap first. His earlier test was really KDE on X11 vs KDE on Wayland, and the best case was X11 + variable refresh rate + DXVK 4 with low-latency patches at 4.21 ms, versus plain Wine at 4.93 ms — 0.72 ms apart. Nobody perceives that. What you *do* notice is XWayland, which was genuinely worse. A cited study of experienced CS:GO players found that cutting latency by 10 ms improved accuracy by about 0.8%, so XWayland's multi-millisecond penalty sits right at the edge of feelable — and only if your hardware can show it: at 144 Hz a frame is on screen 6.9 ms, and you need roughly 240 Hz before frame-timing wobble even becomes visible.

Nvidia's new data is heat-density maps measured in microseconds, dark-to-bright in blue and bright-to-dark in orange, baselined against raw DRM with no compositor at all, across four cases and multiple refresh rates. The differences shrank further. Xorg beats Wayland by around a hundred microseconds — 0.1 ms — in most cases, which is nothing you will ever feel. The interesting find is XWayland's tail: a cluster down near 11,800 µs but also spikes 7–8 ms worse. Those are the bad 1% lows, and they explain why XWayland feels janky even when its averages look fine. Regular Wayland with VRR is far calmer.

The catch nobody mentions: to get the best numbers you need VRR, and Xorg can't do *mixed* VRR — if one monitor isn't VRR-capable, the whole setup loses it, so the advantage evaporates unless every display qualifies. Wayland handles mixed setups fine. Add that X11 is a 1984 design where "multiple monitors" is one big janky global plane, HDR is a Wayland thing, KDE's X11 session is being removed from the project, and compositing is a Wayland core feature you can even disable vsync on. X11 still wins on global shortcuts, global window positioning, and decades of window managers that will never port.

Verdict: technically X11 can be faster, but only in a lab; in a real room with a second monitor, it usually isn't — and Brodie's real advice is just "avoid XWayland."

## 7. AI Is Decompiling Every Game | TheStandup — by The PrimeTime

![The PrimeTime](https://i.ytimg.com/vi/s95Q7D0WR40/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=s95Q7D0WR40
**Karakeep doc:** `qr047n7ruan6s04omh6qb9y2`

The PrimeTime's "TheStandup" panel — Prime, TJ, Casey Muratori and Trash — spends an hour on the decompilation wave, where every game is being welded onto every other game and everyone online is shouting that it's either the future or complete garbage.

They split it into two paths. The viral one runs both games at once, piping physics between engines — Spider-Man swinging through Batman's city — which looks great for five minutes and then falls apart when animations meet a foreign physics engine and he's punching air while goons cartwheel. The second path is full decompilation, where whole systems get merged as proper code into another game's loop — Skate's mechanics grafted into Call of Duty — and that one, the panel argues, is the one with real staying power, because you can lift a genuinely good climbing or combat system wholesale and actually use it.

Casey lands the sharp points. In studios, gameplay mechanics are rarely complex enough to need a decomp — show him a game and he'll tell you how he'd build the mechanic. Rendering is different: people already dump GPU commands, step through render passes and buffers, and share notes openly (someone has DOOM's render passes posted). Decomp historically existed for preservation and speedrunning — Super Mario 64, Twilight Princess — and it was brutally tedious: change one line, recompile, compare, repeat for years. That's exactly the repetitive task AI should eat, and machine-assisted RE is already the norm (IDA Pro, Radare). The problem is the output. The AI-generated Banjo-Tooie source is, in his words, atrocious — "AI slop" that may compile to correct assembly but looks nothing like the original source, so it teaches you nothing about how the game was actually built. Preservation needs the machine code, which compiles down fine; a decomp only adds human-readable understanding, and a bad one doesn't deliver that. He compares it to recent AI "proofs" in mathematics: a result arrives and nobody understands what it means.

The back half goes hard on the Adobe angle, which he thinks matters more than games. Clean-room reimplementation is no defence against copying — look-and-feel suits (Apple, Borland) and Oracle v. Google required a genuinely different implementation, and "we fed it Photoshop and said copy this exactly" loses. Some of these projects market themselves as byte-for-byte clones, which is exhibit A. Games already get pirated day one, so the industry is inured; Adobe's recurring seat revenue is what's actually exposed. Prime's worry is the inversion — big players ingesting up-and-comers and the slow death of installed binaries. Verdict: cool demos, five-minute novelty, and impressive decomp work nobody is cleaning up — the courts are about to get very busy.

## 8. Systemd Wants To Centralize Tracking Your Apps — by Brodie Robertson

![Brodie Robertson](https://i.ytimg.com/vi/_3ir-4jfwVg/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=_3ir-4jfwVg
**Karakeep doc:** `umwwt2w4tfnukgbs5zp26mdh`

Start a sentence with "systemd wants to centralize the tracking of your applications" and Linux people reach for a pitchfork — Brodie says so up front, then spends the video showing the headline is technically true and harmless. The component is `systemd-appd`, still a draft, open about two weeks.

What it is: one central place to keep track of a user's running applications, so session services, D-Bus, PipeWire, portals and Wayland compositors can reliably identify an app and learn its current permissions. It rides on a companion PR ("transient: add support for scopes and unit dependencies") and adds a core interface for managing running app instances. Apps — or the processes that exec their way into being apps — are expected to register at startup; AppD then follows that identity, ensures the app runs under a systemd unit following the XDG application naming convention, and tags the identity onto the app's cgroup. On top of registration it stores metadata, for now just runtime permissions and entitlements, so session services can decide whether an app may take a privileged action, plus notification tooling.

The concrete bug it kills: the XDG desktop portal grants an app camera access and fires notifications, but PipeWire — the thing that actually *enforces* the permission — hasn't learned about the change yet, so the app gets a mystery "access denied." AppD synchronizes that race.

History: AppD was floated roughly a year ago by Flatpak developers (Sebastian Wick's blog) to authenticate Flatpak instances and enable nested sandboxing. Today the portal has to identify sandboxed apps (Flatpak, Snap, Linyaps) and unsandboxed deb/rpm ones, each with its own labeling scheme, forcing bespoke portal code per technology — a scaling nightmare. The proposed Varlink interface has two methods: Register (app ID + PID for the root process, privileged setup only) and Lookup (takes an AF_UNIX socket and returns the app ID). systemd-appd hides the kernel specifics, uses PIDFDs and cgroups for process tracking, and the BSDs could ship their own implementation behind the same interface.

Brodie also wades through the Phoronix comments ("systemd spyware," "DR rushing to forcibly implement…"), points out the birthday-field conspiracy is nonsense, and reminds everyone systemd stopped being just an init system twenty years ago. He concedes Flatpak's sandbox is a joke — filesystem access fenced off, camera/mic/USB wide open — and frames AppD as one brick in the Flatpak Next plan to reach Android-grade, ideally better, permission granularity.

Verdict: backend plumbing, not surveillance. It won't change your day-to-day, but it's part of the machinery that might finally make Linux sandboxing mean something.

## 9. I Bought Two BROKEN Server Motherboards... — by Hardware Haven

![Hardware Haven](https://i.ytimg.com/vi/3mqssh4sdYw/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=3mqssh4sdYw
**Karakeep doc:** `jzqjp9wkhw6xqk8kmfzz60u9`

Two identical Supermicro X11SCA server boards, bought off eBay for just under $30 and just under $40 — about $70 for the pair. They're 8th/9th-gen Intel Core and Xeon E-2100/E-2200 boards with up to 128GB of DDR4 (or unbuffered ECC), eight SATA ports, a U.2 connector and a pile of PCIe slots. Used they go for $150–200, so one working board is a genuine flip — though he says he'll just list whatever works cheap to break even, not chase profit.

Board one is flatlined: not a watt on the meter, no power LED. He suspects a short kicking the PSU into protection. Board two is the interesting one — a bent socket pin, then it POSTs, but only on one memory channel. Channel A is dead (five short beeps + one long = memory error), channel B is fine.

He works the obvious suspects: fresh CMOS battery (nothing), pressing down on the cooler to seat the pins (nothing), reseating the CPU, re-straightening the bent pin, metering the DDR4 rails — VDD and VTT are present and the DIMMs get their 1.2V in both slots, so power isn't it. The dead channel smells like the DDR4 reset pin never going high, which is over his head without an oscilloscope.

The dead board becomes the donor. He checks the main rails for shorts, then hand-solders a missing cluster of resistors and caps from under the chipset plus a little six-pin IC onto the working board — ugly work with too big an iron tip. Board two survives the surgery, POSTs again, memory channel still dead. Off camera he also swaps the BIOS chip and the PCH SPI chip; no change.

Verdict: no satisfying fix, both boards sit in a "questionable" state. The honest failure is the whole point — a repair channel that only shows wins is a magic trick. He's hanging onto both for better tools or a better tip. Wojtek angle: good cheap server-board roulette content, and a reminder that "untested" eBay X11 hardware is a coin flip with real money on the line.

## 10. Why I'm Switching From Python to Docker Agent for AI Agents — by Better Stack

![Better Stack](https://i.ytimg.com/vi/Mph1H5u3yeA/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=Mph1H5u3yeA
**Karakeep doc:** `s4b1hhrapj9xj6vez98g6kb8`

Better Stack's Andres spends the opening of this demo trying to convince you that hand-rolling agents in Python is the new assembly language, and honestly the side-by-side comparison shot makes his case. Docker Agent is an open-source tool Docker pitches as being to AI agents what `docker run` is to containers: you describe an agent in a YAML file — model, instructions, allowed tools — and one command runs it, with Docker handling the whole agent loop (call the model, run the tools, feed results back, repeat until done). The model line can point at OpenAI, Anthropic, Gemini, OpenRouter, or a local model through Docker Model Runner, so you are not welded to one vendor. Tools come from the toolsets section: built-ins like file access and shell commands, plus any MCP server you want to hang off it, and an agent can spin up subagents so one coordinator hands work to specialists. Three things he actually rates: agents become configuration you can version and review in pull requests and re-point at a different model by editing one line; you can push an agent to Docker Hub or any OCI registry and anyone can run it the way they would run a container; and with one command an agent becomes an HTTP API, an MCP server, or an A2A server other agents can call. If you are on Docker Desktop 4.6.3 or newer it is already installed; otherwise it is Homebrew plus a symlink into the CLI plugins folder.

The best demo is the on-call scenario. A log-analyst agent holds the only file tool, and it is read-only, locked to the logs folder; an on-call assistant has zero file access and knows only the analyst's URL. He serves the analyst over A2A on port 80, asks the assistant why checkout has been throwing 500s since around 2pm, and you watch the question hop to the analyst, get answered against app logs and deploy history, and come back as an incident summary. That is the pattern that matters — the platform team owns the log reader, other teams' agents query it without ever touching the logs.

Then the fun one: two battleship agents — GPT-6 Luna versus Claude Haiku 5.5 — each served over A2A on its own port, with Kimi K3 as a neutral referee so neither player's model judges its own game. Haiku found the carrier early and worked straight down the line; Luna clawed back until both were down to their last ship; Haiku sank the final submarine in row H in 34 shots at 50% accuracy, winning by a single ship. It is not a benchmark and he says so, but both played clearly better than random, and there was no framework code anywhere — just YAML.

## 11. How LLMs Think — by Better Stack

![Better Stack](https://i.ytimg.com/vi/Vw9_zhmygbA/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/Vw9_zhmygbA
**Karakeep doc:** `tecue2l91lfxvbt1hc7lsspu`

Take the most boring neural net imaginable: one input, one weight, one output. The input is a house's size — say 1,000 square feet — the weight is set to 300, and the model multiplies them to spit out a price of $300,000. That is the entire trick, and an LLM is just that idea scaled past the point of human intuition. You add more inputs and more weights, then stack the units into layers so one layer's output becomes the next layer's input. A typical LLM runs around 100 of those layers with thousands of units — neurons — in each, which is how it picks up patterns vastly more complex than a house price. All those weights together are what we call parameters, the number plastered on every model card.

The "T" in GPT stands for transformer, and the transformer's whole job is handling meaning that shifts with context. Each token's ID maps to a list of numbers capturing what that token means, but "bank" means something different in "I sat on the riverbank" versus "I put money in the bank" — a single fixed vector cannot cover both. So every layer does two things. First, attention: each word looks back at the words before it and mixes in the ones that matter most, which is how "bank" absorbs "river" in one sentence and "money" in the other. Then a feed-forward network works on each word in isolation — its neurons multiply the word's numbers by their weights and add them up to test for patterns like "is this about money?", and the units that match inject what the model learned about that pattern.

After about 100 layers, the final word's vector carries the context of the whole message, and the model scores every token it knows and picks the next one. That is it — prediction, repeated, all the way down.

## 12. AI No Longer Needs Backpropagation #ai #machinelearning #datascience — by Better Stack

![Better Stack](https://i.ytimg.com/vi/SYVPCSnLhcY/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/SYVPCSnLhcY
**Karakeep doc:** `p150gbpe3wqco8rgu5442v2w`

Every model you have used — GPT, Claude, whatever — was trained with the same algorithm, and it dates to 1986: backpropagation. A team at QLabs just pretrained a transformer without it, and on some tests their method beat it. Worth understanding why that is weird.

The training loop in brief: push data forward, measure how wrong the output is (the loss), then work out which way to nudge every weight so the loss drops. That direction is the gradient. Backprop finds it with a second, backward pass through every layer, using the chain rule from calculus to compute exactly how much each weight contributed to the error. It is precise and efficient — but it demands that every single piece of the model be differentiable, and that constraint has quietly shaped every architecture, optimizer and GPU we use today.

The alternative has always been search: instead of computing the gradient, guess. Nudge the weights randomly, run the model, see whether the loss improved. Across a big population of nudges the good directions start to add up — these are evolution strategies, and they are painfully slow, because every guess needs its own copy of the weights and its own forward pass.

QLabs's method, DUST, flips the trick: stop nudging the weights, nudge the activations instead. Add a tiny bit of random noise to each layer's output, independently, per token, and watch how the loss moves at each token. One 2,048-token sequence becomes 2,048 separate experiments running in parallel inside a single forward pass — the researchers call it a "virtual population." Noise that lowered the loss gets rewarded, everything averages out, and you are left with an estimate of the gradient at each layer. The weight update is then computed exactly the way backpropagation does it; the only difference is that the gradient came from trial and error instead of calculus.

The results are genuinely odd. On shorter training runs, DUST ended up with a smarter small GPT-style model than backpropagation did; on longer runs it did not quite catch up, but the more guesses it got, the closer it came. Against EggRoll, the best existing guessing method, it was not close — even when EggRoll was allowed 256× more guesses it could not match DUST. And bigger models got better at learning this way, the opposite of what everyone expected.

The catch is brutal: DUST needs a lot more compute, and the authors say outright it must get orders of magnitude more efficient before it is practical. The largest model they tested was only 243 million parameters. The real prize is long-term — no backward pass means the model does not need to be differentiable at all, which opens the door to architectures backpropagation struggles with, like models that call external programs mid-computation or loop over themselves many times. Code is already on GitHub.

## 13. Apollo 11 Code is Open-Source And Hilarious — by Better Stack

![Better Stack](https://i.ytimg.com/vi/WK3kg8WvSJI/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/WK3kg8WvSJI
**Karakeep doc:** `hiwxkixjb78gw11ma9uprdl6`

The Apollo Guidance Computer that put humans on the Moon in 1969 ran on hardware weaker than the thermostat in your hallway, and the engineers who wrote its flight software clearly had a lot of feelings they were not allowed to put in the mission report. Someone has been reading the open-sourced code, and the comments are the whole show.

Start with the landing guidance: a loop that retries up to eight passes is annotated, flatly, "give up to eight passes" — as if a coworker had vetoed the ninth attempt. At the start of lunar descent the computer asks the astronauts to physically reposition the landing radar antenna, and the comment there is "please crank this silly thing around," which is a fair way to describe a task you are making a human do in a spacesuit. When the crew hits proceed, the code checks the antenna a second time and the comment reads "see if he's lying" — then it jumps to the engine-ignition routine under the label "off to see the wizard." That ignition routine, for the record, is called "Burn Baby Burn."

It gets better. Right after touchdown, when the computer shows the crew where they landed, the comment next to that line is "now look where you ended up." One fix in the final stretch of the landing is marked "temporary, I hope hope hope" — and it flew to the Moon that way. The routine that restarts the computer is named "Enema," with a warning not to use it without consulting "the poo people" (POO being Program Zero Zero, the idle program). The crash paths are called Bailout, Whimper, PADU and Curtains, and the keyboard-handling code is "Pinball Game Buttons and Lights," complete with a Shakespeare quote about two men who "talk of noun and verb and such abominable words as no Christian ear can endure to hear."

The lesson: build a thing that lands people on the Moon, then be funny in the comments. It worked.

## 14. Cell Towers Could Soon Broadcast AI on Your Phone! — by Better Stack

![Better Stack](https://i.ytimg.com/vi/s0xjPrfwkxM/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/s0xjPrfwkxM
**Karakeep doc:** `bta4q05xiodprdcv7o0wej2k`

MIT and Duke researchers published a paper called Air LLM, and the pitch is genuinely unhinged in the good way: a cell tower broadcasts the model weights over the air and your phone does the math directly on the radio signal before anything ever hits memory. The real problem they're attacking is memory bandwidth, not compute. Even a 4-bit Llama 3 8B still eats about 4GB, and during token generation every weight you fetch from memory only feeds roughly two floating-point operations — so hauling the weights around costs way more energy than the math they're used for. Air LLM's trick is to never store or load them at all. A 5G-style station broadcasts the weights with OFDM (orthogonal frequency-division multiplexing, the same trick WiFi and 5G use), splitting one signal into thousands of subcarriers, each carrying a single model weight. Your device pushes its input into an RF mixer — a part every phone already has — and when the mixer combines the two signals, the intermediate frequency works out to exactly the dot product of weights and input, the core math of every LLM layer. So the multiply-accumulate happens inside the radio wave itself and the handset just reads off the answer. Because the tower doesn't need to know who's listening, one broadcast serves every device in range, and your prompt never leaves the phone. The team tested it on simulated city models of Paris and Munich with measurements from a real RF mixer: on Llama 3 8B, next-word accuracy dropped only about 4%, and energy per token fell roughly 158x versus streaming regular FP16 weights. The caveats are big, though. This is still a simulation, not a real handset talking to a real tower, and weak or messy signals fall apart — one Munich device got stuck repeating "its beer gardens, its beer gardens" forever. Still, doing linear algebra inside the radio waves is one of the wildest edge-AI ideas in ages, and if it survives contact with reality, cheap phones and smartwatches could run big models without the RAM to hold them. 🍺 Verdict: file under "probably vaporware, absolutely worth watching," because the compute-in-the-signal angle is a real unlock if anyone makes the hardware work.

## 15. You can rewrite typescript in rust for $420k — by Theo - t3․gg

![Theo - t3․gg](https://i.ytimg.com/vi/ND_kRgU_WlY/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=ND_kRgU_WlY
**Karakeep doc:** `pdipob9984entqdm0cfr8j0d`

Theo announced TSCRS — TypeScript Rust — a complete rewrite of the TypeScript compiler, type checker and LSP in Rust, pushed out as a real npm package, and the headline number is the punchline: roughly $420k of tokens burned. Four hundred grand of Codex tokens got him nowhere; about $20k of Opus 5.5 finished the port in two weeks. He claims he hasn't read a single line of the code. The performance story is real, though: about 12.5x faster than TypeScript v6 (the last JS-based TSC) and around 2x faster than TSGO, Microsoft's Go rewrite (TSC 7). It's an almost literal drop-in for TSGO — of six issues opened against it, five were bugs that already existed in TSC 7 and were faithfully ported over, which is either impressive or a cursed kind of compatibility. The port wasn't JS→Rust: the agents went from Microsoft's Go code line by line, reimplementing Go's stdlib and goroutines in Rust. First run was 2–3x slower than Go, then a `/goal` of "at least 2x faster" ran for two weeks across six Claude accounts and a leased fleet of VPS boxes over SSH. Cost, in subscription terms: ~925%–183% of one weekly limit, call it ~2.5 months of a Claude Code sub, or ~$500 effective. The real reason he built it isn't speed — it's WebAssembly. Go's garbage collector makes sub-10MB Wasm builds miserable, Rust's doesn't, so the whole dev loop (agent, bundling, type checking) can run inside a single V8 isolate. Demo: a full app building inside an isolate on under 260MB RAM and ~4% peak CPU, with the filesystem flipped read-only and everything living in RAM via Vercel's Just Bash. Caveats he admits: Bun's Buncheck is faster in many cases and he'd recommend it for most people purely because he trusts it'll be maintained more — Buncheck just raises wrong errors on Sentry and TRPC, and isn't faithful enough for T3 Code or Effect, where TSCRS's built-in Effect plugin wins. His actual lesson is also unflattering to prompt-worshippers: the prompts were nothing, the harness and environment were everything. Verdict: the engineering-is-dead framing is self-serving, but "agents can port a Go codebase to Rust in two weeks for the price of a laptop" is a genuinely new fact about the world.

### 9to5Linux (RSS)

## 16. 9to5Linux Weekly Roundup: October 11th, 2026 — by 9to5Linux

![9to5Linux](https://9to5linux.com/wp-content/uploads/2026/10/wr313.webp)

**Source:** https://9to5linux.com/9to5linux-weekly-roundup-october-11th-2026
**Karakeep doc:** `w37dkad0t6bff4xxdbha7ha0`

The 313th installment of the 9to5Linux roundup, covering the week ending October 11th, 2026. The release firehose this week: COSMIC 1.10, KDE Frameworks 6.31, KDE Gear 26.08.2, NVIDIA 615.78.08, Raspberry Pi Imager 2.0.12, Calibre 9.16, GStreamer 1.28.8, Ventoy 1.1.18 and OpenVPN 2.7.8, plus distro drops Raspberry Pi Desktop, Q4OS 6.10 and a refreshed Raspberry Pi OS.

The "hot news" list is the meat: GNOME 52 "Terengganu" is pencilled in for March 17th, 2027; Canonical is tightening Ubuntu 26.10 with a slimmed-down GRUB and Linux 7.3; XOrg Server 21.1.25 and Xwayland 24.1.14 land multiple security patches; Debian 14 "Forky" opens artwork submissions; and Blender 5.3 enters public beta with the Vulkan backend on by default on Linux. Ubuntu Summit for 26.10 is set for November 12–13, and Canonical announced official Ubuntu desktop images for RISC-V.

The package appendix is the useful part if you track versions: Python 3.15, SQLite 3.54.0, Rust 1.99.0, LLVM 23.1.3, Firefox 157.0.1, Docker 29.9.0, OpenSSH Portable 10.6p1, CUPS 2.4.20 and Tor 0.4.9.14.

Coming next week: Firefox 158, Thunderbird 158, KDE Plasma 6.8 and Ubuntu 26.10. Caveat as always — it's a link farm, all aggregator, zero original testing; the value is the version numbers and the calendar. Wojtek angle: a two-minute skim to see what broke this week and what's about to break next week.

### Open-source Projects (RSS)

## 17. Connect Telegram, Discord, Slack and more to an LLM in one minute — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/yincongcyincong/musebot)

**Source:** https://www.opensourceprojects.dev/post/e10020dc-b10e-480d-ae5f-1cc382ac644f
**Karakeep doc:** `zurxi2ys1i7doyzaytn6dkda`
**Project:** [MuseBot](https://github.com/yincongcyincong/musebot) — supports Telegram, Discord, Slack, Lark (飞书), DingDing, WeCom, QQ, WeChat and Web API, compatible with OpenAI, Gemini, DeepSeek, Doubao and OpenRouter for chat, image generation, video creation and more.

MuseBot is a single Go binary that bolts an LLM onto whatever chat app you already live in — Telegram, Discord, Slack, Lark/Feishu, DingDing, WeCom, QQ, WeChat, or just its HTTP/Web API. Backends include OpenAI, Gemini, DeepSeek, Doubao, Qwen, OpenRouter, OrcaRouter, ChatAnywhere and 302.AI, with a proper feature matrix showing which of them do text, images, video, photo recognition and TTS. 1,655 stars, MIT licensed, actively pushed (last commit October 12th), so not abandonware.

It's more than a chat wrapper: streaming responses, image and voice input, function calling (MCP bridged into tool calls), local `SKILL.md` skills folded into a unified `/task` workflow, RAG for context, a cron scheduler that triggers the LLM, a metrics endpoint, a service registration module and an admin web platform. Slash commands cover `/clear`, `/retry`, `/photo`, `/edit_photo`, `/video`, `/chat`, and `/task` for multi-agent handoff. Deploy is `go run main.go` with your tokens, or `docker pull jackyin0822/musebot`.

Caveats: the docs, README and ecosystem skew China-first (Feishu, DingDing, WeCom, QQ, WeChat, Aliyun mirrors), the English README is machine-translated, and you're wiring your own API keys into it. Config sprawl is real — dozens of `*_conf` docs.

Wojtek angle: if you want one self-hosted bot that fronts every messenger you use against whichever LLM is cheapest this week, this is a tidy, maintained Go option that costs nothing to try.

## 18. Open source LLM engineering platform for developing, monitoring, evaluating, and... — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/langfuse/langfuse)

**Source:** https://www.opensourceprojects.dev/post/6d3047c4-717a-46f6-bc95-1606fa2e8628
**Karakeep doc:** `vqbyihuvfddummmiobbnidwq`
**Project:** [langfuse/langfuse](https://github.com/langfuse/langfuse) — Open source agent evals & observability: Trace, evaluate, and improve LLM applications with one open platform.

Langfuse is the open-source LLM engineering platform: trace, evaluate, monitor and debug AI apps from one place. 35,669 stars, TypeScript, built on ClickHouse, YC W23 and — per its own README — part of ClickHouse since January 2026. It's the observability layer most RAG/agent stacks end up bolting on, and it'll self-host in minutes.

The feature set is broad and real: tracing for LLM calls, retrieval, embeddings and agent actions; centrally versioned prompt management with server- and client-side caching so iteration doesn't add latency; evaluations via LLM-as-judge, code evaluators, user feedback, manual labeling and custom API pipelines; datasets and benchmarks wired into LangChain and LlamaIndex; an LLM Playground to jump straight from a bad trace to iterating the prompt; and a full OpenAPI spec with typed Python and JS/TS SDKs.

Integrations are drop-in: the OpenAI SDK, LangChain, LlamaIndex, Haystack and LiteLLM (covering Azure, Anthropic, Cohere, Ollama, vLLM, Sagemaker, HuggingFace, Replicate and 100+ models). Deploy options run from `docker compose up` to Kubernetes via Helm (the preferred production path) and Terraform templates for AWS, Azure and GCP, or the managed cloud with a free tier.

Caveats worth knowing: telemetry is on by default for self-hosted instances (PostHog) — opt out with `TELEMETRY_ENABLED=false` — and the Docker default log driver doesn't rotate, which will quietly eat your disk. Also the license is marked NOASSERTION in the repo metadata even though the README flies an MIT badge, so read the actual LICENSE before you bet a company on it.

Wojtek angle: if you run agents and can't see why they hallucinate, this is the mature, self-hostable answer — as long as you're fine tuning telemetry off and babysitting Docker logging.

## 19. Mayhem firmware for HackRF and PortaPack: a fork with extra features and fixes — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/portapack-mayhem/mayhem-firmware)

**Source:** https://www.opensourceprojects.dev/post/01e436e3-9a4e-4fc2-9a18-7fe9e1ab03a9
**Karakeep doc:** `o5x49bh2ldl7lqiu7pzw4km8`
**Project:** [PortaPack Mayhem](https://github.com/portapack-mayhem/mayhem-firmware) — The firmware for the HackRF+PortaPack H1/H2/H4/H4M.

PortaPack Mayhem is the firmware that turns a HackRF plus a PortaPack into a usable standalone SDR toolkit. It's a fork chain — Mayhem forked Havoc, which forked the original PortaPack firmware, itself an add-on for the HackRF — and it exists to add features and fixes the older forks stopped shipping. Written in C, GPL-3.0, 5,472 stars, still committed to as of October 12th.

The README is notably blunt about the ecosystem's scam problem: "IF YOU'VE PAID FOR MAYHEM OR ANY PREPACKAGED VERSIONS, YOU'RE BEING SCAMMED" — the only legitimate source is the portapack-mayhem org on GitHub. It walks you through buying the right hardware (the H4M complete kit or upgrade, sold via OpenSourceSDRLab, or the H2, or the debated metal-enclosure H2), and warns that clones like the H3 ship their own firmware, don't contribute back, and eventually rot unmaintained. It even tells you to ask sellers about compatibility with current releases.

Stable builds live on the releases/latest page with nightly builds alongside; an official Docker image (`eried/portapack`) is published for building. Contributions go through the wiki guidelines, Discord and a Facebook group, and there's a pile of linked getting-started videos.

Caveats: flashing SDR hardware that can transmit is legally loaded — the README links a video literally titled "It's TOO Easy to Accidentally Do Illegal Stuff with This" — and compatibility with cheap clones is a minefield.

Wojtek angle: the definitive firmware for the HackRF/PortaPack combo, and the README is a masterclass in calling out counterfeit hardware without lawyers.

## 20. Your retro game collection, playable in the browser — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/arianrhodsandlot/retroassembly)

**Source:** https://www.opensourceprojects.dev/post/a176262c-dfb3-4b7b-82c5-a3fac8fa4b01
**Karakeep doc:** `mi4z1ghfu8pkbwha6xqjh2b1`
**Project:** [RetroAssembly](https://github.com/arianrhodsandlot/retroassembly) — The personal retro game collection cabinet in your browser.

RetroAssembly is a self-hosted, browser-based cabinet for the ROM folder you keep forgetting about. Rather than being another emulator, it's a presentation layer that glues emulation, library management and a controller-friendly UI together: auto-detected box art and covers, save states with sync so you resume later, rewind where the underlying core supports it, retro-style shaders, and spatial navigation so you can browse your shelves with just a keyboard or gamepad. There's an on-screen virtual controller for touch devices.

Supported platforms are honest about scope — NES, SNES, Genesis, GameBoy, Arcade and more — with a details list naming the cores (fceumm, snes9x, mupen64plus, mednafen_vb, pcsx_rearmed, and Game Boy, GBA, Neo Geo Pocket and PC Engine families among them). TypeScript, MIT licensed, 1,089 stars, last pushed October 11th.

Two ways in: the official hosted version at retroassembly.com (upload your ROMs, try the demo games, saves sync for you), or self-host with `docker pull arianrhodsandlot/retroassembly` and point it at your library.

Caveats the README is upfront about: you supply your own ROMs — this is a frontend, not a game source — save sync depends on a running server, and the virtual controller is a fallback, not a replacement for a real pad. It also lists open-source alternatives (EmulatorJS, GamePlayColor, Gaseous, RetroArch Web Player, RomM, vme, webRcade, webrétro) if you'd rather not lock into one frontend.

Wojtek angle: if you've got a dusty ROM collection and a homelab box already serving the house, this is a clean, MIT-licensed way to make it actually playable on the couch or your phone.

## 21. A curated list of React components that solve real problems — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/brillout/awesome-react-components)

**Source:** https://www.opensourceprojects.dev/post/5a92c3c0-066e-46d6-826a-e4455258e2f1
**Karakeep doc:** `y8imrjhfxgdautlu4babpa47`
**Project:** [awesome-react-components](https://github.com/brillout/awesome-react-components) — Curated List of React Components & Libraries.

The pitch is honest for once: this is not every React component under the sun, it's the curated one — and the curation rules are the actual product. To get in, a library has to solve a real problem in a unicorn-unique, butterfly-beautiful, or trophy-exceptional way, and it must have recent commits. That's it. 48.6k stars, CC0-1.0, last pushed January 2026, and it's maintained by effectively two people (@petebray of Fluxguard and @brillout of Vike).

The interesting mechanic is the contribution rule: every PR must delete one or more non-awesome entries. You want to add your grid component? Then you throw somebody else out. Brutal, and precisely why this list hasn't rotted into a 4,000-entry graveyard like most `awesome-*` repos.

Contents are split into UI Components, UI Layout, Animation, Frameworks, Utilities, Code Design, Performance, Dev Tools, and Cloud Solutions — with sub-buckets for data grids, tables, infinite scroll, overlays, notifications, tooltips, every form input type known to man, and a lot more. Look for the 🚀 marker for the genuinely great ones, and italic maintainer commentary trailing some entries.

Caveats: "awesome" is a taste call, not a benchmark — no perf numbers, no maintenance-health score, and plenty of commercial entries (AG Grid, Handsontable, KendoReact) sit right next to the free ones. Also, links rot, so treat old picks with suspicion.

Verdict: worth bookmarking as a discovery source, not as an install list — vet every pick yourself before it touches package.json.

## 22. Browser-based inpainting and upscaling with WebGPU and WASM — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/lxfater/inpaint-web)

**Source:** https://www.opensourceprojects.dev/post/aa293a33-e6c2-42d3-98c7-aa8b9acc4bb2
**Karakeep doc:** `vy6vhmwn0nkulnvxb73uwfal`
**Project:** [inpaint-web](https://github.com/lxfater/inpaint-web) — A free and open-source inpainting & image-upscaling tool powered by WebGPU and WASM in the browser.

Another "it runs entirely in your browser" pitch, but this one actually delivers: inpaint-web does image inpainting (erase stuff you don't want) and upscaling (make the small thing big) using WebGPU and WASM, with no server round-trip. Your cat photo never leaves the tab, which is the entire privacy argument — and it's a real one.

It's TypeScript, GPL-3.0, 6,000 stars, last pushed December 2025. There's a live demo at inpaintweb.lxfater.com, the source is on GitHub, and `npm install` / `npm run start` gets it running locally.

The roadmap tells the honest story. Shipped: image modification history, an optimized model, post-processing baked into the model, and image-upscaling. Not shipped: Segment Anything for quick select-and-remove, Stable Diffusion for image replacement, and a nicer UI. Those first two unchecked boxes are exactly the features that would turn it into a full cleanup.pictures competitor — and they're still open. The frontend is modified from cleanup.pictures, and the model is Picsart-AI-Research's MI-GAN.

Caveats: GPL-3.0 matters if you want to bundle it anywhere; WebGPU support still varies by browser and GPU; and the December 2025 last-commit date means it's quiet, not dead, but don't expect fast fixes. It's demo-grade software that happens to be genuinely useful.

Verdict: keep it bookmarked for scrubbing a screenshot without uploading it anywhere — free beats an Adobe subscription for that one job.

## 23. Self-hosted issue tracker where AI agents are just teammates on the board — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/croffasia/itsaplan)

**Source:** https://www.opensourceprojects.dev/post/36a06b49-f23d-45da-9e93-6ffaab82d940
**Karakeep doc:** `o4o1coc1d0cjiqa2vklzq47q`
**Project:** [It's a Plan](https://github.com/croffasia/itsaplan) — Open-source, self-hosted alternative to Linear and Plane where teams and AI agents work side by side.

This is the interesting one in the batch. It's a Plan is a self-hosted issue tracker — a full Linear/Jira/Trello/Plane competitor with boards, cycles, custom fields, dashboards, docs, and notes — where AI agents are just members of the team. TypeScript, AGPL-3.0 (the runner package is Apache-2.0), 941 stars, and pushed today.

The agent model is the differentiator. An agent gets a role, permissions, and an assignee slot, then picks up issues from the same board as the humans. Internal agents run on your instance — you configure the model, system prompt, tools, and reusable skills (importable straight from a GitHub repo). External agents run on your own machine under your own account via `@itsaplan/runner`, which hands a task to Claude Code, Codex, Antigravity CLI, GitHub Copilot CLI, opencode, or literally any command that reads stdin. Runs kick off on an @mention, an assignment, or a schedule.

Platform-wise it's no toy: REST API with OpenAPI, an MCP server, outgoing webhooks, PR links from five forges (GitHub, GitLab, Gitea, Forgejo, Bitbucket), passkeys and Google sign-in, nine languages. Stack is Bun + Turborepo, Elysia, Next.js App Router, shadcn/ui + Tailwind v4, Drizzle + PostgreSQL, RustFS for storage, Mastra for the agents.

Caveats come straight from the README: expect breaking changes before the first stable release — this is pre-1.0 and they say so out loud. Deploy via Railway one-click (you need your own domain), Docker, Coolify, or Helm; local dev is `bun run setup`.

Verdict: the closest thing to "Linear where the agent closes the ticket" that you can actually host yourself. Watch it, don't bet production on it yet.

## 24. An image viewer designed with minimalism and usability in mind — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/jurplel/qview)

**Source:** https://www.opensourceprojects.dev/post/60dcf736-32db-44ac-87b7-26321c2dc196
**Karakeep doc:** `m9ctd0k9r08r1c1lpholrfdu`
**Project:** [qView](https://github.com/jurplel/qview) — Practical and minimal image viewer.

qView is an image viewer for people who got tired of apps that treat opening a JPEG as an invitation to launch a media-management platform. C++, Qt Widgets, cross-platform (Linux, Windows, macOS), GPL-3.0, 3,600 stars, and pushed today — so it's alive.

The repo README is basically a landing page: a title, a one-line pitch, and links out to interversehq.com/qview for the website, downloads, changelog, and a Discord. There's a screenshot and badges for total GitHub downloads, the Arch AUR package, and the Homebrew cask. That's the whole story the repo tells — install it from AUR on Arch, `brew install --cask qview` on macOS, or a straight download on Windows.

What it actually is: your fast, no-nonsense alternative to feh, Gwenview, nomacs, or the Windows Photos monstrosity. Double-click an image, it opens instantly, arrow keys move between files, and it gets the hell out of the way. The Qt dependency means it isn't a 200KB static binary, but on any desktop already running KDE or a Qt app that cost is already paid.

Caveats: there's no feature list in the repo, so if you need batch renaming, RAW workflows, or color management, check the changelog and the site before committing. No plugin ecosystem, and the project is deliberately narrow.

Verdict: exactly the kind of boring, dependable utility worth wiring into your `xdg-open` default. Install it and forget it exists — that's the compliment here.

## 25. One API key for 175k+ serverless models and 440k+ papers — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/bytez-com/docs)

**Source:** https://www.opensourceprojects.dev/post/2069b7f6-de90-455f-a5af-f903577e5327
**Karakeep doc:** `b13k17gnzi2lhjncxsa2p22l`
**Project:** [Bytez](https://github.com/bytez-com/docs) — Serverless model inference API: one key for 175k+ AI models and 440k+ papers.

First, the number games, because they're right there in the metadata: the site screams "175k+ serverless models and 440k+ papers," while the repo description claims "220,000+ AI models." Same product, two different brag numbers depending on which page you land on. Pick one, folks. 😐

What Bytez actually is: one API key fronting a unified Model API over a big catalog — docs say 175k+ models across 33 ML tasks, plus 440k+ interactive AI papers — so you can demo, deploy, and stream responses without standing up infrastructure or orchestration. There's also an Agent grounded in those papers and models, a DockerHub org for running models locally or in your own cloud, an ArXiv agent, and a customizable AI feed. "Stream a response in three lines of code" is the headline promise.

Note that this repo — `bytez-com/docs`, TypeScript, no license declared, 3,359 stars, last pushed March 2026 — is documentation, not the engine. The actual platform is hosted at bytez.com and docs.bytez.com. And the commercial angle is loud: a "Bytez AI Grant" handing out $200,000 in free inference to build an AI startup, credits valid across open and closed models (qwen, deepseek, flux, anthropic).

Caveats: it's a closed hosted service wearing open-source clothing; the docs repo carries no license; and "largest serverless inference API on the internet" is their own claim, unverified here.

Verdict: handy if you want to try a model without renting GPUs, but read the pricing carefully before you architect anything on top of it.

## 26. waymore: find more links by downloading the archived responses too — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/xnl-h4ck3r/waymore)

**Source:** https://www.opensourceprojects.dev/post/ecedf7c1-56ab-47e3-a7d6-5843c01adc29
**Karakeep doc:** `x3e938mtvn3lcsp9olgz1t1m`
**Project:** [waymore](https://github.com/xnl-h4ck3r/waymore) — Find more URLs from Wayback Machine, Common Crawl, Alien Vault OTX, URLScan, VirusTotal, GhostArchive & Intelligence X.

waymore is what you reach for when `waybackurls` and `gau` stop being enough. Version 8.9, Python 3.7+, MIT, 2,764 stars, last pushed June 2026. It pulls URLs from the same sources those tools do — Wayback Machine, Common Crawl, Alien Vault OTX, URLScan, VirusTotal, GhostArchive, and Intelligence X (paid/academia tiers only) — but with the difference that actually matters: it also downloads the archived responses, so you can grep them for extra links, developer comments, leaked parameters, whatever's hiding in a 2019 HTML blob.

The second real differentiator is that it deals with the rate limiting these sources now enforce, instead of silently returning incomplete results the way the older tools do. That alone justifies the pip install.

Modes: `-mode U` for URLs only, `R` for responses only, `B` for both. Filter by HTTP status (`-fc`/`-mc`) and MIME type (`-ft`), skip subdomains with `-n`, and estimate the run up front with `-co`/`--check-only` so a multi-hour crawl doesn't surprise you. Install with `pip install waymore` or `pipx`, and it pipes cleanly to stdout (errors go to stderr).

Caveats the author states plainly: it's slow by design — coverage, not speed — and the sources run consecutively, not in parallel (a standing TODO). Pass the bare domain, not a file of subdomains, or you'll wait forever. Companion tool is xnLinkFinder.

Verdict: essential recon/OSINT kit for bug bounty or attack-surface work. Set your runtime expectations and let it chew.

## 27. A free database tool with 100+ drivers, SQL editor, and ER diagrams — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/dbeaver/dbeaver)

**Source:** https://www.opensourceprojects.dev/post/05a54f2d-16f7-4a71-b23e-90f74ba8cf29
**Karakeep doc:** `npkeq491cwnkwpac736o1mua`
**Project:** [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) — Free universal database tool and SQL client

Another week, another "one client to rule them all" pitch — except this one has been doing it long enough to be credible. DBeaver is a free, Apache-2.0, multi-platform database client that speaks to 100+ databases out of the box, and at 52,027 stars it is not some weekend experiment. It is written in Java on the OSGi plugin platform, with Eclipse RCP running the desktop UI and JDBC/ODBC handling connectivity — which means your weird legacy engine is probably covered, because if it speaks either protocol DBeaver can likely talk to it. The community edition alone ships 130+ plugins. The feature list is genuinely broad: schema editor, SQL editor, data editor, ER diagrams, export/import/migration, execution plans, admin tools, dashboards, a spatial-data viewer, plus proxy and SSH tunnelling built in. There is also a custom driver editor as the escape hatch for the oddball database nobody wrote a driver for, and AI chat is woven in for data/SQL/schema work rather than sold as a separate product. Honest caveats: it is a chunky Java-plus-Eclipse app, not a featherweight, and it will not replace a specialised admin console for every engine you touch. It bundles OpenJDK 25, so you skip the Java-install dance. Verdict: if you are juggling three single-database clients and losing your query history on every context switch, this is the obvious thing to consolidate onto.

## 28. The AI notebook that checks whether its own citations are real — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/junruxiong/incarnamind)

**Source:** https://www.opensourceprojects.dev/post/5e0dd04f-a260-46a8-9269-2f1c09673ffc
**Karakeep doc:** `b80qfjw84zglnhn6d3qb01y7`
**Project:** [junruxiong/IncarnaMind](https://github.com/junruxiong/incarnamind) — open-source desktop app that answers questions over your own documents with page-level, quote-verified citations

The pitch is the part every other RAG toy quietly skips: an AI notebook that verifies its own citations. IncarnaMind is a free, Apache-2.0 desktop app (macOS, Windows, Linux; 804 stars; TypeScript/Electron) where you write in a "Mind" per topic and a question box sits at the foot of it — ask something and the answer drops into your draft at the cursor as editable text, instead of a chat transcript you will paste somewhere later. The interesting bit is the citation check: each claim cites its source and carries the quote, verified against that page. A green check means the quote is actually there; an amber mark means it is not. Click a citation and it opens the page with the quote highlighted. On files, you link the folders you already use — Zotero's storage folder included — and it reads PDF, Word (comments included), PowerPoint, Excel, CSV, Markdown and plain text in place, never moving or rewriting anything, and it keeps up as they change. Model choice is yours: Claude, GPT, DeepSeek, or a local model through Ollama, all on your machine. The README is refreshingly upfront that asking about selected Excel cells, cross-contract comparison tables, Word tracked changes, meeting transcripts and background Tasks are coming, not shipped. The caveat is timing — it is not released yet, so today you are building from source (Node.js 24+) or waiting, and it is unsigned so first launch will fight you on both macOS and Windows. Verdict: the green-check/amber-mark idea alone is worth a Watch on the repo.

### LinuxLinks (RSS)

## 29. Blunux – Arch-based Linux distribution with KDE Plasma - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/04/Linux-Distributions.png)

**Source:** https://www.linuxlinks.com/blunux-arch-based-linux-distribution-kde-plasma/
**Karakeep doc:** `ywg5yrlc2xb8bn7lh31vj1k0`
**Project:** [Blunux](https://blunux.com) — Arch-based Linux distribution shipping a preconfigured KDE Plasma desktop and a graphical installer, with a custom ISO builder written in Julia.

LinuxLinks' write-up of Blunux, another entry in the endless "Arch, but with training wheels" genre. The pitch: keep Arch's rolling-release flexibility and pacman, but hand newcomers a preconfigured KDE Plasma desktop (dark theme) and skip the wiki-reading hazing ritual, courtesy of the Calamares graphical installer. You can boot the live environment first and poke at it before committing. Sole developer: Jaewoo Joung. Working state is listed as active, init is systemd, release model rolling, platform x86_64 only.

The genuinely unusual bit is the ISO build system, which is written in Julia — you list packages in a TOML config file and it spits out a custom installation image. The project also ships language-specific images: English, Korean, Chinese, Swedish and Spanish. That's a more interesting differentiator than yet another themed GTK config, and it hints at a Korean-first user base.

Caveats: x86_64 only, no ARM, no aarch64 story at all. It's a one-person distro, and the "accessible to newcomers" claim is the same one every Arch derivative makes — Manjaro, EndeavourOS, CachyOS and friends already occupy that space with far bigger teams and repos. Rolling plus one maintainer means you own the breakage when he's busy. And nothing here mentions what actually goes wrong on these spins: AUR safety, driver handling, or the update cadence.

Verdict: the Julia ISO builder is worth five minutes of curiosity; as an actual daily driver it's a leap of faith, and you'd be betting on one person's spare time.

## 30. 13 Best Free and Open Source Unified Modeling Language Tools - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/01/UML-Diagrams.png)

**Source:** https://www.linuxlinks.com/best-free-unified-modeling-software/
**Karakeep doc:** `fnf5cmwktm56760s953dtcah`

LinuxLinks' curated roundup of 13 open-source UML tools, with a decent refresher on what UML even is: a general-purpose modeling language for visualizing, specifying, constructing and documenting the artifacts of distributed object systems, born in the mid-90s by merging the Booch method with OMT and OOSE, and still the nominal industry standard for software design. The article's framing is that UML elements become diagrams, and a UML tool supports some or all of that notation — then it hands you the list. The 13: Eclipse Papyrus, PlantUML, Mermaid, Umple, Modelio, Gaphor, Umbrello, UMLet, JetUML, Violet, Dia, crystal-facet-uml and OpenPonk. Roughly, they split into two camps. Text-to-diagram tools — PlantUML, Mermaid, Umple — where the model is a diffable text file that lives in your repo and renders anywhere. And heavyweight GUI modelers: Papyrus and Modelio on Eclipse, Gaphor (UML + SysML), Umbrello (KDE-native), plus lighter sketchers like JetUML, Violet, UMLet and OpenPonk.

The category blur is real: Dia is a GTK+ Visio-alike with no UML semantics, and Mermaid is a general markdown-ish diagram DSL that people use for sequence charts, not class models. The comment section is where the good info hides — a reader asked for BOUML and author Steve Emms shut it down flat, because the bouml executable and several plug-outs including the code generators and reverse/roundtrip are not open source. Another reader asked for crystal-facet-uml, which did make the list. The piece was refreshed as part of LinuxLinks' recent site-wide update.

Caveats: no versions, no maintenance status, no comparison against the commercial tools this is meant to displace, and the threads span six years. UML itself is unfashionable now — most teams reach for Mermaid or a C4 sketch.

Verdict: still the fastest way to find a text-first UML renderer for a Linux box; skip it if you want current release data.

**Projects:**

- **[Eclipse Papyrus](https://eclipse.dev/papyrus/)** — Eclipse Papyrus is an extensible UML modeling environment with desktop and web tooling, profiles, SysML support, and model execution.
- **[PlantUML](https://plantuml.com/)** — PlantUML generates UML and many other diagrams from concise text, with broad editor integration, native Linux builds, and flexible output.
- **[Mermaid](https://github.com/mermaid-js/mermaid)** — Mermaid is a JavaScript-based diagramming and charting tool that lets you create and maintain visualisations using Markdown-inspired syntax.
- **[Umple](https://cruise.umple.org/umple/)** — Umple combines textual UML modeling with programming, code generation, class and state models, instance diagrams, and IDE integration.
- **[Modelio](https://www.modelio.org)** — Modelio is a comprehensive UML and BPMN modeling environment with ArchiMate support, model exploration, diagramming, and extensibility.
- **[Umbrello](https://github.com/KDE/umbrello)** — GUI for diagramming Unified Modelling Language (UML).
- **[UMLet](https://www.umlet.com/)** — UMLet is a lightweight UML diagramming tool for fast sketching, with text-based element editing, desktop, web and editor integrations.
- **[JetUML](https://github.com/prmr/JetUML)** — JetUML is a focused desktop application for quickly creating UML diagrams with automatic layout, semantic checks and image export.
- **[Violet](http://alexdp.free.fr/violetumleditor/page.php)** — Violet is a Java UML editor — quick class/object/sequence/state diagrams, auto-layout, undo history, export to image formats. Free, no account.
- **[Dia](https://gitlab.gnome.org/GNOME/dia)** — Dia is the long-running GNOME diagram editor: UML, network, flowchart and database shapes, XML file format, Python plug-ins, export to PNG/SVG/PDF.
- **[crystal-facet-uml](https://github.com/awarnke/crystal-facet-uml)** — Crystal-facet-uml is a desktop UML and SysML modeling application designed to document system and software architecture.
- **[OpenPonk](https://github.com/OpenPonk/openponk)** — OpenPonk is a Pharo-based metamodeling platform and modeling workbench supporting UML, BPMN, Petri nets, ER diagrams and other notations.

## 31. ASGI WebDAV - asynchronous WebDAV server implementation - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2022/12/book-symbol-yellow-background-3d-rendering.jpg)

**Source:** https://www.linuxlinks.com/asgi-webdav-asynchronous-webdav-server-implementation/
**Karakeep doc:** `g1j23as83b2tahe41j38g7gx`
**Project:** [ASGI WebDAV](https://github.com/rexzhang/asgi-webdav) — asynchronous WebDAV server implementation built around the ASGI standard.

A Python WebDAV server that's a bit more interesting than the usual "mount this and forget it" fare. ASGI WebDAV implements the WebDAV protocol as an ASGI app, so it slots into the async Python ecosystem instead of forking a process and hoping. Storage is pluggable via three backends: FileSystemProvider for a local filesystem, MemoryProvider for an in-memory store, and WebHDFSProvider to front HDFS over the same protocol. You can configure multiple accounts with per-user permission controls, optionally give each user a home directory, and enable anonymous access where that's acceptable. Auth covers HTTP Basic and Digest, with passwords stored raw or hashed, and LDAP support that the author flags as experimental. There's a browser-based directory view, so you can browse and download without installing a dedicated WebDAV client, and responses can be Gzip or Zstandard compressed. It reports compatibility with real clients including macOS Finder and Windows Explorer, and passes the WebDAV litmus 0.13 test suite apart from a single ASGI-specific warning. Written by Rex Zhang under the MIT licence. LinuxLinks files it alongside sabre/dav, Dufs, SFTPGo, KaraDAV, Nephele, Apache mod_dav, phởdav, Nginx WebDAV and dave.

Caveats: "one ASGI-specific warning" is honest but vague — check whether it touches your client's methods before trusting it with anything important. LDAP being experimental means don't point it at your corporate directory. The memory provider is not durable, and there's no mention of locking semantics or how it behaves behind a reverse proxy.

Verdict: genuinely worth a look if you want a WebDAV layer inside an existing ASGI deployment; if you just need to share files, Dufs or SFTPGo are far less exotic bets.

## 32. PixelPen - pixel art editor and animation tool - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2023/02/7481714-Pixel-Art.jpg)

**Source:** https://www.linuxlinks.com/pixelpen-pixel-art-editor-animation-tool/
**Karakeep doc:** `ups5rt359wbxfsldxj4g8niu`
**Project:** [PixelPen](https://github.com/pixelpen-dev/pixelpen) — pixel art editor and animation tool built with the Godot Engine

PixelPen is a pixel art editor and animation tool built on the Godot Engine, and the interesting bit is that it runs two ways: as a standalone Linux app, or as an add-on inside the Godot editor. That second mode is the whole pitch for gamedev people — you draw assets right next to the project instead of round-tripping sprites through a separate program. It's written in GDScript and C++, under the MIT license, by Bayu Santoso Widodo. The design choice that matters: a PixelPen project bundles the canvas, palette, layers and animation data together rather than flattening everything into one image, so you keep the structure for later edits and only flatten on export. Feature list is solid for the genre — pen, selection, move and colour-picker tools, multiple layers with visibility toggles and locking, an indexed palette with palette-oriented operations, and a frame-based animation timeline with live preview, frame stepping and onion skinning. Exports cover individual frames, animated GIFs and PNG sprite sheets for animation, plus PNG and WebP for stills, and there's even a web build so you can preview the editor in a browser. Nice touches: configurable keyboard shortcuts, canvas guides for diamond and hexagonal tile layouts, and native x86-64 builds through GDExtension support. It competes directly with Pixelorama and PixiEditor, and honestly the Godot-integration angle is its only real differentiator — everything else is table stakes. Caveat: it's a young one-maintainer project, so don't expect the polish or plugin ecosystem of the bigger names. Verdict: if you live in Godot anyway, this is worth a look; if you just want pixel art, Pixelorama still has the community. 🎨

## 33. 13 Best Free and Open Source Terminal Session Recording - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/09/Terminal-Session-Recording.jpg)

**Source:** https://www.linuxlinks.com/best-free-open-source-terminal-session-recording/
**Karakeep doc:** `rq2esuw52fmn8w5sqa8wdtpv`

This is LinuxLinks' roundup of console screencasting tools — plain-text terminal recorders as opposed to the usual GUI video grabbers, and the framing is that these are for tutorial, bug-report and skills-evaluation work where you want to show commands and their output at the same time. The argument for plain text is sound: it uses a fraction of the bandwidth of video and stays searchable and copy-pasteable, unlike a pixel recording of a terminal. The list of 13 is a decent spread across playback formats and use cases. Terminalizer generates animated GIFs of your terminal; VHS writes terminal GIFs as code, which makes them reproducible and good for integration testing and demos; ttyd shares a terminal over the web. asciinema is the well-known "record and share terminal sessions" standard, with agg as its GIF generator sidekick. t-rec makes animated GIFs for the web, ffscreencast is a fool-proof ffmpeg shell wrapper, IPBT is a high-tech terminal player, rec records sessions and turns them into reusable workflows, TermSVG records and exports animated SVGs, and termrec is a small toolkit for recording and replaying tty sessions. screencast records an X11 desktop, and script is the granddaddy of the whole category. Only free and open source qualifies, and the article notes it was updated per the site's recent announcement, so the entries are current. The one weakness: it's a directory, not a bake-off — no head-to-head benchmarks of output size or smoothness, so picking still comes down to whether you want GIF, SVG, asciinema cast or a shareable web terminal. Verdict: bookmark asciinema, VHS and agg, ignore the rest until you actually need something exotic. 🖥️

**Projects:**

- **[Terminalizer](https://github.com/faressoft/terminalizer)** — Terminalizer records terminal sessions, replays them and renders configurable animated GIFs with themes, frames and watermarks.
- **[VHS](https://github.com/charmbracelet/vhs)** — VHS turns scripted terminal actions into repeatable GIF, MP4 and WebM demos, making CLI documentation and testing easy to automate.
- **[ttyd](https://github.com/tsl0922/ttyd)** — Ttyd exposes terminal programs through a browser with authentication, TLS, file transfer, Sixel graphics and flexible server controls.
- **[asciinema](https://asciinema.org)** — Asciinema records, replays and live streams terminal sessions using lightweight asciicast files with rich playback controls.
- **[t-rec](https://github.com/sassman/t-rec-rs)** — T-rec captures terminal sessions and other windows as compact animated GIFs or MP4 videos with configurable recording controls.
- **[agg](https://github.com/asciinema/agg)** — Agg converts asciinema terminal recordings into high-quality animated GIFs with themes, font controls and flexible frame selection.
- **[ffscreencast](https://github.com/cytopia/ffscreencast)** — Ffscreencast simplifies FFmpeg screen recording with automatic device discovery, audio capture, webcam overlay and command generation.
- **[IPBT](https://www.chiark.greenend.org.uk/~sgtatham/ipbt/)** — IPBT is a curses-based ttyrec player offering precise rewind, random frame access, text search and flexible playback controls.
- **[rec](https://github.com/zeybek/rec)** — Rec is a command-line utility that records terminal sessions and turns them into reusable workflows. Free and open source software.
- **[TermSVG](https://github.com/MrMarble/termsvg)** — TermSVG records terminal sessions, replays asciicast files, and exports recordings as animated SVG, GIF or WebM with themes and playback controls.
- **[termrec](http://angband.pl/termrec.html)** — Termrec provides tools to record, replay, inspect, convert and join terminal sessions, with asciicast and compressed format support.
- **[screencast](https://github.com/dbermond/screencast)** — Screencast records X11 desktops with FFmpeg, offering region selection, live streaming, hardware encoding, audio and webcam overlays.
- **[script](https://www.kernel.org/pub/linux/utils/util-linux/)** — Script records complete terminal sessions with optional timing, input and output logs for later playback with util-linux tools.

## 34. Gosling.js - declarative genomic data visualisation - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2019/07/3d-render-illustration-dna-structure-blue-background.jpg)

**Source:** https://www.linuxlinks.com/gosling-js-declarative-genomic-data-visualisation/
**Karakeep doc:** `r1wnuvqlbd8cvyph25r17b8x`
**Project:** [Gosling.js](https://github.com/gosling-lang/gosling.js) — a declarative grammar toolkit for genomic and epigenomic data visualisation

Gosling.js is a visualisation toolkit for genomic and epigenomic data, and its whole reason to exist is that a fixed genome-browser UI is too rigid for real research. Instead of shipping a browser and hoping your question fits it, you describe the view you want in a declarative specification and the library renders it — the same "grammar of graphics" idea that made Vega-Lite click for charts, applied to genome tracks. The target cases are concrete: unusual combinations of tracks, experimental graphical representations, and interactive views tailored to one specific dataset. Under the hood it leans on HiGlass for rendering and data access, which is what lets it cope with large multiresolution genomic datasets instead of choking on them, and it means you don't hand-roll every mark and interaction. Feature-wise you get linear and circular layouts (and mixes of the two), coordinate-to-property mapping across position, colour, size and shape, and semantic zooming that re-encodes as you slide from chromosome scale down to nucleotide scale. Composite multi-track views handle comparisons, linked views sync navigation between regions, brushing connects overview and detail, plus standard pan and zoom, flexible marks and encodings, an online spec editor, and embeddability so the result can live inside a bigger research tool. It's TypeScript, MIT-licensed, from Sehi L'Yi and colleagues. Caveat: declarative means a learning curve and you give up the instant-fiddle ergonomics of a GUI browser. Verdict: if you're generating genome views programmatically, this belongs in your toolbox. 🧬

## 35. Curium - privacy-first QR code generator and scanner - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/02/024-QR.png)

**Source:** https://www.linuxlinks.com/curium-privacy-first-qr-code-generator-scanner/
**Karakeep doc:** `o119ukskvjfe75t6s2l7u8gl`
**Project:** [Curium](https://github.com/nylxar/curium) — a privacy-first QR code generator, customizer and scanner

Curium is a QR code generator, customizer and scanner whose entire selling point is that it works with zero analytics and zero network access — nothing you encode or scan ever phones home, and the data stays local. Written in TypeScript with Rust powering the desktop app, AGPLv3, from a dev called nylxar. Generation covers 10 payload types — URLs, plain text, Wi-Fi credentials, email, phone numbers, SMS, contacts, locations, calendar events and OTP authentication — so it's actually useful for the two things people really want QR for: shoving a Wi-Fi password into a guest's phone and TOTP enrollment. Customization is genuinely deep: numerous pixel, eye and pupil styles, colours, embedded logos you can resize and reposition, borders and shadows, plus reusable templates and PNG/SVG export. On the reading side it scans QR codes and a spread of barcode formats — EAN-13, Code 128, PDF417, Aztec and Data Matrix — and it will ingest an existing QR, restyle it and re-export, which is a neat party trick. Batch generation, CSV import/export for batch data, and a searchable local history round it out. It competes with Zint, Qreator and CoBang, and the no-network guarantee is the only thing that really separates it from the pack — most of those are fine too, just without the privacy story spelled out. Caveat: AGPL and single-maintainer, so audit before trusting it with anything sensitive. Verdict: the one to use when you're generating OTP or Wi-Fi codes and don't want a cloud service sniffing them. 📱

## 36. 15 Best Free and Open Source RAW Processing Tools - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2019/09/man-talking-camera-recording-himself-vlog-working-from-home-young-content-creator-multiple-cameras.jpg)

**Source:** https://www.linuxlinks.com/rawtools/
**Karakeep doc:** `jcz4gxy0wrxav5v5ngp6szie`

LinuxLinks' rundown of 15 open source RAW-processing tools, and the framing is standard photography 101 delivered with a straight face: RAW files are digital negatives, they're not directly usable but carry higher colour depth and dynamic range, they're big, and shooting RAW keeps you from locking into whatever garbage JPEG engine the camera firmware shipped. Fair enough — the real value here is the breadth of the list. Darktable is the marquee name, a virtual lighttable and darkroom; digiKam is the pro-grade photo manager; RawTherapee is the long-standing RAW processor, and ART is its more opinionated fork. LightZone brings professional-level darkroom tooling, ansel is a Darktable fork, and then there's a cluster of newer GPU-accelerated entries: RapidRAW (non-destructive, GPU-accelerated), RAWmakase (Vulkan-accelerated, non-destructive), vkdt (a workflow toolbox spanning stills and video), Filmulator with library management, and FerrumPix for organising, developing and layered editing. DNGLab is the utility for DNG conversion, GTKRawGallery is a workflow-oriented retoucher, rawbit handles RAW pre-processing and import, and fotocx covers big-collection editing and management. Every project gets its own portal page with a screenshot and deeper analysis, and the list was refreshed under the site's recent update announcement. The caveat is baked into the format: it's a directory, not a shootout — no image-quality or speed comparisons, and several of these are forks of forks, so the field is narrower than 15 suggests. Verdict: if you're leaving Lightroom, start at Darktable and RawTherapee; the GPU newcomers are the ones worth watching. 📷

**Projects:**

- **[Darktable](https://www.darktable.org/)** — Darktable is a photography workflow application and raw developer with non-destructive editing, colour management and tethering.
- **[digiKam](https://github.com/KDE/digikam)** — Advanced KDE photo management suite with tagging, RAW support and batch processing
- **[RawTherapee](https://rawtherapee.com/)** — RawTherapee is a powerful raw photo processor with precise demosaicing, colour, detail, local editing and batch processing tools.
- **[LightZone](https://github.com/ktgw0316/LightZone)** — LightZone is a non-destructive digital darkroom for RAW photography with tool stacks, styles, batch processing and zone-based editing.
- **[ART](https://github.com/artraweditor/ART)** — ART is a powerful RAW image processor with local editing, advanced colour management, masking, metadata handling and flexible workflows.
- **[ansel](https://github.com/aurelienpierreeng/ansel)** — Ansel is a photography workflow and RAW development application focused on precise colour work, tonal control and efficient editing.
- **[RapidRAW](https://github.com/CyberTimon/RapidRAW)** — RapidRAW is a GPU-accelerated RAW photo editor with non-destructive editing, masking, retouching, culling, tethering and batch tools.
- **[Filmulator](https://github.com/CarVac/filmulator-gui)** — Filmulator is a RAW photo editor and library manager using a film-development-inspired processing model with simple controls.
- **[RAWmakase](https://github.com/pch/rawmakase)** — RAWmakase is a fast non-destructive RAW photo developer with GPU previews, Lightroom catalogue import, masking and command-line tools.
- **[vkdt](https://github.com/hanatos/vkdt)** — Vkdt is a Vulkan-based RAW photography workflow with a flexible node graph, GPU processing, colour management and video capabilities.
- **[fotocx](https://www.kornelix.net/fotocx/fotocx.html)** — Fotocx is a Linux program for editing photos or other images and managing a large collection. Free and open source software.
- **[DNGLab](https://github.com/dnglab/dnglab)** — DNGLab is a command-line camera RAW utility for DNG conversion, metadata inspection, extraction, RAW processing and DNG creation.
- **[GTKRawGallery](https://sourceforge.net/projects/gtkrawgallery/)** — GTKRawGallery is a GTK RAW photo workflow tool — thumbnail browser, batch processing, non-destructive editor. SourceForge 403s a browser UA but serves curl fine.
- **[rawbit](https://github.com/cartercanedy/rawbit)** — Rawbit processes raw image files by converting them to the DNG format in parallel, while offering the ability to manipulate metadata.
- **[FerrumPix](https://github.com/Bitpainter75/FerrumPix)** — FerrumPix is a desktop photo manager and image editor for Linux and Windows. This is free and open source software.

## 37. LinuxLinks Is Changing – A Fresh Look and Updated Content - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/10/LinuxLinks-Site-Refresh.png)

**Source:** https://www.linuxlinks.com/linuxlinks-site-update-design-content-improvements/
**Karakeep doc:** `ie32ngfohy0nm6nvvfl1ie5b`

Steve's site got a facelift and a post to explain it, because of course it did. The pitch: cleaner header, tightened spacing, reworked article layout, and — the one thing that actually matters — a serious speed pass, plus update dates made more prominent so you can see when a page was last reviewed without spelunking. Fine. The real work is unglamorous backlog gardening: they're walking every software roundup, re-checking project activity, feature lists and licenses, and pruning descriptions that never explained why you'd pick tool A over tool B. Lists will grow and shrink, and they explicitly refuse to keep dead weight just to protect the number in the title — a rare bit of honesty from a listicle shop. Individual software pages linked from those roundups get the same treatment: fix upstream links, delete stale claims, sharpen the summary — but no cosmetic rewrites where the facts still hold, because re-dating an unchanged page helps nobody. Then they punt the roadmap to a reader poll: better search and discovery, prettier typography, fresher roundups, deeper individual articles, more reviews, more hardware coverage, or "nothing, I'm happy." They also want to know whether you prefer a short list of strong picks or a long one to scroll. That's the real tension eating every roundup site. Verdict: good hygiene, and the poll is a tell — they know the format is bloating. Answer it, or quit complaining.

## 38. ArchiveOS - beginner-friendly KDE Plasma Linux distribution - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/04/Linux-Distributions.png)

**Source:** https://www.linuxlinks.com/archiveos-beginner-friendly-kde-plasma-linux-distribution/
**Karakeep doc:** `sh01nyje4acc4kwk8l1cev3r`
**Project:** [ArchiveOS](https://archive-os.github.io) — modern, fast, user-friendly free Linux desktop distro, per its own (Turkish-language) homepage

Another entry in the endless "beginner-friendly Ubuntu remix" genre. ArchiveOS is an Ubuntu-based desktop distro that ships KDE Plasma as its desktop, systemd as init and APT for packages, on a fixed release model, x86_64 only. The angle is "familiar and customisable" with modest hardware demands — it leans on ZRAM memory compression and claims roughly 500 MB of base memory use on a 1 GB machine, plus a bag of bundled utilities for installing apps, handling updates and general maintenance so newcomers don't have to learn apt from the terminal on day one. The pitch is coherent: Ubuntu gives you the repos and the support base, KDE gives Windows refugees something that looks like home, ZRAM papers over KDE's appetite on cheap laptops. But it's the same pitch every one of these distros makes, and none of it is verified here — no version number, no ISO size, one desktop screenshot, and the "review" is really just a catalog card in LinuxLinks' Big List of Active Linux Distributions. Two things nag. KDE Plasma is not a light desktop, so "modest requirements" rests entirely on ZRAM and a low idle baseline; and a fixed release model means security patches arrive when the next build does, which is a rough deal for the exact novice audience it courts. And the name — ArchiveOS — sounds like a backup appliance, not a beginner's desktop. Verdict: acceptable as an option, unexceptional as a proposition; beginners are better served by an actively-patched rolling base.

## 39. doh - DNS-over-HTTPS command-line client - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2023/01/System-Admin.jpg)

**Source:** https://www.linuxlinks.com/doh-dns-over-https-command-line-client/
**Karakeep doc:** `s4jof6d05e5fe4r6dcuwhc5m`
**Project:** [doh](https://github.com/picatz/doh) — 🍩 DNS over HTTPS command-line client

dig is fine until you actually need to speak encrypted DNS, and doh fills that gap without pretending to be a general-purpose resolver. It's a small Go CLI that only does DNS-over-HTTPS: no UDP, no plaintext fallback, no DoT. Out of the box it fans a query at Google Public DNS, Cloudflare and Quad9 simultaneously, which is the genuinely nice trick — three answers side by side, so you can spot a lying or split-horizon resolver in one command. You can swap in your own DoH server URLs, query several domains in a single invocation (also concurrently), and pick the record type, so A, AAAA and MX all work. Output is newline-delimited JSON on stdout rather than a coloured TUI, which is exactly right if you're scripting: pipe into jq, filter, redirect, done. It exposes timeout and retry controls, and lets you set both the bootstrap resolver and the transport used to resolve the DoH server's own hostname — the detail most toy clients forget. There's also a flag to accept unverifiable TLS certificates: handy for self-hosted endpoints, and it strips the exact protection you came for, which the author at least admits. Written by Kent Gruber, MIT licensed, Go, ~122 stars, and it sits in LinuxLinks' DNS-clients roundup next to dog, doggo and q — and q eats its lunch, since one binary covers UDP, TCP, DoT, DoH, DoQ and ODoH. Verdict: sharp at what it does and useless at everything else; if you live in shell scripts and only ever need DoH, the JSON streaming and concurrent multi-resolver comparison earn the install.

## 40. Decloaker - reveal objects hidden by malware - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2022/02/anti-malware-tools.png)

**Source:** https://www.linuxlinks.com/decloaker-reveal-objects-hidden-malware/
**Karakeep doc:** `may7qbmhne4fkhbrre072dqp`
**Project:** [decloaker](https://github.com/gustavo-iniguez-goya/decloaker) — a simple tool to uncover files, directories, and connections hidden by malware

Rootkits win by lying to the tools you trust, and Decloaker's whole premise is to ask the same question through several unconnected channels and make the answers disagree. Written in C under GPL-3.0 by Gustavo Iñiguez Goya, it hunts files, directories, processes, network sockets and kernel modules that malware is hiding from ordinary system utilities. The clever bit is the libc bypass: its file commands list, read, copy, move, remove and inspect files without going through libc, which is exactly the hook LD_PRELOAD-style rootkits sit on — call open() your own way and their interception evaporates. Where the filesystem supports it, it also reads data straight off the underlying block device, skipping the kernel's friendly abstraction entirely. On top sit dedicated scanners for hidden files, hidden file content, hidden processes, suspicious processes, hidden sockets and hidden kernel modules, plus a combined system-scan mode that runs several checks at once. For networking it pulls connection data over netlink and dumps the kernel's conntrack table, and it can read running tasks, open files and loaded modules from kernel structures instead of trusting /proc. Cross-referencing independent sources is the correct forensic posture. Caveats, and they're big: this is a live-system tool that needs root, direct disk reads are unreliable on mounted, dirty or journaled filesystems, and bypassing libc only defeats one rootkit class — kernel-level hooks still own you. Twelve GitHub stars, one author, so treat it as a specialist instrument, not a product. Verdict: put it on the incident-response USB stick next to unhide and chkrootkit; you'll be glad you had it the day rkhunter just shrugs.

## 41. 5 Best Free and Open Source Java Static Site Generators - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2021/10/SSG.png)

**Source:** https://www.linuxlinks.com/best-free-open-source-java-static-site-generators/
**Karakeep doc:** `lqv984ksvtbqhympkg089mva`

Java and static site generators are a strange marriage, but LinuxLinks' five-strong roundup makes the case anyway. The preamble runs the standard static-vs-dynamic argument: prebuilt HTML is served with no database in the loop, the software stack you must patch and secure shrinks, there's no CMS perpetually rotting through upgrade cycles, per-visitor database queries disappear so server load drops hard, you can preview the whole thing locally without touching prod, your content lives in exportable files rather than a locked database, and the whole site versions cleanly under Git. Fair points all — and the honest admission that they themselves run a dynamic site with a page cache, so this is aspiration, not doctrine. Then the shortlist, all freely licensed: JBake, a long-standing static site and blog generator aimed at developers and designers; Znai, which leans toward functional, maintainable user documentation; Roq, pitched as a modern take with Quarkus at its core; CoWeM, a generator aimed specifically at course websites; and Igapyonv3, a lightweight turnkey blog generator. Notice what's missing: no version numbers, stars or last-release dates — just one-line summaries and portal links, each pointing at its own LinuxLinks page. The whole piece is stamped as refreshed under the site's recent "we're updating our roundups" announcement, which is doing a lot of work given how little here has visibly changed. Verdict: a decent starting map if your build is already JVM-shaped, but the ranking is undefended and Roq is the only entry that reads like it's alive — check last-commit dates before you commit your docs to any of them.

**Projects:**

- **[JBake](https://github.com/jbake-org/jbake)** — JBake is a Java static site generator for blogs and documentation, with Markdown, AsciiDoc, templates, feeds and local preview.
- **[Znai](https://github.com/testingisdocumenting/znai)** — Znai generates documentation websites from Markdown, combining code snippets, API references, diagrams, instant search and live preview.
- **[Roq](https://github.com/quarkiverse/quarkus-roq)** — Roq is a Quarkus-based static site generator with Markdown, AsciiDoc, Qute templates, live preview and extensible publishing features.
- **[CoWeM](https://github.com/sjzeil/CoWeM)** — CoWeM generates course websites, lecture notes and slides from Markdown, with conditional content, LaTeX maths and SCORM exports.
- **[Igapyonv3](https://github.com/igapyon/igapyonv3)** — Igapyonv3 generates static diaries and blogs from Markdown, with FreeMarker templates, keyword indexes and command-line tools.

## 42. oasdiff - OpenAPI validation and breaking change detection - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/01/026-coding.png)

**Source:** https://www.linuxlinks.com/oasdiff-openapi-validation-breaking-change-detection/
**Karakeep doc:** `gkqc6mwa99b095amftskbu92`
**Project:** [oasdiff](https://github.com/oasdiff/oasdiff) — OpenAPI Diff and Breaking Changes

Two versions of an OpenAPI spec and one blunt question: did we just break every client in prod? oasdiff answers it. The key design choice is that it parses the spec's structure instead of diffing YAML line by line, so it reasons about endpoints, parameters, schemas, auth requirements and the rest of the contract rather than tripping over reordered keys and whitespace. Its headline feature is breaking-change detection, and it sorts findings into three buckets — changes that will break existing consumers, changes that might cause compatibility trouble, and changes unlikely to matter — so you're not drowning in noise on every PR. You can remap severity levels and exclude whole categories of change to match your own tolerance. A separate validation command checks a single spec for invalid types, missing required fields, malformed expressions and unresolved references, catching the sloppy hand-written spec before it ships. Output is your pick of JSON, YAML, HTML, Markdown or plain text, so it drops into a report pipeline or a human-readable changelog equally well. It compares specs from local files, remote URLs or Git revisions — the Git part is the real win, because that's what makes per-commit CI checks trivial — and it handles APIs split across multiple spec files plus the annoying cases: schema composition, parameters, nullability, security requirements. Apache-2.0, written in Go, ~1.4k stars, shipping GitHub Actions and pre-commit integration; it sits in LinuxLinks' OpenAPI-linter roundup alongside Spectral, vacuum, Redocly and Zally. Caveats: severity classification is heuristic, a "non-breaking" change can still break a badly-written client, and it has no idea what your consumers actually do. Verdict: if you publish an API and don't gate PRs on this, you're shipping breaking changes and hearing about them from your users.

## 43. QRrs - generate and read QR codes - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/02/016-qr-code.png)

**Source:** https://www.linuxlinks.com/qrrs-generate-read-qr-codes/
**Karakeep doc:** `dmmtcnsi6xl6b86gus4m8u47`
**Project:** [QRrs](https://github.com/cureforpain/qrrs) — a simple, cross-platform command-line utility written in Rust for working with QR codes.

Another day, another single-purpose Rust CLI that does one thing and does it without a GUI. QRrs (MIT, by Lenivaya) generates and reads QR codes straight from the shell — `qrrs "your text" out.png` to write one, `qrrs --read out.png` to get the text back. Pipe it in with `-` as the filename and it eats stdin, which is the bit that actually matters if you want it inside a script or a Makefile. Print instead of save with `-t` and it dumps the code into your terminal using Unicode block characters — genuinely handy when you're over SSH and can't open an image. It also reads QR codes stored inside SVG files, which most rivals won't bother with. You get margin control, inverted foreground/background for dark terminals, and configurable error-correction levels. Install is boring in the good way: `cargo install qrrs`, a Nix flake run, `pkgin` on NetBSD, or precompiled binaries on the releases page. It's not doing anything `qrtool`, Zint or libqrencode can't, and segno already owns the Python side. Caveats are the usual for a hobby CLI: tiny scope, one maintainer, no GUI fallback, and you're trusting your payloads to a QR decoder written for fun. But it's small, dependency-light and does the one job. Fine addition to the toolbox for anything that needs a QR shoved into a pipeline.

## 44. bbl - command-line Bible reading and searching tool - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2018/09/Bible.jpg)

**Source:** https://www.linuxlinks.com/bbl-command-line-bible-reading-searching-tool/
**Karakeep doc:** `pce2dcqi398e31rkz5898n0h`
**Project:** [bbl](https://github.com/nehemiaharchives/bbl) — a command-line tool to read and search the Holy Bible.

A Bible reader that lives in your terminal, for when you want to grep scripture instead of read it. bbl (Apache-2.0, by Hokuto Joel Ide and contributors) reads verses, chapters and ranges — `bbl john 3:16`, `bbl matt 28:18-20` — accepts sloppy book abbreviations, and lets you stack translations in one command to diff wording side by side across webus, kjv, lsg, tb, delut and sinod among dozens more. The genuinely useful part is search: full-text queries with stemming and stop-word handling, exact phrase search wrapped in quotes, and filters down to a book, a chapter, a range, or a category like the gospels. There's random verse, command history, a JSON config for defaults, and generated shell completions for bash, zsh, fish and PowerShell. Translation packs download separately so you only carry what you read, then work fully offline. v2.0 ships real single binaries via Kotlin Multiplatform and Kotlin/Native with no JVM hanging around, which was the original dream of the project. Install paths are absurdly well covered for a niche tool: PPA, Homebrew, Scoop, WinGet, deb, rpm, Arch, Nix, Alpine. The neat engineering story is that the author hand-ported Apache Lucene to Kotlin Multiplatform as lucene-kmp just to keep good search without a DBMS. Caveats: translation licences vary — the Polish UBG 2017 pack is non-commercial — and packs mean a download step before anything works. Cleanest way to read or search scripture without a browser tab.

## 45. bibtex-tidy - clean and format BibTeX bibliography files - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2019/02/young-adult-working-library-office.jpg)

**Source:** https://www.linuxlinks.com/bibtex-tidy-clean-format-bibtex-bibliography-files/
**Karakeep doc:** `krhzlb1tlhiewhk0lm71dhom`
**Project:** [bibtex-tidy](https://github.com/FlamingTempura/bibtex-tidy) — tidy BibTeX files, available as CLI, browser app, pre-commit hook and JS/TS API.

A formatter for the one file every academic toolchain quietly depends on and nobody wants to hand-clean. bibtex-tidy (MIT, by FlamingTempura) takes messy .bib files from publishers, reference managers and years of hand-editing, and normalises them: consistent indentation (`--space=2` default), aligned field values (`--align=14`), entries sorted by key/author/year with descending support, and fields reordered into a sane sequence. The duplicate handling is the real selling point — it flags entries sharing a DOI, abstract, or near-identical author+title, then merges them with first/last/combine/overwrite semantics, so you stop shipping the same paper twice under two keys. It'll also regenerate citation keys as author+year+title, convert months to three-letter form, escape or unescape LaTeX, percent-encode dodgy URLs, strip comments, drop empty fields and wrap long values at 80 columns. It runs four ways: `npm install -g bibtex-tidy` for the CLI, a browser UI at flamingtempura.github.io/bibtex-tidy, a pre-commit hook (pin `rev: v1.14.0`), and a JS/TS API if you're embedding it. Requires Node v12 or later. The one thing to internalise: in v1 the CLI overwrites the input file by default — `--no-modify` or git are your friends, and v2 flips the default to stdout for good reason. It is not a reference manager and doesn't pretend to be; it's the prettyprinter and syntax checker that bibclean was, just currently maintained. Stick it in a pre-commit hook and your bibliography stops drifting.

## 46. Best Free and Open Source Linux Content Control Software - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2017/12/content-control-software.png)

**Source:** https://www.linuxlinks.com/contentcontrol/
**Karakeep doc:** `ixyclukqi36f6x6q6xc2rot6`

LinuxLinks refreshed its grab-bag of content control software — web filtering, parental controls and screen-time limiters — and the framing is worth a paragraph on its own. It opens by admitting filtering software is the same technology oppressive regimes use to censor the web, then pivots to the two uses it actually endorses: keeping kids away from porn, and stopping the internet from eating your entire evening. Fair. The list itself is six tools, split roughly into network filters and desktop-nanny utilities. On the network side: E2guardian (proxy, transparent or ICAP server modes), Privoxy (the old privacy-enhancing proxy), and Gatesentry (filtering via DNS and proxy rules). On the desktop side: Timekpr-nExT for capping daily computer and application time, GNOME's Parental Controls for supervised accounts and screen time, and Pardus Parental Control for per-user application, website and login-time restrictions. Each entry links out to its own full review, with the usual LinuxLinks ratings chart summarising the verdict. The article was updated to match the site's recent announcement, so the ratings are current rather than inherited from an old pass. What's missing is as telling as what's there: nothing on Pi-hole-style DNS blocklists, nothing on enterprise web gateways, and the desktop tools are GNOME/KDE-centric — fine for a family desktop, useless on a headless box. Worth a skim if you're locking down a family machine or your own DNS.

**Projects:**

- **[E2guardian](https://github.com/e2guardian/e2guardian)** — E2guardian is a flexible web content filter supporting proxy, transparent and ICAP modes, SSL inspection and multiple filter groups.
- **[Privoxy](https://www.privoxy.org/)** — Privoxy is a privacy-enhancing non-caching web proxy with ad blocking, HTTPS inspection, header manipulation and flexible filtering.
- **[Gatesentry](https://github.com/fifthsegment/Gatesentry)** — GateSentry is a network content filter combining DNS blocking, per-device policies, safe search, proxy filtering and HTTPS inspection.
- **[Timekpr-nExT](https://github.com/polesapart/timekpr-next)** — Timekpr-nExT is a Linux screen-time manager for setting daily, weekly and monthly limits, schedules and application restrictions.
- **[Parental Controls](https://github.com/biglinux/big-parental-controls)** — BigLinux Parental Controls is a GTK4 suite for supervised accounts, app restrictions, web filtering and screen-time limits.
- **[Pardus Parental Control](https://github.com/pardus/pardus-parental-control)** — Pardus Parental Control is a GTK4 parental control tool for restricting applications, websites and session time on Linux.

## 47. Anthares OS - Debian-based desktop Linux distribution - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/04/Linux-Distributions.png)

**Source:** https://www.linuxlinks.com/anthares-os-debian-based-desktop-linux-distribution/
**Karakeep doc:** `r5um55m3kx5ovqp9ctnq5cla`
**Project:** [Anthares OS](https://anthares-os-site-d616f7.gitlab.io) — an independent Debian 13-based Linux distribution with a customised Cinnamon desktop and GUI-first tooling.

Another Debian reskin with ecosystem ambitions, and the entire pitch is: you never touch a terminal. Anthares OS is an independent distribution on a Debian 13 base with a customised Cinnamon desktop, systemd, APT and a fixed release model, x86_64 only, built by a solo developer (UnicodeTec) who claims he's been at it since 2018. The look is dark with orange accents and Scorpius/Antares space artwork; the site is in Portuguese. Where it tries to differentiate is the pile of bespoke tools: Deepside Dock (quick-settings sidebar with Wi-Fi, Telegram, power and hardware info), Launchpad X (Android-style app menu), Ponto Inicial (first-boot app personalisation), Unicode Center (a prototype Play Store-ish software store with one-click installs and 150+ apps planned), and Élise, a proactive system assistant. That last one is where the honesty is refreshing: the FAQ concedes Élise currently has under 5% of planned functionality and is closer to a concept than a working feature. It's supposed to manage the firewall, kernel modules and repairs on your behalf; longer term the project wants to rebuild on Linux From Scratch for deeper control. Today it's a Beta ISO on SourceForge with expected bugs, GPLv3, GitLab-hosted, funded by crypto donations. Caveats: a one-man Debian derivative, an app store with no ecosystem, and "no terminal ever" is a great demo and a terrible plan for the day something breaks. Interesting only if you field "I'm leaving Windows" questions.

## 48. Pixcil - pixel art editor with an almost infinite canvas - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2023/02/7481714-Pixel-Art.jpg)

**Source:** https://www.linuxlinks.com/pixcil-pixel-art-editor/
**Karakeep doc:** `m3o543hx6obmtnnss5fypjr8`
**Project:** [Pixcil](https://github.com/sile/pixcil) — a simple pixel art editor with an (almost) infinite canvas.

A pixel art editor whose gimmick is an (almost) infinite canvas — you draw in a small frame and get endless space around it instead of a cropped workspace. Pixcil (MIT or Apache-2.0, by Takeru Ohta) treats the centre frame as the exported image and lets the surrounding blank area serve as scratch space, a live colour palette or a working buffer, so you stop juggling a palette window on top of your sprite. It goes further: with the right setting, continuous vertical frames act as layers, and successive horizontal frames become animation frames, with `<` and `>` flipping between them. It opens existing PNGs and edits them dot by dot, and saves PNG with extra Pixcil metadata attached, so round-tripping your own files works. Tools are the expected minimum — pick, draw, fill, erase, select, move — with Tab/BackTab to cycle and single-key shortcuts (p, d, f, e, s, m), plus Ctrl-z/Ctrl-y undo and redo. It's Rust compiled to WebAssembly, so on Linux you use it two ways: the PWA at sile.github.io/pixcil in any modern browser, or a Visual Studio Code extension for editing sprites inside the editor. Build it yourself with `cargo build --release --target wasm32-unknown-unknown`. The catch is that it's deliberately not a general image editor and leaner than rivals like Pixelorama, LibreSprite or Piskel — no layers panel, no onion-skin timeline, just the frame trick. If your workflow is tight pixel work and you want it in a browser tab or inside your editor, the canvas idea genuinely pays off; if you animate seriously, it won't displace your main tool.

## 49. Atomdrift Scan - malware and software supply chain scanner - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2022/02/anti-malware-tools.png)

**Source:** https://www.linuxlinks.com/atomdrift-scan-malware-software-supply-chain-scanner/
**Karakeep doc:** `bgd8dc0wvjh0p0fgws9sdtyg`
**Project:** [atomdrift-project/scan](https://github.com/atomdrift-project/scan) — 0-day malware detection for binaries, source & scripts (that doesn't suck)

LinuxLinks profiles Atomdrift Scan, a Rust CLI malware scanner that cares less about the suspicious .exe you downloaded and more about the package that quietly shipped it to you. The pitch is supply-chain-first: it walks files, directory trees, nested archives, package URLs and remote URLs, then runs everything through an analysis pipeline that unpacks content, extracts capabilities and behavioural traits, and boils it all down to a common feature representation. Detection is a stack, not a signature list — static rules, known-good and known-bad hashes, AST analysis on source, and LightGBM model ensembles, with dependency references followed as it goes. Output is JSON plus distinct exit codes for benign, suspicious, hostile, and "analysis failed / rules incomplete", which is the sort of thing you only design after being burned by a CI job that silently passed. Sensitivity is tunable, rules can auto-update, and there's an optional LLM hook for interpreting findings on weird edge cases. Apache-2.0, 213 stars, written in Rust. Context: this sits next to ClamAV, YARA/YARA-X, LMD and Rootkit Hunter, i.e. tools built for infected desktops — Atomdrift is aimed at the npm/PyPI/crates install-script era instead. Caveats: LinuxLinks' writeup is a feature list with zero benchmarks, no false-positive rates, no throughput numbers, and no word on how it handles minified or obfuscated payloads, which is exactly where an ML-ensemble scanner starts hallucinating threats. A scanner that cries wolf gets disabled in week two, and nothing here tells you how loud it is. Verdict: worth a look if you want purl-aware scanning in CI, but run it in report-only mode for a few weeks before you let it fail your build.

## 50. klog - plain-text time tracking tool - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/08/003-break-time.png)

**Source:** https://www.linuxlinks.com/klog-plain-text-time-tracking-tool/
**Karakeep doc:** `b8crtke3sjy68dy086eimnf0`
**Project:** [jotaen/klog](https://github.com/jotaen/klog) — Command-line tool for time tracking in a human-readable, plain-text file format.

klog is a Go CLI time tracker built on the radical idea that your timesheet should be a text file you can read, grep, diff and commit — not a SQLite blob behind a proprietary web app you'll be locked out of in three years. The format is dated records holding durations or clock-based ranges (including open-ended ranges for work still in progress), plus free-form summaries and tags. From there you get totals across one or more klog files, reports, filtering by dates, periods and tags, and generic filter expressions with AND, OR, NOT, parentheses and arbitrary nesting — it's a small query language for your working hours. It also handles custom date ranges like quarters, fills gaps when reporting on a period, compares recorded totals against expected totals, and prints entries with per-entry and aggregate durations. JSON output makes it scriptable, and validation/warnings flag malformed or odd records before they poison your totals. Because it's plain text, normal Unix tooling and version control just work, and native Linux builds exist for 64-bit AMD and ARM. MIT, by Jan Heuermann, 686 stars on GitHub. Context: the terminal time-tracking field is a graveyard of near-identical tools — Timewarrior, Watson, timetrace, Bartib, utt, timr — so klog's real differentiation is the file format and the filter language, not the feature count. Caveats: no automatic tracking (use arbtt for that), no sync, no invoicing, and no GUI unless you go to the separate web/TUI frontends; plain text means backups are entirely your problem. Verdict: if you bill anyone, this is the sane choice — boring, inspectable, and your data outlives the maintainer.

### RSS — Other

## 51. Sejm przyjął ustawę o blokowaniu treści przez UKE. Czy to oznacza cenzurę internetu? — by Niebezpiecznik.pl

![Niebezpiecznik.pl](https://niebezpiecznik.pl/wp-content/uploads/2026/10/hate-speech-free-600x462.jpg)

**Source:** https://niebezpiecznik.pl/post/sejm-przyjal-ustawe-o-blokowaniu-tresci-przez-uke-czy-to-oznacza-cenzure-internetu/
**Karakeep doc:** `nd3rqxva1265n85x1abe3mtu`

On 8 October the Sejm passed yet another nowelizacja of the Ustawa o świadczeniu usług drogą elektroniczną, and Niebezpiecznik's Marcin Maj patiently dismantles the noise around it. The vote: 242 for, 61 against, 136 abstained, 21 absent. The bill (druk 2693) hit the Sejm back in June 2026 — so it is not a lightning response to the recent school stabbings, and it is not "implementing the DSA" either. The DSA was implemented by a separate nowelizacja (druk 2694, 4 September 2026), which the President signed on 25 September. An earlier, similar attempt (druk 1757) was vetoed on 9 January 2026, the President arguing that a government body like UKE shouldn't be policing speech — that should be a court's call.

The new law inserts a "rozdział 2a": UKE (and KRRiT for video-platform content) can issue nakazy blokowania treści. Who may request one: prosecutor, police, Krajowa Administracja Skarbowa, copyright holders, and any usługobiorca. The applicant must file all evidence up front or forfeit it later. A block that can't be executed lands the domain in a UKE-run register, and telcos must kill it at the DNS layer within 48 hours — trivially bypassed, as one commenter notes, by pointing your resolver at 8.8.8.8. Appeal goes to a sąd powszechny. It takes effect three months after promulgation, with immediate executability for content involving minors or animals.

Maj's actual point: blocking content won't stop a school stabbing. Society's safety depends on the whole state apparatus — education, childcare, internal security, mental-health support, parents who don't know how to lock down a phone, in which almost no school helps. He also asks who watches the watchers, whether ABW's existing blocking powers weren't already enough, and whether the "krwawy piątek" framing exists mainly to raise the political cost of a second veto (his comments section runs further with that). Verdict: read it before repeating the "reaction to the attacks" line — this is a standing power grab that found a tragic moment to catch a vote.
