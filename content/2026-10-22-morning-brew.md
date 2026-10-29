---
date: 2026-10-22
slug: 2026-10-22-morning-brew
tags: Linux, Open Source Software, File Systems, Storage Management, Disk Partitioning, Software Engineering, Machine Learning, Artificial Intelligence, Programming, VoIP, Linux Distribution, Unified Communications, Telephony, Asterisk
---

Morning Brew for 2026-10-22: 3 items written from 3 hoarded bookmarks and feeds, 0 dropped after a failed retry.

### RSS

## 1. YaST Expert Partitioner - advanced storage partitioning tool - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2022/11/hard-drive-partitioning.png)
**Project:** [yast-storage-ng](https://github.com/yast/yast-storage-ng)
**Source:** https://www.linuxlinks.com/yast-expert-partitioner-advanced-storage-partitioning-tool/ · **Karakeep:** `al87hxlbeudj4wi12pta1y5t`

**In short:** YaST Expert Partitioner is a graphical Linux storage tool for disks, partitions, LVM, RAID, encryption and Btrfs. It looks thorough, but it is a desktop partitioner with no Kubernetes or backup story, so nothing for my projects.

**Key points:**
- From the YaST project, written in Ruby, licensed GPL v2.0 or v3.0.
- Graphical creation, deletion, moving and resizing of partitions, with changes reviewable before writing.
- Full management of LVM physical volumes, volume groups and logical volumes, plus Linux MD software RAID.
- Supports LUKS1 and LUKS2 encryption, Bcache, Btrfs subvolumes, quota groups and multi-device configurations.
- Can create partition tables, clone partition layouts between disks, and edit NFS mounts alongside local storage.

**Details:** YaST Expert Partitioner is the YaST storage tool for detailed disk work. It handles partitions, filesystems, mount points, LVM, software RAID, LUKS encryption, Bcache, Btrfs subvolumes and NFS mounts, and it lets you review changes before writing them. That is a lot of storage surface in one graphical tool.

The catch for me is where it lives. It is a graphical partitioner, not a Kubernetes operator, and the write-up mentions no backup or metrics story. My homelab storage sits behind CloudNativePG, MinIO on OMV and Flux, so I would not add a manual partitioning step there. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 2. 10x engineer (AI Psychosis), by Kai Lentit
![](https://i.ytimg.com/vi/WV6A1Zf3F2Q/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=WV6A1Zf3F2Q · **Karakeep:** `mvaijebig8zb3zvu59ikp9o0`

**In short:** A chaotic YouTube skit about AI psychosis and '10x engineer' culture; funny in places, but not a useful technical source.

**Key points:**
- Title and creator: '10x engineer (AI Psychosis)' by Kai Lentit, a YouTube video.
- Karakeep document id mvaijebig8zb3zvu59ikp9o0; transcript dated 2026-10-22 and produced with Parakeet.
- The dialogue is a rapid-fire parody of AI-era engineering habits: no tests, rewrites, cloud spend, model front-ends, botnets, and homelab chaos.
- It names GPT-5, DeepSeek, MariaDB, S3, NixOS, Claude, Ralph loops, and a Mac Mini cluster, but mostly as jokes.
- No candidate links were supplied with this item.

**Details:** This reads like a comedy sketch built from engineer in-jokes. Someone rewrites an engine with no tests, runs things on AWS and a bedroom Mac Mini cluster, uses GPT-5 only to prompt DeepSeek in Chinese, and worries about Skynet on MariaDB. The jokes lean on LLM culture, cloud bills, NixOS tinkering, cancelled Claude plans, and absurd homelab upgrades. I read it as satire, not advice. The transcript is messy and fast, so it is hard to pull a concrete lesson from it. I would say it is worth a laugh if you already live in this world, but not worth it as a source for decisions. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 3. Issabel - Rocky Linux-based PBX distribution - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2024/04/Linux-Distributions.png)
**Project:** [issabel.com/get-issabel](https://www.issabel.com/en/get-issabel)
**Source:** https://www.linuxlinks.com/issabel-rocky-linux-based-pbx-distribution/ · **Karakeep:** `i0uz9k47xc27ci6zjov6hfb4`

**In short:** Issabel is a Rocky Linux server distribution built around Asterisk for business telephony. I would say it is a niche PBX box, not something I need.

**Key points:**
- Rocky Linux-based unified communications and IP telephony server distribution with web-based administration and Asterisk PBX.
- Fork of Elastix, covering voice calls, extensions, voicemail, conferencing and call centre operations.
- Features include IVR menus, call queues, voicemail, call recording, call detail reports, SIP telephony, MiroTalk video conferencing and optional contact centre capabilities.
- Active project with no desktop, systemd, DNF, fixed release model and x86_64 only.
- Developer is the Issabel community, home page is www.issabel.com.
- Candidate link [1] is the get-Issabel page.

**Details:** I read about Issabel, a Rocky Linux distribution for unified communications and IP telephony, built around Asterisk with a web administration interface. It covers voice calls, extensions, voicemail, conferencing and call centre work, and it came out of an Elastix fork. The feature list is sensible: IVR menus, call queues, voicemail, recording, call detail reports, SIP telephony, video conferencing through MiroTalk and optional contact centre capabilities. On the packaging side it uses DNF, systemd, a fixed release model and x86_64 only, with no desktop because administration is through the web.

The bad news for my setup is that it is a whole server distribution, so it is not a small service I can drop into k3s. There is no Kubernetes path, no backup story and no metrics mentioned, and it is x86_64 only. I would say it is quite a complete PBX if you want one box, but for homelab-2nd it is too much. Candidate link [1] is the get-Issabel page. Nothing for my projects.

**For my projects:** Nothing for my projects.
