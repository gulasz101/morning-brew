---
date: 2026-10-13
slug: 2026-10-13-morning-brew
tags: Git, Command Line Tools, Data Visualization, Productivity, Open Source Software, Cybersecurity, Artificial Intelligence, Programming, Software Development, Content Creation, C++ Programming, Web Development, Linux, Open Source
---

# Morning Brew — 2026-10-13

36 things landed in yesterday's hoard: 6 videos, 30 articles and posts. The heavy stuff is engineering — two Cloudflare deep-dives on hardware life extension and D1's control plane, plus Linus Torvalds using AI to make sense of the kernel's array code. The listicles are LinuxLinks as usual: security testing tools, 22 ham radio apps, 14 JavaScript linters. And one self-hosted app directory got hoarded four separate ways, which is either thorough or a cry for help. On the videos: Craft Computing on broken office promises, Alex Ziskind timing a coding agent that says nothing for 19 seconds, Brodie Robertson on Artcraft cloning Adobe and Office, Better Stack twice (an F1 production incident and modding any game with Claude), and Theo on Meta catching up with Anthropic. Meta's press desk also shipped three announcements, now with the appropriate amount of sarcasm attached. 🍺

### Hand-bookmarked

## 1. COSMIC Desktop 1.9 Adds COSMIC Viewer, On-Screen Keyboard — by Linuxiac

![Linuxiac](https://linuxiac.com/wp-content/uploads/2026/09/cosmic-desktop-19.jpg)

**Source:** https://linuxiac.com/cosmic-desktop-1-9-adds-cosmic-viewer-on-screen-keyboard/
**Karakeep doc:** `ytl9c10jnn80tzbej3tkfca3`

System76 pushed COSMIC Desktop 1.9, and the headline is two new Rust apps. First is COSMIC Viewer, an image viewer that handles a wide range of formats and ships with built-in editing, now recommended as the desktop's default image opener. Second is COSMIC OSK, an on-screen keyboard built for touchscreens and gamepad input, with its own panel applet, dedicated settings, and lock-screen support. COSMIC Store got a visual once-over that finally puts developer names on the app cards, so you can tell who actually made the thing you're about to install. Under the hood, the lock screen can now use COSMIC's own background component, and the compositor can draw layer-shell apps — the OSK included — on top of the lock screen. That combination is the real story if you care about handhelds and tablets, not the image viewer. Plenty of long-standing annoyances got fixed too: context menus in the app library and launcher, the Super key that used to stick after opening the launcher, and Escape failing to close menus. COSMIC Files got fixed drag-selection, Windows `.exe` icons, persistent sort order in dialogs, and better Shift context menus. Settings now shows the installed COSMIC version, configures the OSK, fixes WireGuard, adds a "show day of the week" toggle, and syncs fonts with GNOME apps. Panel border thickness is configurable, notifications behave under Do Not Disturb, and the greeter gained optional systemd-homed support. Packages are landing in Arch, openSUSE Tumbleweed, and CachyOS shortly; Pop!_OS 24.04 LTS users already have it. The caveat: this is 1.9 while a 1.10 release and aerynOS bundling it already showed up. Version churn is real, and the changelog is a wall of small fixes rather than one dramatic feature. Still solid incremental work on a desktop that's maturing fast.

## 2. Linus Torvalds "Did What I Preach", Used AI To Make Code Decipherable & Uncovered More Bugs — by Phoronix

![Phoronix](https://www.phoronix.com/favicon.ico)

**Source:** https://www.phoronix.com/news/Linus-Torvalds-Assoc-Array
**Karakeep doc:** `e6hpxexef2kwos4quqg58t9g`

The JSON title was a Cloudflare interstitial; the real headline is that Linus Torvalds used LLMs again and is talking about it. An `assoc-array-fixes` git tag appeared in his tree on Sunday with a blunt explanation: Nils Ollrogge reported a bug in the kernel's associative array library and even sent a patch, but the code was "too obscure for me to follow." So Linus did what he preaches and handed it to modern LLM tools. The result is an LLM-assisted branch that makes the code readable by splitting up some of the larger, hard-to-follow functions. He then ran tests in user space, which confirmed Nils's original bug and turned up three more — all going back to the very first commit that added the library back in 2013. Three decade-old bugs found while a machine was just tidying up the formatting is the actual prize here. This follows a separate branch, `noref-filemap-read-with-llm`, where he used Claude Code to draft a real I/O improvement. None of it is merged yet; it's expected to get punted to the Linux 7.4 merge window. The context matters: kernel developers are already planning to drop the "Assisted-By" tag requirement for AI/LLM usage, and Torvalds keeps getting louder about treating the tools as legitimate. The irony is hard to miss — the man who spent decades telling everyone their code should be readable now needs an LLM to read `assoc_array`. The counterpoint worth holding onto is that the AI work was refactoring plus bug-hunting, not novel design, and the three old bugs are the reason this branch exists at all. Forty-two comments, presumably spicy.

## 3. I asked ChatGPT to build me a $1,000 effects pedal. Here's what it did — by New Atlas

![New Atlas](https://assets.newatlas.com/dims4/default/cd87d2a/2147483647/strip/true/crop/2000x1050+0+225/resize/1200x630!/quality/90/?url=https%3A%2F%2Fnewatlas-brightspot.s3.ap-southeast-2.amazonaws.com%2F66%2F43%2F1627ef07475789d6ee70ecd1146a%2Fchatgpt-pipedal-header.jpg)

**Source:** https://newatlas.com/technology/chatgpt-build-a-1-000-effects-pedal/
**Karakeep doc:** `hwvjo7utte3rnybtqyz6s2iz`

New Atlas's Howard Armitage wanted a serious multi-effects pedal, then remembered the wife test and went looking for a cheaper route. He landed on PiPedal, a free open-source platform that turns a Raspberry Pi 4 or 5 into a multi-effects unit. PiPedal 2.0 talks straight to TONE3000, a huge library of Neural Amp Modeler captures — digital clones of real amps, cabs, pedals, and whole signal chains — alongside the usual reverb, delay, chorus, compression, EQ, distortion, and pitch-shift plugins.

The interesting bit isn't the hardware. Instead of days in Linux audio docs, he told ChatGPT to use Desktop Commander and "turn the RasPi on my network into a PiPedal." It downloaded, installed, configured, diagnosed failures, and tweaked settings. A couple of hours later he had song presets, amp and cab combos, effect chains, an iPad touch UI, and a six-button MIDI footswitch. NAM's new Architecture 2 also cuts CPU load by roughly 30–40% versus its predecessors.

Caveats, and he's honest about them: it isn't a rugged commercial pedal, one tiny guitar-brand audio interface misbehaved until he swapped in a bigger Arturia unit, and the web UI "has a faint whiff of Geocities." He wouldn't trust it on a 20,000-person stage yet, but would take it to a studio tomorrow. Total spend was about $100 on a footswitch, running on hardware he already owned. My slice carried no repo or project URL for PiPedal, so there's no Project line on this item. The real story is that AI paid the knowledge toll that used to gate projects like this. 🎸

## 4. tortuvshin/open-apps: A curated, self-refreshing directory of real open-source application codebases — by GitHub

![GitHub](https://repository-images.githubusercontent.com/101770883/7d244600-1b34-11ea-95ba-2e75f4c98d2f)

**Source:** https://github.com/tortuvshin/open-apps
**Karakeep doc:** `j981asa0j049ipfmkn61sbcx`
**Project:** [Open App Scout](https://github.com/tortuvshin/open-apps) — hand-picked directory of real open-source applications, self-refreshing via weekly GitHub metadata syncs.

Open App Scout is another "awesome list", except this one has opinions and a build pipeline. It's a hand-picked directory of real open-source applications — the README hammers on "not tutorials, boilerplates, or package-only libraries" — aimed at developers who want to study production code or find something worth contributing to.

Each entry is one human-curated markdown file in `content/records/`, and the catalog is kept fresh by weekly GitHub metadata syncs that land as reviewable pull requests. Adding an app goes through a web form that fetches the repo, asks a few questions and opens a PR with a single file. The list in the README is generated from the records with `grove readme generate`, so you edit data, not the README.

The repo has real traction: 4.4k stars, 829 forks, 663 commits. Content spans Productivity, Finance, Tools, Dev Tools, Media, Games and more. The site is built with Grove on Astro and Tailwind, deploys static to Cloudflare, and publishes `llms.txt` and `llms-full.txt` so AI assistants can read the catalog. It grew out of the older open-source-flutter-apps list, now preserved as README-LEGACY. Requires Node 22.12+ and pnpm; MIT licensed.

Caveat: "curated" means one person's taste, and "self-refreshing" still means PRs and a maintainer who shows up. 📚

## 5. A hand-picked directory of real open-source apps worth running and studying — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/tortuvshin/open-apps)

**Source:** https://www.opensourceprojects.dev/post/open-apps
**Karakeep doc:** `lyq8bwcxujbcx1gi3nk044h9`
**Project:** [tortuvshin/open-apps](https://github.com/tortuvshin/open-apps) — a curated, self-refreshing directory of real open-source app codebases you can run, study and contribute to

GitHub search is a dumpster fire when you don't already know the repo name: type "self-hosted notes" and you drown in boilerplates, dead tutorials and libraries pretending to be apps. Open App Scout is a hand-picked directory built for the other case: browsing for something that actually runs. Every entry is one human-curated Markdown file under `content/records/`, and the metadata re-syncs from GitHub weekly. That week-by-week refresh is why it doesn't rot like your average awesome-list from 2019. It splits into 15 categories (Productivity, Finance, Developer Tools, Media, Education and so on), and each listing gives a short description, a dedicated page and a link to the source repo. The bar is explicit: real deployable apps, not starter templates or package-only libraries. Look at Productivity alone: AFFiNE (local-first docs, whiteboard and databases on one canvas), AnythingLLM (chat with your own documents), anarlog (a local meeting notepad that never joins the call as a bot), Authier (an experimental encrypted password manager). That's a real spread, not ten clones of one idea. Descriptions are honest about licensing where it matters: Baserow is flagged open-core with an MIT community edition. The repo sits at github.com/tortuvshin/open-apps, roughly 4.4k stars, built in Astro. Adding an app is editing one file or using the submit form. Caveat: it's still small and leans mobile/Flutter, so pure server-side people will scroll past chunks of it. Still beats burning an afternoon in search results. 🗂️

## 6. Open App Scout — 204 open-source apps (full list) — by Open App Scout

![Open App Scout](https://openappscout.com/favicon.ico)

**Source:** https://www.opensourceprojects.dev/post/open-apps
**Karakeep doc:** `qfw0570vql13jcg7anc07jfx`
**Project:** [Open App Scout](https://github.com/tortuvshin/open-apps) — curated, self-refreshing directory of real open-source apps (204 entries, Astro-built)

Someone hoovered the entire Open App Scout directory into one bookmarked list: all 204 apps, grouped by category, synced from the GitHub dataset at github.com/tortuvshin/open-apps. The split is blunt — Productivity 82, Developer Tools 37, Tools 28, Business 17, Finance 12, Media 10, Communication 6, and a thin tail of one-off categories. Those leftovers are Education, Entertainment, Games, Social Network and News & Magazine, one or two apps each. Some names are already living on the home server: Immich, Karakeep, Linkwarden, WeKan, Plausible Analytics, Umami. The interesting half is the rest — OpenHands and Goose for coding agents, PocketBase and Supabase for backends, ComfyUI and Invoke for image generation, BlueWallet and MetaMask Mobile for crypto, Keycloak for auth, Zed for an editor with actual opinions. A big chunk of the mobile entries are Flutter or React Native. That tells you exactly where the maintainer's taste sits. Every line pairs a one-sentence description with a source repo, so it works as both a discovery list and a reading list for production code. Caveat: it's a snapshot, and "real app" still includes plenty of weekend-project energy. The curation bar beats raw GitHub search, it doesn't perfect it. Handy when you want to self-host something or steal architecture ideas. 📚 Repos below for the notable ones; the other ~185 sit behind the directory's own search.

**Projects:**

- **[Immich](https://github.com/immich-app/immich)** — Self-hosted photo and video library with mobile backup, timeline, and shared albums.
- **[Karakeep](https://github.com/karakeep-app/karakeep)** — A self-hostable bookmark-everything app (links, notes and images) with AI-based automatic tagging and full text search.
- **[Linkwarden](https://github.com/linkwarden/linkwarden)** — Self-hosted collaborative bookmark manager to collect, read, annotate, and fully preserve what matters, all in one place.
- **[WeKan](https://github.com/wekan/wekan)** — FLOSS kanban board, built with Meteor
- **[Plausible Analytics](https://github.com/plausible/analytics)** — privacy-first, cookie-free web analytics — a lightweight Google Analytics alternative
- **[Umami](https://github.com/umami-software/umami)** — Umami is a privacy-first analytics platform. Traffic, campaigns, behavior, conversions, and revenue in one place — no cookies, no surveillance, self-hosted or in the cloud.
- **[PocketBase](https://github.com/pocketbase/pocketbase)** — Open Source realtime backend in 1 file.
- **[Supabase](https://github.com/supabase/supabase)** — The Postgres development platform. Supabase gives you a dedicated Postgres database to build your web, mobile, and AI applications.
- **[Keycloak](https://github.com/keycloak/keycloak)** — Open Source Identity and Access Management For Modern Applications and Services.
- **[Zed](https://github.com/zed-industries/zed)** — Code at the speed of thought – Zed is a high-performance, multiplayer code editor from the creators of Atom and Tree-sitter.
- **[ComfyUI](https://github.com/Comfy-Org/ComfyUI)** — node-graph GUI and backend for diffusion models — the local-inference workhorse
- **[Excalidraw](https://github.com/excalidraw/excalidraw)** — Virtual whiteboard for sketching hand-drawn like diagrams.
- **[AFFiNE](https://github.com/toeverything/AFFiNE)** — next-gen knowledge base — docs, whiteboards and databases on one canvas; open-source Notion/Miro alternative
- **[AppFlowy](https://github.com/AppFlowy-IO/AppFlowy)** — open-source Notion alternative — projects, wikis and AI-assisted workspaces you host yourself
- **[AnythingLLM](https://github.com/Mintplex-Labs/anything-llm)** — Stop renting your intelligence. Own it with AnythingLLM. Everything you need for a powerful local-first agent experience.
- **[Baserow](https://github.com/baserow/baserow)** — Build databases, automations, apps & agents with AI — no code. Open source platform available on cloud and self-hosted. GDPR, HIPAA, SOC 2 compliant. Best Airtable alternative.
- **[Joplin](https://github.com/laurent22/joplin)** — Joplin - the privacy-focused note taking app with sync capabilities for Windows, macOS, Linux, Android and iOS.
- **[Plane](https://github.com/makeplane/plane)** — Open-source Jira, Linear, Monday, and ClickUp alternative. Plane is a modern project management platform to manage tasks, sprints, docs, and triage.
- **[Rocket.Chat](https://github.com/RocketChat/Rocket.Chat)** — self-hosted team communication platform — chat, channels, federation, omnichannel
- **[OpenHands](https://github.com/OpenHands/OpenHands)** — AI-driven development agent platform (formerly OpenDevin)

## 7. Open Source Apps & Production Codebases — by Open App Scout

![Open App Scout](https://openappscout.com/og/home.png)

**Source:** https://openappscout.com
**Karakeep doc:** `v1nib2li99xb40yhrrywsdx7`

Open App Scout's own site, which is where the article above points. It's an Astro-built directory indexing 205 apps across 15 categories, 7 stacks and 196 owners. The headline numbers are about 3.35 million stars in total and 4.4k stars on the GitHub repo behind it. The framing is "apps you can run, study and contribute to," and the filters match: browse by stack (Flutter 45, native iOS 27, React 26, Tauri 17, React Native 14, JavaScript 9, Svelte 2), by category (Productivity 81, Developer Tools 39, Tools 28, Business 17, Finance 12), or by platform, activity and maturity. The curated collections do the real work: trending, recently added, most starred, actively-maintained Flutter apps, cross-platform mobile, and open-source Airtable alternatives. A sample from the recent bucket: MangoDisk (macOS/Windows disk cleaner), OpenMausBot (turns local Claude, Codex and Grok CLIs into a bot roster), SolidPing (single-binary uptime monitor on SQLite), akou (on-device call recorder for Apple silicon), Orbi (turns GitHub issues into reviewed PRs). Every app page states license, platforms and architecture, and there's search plus a submit form. Caveats: it's an index, not a review site. No word on how well any of it actually runs, and the mobile-heavy mix won't suit everyone. The page links its repo at github.com/tortuvshin/open-apps; the bookmark's own metadata carries no project URL. Good starting point for self-hosting ideas. 🧭

## 8. HK’s manpower shortage to narrow to 130,000 by 2028 as AI boosts productivity — by The Standard 英文虎報

![The Standard 英文虎報](https://image.hkstandard.com.hk/f/1200p0/0x0/100/none/97b7f2bb54aa96b3815187e56a3f98a7/2026-10/WhatsApp_Image_2026-10-13_at_1_51_31_PM.jpeg)

**Source:** https://www.thestandard.com.hk/news/article/345322/HKs-manpower-shortage-to-narrow-to-130000-by-2028-as-AI-boosts-productivity
**Karakeep doc:** `q7jm7o93kuh59x15tl6dwu3r`

Hong Kong's government now projects its overall manpower shortage will shrink to roughly 130,000 by 2028. The stated reason is AI. Roy Chan Kwok-fai, who heads the Labour and Welfare Bureau's research unit, says economic restructuring plus AI adoption will lift productivity and slow growth in labour demand. He reckons 60 percent of the remaining vacancies will be frontline roles (service and technical staff) across city operations, healthcare, international innovation and technology, and international aviation. On the jobs that still exist, the official line is reassuring. The chance of major layoffs over the next three years is "relatively low." The fine print is less soothing: 20 to 30 percent of positions could see their scope of work change, which is a polite way of saying job descriptions get rewritten around whatever the model can do. Chan cites research that 90 percent of enterprises plan to fold AI into daily operations. He predicts SMEs will adopt it faster and faster, breaking development barriers and creating new opportunities. That last part is government optimism in its purest form. A "narrower shortage" can mean more workers, or it can mean fewer jobs left to fill. The release never quite says which. Watch the frontline 60 percent; that's where the reshuffling actually bites. 🤖

### RSS — YouTube

## 9. Where’s The New Office You Promised? — by Craft Computing

![Craft Computing](https://i.ytimg.com/vi/h8BSzwW8M1o/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=h8BSzwW8M1o
**Karakeep doc:** `kfxrw7v647wjqae6dfmghla8`

Jeff from Craft Computing opens with a confession: it's been about two weeks since his last video, closer to three since he shot it, and the question everyone keeps asking is where the hell the studio he promised actually is. Short answer — he's building one. Long answer — it's not the studio he wanted, and the math is why.

Three-plus years ago he pitched an almost-thousand-square-foot, two-story build over his garage: makerspace, CNC, laser cutters, production space, storage. He figured maybe thirty grand doing the labour himself. He made a video, sold "bricks" to viewers for the studio wall, and raised roughly eight thousand dollars. He lined up another twenty thousand in financing, expecting about twenty-eight total. Then permitting ran into winter and the project slid to spring. By spring, materials alone had jumped over ten thousand dollars, so he was already ten grand short before a single wall went up.

Meanwhile YouTube changed. Shorts arrived and the algorithm tilted hard toward them, and Jeff doesn't make shorts. His views "flat out tanked," sponsors stopped signing up, and revenue not only flatlined but receded over two to three years. He burned the twenty-thousand loan keeping the channel alive — paid it off eventually — and the brick money just sat there with no project to spend it on. This summer he got a fresh quote: the studio he wanted now lands near seventy-five thousand dollars, for a building that three years ago was under thirty.

So he scaled down. He's moving out of his two-hundred-square-foot office into 168 square feet carved out of his garage — essentially sixteen by twelve, with two exterior walls and two shared with the garage. A family of six forced the move; a herd of elephants lives above his current desk. He gutted seven years of garage hoard into a storage unit, then framed, insulated, and wired the new room himself.

The build is brutally budget. Wall finish is cheap laminate wood flooring at ninety-nine cents a square foot — about double drywall's fifty cents, but no taping, sanding, or painting, so the whole room lands around $350. He reused an unused twenty-amp circuit "Past Jeff" left for the tools, added a ceiling fan, finally mounted a Unifi 6 Pro access point that had been sitting on his rack for four years, and ran in-wall fiber: multimode for 10 gig, singlemode for 100 gig.

About five grand is sunk into what you can see, and there's no carpet yet — just OSB. He's also rethinking content: less unaffordable high-end AI hardware, more projects, retro tech, home-lab stuff you can self-host. He wants to finally ship the bricks and is floating the wall layout with the people who paid for them. Verdict: an honest downscale, and honestly a better channel for it. 🔨

## 10. My Coding Agent Took 19 Seconds to Say Anything — by Alex Ziskind

![Alex Ziskind](https://i.ytimg.com/vi/bYpdCFz7VtA/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=bYpdCFz7VtA
**Karakeep doc:** `z1hs1m2mcqcua8q86ugvlx71`

Watch a coding agent grind through a 25-turn session on an RTX Pro 6000 and the pattern is ugly. Turn one answers in about 0.12 seconds. By turn 25 it sits there for 19 seconds before writing a single word, because every turn it re-reads its own growing history. Caching doesn't hand you a flat speedup here either — the effect multiplies as the conversation drags on.

Alex walks through the mechanism in the middle of the video. Before the model writes anything it reads your whole prompt and takes notes, which is the KV cache — keys and values. Keep the notes around and you don't re-read the whole book next time, just the new lesson. No cache on a 30-turn session re-reads 150,000 tokens by the end, over 2 million across the session. vLLM's prefix cache never reads more than roughly 10,000 tokens per turn, so 14x less reading. The catch: those notes live in GPU memory next to the model, which is exactly why stuffing a 32GB model into a 32GB card bites you.

Four setups get compared: no cache, vLLM's built-in prefix cache (on by default — he had to switch it off for the baseline), vLLM's CPU offload spilling to system RAM, and LM Cache, which keeps notes in a separate server in RAM or on NVMe.

On a DGX Station GB300 running Qwen3 235B, a 32k document went from 1.35s with no cache to 112–122ms with any cache — 11-12x faster. Overflow it with 48 documents and vLLM's GPU cache gets 0% hits and behaves like no cache at all; vLLM offload and LM Cache both fix it at 164ms and 140ms. With 16 clients and 144 concurrent requests the spread is brutal: no cache 187s, vLLM GPU 107s, vLLM CPU offload 69s, LM Cache basically tied.

The restart test is where LM Cache earns its keep. Kill vLLM and both built-in caches lose everything, straight back to 1.35s. LM Cache reconnects and answers in 141ms with 99.9% hits. The first restart attempt crashed though — LMC held about 89GB of GPU memory for two minutes after the kill, pushing a normal 150s restart to 277s until he found the 30s minimum wait setting.

Coding agents are the workload he actually cares about. Eight agents on the late turns: 104 seconds per turn with no cache, 2.1 seconds with cache. Verdict: leave vLLM's prefix cache on; if everything fits in RAM, vLLM's own offload keeps pace with LMC; reach for LM Cache when restarts shouldn't start cold or the cache outgrows RAM. You pay in moving parts and slower restarts.

## 11. Artcraft Keeps Slopping Clones Of Adobe And Microsoft Office — by Brodie Robertson

![Brodie Robertson](https://i.ytimg.com/vi/_pojeQDbt5Q/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=_pojeQDbt5Q
**Karakeep doc:** `vzxg99jl16zm6emvajbdbwqv`

Brodie starts with the AI game-decompilation and modding scene. There's a Rust rewrite of Call of Duty: Modern Warfare 2 that's one of the better efforts — mostly reasonable, online multiplayer doesn't work, but the rest isn't terrible. Around it sits a pile of worse projects: people jamming Skate 3 and Minecraft into every game, into Elden Ring, even running two games at once with physics objects from one colliding with the other.

His read on the reaction is blunt. Everyone writes each step off as a joke, two weeks later something ten steps ahead lands, and the cycle repeats. He calls it a coping mechanism.

Then he pivots to the ArtCraft suite, which points the same tools at big proprietary apps. PhotoCraft is a "kind of sorta" reimplementation of Photoshop. It's buggy as hell but it runs, and it wasn't made by a person. VectorCraft does Illustrator, DesignCraft does InDesign, FilmCraft does Premiere Pro. Builds exist for basically everything — RPM on Arm Linux, FreeBSD, AppImage, macOS installer, Windows, Windows Arm, even PDFCraft for the Acrobat experience nobody requested.

It's not just Adobe. SoundCraft targets Avid Pro Tools, CadCraft targets AutoCAD, and more recently WordCraft, DeckCraft and GridCraft clone Word, PowerPoint and Excel. All of it landed in roughly two to three weeks. It's unmistakably AI: Claude is the biggest contributor, and the repos run hundreds of commits a day, fifty-plus an hour, with zero QA or engineering practice behind them.

He tested PhotoCraft briefly and calls it mostly stable, mostly. He still won't put a business on it — alpha, experimental, crashes, and performance problems that only surface on large projects. Use the tried-and-tested open source projects instead.

Legally it's a mess. They claim open-source clean-room implementations, but AI-generated code leans toward public domain and nobody knows how UI ownership plays out. Adobe and Microsoft lawyers are surely drafting something, and Nintendo's lawyers set the tone.

Then he reads Eric S. Raymond's take: decompiling a DOS shareware game gave him readable Pascal that transpiled cleanly to Rust, and he now figures anything shipped as a binary is transparent as glass. Only SaaS keeps secrets. Gingerville's thread calls the FilmCraft build outright AI slop and infringement. Brodie's bigger worry is open washing — if AI output is effectively public domain, what happens to the GPL? 🙃

## 12. Formula 1 Just Had a Production Incident #f1 #formula1 #programming — by Better Stack

![Better Stack](https://i.ytimg.com/vi/RsWyIQoJkHY/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/RsWyIQoJkHY
**Karakeep doc:** `gd72rzlg4lb4wd0a3tlv9b72`

The 2026-spec F1 cars got their first wet race at a soaked Spa, and the power unit controller immediately shipped itself a production incident. There's a wet weather mode that trims power, and a bug in it fired whenever drivers crawled along slowly: the cars dropped into idle and just sat there. Max Verstappen had the slowest getaway, tripped the bug first, and only clocked the problem when he looked in his mirror and saw eight other cars still creeping behind him. Red flag. The race started fifty minutes late while the FIA wrote a software patch and pushed it to all eleven teams to install, lifting the usual wet-weather power reduction in the affected zones.

The driver quotes are the good part. Oliver Bearman said his throttle pedal got cut off by something completely outside his control — "I didn't even know that the FIA could control our throttle pedal." Oscar Piastri said he'd never seen an F1 race delayed by a bug. Sergio Perez said it felt like driving a rental car that ran out of time.

Here's why it's a textbook outage and not just a funny race story: this was a low-speed, wet-weather edge case on the very first wet race these cars had ever run. Testing never exercises that corner of the state space. You only find it in production, with a global broadcast and twenty cars on a live track, and the blast radius is the whole field at once. That's the classic recipe — an untested branch, a rare trigger, a shared dependency, no rollback room.

The response is the other half of the lesson. The FIA had a patch coded and deployed to eleven independent teams inside the stoppage window, which is genuinely fast hotfixing under pressure. But it also means every car on the grid runs FIA-controlled firmware that can be rewritten mid-session. Handy for a formation-lap bug; slightly alarming when you remember the same channel can reach a throttle map.

Wojtek cares because it's a clean, no-abstraction example of the thing every on-call engineer fears: a rare path in shared code, discovered live, fixed by shipping to everyone at once. Watch it for the incident narrative, stay for the drivers finding out who actually owns their pedals. 🏎️

## 13. AI Can Mod ANY Game #claudecode #modding #ai — by Better Stack

![Better Stack](https://i.ytimg.com/vi/BjmoXpgbfhQ/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/BjmoXpgbfhQ
**Karakeep doc:** `yhxnu4y0bu605qecmkq3810n`

Modding a game used to mean months in an IDE, reading someone else's decompiled spaghetti, and praying the engine didn't laugh at you. Now there's a Claude Code plugin that does the whole thing on autopilot. Better Stack demos three of them in a minute flat: real Minecraft running inside GTA V with creepers blowing up GTA cars, the Halo Warthog driving around in Minecraft, and Call of Duty Zombies rebuilt inside it. All three came out of AI coding agents, and the dev behind them open-sourced the whole kit as Universal Modder. You point Claude Code at any game you own, describe the mod, and it works out the engine, reads the code, generates its own models, and tests the running game.

The core loop is called "mod any game," and it's brutally simple: search the knowledge base, recon the game, back up your saves, read the real code, build one working slice, verify it in-game, record it, and write a field note. Recon runs through a CLI that fingerprints the engine, spots the anti-cheat, and finds where your saves live. Generated art comes from FAL — sprites, textures, 3D models, sound, even voice — which checks out, since the builder is an ex-FAL engineer. You can probably swap that part for your own tooling, but FAL is the default for a reason.

The knowledge base is the sneaky-good part. There are already 117 game notes and 65 technique notes in there, mostly written by Claude Code and Open Code. Help others out and it'll open a PR to add your notes back.

Caveat, and it's a big one: the tool is upfront that anti-cheat is out of scope. So no, this shouldn't spawn a wave of aimbots — hopefully. Reception is split. One dev called the whole scene a "plague of vibe-coded mashups" that don't hold up as games, and he's not entirely wrong: most of these are 30-second viral clips nobody will actually play. But the narrator's right that it's still cool. He learned Java as a kid just to add stuff to Minecraft. That now takes seconds.

Verdict: fun as hell, thin as a product. Wojtek cares because it's a working template for agentic coding against a hostile, undocumented codebase — which is most of real work. No repo URL was in the slice, so no Project line.

## 14. Meta just caught up with Anthropic — by Theo - t3․gg

![Theo - t3․gg](https://i.ytimg.com/vi/DbWL6Zs2j_g/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=DbWL6Zs2j_g
**Karakeep doc:** `v72bodv4nuipkles85s2khe7`

Meta did the thing nobody expected: shipped a model in the same tier as Anthropic's Fable and OpenAI's Astra. Theo spent a few days with it and came away impressed, and yes, people accused him of being on Meta's payroll.

The release is two models, and the naming is a crime: Muse Wonder and Muse Wonderful — read that as "Wonder Space Full." They're genuinely different sizes: Wonder runs around 120k tokens/sec, Wonderful around 50k. Only Muse Wonder is on the API, priced at $4 per million input, $20 per million output, $0.20 cache reads. Wonderful is locked behind a Muse Code subscription with no published price. That's the biggest problem — the Wonderful Max runs are the ones that beat Fable, Astra and Opus 5 across a pile of benches and landed Meta third overall on Artificial Analysis, and you can't buy them directly.

There's real substance underneath. Meta trained the model to understand how memory works during post-training, and the Terminal Bench scores are strong, close to Astra and Opus 5-S, with state-of-the-art on Deep SWE and SWE Marathon for the full version.

Where it sucks: 3D and UI. Against Opus 5.5 on a tractor demo it's weak, and its Blender output is garbage. Theo's point is that 3D ability isn't emergent from raw smartness — it's trained in post-training on environments someone sells to the labs. On Skatebench, though, Muse Wonderful Full hit 95%, Gemini-only territory.

The real surprise is behaviour. On a Rust-subset project running 115+ agents, Opus did deeper, more correct work, while Muse did more, faster, and reviewed surprisingly well — 209 probes, fair judging, ranking its own work second. On one T3 Code bug, Muse's answer was the most readable of the three, and it found a smaller, cleaner PR the others missed. Theo rates it 1-2/10 on "dumb shit" versus Opus at 3 and Astra at 10.

Caveats: no price for the model he actually likes, and the cheaper Muse Wonder version is bad. Verdict: the first non-OpenAI/Anthropic model he'd daily-drive since Fable, but don't cancel Claude Code — and where the hell is Gemini 4 Argon?

### 9to5Linux (RSS)

## 15. Mozilla Thunderbird 158 Email Client Improves Quick Filter Responsiveness — by 9to5Linux

![9to5Linux](https://9to5linux.com/wp-content/uploads/2026/10/tb158.webp)

**Source:** https://9to5linux.com/mozilla-thunderbird-158-email-client-improves-quick-filter-responsiveness
**Karakeep doc:** `wc4yedsvq57i2xnwx6axaynq`

Mozilla pushed Thunderbird 158 alongside Firefox 158, and it's a small one — the faster release cadence means smaller drops. The headline changes are an ExtensionSettings policy tweak so add-ons install from update_url when install_url isn't set, plus better responsiveness from the quick filter.

The bug-fix list is where the value sits. A crash during body search is gone. SMTP Kerberos authentication on Linux with STARTTLS works again, and POP accounts no longer throw repeated connection errors when Thunderbird starts in offline mode. Right-clicking an inline image now opens the context menu instead of zooming. Quick Filter finally matches accented names when you search without accents. Ctrl+Enter no longer confirms the send prompt and fires off a duplicate message.

Smaller annoyances got cleaned up too. Plain-text inline forwards stop eating signatures below the quote, Copy Link Location grabs the full path for detached attachments, and the Troubleshooting page stops claiming crash reports aren't configured when they are. Unified Folders no longer leaves All Folders stuck on, archived inboxes stop showing up as "INBOX" because of localized names, and OpenPGP gets fixes for unlocking, a handle leak and protection state. The backup password dialog's context menu is clickable again.

There are two security fixes on remote content exceptions: ones missing a URL scheme now cover both HTTP and HTTPS rather than HTTP only, and wildcards like *.example.com are no longer wrongly permitted. CalDAV and CardDAV get a long tail of fixes — saved credentials survive restarts, prompts name the account and calendar, vCard REV timestamps stop corrupting. This is the unglamorous maintenance a mail client actually needs. Binaries for Linux, macOS and Windows are available now.

## 16. TUXEDO Stellaris 16 Gen8 Linux Laptop Unveiled with Intel Core Ultra 9 290HX Plus — by 9to5Linux

![9to5Linux](https://9to5linux.com/wp-content/uploads/2026/10/ts16v8.webp)

**Source:** https://9to5linux.com/tuxedo-stellaris-16-gen8-linux-laptop-unveiled-with-intel-core-ultra-9-290hx-plus
**Karakeep doc:** `ywjimwrlqd6d429jc14rckkj`

TUXEDO Computers dropped the Stellaris 16 Gen8, and the spec sheet reads like someone dared them to stop. Intel Core Ultra 9 290HX Plus, 24 cores (8 performance, 16 efficiency), 5.6 GHz boost. Up to 96 GB DDR5-6400 or 128 GB DDR5-5600. PCIe 5.0 NVMe. This is a desktop that happens to fold shut.

The display is the interesting part: a 16-inch 2560×1600 panel, 500 nits, your pick of OLED or Mini-LED matte, 100% sRGB, 16:10, and a genuinely absurd 300 Hz refresh. Pair that with NVIDIA RTX 5000-series graphics — 5070 Ti, 5080, or 5090, all at 24 GB GDDR7. Ports are equally silly: Thunderbolt 4, two USB-C 3.2, HDMI 2.1 with HDCP 2.3, Mini DisplayPort, three USB-A, 2.5 Gbit Ethernet, Wi-Fi 7 (BE200), Bluetooth 5.4, an SD reader, and a liquid-cooling connector for TUXEDO's Aquaris external loop. Add a 99 Wh battery, TPM 2.0, RGB per-key backlight, and a 1080p webcam.

It ships with TUXEDO OS — KDE Plasma on an Ubuntu base — or plain Ubuntu 26.04 LTS. Pre-orders start at €2,350 / $2,630 for the base config: Ultra 9 290HX Plus, RTX 5070 Ti, 16 GB RAM, 500 GB SSD. Shipping starts early November.

The catch is that entry price. A 5090 and 128 GB will hurt, a lot. And that 300 Hz panel on a 99 Wh battery means you're gaming near a wall outlet 🔋.

## 17. Linux Mint 27 “Adrien” Slated for Release on Christmas, Based on Ubuntu 26.04 LTS — by 9to5Linux

![9to5Linux](https://9to5linux.com/wp-content/uploads/2026/05/lm.webp)

**Source:** https://9to5linux.com/linux-mint-27-adrien-slated-for-release-on-christmas-based-on-ubuntu-26-04-lts
**Karakeep doc:** `h1xyreho61bnkgwqggsg3ute`

Linux Mint is jumping numbers: the next release is 27, not 23, and it targets Christmas Day 2026. After Mint 22.3 “Zena” closed out the alphabet, the devs reset the counter and switched to boys' names, so we get Linux Mint 27 “Adrien.” That's the small change. The big one is that point releases are dead — from here it's 27, 28, 29, straight up.

Adrien is built on Ubuntu 26.04 LTS (Resolute Raccoon) and ships Linux kernel 7.0 by default, with the usual Cinnamon, Xfce and MATE flavours. On paper it's a normal cycle release. In practice it's the heaviest feature drop the project has done in years: brand-new apps in Xepub (an EPUB reader), Clockenstein (calendar) and Clocks (alarm manager); a redesigned Thingy / Library app; a System Administration tool that finally handles kernel management; and real Wayland improvements for Cinnamon. Project lead Clement Lefebvre, 20-plus years deep on Mint, says he's never seen this many changes land in a single release, and admits the beta phase is going to be rough.

No firm date yet, but a beta is expected within weeks. If you're still on Mint 22.x, this is the upgrade worth waiting for.

Caveat: Christmas launches slip. Bet on a January ISO. 🎄

### LinuxLinks (RSS)

## 18. git-graph - visualize Git history graphs — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/01/Git-Clients.jpg)

**Source:** https://www.linuxlinks.com/git-graph-visualize-git-history-graphs/
**Karakeep doc:** `p1h36uepdh4298fddzr00hc6`
**Project:** [git-graph](https://github.com/git-bahn/git-graph) — Rust CLI that renders Git history as a structured branch graph instead of terminal spaghetti.

git-graph is a command-line tool that turns your repo's commit history into a structured branch graph instead of the usual tangle of ASCII noodles. The pitch is simple: `git log --graph` falls apart the moment you've got three long-lived branches and a feature branch that merges twice, and git-graph fixes that by rendering history through a defined branching model rather than guessing.

You pick one of the built-in models — the kind that match named strategies like GitFlow — or write your own in a TOML config file. You can also bind a model to a specific repository, so you don't reselect your preferred view every single time you run it. That last bit is the real quality-of-life win for teams that actually follow a convention.

It does one job: visualization. No staging, no rebasing, no GUI. It reads straight off the Git repo with no separate database to populate or keep in sync. It handles relative worktrees, octopus merges, configurable colouring, and custom commit format strings the same way `git log` does. There's an ASCII-only mode for when your terminal, CI log, or SSH session can't cope with box-drawing characters.

Written in Rust by Martin Lange, MIT licensed. If you like your workflow plain and terminal-bound, it slots in without dragging anything else along. The caveat: it's a rendering layer, so if your team's branching is chaotic, a prettier graph just makes the chaos legible — it won't fix it. Worth a look if you've ever stared at merge spaghetti and given up. 🍝

## 19. 8 Useful Free and Open Source Security Testing Software — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/09/Data_security_02.jpg)

**Source:** https://www.linuxlinks.com/useful-free-open-source-security-testing-software/
**Karakeep doc:** `akik0h9rfs9dk1segbsgy4dv`

LinuxLinks draws a line first: an assessment finds vulnerabilities, testing goes and exploits them. This roundup sticks to testing tools and deliberately skips whatever the vulnerability-analysis and vulnerability-detection lists already cover.

The eight: ZAP for web app scanning, mitmproxy as an interactive HTTPS proxy, ffuf for fast web fuzzing to discover hidden paths, virtual hosts and parameters, Wfuzz as a web app fuzzer plus a Python library, sqlmap for SQL injection penetration testing, Dalfox for hunting cross-site scripting bugs, Commix as a Python-based pentest tool, and jwt_tool for auditing JSON Web Tokens and their security weaknesses.

The post frames the categories it's operating in — vulnerability assessment, penetration testing, runtime testing, code review — then hands you the picks in a ratings chart, LinuxLinks-style, with only free and open source software eligible for inclusion. Each name links off to a fuller writeup if you want the detail behind the one-liner.

It's a directory entry as much as an article: eight tools, one screen, no fluff. Useful as a bookmark if you're building a pentest box or refreshing one that's gone stale. The caveat is that it's an index — it tells you what exists, not which of these actually fits your stack, your workflow, or your license constraints. You'll still do the reading, and the line between "this is tested" and "this is trusted" is entirely on you. 🧰

**Projects:**

- **[ZAP](https://github.com/zaproxy/zaproxy)** — OWASP ZAP — intercepting proxy and automated web-app security scanner.
- **[mitmproxy](https://github.com/mitmproxy/mitmproxy)** — An interactive TLS-capable intercepting HTTP proxy for penetration testers and software developers.
- **[ffuf](https://github.com/ffuf/ffuf)** — Fast web fuzzer written in Go.
- **[Wfuzz](https://github.com/xmendez/wfuzz)** — Web application fuzzer.
- **[sqlmap](https://github.com/sqlmapproject/sqlmap)** — Automatic SQL injection and database takeover tool.
- **[Dalfox](https://github.com/hahwul/dalfox)** — XSS scanner and parameter-analysis tool built for automation
- **[Commix](https://github.com/commixproject/commix)** — automated all-in-one OS command-injection exploitation tool
- **[jwt_tool](https://github.com/ticarpi/jwt_tool)** — toolkit for testing, tweaking and cracking JSON Web Tokens

## 20. Lightwhale – immutable Linux distribution for Docker servers — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/04/Linux-Distributions.png)

**Source:** https://www.linuxlinks.com/lightwhale-immutable-linux-distribution-docker-servers/
**Karakeep doc:** `rud2462d1rrumc7lahb0z68j`
**Project:** [Lightwhale](https://lightwhale.asklandd.dk) — immutable Buildroot-based Linux distro that boots straight into the Docker Engine

Lightwhale is a lightweight Linux distribution built with Buildroot, and it does one job: run Docker containers. It boots from a live ISO straight into a working Docker Engine. No install wizard, no partitioning ritual.

The root filesystem is immutable, stored as a compressed SquashFS image, and both the kernel and rootfs get loaded into RAM at startup. That keeps the core OS walled off from your application data and config, which is the entire point — less to maintain on a container host. Persistent storage is optional. By default your changes sit in RAM and vanish on reboot; enable persistence on a dedicated device and you get Btrfs with snapshots and RAID1 across multiple disks.

It's aimed at homelabs, self-hosted services and container deployments on physical or virtual machines. BIOS and UEFI booting both work, there's guest integration for QEMU/KVM and VMware, and init is plain old SysV-style. Don't ask for a desktop or a package manager — there isn't one, everything goes through Docker. It's x86_64 only, on a fixed release model, actively maintained, and built by Stephan Henningsen.

For a homelab box that should do nothing but churn containers, that's a clean fit. The trade-offs are honest: no package manager means anything outside a container is your problem, and the RAM-resident rootfs eats memory the containers could use. Still, it's the anti-bloat answer to a full-fat server distro. 🐳

## 21. clazy - Qt-oriented static code analyser — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/Linter-Tool-Banner1.png)

**Source:** https://www.linuxlinks.com/clazy-qt-oriented-static-code-analyser/
**Karakeep doc:** `c8ea5veca5m8ll8wcl4z7nb0`
**Project:** [clazy](https://github.com/KDE/clazy) — Clang-based static analyser with 50+ checks aimed specifically at Qt C++ code.

clazy is a static analyser tuned for C++ written against Qt, and it doesn't pretend to be anything else. It's built on Clang and actually understands Qt's idioms and APIs, which is the entire point: generic linters spend all their time talking about C++ and none about the Qt-specific footguns that only blow up at runtime.

It ships more than 50 checks — unnecessary allocations, incorrect API usage, container and iterator handling, broken signal/slot connections, temporary objects, inefficient string operations. The checks come in levels, so you decide how loud it yells at you. It runs primarily as a Clang compiler plugin that drops into your normal build, and there's also clazy-standalone for projects that just hand it a JSON compilation database. A decent chunk of the checks include fix-its, so it will patch the dumb stuff for you.

It's LGPL v2.0, maintained by KDE, and free in every sense. If you write Qt apps and you're not running this, you're shipping bugs your compiler already knew about.

Caveat: it's Qt-only by design, so nothing for plain C++ or other frameworks, and the fix-its need eyeballing — blindly applying automated rewrites has its own special flavour of pain. 🛠️

## 22. Firefly Synth 2 - flexible software synthesizer for sound design — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/04/007-additive-synthesis.png)

**Source:** https://www.linuxlinks.com/firefly-synth-2-flexible-software-synthesizer/
**Karakeep doc:** `c47o7bdrq29jxwx509inj231`
**Project:** [Firefly Synth 2](https://github.com/sjoerdvankreel/firefly-synth-2) — flexible C++ software synthesizer (VST3/CLAP) built for detailed sound design

Firefly Synth 2 is a C++ software synth for people who actually design sounds instead of scrolling presets, and it just shipped as VST3 and CLAP plugins on Linux. It's free, MIT-licensed, and written by Sjoerd van Kreel.

The architecture is the pitch. Four oscillators cover DSF additive generation, basic waveforms, dedicated hard-sync and FM generators, plus a combined string/noise algorithm. Oscillators can modulate each other through inter-osc AM and FM routing, so you don't need external processing to get gnarly. External audio can be used as an oscillator source too, which pushes it past being a closed-off wave generator.

Effects split into four per-voice and four global slots — comb filtering, state-variable filtering, compression, several waveshaping options. Reverb, feedback delay, and multitap delay live in separate per-voice and global echo sections with their own filtering. Modulation is where it gets silly: six per-voice and six global LFOs with subslots and skewing controls, seven per-voice 16-stage MSEG envelopes with a visual editor and configurable loop/release points, and a modulation matrix with 17 per-voice and 9 global slots. Global unison exposes 28 per-voice parameters. Sidechain input works on both the instrument and the effects variants, and realtime graphs show per-voice activity.

Caveats: it's Linux, VST3/CLAP only — no LV2, no AU, no Windows or Mac build mentioned. Microtuning goes through MTS-ESP only. It competes with Surge XT, Vital, and ZynAddSubFX, and it's more flexible than most of them if you're willing to route it yourself.

Verdict: a proper sound-design weapon for the Linux audio crowd, which is finally not a contradiction.

## 23. jwt_tool – JSON Web Token security testing toolkit — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/09/Data_security_02.jpg)

**Source:** https://www.linuxlinks.com/jwt_tool-json-web-token-security-testing-toolkit/
**Karakeep doc:** `hnm1677srrz9314agf131xqs`
**Project:** [jwt_tool](https://github.com/ticarpi/jwt_tool) — command-line toolkit for attacking and auditing JSON Web Tokens

jwt_tool is a Python command-line toolkit for attacking JSON Web Tokens, and if you've ever trusted a JWT because it "looked signed," this is the tool that'll prove you wrong. Andy Tyler and contributors ship it under GPLv3.

What it does: decode and inspect headers, payloads and signatures; validate signatures against supplied keys; and modify claims, headers and expiry timestamps on the fly. Then it goes hunting. It tests for algorithm confusion and unsigned-token flaws, digs into RSA and HMAC signature verification, and checks known JWT vulnerabilities including key injection and ECDSA signature validation bugs.

Brute force and fuzzing are built in. It runs dictionary attacks to crack weak signing secrets, fuzzes claim values to poke at auth behaviour, and tests JSON Web Key Sets and public-key configurations. The JWT Attack Playbook automates the whole checklist. It generates RSA and ECDSA keys, submits modified tokens straight to web apps, imports captured HTTP requests that carry auth tokens, and lets you set custom headers, cookies, proxies and request rates. Everything tested gets logged for later analysis.

Caveats: it needs a target URL and patience — this is a tester's tool, not a one-click exploit. Findings are only as good as the server you point it at, and rate limiting will fight you the whole way.

Verdict: the reference JWT attack kit. Every pentester should have it, and every backend dev should run it against their own auth before someone else does for free.

## 24. 22 Best Free and Open Source Linux Ham Radio Tools — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/06/039-radio-antenna.png)

**Source:** https://www.linuxlinks.com/best-free-open-source-linux-ham-radio-tools/
**Karakeep doc:** `vxr81arudt6mv7vwx2d9keud`

Ham radio is the original off-grid social network: licensed operators talking on designated frequencies, no internet, no cell towers, sometimes bouncing signals off satellites or the moon. LinuxLinks rounded up 22 free and open source tools for it, and the list leans hard on practical gear-day software rather than toys.

WSJT-X leads for weak-signal digital modes — the FT8 stuff that decodes signals you can't even hear. Logging and contesting get the most real estate: Tucnak and Not1MM for contest logs, plus QLog, klog and CQRLOG for everyday logging, and ADIF Multitool when you need to validate or convert those log files. Packet and APRS are covered by Dire Wolf, Xastir and Qtel. Transceiver control is the other cluster: Flrig, Fldigi, wfview for Icom rigs, CatRadio on Hamlib, and AetherSDR for FlexRadio hardware. DMR and handheld programming get qdmr and CHIRP. FreeDV and JS8Call round out the digital-mode crowd, TrustedQSL handles QSO signing, and GridTracker maps the whole thing.

Eligibility is strict — free and open source only, no proprietary demos. Each entry links to a full portal page with a feature breakdown and screenshots, plus a 2026 ratings chart. 22 tools, zero cost, and your SDR dongle finally earns its keep. 📻

**Projects:**

- **[WSJT-X](https://github.com/saitohirga/WSJT-X)** — weak-signal digital modes (FT8, FT4, JT65) — the de-facto standard for HF/VHF digital DX (GitHub mirror of the SourceForge project)
- **[Tucnak](https://tucnak.nagano.cz/wiki/Main_Page)** — Tucnak is multiplatform VHF/HF contest logbook. It is executable on Linux and other unix-type systems, Windows, Android and MacOS.
- **[QLog](https://github.com/foldynl/QLog)** — Qt amateur-radio logbook with SQLite backend.
- **[Dire Wolf](https://github.com/wb2osz/direwolf)** — soundcard AX.25 packet modem/TNC plus APRS encoder and decoder — runs as a tracker, digipeater or iGate
- **[Qtel](https://github.com/sm0svx/svxlink)** — Qtel is a graphical EchoLink client for Linux, offering station browsing, connection management, audio controls, chat, and proxy support.
- **[wfview](https://gitlab.com/eliggett/wfview)** — Many of Icom’s transceivers from the last 20 years will work to some degree with wfview. This is free and open source software.
- **[Flrig](https://github.com/w1hkj/flrig)** — amateur-radio transceiver control application
- **[Fldigi](https://github.com/w1hkj/fldigi)** — amateur-radio digital modem application
- **[TrustedQSL](https://www.arrl.org/tqsl)** — ARRL's TQSL — callsign certificates and LoTW log signing.
- **[klog](https://github.com/ea4k/klog)** — KLog is a ham radio logging application with ADIF support, DXCC tracking, LoTW and eQSL integration, rig control, maps, and statistics.
- **[CQRLOG](https://github.com/ok2cqr/cqrlog)** — CQRLOG is intended for daily general logging of HF, CW &amp; SSB contacts and strongly focused on easy operation and maintenance.
- **[Xastir](https://github.com/Xastir/Xastir)** — Xastir is an X11 graphical APRS client developed for amateur radio operators. Free and open source software.
- **[ADIF Multitool](https://github.com/flwyd/adif-multitool)** — validate, modify and convert ham radio log files from the command line
- **[AetherSDR](https://github.com/aethersdr/AetherSDR)** — Native amateur-radio workstation for FlexRadio (FLEX-6000/8000/Aurora) — Linux, macOS, Windows · Qt6 + C++20.
- **[qdmr](https://github.com/hmatuschek/qdmr)** — A GUI application for configuring and programming cheap DMR radios under Linux and MacOS X.
- **[Not1MM](https://github.com/mbridak/not1mm)** — Not1MM != N1MM, An amateur radio contest logger for Linux.
- **[JS8Call](https://github.com/js8call/js8call)** — Official repository for JS8Call Software.
- **[FreeDV](https://github.com/drowe67/freedv-gui)** — GUI Application for FreeDV – open source digital voice for HF radio.
- **[CatRadio](https://github.com/PianetaRadio/CatRadio)** — CatRadio is a graphical ham radio control application using Qt and Hamlib, with VFO controls, meters, rig settings and remote operation.
- **[CHIRP](https://chirpmyradio.com/projects/chirp/wiki/Home)** — radio programming app for a long list of amateur radios
- **[Hello Contest](https://github.com/ftl/hellocontest)** — Hello Contest is an amateur radio contest logger with fast keyboard entry, scoring, QTC support, CW macros, spots and Hamlib integration.
- **[GridTracker](https://gitlab.com/gridtracker.org/gridtracker2)** — GridTracker is an amateur radio companion for visualising WSJT-X activity, contacts, grids, spots, awards, solar data, alerts, and logging.

## 25. word-sys's PDF Editor - edit PDF text, images and objects — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2019/04/PDF-File.png)

**Source:** https://www.linuxlinks.com/word-syss-pdf-editor-edit-pdf-text-images-objects/
**Karakeep doc:** `q8hxhqk11bppf2s8msve81b3`
**Project:** [word-sys's PDF Editor](https://github.com/word-sys/word-sys-pdf-editor) — GTK/libadwaita graphical editor for creating and editing PDF text, images and objects.

word-sys's PDF Editor is a GTK/libadwaita app that actually edits PDFs instead of just shuffling pages around. Developer Barın Güzeldemirci built it for the Linux desktop with Pardus and Debian in mind, and it's GPLv3.

Unlike PDFsam or PDF Arranger, which split, merge and rotate, this one lets you touch the stuff inside a page. You can select, edit or delete existing text blocks, drop in new text with your own font, size, colour and decoration, and move objects around the canvas. Images keep their alpha transparency. You can add rectangles, ellipses, checkmarks, crosses, freehand strokes and highlighters built from smoothed vector strokes, and select individual words for precise highlighting. Add or remove pages, rearrange them via drag-and-drop thumbnails, merge whole documents.

The interesting bit is export. It uses the anyconvert engine to spit out DOCX, PPTX, ODT, ODP or plain text, with two modes: canvas-based output that preserves visual positioning, or semantic output that rebuilds flowing content. There's multi-level undo/redo, pointer-centred zoom, a tabbed interface and a keyboard-shortcut reference. Safe Save and Restricted Mode keep you from trashing a document by accident.

Honest caveat: it's a young, one-developer project written in Python, so expect rough edges and no OCR. If LibreOffice Draw has been your PDF editor of last resort, this is a cleaner answer. 🧾

## 26. git-tui - human-friendly interfaces for Git — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/01/Git-Clients.jpg)

**Source:** https://www.linuxlinks.com/git-tui-human-friendly-interfaces-git/
**Karakeep doc:** `x2vg26sm71oksukl0g1tzqq9`
**Project:** [git-tui](https://github.com/ArthurSonzogni/git-tui) — interactive terminal interfaces for reviewing git diffs and browsing commit logs.

git-tui is a small, sharp idea: instead of a full Git client, it bolts interactive interfaces onto commands you already type. Arthur Sonzogni's project ships as `git tui <command>` — you keep the usual Git vocabulary, you just get something navigable back.

Right now it covers two jobs. `git tui diff` gives you a browsable diff view where you move between changed files and scroll long hunks with Page Up, Page Down, Home and End. `git tui log` does the same for commit history. Tab characters render consistently, subprocess input and error streams stay out of the interface, and if you ask for something it doesn't handle it falls back to plain git — with an explicit `git` command to force the original behaviour when you want it.

It's C++ on top of the FTXUI library, MIT licensed, and builds from source with CMake. The scope is deliberately narrow: it's a viewer for diffs and logs, not a staging or branching tool. If you want the full client, look at lazygit or tig. If you want a lighter, focused helper that doesn't fight your muscle memory, this earns a look. Compared to delta or difftastic, which are pagers and diff renderers, git-tui is the interactive layer sitting on top. 🐙

## 27. 14 Useful Free and Open Source JavaScript Linter Tools — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/05/921-coding.jpg)

**Source:** https://www.linuxlinks.com/useful-free-open-source-javascript-linter-tools/
**Karakeep doc:** `tw0mmb6i85uy66336fszzcgy`

A linter is a static analyzer. It reads your code without running it and flags dumb errors, style crimes, and things that will detonate in production. That's the pitch. LinuxLinks rounds up 14 free and open source options for JavaScript and TypeScript. The list: ESLint, Biome, standard, Flow, OXC, XO, JSHint, Sherif, RSLint, JSLint, neostandard, deno_lint, quick-lint-js and Putout. ESLint is the heavyweight and effectively the default in most JS shops. Biome is the Rust-rewrite crowd's answer to an entire toolchain. Flow is a Facebook-bred static type checker. XO is a configurable ESLint wrapper for people who hate configuring ESLint. Sherif watches monorepo dependency drift, and Putout doubles as a pluggable code transformer. The author is refreshingly honest about the downside: linters can become a distraction, and on old, enormous codebases they may help less than the marketing claims. There's real overlap here, so running three of them in CI mostly means three ways to see the same warning. The ratings chart is LinuxLinks' usual star rating 🌶️, since no actual benchmarks are on offer. Wojtek angle: if you touch any JS you already run one of these; the rest are fuel for arguing about tabs on the internet.

**Projects:**

- **[ESLint](https://github.com/eslint/eslint)** — Find and fix problems in your JavaScript code.
- **[Biome](https://github.com/biomejs/biome)** — A toolchain for web projects, aimed to provide functionalities to maintain them. Biome offers formatter and linter, usable via CLI and LSP.
- **[standard](https://github.com/standard/standard)** — JavaScript Style Guide, with linter & automatic code fixer.
- **[Flow](https://github.com/facebook/flow)** — Flow is a static type checker for your JavaScript code. It does a lot of work to make you more productive.
- **[OXC](https://github.com/oxc-project/oxc)** — A collection of high-performance JavaScript tools.
- **[XO](https://github.com/xojs/xo)** — JavaScript/TypeScript linter (ESLint wrapper) with great defaults.
- **[JSHint](https://github.com/jshint/jshint)** — JSHint is a tool that helps to detect errors and potential problems in your JavaScript code.
- **[Sherif](https://github.com/QuiiBz/sherif)** — Opinionated, zero-config linter for TypeScript & JavaScript monorepos.
- **[RSLint](https://github.com/rslint/rslint)** — A (WIP) Extremely fast JavaScript and TypeScript linter and Rust crate.
- **[JSLint](https://github.com/jslint-org/jslint)** — JSLint, The JavaScript Code Quality and Coverage Tool.
- **[neostandard](https://github.com/neostandard/neostandard)** — A spiritual successor to the standardjs javascript style guide.
- **[deno_lint](https://github.com/denoland/deno_lint)** — Blazing fast linter for JavaScript and TypeScript written in Rust.
- **[quick-lint-js](https://github.com/quick-lint/quick-lint-js)** — Quick-lint-js finds bugs in JavaScript programs.
- **[Putout](https://github.com/coderaiser/putout)** — pluggable and configurable JavaScript linter, transformer and formatter

## 28. Meet ONLYOFFICE Docs 10.0: new AI tools, modular apps, better PDF editing and security updates — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/10/ONLYOFFICE-Docs-10-banner.png)

**Source:** https://www.linuxlinks.com/onlyoffice-docs-10-ai-tools-pdf-editing-modular-apps/
**Karakeep doc:** `nvua7czmfgh7g82b214agqhs`
**Project:** [ONLYOFFICE Docs](https://www.onlyoffice.com/docs) — open-source office suite for text documents, spreadsheets, presentations and PDFs

ONLYOFFICE Docs 10.0 has landed for the online, desktop and mobile editors, carrying roughly 50 new features and more than 1,000 bug fixes. The headline is AI stuffed into every editor. The PDF Editor now understands your document's contents: ask it questions, generate summaries, rewrite text, fix grammar, redact sensitive data, build tables of contents and translate. Documents, spreadsheets and slides get context-aware AI on a dedicated tab, with configurable quick actions, saved prompts and an AI chat. Spreadsheets can generate formulas, spot trends, and clean up inconsistent data. Presentations can produce a whole slide structure with speaker notes. The genuinely interesting bit for self-hosters: you can wire in any AI model, including a locally hosted one, and the free Community edition ships with no AI module at all if you want to stay clear of the whole thing. Four new AGPL v3 "Apps" extend the suite — AI Agents (MCP-backed), Forms, Files and Rooms. Cloud instances get them on by default; self-hosted boxes install them with a single command. The PDF editor also gains hidden-metadata removal, table detection and signature reuse. Docs get real-time cursor following, "keep with next" and better RTL support. Under the hood, 35 vulnerabilities are patched — good news, though it also means 35 were sitting there before. The desktop client hits 10.0 with a refreshed homepage, template redesigns and Odoo integration. Verdict: the local-model hook is the one feature worth caring about; the rest is checkbox AI.

## 29. Coccinelle - semantic program matching and transformation — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/Linter-Tool-Banner2.png)

**Source:** https://www.linuxlinks.com/coccinelle-semantic-program-matching-transformation/
**Karakeep doc:** `dgyfolyatlposx72yl9hpv1s`
**Project:** [Coccinelle](https://coccinelle.gitlabpages.inria.fr/website) — semantic program matching and transformation engine for C source code

Coccinelle is a program matching and transformation engine aimed squarely at C. Instead of grepping for a string, you describe a recurring code pattern and let the tool find every structurally similar match across a huge codebase, then rewrite them. Its core is the Semantic Patch Language, SmPL, which abstracts away the irrelevant differences between individual code snippets. That's the whole trick: the same semantic patch keeps working even when variable names, expressions and surrounding code change. The `spatch` utility applies those patches, either reporting the matches it finds or emitting modified source. Coccinelle has deep ties to Linux kernel development, where it automates sweeping API changes and hunts recurring programming errors at a scale no human reviewer can match. It supports metavariables for matching varying constructs and understands control-flow relationships, so it can do genuine source-to-source refactoring rather than blind text replacement. It's GPL v2, developed by Julia Lawall, Yoann Padioleau, Rene Rydhof Hansen, Henrik Stuart, Gilles Muller and Nicolas Palix, and written primarily in OCaml. That choice is the caveat: it's fast and expressive, but the tooling around the language is thin and the learning curve for SmPL is steep. For anyone maintaining C at volume, it's a genuine force multiplier. Wojtek angle: if you ever mass-refactor C by hand, this is the tool you didn't know was saving your sanity.

## 30. Full Steam Ahead - import games from other launchers into Steam — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2022/08/space-shooter-games.jpg)

**Source:** https://www.linuxlinks.com/full-steam-ahead-import-games-steam/
**Karakeep doc:** `ch7bnqy3atm57fwikavbd1p1`
**Project:** [Full Steam Ahead](https://github.com/creeperkatze/full-steam-ahead) — desktop app that imports games from other launchers into Steam

Full Steam Ahead is a Rust desktop app that drags your scattered game library into one place. It scans the launchers you already have, lists the games it finds, and lets you cherry-pick which titles to pull into Steam, individually or in a big batch. On Linux it covers Epic Games, GOG, itch.io, Heroic Games Launcher, Legendary, Lutris and MiniGalaxy, plus games running through Bottles or Proton. Anything not detected can be added manually as a non-Steam executable with custom launch options. The part that usually makes imported games look like garbage is artwork; this tool pulls grids, logos, heroes and icons from Steam and SteamGridDB to keep them visually consistent with the rest of your library. You can pick alternative art, and everything previews before it's applied, so nothing silently wrecks your shortcuts. It also buckets imported games into Steam collections based on their original launcher, lets you pick which Steam user account receives the shortcuts, and, smart move, auto-backs up your Steam shortcut config so you can roll back when it all goes sideways. You can even have it close and restart Steam after importing. It's AGPL v3, by creeperkatze and contributors. Caveat: it edits Steam's shortcut file, so back up before you go wild; the built-in backups exist for a reason. Wojtek angle: exactly the kind of glue tool you want when a Steam Deck or Linux box is running five launchers at once.

### RSS — Other

## 31. Higgsfield takes AI video from 1 minute to over 10 — by OpenAI News

![OpenAI News](https://openai.com/favicon.ico)

**Source:** https://openai.com/index/higgsfield-longer-videos-voice/
**Karakeep doc:** `oo4kql82r6agm9mb85m78m68`

Another day, another OpenAI startup love letter, this time to Higgsfield AI, a company on a mission to let anyone with an idea make "professional" video. Per CEO Alex Mashrabov, before GPT-6 Astra their clips topped out around one minute. Now users can make videos over ten minutes long. That's the headline, and it's doing an awful lot of lifting in the deck.

The substance: Higgsfield's creative agents already handle repetitive junk like generating shot variations. With GPT-6 Astra they can also call external tools to do manual 3D modeling work, which Mashrabov says tackles the hard problem of keeping consistency across longer videos. Their own YouTube channel — almost half a million subs, naturally — now generates instructional videos over ten minutes using an AI workflow. That's the case study, such as it is.

GPT-Image-2.5 shows up for the small-business pitch: it can reliably render text and infographics on top of imagery, which Mashrabov calls state of the art. Codex lets the company's roughly 200 creatives prototype software without begging the backend team, and Mashrabov claims GPT-6 Astra "can ship production-ready code, which was never possible before." Right. The deck says revolution, the changelog says a checkbox.

Next up is "voice to movie" with GPT-Live-1 — describe a film out loud and watch it render in real time. Also, Mashrabov supports rural schools in Kazakhstan and used Astra's visual understanding to tailor lesson videos to what students struggle with. Genuinely nice, no sarcasm there. The rest is a press release wearing a customer-story hat. ☕

## 32. Rewinding the exponential: How we keep hardware usage down — by Cloudflare Blog

![Cloudflare Blog](https://blog.cloudflare.com/_emdash/api/media/file/01M4RYTCQFG9RZ8F8JCR9C9TQQ.png)

**Source:** https://blog.cloudflare.com/rewinding-the-exponential/
**Karakeep doc:** `jikpsvjgmw3yg55ofukyx9vk`

Cloudflare's Data team walked through how they fight the same losing battle every infra team fights: traffic grows exponentially, hardware grows linearly. In May their pipeline was pushing roughly two billion events per second through Logfwdr, centralized receivers, the Buftee buffer, and ClickHouse. Five years of work, they claim, is equivalent to deferring two and a half years of hardware expansion. The timeline is concrete. In 2022 they blew up the one monolithic message schema into product-specific streams; that alone cut backbone bandwidth 35–40% and knocked out about a year of growth. In 2024 they swapped LZ4 for zstd compression, nervously watching CPU, and found little impact; compressed throughput dropped nearly 40%, letting the same pipe carry 1.5x the traffic. Then 2026 brought three moves. Load balancing killed double-writing: instead of shipping every non-regional event to two regions, Logfwdr sends it once and a remote inserter makes the second ClickHouse copy from Buftee downstream of sampling. That saved ~43 GB/s of transit for ~7 GB/s of cross-DC replication, a net 36 GB/s. Decentralized sampling adds a second pass in Logfwdr, shuffling by key and taking the square root of each group; it halved compressed data on the top datasets, ~25 GB/s or over 2PB/day. Pipeline-wide aggregation computes rollups at every stage up to ClickHouse aggregating engines; the HTTP dataset fell from 9+ GB/s to under 2 GB/s. Total: ~70 GB/s gone from the backbone, throughput now eight months behind its old projection. The honest caveat is baked in — organic growth erased half a 50% reduction in two months. This is real engineering, not a product launch.

## 33. Under the hood, off the hot path: how D1 scales to millions of databases — by Cloudflare Blog

![Cloudflare Blog](https://blog.cloudflare.com/_emdash/api/media/file/01M4TZKNBC5XJ3T8WNHET65CMR.png)

**Source:** https://blog.cloudflare.com/d1-control-plane/
**Karakeep doc:** `ht5x0y60otlrrxqbdvi3noze`

Cloudflare's D1 control plane deep dive, and it's actually useful for anyone building on Workers. D1 is managed serverless SQLite where each database is backed by one SQLite Durable Object, so you can spin up millions of them. The demand comes from AI-assisted and vibe-coding platforms that want one database per user, tenant, or preview environment. The numbers: 15x growth in live non-deleted databases over one year, 65x over two, and 18x growth in daily active databases (as of October 8, 2026). OpenAI's Jon Abrams gets a quote for ChatGPT Sites. The engineering principles are the takeaway: design for failure and idempotency, keep central single-region components off the hot path, use Workers KV for routing metadata, use Hyperdrive to pool and cache Postgres access, precompute aggregates, accept eventual consistency, and load-test with realistic workloads. The creation flow checks account limits on a read replica, generates a UUID and a fresh `newUniqueId()` Durable Object ID, initializes the object, then writes the metadata row to the Postgres primary — the "creation checkpoint." Retries deliberately use new IDs, so a failed attempt can leave two Durable Objects alive; a 30-second heartbeat plus jitter tells the orphan it doesn't exist and it deletes itself. Query paths never touch Postgres: Edge API Worker → Workers KV lookup → Eyeball Worker → Durable Object. Storage limits (5 GB free, 1 TB paid) get enforced through a queue, batched deltas into an `account_database_stats` table, and a Hyperdrive cache trick where a `dynamic_ttl` parameter keyed on account ID keeps hot rows cheap. Free-tier row limits run on ClickHouse and Quicksilver instead. The caveats are honest: totals are eventually consistent and enforcement lags behind reality. The patterns are worth stealing even if you never touch D1.

## 34. Your Algorithm, Your Words: New Ways to Shape What You See on Facebook — by Meta Newsroom

![Meta Newsroom](https://about.fb.com/wp-content/uploads/2026/10/Your-Algorithm_Your-Words_New-Ways-to-Shape-What-You-See-on-Facebook_Header.jpg?w=1200)

**Source:** https://about.fb.com/news/2026/10/introducing-your-algorithm-facebook/
**Karakeep doc:** `sr7z43739v1sqog6jz7ice16`

Meta's pitch is that you're finally "in the driver's seat." The new Your algorithm tool lives in the three-dot menu on every post and lets you type, in plain language, the topics you actually want in Feed and Reels. Meta says the LLM-backed ranking systems read that stated intent and adapt in real time, shifting within the same session.

The second change is feedback. After you tap Interested or Not interested, Facebook may ask follow-up questions so you can spell out what you liked or disliked, and recommendations supposedly update on the spot. The three-dot menu got a reshuffle to make all of it easier to reach.

What it actually is: one more input stacked on top of the thousands of signals Meta already reads — likes, comments, watch time, the lot. The company's own ranking transparency page still describes a multi-signal machine, and it isn't going anywhere. Typing a sentence doesn't switch the algorithm off or hand you the levers; it nudges a weighting inside a system you still can't inspect. No export, no audit, no list of what the model inferred from your paragraph, and no promise it persists across sessions the way a saved preference would.

Still, real-time natural-language steering is a genuinely different mechanic from a hidden interest graph you can't argue with. Worth poking at. Just don't mistake a text box for control. 🙃

## 35. Leading Tech Companies Join Global Law Enforcement in Major Crackdown on West African Scam Networks — by Meta Newsroom

![Meta Newsroom](https://about.fb.com/wp-content/uploads/2026/10/Leading-Tech-Companies-Join-Global-Law-Enforcement-in-Major-Crackdown-on-West-African-Scam-Networks_Header.jpg?w=1200)

**Source:** https://about.fb.com/news/2026/10/meta-tech-companies-law-enforcement-crackdown-global-scam-networks/
**Karakeep doc:** `yw4aogz0q3h7o76da8ds3mim`

Meta rounded up Coinbase, Google, Microsoft, OpenAI, Starlink, Adobe and friends — 15 companies total — plus law enforcement from ten countries for the biggest joint scam-center operation of its kind. The UK's National Crime Agency hosted it in London alongside the DOJ, FBI, Homeland Security Investigations, Secret Service and Treasury, with partners from Ghana, Nigeria, Australia, Canada, New Zealand and India.

The numbers are the actual story. Meta removed more than 3.7 million Facebook and Instagram accounts, pages, and groups based in West Africa, most impersonating US and UK users. Leads on 30-plus scam centers went out; 28 people were arrested; 117 trafficked victims were rescued from a residential compound in Ghana where they'd been imprisoned, malnourished, and physically and psychologically abused. Coinbase flagged 65-plus active victims and blocked over $415,000 in losses. The FBI's Kash Patel claims at least $11 million in potentially freezable funds and hundreds of devices seized. Silent Push mapped over 35,000 malicious domains and nearly 700 communication channels tied to the centers. Microsoft suspended suspect accounts.

Fraud types swept up: investment, job/task, law-enforcement impersonation, military impersonation, non-delivery, romance, and scam-recovery cons. West African centers are described as more decentralized and less industrial than the Southeast Asia compounds hit earlier this year, which is why they'd been harder to pin down.

It's a press release with a long quote reel from a dozen VPs, and whether the pressure holds is anyone's guess — but the concrete arrests, rescues, and dollar figures make it one of the more substantive corporate security posts this week. 🚨

## 36. Announcing the Official Selection for the Edits Film Festival — by Meta Newsroom

![Meta Newsroom](https://about.fb.com/wp-content/uploads/2021/10/meta-social-16x9-1.jpg?w=1200)

**Source:** https://about.fb.com/news/2026/10/announcing-the-official-selection-for-the-edits-film-festival/
**Karakeep doc:** `upu0jcq2ey7qxejb51hmdo0e`

Meta wants its Edits app to be a thing, so it ran a film festival in Mumbai, co-curated with Yuvaa, and pulled in a little over 200 entries from India between August 25 and October 8. The brief was deliberately loose: build something from your camera roll, funny, informative, or emotionally gutting, your call. Now there are 12 Official Selections, every one of them an Instagram reel, and every one of them conveniently also a demo of what the Edits app can do. Funny how that works.

The top three get picked by a panel of Ahsaas Channa, Dolly Singh, Nikhil Taneja and Rajeev Masand. The other nine get the honor of being named on a newsroom post and, presumably, a hashtag. Follow along with #EditsFilmFestival if that's your thing.

This is a marketing play wearing a talent-search costume, and honestly it's not a bad one — 200 entries for an app nobody was asking for is a decent haul, and the shortlist is real Indian creators instead of Meta employees' pets 🙃. The caveat is the prize: there's no cash, no distribution deal, no contract anywhere in the copy. You get a reel on Meta's site and a shout-out. That's exposure, and exposure doesn't pay rent.

Verdict: worth clocking only as a signal of how hard Meta is pushing Edits against CapCut. Nothing here to act on.
