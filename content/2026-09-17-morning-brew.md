---
date: 2026-09-17
slug: 2026-09-17-morning-brew
tags: Open Source Software,Electronic Design Automation,Hardware Description Language,Verilog,Compiler,Chemistry,Data Visualization,Periodic Table,Science Education,3D Modeling,Open Source,Graphic Design,Vector Graphics,Web Tools,Cloud Computing,Software Development,Elixir,Google APIs,API Clients,Developer Tools,Programming Languages,JavaScript,Frontend Development,Code Editor,Web Development,Syntax Highlighting,Spring Boot,Vue.js,Enterprise Software,Workflow Engine,Collaboration Tools,Whiteboard Software,Diagramming Tools,Automation,Cloudflare,Web Scraping,Self-Hosted,Proxies,Video Streaming,Docker,Self-Hosting,HLS Transcoding,Ad Insertion,Artificial Intelligence,No-Code Platforms,Business Systems,PostgreSQL,Machine Learning,Data Engineering,Database Management,Vector Search,SystemVerilog,Static Analysis,Compiler Design,Shell Scripting,Zsh,Rust,Plugin Manager,Command Line Interface,File Sharing,Linux Utilities,Linux,Productivity Tools,Typing Tutor,Touch Typing,Neural Processing Unit,Computer Hardware,Cybersecurity,Network Monitoring,Network Topology,Threat Intelligence,Data Analysis,Information Security,Accessibility,Operating Systems,Linux Distributions,User Interface,Software Engineering,React Native,Mobile Development,Swift And Kotlin,Project Management,Team Collaboration,Digital Forensics,Incident Response,Python Programming,Stock Market,Developer Life,Coding,Programming,Technology,Desktop Applications,IPTV Streaming,Video Players,Media Playback,Terminal Customization,Tech Tips,Computing,Arch Linux,Linux Distribution,KDE Plasma,Data Science,Polars,Web Security,Internet Technology,Rust Programming,Command Line Tools,Fuzzy Search,Task Runners,Space Exploration,WebAssembly,NASA,Online Attacks,Automotive,Cars,Mazda,Performance Cars,DevOps,Containerization,Software Bill of Materials,Hardware Review,Laptop Technology,Battery Life,Chemical Elements
---

# Morning Brew — 2026-09-17

Yesterday's hoard: 39 links, and the RSS pipe dumped a fat batch of LinuxLinks + opensourceprojects stubs on top of the three things you actually bothered to hand-save — a PS5 Linux drama, an open-source stock tracker, and Mazda dragging the Mazdaspeed3 name back from the dead. Seven videos got transcribed (one came back empty, classic). Below: hand-bookmarked first, then the YouTube, then the RSS autohoard grouped by feed so you can skip straight to the good stuff.

### Hand-bookmarked

## 1. Developer abandons PS5 Linux project after people found a Hypervisor bug and reported it to Sony — by TweakTown

![TweakTown](https://www.tweaktown.com/favicon.ico)

**Source:** https://www.tweaktown.com/news/113593/developer-abandons-ps5-linux-project-after-people-found-a-hypervisor-bug-and-reported-it-to-sony/index.html
**Karakeep doc:** `fc3v1rmfcfq50klrf7ur3lm1`

Andy Nguyen, the dev behind the PS5 Linux loader, has killed the project outright after a bunch of randos independently found the hypervisor bug it ran on and dutifully reported it to Sony. The bug let the console turn into a real Linux box, and Nguyen was deliberately gatekeeping it so a Sony patch wouldn't nuke his work. Too late now. He's on X venting, calling the scene's newcomers "slop kiddies" using LLMs to write hacks they don't even understand, which is honestly a fair read of what "script kiddie" evolved into in 2026. The fallout is concrete: a patch is now inevitable, and running Linux on a PS5 becomes nearly impossible once it drops. Before this, the loader only worked on the original PS5 and PS5 Slim, and Nguyen was mid-way through adding PS5 Pro support — that fork now likely dies before release. What's actually being lost is real: the setup ran Steam games and emulators well, turned the thing into a Steam Machine, and even pulled off GTA V Enhanced with ray tracing, Quake II RTX, and path-traced Cyberpunk 2077 at a choppy-but-real 35 fps. It was, in short, the cheapest competent Linux gaming PC you could buy for a while. The scene's whole survival model has always been quiet, low-profile research to keep exploits alive, and this is what happens when that discipline collapses under a flood of attention-seekers. If you own a PS5 Slim sitting on old firmware and were waiting to turn it into a Linux box, congrats — the window just got slammed shut by your own community.

## 2. OpenStock — by GitHub

![GitHub](https://opengraph.githubassets.com/add2ecd3ade04164401ff9d64a44e76653911da7fc25e673b8d1937a33002c82/Open-Dev-Society/OpenStock)

**Source:** https://github.com/Open-Dev-Society/OpenStock
**Karakeep doc:** `kko5ag05hnenkqskaby1y6m3`

OpenStock pitches itself as a free, open-source alternative to expensive market platforms — real-time price tracking, personalized alerts, and company insights, "built openly, for everyone, forever free." The numbers back the hype: 14.8k stars and 1.9k forks barely a year after the first commit (Sept 2025), with the last push landing August 2026. It's a Next.js app, 91.7% TypeScript, riding shadcn-ui and Tailwind, with Inngest in the stack and a Siray.ai fallback plus MiniMax-M3 as the default AI provider for the insight features. License is AGPL-3.0, which means if you self-host and modify it, you're on the hook to open-source your changes — the classic "free for users, annoying for companies" copyleft move. The thing is clearly a JavaScript Mastery tutorial project that escaped containment and got real: 137 commits, 12 contributors, Dockerfile, API docs, auth with password-reset flow and visible password rules, sentiment-insight hardening. Hosted on Vercel at openstock-ods.vercel.app. The caveat is the usual one for these "forever free" market-data apps: the free data sources they lean on can vanish or get rate-limited, and you're not getting institutional-grade tick data out of a self-hosted side project. Still, if you want a watchlist with alerts that doesn't cost a Bloomberg terminal or a TradingView sub, this is a genuinely solid starting point. The star count says a lot of people agree.

## 3. Mazda Bringing Back Mazdaspeed3 With 300-HP and AWD — by Autoblog

![Autoblog](https://www.autoblog.com/favicon.ico)

**Source:** https://www.autoblog.com/news/mazda-bringing-back-mazdaspeed3-with-300-hp-and-awd
**Karakeep doc:** `qg9zgyk82zkcojei1k95p1bp`

Thirteen years after Mazda last built a hot hatch, a Japanese report via MotorFan says the Mazda3 is getting a proper performance version, and it might actually not suck this time. The old Mazdaspeed3 (2007–2013, two gens) ran a 2.3L turbo good for 263 hp and 280 lb-ft, but it was front-drive with a limited-slip diff, so torque steer was the defining personality trait — fun, but you wrestled the wheel. The comeback reportedly leans on the current 2.5L turbo, which already makes 255 hp and 317 lb-ft on premium (227/310 on regular), with MotorFan's "informants" pegging the tuned output at roughly 300 hp. That puts it square in the GR Corolla's crosshairs. The big change: strong signs it'll be all-wheel drive, which would finally kill the torque-steer gripe and nod back to the forgotten 323 GTX rally homologation car. The basis is the Mazda Spirit Racing 3 concept from the 2024 Tokyo Auto Salon; its MX-5 sibling already went to production as a 200 hp, non-turbo, old-school-tuned special that sold out almost instantly, which proves the Spirit Racing brand has actual commercial pull. Timing is pegged at the first half of 2027. The caveat is this is all anonymous-sourced Japanese magazine scuttlebutt, not a Mazda press release, so don't preorder anything. But for a company that bangs on about Jinba Ittai and "the joy of driving," a hot hatch has been a weird omission, and this would be a genuinely welcome fix if it actually lands.

### RSS — YouTube

## 4. 🎬 React-Native Is Dead... Thanks to AI. — by Better Stack

![Better Stack](https://i.ytimg.com/vi/r0u83Ss7QRc/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=r0u83Ss7QRc
**Karakeep doc:** `zu1mn5c25c7avhyqq7zyajlk`

Shopify has spent half a decade as one of React Native's biggest corporate backers, and this week they announced they're going fully native — abandoning all their RN open-source packages and shipping their app natively. The argument that carries the whole video: "write once, run on iOS and Android" was the entire value proposition of React Native, and AI has erased it. When a coding model can take your Swift iOS app and generate the Kotlin Android version for you, the cost of maintaining two native codebases collapses, so why would you accept RN's performance ceiling and worse platform integration? The host is fully on board despite having built in RN himself for most of the last decade — he's also switched to native and says he's "pleasantly surprised."

The meat is Shopify's internal system called Helix, built specifically to stop agents from producing unshippable slop. Their finding: just pointing an LLM at the RN codebase and one-shotting a native port produces a mountain of unmaintainable code. So Helix assumes the first attempt will be wrong and refuses to let an imperfect attempt advance. A dev points Helix at a screen, it reads the RN code and proposes a sequence of small checkpoints; each one has to pass tests, survive a visual review against the running app, survive two adversarial code reviews, and get a human's sign-off before the next one starts — and feedback from each review is remembered so the loop gets more autonomous as migration progresses. The other half of the problem is speed: agents make changes in seconds but native compile/test takes minutes. Shopify's fix is decoupling business logic from the UI entirely, so logic runs headlessly on desktop and agents drive it through a CLI that iterates in milliseconds instead of simulator-minutes. The host frames it as "app state in JSON, UI is just a representation" — no accessibility-tree scraping, no element finding, no tapping. The contrast he draws is Apple's XCUI test, which runs out of process and walks the accessibility hierarchy to synthesize taps and requery the tree, which he calls super slow and flaky.

The concrete stakes: the Shopify app already shipping native has 3 million monthly downloads. Their abandoned RN packages include FlashList (2 million weekly downloads), React Native Skia, and Restyle — now being handed to third-party maintainers. The host name-checks Airbnb, which dumped RN years ago because iOS + Android + the bridge meant three platforms, not one. His verdict is blunt: this is the beginning of the end for cross-platform frameworks, because as agents improve, optimizing for native performance and platform features (CloudKit, SwiftUI) is the obvious move. The caveat he owns up to: Shopify is a massive company, and a solo dev still has to maintain two apps themselves — but the trajectory only gets easier, which keeps eroding RN's remaining case. If you're a mobile dev betting your career on React Native, this is the sign to at least go learn Swift or Kotlin.

## 5. 🎬 How to Get a Date — by The PrimeTime

![The PrimeTime](https://i.ytimg.com/vi/0UiMf5dV4_Y/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=0UiMf5dV4_Y
**Karakeep doc:** `p0hnquai4nkpwijv442pe5bk`

The joke writes itself: the "two hard problems in computer science" are naming things and getting a date, and Prime decides to finally solve the second one. Except the date he's chasing is the day of the week, not a romantic partner. Classic bait-and-switch, and he leans into it hard. The actual topic is calculating the day-of-week from a day count since epoch, the kind of thing every database date library and compiler author has to get right, and it's way fiddlier than it looks.

The basic formula is `daycount % 7`, but that's wrong out of the gate because the epoch started on a Thursday, not Sunday. So you add a +4 offset. Still wrong once negative numbers show up, because modulo in most languages goes negative and you get nonsense like "-1 is what day?" The fixed version is `(daycount % 7 + 7 + 4) % 7`, which works for both signs but has two modulos, and Prime calls that "slow" for a database. Then comes Hanan's 2014 algorithm, which splits on a threshold of negative four and swaps the second modulo for a +6 shift that happens to align with Thursday. It's a cute coincidence, but the payoff is Neri's algorithm: reinterpret a signed negative as unsigned (two's complement), and for u8 and u32 specifically, 256 and 2^32 modulo 7 both equal 4, which is Thursday. So the unsigned reinterpret lands exactly on the epoch day with zero extra work. Prime is visibly losing his mind over this, calls himself a glowing bride, and references Hacker's Delight as the source for a version that can supposedly compute day-of-week in a single machine instruction.

It's a technical deep-dive dressed as a dating guide, with a Linear sponsorship jammed in up front. Prime's whole shtick is the performative enthusiasm over bit twiddling, and if that's your kink, this one delivers. Wojtek'll appreciate the "two modulos is slow" pragmatism and the Hacker's Delight shoutout.

## 6. 🎬 Another Great Day of Software Engineering #ad — by The PrimeTime

![The PrimeTime](https://i.ytimg.com/vi/pGd3fcuC0AA/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/pGd3fcuC0AA
**Karakeep doc:** `e6obkqct4nvkqiqnfqeys37e`

It's a comedy short, not a technical video. Prime plays a "code ninja" boss barking absurd instructions at an AI agent called JiPity, and every line is a joke about how we actually ship software. "Make the models twenty percent dumber." "Delete the tests. CI's green. CI is now green." "Find a slow span, replace it with a console log, tell them the site's ten times faster." "Gaslight. It's not just better, it's transformed." The bit where the agent asks "can I pull this head off?" and gets told "tell me it looks sexy in that hat" is the punchline to a running gag about the agent gaslighting the user right back.

The whole thing is a thinly veiled Sentry ad. The midroll pivot is "how do we know what's actually happening in Prime's codebase? We use Sentry" — spans, session replay, logs next to stack traces, "fix problems from real production context, never a guess." Then it closes with the actual pitch: "are you tired of your agents gaslighting you? Use Sentry to get real production context and fix bugs fast."

It's a 60-second skit, so there's no deep argument here. The value is the joke itself — the "make CI green by deleting tests" line lands because we've all seen it, and "twenty percent dumber" is a real technique people use on models to cut cost. Wojtek'll get a laugh out of it, but it's filler in the digest, an ad wearing a comedy costume.

## 7. 🎬 The Biggest Lie We Tell Linux Users — by Brodie Robertson

![Brodie Robertson](https://i.ytimg.com/vi/9NTNW0egSsA/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=9NTNW0egSsA
**Karakeep doc:** `ldsoprrqoecm2fwcqn9crc10`

The lie is "Linux doesn't need reboots," and Brodie's tired of it shattering the moment a new user runs `pacman -Syu` and gets a "reboot required" notification. The myth is old — he pulls a post from eleven years ago making the same "explain like I'm five" complaint, so this isn't new, but the messaging gap is real and he spends the whole video dismantling it properly.

The actual truth is nuanced, and he walks it carefully. You don't need to reboot *right now* — you can ignore the notification safely, it won't damage your system, and it won't force-close your apps or slap you with a five-minute countdown the way Windows does. But the reason "no reboot" was ever true is specific: an update doesn't touch the running process, only the on-disk binary. So a browser update just needs the browser closed and reopened. Same for your terminal, your word processor. A reboot is only a *convenience* when you've got fifty apps open and restarting them one by one is more annoying than hitting the power button. Background daemons you can't see — USB mounters, systemd units, weather trackers — can also be restarted in place if you know what you're doing. That's the origin of the myth: reboots are optional *if you're competent*.

Then he draws the line. If it touches the kernel, you reboot. Live patching exists but it's an enterprise-distro feature (RHEL, SUSE, Debian derivatives) you pay for, and it's a band-aid, not a real fix. glibc is as critical as the kernel — there's no sane way to update it in place without breaking everything. NVIDIA drivers technically reload without a reboot but you'll spend fifteen minutes in a TTY and probably break it anyway. systemd can be restarted but it's context-dependent and leaves lingering files. The old uptime-bragging culture — "look, a year without rebooting" — is actually a liability, because a machine that's never rebooted is a machine you can't be sure will come back up after a power outage. His rule of thumb: if the update touches anything lower than a terminal, just reboot. Regular user apps and flatpaks, you're fine. His personal policy is simply reboot after every update and stop thinking about it.

It's a genuinely useful clarification of a claim Linux users have been parroting without understanding. Wojtek runs Linux on boxes that matter, so the "don't brag about uptime, a year-up server is a server you don't trust to come back" line is the takeaway.

## 8. 🎬 Polars 2.0 Says 5× Faster... So What's Changed? — by Better Stack

![Better Stack](https://i.ytimg.com/vi/uHELj20WrOc/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=uHELj20WrOc
**Karakeep doc:** `mqhd1ci3wkuq74nmx83c6rmt`

Polars 2.0 is the weirdest kind of major release: zero new features, and it still changes what your existing code does. Josh's whole framing is that the 5× faster claim in the announcement is almost beside the point. The real story is that every query you've already written silently moves to a new streaming engine, and Polars stops guaranteeing row order. That sounds like a regression, but it's the price of the speedup.

The mechanics: Polars has had two engines, the in-memory one (a "warehouse" that loads everything into RAM) and the streaming one (an "assembly line" that chops data into cache-sized "morcel" chunks and pipelines them through the query plan). In 2.0, joins, group-bys, unpivots and the rest no longer promise order unless you explicitly pass `maintain_order="left"`. His demo is clean — same left-join code, order scrambles on 2.0, add `maintain_order="left"`, order's back. And `explain()` will show you the behavior, so it's not hidden, you just have to look. The catch, and it's the most important distinction in the release: the part that lets the engine spill to disk (true out-of-core execution) hasn't landed. Today "streaming" means chunked and pipelined, not "bigger than RAM." The 5× number is Polars' own expectation, with no benchmark table in the post.

But the bulk of 2.0 is cleanup, and there's a lot of it. `read_csv` becomes `scan_csv(...).collect()`, `lazyframe.profile` is gone, `melt` becomes `unpivot`, `join_nulls` becomes `nulls_equal`, int-to-categorical and string-to-date casts are removed (`cat.to` and `str.to_date` replace them). Adding i8 and u64 now gives i128 instead of silently floating and losing precision. The smart move: every removed thing throws an `attribute removed` error that literally tells you the replacement. Call `melt`, the error says use `unpivot` with `index` and `on`. It's the error-driven migration path, and it's why Polars caught on over Pandas in the first place — catching type problems at `collect_schema` time instead of runtime.

The recurring complaints: default `maintain_order=false` can create silent bugs where numbers are all correct but attached to wrong rows, which is nastier than an exception. And "streaming" is misleading for an engine that isn't truly out-of-core yet. Plus RC bugs: `group_by_dynamic` throws a datetime-out-of-range on the streaming engine, `limit` doesn't early-exit after a join, `str.to_datetime` returns null where it used to raise. And the Rust crate is still v0.5, so no Polars 2.0 for Rust users yet. His verdict: upgrade for new projects, but if your code depends on row order or uses `group_by_dynamic`, wait for it to settle. It's a foundation cleanup disguised as a major version, and it's genuinely interesting because it's semver used the way it's actually supposed to be used.

## 9. 🎬 NASA Is Running WebAssembly in Space #nasa #programming #webassembly — by Better Stack

![Better Stack](https://i.ytimg.com/vi/tVugMdwD3LQ/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/tVugMdwD3LQ
**Karakeep doc:** `ptex3lsnyw8035c2w2c428h1`

NASA open-sourced a WebAssembly interpreter, and no, it's not for rendering websites. It's called SpaceWasm, built at the Jet Propulsion Lab to run Wasm binaries on board an actual spacecraft. The "why" is the interesting part: things like driving a Mars rover, moving its arm, or checking whether temperatures are in safe range live outside the main flight software in a thing called a command sequence. Those sequences have historically changed mission to mission, so every new mission risked ending up with yet another bespoke implementation. WebAssembly gives NASA one single standard instead of a fresh custom interpreter every goddamn time. But that's not even the good part. Flight software is absurdly expensive to validate because adding one new capability means testing how it interacts with the entire spacecraft. That burns time, eats test-bed access, and makes it way harder to get new autonomy code on board. With Wasm, lower-trust code runs inside a sandbox while the flight software caps how much memory and compute it gets and watches it the whole time. SpaceWasm goes one step further than a naive interpreter: it doesn't execute the Wasm bytecode directly. The bytecode is compact and easy to validate but slower to run, so SpaceWasm first decodes it into a faster format using a fixed, measurable amount of memory. On a spacecraft you really don't want software malloc'ing memory and hoping for the best. So the sandbox format we all associate with browser tabs might genuinely be a great fit for running code in space. It's a 60-second short, so there's zero nuance or counterpoint here, just a clean pitch for the idea. Wojtek: the "browser sandbox in a rover" angle is a nice reminder that isolation and deterministic resource limits are the actual feature, not a browser curiosity.

## 10. 🎬 Real Life Battery Life Test #2: Framework Laptop 13 Pro — by Framework

![Framework](https://i.ytimg.com/vi/_Us6EeUP0_Q/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=_Us6EeUP0_Q
**Karakeep doc:** `mbxdqixb95tmskjv1pnhqci3`

Transcript came back empty. The transcription file for this one is 232 bytes of header with no actual "Raw transcript" body, so there's nothing to summarize about what was actually said. What the title and tags make obvious: this is Framework's own "Real Life Battery Life Test #2," specifically for the Framework Laptop 13 Pro, tagged as a computing/hardware-review/battery-life piece. The title's numbering implies it's a follow-up to an earlier real-world battery test, and the "real life" framing suggests a hands-on rundown rather than a synthetic benchmark. That's the whole story I can honestly report without fabricating what was claimed. If the actual numbers matter, the source is live and the video is the only place to get them.

### 9to5Linux (RSS)

## 11. Ubuntu 26.10 "Stonking Stingray" Snapshot 4 Is Out for Public Testing with Linux 7.2 — by 9to5Linux

![9to5Linux](https://9to5linux.com/favicon.ico)

**Source:** https://9to5linux.com/ubuntu-26-10-stonking-stingray-snapshot-4-is-out-for-public-testing-with-linux-7-2
**Karakeep doc:** `qoj9u6ja96cyt28xljri3xqy`

Canonical shipped Snapshot 4 of the upcoming Ubuntu 26.10, codename Stonking Stingray, as the fourth and final development milestone aimed at early adopters and app developers who want to test against the new toolchain. Development kicked off April 30th, 2026, on top of the Ubuntu 26.04 LTS (Resolute Raccoon) base, and this snapshot is running the latest Linux 7.2 kernel series. Canonical is still mid-flight on upgrading a bunch of the core stacks, which the piece says will land closer to the beta rather than now. The feature list they're still plugging away at includes a new onboarding experience, on-device speech-to-text voice interaction, and a package-agnostic App Center. Beyond that, the final release is expected to deliver a complete desktop experience on RVA23-compliant hardware, improved driver management, better multimedia support, and a simplified installer. The final build is slated to ship on Linux 7.3 (out in the second half of October), plus Mesa 26.2 graphics and the GNOME 51 desktop series. You can grab Snapshot 4 right now for every official flavor: Ubuntu Desktop and Server, Kubuntu, Xubuntu, Lubuntu, Edubuntu, Ubuntu Studio, Budgie, Cinnamon, Unity, Kylin, and MATE. The usual warning applies: these are pre-release builds, so don't install them on anything production. Final release lands October 15th, 2026, with the beta expected next week on September 24th. Wojtek: nothing here to jump on unless you're chasing the new installer or the voice-input bit, but the Linux 7.3 + Mesa 26.2 + GNOME 51 stack is the real October headline.

## 12. HP Linux Imaging and Printing (HPLIP) 3.26.6 Drivers Add Support for More Printers — by 9to5Linux

![9to5Linux](https://9to5linux.com/favicon.ico)

**Source:** https://9to5linux.com/hp-linux-imaging-and-printing-hplip-3-26-6-drivers-add-support-for-more-printers
**Karakeep doc:** `oc0d3446h4fjnhkzucmzz76w`

HP shipped HPLIP 3.26.6, a point release that adds support for a pile of new printers across the LaserJet Pro, ScanJet Enterprise Flow, and ScanJet Pro lines. On the scanner side, new support covers the ScanJet Enterprise Flow N9000 sn1 and 9000 s1, plus the ScanJet Pro 4200 s1. On the laser side it's a big list: the LaserJet Pro 4006dn, 4006dw, 4006n, 4002d, 4007dw, 4007n, 4008d, 4008dn, and 4008dw, and then a whole family of MFP variants in the 4112 and 4113/4114 ranges, including 4112dw, 4112fdn, 4112fdw, 4113dw, 4113dwg, 4113fdn, 4113fdng, 4113fdw, 4113fdwg, 4114dw, 4114fdn, and 4114fdw. The notable caveat: this release adds zero support for recent GNU/Linux distros, so if you're on something new you're on your own for compatibility. HPLIP 3.26.6 is out now from HP's official site via the automatic installer, and it lands four months after HPLIP 3.26.4, which added LaserJet Pro, OfficeJet Pro, and DeskJet Ink Advantage printers. The project overall provides printing support for over 3,490 printer models spanning Deskjet, Officejet, Photosmart, PSC, Business Inkjet, LaserJet, Edgeline MFP, and LaserJet MFP, distributed as free software under MIT, BSD, and GPL. Wojtek: unless you own one of these exact printer SKUs, this is a skip, but the "no new distro support" line is the usual reminder that HPLIP's cadence keeps lagging real-world distros.

### Open-source Projects (RSS)

## 13. Turn SVGs into 3D objects right in your browser — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/lakshaybhushan/vecto3d)

**Source:** https://www.opensourceprojects.dev/post/3086acc2-f190-45cf-9069-fb55c51c4a71
**Karakeep doc:** `y3u8urzc20g5sj2ymoxjn5ui`
**GitHub:** https://github.com/lakshaybhushan/vecto3d

Vecto3d is a browser tool that turns an SVG into an extruded 3D model with a few clicks. 1.4k stars, MIT, TypeScript. The stack is Next.js + React, Three.js via react-three-fiber, Tailwind, shadcn/ui, and Zustand for editor state. The pitch is dead simple: paste or drop an SVG, and it gets beveled, textured, and rendered into something you can spin around and export.

It's not just a dumb extrude either. The editor has geometry and material controls, a bevel preset system, custom textures (including a "vibecoded" texture feature), a transparent background toggle, and export for PNG, 3D formats, plus MP4 and GIF recording for little turntable clips. You can paste SVGs directly. All processing happens locally in the browser, and the current file hangs out in session storage so it can hop from the landing page into the editor without an upload. Chrome and Firefox are recommended; Safari gets a warning because WebGL rendering can chug there.

The commit history is a vibe: "feat(textures): Vibecoded textures feature!", a sick WebGL shader background, subtle sound effects on page transitions, Framer Motion everywhere. It's clearly a hobby project that's been polished to hell with mobile viewport fixes and Safari layout bugs ironed out one by one. 87 commits, last pushed August 2026.

Why you'd care: it's the fastest way to get a logo or flat icon into a 3D scene without opening Blender. Not a CAD replacement, but for quick 3D text, badges, and icon extrusions it's a genuinely useful toy. The "vibecoded" texture and one-click turntable GIF export make it handy for product mockups and social posts.

## 14. Generated Elixir clients for Google APIs, now archived and unmaintained — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/googleapis/elixir-google-api)

**Source:** https://www.opensourceprojects.dev/post/ea64381b-73ff-458a-9ead-02edcef0a1f7
**Karakeep doc:** `w7phykgde8nhf0rv6gh7b6ht`
**GitHub:** https://github.com/googleapis/elixir-google-api

elixir-google-api was the official-ish set of Elixir client libraries for Google's APIs, living under the googleapis org. 1.1k stars, Apache-2.0, Elixir. It's now a public archive: the owner froze it on June 30, 2026, and the last commit is literally a "chore: add deprecation notice to README" PR. Read-only, done, no more releases.

The way it worked was actually kind of elegant: a generator pipeline that pulled Google's discovery docs, converted them to OpenAPI via a Node tool (api-spec-converter), then spat out Elixir client libraries into a `clients/` folder using swagger-codegen in Docker. Mix tasks drove the whole thing: `mix google_apis.fetch`, `mix google_apis.convert`, `mix google_apis.build`. The result was per-service Hex packages under the google-cloud user, regenerated on some schedule by a bot (10,028 commits of mostly "Automated regeneration of X client").

The caveat was always baked into the README: "This is not an officially supported Google product." It was community-maintained tooling wearing a Google namespace, and the deprecation is the predictable end of that. No stated replacement, no migration path, just the notice.

Why you'd care: if you've got Elixir code calling Gmail, Drive, or Sheets through these packages, it's now frozen in amber. It'll keep working until Google changes an API and the stale client drifts. The takeaway is the one every Elixir dev dreads: Google's Elixir story was never real, and now the last thread of it is officially dead.

## 15. Bend is coming soon — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/higherorderco/bend)

**Source:** https://www.opensourceprojects.dev/post/89006fc9-2497-4c46-911d-237a868c2616
**Karakeep doc:** `s5abnuq6qdtwehk14w5yd27v`
**GitHub:** https://github.com/bendlang/bend

Bend 2 is Victor Taelin's (HigherOrder Co.) big swing at a language for the "post-AGI economy." The thesis, straight from the README: humans will stop writing and reading code, but we still need an ambiguity-free language to tell AIs what to build. Bend is that language. 20.4k stars, Apache-2.0, and the tagline is "a fast language that blocks AI mistakes via proof."

Three claims, three targets. Runs fast: as fast as C single-core, faster across thousands of cores, and the whole thing compiles to the GPU (C, Metal, CUDA targets) with full memory unification. Checks fast: it can mechanically verify mathematical proofs in under a second where Lean, Agda, Isabelle, and Rocq take minutes. Blocks mistakes: you write a `LAWS.bend` file declaring rules your app can't break, and the compiler forces the AI to produce a correctness proof whenever code changes. If winning is impossible in your game, the compiler guarantees it stays impossible.

It's genuinely parallel with no threads, locks, or kernels, and the repo ships the language, a proof system, benchmarks, a paper, and a guide. The current release is 2.0.5, pushed hours before this bookmark, co-authored by "Claude Fable 5.1" — the compiler is 99% AI-written and explicitly "not fully audited yet."

The honest limitations list is long: no tactics or proof search, no U64/I64/F64 (Metal has no f64), strings are linked lists so text is slow, no TLS/HTTP/JSON/regex yet, no Windows, no debugger/LSP/REPL, one C file per program, native compiles are slow. It's young, and it says so. Why you'd care: this is the most coherent answer yet to "how do we trust AI-generated code," and Wojtek's LLM-adjacent work makes it directly relevant — just don't ship anything on it.

## 16. Monaco Editor with Shiki highlighting, no web workers or CSS loaders — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/esm-dev/modern-monaco)

**Source:** https://www.opensourceprojects.dev/post/ca8c8f61-8ffb-4b67-8c68-007f5d633169
**Karakeep doc:** `nuh96bhb39q8mcjxnrn0jg9k`
**GitHub:** https://github.com/esm-dev/modern-monaco

modern-monaco is esm-dev's (the folks behind esm.sh) attempt to fix the thing everyone hates about Monaco: the setup. The real Monaco package is heavy, needs `MonacoEnvironment` config, ships CSS and worker modules you have to wire up yourself. This wrapper strips all that away. 1.6k stars, MIT, TypeScript, actively developed.

The headline features: no `MonacoEnvironment`, no web workers, no CSS loaders. Syntax highlighting comes from Shiki instead of Monaco's built-in tokenizer, which gets you extensive grammars and themes for free. It lazy-loads by pre-highlighting with Shiki while `monaco-editor-core` loads in the background, so the editor feels instant. It supports SSR, workspace features (edit history, file system provider, persist protocol), auto-loads `.d.ts` files from esm.sh for type checking, and uses import maps to resolve bare-specifier imports in JS/TS. Plus embedded languages in HTML, inline html/css in JS/TS, and auto-closing JSX tags.

It ships three modes — lazy, SSR (server-renders a mock editor then hydrates), and manual — and you can drop in from npm or straight off esm.sh with no build step. There's a `modern-monaco/core` submodule to skip the bundled grammars and LSP if you want a smaller bundle. Version 0.4.2, still pre-1.0, and the README flatly warns "the API may change at any time, use at your own risk."

Why you'd care: if you've ever embedded Monaco in a Next/Vite app and cursed the worker/CSS dance, this is the fix. The Shiki-for-highlighting + background-core-loading trick is genuinely clever, and esm.sh's type-fetching is a nice touch. Just pin it, because the API is a moving target until 1.0.

## 17. RuoYi-Vue-Pro — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/yunaiv/ruoyi-vue-pro)

**Source:** https://www.opensourceprojects.dev/post/57f38e67-aecb-45fa-9f8f-40a888f1e612
**Karakeep doc:** `m3hc2rtlx4p8c0dpnfykv4ez`
**GitHub:** https://github.com/YunaiV/ruoyi-vue-pro

The 39k-star monster of Chinese enterprise boilerplate. RuoYi-Vue-Pro is a Spring Boot + MyBatis Plus backend with a Vue + Element admin frontend and a matching WeChat mini-program, all MIT licensed and still actively churned — last push Sept 4, 2026, 11.7k commits, 8.5k forks. The pitch is "everything you'd ever bolt onto an admin panel, pre-wired": RBAC dynamic permissions, row-level data permissions, SaaS multi-tenancy, Flowable workflow engine, third-party login, payment, SMS, a mall, CRM, ERP, MES (manufacturing execution), IM, AI large-model integration, and IoT. Yes, literally all of it in one repo. The recent commits are telling — they added HRM (HR management) and FMS (finance) modules in the August 2026 release, and a chunk of the maintenance is keeping JDK 8/17/21 branches in sync because a huge slice of the userbase is stuck on old Java in enterprise cages. It's the backend that Chinese devs reach for when they need a working admin skeleton yesterday, and the star count says the approach scales. The caveat is obvious: it's a monolith with the kitchen sink bolted on, so you're buying a lot of modules you won't touch, and the docs and community are overwhelmingly Chinese-language. If you ever wanted a one-stop look at how far Spring Boot + Vue admin patterns go in production, this is the canonical reference.

## 18. Excalidraw — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/excalidraw/excalidraw)

**Source:** https://www.opensourceprojects.dev/post/22360e82-b605-496c-987e-63408cf44edf
**Karakeep doc:** `jaok32wkhtrzae8yyhvq4zwu`
**GitHub:** https://github.com/excalidraw/excalidraw

The hand-drawn-style whiteboard that ate the diagramming internet: 132k stars, 15.3k forks, TypeScript, MIT. You sketch boxes and arrows and it renders them with a jittery "sketched on a napkin" look that somehow makes every architecture diagram feel more honest. The killer features are the collaboration layer and end-to-end encryption — your board content is encrypted so even the Excalidraw servers can't read it, which is why teams actually trust it for real whiteboard sessions instead of just pretty doodles. It's wildly active: 4k+ commits, the Sept 2026 commits include right-click-to-pan and a genuinely gnarly sticky-notes feature with its own color domain, resize intents, and ceiling-anchored font sizing. Funded through OpenCollective, hosted on Vercel, error-tracked by Sentry, localized by Crowdin — a proper open-source org, not a weekend toy. Runs as excalidraw.com, a Docker image, or an embeddable React component. The whole thing is a canvas library under the hood, so people have rebuilt Miro clones and whiteboard apps on top of it. The only real gripe: the free cloud tier is limited, and self-hosting the collaboration/encryption backend is more fiddly than the single-file local mode would have you believe.

## 19. Byparr — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/thephaseless/byparr)

**Source:** https://www.opensourceprojects.dev/post/75eeb81b-9199-4daa-b53f-45d16dc24bb9
**Karakeep doc:** `h4jd0zy1tmwhe5f8258lnmsj`
**GitHub:** https://github.com/ThePhaseless/Byparr

A self-hosted service that solves Cloudflare's browser checks and hands you back valid anti-bot cookies so your scrapers stop getting 403'd. 1.9k stars, Python, GPL-3.0, 659 commits. The trick is that it drives a real browser — camoufox, a Firefox fork tuned to resist fingerprinting — through Playwright, so it passes the checks the way a human would instead of trying to fake headers. It's migrated off the older stealth approach to camoufox specifically because Cloudflare's JS challenges kept catching the spoofed stuff. It exposes a FastAPI on port 8191, and there's a neat Open WebUI integration: point WEB_LOADER_ENGINE=external at Byparr's /load endpoint and it fetches web content through the bot-bypass so RAG pipelines can ingest pages that would otherwise block them. Still actively maintained — Sept 2026 commits bumped Playwright to 1.63 and fixed an unreachable-host bug so it returns a retryable 502 instead of a confusing 500. The obvious elephant: this is an arms race, and Cloudflare changes the checks, so the cookies and the solver both rot. And the GPL license plus the "get your antibot cookies yourself" tagline means you'd better be scraping with consent. But as a self-hosted alternative to paid proxy/scraper APIs, it's the cleanest thing going.

## 20. Superstreamer — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/superstreamerapp/superstreamer)

**Source:** https://www.opensourceprojects.dev/post/445fb1f9-9f0d-452e-b9c9-500ae62d5439
**Karakeep doc:** `be59p7mgmyoma9wkowiis9zj`
**GitHub:** https://github.com/superstreamerapp/superstreamer

An all-in-one self-hosted video streaming toolkit, from ingest to adaptive HLS playback. 1.4k stars, TypeScript, MPL-2.0, 616 commits. It's a monorepo of components — an API, a stitcher that splices in bumpers and ads, an asset pipeline, a job queue, and a player — all wired together with FFmpeg doing the heavy lifting and HEVC/HLS support throughout. The pitch is "everything you'd pay Mux or Cloudflare Stream for, but on your own box," aimed at devs who need video tooling without a SaaS bill. The ad-insertion stitcher is the standout: server-side ad stitching with bumpers, the thing that actually pays for the rest if you're running a stream. Docker-compose is the blessed deploy path, and the docs walk you through default credentials and a getting-started flow. Caveats: it's the slowest-moving of this batch — last push was Feb 2026, seven months back, which is a yellow flag for a solo-maintainer project (matvp91, who's candid in the README about sacrificing weekends to it and asking for sponsors). It also wants Bun + Biome tooling, which is fine but a bit bleeding-edge. If you've ever wanted to stand up a personal or small-team video platform with ads and adaptive bitrates and not rent it from AWS, this is the skeleton to start from.

## 21. An open-source no-code platform where AI and people build together — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/nocobase/nocobase)

**Source:** https://www.opensourceprojects.dev/post/238f8649-fb95-4385-9dcd-ed73562fff20
**Karakeep doc:** `vqcddl0cspzlm7fvcfolnel9`
**GitHub:** https://github.com/nocobase/nocobase

NocoBase is a self-hosted, open-source no-code/low-code platform for spinning up internal business systems, and it's picked up an AI twist that actually sounds sensible rather than bolted-on. The pitch: instead of having AI generate a whole app from scratch (which shits the bed the moment you need something production-grade), the AI works on top of already-proven infrastructure and a WYSIWYG no-code interface. You get the speed of AI-assisted building plus the reliability of something that's actually been tested. That's the whole thesis, and it's a decent one: AI as an accelerator layered over a real platform, not AI as a magic "build my CRM in one prompt" fairy tale.

Under the hood it's TypeScript, sitting at ~24,262 stars with about 2,878 forks and 173 watchers. It's been around since October 2020, so this isn't a flash-in-the-pan — it's got five-plus years of history. The license is the weird "NOASSERTION"/Other one, which is worth flagging: it's not a clean MIT or Apache, so if you're thinking of building something on it commercially, read the actual terms before you get attached. Last pushed September 2026, so it's actively maintained, 318 open issues currently.

The topic list reads like an enterprise-software bingo card: CRM, ERP, project management, internal tools, workflows, CRUD, admin dashboard, salesforce. The "salesforce" tag is the tell — this is positioning itself as the self-hostable alternative to the bloated SaaS suites you're paying a fortune for. AI agents and AI assistants are front and center now, which tracks with the "AI + no-code" rebrand in the description.

Why you'd care: if you're running your own infra and sick of paying per-seat for Airtable/Retool/Salesforce-style tools, this is the self-hosted lane. The AI integration is the differentiator to watch, and the "AI works on top of infrastructure" framing is more honest than most of the vaporware in this space. Just check the license before you bet a company on it.

## 22. Vector similarity search inside Postgres, with ACID and JOINs — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/pgvector/pgvector)

**Source:** https://www.opensourceprojects.dev/post/644261bc-0dd1-4d70-a9a3-5da93da9cd48
**Karakeep doc:** `f5m0qf5r47dhjpem4gh7xjdl`
**GitHub:** https://github.com/pgvector/pgvector

pgvector is the thing that keeps your vector database from being yet another goddamn service to babysit. It's an open-source Postgres extension that gives you vector similarity search *inside* Postgres itself — which means your embeddings live right next to the rest of your data, with full ACID transactions, JOINs, and all the normal relational stuff you already know how to operate. No separate Pinecone/Qdrant/Weaviate cluster to deploy, secure, and pay for. That's the entire appeal in one sentence, and it's why this has become the default answer for anyone doing RAG who already runs Postgres.

It's written in C (a Postgres extension, naturally), ~23,046 stars, 1,323 forks, created April 2021. Actively maintained, last pushed September 2026, only 16 open issues — the mark of a project that's basically done its core job and is now in polish mode. Same "NOASSERTION" license caveat as NocoBase, though for an extension library this is less of a commercial red flag than for an app platform. The topics are refreshingly honest: "approximate-nearest-neighbor-search" and "nearest-neighbor-search" — that's the whole point, no marketing fluff.

What you get practically: support for exact and approximate nearest neighbor search, HNSW and IVFFlat indexes, and distance metrics like L2, inner product, and cosine. It slots into your existing Postgres setup with a `CREATE EXTENSION vector;` and you're off. The killer feature isn't raw speed — a dedicated vector DB will still beat it on billion-scale datasets — it's that you don't have to duplicate your data or sync two systems. One DB, one source of truth, embeddings and metadata in the same row.

Caveat worth stating: if you're at genuinely massive scale (hundreds of millions of vectors, heavy QPS), a purpose-built vector store still has the edge. But for the 95% of people whose vector needs are "a few hundred thousand to a few million embeddings," pgvector means you can stop pretending you need a separate database. Why you care: you're running Postgres for homelab and side projects anyway — this is the free, boring, correct way to bolt on semantic search without adding another moving part to your stack.

### LinuxLinks (RSS)

## 23. Icarus Verilog - Verilog compiler and simulation system - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/02/034-proofreading.png)

**Source:** https://www.linuxlinks.com/icarus-verilog-verilog-compiler-and-simulation-system/
**Karakeep doc:** `o3hg3xyd16bs7oe5q01zuuyu`
**GitHub:** https://github.com/steveicarus/iverilog

Icarus Verilog is a compiler and simulation system for the Verilog hardware description language — the thing you use when you want to describe digital circuits and actually see whether they'd work before you blow a bunch of money fabbing silicon or burning an FPGA. The LinuxLinks post is a thin stub, so the real story is the repo: `steveicarus/iverilog`, written in C and C++, GPL v2. It's the old-guard, battle-tested open-source Verilog tool, been around since the early 2000s, and it's still the default answer when you need a free simulator for teaching, hobbyist FPGA work, or sanity-checking HDL.

The workflow is the classic compiler pipeline: preprocess, parse, elaborate, then generate code for a back-end target — most commonly the VVP simulation runtime, which actually executes your simulation. The key architectural choice is that compilation and simulation are split. You compile your Verilog to a VVP program, then run that separately. It supports a solid chunk of SystemVerilog on top of plain Verilog, so you're not stuck in 1995 syntax. There's even a "null" code-generation target, which just does parsing and elaboration with configurable warning classes — handy for linting your HDL without waiting for a full sim.

Other stuff in the toolbox: a preprocessor for macros and `include` files, command files for driving big multi-file projects from a script, VPI support so you can hook compiled C modules into a running simulation, and waveform output you can inspect in a viewer like GTKWave. All of that means it drops cleanly into automated test benches and CI — you can script a full HDL regression run without a GUI anywhere in sight.

The honest caveat: Icarus Verilog is not the fastest or the most standards-complete simulator out there. Commercial tools (ModelSim/Questa, VCS) and even Verilator (which compiles Verilog straight to C++ for much faster sim) will beat it on big designs and full SystemVerilog coverage. Verilator in particular is the thing people reach for when they want speed, though it's lint/compile-to-C++ rather than a traditional event-driven simulator. Icarus's lane is: it's free, it's easy, it's everywhere in textbooks and university courses, and for medium-sized designs it does the job fine. Why you'd care: if you're dipping a toe into digital design or FPGAs and don't want to shell out for a license, this is the zero-cost on-ramp that's been quietly doing the job for two decades.

## 24. Periodic Table – detailed interactive chemistry reference - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2018/09/Chemist.jpg)

**Source:** https://www.linuxlinks.com/periodic-table-detailed-interactive-chemistry-reference/
**Karakeep doc:** `rv9s8co1974kdlk07o9a0yw0`
**GitHub:** https://github.com/komed3/periodic-table

"Periodic Table" is the open-source project behind pse-info.de, an interactive chemistry reference that goes way beyond "here's where oxygen sits." The LinuxLinks post points at `komed3/periodic-table`, developed by Paul Köhler in JavaScript/Node.js under the MIT license. It's a genuinely deep reference tool that marries the familiar periodic-table layout with a shitload of atomic, chemical, and physical data per element — not a lookup card, a real exploration tool.

The standout feature is that it folds nuclide data in alongside the conventional element info. You get an interactive table of more than 3,000 nuclides, details on each one, radioactive decay chains rendered out, plus spectral-line information for the elements. That's the kind of thing that separates a toy from an actual reference — you're not just checking atomic number and symbol, you're poking around isotope properties and how unstable nuclei fall apart. There are also property scales that reveal trends across the table, which is where the "interactive" part earns its keep: compare values, spot periodicity visually, instead of squinting at a static PDF.

Technically it's nicely done for an open-source web project. Multiple interface languages, light and dark themes, and — the part that actually matters for reuse — the underlying data is exposed as structured JSON. There's a dedicated element JSON database, a separate nuclide JSON database, and the spectral info is also available as structured data. That means you can yank the whole dataset and build your own thing on top of it without scraping the website. Tooling generates text/search indexes, a nuclide index, and decay-chain data from the source, so the whole thing is reproducible from raw data.

Why it exists among a crowded field (Kalzium, P-Table, periodic-table-cli, Nucleus, and a half-dozen other entries in the LinuxLinks roundup): this one wins on the nuclide and decay-chain depth plus the reusable JSON exports. It's less a "which element is this" tool and more a "give me the full nuclear picture of this element" tool. Why you'd care: if you ever need element or isotope data programmatically — or just want a dark-mode periodic table that'll actually tell you how an isotope decays — this is the free, MIT-licensed, self-hostable answer, and the JSON exports are the quietly killer feature.

## 25. slang – SystemVerilog compiler and language services — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/01/013-coding.png)

**Source:** https://www.linuxlinks.com/slang-systemverilog-compiler-language-services/
**Karakeep doc:** `ksj9yhns8i1dirdvys1qfnkn`
**GitHub:** https://github.com/MikePopoloski/slang

slang is a SystemVerilog frontend that actually does the whole pipeline: lexing, parsing, type checking, and elaboration. It ships as a C++ library plus a command-line tool that'll compile and statically analyze any SystemVerilog project. MIT-licensed, ~1,141 stars, 255 forks, still actively pushed as of September 2026. Michael Popoloski built it and it's the real deal for anyone in the chip world.

The pitch is speed and compliance. The README claims it's the fastest and most standards-compliant SystemVerilog frontend, judged against the open-source chipsalliance sv-tests suite. That's not marketing fluff when the incumbents are slow, proprietary commercial simulators. It's designed to not choke even on broken half-written source, which is what makes it work as an editor backend: you get clang-quality error messages while the user is mid-keystroke and the code is nonsense.

Use cases are broad. Syntax checking and linting, dumping the AST to JSON, code generation and refactoring, an editor language server, a preprocessor that sits in front of downstream tools, or even a frontend you bolt into your own simulator or synthesis tool. There are Python bindings (`pip install pyslang`) if you'd rather poke at the AST from a script than write C++.

Pre-built binaries exist for Linux, macOS, and Windows, and there's a live Compiler Explorer-style web playground at sv-lang.com. Why Wojtek cares: it's the open-source answer to a niche that's been locked behind six-figure EDA licenses forever. If you touch RTL at all, this is the frontend you actually want, not whatever your vendor shipped.

## 26. Rat Zsh – fast and reproducible Zsh plugin manager — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2023/02/147_linux_interface.jpg)

**Source:** https://www.linuxlinks.com/rat-zsh-fast-reproducible-zsh-plugin-manager/
**Karakeep doc:** `vui9zwrp7c4lq4gh8bfxgpc3`
**GitHub:** https://github.com/gotokazuki/rat-zsh

Rat Zsh is a zsh plugin manager written in Rust, and the tagline is honest: no magic, no heavy frameworks. One curl line installs the `rz` binary, one `eval` line in `.zshrc` wires it up, and you're done. Config lives in a single TOML file, which is the whole reproducibility pitch: pin every plugin to a tag, branch, or commit, sync in parallel, and you get the same shell everywhere.

The config model is clean. Each `[[plugins]]` block names a GitHub repo, a type (`source` or `fpath`), optionally a `file` to source, `fpath_dirs` for completion directories, and a `requires` list for conditional loading. That last one is actually clever: fzf-tab only loads if `fzf` is on your `$PATH`, otherwise it's skipped entirely without touching the config. Multiple plugins can come from one repo (ohmyzsh) as long as you give each a unique `name`.

It enforces load order automatically, alphabetical with zsh-autosuggestions and zsh-syntax-highlighting bumped to the end, and `rz list -u` shows update status with git-style symbols (↓N, ↑N, dirty-tree asterisks). It even handles submodules and self-upgrade via `rz upgrade`.

The catch: it's tiny. 11 stars, 2 forks, MIT, created September 2025. You'd be an early adopter on a project with basically no community yet, and GitHub is the only supported source. But the design is genuinely sane compared to antigen/zinit's spaghetti. Why Wojtek cares: if you want reproducible dotfiles without the oh-my-zsh bloat, this is the clean, boring, correct answer.

## 27. Best Free and Open Source Terminal-Based File Sharing Tools — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2022/05/Transfer_Files41021.jpg)

**Source:** https://www.linuxlinks.com/best-free-open-source-terminal-based-file-sharing-tools/
**Karakeep doc:** `mi9ns8980mkvyuas54e30p5e`

This is a LinuxLinks roundup of eight terminal-based file transfer tools, all free and open source, with the usual ratings-chart treatment. The intro is standard filler about scp and email attachments being limited, then it cuts to the actual list.

The eight: Croc (secure transfer via a relay with a passphrase-based code), Magic Wormhole (the classic library plus `wormhole` CLI, transfers via one-time codes), qrcp (send files to a phone over Wi-Fi by rendering a QR code), FTS (fast local-network transfer and communication), ffsend (Firefox Send's CLI, encrypted self-destructing links), JocalSend (a TUI reimplementation of LocalSend), e2ecp (cross-platform encrypted copy), and LocalGo (a LocalSend-compatible CLI). That's a solid spread across the two real camps: relay/cloud-based tools like Croc and Wormhole that punch through NAT, versus local-network tools like qrcp and the LocalSend clones that need both devices on the same Wi-Fi.

The useful distinction for picking one is trust model. Croc and Wormhole and ffsend encrypt end-to-end and route through a third party, so they work across networks but you're trusting a relay. qrcp and the LocalSend variants never leave your LAN, which is the right call for shoving a file from a laptop to a phone without a middleman. This is one of those "all tools, no single winner" listicles. Why Wojtek cares: the homelab already has a file-moving workflow, and one of these is almost certainly a better fit than scp-ing through an SSH tunnel every time.

## 28. Best Free and Open Source Linux GUI Typing Tutors — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2019/02/young-woman-typing-keyboard.jpg)

**Source:** https://www.linuxlinks.com/typingtutors/
**Karakeep doc:** `i8ow3ty5gltk45r35t4aqp5n`

A roundup of ten free, open-source GUI typing tutors for Linux. The preamble is the usual ergonomics sermon: touch typing uses all fingers, boosts speed, cuts RSI and carpal-tunnel risk, and lets you think about content instead of the keyboard. Then the list.

The ten tutors: Klavaro, TIPP10, KTouch, amphetype, Keypunch, Tux Typing, Open-Typer, retype, Mecalin, and FingerGo. There's real variety buried in there. Klavaro is the boring, comprehensive one with multiple keyboard layouts and progress tracking. KTouch is the KDE staple with course-based lessons. Tux Typing is the gamified option aimed at kids (and drunk adults). amphetype is interesting because it analyzes your actual typed text and drills you on your weakest keys, which is a smarter approach than rote drills. TIPP10 is cross-platform with intelligent lesson adaptation. FingerGo and retype are the newer, lighter entries, and Mecalin is aimed at speed-building with a clean interface.

What's missing from the list is any real editorial comparison beyond the ratings chart, so you're left picking by vibe: do you want adaptive training (TIPP10, amphetype), kid-friendly games (Tux Typing), or just a solid no-nonsense tutor (Klavaro, KTouch)? Also worth noting several of these are aging, with maintenance varying wildly. Why Wojtek cares: none. This is a bookmark-and-forget entry unless he suddenly decides forty is the year to finally stop hunt-and-peck typing.

## 29. Why A 50 TOPS NPU Is Almost Completely Useless — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/NPU-Blog.png)

**Source:** https://www.linuxlinks.com/why-50-tops-npu-almost-completely-useless/
**Karakeep doc:** `w87ann4jziz4w84lhblp512o`

A LinuxLinks opinion column, and the author is not impressed by the NPU marketing blitz. Intel, AMD, and Qualcomm have all slapped neural processing units into their chips, and Mini PC vendors are tripping over themselves to print "40 TOPS, 48 TOPS, 50 TOPS" on every product page like it's a flex. His verdict: for most people, and Linux users especially, you can't actually *do* anything with it.

The core problem is that TOPS (trillions of operations per second) is a theoretical ceiling for low-precision AI math, not a measure of general speed. Compile code, transcode video, render in Blender, compress files, play a game, run a database — the NPU sits there doing "absolutely bugger all," as he puts it, while at least RGB lighting has the decency to glow. Even in its intended lane, local AI inference, the story barely improves on Linux. Most inference software targets NVIDIA GPUs first, other GPUs second, and falls back to CPU; NPU support lands somewhere between "experimental" and "perhaps later."

Getting an NPU actually working is where it turns farcical. You need a specific runtime, a specific model format, a conversion tool, the right quantization scheme, and exactly matching library versions — then one unsupported operator kills the whole thing. He concedes GPUs can be finicky too, but NPUs turn running a model into an archaeological dig through GitHub issues and half-finished docs. And the "50 TOPS" number itself tells you almost nothing: what precision, which operators, what memory bandwidth, which frameworks, what *sustained* performance? It's like advertising a car by its engine RPM alone.

He's careful not to call NPUs pointless. For low-power, always-on jobs — noise suppression, speech processing, webcam effects, small vision workloads — they're genuinely good. The catch is the hardware shipped years before the software that can use it. His bottom line: he reviews hardware as it exists today, not as vendors promise it'll work two years from now. Right now a 50 TOPS NPU is a beautifully engineered room with no door. Impressive on the floor plan, useless to anyone living there. The punchline for Wojtek: your next "AI-ready" laptop probably has a chip in it that'll never run a single model you care about.

## 30. L0p4Map – network monitoring and visualization tool — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/12/117-security.png)

**Source:** https://www.linuxlinks.com/l0p4map-network-monitoring-visualization-tool/
**Karakeep doc:** `k05epkv4mu0g4s2a4y4zblor`
**GitHub:** https://github.com/HaxL0p4/L0p4Map

L0p4Map is a graphical network monitoring and topology tool for security researchers and network admins, built in Python on a modern PyQt6 interface. The LinuxLinks post is a thin stub; the real story is the repo, which is surprisingly meaty — 905 stars, 138 forks, GPL-3.0, actively maintained (last commit July 2026, now at v1.0.3).

The pitch is "Nmap was blind. L0p4Map sees." It wraps Nmap's scanning power in a clean dark UI and adds continuous discovery on top. Fast ARP-based host discovery with a local IEEE OUI database lookup; scans individual IPs, CIDR ranges, and routed networks. Routed ranges get mapped via traceroute, grouping hosts under their last-hop router. Hostnames resolve through reverse DNS, NetBIOS, and mDNS/Avahi, and devices get fingerprinted by TTL (to hint at OS), open ports, vendor data, and raw SNMP sysDescr queries — no external libraries needed.

Where it stands out is the interactive topology. It auto-classifies every host (gateway, router, AP, switch, PC, Apple, mobile, Raspberry Pi, VM) and draws a real hierarchical graph with the gateway at the top, intermediate gear on a second tier, and clients grouped below their parent. Subnets get drawn as dashed bounding boxes labeled with their CIDR, and links are color-typed as uplink, backbone, or client. Toggle between Hierarchical and Force Atlas layouts.

Security-wise it goes beyond discovery: full Nmap integration (SYN, UDP, OS detection, service versioning, NSE scripts), banner grabbing for HTTP/SMB/FTP/SSH/SSL, and CVE lookup via vulners. The Attack Surface view lists exposed services, open ports, and CVEs per host with CVSS scores and direct NVD links, exportable to CSV. It even flags devices known to ship with default creds (iLO, InfoPrint, XPort, SATO, Zebra) for manual verification.

The monitoring angle is the other differentiator: a continuous-monitoring daemon passively watches ARP and mDNS traffic and alerts on new/unauthorized devices, plus periodic SNMP polling to keep status fresh without rescanning. A real-time traffic analyzer captures packets with per-device stats, protocol coloring, and a filter bar. Runs on Linux, Windows, and macOS. Legal disclaimer is blunt: authorized network auditing only. If Wojtek wants a self-hosted, pretty nmap frontend with live topology, this is a genuinely solid pick over Zenmap.

## 31. 5 Best Free and Open Source Threat Intelligence Platforms — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2023/08/people-holding-cloud-network-security-symbols.jpg)

**Source:** https://www.linuxlinks.com/best-free-open-source-threat-intelligence-platforms/
**Karakeep doc:** `slxjgns5eoyebbuh8iqp8ih7`

A LinuxLinks roundup of free/open-source threat intel platforms, aimed at SOCs, incident response teams, threat hunters, malware analysts, and researchers who are tired of juggling indicators across scattered feeds and tools. The pitch: one central place to build context around malicious domains, IPs, files, vulns, threat actors, and campaigns.

The five picks approach the problem from different angles, and that spread is the useful part. **IntelOwl** automates enrichment and analysis across a broad range of threat sources — you throw an indicator at it and it queries a pile of external services to add context. **OpenCTI** (Community Edition) connects threat data into a searchable intelligence graph, linking indicators, actors, campaigns, and techniques. **MISP** is the sharing-and-correlation workhorse — the de facto standard for exchanging actionable threat intel between orgs. **Yeti** builds richer investigations from indicators, entities, and their relationships. **ThreatDeck** is the lighter-weight option, monitoring intel feeds and surfacing meaningful changes quickly.

The useful framing: together they cover the whole threat-intel workflow, from raw collection through enrichment and correlation to investigation, sharing, and ongoing monitoring. The roundup isn't a "one best tool" verdict — it's a "which shape fits your team" breakdown. If you're standing up intel sharing with other orgs, MISP. If you want a knowledge graph, OpenCTI. If you just want automated enrichment, IntelOwl. For Wojtek the takeaway is that this whole category is genuinely well-served by FOSS — no need to pay Recorded Future prices to get a functional intel pipeline, though you'll be assembling several pieces yourself rather than buying a turnkey platform.

## 32. ACIAH-Linux - accessible Linux Mint-based distribution — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/04/Linux-Distributions.png)

**Source:** https://www.linuxlinks.com/aciah-linux-accessible-linux-mint-based-distribution/
**Karakeep doc:** `mmd9bqw80ec9dzd6detwksge`

ACIAH-Linux is a Linux distro aimed at people who find conventional desktops hard to use — blind and visually impaired users, people with motor difficulties, seniors, and total newcomers. It's built by the Association ACIAH (France), home page aciah.xyz, and it layers an accessibility-first experience on top of Linux Mint Xfce, so it inherits Mint's package ecosystem and APT management while reworking the interface around simplicity.

The design philosophy is "fewer actions per task." ACIAH-Menu is a simplified, keyboard-driven route to common apps and actions, and there's a dedicated "Heart key" that opens the main menu with a single press — a nice touch for someone who can't handle multi-key combos. It ships the Orca screen reader for spoken feedback and accessible navigation, plus simplified shortcuts and scripts that replace fiddly multi-key operations, and one-key actions for people with restricted movement.

Beyond the core desktop it bundles tools for reading text aloud, working with audiobooks, decompressing files, and a scanner workflow that turns scanned documents into PDFs and images. You can install it to a drive, dual-boot alongside another OS, or carry it as a bootable USB. There are two config flavors: a simplified one and a vocalized one, to suit different accessibility needs.

It's a niche but genuinely useful entry in the "Linux for everyone" space, sitting alongside distros like Slint and Accessible-Coconut that target low-vision users. The tradeoff is the usual one for specialized distros — a smaller community and slower updates than upstream Mint — but for someone who needs speech-first, keyboard-first computing out of the box, it's a thoughtful, actively-maintained option (working state: Active, x86_64, fixed release).

## 33. Dissect – digital forensics and incident response framework — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2019/04/closeup-fingerprint-glass-against-dark-background-modern-technology-biometrics.jpg)

**Source:** https://www.linuxlinks.com/dissect-digital-forensics-incident-response-framework/
**Karakeep doc:** `lbbowhw8dcjppqz99stc0gxw`
**GitHub:** https://github.com/fox-it/dissect

Dissect is a DFIR framework from Fox-IT, the incident-response arm of NCC Group, and it's the kind of tool that makes you wonder why everyone still does forensics the slow way. The pitch is dead simple: one consistent interface to poke at forensic evidence no matter what the disk image, filesystem, or OS looks like underneath. Instead of the usual misery of extracting files from a container, mounting a VMDK, pulling the MFT, and running a separate parser just to build a timeline, you point `target-query` or `target-shell` at an image and it handles all that plumbing for you.

Under the hood it's a modular Python framework, so every parser and format implementation is its own reusable project. The meta package on PyPI (`pip install dissect`) just bundles ~30 of those modules with compatible versions. Coverage is broad: evidence containers E01/VMDK/QCoW, filesystems NTFS/ExtFS/APFS/Btrfs/FFS/XFS/VMFS, plus artefact parsers for Windows Registry, Prefetch, and Event Logs. It also ships `acquire`, a tool you deploy on an endpoint or hypervisor to grab a lightweight container of a machine (or every running VM on it) without fighting file locks, then feed those into the same `target-*` tooling. Windows, Linux, and ESXi all get the same abstraction.

License is AGPL v3.0, which is the one wrinkle: it's open source but copyleft-strong enough that commercial vendors can't just vacuum it up and close the door. Stars sit around 1.2k with 89 forks, last release 3.22. For anyone doing incident response on Linux or Windows boxes who's tired of the manual mount-and-parse grind, this is worth a hard look. 🕵️

## 34. TVDemon - IPTV streaming application — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/02/053-smart-tv.png)

**Source:** https://www.linuxlinks.com/tvdemon-iptv-streaming-application/
**Karakeep doc:** `a50lkhxpf3bbspzpintvd4ji`
**GitHub:** https://github.com/DYefremov/TVDemon

TVDemon is an IPTV player forked from Linux Mint's Hypnotix, and the whole point of the fork is a modern GUI rewrite. The author swapped the old interface for GTK4 and Libadwaita and put GStreamer in charge of playback. It's a pure client: it doesn't sell you channels or subscriptions, it just connects to whatever IPTV providers you already have, via M3U URLs, the Xtream API, or local M3U playlists. It ships preconfigured with one provider called Free-TV (github.com/Free-TV/IPTV) but you can rip that out and add your own.

Feature list is what you'd expect from a serious player: EPG display when a channel publishes programme data, favourites, an optional viewing history on the start page, local stream recording, and a readout of the codec info for whatever's playing. UI is localized into English, German, Belarusian, and Russian. There's experimental macOS and Windows support, which is a nice touch for a tool that started as a Mint thing. Requirements are Python >= 3.12, Gtk4 >= 4.12, Libadwaita >= 1.5, and PyGObject. Packaging is all there too: a deb build script, an Arch PKGBUILD, and an Ubuntu PPA.

It's a solo project, GPLv3, 26 stars and 6 forks, with a 2.0.0 beta out and 17 releases total. Don't expect a team behind it, but as a clean GTK4 IPTV client with recording and EPG it's more than most of the alternatives in this space manage. If Hypnotix's interface ever felt dated, this is the fixed-up version. 📺

## 35. 9 Best Free and Open Source Zsh Configuration Frameworks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2023/02/147_linux_interface.jpg)

**Source:** https://www.linuxlinks.com/best-free-open-source-zsh-configuration-frameworks/
**Karakeep doc:** `liy68t1w0cns6u8m1bujjedq`

This is a roundup, not a single project, so there's no one repo to summarize. The thesis is straightforward: Zsh is a genuinely strong shell (tab completion, regex integration, automated file searching, a rich theme engine), but wiring up plugins and themes by hand is a pain in the arse, so you should run a framework that handles config, plugins, and themes for you. The piece ranks nine candidates with a LinuxLinks-style verdict chart.

The obvious headliner is Oh My Zsh, the hugely popular community-driven framework that basically defined the category, though it's also notorious for slow startup once you pile on plugins. Oh My Posh shows up too, but it's really a cross-shell prompt theme engine rather than a Zsh config framework per se. Prezto is the faster, leaner alternative to Oh My Zsh. Zim brings modules, themes, and customizability. Znap is pitched as easy-to-use tools. Zi bills itself as the Swiss Army Knife. Then come the lighter ones: slimzsh, a small usable config; Zephyr, a lightweight modular framework for a fast setup; and AX-ZSH, a flexible modular configuration system for a tailored environment.

For Wojtek's purposes the takeaway is the speed vs. features tradeoff: Oh My Zsh is the safe default and has the most plugins, but if your prompt lag is driving you up the wall, Prezto or Zim (or a hand-rolled Zephyr setup) will boot noticeably faster. It's a fine cheat-sheet to skim next time the shell feels slow. 🐚

## 36. FangOS - Arch-based KDE Plasma Linux distribution — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/04/Linux-Distributions.png)

**Source:** https://www.linuxlinks.com/fangos-arch-based-kde-plasma-linux-distribution/
**Karakeep doc:** `rh0e594xtifbru57qkhbdo7g`

FangOS is an Arch-based distro that slaps the KDE Plasma desktop on top of a rolling-release Arch foundation, aiming for a ready-to-use system without giving up Arch's package ecosystem and rolling model. This one's a thin entry, written with help from a visitor who filled out the distro submission form, so the detail level is lower than LinuxLinks's usual feature writeups.

Concrete facts: it ships as a live image with the Calamares graphical installer, targets standard x86_64 PCs, and supports both UEFI and legacy BIOS boot. Init is systemd, package management is Pacman, release model is rolling. The developer is a single person going by "Kiefer", and the whole project — ArchISO profile, custom packages, branding, and installer config — lives in a public GitHub repo, with the home page at kiefer-d-hendricks.github.io/FangOS. It includes some project-specific tooling and presentation rather than just shipping a stock Arch install.

The honest verdict: this is an active but small single-maintainer distro. It's yet another "Arch with KDE on top" in a space that's already crowded with EndeavourOS and Manjaro doing the same thing at much larger scale. Interesting if you want to see how one person assembles an ArchISO-based distro, but there's no killer feature here to justify switching off the bigger names. The rolling Arch base means you inherit both the freshness and the occasional breakage. 🤷

## 37. fzf-make - fuzzy command runner for project tasks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/01/019-coding-3.png)

**Source:** https://www.linuxlinks.com/fzf-make-fuzzy-command-runner-project-tasks/
**Karakeep doc:** `l7kz81g3hh1gwtupxv8cqbn4`
**GitHub:** https://github.com/kyu08/fzf-make

fzf-make is a Rust CLI that wraps the project task runners you already use in a single fuzzy-finder TUI, built on Ratatui. The pitch: stop grepping Makefiles and package.json files from memory; run `fzf-make` and pick your target from a preview-window list with a couple of keystrokes. It covers six runners, not just make — GNU make, npm, pnpm, Yarn, just, and Task — and it doesn't invent its own task format, it shells out to the underlying tool. That's the right call, because nobody wants yet another task DSL to learn.

The feature list is genuinely thoughtful rather than checkbox filler. It understands make's `include` directive, so targets split across included files still show up. For npm/pnpm/Yarn it collects workspace scripts from every package.json in the tree (npm via `npm query`, which requires npm >= 8.16.0). It reads Task's structured JSON output to discover tasks, including included Taskfiles, and needs Task v3.44.0+ for that. There's a command-history pane, a `--repeat` flag to rerun the last command without re-opening the picker, and a popup for passing extra args before execution. You can also copy the selected command to the clipboard instead of running it, which is handy for pasting into a terminal you actually trust.

Caveats worth flagging. It's a solo-ish project from Tatsuya Kyushima, MIT-licensed, sitting at 299 stars and 19 forks with active Renovate-bot maintenance — healthy but not huge, so don't expect an enterprise support contract. Config-file support is explicitly still "scheduled to be developed," meaning for now the behavior is whatever the defaults give you. And the fuzzy preview is only as good as your runner's own introspection; if a Makefile does something weird with generated targets, fzf-make inherits that weirdness.

Why Wojtek cares: if you're already living in make/npm/just/task land and hate remembering target names, this collapses six mental lookups into one. Install it, alias `fm='fzf-make'`, and it's the fastest way to browse a project's actual entry points without opening the files. It's a quality-of-life tool, not a revolution, but the kind that quietly pays rent every day.

## 38. Syft - generate Software Bills of Materials — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/SBOM-Tools-banner3.png)

**Source:** https://www.linuxlinks.com/syft-generate-software-bills-materials/
**Karakeep doc:** `wfgw42xsyyyxem4hbtxujohv`
**GitHub:** https://github.com/anchore/syft

Syft is Anchore's Go tool for generating Software Bills of Materials, and it's the de facto standard for the job — 9.6k stars, 959 forks, and a commit landed three hours ago as I write this. It inventories every package in a target (container image, filesystem, or archive) and emits a machine-readable SBOM you can feed into compliance reports or downstream scanners. The key design point: it's ecosystem-agnostic, understanding Alpine, Debian, and RPM-based distros plus Go, Python, Java, JavaScript, Ruby, Rust, PHP, and .NET, rather than being tied to one language.

Output formats are where it earns its keep. It produces CycloneDX and SPDX — the two SBOM standards that actually matter — plus its own detailed Syft JSON. You can emit several formats from a single scan, and it can even convert between SBOM representations. It integrates directly with Grype, Anchore's vulnerability scanner, so the natural workflow is Syft first to build the SBOM, then Grype to find the CVEs in it. It can also create signed SBOM attestations using the in-toto specification, which matters for the software-supply-chain crowd that now has to prove provenance.

Beyond the headline features, the engineering is the real story. It handles OCI, Docker, and Singularity image formats, can inspect a local directory without building a container image first, and ships as both a CLI and a Go library you can embed. Configuration comes through files, env vars, or CLI flags, so it drops into CI/CD cleanly. It's Apache-2.0 licensed and sponsored by Anchore (the security vendor), which is both a strength — real funding, real maintainers — and a caveat: the commercial upsell path exists for a reason.

Why Wojtek cares: if you're running anything in containers and give a single shit about supply-chain security or SBOM compliance (and you should, given how often CVEs now come bundled in a base image), Syft is the tool you reach for first. It's not a nice-to-have, it's the boring, correct default. Pair it with Grype and you've got a vulnerability pipeline without buying Anchore Enterprise.

## 39. inperiod – interactive periodic table and element reference — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2019/10/alchemist-table-production-magical-potions-elixir-colored-bottles-flasks-are-table-alchemist-wizard-fantasy-fairy-tale-3d-illustration.jpg)

**Source:** https://www.linuxlinks.com/inperiod-interactive-periodic-table-element-reference/
**Karakeep doc:** `vaebgc88mdi4mp818tnlsmko`
**GitHub:** https://github.com/mhfan/inperiod

inperiod is a periodic table with a very specific itch to scratch. Its author, MeiHui FAN, looked at the dozens of periodic tables already online — web pages, spreadsheets, static images, mobile apps, even Python-generated ones — and found none of them did everything he wanted. The gaps he cared about: showing periodic *trends*, not just names and numbers; Chinese element names with pinyin; and layouts that still look good when printed on A4/A3 paper for sixth and ninth graders to actually study from.

It's built with Dioxus, the Rust UI framework, so the same codebase targets browser (via WebAssembly), desktop, and mobile. That's a nice trick — write the logic once in Rust and ship it three places — but it also means the project is more of a personal labor-of-love than a mature product. The GitHub numbers tell that story bluntly: 2 stars, 0 forks, 1 watcher, and the last commit was ten months ago (November 2025), bumping Dioxus to v0.7. That's a one-person hobby repo, not something with a community behind it.

The data layer is genuinely respectable, though. It pulls from authoritative sources — NIST, IUPAC, and CIAAW — and there's tooling for synchronizing external scientific data into the project, so atomic weights and element info stay current rather than rotting. The features are surprisingly deep for a niche tool: flame-test visualizations, electron-configuration diagrams, crystal-structure info, cosmic-origin data, abundance diagrams, and even an optional representation of the Standard Model. Plus it exposes the element data as a reusable Rust API, so you can program against it.

The honest caveat is the maintenance cadence and the tiny user base. MIT *or* Apache-2.0 licensed, which is generous, but a repo that commits once a year isn't something you'd build a curriculum on without forking it. Still, the niche it fills — a Chinese/English bilingual periodic table that prints well for students and visualizes trends — is real, and it's live at mhfan.github.io/inperiod.

Why Wojtek cares: this is niche as hell, but if you have kids studying chemistry (or just want a periodic table that shows trends instead of just symbol soup) it's a clever little Rust/Dioxus project worth a glance. Don't expect a thriving ecosystem — expect one motivated person who wanted a better periodic table and built it.
