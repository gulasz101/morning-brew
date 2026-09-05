---
date: 2026-09-04
slug: 2026-09-04-morning-brew
tags: Application Delivery Controller,Apps,BorgBackup,C,CLI,Calamares,DNSSEC,Debian,Distro,Distros,Documents,Domain Name Service,FTP,GTK+,GUI,Graphics,Grml,High Availability,Hyprland,Internet,JSON,JavaScript,LibreOffice,Linux distribution,Lua,Multimedia,News,OCR,Other,PHP,Programming,Python,Qt,Reverse Proxy,Roundup,Rust,Scientific,System Software,TUI,Ubuntu,Utilities,Web Apps,Xfce,astronomy,backup,chemical engineering,chemistry,distribution,font editors,fonts,free,java,load balancer,mailing list manager,networking,office suite,open source,scientific,screen capture,surveillance,system administration,system administrator,systemd,tui,web development,web server,webcam
---

# Morning Brew — 2026-09-04

Twenty-five items hoarded on 2026-09-04 — four YouTube videos (now transcribed) and twenty-one articles, mostly the usual LinuxLinks firehose plus a few 9to5linux distro drops and one InfoQ piece. Here's the lot, with attribution so you know who's talking.

## 1. Gammapy – analyse gamma-ray astronomy data — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2023/02/space-galaxy-background.jpg)

**Source:** https://www.linuxlinks.com/gammapy-analyse-gamma-ray-astronomy-data/
**Karakeep doc:** `ck3gwtu9nl202hbvj6r730lg`

Gammapy is a Python package for crunching gamma-ray astronomy data, built on NumPy, SciPy and Astropy. It's the actual core library behind the Cherenkov Telescope Array's science analysis software and the H.E.S.S. collaboration straight-up recommends it for publications, so it's not some toy — MAGIC, VERITAS and HAWC data all run through it too. You model sources with spatial/spectral/temporal models, fit them through a common interface, and drive the whole thing from Python or YAML for reproducible pipelines. BSD 3-Clause, free and open source.

## 2. scantpaper – scan documents to PDF or DjVu — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/07/014-ocr.png)

**Source:** https://www.linuxlinks.com/scantpaper-scan-documents-pdf-djvu/
**Karakeep doc:** `phszmsdv6363n59iu0onmns3`

scantpaper is a GTK scanning app that's basically a Python rewrite of gscan2pdf, pulling scans in through SANE and spitting out PDF, DjVu, TIFF or plain images. It handles flatbed and ADF scanners, single/double-sided with auto page interleaving, batch scanning, and OCR via Tesseract + OCRmyPDF to produce searchable PDF/A. You get crop/rotate/split/delete, brightness/contrast/threshold tweaks, unpaper cleanup, and it even recovers crashed sessions on restart. GPL v3, by Jeffrey Ratcliffe.

## 3. Ubuntu 26.10 "Stonking Stingray" Snapshot 3 Is Now Available for Public Testing — by 9to5Linux

![9to5Linux](https://9to5linux.com/wp-content/uploads/2026/09/u2613.webp)

**Source:** https://9to5linux.com/ubuntu-26-10-stonking-stingray-snapshot-3-is-now-available-for-public-testing
**Karakeep doc:** `jfr5t5m09muud42whovqpm36`

Canonical dropped Snapshot 3 of Ubuntu 26.10 (Stonking Stingray), the third dev milestone aimed at early adopters and app devs. It's still on Linux kernel 7.0 like the last two snapshots, but this one jumped to GNOME 51 Beta, with the final release expected to land on kernel 7.2, Mesa 26.2 and GNOME 51. New stuff includes a full desktop on RVA23 hardware, better driver management, a simplified installer, on-device speech-to-text, and a package-agnostic App Center. Final release hits October 15th, 2026, supported only nine months until June 2027 — and yes, don't run this on production boxes.

## 4. Grml 2026.09 Linux Distro Is Out with Linux Kernel 7.1, Based on Debian 14 Forky — by 9to5Linux

![9to5Linux](https://9to5linux.com/wp-content/uploads/2026/09/grml269.webp)

**Source:** https://9to5linux.com/grml-2026-09-linux-distro-is-out-with-linux-kernel-7-1-based-on-debian-14-forky
**Karakeep doc:** `h86fc2x6twk2ip1alvqke65x`

Grml 2026.09 (codename Hättiwaritätti) is out, the Debian-based bootable live distro for sysadmins and CLI junkies. It's on Linux 7.1 and pulls all the package updates and security patches from Debian Testing as of September 2026, which becomes Debian 14 "Forky" next year. Notable changes: GNU Screen 5.0.1 (so grml screenrc users need to upgrade or fall back to screenrc_v4), exFAT boot support in the initramfs, GPT/Raspberry Pi fixed disk identifiers, and grml-live dropped i386 and its old config file. Ships as Full and Small editions for amd64 and arm64.

## 5. 12 Best Free and Open Source Font Editors — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/05/044-font.png)

**Source:** https://www.linuxlinks.com/best-free-open-source-font-editors/
**Karakeep doc:** `rjgxwbhf6skokks7g6qk6tdm`

A roundup of the best free and open source tools for editing fonts, since Linux users don't exactly drown in font choices. The list covers FontForge (the big one for PostScript/TrueType/OpenType), fontTools (Python library), Birdfont, Glyphr Studio for beginners, Fontra (browser-based), ftcli, Ygt for hinting, Slice, TruFont and Modular Font Editor K. Each entry gets a portal page with a full feature breakdown and screenshot, plus a LinuxLinks-style ratings chart. Only FOSS makes the cut.

## 6. 10 Best Free and Open Source BorgBackup Front-Ends — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/01/Backup-software.png)

**Source:** https://www.linuxlinks.com/best-free-open-source-borgbackup-front-ends/
**Karakeep doc:** `jhlx10hieqh4r484lfjdewbv`

BorgBackup is a deduplicating backup tool with optional compression and authenticated encryption — 256-bit AES, HMAC-SHA256 integrity, and lz4/zstd/zlib/lzma compression — but it's CLI-only, so this roundup covers the front-ends that make it usable. The ten picks span GUI, CLI and web: Vorta (Qt), borgmatic, Pika Backup (GNOME), Emborg, BorgWarehouse, Borg UI, Borgitory, BorgTUI, snapborg and Borg Backup Server. The ratings chart only judges the front-ends, not Borg itself, and only FOSS is included.

## 7. OpenEMM – self-hosted web application for email marketing and email automation — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/03/businessman-touching-wireframe-e-mail-email-marketing-newsletter.jpg)

**Source:** https://www.linuxlinks.com/openemm-email-marketing-automation/
**Karakeep doc:** `iuj2zaiwjoir5gyzfo1sedk0`

OpenEMM is a self-hosted email marketing and automation platform from AGNITAS AG, covering newsletters, multi-stage campaigns, transactional mail and autoresponders with targeting, tracking and reporting. It's got a drag-and-drop workflow manager, GDPR-compliant anonymous tracking, bounce management, real-time KPI stats, and a scalable multi-queue mail backend for high-volume sending. Integrates via REST/SOAP APIs, webhooks, scripting, and connectors for Make and n8n, running on MariaDB, Postfix, OpenJDK, Node.js and Tomcat. AGPL v3.


## 8. pychemqt – chemical engineering process simulator — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2018/09/Chemist.jpg)

**Source:** https://www.linuxlinks.com/pychemqt-chemical-engineering-process-simulator/
**Karakeep doc:** `r33y2znujlxnsez3htjvvlgh`

A graphical chemical-engineering process simulator written in Python with a Qt frontend, backed by NumPy, SciPy and Matplotlib. It's not just a pile of calculators — you can define process streams, build flow diagrams and model actual equipment, with a database of roughly a thousand predefined compounds plus custom ones and petroleum-fraction pseudocomponents. It ships a proper spread of thermodynamic models (Redlich-Kwong, Soave-Redlich-Kwong, Peng-Robinson and friends), models for mixers, dividers, valves, compressors, pumps, heat exchangers, flash calcs and even cyclones and baghouses. GPL v3, by Juan José Gómez Romera.

## 9. Forget SQS, RabbitMQ and Kafka. Just use Postgres. — by Better Stack

![Better Stack](https://i.ytimg.com/vi/KZw8et-e6vk/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=KZw8et-e6vk
**Karakeep doc:** `dk8bas1m6vth16ct4cuw58ha`

The pitch is that you can ditch SQS, Kafka and RabbitMQ and run your queues straight inside Postgres with PGMQ, and the "it doesn't scale" objection gets answered with a stress test. Each queue is just its own table; you create it with `pgmq.create`, send JSON messages (optionally with a delay), and read them with a visibility timeout that guarantees exactly-once delivery — unacked messages become visible again after the window. The demo shoves 100k rows in ~0.4s, then 100 workers each pulling batches of 10 chew through them at a combined ~11,100 messages/sec on a container capped at 2 CPUs and 2GB RAM. You can drive it SQL-only or via Rust/Python/TypeScript client libs, and the whole thing is part of their broader "replace your stack with Postgres" crusade.

## 10. Hyggshi OS – customizable Debian-based Linux distribution — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/04/Linux-Distributions.png)

**Source:** https://www.linuxlinks.com/hyggshi-os-customizable-debian-based-linux-distribution/
**Karakeep doc:** `gq0cyfzwogcmidpr8alyvgx7`

A custom distro built on a Debian-family base, but instead of live-build it assembles bootable images directly with debootstrap, mksquashfs and xorriso — and the same framework can target Ubuntu and Linux Mint too. It boots into a live Xfce session with autologin for instant use, then Calamares handles the install and strips the autologin so you get a normal login prompt afterward. You can pick KDE Plasma, LXQt, GNOME, MATE or Cinnamon at build time, with LightDM, NetworkManager and systemd underneath, plus custom GRUB and Plymouth branding. Builds run via shell scripts or a container, configurable through env vars, and the same pipeline powers their GitHub Actions.

## 11. Best Free and Open Source Alternatives to Citrix NetScaler — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2017/12/hypervisors.jpg)

**Source:** https://www.linuxlinks.com/best-free-open-source-alternatives-citrix-netscaler/
**Karakeep doc:** `fpmslx2k11sy2l8ase1grvt9`

NetScaler is Citrix's proprietary application delivery controller — load balancing, traffic management, SSL/TLS offloading, app acceleration and security — and this roundup lines up the open-source stand-ins. HAProxy is the pick for straight-up L4/L7 load balancing and high-availability traffic distribution; Traefik shines in dynamic, containerized/cloud-native setups with its service-discovery integration and auto TLS; NGINX Open Source covers reverse-proxy and load-balancing duties with its event-driven concurrency; and OpenResty layers LuaJIT scripting on the NGINX core for the more complex policy work. The honest caveat up front: none of these individually replaces NetScaler's whole integrated stack, which also spans WAF, API security and bot management.

## 12. LibreOffice 26.2.6 Open-Source Office Suite Released with More Than 30 Bug Fixes — by 9to5Linux

![9to5Linux](https://9to5linux.com/wp-content/uploads/2026/02/lo262.webp)

**Source:** https://9to5linux.com/libreoffice-26-2-6-open-source-office-suite-released-with-more-than-30-bug-fixes
**Karakeep doc:** `mq3zh9ohp8sfhevuugto083q`

The sixth maintenance release of the LibreOffice 26.2 series, landing a month and a half after 26.2.5, and it fixes 36 bugs — crashes, annoyances and stability issues reported by users and patched by the community. It's out now as DEB and RPM binaries plus a source tarball, but if you installed from your distro's repos you should wait for it to land there. The 26.2 series gets one more update (26.2.7, due late Oct/early Nov) before hitting end of life on November 30th, 2026 — though the article nudges you to jump straight to LibreOffice 26.8, released in August, if your distro already has it.

## 13. Kubernetes Promotes KYAML as a Safer, More Consistent Way to Work with Manifests — by InfoQ

![InfoQ](https://res.infoq.com/news/2026/09/kubernetes-kyaml-manifests/en/headerimage/generatedHeaderImage-1787909718521.jpg)

**Source:** https://www.infoq.com/news/2026/09/kubernetes-kyaml-manifests/
**Karakeep doc:** `p5go72qcf300atboiq174idu`

KYAML is a strict subset of YAML — not a new language — that forces objects to `{}`, arrays to `[]` and strings to double quotes, so it looks closer to JSON but stays valid YAML that existing parsers and kubectl can still chew on. It went alpha in v1.34 and beta (on by default) in v1.35, and you don't have to hand-rewrite anything: `kubectl -o kyaml`, the Kubernetes yamlfmt tool and Google's yamlfmt all convert existing manifests. The real argument is that manifests are increasingly generated by Helm, GitOps and AI coding agents rather than hand-written, and a stricter dialect gives those systems fewer ways to screw up indentation or implicit type coercion. Kubernetes is deliberately not making it the default — it's pitched as an incremental practice, not a migration.

## 14. WeaveDreamer – fabric design software for hand weavers — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/06/Linux-Home-Embroidery.png)

**Source:** https://www.linuxlinks.com/weavedreamer-fabric-design-software-hand-weavers/
**Karakeep doc:** `ex4aaqxyeerazdc8pc7ayl1l`

Fabric-design software for hand weavers that handles weaving drafts with arbitrary numbers of warp/weft threads, treadles and harnesses, and lets you edit threading, tie-up and treadling sections while generating a visual drawdown of the resulting fabric. It does liftplan and network drafts, imports/exports WIF files, and has configurable colour palettes you can save and reuse. The editing is surprisingly fleshed out — drag-select cells, copy/paste picks and tie-ups, Paste Special that repeats/scales/transposes selections, undo, and a tile view for repeating sections. Java 21+, GPL v2, by Pete Hammond.


## 15. This Open-Source Tool Makes Claude Create Architecture Diagrams — by Better Stack

![Better Stack](https://i.ytimg.com/vi/iuJszJuiuSg/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=iuJszJuiuSg
**Karakeep doc:** `pblgqn9xufhz07z4saufmvb2`

Josh from Better Stack puts Archify through its paces — the tool that got 44k stars in a few months by plugging straight into Claude Code, Cursor, and Codex. The trick is the agent never draws anything: it spits out typed JSON, Archify validates it against a strict schema, and only then does a local compiler render the HTML. If the graph is invalid it just fails closed, so you get diagnostics and rule codes instead of a pretty-but-wrong diagram. His verdict: genuinely useful for PR reviews and design docs where you commit the JSON and diff two validated snapshots to see what actually changed, but don't point it at a huge repo and say "map everything" — that's a bad question, not an Archify failure. One rule he swears by: one question per file, and if you can't say what question the diagram answers, don't generate it.

## 16. 31 Best Free and Open Source JSON Tools — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2021/10/JSON-Tools-1.jpg)

**Source:** https://www.linuxlinks.com/best-free-open-source-json-tools/
**Karakeep doc:** `x8lx8tsl25yqurpuzrwjywa2`

LinuxLinks' roundup of JSON tooling, and despite the manifest title saying 31 the actual page lists 27 — jq, fx, jaq, gron, gojq, jless, jnv, jid, jo, faq, jello, and a pile of TUI viewers and validators. The usual suspects are all here: jq billed as "sed for JSON," gron for making JSON greppable, jless as the Rust CLI viewer, plus newer stuff like jnv and json-tui. It's the standard LinuxLinks format — a ratings chart, a table of one-liners, and a portal page per tool. Nothing revolutionary, just a solid reference list if you're tired of squinting at raw JSON in a terminal.

## 17. Inetutils - traditional networking utilities and servers — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/04/003-ftp-1.png)

**Source:** https://www.linuxlinks.com/inetutils-traditional-networking-utilities-servers/
**Karakeep doc:** `ltiypa0xl095bi35xi6mbvhp`

The GNU Project's Inetutils — a grab bag of the classic networking tools you thought were dead but apparently still ship: ping, traceroute, whois, ifconfig, hostname, logger, plus FTP/TFTP clients and servers, telnet/telnetd, and the ancient rsh/rlogin/rexec/rcp family. It's all derived from 4.4BSD-Lite2, and version 2.8 actually tightened up telnet security with fixes for authentication bypass and a stack-buffer overflow. If you're running some legacy box that still needs telnet or rlogin, this is the portable GNU-licensed way to get it. For everyone else it's a nostalgia trip through 1995.

## 18. 16 Best Free and Open Source Linux Webcam Tools — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2021/12/webcam-tools.png)

**Source:** https://www.linuxlinks.com/webcam/
**Karakeep doc:** `djq17ux98gs39i8mlh2ps2rq`

LinuxLinks' webcam roundup covering capture, video chat, and surveillance — Webcamoid, ZoneMinder, Motion, DroidCam, Kerberos.io, Guvcview, Cheese, Kamoso, and a few oddballs like HasciiCam (live ASCII video, because of course). The list splits roughly into "take a picture of yourself" tools and "turn a Pi into a security camera" tools, with ZoneMinder and Motion doing the motion-detection heavy lifting. DroidCam is the one worth knowing if you want to repurpose an old phone as a network IP cam. Standard LinuxLinks fare — ratings chart, one-line descriptions, portal pages.

## 19. FramR - Wayland screenshot and screen-recording utility — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/03/screen-capture-roundup-c.png)

**Source:** https://www.linuxlinks.com/framr-wayland-screenshot-screen-recording-utility/
**Karakeep doc:** `zlmszovudixs3swu3uovmywy`

FramR is a Rust Wayland screenshot and screen-recording tool with built-in annotation and upload, aimed at wlroots/scenefx compositors like Hyprland, Sway, and River, plus KDE Plasma. You can capture a screen, monitor, or region, annotate with arrows/circles/text, blur sensitive bits, and record video with H.264/AV1/VP9 encoding through VAAPI or NVENC. The standout feature is ShareX/iShare-compatible uploaders, so you can fire captures straight to a hosting service with one click. It's basically the Wayland answer to ShareX, and the annotation-before-save workflow is genuinely handy for quick bug reports.

## 20. reeve – local web development stack manager — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2022/06/170y-utilities.jpg)

**Source:** https://www.linuxlinks.com/reeve-local-web-development-stack-manager/
**Karakeep doc:** `rn4mexfgnehr1el1pu34t78m`

reeve is a Rust TUI/CLI manager for local web dev stacks on Linux and macOS — it orchestrates Caddy, Apache, and nginx, PHP-FPM, MySQL/MariaDB/PostgreSQL/Redis/memcached, local DNS, and HTTPS certs via mkcert. The killer feature is running different PHP versions per site simultaneously, so you stop doing the global-PHP-version shuffle every time a project needs a different environment. It's got Valet-style directory parking, presets for Laravel/WordPress/Symfony/Drupal, and a live traffic monitor showing request rates and latency. Basically a self-hosted Herd/Valet alternative that manages what's already on your box instead of bundling its own copies.

## 21. This is not ready — by Less Bitter

![Less Bitter](https://i.ytimg.com/vi/zcM0lR3r5Do/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=zcM0lR3r5Do
**Karakeep doc:** `s3lcwa2ppgrqk0n9adqasve9`

Less Bitter puts Grokbot and Claude's desktop-use through a torture test: control the computer, open Final Cut Pro, drag a clip into the timeline, do some cuts. Grokbot is painfully slow and scary — it renamed one of his cameras to "meta spark" and he nearly called it busted. Claude's desktop use is faster and actually manages to import a clip and cut dead space, but it's agonizingly slow, burns tokens like crazy, and gets blocked by an invisible WhisperFlow overlay window for fourteen minutes trying to draw a rectangle in Sketch. His verdict: it's the "Will Smith eating spaghetti" phase of computer use — the only real use case right now is accessibility, and it needs to be ten times faster before it's anything but a novelty.


## 22. POVThread – convert bitmap images into three-dimensional POV-Ray scenes — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/07/postcard-with-embroidery-kettle-macro-shot-closeup.jpg)

**Source:** https://www.linuxlinks.com/povthread-convert-bitmap-images/
**Karakeep doc:** `brlyb33ou76a1uq3wlbwbcqo`

POVThread turns any bitmap into a 3D POV-Ray scene that looks like woven canvas or cross-stitch embroidery — every single pixel becomes its own coloured 3D object. It reads PNG/PPM/PGM, has a Tkinter GUI for previewing and filtering, and gives you a "linen" effect for taffeta-like fabric plus a "stitch" effect for proper cross-stitch. The clever bit is it's pure Python with no heavy compiled image libs, uses Perlin noise to break up unnaturally uniform thread placement, and spits out editable POV-Ray files with configurable camera and lighting. Public domain (Unlicense), needs Python 3.11+, by Ilya Razmanov.

## 23. Linux Doesn’t Have to Be Ugly — by NetworkChuck

![NetworkChuck](https://i.ytimg.com/vi/yQ4prIKen74/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/yQ4prIKen74
**Karakeep doc:** `aec4nit5eool03oufkt8spwo`

Chuck's whole point is that Linux desktops don't have to look like they were designed by someone colourblind — you can actually make an OS look like the hacker-movie aesthetic from The Matrix. He's tired of window arrangements and colour coordination that look like garbage, and wants to be the guy at the airport whose screen makes people go "is he hacking us right now?" His pitch: open a few terminals, run a screen tabor, and people will genuinely wonder what the hell you're doing. It's a short, vibes-heavy rant about ricing your setup into something that looks cool rather than functional-but-ugly.

## 24. Knot Resolver – scalable caching DNS resolver — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2023/01/System-Admin.jpg)

**Source:** https://www.linuxlinks.com/knot-resolver-scalable-caching-dns-resolver/
**Karakeep doc:** `et4oey3226k6p3jeb9tkc21f`

Knot Resolver is a caching recursive DNS resolver from CZ.NIC that scales from a tiny home box up to heavy resolver infrastructure. It's built on C + LuaJIT with a state-machine API you extend via modules, plus a Python management layer for config and ops. The scaling story is shared-nothing — independent workers get pinned to CPU cores and can be added or removed without dropping service, while an MVCC cache is shared where it makes sense. It does full DNSSEC validation, DNS-over-TLS/HTTPS/QUIC, YAML declarative config, an HTTP API for live changes, and even etcd for auto-config in big deployments. GPLv3.

## 25. SunPy – Python tools for solar physics data analysis — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2023/02/space-galaxy-background.jpg)

**Source:** https://www.linuxlinks.com/sunpy-python-tools-solar-physics-data-analysis/
**Karakeep doc:** `fl096q9wubddud9yno4kk36d`

SunPy is the Python package for solar physics — a common interface over data from a pile of instruments and observatories. Its Fido system searches and downloads observations by time, instrument and wavelength from VSO, JSOC, CDAWeb, HEK, SOLARNET and a bunch of mission-specific archives. It gives you metadata-aware Map objects (image arrays + FITS metadata with coordinate-aware ops like crop/rotate/convert between physical and pixel coords) and TimeSeries containers for anything sharing a time axis, supporting FITS/CSV/CDF. BSD 2-Clause, from the SunPy Project.

