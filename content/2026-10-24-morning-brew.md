---
date: 2026-10-24
slug: 2026-10-24-morning-brew
tags: Operating Systems, Wayland, Linux Distribution, Ubuntu, Tiling Window Manager, Linux, Open Source Software, System Administration, Troubleshooting, Log Analysis, Multimedia, Audio Conversion, Batch Processing, Cybersecurity
---

Morning Brew for 2026-10-24: 27 items written from 27 hoarded bookmarks and feeds, 0 dropped after a failed retry.

### RSS

## 1. LumaOS - Ubuntu-based Linux distribution featuring Niri - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2024/04/Linux-Distributions.png)
**Source:** https://www.linuxlinks.com/lumaos-ubuntu-based-linux-distribution-featuring-niri/ · **Karakeep:** `mtc6qe46vbrgz3lt86ssuw83`

**In short:** LumaOS is an Ubuntu-based desktop distribution built around the Niri scrollable-tiling Wayland compositor. I would say it is a niche preconfigured desktop, and it has nothing for my projects.

**Key points:**
- Ubuntu-based, with APT package management and a graphical installer.
- Built around Niri, a scrollable-tiling Wayland compositor with horizontally scrolling workspaces.
- Deep-space aesthetic across Niri and the bundled desktop utilities.
- Active project by Luciano Magri; fixed release model on x86_64.
- Aimed at users who want scrollable tiling without assembling the parts.

**Details:** LumaOS is a fixed-release Ubuntu derivative that ships Niri as its desktop, plus a set of utilities and custom applications in a consistent deep-space look. Niri puts windows in a horizontally scrolling workspace instead of fixed tile layouts, and the distribution is aimed at people who want that preconfigured rather than built by hand. It keeps systemd and APT, and a graphical installer is provided.

Unfortunately it is a desktop OS with no Kubernetes path, no backup story and no metrics, so it is not going into homelab-2nd. It is x86_64 only, which that's a limit for my M1 Max, and it has no place in RiffRadar. I would say it is worth a look if you want Niri ready-made, and not worth it for my setup. So yeah, that's that.

**For my projects:** Nothing for my projects.

## 2. 11 Best Free and Open Source Linux System Log and systemd Journal Viewers - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2026/09/Logfile-viewer1.png)
**Source:** https://www.linuxlinks.com/best-free-open-source-linux-system-log-systemd-journal-viewers/ · **Karakeep:** `hz2pfse19n9iavnq7bxhzecz`

**In short:** LinuxLinks rounds up eleven free and open source Linux log and systemd journal viewers. It is a useful catalogue if raw journal output is wearing you down, but it does not pick a clear winner.

**Key points:**
- Eleven tools are listed, and all are free and open source.
- journalctl is the baseline command-line access to system events and diagnostic messages.
- The rest range from KDE, GNOME, Qt and Deepin GUI viewers to terminal tools such as SEE and LogLens.
- Grafito is the self-hosted web option with live updates and filtering.
- systemd_commander is described as a graphical interface for managing services and their status.
- No versions, prices or benchmark numbers are given in the roundup.

**Details:** Raw logs are a pain, and systemd journals are structured but still dense. This roundup covers eleven viewers, from journalctl itself to KDE Journald Browser, KSystemLog, GNOME Logs, QJournalctl, SEE, Journal Viewer, Deepin Log Viewer, Grafito, systemd_commander and LogLens. The useful split is GUI versus terminal: some are desktop tools for browsing and searching, while SEE and LogLens are keyboard or interactive terminal options. Grafito stands out as the self-hosted web one with live updates and filtering. I would say the page is more a catalogue than a verdict, because it does not compare performance or give versions. For my homelab, none of these come with a Kubernetes path, backup story or metrics, so they would need a fight to get in. So yeah, that's that.

**For my projects:** Nothing for my projects.

**Projects:**
- [journalctl](https://systemd.io/CATALOG/): Journal Message Catalogs.
- [KSystemLog](https://apps.kde.org/ksystemlog/): System log viewer.
- [GNOME Logs](https://www.gnome.org/): An easy and elegant way to use your computer.
- [QJournalctl](https://github.com/pentix/qjournalctl): A multi-platform, Qt-based frontend for systemd's journalctl command. Accepting local as well as remote (SSH) data sources.
- [SEE](https://github.com/NustyFrozen/SEE): See (Service Event Extraction) is a TUI based tool to lookup logs from services (systemd) - NustyFrozen/SEE.
- [Journal Viewer](https://github.com/mingue/journal-viewer): Visualize your systemd logs with filters, themes... built on Rust &amp; Vue - mingue/journal-viewer.
- [Deepin Log Viewer](https://github.com/linuxdeepin/deepin-log-viewer): Contribute to linuxdeepin/deepin-log-viewer development by creating an account on GitHub.
- [Grafito](https://github.com/ralsina/grafito): A simple, nice journald web frontend. Contribute to ralsina/grafito development by creating an account on GitHub.
- [systemd_commander](https://github.com/systemd/systemd): The systemd System and Service Manager . Contribute to systemd/systemd development by creating an account on GitHub.
- [LogLens](https://github.com/nirakar24/loglens): A powerful Linux log processing engine with an interactive Terminal UI for viewing and analyzing system logs. Think of it as a Linux equivalent to Windows Event Viewer. - nirakar24/Loglens.

## 3. Transition - graphical multimedia to audio converter - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2022/02/Audio-Editors.jpg)
**Project:** [transition](https://codeberg.org/grinka/transition)
**Source:** https://www.linuxlinks.com/transition-graphical-multimedia-audio-converter/ · **Karakeep:** `xbt1rdvq5r1atunw5kwrkkpp`

**In short:** Transition is a Rust, GPL v3 graphical Linux converter for turning audio and video files into audio; I would say it is a tidy front-end for a common job, but there is nothing here for my projects.

**Key points:**
- Graphical audio and video-to-audio converter for Linux, written in Rust.
- Licensed under GNU GPL v3; developer is Oleksii Tishchenko.
- Project website and source are on Codeberg.
- Outputs Ogg Opus, Ogg Vorbis, MP3, FLAC and WAV; handles batches and video soundtracks.
- Can set channel count, adjust format-specific quality, remember preferences and replace originals.
- Adaptive layout keeps controls usable on narrower screens.

**Details:** Transition is a graphical converter for turning audio and video files into audio on Linux, aimed at people who do not want to build FFmpeg commands or open a full audio editor. The workflow is selecting a batch of source files, choosing output settings and starting the job, with mixed audio and video sources in one queue. It can extract a soundtrack, set channels, adjust quality per format, avoid raising quality on already low sources unless that behaviour is disabled, remember preferences and replace originals.

It is written in Rust by Oleksii Tishchenko, licensed under GPL v3, and the website points to Codeberg. Five output formats cover most storage and playback needs, which that's plenty for a small converter, and the adaptive layout is a sensible touch for narrow screens. I would say it looks like a tidy front-end for a common task, and there is nothing here for my projects.

**For my projects:** Nothing for my projects.

## 4. Signal Calls Could Keep Going After You Hang Up #signal #security #programming, by Better Stack
![](https://i.ytimg.com/vi/MIcqHQ4jAFg/maxresdefault.jpg)
**Source:** https://www.youtube.com/shorts/MIcqHQ4jAFg · **Karakeep:** `gibu0e1lsx2e0vibb3ane2sf`

**In short:** Signal had a critical 9.3 bug in Ring RTC where pressing hang up did not always end the call, and the other person could keep hearing or seeing you. I would say update Signal, it is a bummer, but it only affected calls already in progress.

**Key points:**
- Rated 9.3 critical; in Ring RTC, the open source library Signal uses for voice and video calls.
- Flooding the call's internal queue could stop hang up from tearing the call down, including audio and perhaps video.
- Fixed on 4 September; changelog only says ensure calls terminate completely in corner cases, with no security wording.
- Rolled out to Android, iPhone and desktop over the following weeks; CVE made public on 20 October.
- Only someone already on the call could do it; messages, account and encryption were not touched, and there is no evidence anyone used it.

**Details:** This is the kind of bug that makes you stare at the red button. Someone already on a Signal call could flood the call's internal queue, so your hang up did not tear the call down, and they could keep hearing you and maybe seeing you. It was fixed on 4 September, but the changelog only had one bullet, ensure calls terminate completely in corner cases, with nothing saying it was a security fix, and the CVE only went public on 20 October. That is a bit wonky, and the gap between fix and disclosure is the part I would grumble about. The rest is bounded: only someone you were already on a call with could do it, your messages, account and encryption were not touched, and there is no evidence anyone used it. Signal is not alone here either, FaceTime had a similar 2019 bug and Project Zero found the same pattern in Google Duo and Facebook Messenger. So yeah, update Signal and move on. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 5. 2026 Linux Maintainers Summit Was All About AI, by Brodie Robertson
![](https://i.ytimg.com/vi/ObKIuIzFzYs/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=ObKIuIzFzYs · **Karakeep:** `y8j5yyu58g57q3bbk0o53b7t`

**In short:** Brodie Robertson walks through Jonathan Corbett's LWN report on the 2026 Linux Maintainers Summit, and it is mostly an argument about AI-generated patches, reviews and forks. I would say it is more useful as a temperature check on kernel culture than as technical news.

**Key points:**
- Brodie Robertson covers Jonathan Corbett's LWN write-up of the 2026 Linux Maintainers Summit.
- Sushka, an agentic review tool for kernel patches, sat at the centre of the review discussion.
- Torvalds says LLMs can do good work, but only in competent hands; his own setup took six months.
- One reported flood was well over 100 patches from a new identity within an hour.
- The summit also touched private kernel forks, succession and how attendees are selected.
- No decisions were made on succession; that discussion moves to a mailing list.

**Details:** This is Brodie Robertson talking through Jonathan Corbett's LWN report, not a release notes video. The headline is AI, and the argument is about who should review what. Sushka, the agentic review tool, is both praised for finding real problems and resented by developers who feel judged by it while machine-written patches sail through. Torvalds's line is the one I keep: the tools are not the problem, clueless people driving them are. He has used an LLM on a separate project for months and says it took six months to stop bad responses, so this is not a spin-up-Claude story. There is also a blunt example of scale, a series of well over a hundred patches from a new identity within an hour, which reads like a bot. On forks, the room's view is that private kernels are welcome to try, but the edge cases are still the hard part. Nothing was decided on succession, and the summit process itself got a mild critique as a closed clique. Nothing for my projects. So yeah, the bubble is not going away.

**For my projects:** Nothing for my projects.

## 6. liber - local-first reference manager for academic research - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2019/10/reference-management.png)
**Source:** https://www.linuxlinks.com/liber-local-first-reference-manager-academic-research/ · **Karakeep:** `vzs7jy5tmon345oogjy2si4o`

**In short:** liber is a local-first reference manager for academic papers by Lukas Karner, with a CLI and browser interface, GPL v3 and Python. I would say it looks tidy, but it is not for my projects.

**Key points:**
- Local-first reference manager for academic papers, bibliographic references and notes.
- Each paper is stored in its own directory with a BibTeX record, optional PDF and Markdown notes.
- CLI and browser interface, with search, tags, BibTeX import and export, and citation key generation.
- Free and open source under GPL v3, written in Python, by Lukas Karner.

**Details:** It keeps each paper as ordinary files rather than one opaque database, which I like on principle. The feature list is the usual reference-manager set: search by title, author, keyword, year or tag, AND filters, browsing and sorting, BibTeX import and export, PDF attach and remove, Markdown notes, custom tags, renamed citation keys and separate library directories. I have not tried it, so I cannot say how stable it is. The CLI plus web split is sensible, and local-first is the right shape for this kind of tool. Still, I have no academic workflow, so nothing for my projects. I would say it is a tidy niche tool, not worth pulling into my stack.

**For my projects:** Nothing for my projects.

## 7. GitLab Is Having a Rough Month #gitlab #security #programming, by Better Stack
![](https://i.ytimg.com/vi/ihNCXbHS4xI/maxresdefault.jpg)
**Source:** https://www.youtube.com/shorts/ihNCXbHS4xI · **Karakeep:** `wxxgyzyn0ilwihj747uncic0`

**In short:** GitLab has had another critical 10/10 bug in self-managed installs, and the only fix is to upgrade. I would say that is a bummer for anyone running their own GitLab.

**Key points:**
- Affects every self-managed GitLab from version 7, released June 2014, if the server has at least one public project.
- The flaw is unauthenticated remote code execution through a regex compiler integer overflow, in the Onigmo engine bundled with GitLab's Ruby.
- GitLab.com is already patched; self-hosted servers have no workaround and must be upgraded.
- It is the second perfect 10 this month, after another in the CI/CD regex compiler nine days earlier.
- GitLab had four perfect 10s from 2019 to the end of 2025, then three in six weeks this year.
- About 82,000 GitLab servers are reachable from the internet.

**Details:** GitLab disclosed a critical CVE rated 10 out of 10 for self-managed servers. The bug lets someone without an account run code on the server, but only if it has at least one public project. It reaches every self-managed version from GitLab 7, which came out in June 2014, and GitLab patched GitLab.com already. Self-hosted admins get no workaround, just an upgrade.

The bug sits in the regex compiler: a crafted regex causes an integer overflow when compiled, leading to code execution. GitLab points at Onigmo, the regex engine built into Ruby, and fixed it by patching the copy of Ruby that GitLab ships. Nine days earlier there was another 10 in the CI/CD regex compiler. Perfect 10s used to be rare for GitLab, four from 2019 to the end of 2025, but this year brought three in six weeks. The September one was exploited within a day of the patch. There is no sign this latest one is in use yet, but with around 82,000 GitLab servers reachable from the internet, that is not much comfort. I would say it is a rough month for GitLab.

**For my projects:** Nothing for my projects.

## 8. PKScreener - stock screening and technical analysis tool - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2023/09/stock-market-chart-virtual-screen.jpg)
**Source:** https://www.linuxlinks.com/pkscreener-stock-screening-technical-analysis-tool/ · **Karakeep:** `lbl9kly2zx1pxao4p8ptp92o`

**In short:** PKScreener is a Python CLI stock screener for India's NSE with 40+ technical scanners, backtesting and Telegram alerts. It looks capable, but it is India-focused and not something I'd reach for.

**Key points:**
- Python CLI/TUI stock screener aimed at India's National Stock Exchange (NSE).
- More than 40 predefined scanners for breakouts, consolidation, reversals, volume and momentum.
- Covers Nifty and sectoral indices, futures and options stocks, new listings and custom watchlists.
- Indicators include RSI, MACD, CCI, ATR, Aroon, moving averages and Ichimoku signals.
- Runs on Linux, in Docker and via Python packages; MIT licence.
- Includes backtesting, portfolio-level filter summaries and Telegram bot alerts.

**Details:** PKScreener is a Python-based stock screener aimed at India's NSE, with an interactive CLI and Docker support. The catch is that it is India-focused and built for technical screening, not portfolio management. It has more than 40 predefined scanners, coverage for Nifty and sectoral indices, futures and options stocks, custom watchlists, indicators like RSI, MACD, CCI, ATR, Aroon, moving averages and Ichimoku signals, plus chart pattern detection. Piped scanners let you combine conditions, and there is intraday monitoring, backtesting, portfolio-level summaries and Telegram alerts. It is MIT-licensed Python from pkjmesra. I would say it is a lot of tool for one market, and I have no Indian-market workflow, so nothing for my projects.

**For my projects:** Nothing for my projects.

## 9. AI Skills Are Hiding Instructions From You #virustotal #aiagents #cybersecurity, by Better Stack
![](https://i.ytimg.com/vi/KrsNGFodfOg/maxresdefault.jpg)
**Source:** https://www.youtube.com/shorts/KrsNGFodfOg · **Karakeep:** `aa1bt251ndrpqwqo417p4nm0`

**In short:** VirusTotal found 6,637 malicious skills out of 36,000 analysed, and the awkward part is that 62% of them have no malicious code at all, so the attack is just plain English.

**Key points:**
- VirusTotal analysed 36,000 skills and found 6,637 malicious, nearly one in five.
- 62% of the malicious skills have no malicious code; the attack is written in plain English.
- Open source skill scanners miss between a third and two-thirds of them.
- Only 90 skills use hiding tricks, including 733 blank lines, HTML comments, or invisible Unicode.
- Some write themselves into memory files such as memory.md or agents.md.
- Advice: read the raw file, check the end, and do not let a skill write to agent memory without asking.

**Details:** VirusTotal has been tracking malicious AI skills, and out of 36,000 analysed, 6,637 were malicious, so nearly one in five. That is a lot. Even worse, 62% have no malicious code at all, the attack is just plain English, and the agent follows along. So open source scanners miss between a third and two-thirds, which yeah, that is the part I would worry about.

The hiding tricks are smaller than I expected. Only 90 skills use them. One hides 733 blank lines after a World Health Organization data pull, then tells the agent to report malaria in Nigeria as zero, and I have no idea why. Others use HTML comments, invisible Unicode, or memory files like memory.md and agents.md so the effect sticks around.

For me it is the old package problem again, except the payload is now a sentence. I would say read the raw file, check the very end, and never let a skill write to agent memory without asking. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 10. grimshot - command-line screenshots for Sway - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2026/03/screen-capture-roundup-c.png)
**Source:** https://www.linuxlinks.com/grimshot-command-line-screenshots-sway/ · **Karakeep:** `thlet0m1168qow54iub28wo1`

**In short:** grimshot is a small shell-script helper that drives grim, slurp, swaymsg and wl-copy for screenshots under Sway. It looks tidy and useful on a Sway desktop, but it has no bearing on my projects.

**Key points:**
- Command-line screenshot helper for the Sway Wayland compositor; it coordinates grim, slurp, swaymsg and wl-copy rather than capturing pixels itself.
- Can capture the focused window, active output or all displays, plus interactive window and rectangle selection.
- Can save a PNG, copy to the clipboard, do both, or write to standard output when the destination is a hyphen.
- Supports XDG_SCREENSHOTS_DIR, XDG_PICTURES_DIR, GRIMSHOT_FILENAME_FORMAT, optional delay, cursor inclusion and notifications.
- Includes a check command for required utilities and can be bound to Sway keyboard shortcuts.
- Free and open source under the MIT Licence; developed by Sway-Contrib contributors.

**Details:** The appeal is that it stays out of the way: no background service, just a script that wraps tools Sway users already have. It covers the useful cases, including focused window, full output, interactive region selection, clipboard copy and delayed captures with notifications. I like that it can pipe screenshot data to stdout for shell use, and that it checks for missing dependencies. It is clearly aimed at Sway, so I would treat it as a Sway-specific helper rather than a general Wayland screenshot tool. Nothing for my projects: my homelab work is Kubernetes and storage, not desktop screenshots, and this does not touch image generation or guitar practice.

**For my projects:** Nothing for my projects.

## 11. KDE Journald Browser - graphical systemd journal viewer - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2026/09/Logfile-viewer4.png)
**Source:** https://www.linuxlinks.com/kde-journald-browser-graphical-systemd-journal-viewer/ · **Karakeep:** `d5iupaifccssaxzxcn3ssbte`

**In short:** KDE Journald Browser is a Qt/Kirigami viewer for systemd journals, local or saved, with filtering and search. I would say it is a nice desktop tool, but nothing for my projects.

**Key points:**
- Part of the KJournald project, using a Qt-based library with a Qt Quick and Kirigami interface.
- Developer: KDE Community and Andreas Cord-Landwehr; licence: GNU LGPL v2.1 or MIT.
- Written in C++; can examine local, collected and offline journal databases.
- Filters by systemd unit, boot session and message priority, with colour-coded highlighting.
- Can include or exclude kernel messages; search is case-insensitive with highlighted terms and persistent history.
- Shows UTC timestamps, supports keyboard navigation, and can copy the displayed view to the clipboard.

**Details:** KDE Journald Browser is a graphical alternative to journalctl for reading systemd journal logs. It can show local journals and saved databases from other Linux systems, so it is useful after a machine is shut down or unreachable. The interface uses Qt Quick and Kirigami, with the KJournald library underneath. It filters by unit, boot session and priority, highlights services and priorities in colour, can include or exclude kernel messages, and searches case-insensitively with a persistent history. It also groups templated service instances, shows UTC timestamps, has keyboard shortcuts including jumping to the oldest or newest entry, and can copy the displayed view to the clipboard. It is free and open source. For my homelab this is a desktop viewer rather than something I would deploy in k3s, so there is no real fit. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 12. Google’s Batteries Ran Out, Revolut Went Down #googlecloud #outage #programming, by Better Stack
![](https://i.ytimg.com/vi/qLAcIYRVRiA/maxresdefault.jpg)
**Source:** https://www.youtube.com/shorts/qLAcIYRVRiA · **Karakeep:** `p6igelqoe4xf4iitejel5prt`

**In short:** Google Cloud lost a London zone when both generator controllers failed, and Revolut was down for most of the day. I would say it is a useful reminder that three zones do not help if failover itself becomes the load.

**Key points:**
- Revolut has about 80 million customers.
- Login, transfers and card payments stopped, and cards were declined.
- Just before 7am UK time the power grid dropped at the data centre running one of Google's three London zones.
- The main and backup generator controllers both failed, so the batteries ran out about seven minutes later.
- Google says most customers recovered around 1pm, six hours later, but Revolut said it was back at 20 to 7 that evening.
- The UK named Google Cloud a critical third party to the financial system in July, and the Treasury Committee chair wrote to the Bank of England and FCA on the day.

**Details:** Google's report says the grid dropped just before 7am UK time at the data centre behind one of its three London zones. Batteries took over and the diesel generators should have started, but the main and backup controllers both failed, so the zone went dark about seven minutes later. Having three zones is meant to cover this, but Google says the sudden failover traffic overloaded the other two zones, and some services were stuck waiting on the offline one, so customers in healthy zones were hit too. Revolut's first message only called it a service disruption, then blamed Google Cloud that evening; most Google customers recovered around 1pm, while Revolut said it was back at 20 to 7. Regulators had already named Google Cloud a critical third party in July, and the Treasury Committee chair wrote to the Bank of England and FCA asking when they were first alerted and by whom. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 13. 20 Best Free and Open Source Linux Power Management Tools - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2022/08/energy-saving-technology.jpg)
**Source:** https://www.linuxlinks.com/best-free-open-source-linux-power-management-tools/ · **Karakeep:** `mwt1qe031hezh982v91oq7ss`

**In short:** LinuxLinks rounded up 20 free and open source Linux power management tools, from TLP to PowerDevil. It is handy for discovery, but it is a catalogue rather than a test, so I would treat it as a starting point.

**Key points:**
- 20 tools listed, all free and open source
- Covers CPU scaling, GPU power, Wi-Fi saving, battery thresholds, thermal control and monitoring
- Arrow Lake efficiency gains are described as fairly modest
- Examples include TLP, auto-cpufreq, RyzenAdj, PowerTOP, LACT, TuneD and PowerDevil
- Lower power use is tied to less noise and longer battery life

**Details:** This is a LinuxLinks roundup dated 24 October 2026. It argues that small watt-hour reductions add up when a computer runs for many hours, then lists software for processor frequency scaling, GPU power management, Wi-Fi saving, battery charge thresholds, thermal control and power monitoring. The hardware note is blunt: 15th generation Arrow Lake chips use fewer watts, but the reduction is fairly modest in most applications. I would say the page is useful for finding names in one place, but it does not benchmark the tools or say which one wins on a normal desktop. Nothing here maps cleanly onto my projects; it is Linux desktop and laptop tuning, not homelab storage, image generation or guitar practice.

**For my projects:** Nothing for my projects.

**Projects:**
- [TLP](https://github.com/linrunner/TLP): TLP - Optimize Linux Laptop Battery Life.
- [auto-cpufreq](https://github.com/AdnanHodzic/auto-cpufreq): Automatic CPU speed &amp; power optimizer for Linux. Contribute to AdnanHodzic/auto-cpufreq development by creating an account on GitHub.
- [RyzenAdj](https://github.com/FlyGoat/RyzenAdj): Adjust power management settings for Ryzen APUs. Contribute to FlyGoat/RyzenAdj development by creating an account on GitHub.
- [PowerTOP](https://github.com/fenrus75/powertop): The Linux PowerTOP tool  -- please post patches to the mailing list instead of using github pull requests.
- [TLP UI](https://github.com/d4nj1/TLPUI): A GTK user interface for TLP written in Python. Contribute to d4nj1/TLPUI development by creating an account on GitHub.
- [cpupower](https://github.com/torvalds/linux/tree/master/tools/power/cpupower): Linux kernel source tree. Contribute to torvalds/linux development by creating an account on GitHub.
- [power-profiles-daemon](https://gitlab.freedesktop.org/upower/power-profiles-daemon): [BOT-WALL].
- [cpupower-gui](https://github.com/vagnum08/cpupower-gui): Cpupower-gui is a graphical program that is used to change the scaling frequency limits of the cpu, similar to cpupower.
- [batctl](https://github.com/Ooooze/batctl): ⚡ Battery charge threshold manager for Linux laptops - Ooooze/batctl.
- [TuneD](https://tuned-project.org/): TuneD project.
- [asusctl](https://github.com/OpenGamingCollective/asusctl): Daemon and tools to control your ASUS ROG laptop. Supersedes rog-core. - OpenGamingCollective/asusctl.
- [system76-power](https://github.com/pop-os/system76-power): Power profile management for Linux. Contribute to pop-os/system76-power development by creating an account on GitHub.
- [jolt](https://github.com/jordond/jolt): ⚡️A terminal-based battery and energy monitor for macOS and Linux. - jordond/jolt.
- [thermald](https://github.com/intel/thermal_daemon): Thermal daemon for IA. Contribute to intel/thermal_daemon development by creating an account on GitHub.

## 14. CalibRaw - GPU-accelerated RAW photo editor - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2019/09/man-talking-camera-recording-himself-vlog-working-from-home-young-content-creator-multiple-cameras.jpg)
**Source:** https://www.linuxlinks.com/calibraw-gpu-accelerated-raw-photo-editor/ · **Karakeep:** `ordh1buthd55qvvj3d35hdz1`

**In short:** CalibRaw is a Rust-based GPU-accelerated RAW photo editor with local AI masking and non-destructive sidecars; it looks feature-heavy and free, but I have no photo workflow to feed it, so nothing for my projects.

**Key points:**
- GPU processing with wgpu and WGSL compute shaders
- Rust-based engine, GPL v3, by Duecki and contributors
- Non-destructive JSON sidecars; LibRaw and Rawler RAW plus JPEG, PNG, HEIC and TIFF
- Local AI masks, noise reduction and object removal after user consent
- HDR merging, focus stacking, creative effects, batch CLI and Linux, macOS, Windows, Android support

**Details:** CalibRaw is a GPU-accelerated RAW photo editor built in Rust, with a non-destructive workflow that keeps originals untouched and stores adjustments in JSON sidecar files. It uses wgpu and WGSL compute shaders, reads many RAW formats through LibRaw and Rawler, and also handles JPEG, PNG, HEIC and TIFF. The feature list is long: exposure, tone, colour grading, lens corrections, selective masks, clone and heal, HDR merging, focus stacking, creative effects, presets, batch rendering, and MP4 exports of the edit history. AI masking, noise reduction and object removal run locally, with models downloaded only after consent. It is GPL v3 and cross-platform, including Linux. It sounds like a serious Darktable competitor rather than a toy, and local processing is the right instinct. I would say it is worth watching for photographers on Linux, but I do not have a RAW photo pipeline, so nothing for my projects.

**For my projects:** Nothing for my projects.

## 15. This Tiny Qwen 27B Model Runs on a 12GB GPU, by Better Stack
![](https://i.ytimg.com/vi/XKejQWnispc/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=XKejQWnispc · **Karakeep:** `xahfx8cxdvb14baznoug1155`

**In short:** Underdog Saluki 27B is a heavily quantised Qwen 27B variant, down to 7.9GB, tuned to preserve tool calling at the cost of math and general scores. I would say it is interesting for cheap local agents, but the vendor benchmarks need independent checking.

**Key points:**
- Underdog Saluki 27B is based on Qwen 3.8 27B and shrinks the 55GB original to 7.9GB, about 2.35 bits per weight.
- It runs through stock llama.cpp and Ollama, with a reported 32,000 context and roughly 22 tokens/s on a 12GB RTX 3060.
- On Underdog's own tool-calling benchmark it scores 88 against the full model's reported 84, but on AIME 2025 math it drops from 96.7 to 79.
- The release is a preview checkpoint with no full-precision checkpoint and no detailed training method yet.
- Recommended agent setup is thinking off and temperature zero; the same agent-loop test found Saluki slowest because of prefill.

**Details:** Saluki is a 7.9GB quant of Qwen 3.8 27B, down from 55GB, and it is tuned to protect tool calling rather than overall quality. That is a sensible trade for an agent that mostly picks tools and formats arguments, and the reported 88 against 84 on Underdog's tool-calling benchmark is the headline. But the same card shows AIME 2025 dropping from 96.7 to 79, and SWE-bench verified from 33 to 30, so the gain is narrow. It also runs on stock llama.cpp and Ollama, which matters more to me than a custom fork, and one user reported 22 tokens/s on a 12GB RTX 3060. The catch is that the benchmarks are vendor numbers, the release is a preview with no full-precision checkpoint, and the same agent-loop test found Saluki slowest because of prefill. So yeah, it is a real option for a cheap local tool-calling model, but I would not treat the benchmark gap as settled.

**For my projects:** Nothing for my projects.

## 16. 10 Best Free and Open Source Linux Partitioning Tools - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2018/10/Harddiskimage.jpg)
**Source:** https://www.linuxlinks.com/partitioningtools/ · **Karakeep:** `g0izqh0fitvskml2x6s5in6e`

**In short:** LinuxLinks lists ten free and open source Linux partitioning tools, with GParted, KDE Partition Manager and GNOME Disks among them. I would say it is a useful index, but it does not test them or tell you which one is safest on a live disk.

**Key points:**
- Ten tools are listed: GParted, KDE Partition Manager, GNOME Disks, Parted, GPT fdisk, fdisk, disktui, YaST Expert Partitioner, systemd-repart and blivet-gui.
- A special mention goes to util-linux, which includes fdisk and cfdisk.
- The tools cover graphical, command-line, TUI and declarative partitioning.
- The article warns to back up before changing partitions, and says the process should not cause data loss.

**Details:** LinuxLinks has put together a roundup of ten free and open source partitioning tools for Linux, from GParted and KDE Partition Manager to systemd-repart and blivet-gui. It is the usual LinuxLinks shape: a short explanation of why partitions exist, then a chart of names with one-line descriptions. I read it as a catalogue rather than a review, because there is no side-by-side test, no version list and no note on which tool is safest when a partition move goes wrong.

The useful part is the spread. You get graphical editors, text-mode tools like GPT fdisk, a TUI in disktui, and systemd-repart for declarative setup. That is handy if you are choosing a tool for a fresh machine. For my homelab I would not pick from a list like this without checking backup, rollback and storage integration first, and the article does not go there. So yeah, it is a good index to bookmark, and that is about it.

**For my projects:** Nothing for my projects.

**Projects:**
- [GParted](https://gparted.org/): Graphical disk partition editor
- [KDE Partition Manager](https://apps.kde.org/partitionmanager/): Manage disks, partitions, and file systems.
- [GNOME Disks](https://www.gnome.org/): An easy and elegant way to use your computer.
- [Parted](https://www.gnu.org/software/parted/): Parted - GNU Project - Free Software Foundation.
- [GPT fdisk](https://www.rodsbooks.com/gdisk/): GPT fdisk Tutorial.
- [fdisk](https://github.com/util-linux/util-linux)
- [disktui](https://github.com/mkbula/disktui): TUI for disk management on Linux. Contribute to mkbula/disktui development by creating an account on GitHub.
- [YaST Expert Partitioner](https://github.com/yast/yast-storage-ng): Rewrite of https://github.com/yast/yast-storage. Contribute to yast/yast-storage-ng development by creating an account on GitHub.
- [systemd-repart](https://github.com/systemd/systemd): The systemd System and Service Manager . Contribute to systemd/systemd development by creating an account on GitHub.
- [blivet-gui](https://github.com/storaged-project/blivet-gui): GUI tool for storage configuration using blivet library - storaged-project/blivet-gui.
- [util-linux](https://github.com/util-linux/util-linux)

## 17. Why Rust Is The New GOAT For AI, by Better Stack
![](https://i.ytimg.com/vi/R-tLX37Xgx8/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=R-tLX37Xgx8 · **Karakeep:** `hzr2lgiz6g54qirfod4ilz7s`

**In short:** A Better Stack video arguing Rust is becoming the default for AI tooling, with examples from GitHub, OpenAI and X AI. I would say the performance claims are interesting, but it is mostly vendor anecdotes and Rust cheerleading.

**Key points:**
- Elon Musk said X AI's code is mostly Rust; GitHub rewrote Copilot's runtime in Rust and Bun moved from Zig to Rust this summer.
- OpenAI's Codex CLI is now 97% Rust and dropped Node because requiring Node 22 or newer blocked some users.
- Copilot session plus first reply went from 5.25s to 292ms; the old TypeScript runtime used about 100MB per Node process.
- Microsoft said about 70% of its 2019 CVE security bugs were memory-safety bugs; Chrome found about 70% of high-severity bugs were memory bugs.
- Python packages hide Rust underneath: tokenizers has a 9.6 MB compiled Rust file, Pydantic v2 has a Rust core, TikToken has a Rust core, and UV is written in Rust.

**Details:** This is a Better Stack video about Rust moving into AI tooling, from GitHub Copilot to Codex CLI and Bun. It opens with the elevator origin story and explains ownership, the compiler and Cargo, then gives the Copilot rewrite numbers: 430,000 lines of TypeScript became 832,000 lines of Rust plus 470,000 lines of tests in about 14.5 weeks, with Copilot's agents writing most of it. I would say the performance claims are the useful part: Copilot session plus first reply dropped from 5.25 seconds to 292 milliseconds, and the Rust build is one native file instead of a Node process per app. The memory-safety stats are strong too, Microsoft's 70% CVE figure and Android below 20% memory bugs last year. But the video is selling Rust hard, and Nvidia's Rust GPU kernels are explicitly not production-ready. Python stays the interface, Rust does the heavy lifting underneath. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 18. Autohook - lightweight Git hook manager - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2020/01/Git-Clients.jpg)
**Project:** [Autohook](https://github.com/Autohook/Autohook)
**Source:** https://www.linuxlinks.com/autohook-lightweight-git-hook-manager/ · **Karakeep:** `s5nvmefobx03k8m564h28ek2`

**In short:** Autohook is a tiny Bash-based Git hook dispatcher that links .git/hooks to directories of executable scripts. I would say it is neat for simple repos and not worth it if you already use lefthook or pre-commit.

**Key points:**
- Single Bash script dispatches Git hook events to scripts in a matching directory.
- Installs symbolic links into .git/hooks; relative for repo-local scripts, absolute for central ones.
- Supports pre-commit, commit-msg, post-checkout, pre-push and other hook types.
- Runs multiple numbered scripts per event and forwards arguments and standard input.
- No config file and no runtime beyond Bash; MIT, by Nikola Kantar and contributors.

**Details:** Unfortunately there is no version number in the article, so I cannot pin it, and it is still shell plumbing with no Kubernetes path, backup story or metrics. Autohook is built around a single Bash script, which keeps it small, and it supports two approaches to managing hooks, which is flexible, yeah, but it only dispatches scripts. It creates symbolic links in .git/hooks, runs numbered prefixes in order, forwards arguments and standard input, and lets project scripts run beside shared ones through AUTOHOOK_HOOKS_PATH. That is a quite good job for a tiny repo, but for my homelab-2nd repo I would rather keep hooks plain and let CI do the heavy lifting. Nothing for my projects. So yeah, that's that.

**For my projects:** Nothing for my projects.

## 19. 8 Best Free and Open Source Linux Astrology Software - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2019/12/20594.jpg)
**Source:** https://www.linuxlinks.com/astrology/ · **Karakeep:** `h6zjtdhls6l7eubtsdi2px3j`

**In short:** LinuxLinks rounds up eight open source astrology programs for Linux, from KDE charts to a Python library. I would say it is a niche list with a few maintenance question marks, not something I would build on.

**Key points:**
- Eight named programs: Skylendar, Cenon Astro, Astrolog, Asteria, Maitreya, Kerykeion, Astrologer Studio and Morinus.
- Kerykeion is a Python library for astrological calculations and SVG charts.
- Morinus uses the Swiss ephemeris.
- Comments say Skylendar is hard to install on some distributions, including LMDE 7.
- One commenter says Cenon Astro, Astrolog and OpenAstro.org have not been updated in years; another says Astrolog 7.80 came out last year.

**Details:** LinuxLinks describes astrology as traditions and symbolism rather than science, then lists eight native Linux programs. Skylendar is KDE software with SQL support, Astrolog is called award winning, Maitreya covers Vedic and Western astrology, and Astrologer Studio is an astrology workspace. The comments are more useful than the roundup: installation seems uneven, and at least one reader could not get Skylendar running on LMDE 7 while the author says it built on Manjaro and CachyOS. I have not tried any of it, and nothing here fits my projects. It is a small, odd corner of open source software, and I would treat the list as a starting point rather than a recommendation.

**For my projects:** Nothing for my projects.

**Projects:**
- [Skylendar](https://sourceforge.net/projects/skylendar/): Download skylendar for free. Powerful and portable astrology program. Powerful and portable (Linux/Windows) astrology program, based on the swisseph library, with multitasking charts and data store….
- [Cenon Astro](https://www.cenon.info/): Cenon - Free Graphics Software with Style.
- [Astrolog](https://www.astrolog.org/): Official site of Astrolog, Daedalus, and other free content.
- [Asteria](https://github.com/alamahant/Asteria): Astrological chart calculator and analyzer with AI interpretations - alamahant/Asteria.
- [Maitreya](https://saravali.github.io/): Saravali: Home.
- [Kerykeion](https://github.com/g-battaglia/kerykeion): Data-Driven Astrology 💫 Kerykeion is a Python library for astrology. It generates SVG charts and extracts detailed structured data for birth charts, synastry, transits, composite charts, and more...
- [Astrologer Studio](https://github.com/g-battaglia/AstrologerStudio): Astrologer Studio is a free/libre open-source professional astrology workspace that helps astrologers manage their clients, generate precise astrological charts, and get AI-powered interpretations ...
- [Morinus](https://github.com/IngenieriaAstrologica/Morinus): Software libre de astrología tradicional — Free traditional astrology software (Morinus SE) - IngenieriaAstrologica/Morinus.

## 20. yq - command-line YAML, XML and TOML processor - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2021/10/JSON-Tools-1.jpg)
**Source:** https://www.linuxlinks.com/yq-command-line-yaml-xml-toml-processor/ · **Karakeep:** `n4avax1wgm8ql128c398pdx1`

**In short:** yq is a Python CLI that runs jq filters over YAML, XML and TOML, with xq and tomlq for the other formats. I would say it's handy if you already live in jq, but another Python dependency in a shell pipeline is a small bummer.

**Key points:**
- Python CLI by Andrey Kislyuk, Apache License 2.0, runs on Linux and macOS.
- Wraps jq: yq for YAML, xq for XML, tomlq for TOML, with conversion to and from JSON.
- In-place editing, round-trip YAML that keeps custom tags, scalar styles and comments, and TOML comment/whitespace preservation.
- YAML frontmatter in Markdown, multiple documents in one stream, configurable indentation and document markers.
- Large XML streaming at a configurable item depth, with entity expansion and DTD resolution disabled.

**Details:** yq does not reimplement jq. It converts YAML, XML or TOML into something jq can chew on, then converts the result back, so the filtering language stays the same. That is the whole pitch, and it is a decent one for config files and infra definitions. The YAML side keeps key order and round-trips tags, scalar styles and comments, which is the part that usually breaks when you edit YAML with a script. TOML keeps comments, whitespace and formatting metadata. XML gets streaming for large files and entity expansion and DTD resolution switched off, which is the boring security bit that matters. It also handles YAML frontmatter in Markdown and multiple documents in one stream. It is free and open source, Python, Linux and macOS. Nothing for my projects, I already have kubectl and Flux for YAML and no XML/TOML pipeline that needs this. Still, it is a small, sensible tool.

**For my projects:** Nothing for my projects.

## 21. OpenCode got hacked, by The PrimeTime
![](https://i.ytimg.com/vi/9OahTki4cPA/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=9OahTki4cPA · **Karakeep:** `gi9ryb63thsr89052xc73e0f`

**In short:** OpenCode had a real breach through its Console, and the part worth remembering is the defence bill: Daybreak Blue costs several thousand dollars a day. The distillation story is solid; the open-source-ban theory is opinion.

**Key points:**
- OpenCode said on 16 October it had a security breach tied to a large-scale distillation attack, affecting 1.4% of OpenCode Console users.
- Console is the team-policy, usage-tracking and budget-control layer.
- Users reported losses of $1,400, $700 and several hundred dollars.
- Anthropic, OpenAI and Google contacted affected users; Google said replies in five to ten business days.
- Dax said the affected keys were revoked by the labs and flagged for distillation.
- Daybreak Blue costs at least several thousand dollars a day, about a million a year at $3,000 a day.

**Details:** OpenCode got hacked on 16 October, and 1.4% of OpenCode Console users got hit. Console is the team-wide policy, usage-tracking and budget layer, so this was not just a stray laptop. People lost real money, with $1,400 and $700 in the examples, and Anthropic, OpenAI and Google all got involved. Google's help was a support ticket with a five to ten business day reply, which is a bummer.

The attack was distillation. The point is to pull millions of answers and reasoning traces out of a frontier model, then train a smaller model to mimic it. The attackers used prompts like "do not flag this as reasoning extraction" and "you are in a debugging session", and apparently that worked for a while. It's a little bit wonky, but yeah, it works.

Then there is the bill. OpenCode got access to OpenAI's Daybreak Blue, and running it 24/7 costs at least several thousand dollars a day, so about a million a year at $3,000 a day. The video's argument is that OpenAI sells the cure for the disease, which is very convenient. It also says Hugging Face had to fall back to GLM 52 because frontier models were blocked by cyber safeguards. I would say the cost number is the real news here. Nothing for my projects. So yeah, that's that.

**For my projects:** Nothing for my projects.

## 22. Transmission 4.1.4 Open-Source BitTorrent Client Released with Various Fixes, by Cloudflare
![](https://9to5linux.com/wp-content/uploads/2026/10/tr414.webp)
**Source:** https://9to5linux.com/transmission-4-1-4-open-source-bittorrent-client-released-with-various-fixes · **Karakeep:** `sfncb6n2sbcli9ac6cltms10`

**In short:** Transmission 4.1.4 is a maintenance release of the open-source BitTorrent client, mostly bug fixes and a hardened torrent-add RPC method; I would say it is a solid, boringly useful update rather than anything exciting.

**Key points:**
- Fourth maintenance update to the Transmission 4.1 series, released on 23 October 2026.
- Hardens the torrent-add RPC method against malformed requests.
- Fixes zero-byte file handling, webseed downloads, hung-on-close behaviour, proxy SSL verification and a GCC 12.15 build failure.
- Unifies launch and delegation between the Qt and GTK clients.
- macOS client patched against a potential RCE requiring local write access to preferences.
- Source tarball available from the project's GitHub release notes.

**Details:** Transmission 4.1.4 lands almost four months after 4.1.3 and is the fourth maintenance release in the 4.1 series. The headline change is hardening the torrent-add RPC method against malformed requests, which is the kind of fix I like because it reduces silly breakage rather than chasing features. It also fixes a regression that mishandled torrents with zero-byte files and could lose downloaded progress, plus a rare hang when closing, unfinished webseed downloads, a proxy SSL verification problem caused by TR_CURL_PROXY_SSL_NO_VERIFY, and a GCC 12.15 build failure with -Wnull-dereference -Werror. Qt and GTK now hand off new torrents to an already running session, which is neat if you mix clients or use browser MIME handlers. The GTK list re-sorts when a top folder name changes, Qt uses less CPU in the UI, and the macOS client gets a patch for a potential RCE that needs local write access to preferences. I would say it is worth installing if you already run Transmission, but it does not change the basic shape of the tool. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 23. Memray - memory profiler for Python applications - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2025/08/002-process.png)
**Source:** https://www.linuxlinks.com/memray-memory-profiler-python-applications/ · **Karakeep:** `f95x1wi2uc6m7h59zfqukt1n`

**In short:** Memray is Bloomberg's open-source Python memory profiler, tracing allocations through Python, the interpreter and native extensions. I would say it is a solid tool for finding memory bloat, but only if you actually run Python services.

**Key points:**
- Developer is Bloomberg; free and open source under Apache License 2.0.
- Traces allocations made by Python code, the interpreter itself and native C or C++ extension modules.
- Captures full call-stack information and follows multi-threaded workloads, including threads from native libraries.
- Generates HTML flame graphs, HTML tables, terminal summaries, statistics and allocation-tree reports, plus an interactive live terminal view.
- Can profile a script or module from the command line, or instrument selected code regions with the Tracker API.
- Saves binary capture data for later analysis, and has an optional pytest integration for allocation reporting and memory limits.

**Details:** Memray records allocation activity during execution and ties memory costs to individual call stacks, which is useful when Python delegates work to libraries outside pure Python. It can be run from the terminal or embedded with the Tracker API, so it fits one-off investigations and targeted profiling. Reports cover HTML flame graphs for peak allocated memory, HTML tables, terminal summaries, statistics and allocation trees, plus an interactive live view with sorting and thread switching. Native stack tracking is available for Python plus compiled-library cases. Binary captures can be saved and analysed later without rerunning. The optional pytest companion can report allocations in tests and enforce limits. It is written in Python and Apache 2.0 licensed. Nothing for my projects unless a Python service in my homelab starts eating memory.

**For my projects:** Nothing for my projects.

## 24. OBS Studio 33 Officially Released with Many New Features and Improvements, by Cloudflare
![](https://9to5linux.com/wp-content/uploads/2026/10/obs33.webp)
**Source:** https://9to5linux.com/obs-studio-33-officially-released-with-many-new-features-and-improvements · **Karakeep:** `z2nc14ju2cq42dy8yxfb1stg`

**In short:** OBS Studio 33 is a major update to the free, cross-platform video recording and live streaming tool, with NVIDIA Broadcast SDK support and a plugin loading overhaul. I would say it is worth a look if you stream, but dropping Ubuntu 24.04 LTS support is annoying.

**Key points:**
- Open-source, cross-platform, free video recording and live streaming software
- Adds support for the newest NVIDIA Broadcast SDKs for NVIDIA Audio Effects and Video Effects
- Adds NVENC (NVIDIA Encoder) support on AArch64 (ARM64)
- Overhauls plugin loading: first-party plugins move to a new core folder, third-party plugins get an updated install location and folder structure
- Existing third-party plugins still load from legacy locations until OBS Studio 34
- Removes support for Ubuntu 24.04 LTS

**Details:** OBS Studio 33 was released on 23 October 2026 as a major update. It adds support for the newest NVIDIA Broadcast SDKs for NVIDIA Audio Effects and Video Effects, hotkeys for controlling audio monitoring of a source, and NVENC support on AArch64. It also overhauls plugin loading, moving first-party plugins into a new core folder and giving third-party plugins an updated installation location and folder structure, while existing third-party plugins still load from legacy locations until OBS Studio 34. Source snapping gets a visual indicator, snapping along the whole axis, and no snapping to hidden sources. Spinboxes are less annoying now, values update after Enter, and Shift plus Up or Down jumps multiple steps. There are also fixes for groups in Studio Mode, PipeWire screencast duplication, and a potential Linux crash when a USB mic is removed. Unfortunately it drops Ubuntu 24.04 LTS support, which that's a bummer for older boxes. I would say it is a solid update for streaming and recording, but check your plugins and distro before upgrading.

**For my projects:** Nothing for my projects.

## 25. tincan - peer-to-peer voice and text chat for the terminal - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2025/07/008-chat.png)
**Source:** https://www.linuxlinks.com/tincan-peer-to-peer-voice-text-chat-terminal/ · **Karakeep:** `zzwtigayks9kyoicfy1po18f`

**In short:** tincan is a Rust terminal voice and text chat for small peer groups, with encrypted QUIC calls and in-memory room history; I like the feature set, but the IP leakage and public-service dependencies make it a maybe rather than a must.

**Key points:**
- Terminal voice and text chat for small peer groups, written in Rust and MIT-licensed.
- One participant is coordinator for roster, channels and chat; voice goes peer to peer.
- Voice uses encrypted QUIC, Opus audio, RNNoise suppression, mute, deafen, push-to-talk and per-peer volume.
- Room admission uses Argon2id and a keyed BLAKE2b proof; text history is in memory only.
- Peer discovery, NAT traversal and relay fallback depend on public services from Number Zero; peers can learn each other's IP addresses.

**Details:** tincan is from developer Ahmet Bilal Yazıcıoğlu. A room is opened by one participant who acts as coordinator for the roster, channels and chat, while voice travels between peers instead of through a tincan-operated mixer. Rooms can be created with a memorable name and passphrase or a longer invite code based on the host's public key.

The audio side is complete: encrypted QUIC peer-to-peer connections, relay fallback, Opus with resampling, loss concealment and per-peer jitter buffering, RNNoise with a runtime switch, mute, deafen, push-to-talk, selectable devices and per-person volume. Text viewing and voice participation are independent, so one channel can be read while speaking in another. The coordinator keeps recent text in memory for late joiners; it is not written to disk and disappears when the room closes.

The catch is operational. Peer discovery, NAT traversal and relay fallback currently depend on public services operated by Number Zero, and room members can learn each other's IP addresses. For a small trusted group that is a known trade-off; for anything sensitive I would say it is a bummer. Nothing for my projects, since it has no Kubernetes path, backup story or metrics.

**For my projects:** Nothing for my projects.

## 26. We Were Wrong About How AI Thinks, by Better Stack
![](https://i.ytimg.com/vi/XqUDQcPo3O0/maxresdefault.jpg)
**Source:** https://www.youtube.com/shorts/XqUDQcPo3O0 · **Karakeep:** `xn4f6p0aj0kvc491zpcemglh`

**In short:** Nick Camarada at Goodfire argues neural networks may be far more directly interpretable than superposition suggested, with about 99% of neurons in a modern Inception-sized image model easily interpretable, but the detailed paper is not out yet, so I would say it is promising and still unverified.

**Key points:**
- Nick Camarada at Goodfire now says neural networks are already clean, reversing the superposition view he helped push in the 2020 Zoom In paper.
- The famous Inception V1 neuron 4E55 was not mixing cats and cars; it was detecting a V shape, also linked to flames, fox snouts and water jets.
- A modern image model of the same size and data had about 99% of last-layer neurons easily interpretable.
- Goodfire's preliminary Qwen 3 32B audit puts about 90% of neuron poles on one main job, about 7% on two related jobs, and 2 to 4% not understood.
- The detailed technical paper has not been published yet, and the current claim is an informal essay.

**Details:** This Better Stack short is about Nick Camarada at Goodfire arguing that neural networks are already clean, not tangled by superposition. The old story was that neurons cram unrelated ideas together, so you first had to train something like a sparse autoencoder to untangle them. His re-read of Inception V1 neuron 4E55 is the hook: it looked like cats and car fronts, but it was really a V detector, and a modern image model of the same size on the same data made about 99% of last-layer neurons easily interpretable. That is a big jump, but it is one image-model comparison, and the language-model numbers are still mixed: Anthropic's 2023 Towards Monosemanticity gave the median neuron 0 out of 14, while OpenAI's automated interpretability found about 1.7% interpretable. Goodfire's preliminary Qwen 3 32B audit says about 90% of neuron poles have one main job, about 7% have two related jobs, and only 2 to 4% are not understood, with similar claims for Kimi K3. Unfortunately the detailed technical paper is not out yet, so I would say this is interesting and still needs checking. So yeah, that's that.

**For my projects:** Nothing for my projects.

## 27. Even The NSA Got Involved, by Theo - t3․gg
![](https://i.ytimg.com/vi/nXpoU99pTho/maxresdefault.jpg)
**Source:** https://www.youtube.com/shorts/nXpoU99pTho · **Karakeep:** `n4lj6z3pnqkta78wuakh475j`

**In short:** Theo splits recent security news into disclosed CVEs and actual incidents, and argues the incidents are the scarier bit. I would say it is a quick framing video, not a detailed report.

**Key points:**
- Two separate things are happening at once, not one single wave of hacks.
- The CVE side names Node, GitLab, PHP, Quick and Light LLM among others.
- The other side covers Railway and open code as actual attacks with incident reports.
- Both are bad, but for different reasons.
- Theo says the incident side should worry people more, despite attention on the CVE side.

**Details:** Theo's point is that CVEs and real attacks get lumped together, which makes the whole thing look like one big hack. The CVE list is the familiar kind: Node, GitLab, PHP, Quick, Light LLM and more. Those are bugs that exist and could be exploited. The other side is Railway and open code, where he is talking about actual attacks and incident reports. He says both are bad, but the incident side is worse, and people are looking at the wrong one. I agree with the split as a way to calm down, but the short gives no versions, patches or dates, so there is nothing to act on from it. Nothing for my projects.

**For my projects:** Nothing for my projects.
