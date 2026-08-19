---
date: 2026-08-15
slug: 2026-08-15-morning-brew
tags:
  - digest
  - karakeep
  - Linux
---

# Morning Brew — 2026-08-15
Two saves today, both Linux-adjacent. One is Nvidia finally shipping a native app so you don't have to squint at cloud gaming through a browser tab. The other is a hype-cycle promise of building your own distro with AI, delivered pre-alpha and held together by a developer's goodwill and a 9 GB ISO.

## 1. Nvidia just made gaming on Linux a whole lot easier

**Publisher:** How-To Geek · **Link:** https://share.google/JSFG8R9kCkcT91HKO (→ https://www.howtogeek.com/nvidia-geforce-now-linux-app-release-game-streaming/) · **Karakeep doc:** `asbqg7b9plix540slei4y5cw`

Nvidia's native GeForce Now app for Linux has finally left beta, so you no longer have to run the whole damn thing through a web browser like it's 2010. The pitch: skip Proton, skip the compatibility roulette, skip watching your disk fill up with games you'll never finish — just stream the whole thing and let Nvidia's datacenter do the heavy lifting.

The requirements are honest enough: Ubuntu 24.04 LTS or later, dual-core 2 GHz, 4GB RAM, a GPU that can decode Vulkan-based H.264/H.265, and a 15Mbps connection minimum (that's the floor, not the fun). There's a new Flatpak repo so installation and updates don't make you want to scream.

Now the catch, because there's always a catch: the free tier is 1080p with ads. Pay $10/month for Performance and you get 1440p, ray tracing, HDR, 100 hours of play time, and no ads. $20/month for Ultimate pulls you up to 5K from a GeForce RTX 5080 with 360 FPS and eight-hour sessions. Nvidia says it's optimized DLSS frame generation for the cloud to cut latency at higher resolutions — games should feel local-ish. All these tweaks apply to ChromeOS, Mac, and Windows too, so your Chromebook gets better for free.

The skeptical take, and the commenters nailed it: this is browser gaming with better seats, not "gaming on Linux." It's the fun of NOT owning your hardware. If you like running things yourself, Proton's right there. But if you just want to hit play and stop messing with driver purgatory, this is the first real cloud-streaming option that doesn't feel like a beta apology.

## 2. I used OpenFactory to build my own Linux distro overnight — this AI tool is going to be big

**Publisher:** ZDNET · **Link:** https://www.zdnet.com/article/openfactory-is-an-impressive-new-service-that-allows-you-to-build-your-own-linux-distribution/ · **Karakeep doc:** `h8ptcacyjqb56etamugec9kv`

Jack Wallen claims he typed a prompt and got a custom Linux distro built "overnight" using OpenFactory, an alpha service that lets you describe an OS in plain English (or click a menu) and get a bootable ISO back. Pick a base like Debian or Ubuntu, tell it what desktop and apps you want, hit Validate Recipe and then Start Build, and it orchestrates a whole chain of agents — Git Agent, Planning Agent, Config Agent, Apps Agent, Package Agent, Build Agent, Test Agent — to assemble your bespoke distro, even a PinePhone OS.

Here's the unfiltered truth about the actual experience: it was bumpy, in the way that ALL pre-alpha software is. His first successful build gave him a Debian/KDE Plasma distro. His second attempt threw a `Failed to create download package` error on download. His third build took half an hour to hit 58%, produced a 9+ GB ISO with a two-hour download, and then booted into Ubuntu with GNOME and only LibreOffice installed — not the KDE Plasma / macOS-look / full creator toolkit he asked for. The Calamares installer failed. Every bug got fixed by chatting the developer, who added the install-to-disk test loop on Aug 12 after Jack tripped on its absence.

Pricing: a free tier gives 15 ISO builds/month and a single download; $15/month Builder bumps that to 50 builds with 5 hosted VM hours; $59/seat Team adds SSH, snapshots, SBOMs, and BYOK/self-hosted LLM; and a Compliance tier for enterprises. The verdict is basically "impressive idea, rough execution" — the whole pipeline is AI-orchestrated and the agent chain is doing real work, it's just not stable yet. If you've ever wanted a custom distro and didn't want to spend months on Linux From Scratch, this is the shortcut. Just don't build anything you need to be up at 9am.
