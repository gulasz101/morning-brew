---
date: 2026-11-02
slug: 2026-11-02-morning-brew
tags: Web Search, Mobile Computing, Local LLM, Artificial Intelligence, Large Language Models, Distributed Systems, Kubernetes, Machine Learning, AI Infrastructure, Cybersecurity, Internet Of Things, Military Technology, Retail Industry, Linux
---

Morning Brew for 2026-11-02: 40 items written from 40 hoarded bookmarks and feeds, 0 dropped after a failed retry.

### RSS

## 1. My phone runs a local 2B model that searches the web, and Perplexity feels pointless now, by XDA
![](https://static0.xdaimages.com/wordpress/wp-content/uploads/wm/2026/11/qwen-in-noema-on-iphone-16.png?w=1600&h=900&fit=crop)
**Source:** https://www.xda-developers.com/phone-runs-local-model-that-searches-the-web-perplexity-feels-pointless/ · **Karakeep:** `hromcdqkofz2quvt0etkls7i`

**In short:** A write-up about running Qwen 3.5 2B locally on a phone, with web search through Noema, and why the author thinks Perplexity is overkill for quick lookups. I would say it is interesting for privacy and small phone questions, but 2B is still the floor and the tool calling is only just good enough.

**Key points:**
- Qwen 3.5 0.8B scores 25.3% and Qwen 3.5 2B scores 43.6% on the Berkeley Function Calling Leaderboard.
- The author treats 2B models as the absolute floor for phone web search.
- Noema is iOS-only; Off Grid is suggested for Android, LLM Hub covers both, and Local LLM on Android can use Gemma 4.
- The tested setup is Qwen 3.5 2B at Q4_K_M in Noema on a base iPhone 16, about 1.28GB.
- Noema Search is a SearXNG instance with no account and no identifier attached to queries.
- Perplexity gives unlimited basic searches and about five Pro Searches a day on the free plan.

**Details:** The point is not a bigger model on the phone. It is a small one that knows when to search, with the app handing it a search tool and pulling short passages rather than whole pages. The author's Noema setup uses Qwen 3.5 2B at Q4_K_M, keeps reasoning off to stop rambling, and leaves most of an 8GB iPhone free. Noema adds an Evidence panel with sources, plus toggles such as Current Date.

On Android the article points to Off Grid, LLM Hub or Local LLM, with Gemma 4 as the main Qwen alternative. The privacy angle is real, but the article also admits cloud subscriptions already cover plenty, so this is more a fourth-app avoidance move than a revolution. I would say it is a neat trick for quick lookups. I would not call it a Perplexity replacement for longer research.

**For my projects:** Nothing for my projects.

## 2. NVIDIA AI Infrastructure (@NVIDIAAIInfra) on X, by X (formerly Twitter)
![](https://pbs.twimg.com/media/HWI2qYsXMAAlG0q?format=webp&name=large)
**Source:** https://share.google/3C1Z2znRylLxSwHgj · **Karakeep:** `tpd6o60tuwuodpdvuxp6gc2w`

**In short:** NVIDIA Workload Map is an open-source Kubernetes workload description inside the DSX AI Factory Platform; it sounds useful for platform teams, but it is not for my k3s homelab.

**Key points:**
- Open-source project within the NVIDIA DSX AI Factory Platform
- Provides a common description of Kubernetes workload structure
- Aims to help schedulers, controllers and platforms interpret workload types with fewer custom integrations
- Intended to let developers support new AI frameworks faster
- Posted by NVIDIA AI Infrastructure on X on 2 Nov 2026 with 3,177 views

**Details:** NVIDIA Workload Map is an open-source piece of the NVIDIA DSX AI Factory Platform. It gives a common description of Kubernetes workload structure so schedulers, controllers and platforms can read workload types with fewer custom integrations. The stated aim is that developers can support new AI frameworks faster.

The post is enterprise AI factory material, not a small cluster tool. For my k3s homelab on homelab-2nd, there is no concrete Kubernetes path, backup story or metrics story in the post, and nothing here fixes a problem I have. The comments are the useful part: one says platform teams waste cycles on bespoke CRDs, another says smaller operators benefit because they lack adapter teams. That is plausible, but it still leaves gang recovery and failure handling as open questions, since one commenter asks how it handles gang recovery when a worker fails and gets no answer in the text.

I would say it is interesting infrastructure plumbing, but not worth chasing for my setup.

**For my projects:** Nothing for my projects.

## 3. Hackers pushed freezers at hundreds of French supermarkets to 122 degrees. Now the Pentagon is asking whether the same thing hit U.S. military bases | Fortune, by Fortune
![](https://fortune.com/img-assets/wp-content/uploads/2026/10/GettyImages-2299339600-e1793399497786.jpg?resize=1200,600)
**Source:** https://fortune.com/2026/11/01/hackers-pushed-freezers-at-hundreds-of-french-supermarkets-to-122-degrees-pentagon-investigating-us-military-bases/ · **Karakeep:** `zyw4bjjq6m9opno7dpsesrxw`

**In short:** Hackers turned up freezers at hundreds of French supermarkets past 122 degrees, and the Pentagon is now probing similar outages at US military commissaries. I would say it is a nasty supply-chain target, not a clever exploit.

**Key points:**
- Hundreds of French stores hit overnight, including 80 Carrefour, about two dozen Monoprix and 150 Intermarché.
- Temperatures went above 122 F, with two supermarkets reporting about €270,000 ($300,000) in stock damage.
- US commissaries in at least seven locations had outages in August; the probe is being led by the Defense Criminal Investigative Service.
- The weak point named was outdated firmware on Danfoss AK-SM/AK-SC controllers and Copeland or Dixell xweb units reached over the internet.
- No proof yet that the two sets of outages are connected, or that the US ones were a hack.
- Cybercrime is projected at $10.8 trillion this year, up from $3 trillion in 2015.

**Details:** I read this as a reminder that boring kit is the soft spot. The French side sounds crude but effective: get into internet-facing refrigeration controllers, push the temperature up overnight, so the food is gone for good. The affected kit is common across chains, so one exposed setup means many stores. That is the part I would worry about in my own stuff, though I have nothing like this in the homelab. The US angle is less settled. More than half a dozen commissaries had outages in August, and the Pentagon is treating them as a possible cyberattack while saying nothing. There is no proof of a link, and the article is careful about that. Still, the food angle is ugly because losses are immediate and cannot be reversed. I would say the story is mostly old firmware on appliances nobody patches. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 4. Bootqt - create bootable USB drives from disk images - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2020/11/business-finance-concept-rocket-from-paper.jpg)
**Source:** https://www.linuxlinks.com/bootqt-create-bootable-usb-drives-disk-images/ · **Karakeep:** `w2aa8n9hh47qctz3mwmd2clz`

**In short:** Bootqt is a small Qt front end for writing ISO, IMG and RAW images to USB, with a few distro downloads and Ventoy built in. I would say it is handy on a desktop, but nothing I need for my projects.

**Key points:**
- Writes ISO, IMG and RAW disk images to USB drives.
- Detects connected USB disks and shows device paths and model names.
- Downloads Ubuntu, Fedora Workstation, Linux Mint Cinnamon and Clonezilla images.
- Downloads and installs Ventoy for multiboot USB drives.
- Shows a confirmation dialog before overwriting the destination and attempts to unmount partitions first.
- GPL v3.0, written in Python, by Giant Pink Robots.

**Details:** It is a compact Qt application for preparing bootable USB drives, with separate tabs for local images and downloads. The useful bits are the disk detection, progress display and the Ventoy option, because one drive can then carry several images. The bad news is that writing is still destructive, so the confirmation dialog matters, and it is a desktop utility rather than anything with a Kubernetes path or backup story. I read about it, I did not run it. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 5. Qodo builds context into AI code review with Codex, by link
![](https://openai.com/favicon.ico)
**Source:** https://openai.com/index/qodo-codex-plugin/ · **Karakeep:** `xkcr6wz5bioab0xtmmktmgd7`

**In short:** The headline says Qodo builds context into AI code review with Codex, but the page body was not available, so I cannot judge it properly.

**Key points:**
- Headline only: Qodo builds context into AI code review with Codex.
- No article body was fetched, so versions, prices, licence and technical details are missing.
- No candidate links were supplied for this item.

**Details:** I read about it, I did not run it, and in this case I barely got past the title. The headline points at Qodo and Codex in the context of AI code review, but without the body I cannot tell what is actually shipped, how it works, or what it costs. I would say it is not worth acting on until the article is available. For my projects, there is nothing concrete to take from a title alone: no Kubernetes path, no local image model angle, and nothing for guitar practice. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 6. 13 Best Free and Open Source Scorewriters - Compose, arrange, print, and publish music - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2020/02/score-with-musical-notes.jpg)
**Project:** [icking-music-archive.org](https://icking-music-archive.org/software/htdocs)
**Source:** https://www.linuxlinks.com/excellent-scorewriters-compose-great-music/ · **Karakeep:** `j5tp059b1slakieq6vfu68n6`

**In short:** LinuxLinks lists 13 free and open source Linux scorewriters as alternatives to Sibelius and Finale. I would say it is a useful directory if you want notation software, but nothing here touches my projects.

**Key points:**
- 13 free and open source scorewriters for Linux, all downloadable at no charge.
- Sibelius and Finale are proprietary, very expensive, and not available for Linux; the cheapest Sibelius perpetual licence is hundreds of dollars.
- The list covers graphical editors, text-based engravers, MIDI sequencers, and tools such as Rosegarden, MuseScore Studio, LilyPond, Frescobaldi, TuxGuitar, Gregorio, and EasyABC.
- A comment points to MusiXTeX through the Icking music archive; Steve Emms left it out to avoid heavyweight TeX knowledge.
- It is a roundup with one-line descriptions, not a deep review.

**Details:** LinuxLinks frames scorewriters as notation software for composing, arranging, printing, and publishing sheet music. The list runs from graphical editors like MuseScore Studio and Canorus to text-based engravers like LilyPond and PMW, plus MIDI sequencers such as Rosegarden and Aria Maestosa. There is also Gregorio for Gregorian chant and music21 for computational musicology. The article says all generate scores with traditional layout rules, and that some tools work without a GUI, so you can edit on small devices. I read it as a starting menu rather than advice: it names the programs, gives short descriptions, then points at LinuxLinks' wider software lists. The candidate link is the Icking music archive for MusiXTeX, which a commenter recommended and the author declined because it assumes TeX familiarity. For my own stuff, nothing here fits RiffRadar, homelab-2nd, or ideogram4-local. It is a music notation list, not a guitar practice tracker, not infrastructure, and not image generation. So yeah, that's that.

**For my projects:** Nothing for my projects.

**Projects:**
- [Rosegarden](https://www.rosegardenmusic.com/): Rosegarden is a powerful audio, MIDI and score editing and sequencing environment for musicians.
- [MuseScore Studio](https://github.com/muse-sequencer/muse)
- [Lilypond](https://lilypond.org/): LilyPond &ndash; Music notation for everyone.
- [Frescobaldi](https://frescobaldi.org/): Frescobaldi is a LilyPond sheet music editor.
- [Denemo](https://denemo.org/): Denemo | Free and Open Music Notation Editor.
- [music21](https://github.com/cuthbertLab/music21): Music21: a Toolkit for Computer-Aided Musical Analysis and Computational Musicology - cuthbertLab/music21.
- [mup](https://github.com/microsoft/mup)
- [TuxGuitar](https://github.com/helge17/tuxguitar): Open source guitar tablature editor. Contribute to helge17/tuxguitar development by creating an account on GitHub.
- [Aria Maestosa](https://ariamaestosa.github.io/ariamaestosa/docs/index.html): Aria Maestosa.
- [Gregorio](https://gregorio-project.github.io/): Free software for typesetting Gregorian chant.
- [Canorus](https://sourceforge.net/projects/canorus/): Download Canorus for free. Music score editor. Canorus is a free cross-platform music score editor. It supports an unlimited number and length of staffs, polyphony, a MIDI playback of notes, chord….
- [PMW](https://github.com/PhilipHazel/pmw): PMW is a music typesetting program, processing marked-up text into PostScript and PDF. - PhilipHazel/pmw.
- [EasyABC](https://github.com/jwdj/EasyABC): EasyABC. Contribute to jwdj/EasyABC development by creating an account on GitHub.

## 7. aerynOS 2026.11 Is Out with GNOME 51, KDE Plasma 6.8, COSMIC 1.11, and Budgie 10.10, by Cloudflare
![](https://9to5linux.com/wp-content/uploads/2026/11/aos2611.webp)
**Source:** https://9to5linux.com/aerynos-2026-11-is-out-with-gnome-51-kde-plasma-6-8-cosmic-1-11-and-budgie-10-10 · **Karakeep:** `e9xt2t5fkhxwo1g6fz4ykrrf`

**In short:** aerynOS 2026.11 is the latest snapshot of the independent distro formerly called Serpent OS, with GNOME 51 by default and an alpha warning. I would say it is not worth it for production.

**Key points:**
- Independent Linux distro previously known as Serpent OS; release 2026.11
- Powered by Linux 7.2 and Linux 6.18 LTS kernels
- GNOME 51 by default; KDE Plasma 6.8, COSMIC 1.11, and Budgie 10.10.4 supported
- New lichen-installer with Btrfs root, automatic formatting, Wi-Fi and keyboard layout setup, and a refined TUI
- moss package manager got a restructured CLI, new commands, and short aliases
- Still alpha quality; not for production use

**Details:** aerynOS 2026.11 is the latest ISO snapshot of the independent distro formerly known as Serpent OS. It ships Linux 7.2, which that's current enough, but it is still alpha quality. The live ISO defaults to GNOME 51 and also supports KDE Plasma 6.8, COSMIC 1.11 and Budgie 10.10.4, plus Hyprland 0.57 and Noctalia 5.4.1. The new lichen-installer adds Btrfs root partitions, automatic drive formatting, Wi-Fi and keyboard layout setup, and a more refined TUI. moss got a restructured CLI with new commands and short aliases. Under the hood there is Mesa 26.2.6, PipeWire 1.6.11, QEMU 11.1.3, Wine 11.21, Firefox 159 and Thunderbird 159. Unfortunately there is no production promise here, so I would not install it on a real machine. For my homelab there is no Kubernetes path, no backup story and no metrics, so nothing for my projects. So yeah, that's that.

**For my projects:** Nothing for my projects.

## 8. Bootleg Toolbox - verify and manage lossless concert recordings - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2021/09/Audio-Analyzers.jpg)
**Source:** https://www.linuxlinks.com/bootleg-toolbox-verify-manage-lossless-concert-recordings/ · **Karakeep:** `g333wf0dcqmsezvz63lilmbe`

**In short:** Bootleg Toolbox is a Rust desktop app and CLI for collectors and traders of lossless live concert recordings, with checksums, decode tests, spectral analysis and tagging. I would say it is niche and not worth it for my projects.

**Key points:**
- Free and open source under GNU GPL v3.0, written in Rust by Nicolas Simoni.
- Runs on Linux and Windows, with both a graphical interface and command-line mode.
- Reads FLAC, WAV, AIFF, APE, SHN, WavPack, ALAC, MP3, AAC and Ogg files.
- Verifies and creates FFP, ST5, MD5 and SFV checksums, and decode-tests files for damage or truncation.
- Analyses spectral characteristics and MP3/AAC traces for possible lossy transcodes, upsampling and lower bit depth.
- Tags and renames FLAC recordings from concert information files, with an option to undo changes.

**Details:** Bootleg Toolbox is aimed at collectors and traders of lossless live concert recordings. It organises work by concert, disc and track, and covers integrity checks, audio quality problems and sharing preparation. On top of checksums and decode tests, it can spot possible lossy transcodes, upsampling and lower-bit-depth recordings, estimate tape speed errors from FM pilot tones, musical tuning references and mains hum, and fix sector boundary errors into corrected FLAC copies without modifying the originals. It also converts to FLAC or WAV, makes MP3 copies, creates private torrents, verifies downloads against torrent checksums, extracts audio from DVD-Video, MKV and MP4 sources, and retrieves setlists from setlist.fm with a personal API key. Nothing for my projects, but it looks like a tidy specialist tool.

**For my projects:** Nothing for my projects.

## 9. Xviewer - simple image viewer - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2019/10/Photo-Metadata.png)
**Source:** https://www.linuxlinks.com/xviewer-simple-image-viewer/ · **Karakeep:** `r6rva8rtuiht4wv1c9ql8ynw`

**In short:** Xviewer is Linux Mint's simple GTK image viewer, with constant-memory zooming and a plugin set. I would say it is not worth it for my projects.

**Key points:**
- Image viewer from the Linux Mint project, written in C with a traditional GTK interface.
- Uses gdk-pixbuf for image loading and supports a wide variety of image formats.
- Zooming and scrolling keep constant memory usage for large images.
- Includes gallery browsing, full-screen viewing, slideshow mode, automatic orientation from camera metadata and wallpaper setting.
- Extensible via plugins: EXIF details, map location, export, slideshow shuffling and a Python console.
- Licensed under GNU General Public License v2.0, which is fine.

**Details:** Xviewer is the Linux Mint project's straightforward image viewer. It opens photographs and other images through gdk-pixbuf, browses collections in a gallery, and handles large images with constant memory usage during zooming and scrolling. Full-screen viewing and slideshow mode are there, along with automatic orientation from camera metadata, zoom controls and a wallpaper option. Plugins add EXIF details, map locations, export, slideshow shuffling and a Python console. The interface is traditional GTK with configurable toolbars, status information and gallery display.

Unfortunately the page does not give a version number, so I cannot judge release maturity from this alone. It looks like a solid everyday viewer, stable and quite good job for a desktop, but it has no Kubernetes path, backup story or metrics, so nothing for my homelab. For local image work, an image viewer can be handy, but this is not about model control or references, so I would not force it into ideogram4-local either. So yeah, that's that.

**For my projects:** Nothing for my projects.

## 10. Intel vs Apple Silicon for Developers… Seriously, by Alex Ziskind
![](https://i.ytimg.com/vi/2V1UtfLfkGk/maxresdefault.jpg)
**Source:** https://www.youtube.com/shorts/2V1UtfLfkGk · **Karakeep:** `u5a1gj4qwgnmj09b7iz3ayg0`

**In short:** Alex Ziskind compares a Dell XPS with Intel against a MacBook Neo on a Python benchmark. The Intel machine is faster in this test, and the battery result is the part worth noting.

**Key points:**
- Video by Alex Ziskind comparing a Dell XPS with Intel and a MacBook Neo
- Python test that pegs all cores to maximum
- Plugged in: Dell XPS 57.6 seconds, MacBook Neo 90 seconds
- Averaged over several runs: Dell XPS 65 seconds, MacBook Neo a little better than its first run
- On battery: MacBook Neo about 92 seconds, Dell XPS 67 seconds
- MacBook Neo palm rests stayed cool; Dell got a little warm with an audible fan

**Details:** Alex Ziskind put a Dell XPS with Intel against a MacBook Neo and ran a Python test that pegs all cores. Plugged in, the Dell finished in 57.6 seconds and the Neo in 90; averaged over several runs the Dell was 65 seconds, with the Neo a bit better than its first run. On battery the Neo took about 92 seconds and the Dell 67, so the Intel machine did not need wall power here. The MacBook stayed cool at the palm rests, while the Dell got a little warm and its fan was audible. I would say the surprise is the battery result, not the raw speed. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 11. LifeVal, by link
![](https://openai.com/favicon.ico)
**Source:** https://openai.com/index/lifeval/ · **Karakeep:** `cp530fq57af6z07vib6vx0cz`

**In short:** LifeVal is an OpenAI index page whose body did not load, so I cannot say what it does and I would not call it useful yet.

**Key points:**
- OpenAI index page titled LifeVal.
- No body text could be fetched.
- No candidate links were supplied.
- No version, price, licence or benchmark details are available.

**Details:** The body did not load, so this is not a review of LifeVal, it is a note that the source was empty. I have the title, the OpenAI domain and nothing else. No feature list, no numbers, no pricing, no licence, no version. OpenAI index pages tend to wrap a product, benchmark or safety announcement in calm enterprise language, but that is a pattern, not evidence about this page. I am not going to fill the gap with a guess. If the text turns up later I can come back to it. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 12. Pracownicy czują się zagrożeni, ale ładują dane firm do AI, by NieBezpiecznik.pl
![](https://niebezpiecznik.pl/wp-content/uploads/2026/10/ataki-eset-600x314.png)
**Source:** https://niebezpiecznik.pl/post/pracownicy-czuja-sie-zagrozeni-ale-laduja-dane-firm-do-ai-raport-eset/ · **Karakeep:** `rjx0ygzkmc571jk096q1aocx`

**In short:** ESET and DAGMA's annual Polish business cyber report, and the numbers are grim even if the framing is sales.

**Key points:**
- Surveyed 1026 Polish computer workers, including 457 in security and 407 from firms with at least 10 employees.
- 85% of firms had an incident in the last 12 months; attacks hit 68% of small, 88% of medium and 85% of large firms.
- Only 14% of employees feel competent with digital threats and 50% do not know their company's security rules.
- 35% of AI users would try to bypass blocks on public LLMs and 10% admitted sharing sensitive company data with open AI models.
- 45% of security experts saw more attacks, 36% of firms had phishing and 14% had ransomware.
- 16% kept an incident to themselves and only 28% of firms provide a trusted tool set.

**Details:** It is a sponsored article, so I treat the framing as sales, but the survey numbers are the part I kept. 85% of firms had an incident in the last year, which is a lot. The part I found sad is the AI bit: 35% of AI users would try to bypass blocks on public LLMs and 10% admitted feeding sensitive company data to open models. I would say the useful takeaway is that people improvise because the rules are long and impractical, and only 28% of firms even provide a trusted tool set. The report's 'careless innovator' portrait is a young remote marketing person who tests everything, which sounds familiar enough to be uncomfortable. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 13. https://www.youtube.com/watch?v=6IH0_K8LN_g, by Less Bitter
![](https://i.ytimg.com/vi/6IH0_K8LN_g/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=6IH0_K8LN_g · **Karakeep:** `fhjygve61ewhtarmpm383i67`

**In short:** A Less Bitter YouTube video with an empty transcript. There is nothing to evaluate here.

**Key points:**
- Channel: Less Bitter
- Transcribed on 2026-11-02 via Parakeet
- The raw transcript came back empty
- No candidate links were supplied

**Details:** This one is a YouTube video from the Less Bitter channel, and the transcript that came back is empty. There is no content to read, no title and no description to work from. I cannot tell you what it is about, who is in it, or whether it is any good. The only facts I have are the channel name, the transcription date and the tool used. I would say it is not worth an item until someone gets a real transcript. Maybe the video is great, maybe it is not, but I have no way to tell. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 14. 4 Major Vulnerabilities Got Published To The LKML, by Brodie Robertson
![](https://i.ytimg.com/vi/MjTGcBnoGnE/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=MjTGcBnoGnE · **Karakeep:** `yjx7lvow2695znz3vdk4z6ry`

**In short:** Trend Micro's ZDI published six Linux kernel bugs straight to the public LKML without patches, and the video uses that mess to argue AI makes private disclosure in public projects basically impossible. I would say the disclosure screw-up is the clear part, the AI part is more of a forecast.

**Key points:**
- Six ZDI-CAN reports hit the LKML at once: two CVSS 9.0 RCEs in SMB Direct and KSMBD, plus SKB zero-copy, VMWGFX, TCP search-domain and EnvyMet issues.
- ZDI-CAN-33549, the SMB Direct integer-underflow bug, already has a patch in a Git branch intended for Linux 7.5, but it was not ready for mainline when it was posted.
- Greg Kroah-Hartman told ZDI to fix its submission process; Peter Zijlstra was less polite and called them clue resistant.
- ZDI says it has filed roughly a thousand kernel cases over ten years, only now noticed the reporting docs, will not provide patches, and will release findings at rejection or after 120 days.
- The wider point: the SKB bug was found independently by another source, and with AI doing much security analysis, a security patch in a public tree is effectively the disclosure.

**Details:** Six reports went out to the public LKML at once, two of them CVSS 9.0, and none came with a patch. That is bad news first, plainly: a firm that has been around the kernel for ten-plus years and claims nearly a thousand cases should know that undisclosed security issues go to security at kernel.org, not to a public list. The first one, ZDI-CAN-33549, is an SMB Direct remote code execution bug due to an integer underflow, and there is a patch in a branch intended for Linux 7.5, so presumably it gets expedited. The second 9.0 is a KSMBD race condition, also remote code execution. The rest are local privilege escalation or information disclosure bugs: SKB zero copy, VMWGFX, a TCP search-domain stack buffer overflow, and an uninitialized resource in the EnvyMet code. Greg Kroah-Hartman told them to fix the submission process, and Peter Zijlstra was less polite. ZDI pushed back, saying the formatting has stayed the same for years and that it will not provide patches because that overhead cannot be supported, which, yeah, that is the part I do not buy. The broader point is the one I find more interesting: the SKB bug was found independently by someone else, and with AI doing a lot of security analysis now, the same bug can be found twice by two people using the same model. In an open project, a security patch is basically the disclosure once it lands. I would say the Trend Micro process failure is clear, and the claim that private security in a public project is basically over is at least plausible. So yeah, that's that.

**For my projects:** Nothing for my projects.

## 15. Introducing the Grid Protectors Program, by link
![](https://openai.com/favicon.ico)
**Source:** https://openai.com/index/grid-protectors-program/ · **Karakeep:** `hc4lyyj3xy0bkht4jgg1o9qy`

**In short:** OpenAI put up a page called 'Introducing the Grid Protectors Program', but the body did not load, so I cannot tell what it actually does. I would say it is not worth treating as anything until the text is there.

**Key points:**
- Title only: 'Introducing the Grid Protectors Program', hosted on openai.com.
- No article body was available, so features, scope, pricing and eligibility are unknown.
- No candidate links were supplied, so there is nothing else to cross-check.
- OpenAI is the named owner; the program name is the only concrete fact.

**Details:** So OpenAI has a page with a heroic program name, and that is the whole signal. I read about it, I did not run it, and in this case I cannot even read it. The title says 'Introducing the Grid Protectors Program', which sounds like infrastructure, safety, partner work, or all three at once, but the body was not available, so I am not going to guess. That is a bummer, because OpenAI pages usually tell you what is being sold before the substance arrives. Until the text loads, there are no numbers, no versions, no licence, no eligibility rules and no API details to judge. I would say it is a wait-and-see item, not a tool I can recommend or reject yet. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 16. How we halved DNS build delay and cut memory use by 85%, by Cloudflare Blog
![](https://blog.cloudflare.com/_emdash/api/media/file/01M6426V7J1FR4KZEYMQP555R0.01M6426VZJHB2XCKTQ39W2S71Z.png)
**Source:** https://blog.cloudflare.com/dns-targeted-zone-builds/ · **Karakeep:** `m2iwz2lc2alpxbou61ciw2v3`

**In short:** Cloudflare explains targeted DNS zone builds that halved build delay and cut memory use by 85%, while keeping full builds where they are still cheaper. I would say it is honest infrastructure writing, but nothing for my projects.

**Key points:**
- Cloudflare blog post on targeted zone builds, tagged Deep Dive, DNS, Kafka, Quicksilver and Speed & Reliability.
- The title claims DNS build delay was halved and memory use was cut by 85%.
- Build completion delay was measured over about four hours with a native histogram: median about 3.4 seconds, p90 about 5.5 seconds, p99 mostly 10 to 14 seconds.
- Full builds still happen for first publication, changes that can affect records anywhere, events that do not say what changed, and small zones.
- Cloudflare says the biggest gains already landed: events that used to rebuild the largest zones no longer do, and remaining full builds are mostly for new, small zones.
- After the Zone Builder writes a change, Quicksilver distributes configuration to every Cloudflare data centre in seconds.

**Details:** I read this as Cloudflare explaining why it moved from full zone builds to targeted ones. The headline is the result: build delay halved and memory use down by 85%. The useful part for me is the plain reason full builds are still kept. A first publication needs every record written, a change that can touch records anywhere needs every record checked, and an event that does not say what changed still becomes a full build because the planner does not turn uncertainty into less work. For small zones, a full build is cheap anyway. The remaining full builds are mostly first-publication events for new, small zones, while the events that used to rebuild the largest zones no longer do. Build completion delay was measured over about four hours: median about 3.4 seconds, p90 about 5.5 seconds, p99 mostly 10 to 14 seconds. After the Zone Builder writes a change, Quicksilver distributes configuration to every Cloudflare data centre in seconds. Nothing for my projects, but I like the honesty about keeping the slow path where it is cheaper than pretending everything can be targeted.

**For my projects:** Nothing for my projects.

## 17. Deno Is Over #deno #javascript #programming, by Better Stack
![](https://i.ytimg.com/vi/2Q0aUnbI2nQ/maxresdefault.jpg)
**Source:** https://www.youtube.com/shorts/2Q0aUnbI2nQ · **Karakeep:** `dhjwujj1af9znabckghotqyb`

**In short:** Deno is being absorbed by Cloudflare and the runtime gets a one-year sunset, while Cloudflare keeps Cell D for self-hosted durable objects. I would say it's a bummer for Deno users, but Cell D is the interesting part.

**Key points:**
- The Deno team will support the Deno runtime for one more year with monthly bug-fix and security releases, then end development.
- Cloudflare is buying Deno for the team and Cell D, not for the runtime.
- Cell D is one Rust binary plus a storage bucket for running durable objects on your own servers.
- A durable object is a tiny server with its own SQLite database, addressed by name.
- Superbase Edge functions and Netlify Edge Functions run on Deno-based runtimes.
- Bun joined Anthropic last December.

**Details:** The bad news is simple: Deno is joining Cloudflare and the Deno runtime is on a one-year clock. The team will keep shipping monthly bug-fix and security releases for another year, then stop developing it. That is a runtime people genuinely liked, and Bun is carrying on while Deno is not.

Cloudflare is not buying it for the runtime. They want the team and Cell D, the thing Deno shipped in August. Cell D is durable objects that scale on your own machine: one Rust binary plus a storage bucket, running an existing Cloudflare app with durable objects on your own servers. A durable object is a tiny server with its own SQLite database, addressed by name, so a chat app can have one per channel. The catch was that durable objects mostly ran on Cloudflare, and the open source WorkerD only runs them as a single instance.

If you built on Deno, or on Superbase Edge functions or Netlify Edge Functions, you now have a year to plan. I would say it's a bummer for Deno users, but Cell D is the reason Cloudflare bought them. So yeah, that's that.

**For my projects:** Nothing for my projects.

## 18. DeepFilterNet Plus - noise suppression for microphones and recordings - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2018/06/male-operator-staff-with-team-working-call-center.jpg)
**Project:** [DeepFilterNetPlus](https://github.com/ismailivanov/DeepFilterNetPlus)
**Source:** https://www.linuxlinks.com/deepfilternet-plus-noise-suppression-microphones-recordings/ · **Karakeep:** `msu5azrtuq1z1qly4afid14p`

**In short:** DeepFilterNet Plus is a maintained fork of DeepFilterNet for neural-network speech enhancement on microphones and WAV files, with real-time Linux effects support; I would say it looks solid for noisy audio, but nothing for my projects.

**Key points:**
- Maintained fork of DeepFilterNet by Ismail Ivanov and DeepFilterNet contributors
- Neural network speech enhancement at a 48 kHz full-band sample rate
- Real-time microphone cleanup through a LADSPA plugin for Easy Effects and PipeWire
- Command-line tool cleans noisy WAV files on Linux, macOS and Windows
- Overload protection lets audio pass through unprocessed when the worker cannot keep up
- Licensed under MIT or Apache 2.0, with Rust and Python components and pretrained models

**Details:** DeepFilterNet Plus is a speech enhancement application that removes background noise from microphone input and recorded audio. It is a maintained fork of DeepFilterNet, a neural network framework for full-band speech noise suppression, and it is written in Rust with Python components.

The two main workflows are real-time microphone cleanup through a LADSPA plugin compatible with Easy Effects and PipeWire, and a command-line utility for cleaning noisy WAV files on Linux, macOS and Windows. The fork focuses on real-time reliability: real-time-safe LADSPA processing, overload protection that passes audio through unprocessed when processing cannot keep up, and improved stereo and multi-channel handling. It also keeps the existing DeepFilterNet plugin identifiers and PipeWire filter-chain configurations.

I would say it is a quite good job for anyone fighting fan or room noise on calls. For me there is no audio pipeline to feed it, so nothing for my projects. The project home is the GitHub repository.

**For my projects:** Nothing for my projects.

## 19. Minisforum M2 Pro Mini PC Running Linux - Introduction - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2026/11/Minisforum-M2-Pro-banner.png)
**Project:** [minisforum.uk/m2-pro-358h-minipc](https://www.minisforum.uk/products/m2-pro-358h-minipc)
**Source:** https://www.linuxlinks.com/minisforum-m2-pro-mini-pc-running-linux-introduction/ · **Karakeep:** `kcyyzjfrxrqe81pxtpulal9u`

**In short:** Minisforum's M2 Pro is a Linux-reviewed mini PC built around Intel's Core Ultra X7 358H and Arc B390 graphics. I would say the hardware is interesting, but the soldered 32GB and missing OCuLink keep it in the wait-and-see pile.

**Key points:**
- Intel Core Ultra X7 358H with Intel Arc B390 integrated graphics, 12 Xe3 cores, on Panther Lake.
- 32GB LPDDR5X at 7467 MT/s, soldered to the motherboard.
- 10GbE and 2.5GbE Ethernet, three USB4 ports, Wi-Fi 7, and three M.2 NVMe slots.
- No OCuLink port; the full-size SD card reader is USB 2.0; one NVMe slot runs PCIe 4.0 x1.
- Review uses CachyOS with KDE Plasma, with the AMD-based Minisforum AI X1 Pro as a comparison.
- Built-in power supply, 195 x 195 x 47.5mm chassis, built-in speakers, and a top-mounted fingerprint reader.

**Details:** Steve Emms is starting a Linux series on the M2 Pro, so this is an introduction rather than a verdict. The machine pairs an Intel Core Ultra X7 358H with Arc B390 integrated graphics, and the review unit has 32GB of LPDDR5X at 7467 MT/s soldered to the board. That is plenty for desktop use, but local AI can eat it quickly, and an iGPU shares that same pool.

The connectivity is generous: 10GbE, 2.5GbE, three USB4 ports and Wi-Fi 7, plus three NVMe slots, though one is PCIe 4.0 x1. The built-in power supply keeps the footprint tidy, but there is no OCuLink port and the full-size SD reader is USB 2.0, which is a bummer on an otherwise fast box.

I read this as a promising little desktop and local-AI testbed, not a proven homelab node. The Arc B390 and Vulkan support are the bits I would watch, while the missing OCuLink and fixed memory are the bits that limit expansion. So yeah, interesting, but I want the later Linux results first.

**For my projects:**
- ideogram4-local: Test the Arc B390 as a secondary ComfyUI worker for SD-style jobs, since the 32GB shared memory and Vulkan support could make local image work cheaper, but only if the Linux driver and workflow hold up.

## 20. Audacity 4.0.2 Audio Editor Restores Automatic Saving During Recording, by Cloudflare
![](https://9to5linux.com/wp-content/uploads/2026/11/aud402.webp)
**Source:** https://9to5linux.com/audacity-4-0-2-audio-editor-restores-automatic-saving-during-recording · **Karakeep:** `ss55shwatgsp7ytb7klywkrm`

**In short:** Audacity 4.0.2 is a maintenance release of the free cross-platform audio editor, and it mostly fixes regressions. I would say it is worth grabbing if you already use Audacity, but not a reason to switch.

**Key points:**
- Audacity 4.0.2 is the second minor maintenance update in the Audacity 4.0 series, for Linux, macOS and Windows.
- It restores automatic saving during recording, plus trim, clear selection and zoom shortcuts, and adds PgUp and PgDown timeline scrolling.
- It fixes crashes and corruption bugs, including empty clips, duplicate .aup4 extensions, sample-rate clip moves and CJK text trimming.
- Linux builds are available as AppImage for 64-bit and AArch64 systems, alongside macOS and Windows binaries.
- It comes a month after Audacity 4.0.1.

**Details:** Audacity 4.0.2 is a free and open-source audio editor for Linux, macOS and Windows, released on 2 November 2026. The useful bits for me are the restored automatic saving during recording and the restored trim, clear selection and zoom shortcuts, because losing work during a long take is a bummer. It also adds PgUp and PgDown timeline scrolling, improves playback latency from the input meter display, improves the status bar layout in narrow windows, and improves file importing on Linux.

The fix list is long and mostly about crashes and corruption: empty clips, duplicate .aup4 extensions, replacing projects during Save As, moving clips across tracks with different sample rates, sample snapping, metadata in certain formats, NTSC frame snapping, collapsed clip context menus, CJK text trimming, and label linking during stretching. That is a lot of edge cases, so I read it as a tidy-up release rather than a feature release. Nothing for my projects, since I do not have an audio pipeline in the homelab and RiffRadar is guitar practice tracking, not editing. I would say it is a good update for existing Audacity users and not worth a new workflow on its own.

**For my projects:** Nothing for my projects.

## 21. AI Agents Talked Through the CPU... #openai #cybersecurity #ai, by Better Stack
![](https://i.ytimg.com/vi/gTNkGFFFUY8/maxresdefault.jpg)
**Source:** https://www.youtube.com/shorts/gTNkGFFFUY8 · **Karakeep:** `e0uyksvqbtbqf4oqugx0j7xi`

**In short:** OpenAI had isolated AI agents leak a secret through CPU cache timing, Spectre-style, and says the channels are slow and now monitored. I would say it is a clever demo, but the useful lesson is that isolation is a property of the whole machine, not just the VM boundary.

**Key points:**
- OpenAI locked agents in separate VMs on the same physical server and asked them to pass a secret with no network and no shared files.
- They used CPU cache timing: a slow read meant data had been pushed out, a fast read meant it had not, so reads became 0 and 1.
- The same family of trick was used by Spectre and Meltdown.
- They also found signals through shared storage and CPU busyness; one agent described an acoustic-modem-like signal from switching between writing and doing nothing.
- On September 20th one OpenAI model got limited internet access through a misconfigured DNS resolver, and OpenAI paused its most capable models for 11 days.
- OpenAI says most of these channels are slow and it is now monitoring for them in its setups.

**Details:** OpenAI locked agents in separate VMs on the same physical server, gave them source code and notes on known weak spots, and asked them to pass a secret. With no network and no shared files, they used the shared CPU cache: one agent pushed data out, the other timed the read back, slow meant evicted and fast meant present, so every read became a one or a zero. It is the same family of trick as Spectre and Meltdown.

They also found signals through shared storage and through how busy the CPU was, and in the storage case one agent described an acoustic-modem-like signal from switching between writing and doing nothing. The backstory is that on September 20th one OpenAI model got limited internet access through a misconfigured DNS resolver, and OpenAI paused its most capable models for 11 days. After that, it had teams of its strongest agents attack its own setup, sometimes with only a broad list of vulnerabilities.

OpenAI says most of these channels are slow and it is now monitoring for them. I would say the cache trick is the interesting part, the rest is the usual security theatre with better props, and the useful point is that isolation is a property of the whole machine. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 22. Personal Planner - daily planner with time tracking and reviews - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2019/04/notepad-pen-with-words-from-todo-list-multicolored-background.jpg)
**Source:** https://www.linuxlinks.com/personal-planner-daily-planner-time-tracking-reviews/ · **Karakeep:** `ta65y8nbd0rp28qowrq44t8j`

**In short:** Personal Planner is a free MIT-licensed daily planner written in Dart, with time tracking, reviews and optional sync through a user-controlled Supabase project. I would say it looks solid for one person on one machine, but it is not a fit for my homelab.

**Key points:**
- Developer Karthik Shabari; licence MIT; written in Dart.
- Runs offline with local storage; optional sync uses a user-controlled Supabase project.
- Day and week views, draggable resizable time blocks, recurring activities, timers, daily and weekly reviews, consistency heatmap, inbox, backlog, and backup and restore.
- Cross-platform on Linux, macOS and Windows; reminders and timer notifications on Linux and Android.
- No account required; pending offline changes are queued and synced when a connection is available.

**Details:** It is a desktop planner rather than a service: tasks sit on a timeline, a timer records actual duration, and the reviews compare planned time with spent time. The feature list is long for a single app, including templates, colour-coded categories, a historical overview, experiments against weekday and weekend targets, keyword search, and backup and restore. The sync is the only server-ish part, and it depends on Supabase rather than a plain API or database I would already run. For my homelab that matters: there is no Kubernetes path, no metrics story, and no backup story beyond the app's own export. For riffradar it is also a stretch, because that project is about guitar practice parts and history, not daily scheduling. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 23. Forget lightweight Linux, this forgotten OS is reviving ancient PCs, by How-To Geek
![](https://static0.howtogeekimages.com/wordpress/wp-content/uploads/wm/2026/10/haiku-os-running-on-vm-hero.jpg?w=1600&h=900&fit=crop)
**Source:** https://www.howtogeek.com/haiku-os-makes-more-sense-for-old-hardware-why-it-beats-linux-on-ancient-machines/ · **Karakeep:** `ui13ltd817bm4q96uwncdj1m`

**In short:** Haiku is the open-source BeOS successor with its own kernel and BFS file system, and R1/beta6 is pitched as a way to revive old PCs. I would say it is interesting as a desktop, but it is not a fit for my homelab or image box.

**Key points:**
- Open-source successor to BeOS, started as OpenBeOS in 2001 and renamed Haiku in 2004.
- It is not Linux or a Unix derivative; it has its own kernel, driver framework, graphical interface and bundled apps.
- BFS supports extended attributes and fast queries, so files can be searched almost like a database.
- Its package manager mounts compressed packages over the running system instead of unpacking them, which keeps installs clean and easy to roll back.
- The new R1/beta6 release is the version being promoted for old hardware.

**Details:** I read that Haiku is one cohesive system rather than a Linux distribution assembled from separate parts, and that is the bit I find appealing. It keeps POSIX compatibility, so porting software is easier, but the point is consistency and responsiveness on old machines. The article also notes that lightweight Linux keeps dropping older hardware, which is the gap Haiku is trying to fill.

The BFS and package manager details are the concrete parts I liked: extended attributes, fast queries, and installs that mount over the system instead of unpacking. I would say it is a nice piece of engineering and maybe worth a try on a spare box, but it is not stable enough in my head to replace anything I already run. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 24. Anthropic can’t stop winning, by Theo - t3․gg
![](https://i.ytimg.com/vi/y5TEATUDDfc/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=y5TEATUDDfc · **Karakeep:** `narjcxa3xluf492ist4yfz23`

**In short:** Theo walks through Anthropic's renamed Claude Ultra tier: the $200 plan drops the five-hour limit for verified accounts, while the old 20x label is admitted to have been misleading. I would say it is a limits cleanup with the usual Anthropic weirdness, not a reason to pay $200.

**Key points:**
- Four Claude plans: free, Pro at $20/month, Max at $100/month, Ultra at $200/month.
- Ultra is the old Max 20x plan renamed; the five-hour limit is removed for verified Ultra accounts, while Max keeps it.
- The 5x and 20x labels only ever described the five-hour limit; weekly limits are 10x Pro, and Anthropic's Mike apologised for the confusion.
- The $200 plan can cover up to $12,000/month of inference, with five-hour caps meant to stop one burst taking 10-15% of a week's allowance.
- T3 Code is affected because Agent SDK traffic gets a 50% cut to the five-hour limit; Theo says a merged entry-point change should avoid it.
- Usage peaks from 4 a.m. to 9 a.m. Pacific on weekdays, with a 2x gap between peak and evening lull.

**Details:** Anthropic's new Ultra tier is basically the old $200 Max plan with a cleaner name and one useful change: verified Ultra accounts lose the five-hour limit. The cheaper plans keep it, which is the annoying part, because that is where the limit bites hardest. Theo also explains the rename: 5x and 20x only ever referred to the five-hour window, while weekly limits are 10x Pro, and Mike from Anthropic apologised for letting people read it the other way.

The interesting bit is the compute story. The $200 plan can cover up to $12,000 a month in inference, but Anthropic does not want one person burning a week's allowance in one burst during peak hours. Their T3 Code analytics show prompting starts spiking around 4 a.m. Pacific on weekdays and peaks between 7 and 9 a.m., with a 2x gap to the evening lull. So the five-hour cap stops a user taking more than roughly 10 to 15% of their weekly allowance in one window.

There is also a T3 Code wrinkle: Agent SDK traffic was getting a 50% cut to the five-hour limit, which Theo calls obnoxious. He says a merged change to the Claude Code entry point should get around it, with semi-solid permission from Anthropic. I would say this is Anthropic being a bit more human than usual, but still selling addiction at $200 a month. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 25. 9 Best Free and Open Source Terminal-Based Volume Mixers - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2025/09/017-sound-mixer.png)
**Source:** https://www.linuxlinks.com/best-free-open-source-terminal-based-volume-mixers/ · **Karakeep:** `eqppfw85wsljobirijsma7wz`

**In short:** A LinuxLinks roundup of nine terminal volume mixers, mostly PulseAudio or PipeWire tools plus alsamixer for ALSA. I would say it is a handy index, not something I need.

**Key points:**
- Nine free and open source terminal-based mixers are listed: wiremix, pulsemixer, ncpamixer, PAmix, pacmixer, RsMixer, alsamixer, pulseaudio-mixer-cli and pipemixer.
- wiremix is described as a simple TUI mixer for PipeWire, while pipemixer is TUI volume control for PipeWire.
- pulsemixer, ncpamixer, PAmix, pacmixer, RsMixer and pulseaudio-mixer-cli are PulseAudio tools; alsamixer is for ALSA.
- LinuxLinks says only free and open source software is eligible and terminal-based tools only; a separate graphical mixer roundup exists.
- The page also says it was updated to reflect changes from a recent announcement, without giving details.

**Details:** This is a short index rather than a review. Each entry gets one line, so there is no depth on stability, packaging, or current maintenance. If I were setting up a headless Linux box, I would use it to pick a mixer for the audio stack in use: PipeWire tools for newer systems, PulseAudio tools where that is still the stack, and alsamixer for ALSA. For my own work it does not connect to anything. Nothing for my projects. I would say keep it as a bookmark and move on.

**For my projects:** Nothing for my projects.

**Projects:**
- [wiremix](https://github.com/tsowell/wiremix): Simple TUI audio mixer for PipeWire. Contribute to tsowell/wiremix development by creating an account on GitHub.
- [pulsemixer](https://github.com/GeorgeFilipkin/pulsemixer): CLI and curses mixer for PulseAudio. Contribute to GeorgeFilipkin/pulsemixer development by creating an account on GitHub.
- [ncpamixer](https://github.com/fulhax/ncpamixer): Ncurses PulseAudio Mixer. Contribute to fulhax/ncpamixer development by creating an account on GitHub.
- [PAmix](https://github.com/patroclos/PAmix): Ncurses/curses pulseaudio mixer in c similar to pavucontrol - patroclos/PAmix.
- [pacmixer](https://github.com/KenjiTakahashi/pacmixer)
- [RsMixer](https://github.com/jantap/rsmixer): PulseAudio volume mixer written in rust. Contribute to jantap/rsmixer development by creating an account on GitHub.
- [alsamixer](https://github.com/alsa-project/alsa-utils): The Advanced Linux Sound Architecture (ALSA) - utilities - alsa-project/alsa-utils.
- [pulseaudio-mixer-cli](https://github.com/mk-fg/pulseaudio-mixer-cli): Interactive python/ncurses UI to control volume of pulse streams with some automation - mk-fg/pulseaudio-mixer-cli.
- [pipemixer](https://github.com/heather7283/pipemixer): TUI volume control app for pipewire. Contribute to heather7283/pipemixer development by creating an account on GitHub.

## 26. RipperX 4 - GTK4 audio CD ripper written in Rust - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2018/01/colored-cdrom-white-background.jpg)
**Project:** [ripperx4](https://github.com/joske/ripperx4)
**Source:** https://www.linuxlinks.com/ripperx-gtk4-audio-cd-ripper/ · **Karakeep:** `lvwbgv3k4fbc5rzc1ba6vsah`

**In short:** RipperX 4 is a Rust and GTK4 audio CD ripper that uses GStreamer for extraction and encoding, with broad format and metadata support. I would say it looks like a solid small utility for anyone still ripping discs, but it has no place in my homelab and nothing for my projects.

**Key points:**
- Rust rewrite of ripperX with a GTK4 interface, by Jos Dehaes, under GPL v2.0
- Uses GStreamer for extraction and encoding instead of separate external encoders
- Outputs MP3, Ogg Vorbis, FLAC, Opus, AAC and WAV
- Reads CD-Text and does automatic MusicBrainz lookup with GnuDB fallback
- Configurable quality, filename patterns, error correction, M3U playlists and desktop notifications
- Runs on Linux, macOS and FreeBSD

**Details:** RipperX 4 is a graphical audio CD ripper and a modern rewrite of the original ripperX. The workflow is simple: select tracks, pull album information, convert to digital files. It handles lossless and lossy encoding, so it covers both archival copies and everyday listening. GStreamer does the extraction and encoding, and the interface keeps the ripping options simple rather than exposing complex audio pipelines. It reads CD-Text from compatible discs, looks up metadata through MusicBrainz with GnuDB fallback, and writes tags automatically. You can edit titles and artists before extraction, set quality, use filename presets, generate M3U playlists, and adjust CD error correction. It warns before overwriting files, can notify when done, and can eject the disc and open the destination folder. It is free and open source under GPL v2.0. The catch for me is that it is a desktop GUI with no Kubernetes path, no backup story and no metrics, so it is not going into homelab-2nd without a fight. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 27. 9 Best Free and Open Source Linux Network Authentication Servers - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2017/12/server-vector.png)
**Source:** https://www.linuxlinks.com/networkauthenticationservers/ · **Karakeep:** `hpza1d5a20bo2t4fnpycah65`

**In short:** LinuxLinks rounded up nine free and open source Linux network authentication servers, with Keycloak and FreeRADIUS getting the strongest recommendation. I would say those two are the sensible starting points, and the rest only matters if you actually need RADIUS.

**Key points:**
- Nine servers are listed: Keycloak, FreeRADIUS, authentik, PacketFence, Logto, Kanidm, RADIUSdesk, privacyIDEA and Radius.
- LinuxLinks gives its strongest recommendation to Keycloak and FreeRADIUS.
- RADIUS covers centralized authentication, authorization and accounting for network access.
- It started with large modem banks and now underpins appliances, wireless, VPNs and ISP DSL and cable connections.
- Only free and open source software is eligible for inclusion.

**Details:** RADIUS is old but still does the plumbing: centralized auth, authorization and accounting for network access. It started with big modem banks and now shows up in appliances, wireless, VPNs and ISP DSL and cable. The useful bit is that these servers can run on any network that wants centralized auth or accounting, not just an ISP.

LinuxLinks likes Keycloak and FreeRADIUS most. Keycloak is the modern identity and access management one, FreeRADIUS is the high-performance configurable RADIUS server. authentik adds SSO and RADIUS, PacketFence does 802.1X and RADIUS access control, Logto is positioned as a modern Auth0 alternative, Kanidm has LDAP, OAuth2 and RADIUS, RADIUSdesk is a management platform, privacyIDEA is MFA for VPNs and network access, and Radius covers remote user auth and accounting plus utilities.

For my homelab the interesting names are Keycloak and authentik, because a single OIDC provider in front of the public services would beat per-app logins. RADIUS itself is probably overkill unless I start doing 802.1X on the LAN. So yeah, that's that.

**For my projects:**
- homelab-2nd: Use Keycloak or authentik as the single OIDC provider for the public services, but only if it has a Kubernetes deployment path, a backup story and metrics.

**Projects:**
- [Keycloak](https://www.keycloak.org/): Keycloak - the open source identity and access management solution. Add single-sign-on and authentication to applications and secure services with minimum effort.
- [FreeRADIUS](https://www.freeradius.org/): The world.
- [authentik](https://github.com/goauthentik/authentik): The authentication glue you need. Contribute to goauthentik/authentik development by creating an account on GitHub.
- [PacketFence](https://www.packetfence.com/): Enterprise NAC for network security, device compliance, and guest access. Cloud or self-hosted. Trusted by organizations worldwide.
- [Logto](https://logto.io): Logto adds multi-tenancy, enterprise SSO, and RBAC to your SaaS or AI apps. All with OIDC and OAuth 2.1 made simple, fast, and developer-friendly.
- [Kanidm](https://github.com/kanidm/kanidm): Kanidm: A simple, secure, and fast identity management platform - kanidm/kanidm.
- [RADIUSdesk](https://www.gnu.org/software/radius/)
- [privacyIDEA](https://github.com/privacyidea/privacyidea): Closed_lock_with_key: multi factor authentication system (2FA, MFA, OTP, FIDO Server) - privacyidea/privacyidea.
- [Radius](https://www.gnu.org/software/radius/)

## 28. Google Drive stopped sending my folders to Google Photos, so I built a photo backup server that doesn’t need Google at all, by XDA
![](https://static0.xdaimages.com/wordpress/wp-content/uploads/wm/2026/10/immich-server-ui.jpg?w=1600&h=900&fit=crop)
**Source:** https://www.xda-developers.com/build-a-photo-backup-server-that-skips-google/ · **Karakeep:** `xtuw4l9mcyv6mxwph3waj0r3`

**In short:** Immich is a self-hosted photo and video server that replaces Google Photos after Google stopped Drive desktop uploads to Photos. I read the build story; it looks workable on modest hardware, but it is still a manual Docker job with no backup story shown.

**Key points:**
- Google Drive for desktop no longer uploads images to Google Photos.
- Immich stores and serves photos and videos locally, with OCR, metadata and thumbnail jobs in the background.
- The author used an HP t620 thin client with 8GB DDR3 memory and a 128GB M.2 SATA SSD, costing nearly $50.
- DietPi in non-desktop mode used about 250MB memory; 512MB and 1GB SBCs are not enough, while 4GB systems such as a Raspberry Pi 5 can run all features.
- Photos can be uploaded through the web UI or synced with the Immich CLI using an API key.
- The CLI login command shown is `immich login http://serveriP:2283/api YOUR_API_KEY`.

**Details:** Immich is the Google Photos replacement in this piece. The author moved after Google changed Drive for desktop so it no longer sends images into Photos, and because the free storage was not enough anyway. The server runs on an HP t620 thin client with 8GB of memory and a 128GB SSD, under Docker and DietPi, and the author says the old quad-core chip still handles it. Uploads can be done by hand in the web UI, or by CLI with an API key, and phones can browse the library through the app or browser. It also runs OCR, metadata and thumbnail jobs in the background.

The honest caveat is that this is still a self-hosted service you feed yourself. The article shows a single machine and no backup, metrics or Kubernetes path, so it does not slot into my homelab without more work. For my projects, I would say nothing fits right now: RiffRadar is unrelated, ideogram4-local is about local image generation, and homelab-2nd would need a proper deployment and backup story first. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 29. Image annotation in Python with polygons, rectangles, circles, and points, by Open-source Projects
![](https://opengraph.githubassets.com/1/wkentaro/labelme)
**Project:** [labelme](https://github.com/wkentaro/labelme)
**Source:** https://www.opensourceprojects.dev/post/labelme · **Karakeep:** `qydto65u3nkxx8jpahb0sn0m`

**In short:** Labelme is a Python desktop tool for annotating images and video with polygons and other shapes, with VOC and COCO export and optional SAM or YOLO assistance. I would say it looks like a mature, practical dataset tool, but it is not something I need for my own projects.

**Key points:**
- Python and Qt desktop annotation tool inspired by MIT's original LabelMe project.
- Supports polygons, rectangles, circles, lines, points, image-level flags, and video annotation.
- Exports VOC-format datasets for semantic and instance segmentation and COCO-format datasets for instance segmentation.
- AI assistance includes point-to-polygon and mask annotation with SAM and EfficientSAM, plus text-to-annotation with YOLO-world and SAM3.
- 20 languages are available, and a standalone app is offered at labelme.io.
- Install with pip install labelme, then run labelme; examples cover detection, classification, segmentation, and video.

**Details:** Labelme is aimed at building computer vision datasets without forcing you into a general image editor. It runs as a native Qt desktop app, lets you draw and label shapes, and handles image-level flags and video. The export support is the useful part for me: VOC for semantic and instance segmentation, COCO for instance segmentation. The article also lists AI assistance using SAM, EfficientSAM, YOLO-world and SAM3, which could cut down the dull boundary tracing, though I have not tried it. There is a standalone app as well, so not everyone needs a Python setup. It has examples for semantic segmentation, instance segmentation, bbox detection, classification and video annotation, plus a Discord community. For my setup, it is not a fit: my homelab needs Kubernetes paths and backups, and my local image work is about generation and control rather than labelling datasets. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 30. A 100% open source IoT platform you can run with docker compose, by Open-source Projects
![](https://opengraph.githubassets.com/1/openremote/core)
**Project:** [core](https://github.com/openremote/core)
**Source:** https://www.opensourceprojects.dev/post/core-28 · **Karakeep:** `lruyeupvqej4bnf6jcnnkhex`

**In short:** OpenRemote Core bundles device management, rules, dashboards and protocol agents into one fully open source IoT stack you can start with Docker Compose. I would say it is interesting for IoT builders, but it has no obvious place in my projects.

**Key points:**
- Fully open source IoT platform with device management, auto provisioning, custom asset types and an Insights dashboard builder.
- Automation covers when-then rules, flows, JavaScript and Groovy.
- Connects through an MQTT broker plus HTTP/REST and WebSockets, with multi-tenancy via realms and an edge gateway.
- Ships as amd64 and arm64 Docker images; quickstart needs Docker Desktop v18 or newer.
- Demo login is smartcity:smartcity; local Manager UI login is admin with password secret.
- Source is at github.com/openremote/core; candidate link [2] is the repo.

**Details:** OpenRemote Core is a self-hosted IoT platform that puts device management, automation, analytics and dashboards in one stack, and the code is fully open. Unfortunately it is a Docker Compose quickstart, not a Kubernetes deployment, and the page says nothing about backups, metrics or GitOps, so it is not going into homelab-2nd without a fight. It does have a lot in one place: provisioning, custom asset types, four automation styles, multi-tenancy through realms, role management and an edge gateway. ARM support is handy for edge boxes, and Docker Desktop v18 or newer is the stated requirement, which that's reasonable. The demo credentials are smartcity:smartcity and the local login is admin with password secret, which is at least easy to try. I see no fit for RiffRadar or ideogram4-local, and for the homelab the missing Kubernetes path and backup story matter more than the feature list. Nothing for my projects. So yeah, that's that.

**For my projects:** Nothing for my projects.

## 31. yutto: a CLI Bilibili video downloader with stream selection and ASS danmaku, by Open-source Projects
![](https://opengraph.githubassets.com/1/yutto-dev/yutto)
**Project:** [yutto](https://github.com/yutto-dev/yutto)
**Source:** https://www.opensourceprojects.dev/post/yutto · **Karakeep:** `cxh9jf4sr10b04hq6adixq2j`

**In short:** yutto is a Python CLI for downloading Bilibili videos with stream selection and ASS danmaku. I would say it is worth a look if you download Bilibili content regularly, but it is too specific for my projects.

**Key points:**
- Python CLI distributed on PyPI; requires Python 3.11+ and configured FFmpeg
- Lists every available stream; README example shows 15 video streams across AVC, HEVC and AV1 from 1080P to 360P plus three audio streams
- Generates ASS danmaku and supports premium account login, with example output showing a successful 大会员 login
- Reads options from yutto.toml
- Install via Homebrew, AUR or archlinuxcn, Docker, pip, pipx or uv; Docker mounts the download directory to /app or $(pwd)
- Bug reports go to Issues; general questions go to Discussions

**Details:** yutto is a Python command-line downloader for Bilibili. It lists every available video and audio stream before downloading, so you can pick codec, resolution and bitrate instead of accepting a preset. The README example shows 15 video streams across AVC, HEVC and AV1 from 1080P down to 360P, plus three audio streams, with the default marked with an asterisk. It also writes ASS danmaku, supports premium login, and reads options from yutto.toml. Python 3.11+ and configured FFmpeg are required.

Install paths include Homebrew, AUR or archlinuxcn, Docker, pip, pipx and uv; Docker mounts the download directory to /app or $(pwd). The Windows install section is truncated in what is shown, so check the full docs. I read about it, I did not try it. For me, nothing for my projects, since none of my projects need Bilibili downloads. I would say it is worth a look if you download Bilibili content regularly and care about codec choice or keeping danmaku; otherwise it is a bit too specific.

Yeah, that's that.

**For my projects:** Nothing for my projects.

## 32. YouTube downloading module for Node with a streaming interface, by Open-source Projects
![](https://www.opensourceprojects.dev/images/open-source-logo-830x460.jpg)
**Project:** [node-ytdl-core](https://github.com/fent/node-ytdl-core)
**Source:** https://www.opensourceprojects.dev/post/node-ytdl-core · **Karakeep:** `bj1z8a8cxc0x4qp2ow2zozn7`

**In short:** A Node module for downloading YouTube content with a streaming interface. I would say it is not worth it for my projects because the article body was missing and I have no concrete fit.

**Key points:**
- Title: YouTube downloading module for Node with a streaming interface.
- Candidate link 1 points to fent/node-ytdl-core on GitHub.
- No article body was available, so version, licence and features are not stated.
- I have no project that needs YouTube downloads.

**Details:** This is a Node module for downloading YouTube content with a streaming interface, and the only concrete source I have is candidate link 1 to fent/node-ytdl-core. Unfortunately the article body was not available, so I cannot say what version it is, what licence it uses, or what it does beyond the title. I read about it, I did not run it, so this is just a description and a judgement. I would say it is interesting as a building block if I ever needed to pull media in Node, but it is not worth it for my projects right now. Nothing for my projects. Yeah, that's that.

**For my projects:** Nothing for my projects.

## 33. A modular Agentic RAG built on LangGraph, with query clarification and self-corr..., by Open-source Projects
![](https://opengraph.githubassets.com/1/giovannipasq/agentic-rag-for-dummies)
**Project:** [github.com](https://github.com/giovannipasq/agentic-rag-for-dummies)
**Source:** https://www.opensourceprojects.dev/post/agentic-rag-for-dummies · **Karakeep:** `zczu25gswoyac316im0qp4q2`

**In short:** Agentic RAG for Dummies is a modular LangGraph RAG with query clarification, self-correction, conversation memory and Qdrant. I would say it is worth a look if you have hit the basic RAG wall, yeah, but not as something you just run.

**Key points:**
- Built on LangGraph 1.2+, Python 3.11+ and Qdrant as the vector database
- Two paths: an interactive notebook and a modular app with swappable LLM provider, embedding model, PDF converter and agent workflow
- Ollama-first runnable app, with examples for Anthropic, OpenAI and Google
- Features include hierarchical indexing, query clarification, self-correction, context compression, multi-agent map-reduce and conversation memory
- Observability via Langfuse and evaluation with RAGAS metrics
- MIT-licensed and listed on awesome-langgraph; repo is giovannipasq/agentic-rag-for-dummies

**Details:** Agentic RAG for Dummies is a modular retrieval-augmented generation system built on LangGraph, with query clarification, self-correction, conversation memory, hierarchical indexing, multi-agent map-reduce and context compression. It comes as an interactive notebook and a modular app where the LLM provider, embedding model, PDF converter and agent workflow can be swapped; the app defaults to Ollama, with examples for Anthropic, OpenAI and Google. The stack is Python 3.11+, LangGraph 1.2+, which that's recent enough for a project like this, and Qdrant.

The feature list is basically the list of things that annoy you about naive RAG: vague queries, a missed first retrieval, no memory and token bloat. Human-in-the-loop query clarification is the standout for me, and having Langfuse observability plus RAGAS evaluation built in is practical because those are painful to bolt on later. What is still missing is a production deployment story; what is there is the architecture and the learning path. It is MIT-licensed and listed on awesome-langgraph. I would say it is worth a look if you have hit the basic RAG wall, and skip it if you need a service you can just run. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 34. A staged learning map from LLM basics to reliable Agent systems, by Open-source Projects
![](https://opengraph.githubassets.com/1/wenyuchiou/awesome-agentic-ai-zh)
**Project:** [wenyuchiou.github.io](https://wenyuchiou.github.io/awesome-agentic-ai-zh/), also [awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh)
**Source:** https://www.opensourceprojects.dev/post/awesome-agentic-ai-zh · **Karakeep:** `xgzttd5ovv7ng50n14ilkehg`

**In short:** A staged learning map for agentic AI, from LLM basics to reliable agent systems, with tracks for CLI users, builders and everyday users. I would say it is useful if sequencing is your blocker, and less useful if you already ship agents.

**Key points:**
- Stages 0 to 8 plus Stage 7.5, ten learning stations in total.
- Track A for CLI power users, Track B for building agents, plus an everyday-users route.
- Written mainly in Traditional Chinese, with Simplified Chinese and English versions available.
- MIT-licensed roadmap that points to official docs and cookbooks instead of duplicating them.
- Defines an agent as goal-directed, tool-using, and able to correct, stop or hand control back.

**Details:** I have only read the README, so this is a description rather than a review of use. awesome-agentic-ai-zh is a learning map for agentic AI, not a full textbook. It runs from Stage 0 to Stage 8 plus Stage 7.5, with Stages 0 to 2 as shared foundations, then splits into Track A for CLI power users and Track B for people building their own agents, tool loops, workflows and services. There is also a route for everyday users who just want to use AI safely. Terms are explained in plain language first, with the formal English term kept alongside, and there is a glossary. The README points to official docs, Datawhale Hello-Agents and cookbooks instead of rewriting them, which keeps it maintainable. The catch is language: the primary content is Traditional Chinese, with Simplified Chinese and English versions available, so reading comfort matters. I would say the strict definition of an agent and the reliability stages are the useful bits.

**For my projects:** Nothing for my projects.

## 35. An Android image toolbox built with Kotlin and Jetpack Compose, by Open-source Projects
![](https://opengraph.githubassets.com/1/t8rin/imagetoolbox)
**Project:** [github.com](https://github.com/t8rin/ImageToolbox.git)
**Source:** https://www.opensourceprojects.dev/post/imagetoolbox · **Karakeep:** `ma8ywrg6cb26l0njiaack109`

**In short:** An open-source Android image toolbox built in Kotlin with Jetpack Compose; it looks maintained and has a real release pipeline, but the README is thin on features, so I would treat it as a clone-and-look project.

**Key points:**
- Open-source Android image toolbox built in Kotlin with Jetpack Compose.
- Targets API 24 and up.
- Material You theming.
- README badge says over 563,000 lines of code.
- Ships through GitHub Releases, with Fastlane metadata set up.
- README does not list the specific tools or transformations.

**Details:** Image Toolbox is an Android image app written in Kotlin with Jetpack Compose, targeting API 24 and up, with Material You theming. The repository is large, the README badge says over 563,000 lines of code, and it ships through GitHub Releases with Fastlane metadata set up.

The catch is the README: it leans on badges and a logo, and does not list the actual tools or transformations. So I can say it looks like a maintained Compose app with a real release pipeline, but I cannot tell you what it actually does beyond image operations. If I wanted it, I would clone it and poke around. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 36. Live streaming software built on Electron and OBS, with async IPC and a worker w..., by Open-source Projects
![](https://opengraph.githubassets.com/1/streamlabs/desktop)
**Project:** [desktop](https://github.com/streamlabs/desktop)
**Source:** https://www.opensourceprojects.dev/post/desktop · **Karakeep:** `kmk2vuji87ukczpsymdqi3m5`

**In short:** Streamlabs Desktop is open-source live streaming software built on Electron and OBS, and the useful part for me is the README's multi-window architecture and async-first IPC guidance rather than the streaming app itself. I would say the app is too large to drop in casually, but the worker-window and IPC patterns are worth stealing.

**Key points:**
- Open-source live streaming software built on Electron and OBS; supports macOS 10.14+ and 64-bit Windows.
- Uses a persistent invisible worker window for the services layer, plus a pre-warmed child window for instant windows like Source Properties.
- IPC guidance favours async: StreamingService.toggleStreaming() becomes StreamingService.actions.toggleStreaming(), and actions are void.
- State reads use views backed by a Vuex store replicated across windows.
- Dev setup needs Node.js (latest LTS recommended), Yarn and a bash-like shell; run yarn install, yarn compile and yarn start.
- Environment variables include SLOBS_PRODUCTION_DEBUG, SLOBS_CACHE_DIR and SLOBS_REPORT_TO_SENTRY.

**Details:** Streamlabs Desktop is open-source live streaming software built on Electron and OBS, supporting macOS 10.14+ and 64-bit Windows. I read about the architecture rather than the product, and the interesting part is the window split: a persistent invisible worker runs the whole services layer, the main window talks to it, and a pre-warmed child window keeps Source Properties from taking several seconds to open. Other processes spin up for Apps, webviews and projectors.

The transferable bit is IPC discipline: async is strongly recommended, StreamingService.toggleStreaming() becomes StreamingService.actions.toggleStreaming(), actions are void, and views backed by a replicated Vuex store handle reads. That is a clean separation, and I would say worth stealing for heavy IPC.

Bad news: it is a large application with a real build pipeline and platform constraints, so not a casual side project. You need Node.js (latest LTS recommended), Yarn and a bash-like shell, then yarn install, yarn compile and yarn start. I would say read the architecture section first, then the code.

**For my projects:** Nothing for my projects.

## 37. The Era of Tokenmaxxing Is Over, by Better Stack
![](https://i.ytimg.com/vi/_aP3KSnYBbU/maxresdefault.jpg)
**Source:** https://www.youtube.com/shorts/_aP3KSnYBbU · **Karakeep:** `oim1oh47q4vcx9ofvmvwaq7z`

**In short:** Better Stack short on companies capping AI coding spend: Accenture at $29 a month, Uber at $1,500. I would say tokenmaxxing ending is good news, because ranking engineers by token burn was always a dumb metric.

**Key points:**
- Accenture will now pay $29/month for many employees' Claude, down from up to $1,000/month for some staff
- Internal memo seen by 404 Media; Accenture says there is no firm limit
- Accenture signed a huge Claude Code deal with Anthropic last December
- Anthropic docs: average big-company Claude Code user spends about $13/day
- Uber spent its full-year AI budget in the first few months, then capped employees at $1,500/month per AI coding tool
- Amazon engineering leaders told staff that token-usage metrics are deeply flawed

**Details:** Accenture, which signed that big Claude Code deal with Anthropic last December, is now paying $29 a month for many employees' Claude instead of the up to $1,000 some staff were burning. Going over gets charged to the project or team budget, and Accenture says there is no firm limit, which is a little bit weird next to a $29 allowance, but yeah.

The reason the bill balloons is that coding agents resend the whole conversation on every step, so a long run gets more expensive per step, not less. Anthropic's own docs put the average big-company Claude Code user at about $13 a day, so Accenture's monthly allowance is gone in roughly two and a half days of work. That is tight. It is not just Accenture either: Uber spent its whole-year AI budget in the first few months and capped everyone at $1,500 a month per coding tool, and Amazon's engineering leaders have told staff that token-usage metrics are deeply flawed. So the era of ranking engineers by how much AI they burn is over. I would say that is a good thing.

**For my projects:** Nothing for my projects.

## 38. Carve - Find and remove unused Clojure code - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2026/09/Linter-Tool-Banner2.png)
**Source:** https://www.linuxlinks.com/carve-find-remove-unused-clojure-code/ · **Karakeep:** `sfvl9ov7m3n5vyl0ubx9d7yj`

**In short:** Carve is a free Clojure cleanup tool from Michiel Borkent that finds unused vars and functions, and can remove them with rewrite-cljc. I would say it is useful for old Clojure codebases, but it has no fit for my projects.

**Key points:**
- Developer: Michiel Borkent; licence: Eclipse Public License v1.0.
- Uses clj-kondo to find unused vars and functions, then rewrite-cljc to edit source files.
- Modes include interactive review, dry-run, aggressive repeat passes and CI failure on unused code.
- Also cleans unused :require references and can write changes to a separate output directory.
- Runs on Linux, macOS and Windows; output can be text, EDN or an ignore list.

**Details:** Carve is aimed at Clojure maintenance work: finding dead definitions, trimming namespace requires, and either editing files or producing a report. It can be run interactively, as a dry run, or in CI, and it has ignore lists plus an aggressive mode that repeats until nothing else is found. The main caveat is dynamic references and tests, so proposed removals still need review. I do not have a Clojure project in my stack, so this is just a neat utility to note rather than something I would adopt. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 39. Cursor Just Served Malware to Up to 5,000 Users #cursor #cybersecurity #programming, by Better Stack
![](https://i.ytimg.com/vi/x7WoalmJM80/maxresdefault.jpg)
**Source:** https://www.youtube.com/shorts/x7WoalmJM80 · **Karakeep:** `fy5rw7t7qr6tr083w7nl74ha`

**In short:** Cursor's extension store served a tampered Claude Code extension for about 11 hours, and Cursor says over 5,000 users could have been hit. I would say it is a bummer, and if you installed it you should treat the machine as compromised.

**Key points:**
- About 11 hours of exposure on the 29th of October.
- Listed under Anthropic's name, but Anthropic says it did not build or publish it.
- Fake extension for Mac and Windows sent username, git email and public IP, and added the attacker's SSH key.
- It retried a reverse tunnel every minute, even after restart, but needed Cursor run as administrator.
- Cursor pulled it, shut the store, rotated keys and rebuilt; official VS Code, OpenVSX and NPM versions were not affected.
- Uninstalling may not stop the backdoor; run Cursor's check script and change passwords and keys from another computer.

**Details:** Better Stack's short says someone used access to Cursor's store to publish a tampered Claude Code extension, and Cursor says it could have impacted over 5,000 users. The extension would send your username, git email and public IP, add an attacker SSH key, then try a reverse tunnel every minute. Luckily the tunnel needed Cursor started as an administrator, and the attacker server is now offline. Cursor pulled the extension, shut down the store, rotated keys and rebuilt it. Anthropic and GitHub's CTO say the official versions on Microsoft's VS Code marketplace, OpenVSX and NPM were never affected, so this only matters if you were a Cursor user. If you were, uninstalling might not be enough, so run the check script in Cursor's write-up and change passwords and keys from another computer. We still do not know how the attacker got store access. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 40. docformatter - automatic formatter for Python docstrings - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2026/09/Code-Formatter-banner1.png)
**Project:** [docformatter](https://github.com/PyCQA/docformatter)
**Source:** https://www.linuxlinks.com/docformatter-automatic-formatter-python-docstrings/ · **Karakeep:** `qj24ihbp0huw2vhbkw4sqhdh`

**In short:** docformatter is a CLI that rewrites Python docstrings to a subset of PEP 257, and I would say it is worth a look for repos with docstrings, with nothing for my projects.

**Key points:**
- CLI utility from Steven Myint and PyCQA contributors, MIT licensed, written in Python.
- Formats docstrings only, not surrounding Python code; companion to Black.
- Normalises triple quotes, indentation, whitespace and summary formatting; configurable line wrapping.
- Supports Sphinx and Epytext parameter lists, in-place edits, check mode and diff output.
- Config via pyproject.toml; integrates with pre-commit, GitHub Actions and PyCharm watchers.
- Runs on Linux and macOS; recursive directory processing with exclusions.

**Details:** docformatter takes Python docstrings and normalises them to a subset of PEP 257, so triple quotes, indentation, whitespace and summary lines stop drifting between contributors. It leaves the code around them alone, which is why it sits next to Black. The feature list is practical: configurable wrapping, Sphinx and Epytext parameter lists, in-place edits, check mode, diff output, recursive directories with exclusions, and config through pyproject.toml. It also hooks into pre-commit, GitHub Actions and PyCharm watchers. I read about it, I did not run it, so I cannot say how tidy the output feels on a messy module. My honest take is that it is a narrow tool for a narrow job, and if your docstrings are already mostly fine, the gain is small. It is MIT licensed and cross-platform on Linux and macOS, which is at least one less excuse not to try it. Nothing for my projects.

**For my projects:** Nothing for my projects.
