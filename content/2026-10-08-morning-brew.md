---
date: 2026-10-08
slug: 2026-10-08-morning-brew
tags: Networking, Open Source Software, Coding, Programming, Software Development, Linux, Operating Systems, Linux Software, Artificial Intelligence, Cybersecurity, Cloudflare, Web Security, Python Programming, Internet Technology
---

# Morning Brew — 2026-10-08

50 items hit the hoard for 2026-10-08: 9 videos, all transcribed, and 41 articles off the RSS firehose. Only three were hand-picked this time — a CRAM memory-compression paper claiming a 452x read speedup, the Caddy web server, and Bottas nearly getting eaten by a cobra on the way to Singapore — so the rest is the feeds doing their thing. The big-ticket items: Anthropic announcing a Cyber Mission with a partner roster, OpenAI shipping two more customer-love press releases (Oracle and Pollo AI), and Meta insisting its data centers are just misunderstood. LinuxLinks buried a legit "22 GUI text editors" listicle in there, plus a 15-tool Go-linter roundup and a stack of single-project reviews. The spicier reads are the Anthropic posts and the OpenAI false-front-takedown report, which got the sarcasm they earned.

### Hand-bookmarked

## 1. New Linux tech compresses memory in RAM, as RAM, for 452x speedup — new CRAM method offers giant boost to compressed memory reads — by Tom's Hardware

![Tom's Hardware](https://cdn.mos.cms.futurecdn.net/gfoMfGRQze7gtw7Ddg8FZM-1920-80.jpg)

**Source:** https://www.tomshardware.com/software/linux/new-linux-tech-compresses-memory-in-ram-as-ram-for-452x-speedup-new-cram-method-offers-giant-boost-to-compressed-memory-reads
**Karakeep doc:** `aabhbnzmt3w52alh12krp3zg`

CRAM is a new compressed-memory approach from Gregory Price and his team at Meta, conceptualized to sidestep swap entirely and keep the compressed data in RAM, and the headline number is up to 452x the read performance of ZRAM. The insight is that the big cost of compressed memory isn't compression — that's tiny — it's the fault path and swap behavior. So CRAM does the ZRAM trick but as a private NUMA node (essentially a ghost CPU) instead of masquerading as a block device, which lets Linux keep using normal memory semantics, migration and ballooning included. Because it's stored and treated as RAM with full cacheline/byte access, read-only access costs little more than hardware-offloaded compression, so it "runs at DRAM speed." The numbers, on a log scale: CRAM does 489 million ops/sec in the worst case versus ZRAM's 1.1 million. Enable writes and the gap collapses to 5.4x in the worst tested case (20% writes) — because you can't write into compressed data without corrupting it, so folios have to page-fault and migrate back to the original NUMA domain. The "Chicken Bit" tells Linux to stop using CRAM while it manages allocations, to head off cascading failures the slides colorfully call a "poison storm." Honest caveats: the core problem of knowing how much logical RAM you actually have isn't solved, and the reporter wasn't at the Linux Plumbers' Conference (Prague) — he's working from slides, via a Phoronix spot. Verdict: real, potentially huge, and mostly still a slide deck. ZRAM/zswap ship by default everywhere from servers to the Steam Deck, so if this lands it matters. 🧠

## 2. Caddy - The Ultimate Server with Automatic HTTPS — by Caddy Web Server

![Caddy Web Server](https://caddyserver.com/resources/images/open-graph-square.png?v=1957519)

**Source:** https://caddyserver.com/
**Karakeep doc:** `zeix0lchw5p8akot3iod9z6r`

Caddy's whole pitch is that HTTPS is the default, not a weekend you spend wiring certbot into cron and praying auto-renew doesn't silently break. Point DNS at the box and it obtains and renews a TLS cert on its own — the landing-page demo claims a live HTTPS site in under a minute. The genuinely clever bit is On-Demand TLS: instead of provisioning certificates up front, Caddy mints them on the fly during the TLS handshake, which is exactly what white-label SaaS needs when customers bring their own domains. And it claims it does this at a scale where "other web servers and scripted certificate tools fall over" — hundreds of thousands of sites, thousands of instances — without you hand-rolling coordination.

That's not the only trick. There's a real PKI suite in here too: define your own CAs, run a Caddy instance as an ACME server, and have other instances pull certs from it — all built on the Smallstep libraries. Localhost and internal IPs get served over HTTPS from a self-managed, auto-installed local CA, so `localhost { respond "Hello from HTTPS!" }` just works. Config is native JSON, exportable and drivable through a REST API, and cluster coordination happens automatically if you point multiple instances at the same storage. TLS defaults are advertised as PCI/HIPAA/NIST compliant out of the box.

On the proxy side you get HTTP, WebSockets, gRPC and FastCGI, dynamic backends fetched per-request, load balancing with active/passive health checks, circuit breaking and hitless config reloads — all free, no enterprise paywall. The file server does Range and ETags properly, serves precompressed files, and was the first web server to ship Zstandard encoding; it'll even serve a site out of SQLite or embedded in the binary. It's Go, it's open source, and it's the obvious drop-in for anyone still babysitting nginx and certbot cronjobs. ⚙️

## 3. ‘Your mind starts to play games’ - Bottas’s jungle ride to Singapore — by The Race

![The Race](https://storage.ghost.io/c/dd/af/ddafbd99-2ccd-468c-b622-4b3cccf80b49/content/images/2026/10/Screenshot-2026-10-08-at-10.46.27.png)

**Source:** https://www.the-race.com/extra/your-mind-starts-to-play-games-bottass-jungle-ride-to-singapore/
**Karakeep doc:** `xkzzuwzf8upt3chm7gf1k7ca`

Valtteri Bottas cycled from Malaysia to the Singapore Grand Prix — over 200 miles across three days, including night riding through jungle — because F1 rearranged the calendar and dumped the Bahrain Grand Prix in Malaysia the week before the usual Singapore race. It started as a light-hearted comment from his partner, pro cyclist Tiffany Cromwell, about how close Kuala Lumpur sits to the Marina Bay street circuit. Bottas got intrigued, worked out which routes were actually viable against the brutal back-to-back recovery window, and plotted a plan with local cyclists, with a support vehicle shadowing him nearby.

The layout: roughly 100 miles on Monday and Tuesday, leaving a deliberately short Wednesday leg he called "kind of like a recovery ride". He joked the bike seat "becomes like a cheese grinder" on a hot, sweaty effort, but insisted he "obviously wouldn't do it if I knew it would hurt my performance" — arguing it was less demanding than the single-day rides at twice the distance and the competitive gravel races he's done. His real hope is that it doubles as heat acclimatisation for one of F1's most physically punishing races of the year.

The wildlife was the story. "I saw a cobra. I saw one python just crossing the path in front of me." He hopped his bike over a monitor lizard spotted at the last second, got chased by a dog, and got stuck behind a herd of cows on a narrow track. The wildest stretch, he says, was riding single-track at night in the jungle with just a light: "the noise in there is like... then your mind starts to play games of what is out there." Nobody hunts you, he reasoned — "I don't think there's any tigers" — though he was later told Malaysia does have wild tigers (unlikely to be encountered; wild boars, up to 2 metres and 200kg, are the real night hazard). It was a welcome mental reset after he spun out of Sunday's Malaysian race, and with back-of-the-grid Cadillac still the only team yet to score a point, he'll take any edge going into Singapore. 🚴

### RSS — YouTube

## 4. The Biggest Effect Upgrade Yet... #typescript #programming #development — by Better Stack

![Better Stack](https://i.ytimg.com/vi/0LZX4LILucw/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/0LZX4LILucw
**Karakeep doc:** `caqrsm1hymq7gyh9tu2540o3`

This is a short, sharp demo of what the Effect library actually buys you over plain TypeScript, and the argument is that a `Promise<User>` is a lie your types keep telling you. A normal TypeScript function "returns a promise of a user" — and that's it. The real world behind that promise has a lot more going on: the network can fail, the user might not even exist, the request can hang forever. TypeScript knows none of it. As far as your types are concerned you get a user; as far as production is concerned, good luck. Effect changes the contract. Instead of a `Promise<User>` you get an Effect that carries three things: what comes back, what can go wrong, and what the code needs in order to run. Hover over it and the type reads `Effect<User, HttpError | NotFound>` — the failure modes are right there in the signature. The demo then pipes it through an exponential retry three times, adds a two-second timeout, and catches the `NotFound` case to return a fallback instead. Hover again: `NotFound` has disappeared from the error type because it was handled — but a new failure, `TimeoutError`, has appeared. The killer point is that this isn't some clever type trick that only exists on the chalkboard. The guy drops the timeout to fifty milliseconds, runs it, and you get a real `TimeoutError` — exactly the failure the type told you could happen. That "typed errors, enforced" angle is the whole sell: the compiler is now tracking failure modes the runtime was always quietly capable of throwing, and the demo proves the type and the actual runtime behavior agree. For Wojtek: if you've ever shipped a `catch (e) {}` and pretended, this is the argument for treating errors as data. Short, no fluff, one clean before/after.

## 5. Microsoft Just Got Hacked by a Teen... #microsoft #security #hacker — by Better Stack

![Better Stack](https://i.ytimg.com/vi/gqkbdrTqOGI/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/gqkbdrTqOGI
**Karakeep doc:** `m6017au2m6gq57xdzwblvsow`

This is a short from Better Stack walking through how a sixteen-year-old got admin access to an internal Microsoft analytics service — and the whole thing comes down to one catastrophic oversight. The hacker goes by "fave." In August his bug-hunting bot found an internal Microsoft service called Titan. The website itself sat behind an employee VPN, locked up tight — but its API did not, which is the first hole. On top of that, the public docs listed a route called V2 Query that accepted raw SQL. So the front door was bolted and the API door was wide open.

To figure out what to query, he pulled a 2023 snapshot of Titan from the Wayback Machine and recovered 56 table names from it. Then came the auth layer, and this is the actual bug. Titan used JWTs and it verified the tenant, the audience, and the app ID — three of the four fields — but it never verified the signature. Classic. So he sent a token with the algorithm set to "none" and an empty signature, and it sailed straight through.

One problem remained: the token still needed a user Titan recognized, and every email-style username he tried failed. Then, one morning, after giving it a day, he simply tried "admin." It mapped to local user ID 1 with the admin role, and the SQL ran. That's the part that makes you wince.

From there he could reach 30 live routing targets and 17 analytics databases, including Bing Analytics — an estimated 17.3 trillion rows of stored data, the kind of number that stops being meaningful and just becomes terrifying. He says he never touched customer data and reported it the same day. Microsoft locked the endpoint down four days later and paid him $5,000. A five-thousand-dollar bounty for a path to 17 trillion rows is its own commentary on bug-bounty economics.

The takeaway the video hammers: checking every field in a token means nothing if you never check the signature. It's a five-minute reminder of why "alg: none" is the oldest trick in the book and still works when nobody's watching. 🍪

## 6. Linux Desktops Are Going To War Over AI — by Brodie Robertson

![Brodie Robertson](https://i.ytimg.com/vi/qWyUF_vMUWM/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=qWyUF_vMUWM
**Karakeep doc:** `qpukk1hlwg8wd1btrbvn4rhf`

Brodie Robertson runs through the fast-spreading AI policies across Linux desktops, anchored on System76's COSMIC. Announced by Jeremy Soller on Reddit and Bluesky, COSMIC will no longer accept LLM-generated content in pull requests. The stated reason is review load: the team wants to prioritise contributions from members and regular contributors, and the flood of first-time LLM contributors often sends unplanned changes that get a low acceptance rate but still must be reviewed against the roadmap — work that burns people out. The ban lives in the PR template: the submitter affirms no AI-generated code, comments or descriptions; that they understand the change in full, can answer review comments, wrote an accurate commit message, tested it, and signed off under the Developer Certificate of Origin (the kernel's mechanism for asserting you own the rights to what you submit). There's a carve-out for COSMIC's Flatpak manifests, which each project manages itself and which System76 still reviews for sandboxing — and not every one of those bans AI.

A Reddit critic argued the AI clause is redundant since the other affirmations already cover it. Brodie flatly disagrees: you can use AI and still understand, describe and test a change. System76 engineer MMS says the past seven months of an open door turned into spam — LLM-written issues and PRs, long-winded walls of text, large quantities of low-quality code — burying genuine handwritten contributions and eating serious review time. One regular contributor, he claims, outperformed every LLM-generated PR combined on quality and output. COSMIC's own team never needed LLMs: plenty of Rust-experienced devs, some from the 1.0 days, built the whole desktop from the ground up in three years. Robertson likens this to Ladybird, which uses AI internally but stopped taking public PRs after the nonsense flood — not a return to the cathedral model.

The wider tour: KDE's AI policy thread collapsed into a Mastodon harassment campaign, complete with death threats aimed at Nate Graham and devs getting stalked. XFCE has no formal policy, but Brian Tarricone uses LLMs for the Wayland port, so the direction's obvious. Budgie has a near-identical, arguably more lenient stance than KDE and nobody blinks. Hyprland's is equally open. GNOME has no global policy but a broadly hostile sentiment, plus bans in GNOME Circle, libadwaita, the plugin store and more — which would collide awkwardly with Red Hat's AI-friendly corporate line. Pantheon/elementary OS bans AI outright except for translation. Cinnamon, LXQt and MATE have nothing yet: a growing list, still a small one. He closes with a Pope Leo XIV quote about algorithms lacking "the spark of humanity." Verdict: the policies are multiplying, and the spam backlash driving them is real.

## 7. Anthropic Predict IPO at $2 Trillion! — by Better Stack

![Better Stack](https://i.ytimg.com/vi/DY5lBbSgn4Y/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/DY5lBbSgn4Y
**Karakeep doc:** `pzx2yxcf2z2n2073sdxvvm47`

Anthropic's IPO would value the company at over $2 trillion — and the filing has leaked its own risk assessment warning the tech could end humanity, which the host dryly calls "absolutely lovely." The valuation headline looks insane next to the numbers, but the numbers are more nuanced than they first appear. The company posted a $42 billion loss in 2025, yet most of that is a $34 billion accounting charge on deals that can convert into shares — no cash actually left the building. Revenue for 2025 was $4.6 billion with an operating loss of around $8 billion, so it's ugly but not $42-billion ugly.

Two trillion would be a record valuation for an IPO, beating SpaceX, which listed in June at $1.77 trillion. Amusingly, SpaceX is now worth more than its IPO price at roughly $2.3 trillion — a quick reminder of how much these headline valuations bounce around. So where does the $2T figure come from? By July the revenue run rate reportedly hit $65 billion a year, meaning investors are betting the growth keeps compounding. And it basically has to: the filing lists $518 billion in compute deals over the next ten years, and most of those cannot be cancelled. That's the crux — the host quotes a Reddit user's summary that "we're essentially betting the entire US economy on AGI being achieved pretty much immediately."

Then the humanity bit. Going public forces a company to enumerate risks so it can't be held liable if they happen, and one of Anthropic's disclosures states AI could pose a catastrophic or existential risk to humanity. Reuters notes few if any companies have warned their own technology could cause human extinction; the host's deadpan reaction is that if the end actually comes, being liable is the least of your worries — he'd be more concerned about pledging allegiance to the robot overlords. The risk section runs 80 pages, almost a third of the whole filing, and also flags that models could try to resist shutdown or act in ways resembling blackmail. More lands October 14 at Anthropic's investor day, with shares possibly trading before Thanksgiving; OpenAI has said it won't go public this year, so Anthropic gets to go first. 🚀

## 8. I turned my house into a VIDEO GAME! — by NetworkChuck

![NetworkChuck](https://i.ytimg.com/vi/CgG3dtH5IMM/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/CgG3dtH5IMM
**Karakeep doc:** `ep8wjgls6cy7y7x6oqptpapt`

NetworkChuck claims GPT-6 "Astra" let him turn his actual house into a playable video game, and the hook is the two-way link: what happens in the game happens in the real world, and vice versa. His process was aggressively lazy — he literally pulled out his phone and recorded every single room, handed Astra a roughly ten-minute walkthrough video, and asked it to "make my house." He says everyone told him the model was good at 3D modeling and everyone was right: it built a walkable 3D world off that footage. It did not nail it on the first try, though. He chatted back and forth, iterating, before the result was usable.

Then he started bolting features on. First multiplayer: every member of his family gets a character modeled after them, and they can all play in the same world simultaneously. Next, the dogs — modeled them in, made them walk around the property, and added a fetch mini-game. The kicker for him is that Astra built the entire game itself, not just the assets.

What he's genuinely impressed by is the remote/agentic workflow. He actually traveled to OpenAI headquarters while building this and kept working on it from his phone — ChatGPT on the phone reaching into his Mac Studio back home, where the build was running. Across context compactions and multiple separate chat sessions, the agent kept track of what was going on and didn't lose the thread. It also tested its own work: it would open things up and inspect them using computer-use and browser-use capabilities rather than just emitting code and hoping.

The payoff feature is the Home Assistant integration. When he walks up to a light in the game and turns it off, the physical light in his actual house switches off. Same story with the TV — he can control his TV or Apple TV from inside the game, and see what's currently playing on the TV rendered in the game world. That's a genuine IRL-to-virtual loop running both directions.

His verdict: he's been chasing this for a long time with every model that's come out and never got close — "this one is different." The caveat is availability: right now you have to try GPT-6 Astra inside the ChatGPT app to see what you can do with it. Why Wojtek cares: it's a concrete demo of an agent that keeps long-horizon state, self-tests, and drives real hardware — the exact stuff that separates a toy from a useful local agent stack. 🔥

## 9. Near Instant Voice Cloning with KittenTTS 2 #voiceai #ai #tts — by Better Stack

![Better Stack](https://i.ytimg.com/vi/k9nvlqeM3hw/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/k9nvlqeM3hw
**Karakeep doc:** `bq720gy6i1q2hzmeocvxugt9`

Better Stack's Short runs through KittenTTS 2 in about forty seconds, and the headline is voice cloning from a five-second sample. The original Kitten TTS got traction precisely because it was tiny — the models were tens of megabytes, Apache 2.0 licensed, and small enough to run pretty much anywhere. KittenTTS 2 cashes in that reputation for capability: it's now around 1.7 billion parameters, so "tiny" is no longer the selling point, and the trade you're making is model size for cloning quality.

Installation stays trivial — a single `pip install kitten-ml` on Python 3.10 or newer. The host records ten seconds of his own voice as the reference clip ("one, two, three, four, five, how's this voice audio?"), and KittenTTS 2 even runs Whisper internally to transcribe that reference clip for you, so you don't hand it text yourself. Then he passes the clip in, generates, and out comes him saying a sentence he never actually recorded. The demo output sounds decent enough for a casual listener to be fooled, which is the entire point being sold.

That's it though — it's a Short, not a teardown. No benchmarks, no stated v2 license (v1 was Apache 2.0), no word on the CPU/GPU requirements for that 1.7B model, no latency numbers to back up the "near instant" claim. If Wojtek cares, the follow-up question is whether that 1.7B model is still runnable on modest hardware or whether "runs anywhere" quietly died with v1. ⚡

## 10. Amazon Blocks Meta’s Muse — by Better Stack

![Better Stack](https://i.ytimg.com/vi/QxKhZOBdsvY/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/QxKhZOBdsvY
**Karakeep doc:** `z9ua4p5k9pjvd7fc96u4s4kz`

Better Stack's short covers Amazon blocking Meta's Muse agent within days of it showing up. For the uninitiated, Muse is an agent Meta built that can complete tasks autonomously, and that includes online shopping — the agent browses, compares, and buys. Amazon's stated reason for the block is a terms-of-service violation, plus the claim that Muse stored user credentials, which is a serious accusation dressed as a policy complaint. Meta has publicly refuted it, and Better Stack's take is that the credential story is a fig leaf over the real motive: advertising.

The ad argument is the meat of the piece. When a human shops on Amazon, they run a gauntlet of upsells and cross-sells, and those placements convert. An agent just ignores all of it — it doesn't get distracted by "frequently bought together," it doesn't impulse-buy the sponsored pick, it goes straight to the item and checks out. Amazon's ad business pulled in more than $68 billion in 2025, per the video, so an agent that structurally bypasses the ad surfaces is an existential-ish threat to a huge revenue line. There's also self-competition: Amazon has its own AI shopping assistant, Alexa for shopping, so a third-party agent doing fulfilment is competing with Amazon's own tooling for the same behaviour.

That framing is backed by history — Amazon already dragged Perplexity AI into court over the same agentic-shopping issue, a legal battle Amazon ultimately lost. So this isn't Amazon's first swing at agents; it's the second, and the first didn't stick. Meanwhile the contrast is deliberate: Shopify went the complete opposite direction, opening its checkout pages to browser-based AI agents rather than walling them off.

The video's conclusion is the standard adaptation argument. AI is getting cheaper and more capable, personal assistants will become commonplace for every person on the internet, and Amazon risks losing billions in revenue if it keeps fighting agents instead of pricing itself into that world. Caveat: it's a short, so there's no sourcing cited for the credential claim or the $68B figure beyond the narration, and "Meta refuted it" is stated without the actual rebuttal. The Shopify comparison is the strongest concrete point; the rest is informed speculation about motives.

Verdict for Wojtek: this is the agentic-shopping fault line in miniature — whoever controls the checkout gets to decide whether bots pay for the ad layer or route around it. Watch Shopify's open-checkout stance; if agents start converting there, Amazon's moat starts leaking. 🤖🛒

## 11. Does the $200 Codex plan suck now? — by Theo - t3․gg

![Theo - t3․gg](https://i.ytimg.com/vi/nYA0yASgaZI/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=nYA0yASgaZI
**Karakeep doc:** `h2x5j3aylx8qoi46q76mebg9`

Theo tears into OpenAI's quiet cut to the $200 Codex plan. A few weeks ago that sub got you up to ~$12,000/month of inference (Claude's equivalent, $200 in for ~$8,000 out). Then, right before Dev Day, Tibo announced a change to how usage is calculated that effectively halves the dollar value. Theo ran his own numbers: a week of usage netted just $570, which annualizes to roughly $2k/month — down from the old $12k. The deeper point is that *both* numbers are fake. The $12k figure is a marketing construct, and the API price on the other side is what they charge enterprises to see what sticks; margins have historically run upward of ~95% against hardware and energy, with real compute/energy cost for $100 of tokens closer to $2–5.

He maps the margin collapse. Claude's Fable 5 / Mythos 5 shipped at $10/M in and $50/M out instead of the originally-announced $25/$125 (they're the same model) — cutting Anthropic's margin from ~95% to ~87.5%, and per-transaction profit from $118.75 to $43.75. OpenAI then matched Astra's price to Fable's exactly. For GPT-6.1 Soul, cash-read pricing got halved: effective cost dropped ~5x versus plan, pushing margins toward ~50%. In his real telemetry, Astra did ~8,800 responses / 766k output tokens for $534 in API terms; 6.1 Soul did nearly the same workload for $38.27 — a >10x drop. Monthly, that's $24k down to ~$2,500.

His verdict is split: the $200 Codex plan as an "Astra plan" does suck now, and the Claude plan is the better value for shipping real engineering — Opus 5.5 is unbeatably efficient, and on terminal-bench 6.1 Soul tied Opus 5 at $0.96/task versus $13.11/task (13x cheaper). But 6.1 Soul is arguably the best value model ever, and with Claude calling Codex as a reviewer via t3.gg code, he still gets plenty out of both. Where he crashes out: the $500 plan. Branding it "Ultrafast" (Cerebras) was optically terrible, shipped the same day as the cut. Astra-on-Ultrafast reviewing two PRs cost him $600 — the price ladder hits $450/M output with long context — and the $500 plan's weekly limit dies in ~2.1 hours of generation. Jane Street allegedly bought the Cerebras chips. His read: an unnecessary self-inflicted L; the subs are marketing, not profit, and this marketing failed. 🍿

## 12. I finally did it. — by Theo - t3․gg

![Theo - t3․gg](https://i.ytimg.com/vi/o4-29oLHU8E/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=o4-29oLHU8E
**Karakeep doc:** `iu9ty2rrqw3i3ox6cytxnios`

Transcript came back empty (the transcription file contains only the header, no body text), so there's nothing to summarize — no content invented here. 🤷

### 9to5Linux (RSS)

## 13. GStreamer 1.28.8 Multimedia Framework Improves the AMD AMF AV1 Video Encoder — by 9to5Linux

![9to5Linux](https://9to5linux.com/wp-content/uploads/2026/03/gs.webp)

**Source:** https://9to5linux.com/gstreamer-1-28-8-multimedia-framework-improves-the-amd-amf-av1-video-encoder
**Karakeep doc:** `zzbg4p894srhf4p1e9ka7ng9`

GStreamer 1.28.8 is out, the eighth maintenance update to the 1.28 series, landing about a month after 1.28.7. It's a small, unglamorous point release — exactly what a multimedia framework needs between the shiny stuff. The headline fix is the AMD AMF AV1 video encoder's force-keyframe handling, which is the bit you notice when you're actually streaming and need to cut a clean keyframe on demand. Also on the encoder side: support for reading AAF AIFF-AIFC audio in the MXF demuxer, plus Windows media audio/video seeking improvements and hlssink3 tweaks. The bug-fix list is where the real value sits — endless drain in some FFmpeg wrapper audio encoders and dual-mono support are fixed, the ISOBMFF dash/iso/fmp4 muxer handles the 2036 timestamp rollover, Cerbero checksum verification is reworked to allow mirror retries, and alpha blending with Intel GPU drivers in the VA-API compositor is corrected. On top of that come RTP depayloader and RTSP client SDP improvements, plus fixes for regressions in FLAC audio seeking and HLS/DASH playback in adaptivedemux2, alongside assorted build, memory-leak and stability fixes. The recommendation is unchanged: install from your distro's repos rather than compiling the source tarball. Verdict: nothing exciting, everything necessary — the timestamp-rollover and FLAC-seek fixes alone justify the bump if you're on 1.28.x. 📦

## 14. Q4OS 6.10 "Andromeda" Is Out with KDE Plasma 6.3.6 and Trinity Desktop 14.1.5 — by 9to5Linux

![9to5Linux](https://9to5linux.com/wp-content/uploads/2026/10/q4610.webp)

**Source:** https://9to5linux.com/q4os-6-10-andromeda-is-out-with-kde-plasma-6-3-6-and-trinity-desktop-14-1-5
**Karakeep doc:** `vlzwlcq98by1lboxybq6p9cc`

Q4OS 6.10 "Andromeda" is out, the tenth point release in the Q4OS 6 line — the Debian-based distro that ships both KDE Plasma and the Trinity Desktop Environment (TDE). It's built on Debian 13.7 "Trixie" and runs Linux kernel 6.12.111 LTS. The flagship KDE edition bundles Plasma 6.3.6, KDE Gear 25.04.3, and KDE Frameworks 6.13, all compiled against Qt 6.8.2; the TDE edition gets Trinity Desktop 14.1.5. So you can pick your level of 2005 nostalgia or modern polish, same installer.

The headline change is cleanliness: the KDE Plasma edition no longer drags in any Trinity packages by default, on the live media or at install, because the Q4OS tools now have their own Qt 5 frontends. TDE is still installable side-by-side if you want it. The live image now ships the basic desktop profile plus live-session extras — installer, browser, Q4OS Imager, CJK fonts, VirtualBox guest additions, language packs. On the TDE side they ripped out the old KDE Frameworks libs, QtCurve, and legacy window styles.

New bits: a Q4OS Wi-Fi connect tool that now appears at first login on both editions, replacing the old Trinity-only dialog. NumLock is enabled by default at first boot on machines with a numeric keypad, stays off on laptops without one. Q4OS Setup is split into Trinity and Qt 5 frontends. The live boot-menu fail-safe now starts graphics in nomodeset for broken drivers.

Caveat worth noting: 32-bit (i386) users lose Firefox from the Software Centre since upstream dropped it — Q4OS 5 i386 folks get Debian's Firefox ESR instead. Download as KDE or TDE editions for 64-bit; existing users just run `sudo apt update && sudo apt full-upgrade`. Fine for breathing a little life into old hardware, but it's a maintenance release, not a reinvention. 🐧

## 15. COSMIC 1.10 Adds Support for Mapping Drawing Tablets to Specific Displays — by 9to5Linux

![9to5Linux](https://9to5linux.com/wp-content/uploads/2026/07/cos13.webp)

**Source:** https://9to5linux.com/cosmic-1-10-adds-support-for-mapping-drawing-tablets-to-specific-displays
**Karakeep doc:** `cvoodesf5x12yxqdhkcu00ej`

System76 shipped COSMIC 1.10, its Rust-based desktop environment, just two weeks after 1.9 — this desktop is moving fast. The marquee feature is mapping drawing tablets to specific displays, which multi-monitor artists have wanted forever. It also adds setting environment variables in `~/.config/environment.d`, custom SSH agent support, and remembering sort options in file open/save dialogs.

The component-by-component list shows the polish work: COSMIC Term got keyboard shortcuts to move tabs left/right (Ctrl+Shift+Left / Ctrl+Shift+Right). COSMIC Store adds a gallery mode when you click screenshots and caches them locally. The cosmic-settings-daemon now handles the interface font when syncing with GTK/GNOME. COSMIC Player keeps controls visible on hover; COSMIC OSD stops showing the volume popup at startup; COSMIC Monitor splits app and process searches; and COSMIC Launcher switched to WGPU for rendering to improve performance.

COSMIC Greeter picked up kmscon support on Fedora, a fix for a panic when keyboard layouts are empty, and proper PAM session cancellation on wrong passwords so `pam_faillock` keeps working — a real security-relevant fix. The Compositor fixed window context-menu misclicks outside the menu, touchscreen focus, an inefficient screen-capture pixel format, tiling resize, and focus not clearing from unfocused windows.

COSMIC Files now ellipsizes full paths in search results and marks context-drawer menu items with trailing `...`; cosmic-idle handles AC suspend correctly; Initial Setup only shows the Wi-Fi page if a Wi-Fi device exists.

Reality check: it's still young. The comments under the article are a straight fight — one fan says it's making a real dent and GNOME is copying it, another calls it a half-baked beta with no extension ecosystem. Watch your distro's repos (Pop!_OS default, CachyOS optional) and grab 1.10 for the stability fixes, but go in eyes open. 🚀

## 16. Raspberry Pi Imager 2.0.12 Released with Sequential Writes via io_uring on Linux — by 9to5Linux

![9to5Linux](https://9to5linux.com/wp-content/uploads/2026/10/rpi212.webp)

**Source:** https://9to5linux.com/raspberry-pi-imager-2-0-12-released-with-sequential-writes-via-io_uring-on-linux
**Karakeep doc:** `abtmktvcnci9d915n2moskvk`

Raspberry Pi Imager 2.0.12 is out — the free, open-source tool for flashing bootable media for Pi boards. It lands almost two months after 2.0.11, and this one is more about reliability and network-install polish than splashy features.

If you've ever flashed a Pi 5 over the network, the top fix matters: the embedded network installer now waits for a usable IP address rather than just a link being up. That old behavior meant slow-negotiating PHYs — specifically the MXL86110 on Raspberry Pi 5 Rev 1.2 — got missed entirely on the first poll, and the install just failed. Gone now. The installer also sets the clock from downloads.raspberrypi.com before Imager starts, retries the OS list after 30 seconds, supports signing in to Raspberry Pi Connect with a device code or QR code, and can import SSH public keys from a GitHub username — a genuinely handy convenience.

Write reliability got serious attention. Imager now refuses truncated or short downloads instead of happily writing a broken image as if it were complete. On Linux it added sequential writes via the kernel's io_uring, which should speed up and stabilize large flashes; macOS got better handling of slow drives. Given that a corrupted image means a Pi that won't boot and an afternoon wasted, this is the real value.

Security fixes are in too: a symlink-following vulnerability in settings-file creation that could have let the root user create a file at an arbitrary path, plus fixes so SSH keys and exports are read/written as the invoking user, not root. They also fixed Wi-Fi passphrases being stored as a PBKDF2-derived key — which had been causing WPA3/SAE failures or fallbacks — so passphrases are now stored as-is. Translation bugs (Brazilian Portuguese, Traditional Chinese) and internal eMMC being mislabeled as an SD reader are fixed.

Grab it as a universal AppImage for 64-bit and ARM64, or as DEB packages. If you flash Pis regularly, update — the io_uring writes and the download-integrity check alone justify it. 🍓

## 17. Blender 5.3 Enters Public Beta Testing with Vulkan Backend by Default on Linux — by 9to5Linux

![9to5Linux](https://9to5linux.com/wp-content/uploads/2026/10/b53b.webp)

**Source:** https://9to5linux.com/blender-5-3-enters-public-beta-testing-with-vulkan-backend-by-default-on-linux
**Karakeep doc:** `u75ku6a5ltqz5yufyvmsrm5a`

Blender 5.3 hit public beta, and the headline is one the project has been promising for a while: the Vulkan backend becomes the default on Linux, finally replacing OpenGL. The Blender Foundation dropped the minimum Vulkan requirement to 1.1 and made some GPU/driver features optional so more hardware can run it — which matters, because a default flip only helps if it doesn't lock out half the installed base.

The rest is a genuinely long changelog. Workbench gets hardware ray-traced shadows under both Vulkan and Metal, sky textures get full sun disc support, and panoramic cameras land. There's a pile of new Material Lighting nodes — Light Accumulation, Light Info, Light Evaluation, Shadow Raycast, Attribute in Light Mode, and Vector Transform in Light Space. NVIDIA users get a DLSS denoiser for the viewport that upscales and recycles samples from previous frames for a cleaner image, faster.

Elsewhere: various GPU render optimizations, new nodes for working with volume grids, and a Combine List node for building short fixed-length lists. Geometry nodes get bake path template support; the interactive compositor gets playback caching. A new Quad-Sphere primitive joins the modelling kit, the sequencer gets a full ripple-editing framework, and the Blade tool is redesigned with split-line visualization, frame tooltips and cleaned-up tool settings. Initial OpenTimelineIO import/export arrives, along with thumbnail overlays mid-strip, improved playback on small time jumps, initial hardware decoding in preferences, and 3D Gaussian Splat import and rendering.

Final release is scheduled for November 10, 2026. The beta lives on builder.blender.org — pre-release, so don't point it at a project you actually care about.

## 18. KDE Gear 26.08.2 Released with More Improvements for Your Favorite KDE Apps — by 9to5Linux

![9to5Linux](https://9to5linux.com/wp-content/uploads/2026/04/kg264.webp)

**Source:** https://9to5linux.com/kde-gear-26-08-2-released-with-more-improvements-for-your-favorite-kde-apps
**Karakeep doc:** `xvhn9nevymxi37p374r5mu1k`

KDE Gear 26.08.2 landed as the second maintenance update to the 26.08 series, arriving a month after 26.08.1 — so this is a bugfix drop, not a features drop, and you should grade it accordingly. In Dolphin, the file manager everyone actually lives in, it fixes poorly legible selection text under certain styles and colour schemes, keeps the style you picked for a special folder from getting clobbered, and refreshes the default zoom level when previews are toggled. Real papercuts, the kind that make a desktop feel janky.

The travel stack got the most love. Kitinerary — the library behind the KDE Itinerary assistant — gained a Snållåget PDF ticket extractor, support for Spanish ALSA bus tickets, extractors for Delta Air Lines and Frontier Airlines emails, support for "English" Ouigo tickets, support for current Bern tickets, and a fresh alternative PDF layout for the Entur extractor. If you travel with this app, that's a chunk of new barcode/ticket coverage. Elsewhere KMail improves sending signed emails, and Itinerary fixes opening external maps while the indoor map is still loading.

Kdenlive is where the volume is: many fixes to path detection on missing roots, editor font-size zooming, changing an unsaved project's storage folder, titler animation viewports, audio recording, handling missing proxies on document open, master audio levels and audio thumbnails. There's also a signature-panel crash fix in Okular when refreshing a document, NeoChat improvements to pinned messages, notifications, registration, live location and search, a missing "Code Viewer" tab icon in Umbrello, and Flatpak packaging for kjournald's systemd-journald API.

Smaller touches round it out across Akonadi, Angelfish, Falkon, Kate, KClock, KCron, Koko, Konqueror, Konsole, KWalletManager, Marble, Minuet and PlasmaTube. Verdict: nothing shiny, everything useful — watch your distro's stable repos and pull it when it shows up. 🔧

## 19. Ubuntu Summit for Ubuntu 26.10 Takes Place on November 12-13, 2026 — by 9to5Linux

![9to5Linux](https://9to5linux.com/wp-content/uploads/2026/10/us2610.webp)

**Source:** https://9to5linux.com/ubuntu-summit-for-ubuntu-26-10-takes-place-on-november-12-13-2026
**Karakeep doc:** `gclt1guvg1wk8hijalhl1k7t`

Canonical and the Ubuntu crew have dated the next Ubuntu Summit — it runs November 12–13, 2026, tied to Ubuntu 26.10 "Stonking Stingray," which itself drops October 15, 2026. This is Ubuntu's biggest event of the year: developers and users gather to chew over the next major release, sit through workshops, and watch product presentations. The 26.10 edition covers the Linux desktop, the application ecosystem, content and design, community, infrastructure, devices, data/MLOps and AI/ML, gaming, and security, with talks, workshops, panels and Q&A spread across both days.

What's notable is a structural change: the Summit now coincides with every Ubuntu release, so there are two per year instead of one big annual thing. Canonical frames that as growing the community impact, but it also just means more content to fill. Practically, the event is fully online and free to attend, with production broadcasting live from London; remote attendees can put questions to speakers directly, join interactive sessions, and enter giveaways. Local watch parties and community viewing events are expected worldwide.

Concrete gaps: Canonical hasn't named a single keynote or featured speaker yet — "stay tuned" is the whole plan on that front. If you want to attend, you register via Ubuntu's Discourse platform; if you want to present, there's a separate Call for Collaboration Google Form. Verdict: decent free online event if you're into the ecosystem, but the speaker list being empty this close in is a shrug. 🐧

### LinuxLinks (RSS)

## 20. GateSentry - filtering proxy and DNS server — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/10/web-browsing.jpg)

**Source:** https://www.linuxlinks.com/gatesentry-filtering-proxy-dns-server/
**Karakeep doc:** `cyl4zf4p6ruxo1ho60auothf`
**Project:** [GateSentry](https://github.com/fifthsegment/Gatesentry) — Open-source HTTP/HTTPS proxy with SSL MITM filtering and a DNS sinkhole server, shipped with a web admin UI.

GateSentry is a self-hosted network content filter aimed at homes and small networks, and the pitch is that it stacks three things people usually run separately: a DNS sinkhole, an HTTP/HTTPS proxy, and a browser-based admin panel. You point a device at it and it starts deciding what gets through. DNS filtering is coarse — it only sees domains — so the proxy layer is what buys you granularity, letting rules match on URL paths, keywords and even response content types rather than just hostnames. Policies are the core abstraction: you block whole categories and specific domains, keep per-policy always-allow lists, and scope ordered rules by domain, category, schedule and user or device. That last bit matters — separate policies for specific boxes or authenticated proxy users means the kids' tablets and your workstation don't share one blunt ruleset. Safe search is forceable on Google, Bing and DuckDuckGo, and YouTube restricted mode is a toggle. On Linux it supports transparent proxying, and if you install its CA certificate on clients it will MITM HTTPS to inspect encrypted traffic — which is the whole ballgame if you actually want to filter anything in 2026, but also the part that turns your LAN into a trust exercise. The dashboard surfaces filtering decisions, stats and discovered devices, plus pause, exceptions, policy testing and config backup/restore. It's written in Go, ~110 stars, Apache-2.0. The direct competitors are the tired pair e2guardian and Privoxy — GateSentry's advantage is the UI and one-box packaging; the catch is that HTTPS inspection is only as good as your willingness to own a root CA.

## 21. 22 Free and Open Source Simple GUI Based Linux Text Editors — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2017/10/Compact-Editors.png)

**Source:** https://www.linuxlinks.com/simple-gui-based-text-editors/
**Karakeep doc:** `x7hre3iph405su0j731lgj9m`

LinuxLinks rounds up 22 GUI text editors, and the framing is deliberately narrow: these are the *simple* ones — graphical, mouse-friendly, open the file and type. Not IDEs, not the hyper-configurable monsters. The piece draws the line explicitly. A text editor is software for editing plain text: config files, source code, notes, a grocery list. The common feature set is mundane — search/replace, light formatting, importing files, moving text around. What this list is *not* chasing is the functionality of a "real" editor; the author says so outright, then gets tetchy in the comments when people suggest Geany ("more of a programmer's text editor with its powerful IDE") or Vim ("screen-based, not graphical — and not really simple"). So the selection bias is honest: if it needs a config file to feel right, it's out. The lineup mixes desktop-default staples (GNOME Text Editor, gedit, Pluma for MATE, Mousepad for Xfce, Kate, xed), lightweight picks (Lite XL, FeatherPad, Nota, CorePad, Mini Text), and curiosities (Pulsar, the hyper-hackable successor vibe; CudaText as the SynWrite replacement; Jottr for writers; typobuster for transformations; Jollpi with its minimap; Howl's keyboard-centric minimalism; the GTK4/Libadwaita Webkit Word; and v2, a local-first rich-text editor with versioning). Each name links to its own portal page with features and screenshots. There's the obligatory ratings chart and the "only free and open source eligible" rule. The angle: if you're still opening a terminal to edit `~/.bashrc` when a two-click GUI would do, this is your shopping list. Mildly redundant with the desktop defaults, but the oddities are where the value is — v2's versioning and Jollpi's minimap are genuinely worth a look.

**Projects:**

- **[Notepad Next](https://github.com/dail8859/NotepadNext)** — A cross-platform, reimplementation of Notepad++.
- **[Pulsar](https://github.com/pulsar-edit/pulsar)** — A Community-led Hyper-Hackable Text Editor.
- **[Lite XL](https://github.com/lite-xl/lite-xl)** — A lightweight text editor written in Lua.
- **[Kate](https://kate-editor.org)** — Kate - Get an Edge in Editing.
- **[GNOME Text Editor](https://apps.gnome.org/TextEditor/)** — Text Editor – Apps for GNOME.
- **[CudaText](https://github.com/Alexey-T/CudaText)** — Cross-platform text editor, written in Free Pascal.
- **[Pluma](https://github.com/mate-desktop/pluma)** — A powerful text editor for MATE.
- **[Mousepad](https://gitlab.xfce.org/apps/mousepad)** — Mousepad project page
- **[FeatherPad](https://github.com/tsujan/FeatherPad)** — Lightweight Qt Plain-Text Editor for Linux.
- **[Nota](https://mauikit.org)** — Maui Project – Free and Open Source UI Framework.
- **[CorePad](https://gitlab.com/cubocore/coreapps/corepad)** — CuboCore / CoreApps / corepad · GitLab.
- **[xed](https://github.com/linuxmint/xed)** — X-Apps [Text] Editor (Cross-DE, backward-compatible, GTK3, traditional UI).
- **[gedit](https://gedit-text-editor.org/)** — Gedit, an easy-to-learn text editor | gedit text editor.
- **[Jottr](https://github.com/mfat/jottr)** — Jottr is a cross-platform plain text editor focused on usability and speed.
- **[typobuster](https://github.com/nwg-piotr/typobuster)** — Lightweight editor with text transformations and auto-correction.
- **[Jollpi](https://github.com/zulfian1732/jollpi-text-editor)** — Lightweight GTK 4 text editor with syntax highlighting
- **[Howl](https://howl.io)** — Howl :: Editor.
- **[Parchment](https://codeberg.org/vtrlx/parchment)** — Vtrlx/parchment: Write and edit plain text. - Codeberg.org.
- **[Janus](https://github.com/gholmann16/janus)** — Simple text editor.
- **[Webkit Word](https://github.com/fastrizwaan/webkitword)** — Webkit based word processor.
- **[Mini Text](https://github.com/Nokse22/mini-text)** — A very small and basic text editor.

## 22. KemmOS - openSUSE Linux distribution with GNOME — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/04/Linux-Distributions.png)

**Source:** https://www.linuxlinks.com/kemmos-opensuse-linux-distribution/
**Karakeep doc:** `myib1163heborrf1bakb8qwh`
**Project:** [KemmOS](https://nawre-tech.log.bzh/kemmos) — An openSUSE Tumbleweed-based Linux distribution pairing hardened security defaults with a customised GNOME desktop.

KemmOS is a Linux distribution built on openSUSE Tumbleweed — the rolling-release branch — with a clear thesis: strong security defaults plus a desktop that doesn't make you feel like you're running a server. It ships GNOME 50 (the latest major version) and leans hard on hardening out of the box. Full-disk encryption, SELinux in enforcing mode, Secure Boot support, and system rollback via Tumbleweed's snapshot mechanism are all on by default rather than left as an exercise for the admin. That "enforcing SELinux on a desktop" combination is unusual — most desktop distros either disable it or leave it permissive because it breaks things — so KemmOS is staking its identity on being the security-first desktop that still works. The desktop is a customised GNOME with fifteen bundled wallpapers, alternative icon themes and a graphical tool for tweaking the appearance, so it's not just stock GNOME with a wallpaper pack. LibreWolf is the default browser — the hardened Firefox fork, which fits the privacy theme — and a set of productivity apps plus Flatpaks come preinstalled. It also has its own system management centre showing hardware, drivers, security settings and updates, and a custom updater that handles software, firmware and general maintenance in one place, a nice consolidation that openSUSE normally spreads across YaST and zypper commands. Installation runs through a customised Calamares installer with optional software groups for gaming, networking and virtualisation. Under the hood: systemd, Zypper package management, rolling release, x86_64 only, single developer (Nawrerwan), active. Verdict: a niche pick, but if you want openSUSE Tumbleweed's rolling edge and its famously solid snapper rollbacks *without* hand-rolling the security hardening yourself, KemmOS is the pre-built bundle — though single-maintainer distros always carry the bus-factor caveat, so keep backups regardless of how good the encryption is.

## 23. Walldo - lightweight graphical wallpaper changer — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2022/06/edinburgh-city-view-panorama-night-uk.jpg)

**Source:** https://www.linuxlinks.com/walldo-lightweight-graphical-wallpaper-changer/
**Karakeep doc:** `gxc7sdp8sqp3h703vrnzwlqc`
**Project:** [Walldo](https://github.com/Elias-Gill/Walldo) — A simple wallpaper changer written in Go that browses a local image collection and sets one as your desktop background.

Walldo is a wallpaper changer defined almost entirely by what it refuses to do, and that's the pitch. Most desktop-customisation apps pile on features — background daemons, auto-rotating slideshows, video and live wallpapers, online wallpaper services, the works. Walldo has none of it. No background daemon, no automatic rotation, no video playback, no online service, no live wallpaper. It opens when you need it, you find an image, you set it as the wallpaper, you close it. That's the whole program. It scans wallpaper directories *recursively*, which is the practical win — if you've got years of screenshots and photos spread across nested folders, it'll find them all instead of making you flatten your collection. There's also a fuzzy search that narrows a large library without needing exact filenames, so you can type a couple of letters of what you half-remember and get there. It uses a native graphical interface rather than embedding a browser engine like Electron, so the binary stays small and there's no leftover service chewing RAM in the background — a real contrast to the web-tech bloat in this category. Desktop-environment support is genuinely broad: GNOME, KDE Plasma, Xfce, Cinnamon, LXDE, LXQt, MATE and Deepin are handled directly with no extra wallpaper utility needed. Standalone X11 window managers fall back to feh, and Wayland compositors use swaybg, which covers the awkward corners most changers ignore. Only JPEG and PNG are supported — no WebP or AVIF — and the emphasis is strictly static wallpapers. Written in Go, MIT-licensed, twenty-one stars, single dev (Elias Gill). Verdict: exactly the right tool if you want to set a wallpaper and get out; wrong tool if you wanted a slideshow daemon, which it explicitly isn't.

## 24. Zuban - fast Python type checker and language server — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/Linter-Tool-Banner1.png)

**Source:** https://www.linuxlinks.com/zuban-fast-python-type-checker-language-server/
**Karakeep doc:** `z97urhreoll40juk9cznrrw3`
**Project:** [Zuban](https://github.com/zubanls/zuban) — high-performance Python type checker and language server implemented in Rust.

Zuban is a Python static type checker and language server written in Rust, from David Halter — the author of Jedi, the autocompletion library half the Python editor ecosystem leans on. The pitch is speed without forcing you to abandon your existing type-checking setup, which is the boring, practical reason people actually migrate tools.

The numbers are the story: the project claims Zuban is 20–200× faster than Mypy while using roughly half the memory and CPU compared to Ty and Pyrefly — its two main Rust-based rivals. That's a big gap, and it's the same story as Ruff versus the old Python linters, now applied to type checking.

Where it gets smart is the two modes. There's a Pyright-like mode as the default, and a separate Mypy-compatible mode that behaves just like Mypy — same config files, same command-line flags, same diagnostic messages. So you can point it at an existing mypy.ini, run `zuban mypy` (or the `zmypy` alias), and get drop-in behavior instead of rewriting your CI. It passes over 95% of Mypy's relevant test suite and covers generics, type narrowing, and structural typing.

The language server side implements LSP: diagnostics, completions, goto, references, rename, hover, document highlights, plus incremental analysis so big codebases don't re-check from scratch on every keystroke. Install with `pip install zuban` (activate your venv first so it picks up deps).

Caveat: it's AGPL-3.0, with a commercial license for orgs that won't touch the copyleft — so this is a paid escape hatch for companies, not a freebie for everyone. At ~1.2k stars it's still young, but "Rust rewrite, faster, drop-in compatible" is a formula that has eaten the Python tooling world before. 🦀

## 25. Linux Will Never Succeed on the Desktop Until It Stops Expecting Users to Be Experts — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/10/Puzzled-person-linux.png)

**Source:** https://www.linuxlinks.com/linux-desktop-stop-expecting-users-to-be-experts/
**Karakeep doc:** `l20at99988rhihnf424pugcl`

Another day, another "the users are broken, not the software" debate — except this guest column, published under LinuxLinks' guest-blog slot, argues the opposite. The hook is the odd gatekeeping test some enthusiasts run: can you repair a broken package, parse a terminal error, name your graphics session? Fail, and Linux apparently isn't for you. Which, the author notes, is a frankly daft way to promote an operating system.

Most people don't want a relationship with their computer. Nobody brags that their washing machine only works if you can read diagnostic codes and edit a config file — yet the moment a newcomer hits trouble, three terminal commands land in their lap with an air of "there you go, job done." The kicker is that Linux is often easy: a graphical software centre beats hunting Windows installers and clicking through a dozen prompts, updates happen centrally, and KDE Plasma and GNOME have put years into polish. GNOME's own design principles explicitly aim to reduce user effort and avoid demanding specialist knowledge.

Then something breaks. Suddenly you're juggling three packaging formats, a distro-specific command, a kernel parameter and a mystery file somewhere under `/etc` or `.config`. The author admits he uses Linux daily and still gets snagged — most recently losing far too long to blurry screenshots from fractional scaling on his 4K monitor. He's careful not to argue for ditching the terminal, calling it a genuine strength. His complaint is that command-line workarounds have quietly become a substitute for fixing rough GUI edges, and that "just learn the command line" is passing the buck. He also torches the old "wrong expectations from Windows" excuse: being different doesn't license an awkward interface or ropey docs. Verdict: correct, unoriginal, and the comment thread — elitists on one side, a trucker who compiles his own kernels on the other — proves his point either way. There's a poll: how much terminal knowledge should an ordinary desktop user need?

## 26. XXRI OS Lite - Lightweight Linux Distribution for Older Computers — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/04/Linux-Distributions.png)

**Source:** https://www.linuxlinks.com/xxri-os-lite-lightweight-linux-distribution/
**Karakeep doc:** `wlgweczz2v04ydmiy25nt2p9`
**Project:** [XXRI OS](https://xxri.flows.best) — an independent Linux derivative (Lite edition) built to give older, low-spec 32-bit hardware a modern desktop.

XXRI OS Lite is a lightweight distro derived from Tiny Core Linux, built to drag old computers into a modern desktop without asking for real hardware. It targets 32-bit x86 (i686) boxes and quotes a minimum memory requirement of just 256 MB, which is genuinely ancient-hardware territory. Instead of the bare Tiny Core shell, it ships its own "XXRI Desktop": a dock, an application launcher, translucent UI bits and custom window management. Native apps cover file management, software install and system config, so a non-technical owner can avoid the terminal entirely — the whole pitch is accessibility for people who never wanted to learn Linux.

The stack: BusyBox init, a fixed release model, and the "XXRI Store" as package management, handling AppImage binaries and Tiny Core extensions. Developer Jantzen puts the working state as active. Per the project site, version 2.5 is the current Lite build; two sibling editions — XXRI OS Regular for everyday use and XXRI OS Pro for power users — are still in development with no release and no screenshots yet, so Lite is the only thing you can actually install today.

Context: it lands in the crowded "revive your old PC" niche alongside the usual Puppy/antiX/Damn Small Linux suspects, differentiated mostly by that custom desktop and the store. Caveats: 256 MB is the floor, not the comfort zone; a fixed release model means no rolling updates; and two of the three advertised editions don't exist. LinuxLinks files it in its Big List of Active Linux Distributions. Verdict: worth a look if you've got a 2000s-era 32-bit brick and a spare afternoon — just don't expect the Pro edition it keeps teasing. 🐧

## 27. NumNum - text editor that understands calculations — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/01/039-calculator.png)

**Source:** https://www.linuxlinks.com/numnum-text-editor-understands-calculations/
**Karakeep doc:** `iq96idmi3abgkvf2elznny2f`
**Project:** [NumNum](https://github.com/rudrabhoj/numnum) — blazingly fast GPU-rendered open source alternative to Numi: a notebook calculator that understands maths in plain English, built in Rust with GPUI.

NumNum throws out the calculator grid and gives you a text editor that does math in place, with results shown alongside each expression. The killer feature is that expressions span multiple lines and variables defined on one line can be referenced later — change a variable and everything downstream recalculates, so it's built for working through a whole cluster of related figures rather than punching isolated numbers.

It handles arithmetic, parentheses and math functions, plus percentages, currencies and physical units. You can add a percentage to a value, convert money, or combine compatible units; it ships support for more than 100 units and more than 170 currencies, with exchange rates pulled online and cached for offline reuse. Numbers come in hex, binary and scientific notation. There are functions for common operations and aggregation facilities for sums and averages — so you can total a column of your own scratch figures.

It's a real editor, not a glorified expression box: syntax highlighting, autocomplete, undo/redo, text selection, line wrapping and configurable fonts. Calculations split into named sessions and those sessions auto-save, so your work survives a restart. Themes, fonts and appearance are all configurable.

Per the repo it's authored by Rudrabhoj Bhati in Rust using GPUI (Zed's GPU-accelerated UI toolkit), GPL-2.0, and — at time of writing — a modest 29 stars, so it's early and niche rather than battle-hardened. Context: it's competing with the heavyweight desktop calculators LinuxLinks lists alongside it — Qalculate!, SpeedCrunch, KCalc, Genius — which are more powerful but don't give you the editable, visible working. Caveat: 170 currencies with online rates means your conversion is only as fresh as the last cache. Verdict: genuinely nice for engineering or budget scratch-padding where you want the reasoning kept visible. 🧮

## 28. 6 Useful Free and Open Source Code Formatters for Go — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/Code-Formatter-banner2.png)

**Source:** https://www.linuxlinks.com/useful-free-open-source-code-formatters-go/
**Karakeep doc:** `ih5uikyek529ah3s6evz8tt2`

LinuxLinks runs its usual format: take one mundane category, collect the decent FOSS options, rank them in a ratings chart nobody can read, done. This time it's Go code formatters — tools that reindent, rewrap and reshuffle your source without touching what it does. The pitch is honest enough: you hand over control of hand-formatting in exchange for speed, determinism, and never again arguing about whitespace in a PR review. Only free and open source qualifies, so no JetBrains-style paid tooling sneaks in.

Six tools make the cut. **gofmt** is the baseline — Go ships it, it applies the canonical indentation, spacing and layout, and everything else here is basically a correction to it. **goimports** bolts import management on top: it adds missing imports and strips unused ones so you stop hand-editing that block. **gofumpt** is the stricter fork that enforces additional styling rules gofmt deliberately leaves alone — the "cleaner, more consistent" crowd. **goimports-reviser** goes further on imports, sorting and grouping them into standard, third-party and project buckets. **golines** deals with Go's tendency toward long single-line calls by breaking them into readable shorter lines. **gocondense** does the opposite of golines — it collapses multiline constructs to cut useless vertical space.

The verdict: none of this is exciting, and that's fine — formatters are exactly the boring infrastructure you want boring. gofmt + goimports is the floor most teams should be at, gofumpt if your team likes pain, golines/gocondense if you care about line length. The ratings chart adds nothing; the tool list is the whole value. 😴

**Projects:**

- **[goimports-reviser](https://github.com/incu6us/goimports-reviser)** — Right imports sorting & code formatting tool (goimports alternative).
- **[gofumpt](https://github.com/mvdan/gofumpt)** — A stricter gofmt.
- **[gofmt](https://pkg.go.dev/cmd/gofmt)** — Gofmt command - cmd/gofmt - Go Packages.
- **[golines](https://github.com/segmentio/golines)** — A golang formatter that fixes long lines.
- **[goimports](https://github.com/golang/tools)** — [mirror] Go Tools.
- **[gocondense](https://github.com/abemedia/gocondense)** — A golang formatter that condenses code.

## 29. Machine Learning in Linux: Local AI Studio – local AI toolkit — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2023/02/machine-learning.png)

**Source:** https://www.linuxlinks.com/machine-learning-linux-local-ai-studio/
**Karakeep doc:** `fztutyt2lp501wtoof51mfaq`
**Project:** [Portable-Local-Studio](https://github.com/techjarves/Portable-Local-Studio) — Portable local AI studio for Windows, Linux, and macOS; zero-setup GUI for image generation, GGUF LLMs, TTS & STT (MIT, ~1.5k stars, JavaScript).

Local AI Studio is LinuxLinks' latest pick in the "Machine Learning in Linux" series, and the angle is convenience over depth. The local-ML pitch is standard — prompts and data stay on your machine, zero API charges, no dependence on a remote service staying up — but the usual pain is setting up separate stacks for image generation, LLMs, speech-to-text and TTS. This project wraps all four in one browser-based interface with minimal configuration. Naming is a mess: it's branded Portable AI Studio in the docs, still says Local AI Studio in the UI, and was previously Uncensored Local Studio.

Under the hood it's a common front end over established engines: image generation via stable-diffusion.cpp, GGUF text chat via llama.cpp, speech recognition via whisper.cpp, and TTS via the compact Kokoro-82M model through kokoro-js. No external API keys or accounts, everything runs locally. Installation isn't a package: you clone the repo, chmod +x linux.sh, and run it; first launch downloads the portable runtime and sets up inference backends (CUDA/Vulkan for NVIDIA, ROCm/Vulkan for AMD, Vulkan for Intel, experimental OpenVINO for Intel Core Ultra NPUs, CPU as fallback). The UI serves locally on port 1420, and prebuilt backends need glibc 2.38+, so older Debian/Ubuntu may need an OS upgrade or locally compiled backends.

Reviewer tested on Kubuntu 26.04 with an RTX 3060 Ti (8GB). The Model Manager is the sensible start — curated models plus Hugging Face URL imports. A 2.1GB SD1.5 checkpoint (DreamShaper 8) at 512×512/20 steps rendered in ~5 seconds; the two 6.6GB SDXL models overflowed the 8GB VRAM and only ran with painful CPU fallback. LLMs: Mistral 7B hit ~65 tokens/sec at a suitable quantisation. Whisper handles speech, Kokoro TTS handles voices. Notable caveat — image and text workspaces use separate backends, so GPU acceleration working for Stable Diffusion doesn't prove llama.cpp is on the GPU.

The limits are real: no LoRA or ControlNet support, no Flux/HiDream/Hunyuan/Wan/Qwen-Image workflows, and the image generator is far weaker than ComfyUI or Easy Diffusion. Verdict: a clean onboarding ramp for exploring four branches of local AI without maintaining four Python environments. If you only want one of the four, a specialist tool is better. 🧰

## 30. wpaperd - modern wallpaper daemon for Wayland — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2021/12/wallpaper-setter.jpg)

**Source:** https://www.linuxlinks.com/wpaperd-modern-wallpaper-daemon-wayland/
**Karakeep doc:** `awsnl7czy1ijgzfxu8r2uexe`
**Project:** [wpaperd](https://github.com/danyspin97/wpaperd) — Modern wallpaper daemon for Wayland, written in Rust under GPL-3.0.

wpaperd is a wallpaper daemon for Wayland that does the one thing desktop setups keep getting wrong: it changes your background on a schedule, per display, with hardware-accelerated transitions that don't eat your CPU. Point it at a fixed image or a directory, tell it how often to cycle, and pick ascending, descending or random order. Different wallpapers can be assigned to individual outputs, or displays can be grouped so several share the same image under random selection; regex-based output matching handles messier multi-monitor rigs. It's configured via a TOML file and driven by the bundled `wpaperctl` CLI — next/previous, pause/resume/toggle-pause, or set a specific image to one monitor (`wpaperctl set /path/to/image.png DP-1`). Config reloads hot while the daemon runs.

Under the hood it renders through OpenGL ES and supports configurable transition timing plus fit, centre, stretch and tile placement modes — the docs ship a long list of gl-transitions ports (linear-blur, pixelize, water-drop, swirl and friends) each with tunable params. The project is Rust, MIT-flavoured dependencies aside, licensed GPL-3.0, maintained by Danilo Spinella, around 615 stars and 474 commits.

Two caveats you actually need to read: it uses the `wlr_layer_shell` protocol, so it works on wlroots compositors (sway, and KDE) but **will not work on GNOME** — and the README explicitly states **Hyprland is not supported**, because Hyprland's behaviour breaks it in ways the maintainer won't chase. If you're on sway and want more than `swaybg`'s static image, this is the upgrade; if you're on Hyprland, look elsewhere. 🖼️

## 31. Timekpr-nExT - control computer usage — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2017/09/website-hosting-concept-with-circuits.jpg)

**Source:** https://www.linuxlinks.com/timekpr-next-control-computer-usage/
**Karakeep doc:** `ojmb0pbt1f4m9neptdbqq99r`
**Project:** [Timekpr-nExT](https://github.com/polesapart/timekpr-next) — screen-time management app that limits how long each Linux account can use the machine.

LinuxLinks spotlights Timekpr-nExT, a screen-time manager that enforces hard limits on how long individual accounts can stay logged in. It's not a polite timer that nags you — it forcibly terminates sessions, locks them, suspends, or shuts down the box once a user's allowance runs out. The architecture splits into a background service plus separate client and administration interfaces, so a parent or supervisor configures restrictions while the victim just sees a countdown widget. 🕒

The granularity is the point. You can set different allowances for each day of the week, define permitted usage windows and "unaccounted freeride" periods, and stack weekly or monthly caps on top of the daily ones. PlayTime goes further and meters individual applications and games rather than the whole session — handy when you don't want to ban the PC, just Minecraft. Lockout behaviour is configurable: terminate, lock, suspend, or full shutdown when time expires.

The fairness angle is real. Time accounting deliberately excludes inactive and locked sessions and anything while the system is asleep, so a machine left idle doesn't burn the kid's allowance. The client surfaces remaining time and configurable warnings before restrictions kick in, and a supervisor can hand out a temporary top-up without rewriting the normal schedule. It's written in Python, GPLv3, developed by Eduards Bezverhijs, and the project page notes it's aimed at parents and supervisors optimising time for "subordinates, children, or even yourself."

Caveat: it's a deliberately restrictive tool, and the README warns you to know what each option does before enforcing it on a user, since combinations produce very tailored (read: surprising) behaviour. The repo sits at ~59 stars and is actively updated. Verdict: a solid self-hosted answer to Google's Family Link or a router's parental controls, except it actually understands what a "session" is. Linux-native, no cloud, no account — exactly the kind of tool Wojtek would wire into a homelab.

## 32. 9 Best Free and Open Source Linux MPRIS Tools — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2023/08/music-text-banner-flyer-poster.jpg)

**Source:** https://www.linuxlinks.com/best-free-open-source-linux-mpris-tools/
**Karakeep doc:** `feg974n5awc0nssmvvdtsj5d`

LinuxLinks rounds up nine small, independent MPRIS utilities — and the framing matters. MPRIS is the Media Player Remote Interfacing Specification, a D-Bus interface that gives apps one standard way to talk to and control any media player, instead of every player exposing its own bespoke API. If your keyboard's play/pause key works regardless of whether you're in Spotify, mpv, or VLC, that's MPRIS doing the work underneath. 🎵

The spec isn't just transport buttons. It lets a consumer read the current track's title, artist, album, artwork, and playback position, and — depending on the player's implementation — adjust volume, seek within a track, and watch playback status. That's why status bars, desktop widgets, lock-screen media controls, and automation scripts all lean on it. The roundup deliberately excludes full media players and whole desktop environments; the focus is the lightweight glue layer.

The nine names it actually lists: playerctl (the well-known command-line controller), mpris-ctl (minimalist CLI), mpv-mpris (an mpv plugin so standard media keys work), mpd-mpris (MPRIS for MPD), mprisence (bridges MPRIS-compatible players — typically for Discord Rich Presence), empress (simple MPRIS media controls), mpris-scrobbler (a minimal daemon for Last.fm-style scrobbling), MPRIS MiniPlayer (shows whatever a compatible player is playing), and mpdris2-rs (exposes MPD playback through MPRIS2, the Rust rewrite).

Caveats: the title says "9", and that's exactly what the body lists, but there's no ratings verdict per tool here — just a chart image and one-liners — so the roundup's value is discovery, not depth. Some entries overlap heavily: mpd-mpris and mpdris2-rs both bridge MPD to MPRIS, and if you're on a modern desktop using playerctl for scrobbling you may already have what you need.

Verdict: this is a reference list, not a review. Useful if you're wiring a Wayland status bar, a scripted "now playing" ticker, or scrobbling from a player that forgot to implement MPRIS itself. Grab playerctl and you're basically done. 🎧

**Projects:**

- **[playerctl](https://github.com/altdesktop/playerctl)** — 🎧 mpris media player command-line controller for vlc, mpv, RhythmBox, web browsers, cmus, mpd, spotify and others.
- **[mpris-ctl](https://github.com/mariusor/mpris-ctl)** — Basic mpris player control for linux command line.
- **[mpv-mpris](https://github.com/hoyon/mpv-mpris)** — MPRIS plugin for mpv.
- **[mpd-mpris](https://github.com/natsukagami/mpd-mpris)** — An implementation of the MPRIS protocol for MPD.
- **[mprisence](https://github.com/lazykern/mprisence)** — A Discord Rich Presence for MPRIS media players and web players.
- **[empress](https://github.com/ray-kast/empress)** — A D-Bus MPRIS daemon for controlling media players.
- **[mpris-scrobbler](https://github.com/mariusor/mpris-scrobbler)** — A minimalistic user daemon to submit the songs you're playing to audioscrobbler services like listenbrainz.org, libre.fm and last.fm.
- **[MPRIS MiniPlayer](https://git.dummkopf.live/InventorX/mpris-miniplayer)** — InventorX/mpris-miniplayer - Git hosting needs a hero.
- **[mpdris2-rs](https://github.com/szclsya/mpdris2-rs)** — Expose MPD playback through MPRIS2

## 33. edb - graphical debugger inspired by OllyDbg — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/05/7060468-devops.jpg)

**Source:** https://www.linuxlinks.com/edb-graphical-debugger/
**Karakeep doc:** `qe281a1psqr501zcmxcxkby5`
**Project:** [edb](https://github.com/eteran/edb-debugger) — graphical low-level debugger for AArch32/x86/x86-64, styled after OllyDbg.

LinuxLinks profiles edb, a graphical debugger for AArch32, x86, and x86-64 applications. The pitch is simple and unapologetically retro: it's inspired by OllyDbg and gives you a traditional low-level debugging environment built around disassembly, registers, memory, and process state, rather than a modern source-level IDE frontend. If you've ever wanted OllyDbg's muscle memory on Linux, this is the closest thing. 🔧

The interface is oriented at machine code. You get disassembled instructions, register inspection, stack contents, and memory inspection and editing while you control execution with software and hardware breakpoints plus single stepping. It's genuinely dual-use: conventional debugging when source is available, and reverse engineering when it isn't — the disassembly-centric layout is exactly what you want to examine a stripped binary, and the register/memory views let you watch program state change as you step.

Under the hood, edb uses Capstone for disassembly and Qt for the GUI. It's built around a plugin architecture, so extra debugging and analysis functionality can be bolted on without bloating the core, and optional Graphviz integration is available where a control-flow or call graph helps. You can build it with either GCC or Clang, and current development tracks modern Qt — both Qt 5 and Qt 6 — with recent work focused on compatibility fixes for newer Qt and Capstone releases. It's C++, GPLv2, by Evan Teran.

Context: edb has been in development for many years and carved out a real niche, sitting alongside GDB, LLDB, Radare2, Ghidra, and iaito as one of the more established free GUI debuggers on Linux. The repo itself is healthy — around 2,973 stars, actively pushed, tagged with capstone, ollydbg, qt5/qt6, and reverse-engineering. Caveat: this is a LinuxLinks blurb, so there's no hands-on benchmark or comparison against GDB's TUI here; whether edb beats Radare2's iaito for your reversing workflow is a taste call.

Verdict: if you do binary analysis, CTF work, or malware triage on Linux and miss a proper graphical disassembly view, edb is worth a look — mature, still maintained, and honest about being a low-level tool rather than a source-level IDE. 🐛

## 34. 15 Best Free and Open Source Go Linter Tools — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/05/921-coding.jpg)

**Source:** https://www.linuxlinks.com/best-free-open-source-go-linter-tools/
**Karakeep doc:** `ft6a3o3vbf4td1emkf42h73u`

LinuxLinks reruns its sweep of Go linters — the tools that read your source without executing it, hunt for bugs, style crimes and coding-standard violations before they hit production. The pitch is early detection: catch the crap in the dev loop and your code quality and maintainability go up instead of sideways. Then the honesty kicks in. The intro flat-out admits a linter "is not necessarily a quick fix, can be a distraction," and that it may be useless on old, large codebases where the noise buries the signal. Rare for a listicle to warn you off its own subject. 🧹

Fifteen tools make the cut, ranked in the usual LinuxLinks ratings chart, and only free and open source software is eligible. The headliners: revive, sold as a drop-in replacement for the dead golint; golangci-lint, the fast runner that chains a dozen linters behind one config; gosec for security scanning; Staticcheck for deeper analysis; and go-critic for the opinionated crowd. Then Vet for suspicious constructs, gofmt and its stricter sibling gofumpt for formatting, goconst for repeated literals you should have made constants, go-ruleguard for dynamically loaded rules, sloglint for consistent log/slog style, forbidigo for banning identifiers, godot for comment consistency, Godoc-Lint for doc comments that don't suck, and exhaustive for catching missing enum cases in switch statements.

The piece was refreshed under the site's recent announcement, so the ratings are current. Verdict: solid bookmark, not gospel. Linters are a stack, not a single pick — golangci-lint gluing Staticcheck and gosec together is the pragmatic start. Turn it on, eat the warnings, and stop pretending your Go is clean.

**Projects:**

- **[revive](https://github.com/revive-lint/revive)** — 🔥 Fast, strict, configurable, extensible, and beautiful linter for Go.
- **[golangci-lint](https://github.com/golangci/golangci-lint)** — Fast linters runner for Go.
- **[gosec](https://github.com/securego/gosec)** — Go security checker.
- **[Staticcheck](https://github.com/dominikh/go-tools)** — Staticcheck - The advanced Go linter.
- **[go-critic](https://github.com/go-critic/go-critic)** — The most opinionated Go source code linter for code audit.
- **[Vet](https://pkg.go.dev/cmd/vet)** — Vet command - cmd/vet - Go Packages.
- **[gofumpt](https://github.com/mvdan/gofumpt)** — A stricter gofmt.
- **[gofmt](https://pkg.go.dev/cmd/gofmt)** — Gofmt command - cmd/gofmt - Go Packages.
- **[goconst](https://github.com/jgautheron/goconst)** — Find in Go repeated strings that could be replaced by a constant.
- **[go-ruleguard](https://github.com/quasilyte/go-ruleguard)** — Define and run pattern-based custom linting rules.
- **[sloglint](https://github.com/go-simpler/sloglint)** — 🪵 Ensure consistent code style when using log/slog.
- **[forbidigo](https://github.com/ashanbrown/forbidigo)** — Go linter for forbidding identifiers.
- **[godot](https://github.com/tetafro/godot)** — Linter that checks that comments end in a period.
- **[Godoc-Lint](https://github.com/godoc-lint/godoc-lint)** — A linter for Go documentation practice (aka "Go Doc Comments" or "godoc").
- **[exhaustive](https://github.com/nishanths/exhaustive)** — Check that expression switches and type switches in Go source code are exhaustive.

## 35. terminal-anki - flashcards with spaced repetition in your terminal — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/04/038-online-learning.png)

**Source:** https://www.linuxlinks.com/terminal-anki-flashcards-spaced-repetition/
**Karakeep doc:** `njvf1g2udiblumz7ia9kpbpb`
**Project:** [terminal-anki](https://github.com/dandrok/terminal-anki) — a modern, intelligent terminal-based flashcard application with spaced repetition learning.

terminal-anki is a keyboard-driven flashcard app that does the whole review loop inside a TUI: reveal the answer, grade recall with fixed number keys, move through cards, and bounce back to the surrounding views without ever leaving the terminal. It schedules reviews with the SM-2 algorithm — the old Anki standby — so you're not fighting a shiny new scheduler, just the classic one. 🗂️

The real story here is that it's a full collection manager, not a read-only reviewer. You can browse, search, add, edit and delete cards, spin up custom study sessions filtered by scope, tags, difficulty, card count and order, and undo grades or collection changes when you inevitably fat-finger a key. The statistics side is genuinely overbuilt for a terminal tool: activity heatmap, session history, tag breakdowns, quick stats, streak tracking and configurable daily goals. Themes, session size and card ordering are all tweakable in-app, and a persistent frame keeps navigation and status on screen.

Interop is the killer feature. It imports Anki `.apkg` packages and Anki text exports, preserves existing scheduling data where it can, and exports back out in an Anki-compatible text format. Images render on cards in supported terminals. All study data and config stay local, with atomic writes and recovery handling that quarantines a corrupted collection instead of silently nuking it — which is more respect than most tools give your data. It's MIT-licensed, written in TypeScript, and ships via npm.

Verdict: niche but well-made. If you live in the terminal and want Anki's SM-2 brain without Anki's Qt elephant, this is the one. One star on GitHub though, so you're an early adopter, not a crowd-follower. ⭐

## 36. Calculator - simple calculator for the COSMIC desktop — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/01/037-calculator.png)

**Source:** https://www.linuxlinks.com/calculator-simple-cosmic-desktop/
**Karakeep doc:** `vo7h2olr9a6pcy3v34d13g3d`
**Project:** [Calculator](https://github.com/cosmic-utils/calculator) — Calculator for the COSMIC desktop.

Calculator is a graphical calculator built specifically for COSMIC, System76's Rust-based desktop environment. It does everyday arithmetic and nothing else — no programmable functions, no computer algebra, no scientific-math cosplay. It's built on the COSMIC application toolkit so it behaves and looks like a native system utility instead of a bolted-on GTK app wearing the wrong theme. 🔢

The one feature worth mentioning is calculation history. Previous results stick around so you can inspect them instead of re-running the same sum, and you can pull an old calculation back into the main display to reuse or edit it. The interface keeps numbers, operators and the result front and center. That's the whole pitch.

And it's honest about the whole pitch. LinuxLinks is explicit that this is not competing with Qalculate, Genius or SpeedCrunch — it exists because 90% of desktop calculator use is "quick, give me a number" and you don't need a scientific package for that. Written in Rust by Eduardo Flores, GPL-3.0 licensed, hosted under the cosmic-utils org. It's a young project — 53 stars, 24 forks, 14 open issues — so expect rough edges.

Verdict: if you're on COSMIC, this is the obvious pick because it's the only one that's actually native to your DE. If you're not on COSMIC, you have no reason to care — go grab Qalculate. 🧮

## 37. RAWmakase - fast non-destructive RAW photo developer — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/09/couple-taking-photos-light-movie-projector.jpg)

**Source:** https://www.linuxlinks.com/rawmakase-fast-non-destructive-raw-photo-developer/
**Karakeep doc:** `wvbvfjavtlpx9bxphuddhmtc`
**Project:** [RAWmakase](https://github.com/pch/rawmakase) — free, fast, Lightroom-compatible RAW photo editor for Linux, macOS, and Windows.

RAWmakase is a fast, non-destructive RAW developer that opens images from a huge range of cameras via LibRaw and exports finished shots as JPEG or 16-bit TIFF. Non-destructive means your edits live in an SQLite catalogue while the original raw files stay untouched — edit, revert, re-edit, no regrets and no duplicate files littering your drive. 📷

The development controls are deliberately Lightroom-shaped: exposure, shadows and highlights, clarity, dehaze, point curves, levels, HSL colour mixing and three-way colour grading. Detail work covers denoising and sharpening plus crop, straighten, perspective correction and lens corrections. Colour and tone processing is GPU-accelerated — Vulkan on Linux — with a CPU fallback for the unlucky. There are presets, camera profiles, masking and spot-removal tools, and a command-line interface for inspection, rendering and catalogue operations when you want to script instead of click.

The headline feature is migration: it imports a Lightroom Classic catalogue complete with ratings, flags, colour labels, keywords and compatible development settings, without touching the source catalogue or your originals. It also reads Lightroom XMP presets and imported DCP/XMP camera profiles alongside its own. Local editing (Heal and Clone spot removal, brush, gradient and range masks) is still experimental, so temper expectations there.

Verdict: an MIT-licensed, Rust-built Lightroom escape hatch on Linux, macOS and Windows — 264 stars in under two weeks, so people are clearly desperate to leave Adobe. Darktable and RawTherapee are the mature incumbents, but if you want your Lightroom edits to survive the move, this is the one that actually promises it. 🔓

## 38. pSync - synchronize files securely between networked hosts — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/04/Transfer_Files41021-c1.png)

**Source:** https://www.linuxlinks.com/psync-synchronize-files-securely-networked-hosts/
**Karakeep doc:** `gi61t2nf36bc15h00707o3xm`
**Project:** [pSync](https://github.com/kobayasy/pSync) — SSH-based, manual-trigger file synchronization between networked hosts

pSync is a command-line file synchronization system for keeping chosen directories aligned between networked hosts, and its whole personality is the *deliberately manual* approach — nothing runs in the background waiting to fire. You synchronize when you ask it to. That's a feature, not a limitation: if you've ever had a watcher grab a file mid-edit and ship a half-written version across the network, you already understand why that matters. Directories get associated with labels, so the paths don't have to match on both ends; you can configure several sync directories, and map different sets of them to different remote hosts.

The same binary runs on both ends, so it handles direct local-to-local sync as well as remote or cloud workflows. It communicates over SSH and supports both public-key and password auth, encrypting and compressing the payload. There's no dedicated pSync server process to babysit, and it doesn't need admin rights to install. Before it changes anything it stashes the previous state of updated or deleted files as temporary backups, and it does the whole operation atomically — if it gets interrupted, you're left with the pre-sync state, not a half-mangled tree. It handles regular files, symlinks and directories, and preserves permissions, creation and modification times. One quirk worth flagging: it treats hard links as individual files rather than preserving the link structure — so if that's central to your workflow, look elsewhere.

It's written in C, MIT-licensed by Yuichi Kobayashi, with few external dependencies and low memory use, and it supports cross-compilation. Optional progress display if your terminal libs are there. At ~10 stars it's very much a solo project, not battle-tested at scale. Context: it sits alongside rsync, Syncthing and Unison — pSync's angle is manual + SSH-only + atomic + no daemon. Verdict: niche but honest; if you want rsync-ish semantics without a watcher and without root, it's worth a look. 🔁

### RSS — Other

## 39. How Oracle turns days of work into minutes with ChatGPT and Codex — by OpenAI

![OpenAI](https://openai.com/favicon.ico)

**Source:** https://openai.com/index/oracle/
**Karakeep doc:** `lj5l7qwyi7uep5jzlaw0f4gk`

Another OpenAI customer story, another headline promising to turn days into minutes, and — shocker — the body is one stat card and a testimonial under every subhead. The numbers are the real content here: Oracle's own figures say 130K active ChatGPT users and 95K+ active Codex users inside the company, plus a claimed 98% decrease in the time it takes for talent-acquisition research. The recruiting team used ChatGPT Work to build a "talent market intelligence" tool that takes a job description, finds comparable roles, benchmarks compensation and assesses the talent pool by location — work that used to eat 2–4 days now gets prepped in 15–20 minutes, per SVP Jan Ackerman, who also notes the process is now consistent instead of reinvented every search. Oracle Applications Lab built an ontology of the company's objects, relationships and rules so a plain-language business question becomes a reliable SQL query through Codex; one user reportedly got an answer almost instantly to something that used to take a couple of hours, and the numbers matched the old manual process exactly. SREs use Codex to pull incident context and surface the right playbook — "a typical simple incident that used to take an hour to resolve can now be handled in minutes," says VP Richard Lam. Credit where due: the piece keeps the caveats, quoting Lam that none of this runs on autopilot and that you have to own your code or end up with unmaintainable sludge. Verdict: genuinely large-scale deployment, wrapped in the usual press-release gloss — read it for the user counts, not the adjectives. 🍊

## 40. Pollo AI turns creative ideas into campaigns with OpenAI — by OpenAI

![OpenAI](https://openai.com/favicon.ico)

**Source:** https://openai.com/index/pollo-ai/
**Karakeep doc:** `h6ddoochf8v32fmhio4g8lbi`

The second OpenAI customer story of the day, and this one is basically a pitch deck with a logo swap: Pollo AI, a startup that turns creative ideas into finished images and video without production expertise, and the model names are doing a lot of heavy lifting. The stack is GPT‑5.6, GPT‑6 Astra and GPT‑Image‑2.5. Founder and CEO Bill Zhu sets the ambition as "do for video what Canva did for design," and claims more than 26 million users on the platform. The concrete product detail is decent: video templates now start 30% of creator sessions, and the newer Pollo Agent builds storylines, scene flows and scripts from rough input. CTO Peter Zhou says GPT‑5.6 handled ambiguous creative inputs best, and the team runs GPT‑5.6 for routing and GPT‑6 Astra for the harder narrative and scene-revision work to balance reasoning, speed and cost — which they claim cuts time users spend choosing or switching models by more than 50%. Image generation is all GPT‑Image‑2.5: "if we receive any task to generate an image, we always use GPT‑Image‑2.5," Zhou says, praising it on varied characters and letters. The showcase cases are the usual three: a product photo turned into a 15-second fragrance ad with velvet textures and warm spotlights, a jewelry campaign with a model beside a cheetah, and a peach-soda bottle turned into a snowy miniature landscape with a train and lizards. Region is Asia-Pacific, product is the API, and the pitch is that AI video becomes everyday within 12 months. Verdict: real model-mixing discipline buried under marketing copy — take the architecture, leave the cheetah. 🎬

## 41. Introducing the Anthropic Cyber Mission — by Anthropic

![Anthropic](https://www-cdn.anthropic.com/images/4zrzovbb/website/d2af4f6715cbe9766a47430a24420cfca0a2c588-1200x630.jpg)

**Source:** https://www.anthropic.com/news/anthropic-cyber-mission
**Karakeep doc:** `wo7880w9fpovuop1mvk9pz7q`

Anthropic has discovered that "cyber mission" sounds substantially more heroic on a landing page than "we're selling Claude into the security budget," and has helpfully wrapped both in one announcement. The substance: a long-term "Cyber Mission" split into two prongs. First, the Critical Infrastructure Defense Program (CIDP), aimed at the operational technology behind power grids, water, factories and transport — stuff that can't be taken offline to patch, so known vulns linger for years. Founding partners are the full enterprise-bloc roster: Accenture, Booz Allen, CrowdStrike, Deloitte, Dragos, Hitachi, Insane Cyber, Nozomi, Palo Alto, PwC and Rockwell. Second, OSS Scanner: an opt-in, inspired-by-OSS-Fuzz service for open-source maintainers where Anthropic's strongest models periodically scan projects for free and send model-generated reports — proof of concept plus suggested fix — with no human review, so some will carry wrong severity ratings. Anthropic itself expects a true-positive rate above 90%. The honest caveats are the good part: the cost of exploiting vulns has dropped while verifying and fixing is still slow and manual, Glasswing often saw months between find and fix, and OT fixes can wait decades before it's safe to apply them on running machinery. It's also an admission that AI finding bugs faster than humans can triage them is a new bottleneck Anthropic helped create. Verdict: a real commitment with real funding behind the open-source side — just don't mistake the brand name for the substance. 🛡️

## 42. 2026 Usage Policy update — by Anthropic

![Anthropic](https://www-cdn.anthropic.com/images/4zrzovbb/website/6d4a0d28992ade92d6fa63646fd9c9d318245c6c-2400x1260.jpg)

**Source:** https://www.anthropic.com/news/2026-usage-policy-update
**Karakeep doc:** `qfuj6u2dav0ibwrz1e60pzud`

Anthropic's annual ritual of dressing up a vibe-check as considered legal prose is back. The blog frames this as responding to Claude doing "longer, more independent work"; read the changelog and it's mostly relabelling things they already policed and stretching the language to cover what the model can now do unattended. Lots of "clarify," very little "ban."

The one genuinely new bucket is "Do Not Engage in Deceptive Campaigns or Artificial Activity," which gathers the scattered election, fraud, privacy and disinformation rules into a single home. It covers fake-account networks, astroturfing and the infrastructure for running influence ops. The old elections section is renamed "Do Not Undermine Democratic Processes," and — the interesting bit — the blanket ban on personalized vote and campaign targeting is gone, because it was also choking legitimate civic work like nonprofits writing voter info in other languages or officials sending ballot-cure notices.

Weapons prohibitions now explicitly reach guidance and control software, arming drones and autonomous vehicles. Surveillance rules spell out that non-consensual tracking is out, real-time or retroactive; Claude can't decide who to investigate, arrest or charge; and you can't build or improve surveillance tooling. Fraud monitoring, content moderation, journalism and legal research stay permitted. High-risk health and finance uses still need a human in the loop who can override the output, and the affected person must be told AI was involved. New hardware clause: if Claude drives something physical, an operator must be able to watch and stop it, and the kit must fail safe if Claude disconnects. You're also now banned from sustained, needless cruelty toward the model — extreme cases only, Tuesday-afternoon swearing doesn't count. Takes effect November 12. It's a compliance document cosplaying as a manifesto, and it knows it.

## 43. Debunking the Biggest Data Center Myths — by Meta Newsroom

![Meta Newsroom](https://about.fb.com/wp-content/uploads/2026/10/Debunking-the-Biggest-Data-Center-Myths_Header.jpg?w=1200)

**Source:** https://about.fb.com/news/2026/10/debunking-the-biggest-data-center-myths/
**Karakeep doc:** `hv869tc4l06a7fu9csa515fp`

Meta's newsroom has decided the discourse around data centers is unfair and has dispatched software developer–cum–content creator Tom Shaw to set us straight. Three myths get the treatment, and the evidence is refreshingly specific — as far as it goes.

On water: he describes two Meta facility types he's toured. A traditional air-cooled center uses water for only a few months a year to cool incoming air. An AI-optimized closed-loop liquid-cooled center circulates a water-and-glycol mix through a sealed loop, passing cold liquid over the servers, then through a heat-rejection system that cools it and sends it back — so the water isn't consumed as it circulates, it's reused. Sources differ by site: one off the municipal system, one from a permitted on-site well, both metered and counted inside the local water plan rather than carved out of it. The well tapped an aquifer that wasn't drinkable anyway, and in water-stressed regions the closed-loop design is the default. His headline comparison: many Meta facilities use less water annually than an average US golf course. Caveat stated plainly — he only vouches for the two sites he visited.

On energy: Meta pays its own bills and, he argues, funds the new generation and transmission its load requires rather than dumping the cost on neighbours. In Louisiana the Entergy agreement is structured so existing customers aren't left holding the infrastructure spend.

On jobs: construction employs thousands of trades across multi-year builds, and operation needs engineers, technicians, IT and security staff — often making Meta a top local employer. There's also America's Workforce Academy, free skilled-trade training with a guaranteed job at a partner site on completion. It's advocacy with receipts, but the receipts only cover Meta.

## 44. Building on our commitment to American scientific discovery — by Anthropic

![Anthropic](https://www.anthropic.com/api/opengraph-illustration?name=Object%20DoubleHelix&backgroundColor=heather)

**Source:** https://www.anthropic.com/news/genesis-mission-commitment
**Karakeep doc:** `ct7t0sfz0h69x9l1ew7yu4k3`

Anthropic has pledged $150 million over three years to the Genesis Mission, a federal initiative to accelerate scientific discovery through AI. The money buys Claude for more than 15 participating agencies, namechecked as NASA, the National Institutes of Health and the National Science Foundation. The press release frames this as "deepening" a commitment first announced last December with the US Department of Energy; since then Anthropic says it has been plugging Claude into the national labs. 🎻 The announcement drop date is timed to the Science: A New Golden Age Summit at the White House Office of Science and Technology Policy, which is the actual deliverable here — a photo op with the administration's science agenda, quoting its "Science: A New Golden Age" framing back at it.

Strip the deck and here is the changelog. Over three years: Claude, Claude Code and API credits to "several hundred" Genesis Mission research projects; partnership on fusion energy and quantum computing; and — the honest part — training, onboarding and technical support, plus hand-holding for agencies new to the whole thing. No benchmarks, no model version, no per-agency numbers, no definition of "several hundred." It is a credits-and-training package dressed as scientific infrastructure.

Context: this sits on top of Claude Science, an academic research workbench; 10,000 free or discounted Claude seats for academic scientists; the AI for Science credits program; and a research preview of the Model Hardware Standard for agents driving lab instruments. All coherent, all in service of locking in a generation of researchers on Claude. Caveat: $150M over three years is a rounding error next to the labs' real budgets — the value is the logo and the lock-in, not the cash. Verdict: competent, on-brand government-relations theater. If you're a scientist, claim the credits; just don't call it altruism. 🔬

## 45. Disrupting AI-enabled "false front" operations — by OpenAI

![OpenAI](https://openai.com/favicon.ico)

**Source:** https://openai.com/index/disrupting-ai-enabled-false-front-operations/
**Karakeep doc:** `r0d2nu0pazw108qtbuiiooqi`

OpenAI's latest safety report — the genre where a company publishes its own scorecard and, remarkably, grades itself well — covers two banned influence operations, one Russian and one Iranian, both of which used ChatGPT to dress up "false front" entities. 🚨

Russia's "Dark Clark" ran a fake research outfit called the Social Research Center (SRC), supposedly studying the Indian diaspora in Latin America. A stable of operators prompted in Russian (one in Spanish, still located in Russia), VPN-ing around the fact that OpenAI doesn't serve Russia at all, and used the model mostly to write internal reports to an unknown superior, plus campaign content and perf reviews for the think-tank cover. The twist the report leans on: the SRC co-opted actual, unwitting Latin American staff — the operators discussed pay scales, hiring and firing, so they controlled it, not merely partnered with it. Open-source research found 60+ mostly-original articles on the SRC site. They also posed as a fake persona, "Mia Clark," to run the socials and talk to the ground staff. Fakes spread far enough to trigger fact checks and official denials in Ecuador, Peru and Bolivia, and one Peru story even fed Ukraine–Poland tensions.

Iran's "Bogus Bylines" is the other half: seven fake journalist personas — Hoskins, Lamington, Gonzalez, Harrison, Feusier, Williams, Johnson — pitching long-form US-Iran articles to small outlets. OpenAI counted almost 100 published or syndicated pieces across roughly a dozen outlets, the earliest July 2025, the latest October 2026, exploding after the US-Iran conflict kicked off in March 2026. The social-media "mass commenting"? Double-digit likes, replies that were a minority of each thread, many likes from the operation's own accounts.

The scoring is the fun part. On the Brookings Breakout Scale (1–6), Dark Clark landed Category 5 — stated as the first Category 5 OpenAI has disrupted in its reporting — and Bogus Bylines' article arm hit Category 4, while its commenting arm flopped to Category 2. The tell: the highest-reach ops are the ones landing content in real media, not just posting to fake accounts. And OpenAI openly notes the operators inflated their own metrics — the Iranian crew measured impact by view-counting the *original* posts they replied to, not their replies, which is either incompetence or fraud, and the report cheerfully can't decide which. Everything was shared with authorities, of course. Verdict: genuinely useful intel wrapped in self-congratulation — the data is solid, the framing is a victory lap. 🍿

## 46. Bridging technical depth and usability: The story behind Radar’s redesign — by Cloudflare Blog

![Cloudflare Blog](https://blog.cloudflare.com/_emdash/api/media/file/01M4ATYE1DJVAKAH76KY2N8CN1.png)

**Source:** https://blog.cloudflare.com/radar-redesign/
**Karakeep doc:** `t4ptdvtdy7w75r12h808bb15`

Cloudflare redesigned Radar, its real-time view into global Internet trends, and the post is a design-process writeup rather than a feature launch. Radar launched in 2020 and found its natural audience among network operators and academic researchers who actually read the data. The problem: it was intimidating to everyone else — journalists, human-rights advocates, policymakers, everyday users — and Cloudflare wanted it to become a self-serve resource for that wider crowd without gutting the depth the experts rely on.

The old landing page used a bento-box layout where everything carried similar visual weight, vertical cards broke natural reading patterns, and the styling felt disconnected from Cloudflare's brand. User feedback backed that up — one external user said his biggest frustration was that Radar was hard to even show to his students. So the redesign replaced the bento grid with a map as the top-level visual anchor. The Internet mostly ignores national borders, but Cloudflare's bet is that geography is the most familiar way to make scope legible. The top section leads with outages (concrete, timely, salient) and traffic (communicates Radar's breadth), and the map doubles as navigation into country-level and trend views.

Below that, the chart widgets became a tabbed flow that serves summary stats plus a call-to-action to go deeper — a clearer hierarchy that previews what Radar offers instead of dumping it all at once. For design language, Cloudflare split its ecosystem into three pillars — marketing pages, content experiences (blog/docs), and product experiences — and decided Radar sits at the intersection of all three: approachable like marketing, structured like content, maintainable by migrating to Kumo components, the UI kit used in Cloudflare's product system.

The iteration story is candid: early maps were too dense, trying to earn credibility through data-heavy visuals; later ones swung too far toward marketing styling and made live data feel static. The shipped version sits between — reads as live, but still legible. Cloudflare notes it sits in front of roughly 20% of all web traffic, which is the real reason Radar can tell stories nobody else can.

Verdict: a solid, honest design post with no new numbers or features — the interesting bit is the institutional admission that expert-first tools lose the broader audience, and Radar is being deliberately softened. Feedback is actively solicited via @CloudflareRadar. 🗺️

## 47. Jak używać AI do ochrony przed atakami, wykrywania włamań i analizy incydentu? — by NieBezpiecznik.pl

![NieBezpiecznik.pl](https://niebezpiecznik.pl/wp-content/uploads/2026/10/socai-b-600x338.png)

**Source:** https://niebezpiecznik.pl/post/jak-uzywac-ai-do-ochrony-przed-atakami-wykrywania-wlaman-i-analizy-incydentu/
**Karakeep doc:** `rvrhndtpbpae0i7xqjcx7xc7`

This is a promo post, not a technical article — NieBezpiecznik is selling an online training, and the pitch is that attacks on Polish companies (not just healthcare) have ramped up lately, so maybe you should learn to use AI defensively. Their new ~2-hour practical workshop, "Jak używać AI do ochrony przed atakami?", runs online on 14 October (Wednesday) at 19:00, and it's recorded with 30 days of access, so you can sign up even if the date doesn't suit you. The urgency hook: today only, until 23:59, it's 65% off, and the price climbs every day after.

Substance-wise, the course is about using LLMs and agents for defensive work — building out your SOC/SIEM with AI-backed detection and faster incident analysis. The labs are the bulk of it, and the structure is nicely adversarial: whatever you build in lab one gets attacked in lab two, so you see the weak points of AI agents firsthand. A free OpenAI or Anthropic account technically suffices, but they push you to a plan with Codex or Claude Code so the labs go quicker — otherwise you're a "meat proxy" copy-pasting prompts and responses by hand. Grok in Cursor works too, but you adapt the instructions yourself.

The trainer is Michał Garcarz, who carries 30 years in network security, 11 of them at Cisco running managed SOC work and incubating AI/ML solutions — back when nobody had heard of OpenAI. The intended audience is SOC/monitoring staff, pentesters, security analysts, admins, and honestly anyone who wants to mess with AI agents for home incident analysis. There's practical labs plus a Q&A session. Companies sending 5+ people get an extra discount, and they'll provide a proforma/English PDF if you need to bill it to a training budget.

Verdict: it's a sales page, so treat the urgency with the usual skepticism — the daily-price-ladder is a marketing device. But Garcarz's background is real, and "build it in lab 1, break it in lab 2" is a genuinely good way to teach agent security. 🛡️

## 48. SpaceXAI joins as a Founding Corporate Patron with $1.5 million in Grok tokens - Omarchy News — by Omarchy

![Omarchy](https://omarchy.org/brand/social/everforest.png)

**Source:** https://omarchy.org/news/2026/10/spacexai-joins-as-founding-corporate-patron
**Karakeep doc:** `z3u22bd9lpqhgtl9t0kubte2`

SpaceXAI (the xAI shop) is joining the Omacom Foundation as a Founding Corporate Patron, and the donation is notably not cash. It's $1.5 million in Grok tokens — which is either a generous subsidy for the open-source project or a very expensive way of telling the world your inference product has capacity to spare. Omarchy is taking it either way. 🚀

Where the tokens go: Grok 4.7 and later will power the project's automated agents, chief among them Omabot, which reviews the PR flood. And it is a flood — Omarchy is closing in on 7,000 pull requests from more than 550 contributors, and the post's own framing is that reviewing all of them is "not a job for mere humans." So the bots get the bulk, but every Omarchy team can also tap the pool — bug hunting, theme polish, hardware ports, whatever comes next.

The money quote is the arithmetic of the pledge. SpaceXAI joins Meta Superintelligence Labs, DigitalOcean, and Alibaba Cloud as Founding Corporate Patrons, and together the foundation's total backing reaches roughly $23.2 million. For a project that, in the author's own words, "started as a pile of dotfiles," that's a serious war chest for people, infrastructure, and upstream open-source work.

Caveat: tokens are not cash. Their real value depends entirely on Grok pricing staying put and the API staying up — a $1.5M token grant is only worth what the tokens buy, and it chains part of Omarchy's agent infrastructure to one vendor's endpoint. Still, the post leans hard into the romantic angle: "Omarchy, now powered by intelligence from orbit," with a wink at rockets, boosters caught by chopsticks, and eventual orbital data centres.

Verdict: whether you buy the Year-of-Linux-on-the-Desktop theatrics, the substance is real — a small distro-framework pulling in a nine-figure-patron tier of backers and funnelling it into reviewing seven thousand PRs. That's the open-source funding model everyone claims to want, with a Grok-shaped asterisk attached. 🤖

## 49. Meta Donates 1,000 AI Glasses to Singapore's Disability Community — by Meta Newsroom

![Meta Newsroom](https://about.fb.com/wp-content/uploads/2026/10/Meta-Singapore-Wearables-Event.jpg?w=1200)

**Source:** https://about.fb.com/news/2026/10/meta-donates-1000-ai-glasses-to-singapores-disability-community/
**Karakeep doc:** `o0utluuycs8ncthvi4h6bzmb`

Meta announced in Singapore that it's handing 1,000 Ray-Ban Meta AI glasses to four community organisations, plus a US$30,000 grant to the Singapore Association of the Visually Handicapped (SAVH) for accessibility training. The recipients are SAVH, Guide Dogs Singapore, the Singapore Disability Sports Council and Gardens by the Bay. Joel Kaplan, Meta's Chief Global Affairs Officer, made the announcement at an "AI glasses accessibility showcase" co-hosted with the SDSC, with Senior Parliamentary Secretary Eric Chua as Guest-of-Honour. 🙌

The substance, such as it is: for people who are blind or have low vision, the glasses do text reading, object identification and scene description — the standard accessibility pitch. The grant funds a free accessibility curriculum teaching safe, effective everyday use: identifying objects, reading text, voice commands. Meta frames it as "the future is for everyone." Kaplan's quote is the usual "I've seen firsthand how meaningful this technology is." Cheryl Yeo of SAVH calls the support a path toward "inclusion, dignity, and self-reliance," while also noting SAVH's role in "guiding responsible use" — a quiet admission that dumping 1,000 surveillance-capable cameras into a vulnerable community comes with strings. Damon Goh of Guide Dogs Singapore hopes it changes how blind people navigate; Linda Tay of Gardens by the Bay ties it to their sensory tours and a robotic guide dog pilot.

Caveats: this is a press-release, so there's zero independent data on whether the glasses actually help, no follow-up metrics, no word on the data those glasses pipe back to Meta. It's hardware philanthropy with a product-launch aftertaste. Verdict: the donation is real and probably useful for the recipients; the announcement is a marketing asset dressed as charity. 🕶️

## 50. Why Data Centers Are Such a Big Part of Meta's AI Approach — by Meta Newsroom

![Meta Newsroom](https://about.fb.com/wp-content/uploads/2026/10/Tom_Interview_Santosh-on-how-AI-is-shifting-Infra-Strategy_Social-Share.jpg?w=1200)

**Source:** https://about.fb.com/news/2026/10/meta-data-centers-ai-approach/
**Karakeep doc:** `z6t18rc94hu4mpsb230q5vhn`

This is a Meta newsroom post wrapping an interview — developer/creator Tom Shaw sat down with Meta's Head of Infrastructure, Santosh Janardhan — and it reads like a teaser, not an article. The hook is the argument that Meta is "more than just a software company" and that AI is categorically different from prior tech, so owning the data centers is the whole game. The piece frames it as a Q&A and then just lists the questions without answering them: how Meta powers its AI infrastructure, what a gigawatt of energy actually means, how it picks chips for its data centers, why it's so focused on AI right now, and what the benefits of building your own data centers are.

That's it. No gigawatt number, no chip vendor named, no capex figure, no megawatt capacity, no timeline — none of the concrete specifics you'd want are in the body. Context: Meta has been loudly betting on vertical integration (custom silicon, own facilities) against the rent-from-hyperscaler model, and this is that thesis in PR form. The real content is presumably in the video interview the page is promoting, not the text. Verdict: 👎 a marketing stub dressed as an article — zero numbers, all vibes, and the questions are doing the work the answers should. File it as "Meta wants you to know it builds its own stuff," nothing more.
