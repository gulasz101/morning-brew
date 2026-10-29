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

**In short:** YaST Expert Partitioner is YaST's graphical storage tool for disks, partitions, LVM, RAID, encryption and Bcache. It looks capable, but it is a desktop administration utility, so I would say it is not an obvious fit for my setup.

**Key points:**
- From the YaST project, developed by the YaST Team.
- Free and open source under GNU GPL v2.0 or v3.0.
- Written in Ruby.
- Covers partitions, filesystems, mount points, LVM, MD RAID, LUKS1 and LUKS2, Bcache and Btrfs.
- Changes can be reviewed before they are written to storage.
- The linked source repository is yast-storage-ng.

**Details:** YaST Expert Partitioner is an advanced storage management tool from the YaST project. It gives detailed control over disks, partitions and filesystems, including creating, deleting, moving and resizing partitions, with changes reviewable before they hit the device. It goes beyond basic partition editing into LVM, software RAID, LUKS encryption, Bcache and Btrfs, plus NFS mounts and cloning partition layouts between disks. It is free and open source under GPL v2.0 or v3.0, written in Ruby, and developed by the YaST Team.

The feature list is broad, and LUKS1 plus LUKS2 support is a useful detail. For me, though, this is a desktop administration tool rather than something I would wire into a Flux-managed k3s cluster or the M1 Max image stack. Nothing for my projects, I would say, unless I was already running SUSE and wanted one graphical place to inspect storage before touching it.

**For my projects:** Nothing for my projects.

## 2. 10x engineer (AI Psychosis), by Kai Lentit
![](https://i.ytimg.com/vi/WV6A1Zf3F2Q/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=WV6A1Zf3F2Q · **Karakeep:** `mvaijebig8zb3zvu59ikp9o0`

**In short:** A YouTube sketch by Kai Lentit mocking AI-era 10x-engineer culture; funny in places, but there is nothing to build or deploy from it.

**Key points:**
- YouTube video '10x engineer (AI Psychosis)' by Kai Lentit, transcript dated 2026-10-22.
- Comedy about cloud and bedroom clusters, no tests, LLMs reading code, NixOS, and cancelled Claude plans.
- Throws in GPT-5 as a front end to DeepSeek in Chinese, a 38-week supplier lead time, and 3200 botnet cores.
- No tool, version, benchmark, licence, or implementation detail is provided; it is a joke sketch.

**Details:** It is a rapid-fire sketch about two people talking over each other while building absurd AI infrastructure. The jokes land on familiar targets: rewriting engines without tests, putting clusters where a mattress should be, arguing about NixOS, and treating LLMs as if they remove the need for engineering discipline. I only have the transcript, and it is messy, which suits the bit but makes it hard to quote cleanly.

I would say it is worth a watch if you like this kind of chaos, but there is no product here and nothing I would put into my homelab. Nothing for my projects. The useful part is only the reminder that hype culture can make bad engineering sound normal.

**For my projects:** Nothing for my projects.

## 3. Issabel - Rocky Linux-based PBX distribution - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2024/04/Linux-Distributions.png)
**Project:** [issabel.com/get-issabel](https://www.issabel.com/en/get-issabel)
**Source:** https://www.linuxlinks.com/issabel-rocky-linux-based-pbx-distribution/ · **Karakeep:** `i0uz9k47xc27ci6zjov6hfb4`

**In short:** Issabel is a Rocky Linux-based PBX distribution around Asterisk with a web admin; I would say it is a serious phone system and not worth it for me.

**Key points:**
- Rocky Linux-based server distribution for unified communications and IP telephony.
- Combines the Asterisk PBX platform with a web-based administration interface.
- Originated as a fork of Elastix.
- Features include IVR menus, call queues, voicemail, recording, reports, SIP telephony, MiroTalk video conferencing and optional contact centre capabilities.
- Working state is active; desktop is none, init is systemd, package management is DNF, release model is fixed, platform is x86_64.
- Home page is issabel.com; developer is the Issabel community.

**Details:** Issabel is a Rocky Linux-based server distribution for unified communications and IP telephony, built around Asterisk with a web-based admin. It is a fork of Elastix and covers voice calls, extensions, voicemail, conferencing and call centre work. The article lists IVR menus, call queues, recording, reports, SIP telephony and MiroTalk video, plus optional contact centre capabilities. Unfortunately it gives no version number, release date or install size. I would say it is a serious PBX and not worth it for me. One platform, x86_64, which that's narrow. Nothing for my projects. So yeah, that's that.

**For my projects:** Nothing for my projects.
