---
date: 2026-11-10
slug: 2026-11-10-morning-brew
tags: 
---

Morning Brew for 2026-11-10: 2 items written from 2 hoarded bookmarks and feeds, 0 dropped after a failed retry.

### RSS

## 1. OceanBase - distributed relational database - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2019/03/online-business-database.jpg)
**Project:** [oceanbase](https://github.com/oceanbase/oceanbase)
**Source:** https://www.linuxlinks.com/oceanbase-distributed-relational-database/ · **Karakeep:** `vqdtx7s351ktjcc3ho36kr04`

**In short:** OceanBase is an open source distributed relational database from Ant Group, MySQL-compatible and Apache 2.0 licensed. I would say it is serious on paper, but too much for my small homelab.

**Key points:**
- Distributed relational database with SQL support and MySQL compatibility.
- Shared-nothing architecture with horizontal scalability and Paxos-based replication.
- HTAP support for OLTP and OLAP in one database.
- Distributed transactions, automatic partition management and multi-tenancy are listed features.
- Developed by Ant Group and contributors, licensed Apache 2.0, written in C++.
- The listed website points to the GitHub repository, candidate link 1.

**Details:** OceanBase is a distributed relational database from Ant Group, built as shared-nothing and MySQL-compatible, with Paxos replication, horizontal scaling, distributed transactions, automatic partition management and multi-tenancy. It targets HTAP, so operational and analytical workloads in one engine. The licence is Apache 2.0 and the code is C++. For my homelab, there is no Kubernetes path, backup story or metrics mentioned here, so it is not going in without a fight. Nothing for my projects. I would call it a serious database, but too much for three workers and one durable storage box.

**For my projects:** Nothing for my projects.

## 2. 13 Best Free and Open Source Hard Disk Utilities for System Tweakers - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2018/10/Harddiskimage.jpg)
**Source:** https://www.linuxlinks.com/harddiskutilities/ · **Karakeep:** `iekigkzriummnu9u2xrlym84`

**In short:** LinuxLinks rounds up thirteen free and open source disk utilities for Linux, covering SMART health checks, tuning, secure erase and benchmarking. I would say it is a handy reference, not a must-read.

**Key points:**
- Thirteen utilities are listed: NVMe-CLI, Smartmontools, scrutiny, openSeaChest, GSmartControl, hdparm, sg3_utils, sdparm, QDiskInfo, nwipe, smartctl_exporter, GNOME Disks and Bonnie++.
- The article stresses that SMART monitoring is not a substitute for regular backups.
- Coverage spans NVMe, SATA, SAS and USB storage, plus SCSI commands and disk tuning.
- smartctl_exporter exposes SMART drive metrics to Prometheus; GNOME Disks and GSmartControl provide graphical views.
- nwipe is included for secure disk erasing; Bonnie++ is for drive and file system performance testing.

**Details:** This is a LinuxLinks roundup by Steve Emms, dated 10 November 2026, listing free and open source tools for checking disk health and tweaking performance. It opens with the usual warning that backups matter and SMART is only a monitoring aid, which I think is the right framing. The list mixes low-level CLI tools such as hdparm, sg3_utils and sdparm with GUIs like GSmartControl, QDiskInfo and GNOME Disks, plus scrutiny for smartd and smartctl_exporter for Prometheus. There is also nwipe for secure erasure and Bonnie++ for benchmarking. I would say it is useful as a catalogue when a disk starts behaving oddly, but most entries are point tools rather than a complete storage workflow. Nothing for my projects.

**For my projects:** Nothing for my projects.

**Projects:**
- [NVMe-CLI](https://github.com/linux-nvme/nvme-cli): NVMe management command line interface. Contribute to linux-nvme/nvme-cli development by creating an account on GitHub.
- [Smartmontools](https://www.smartmontools.org/): [BOT-WALL].
- [scrutiny](https://github.com/AnalogJ/scrutiny): Hard Drive S.M.A.R.T Monitoring, Historical Trends &amp; Real World Failure Thresholds - AnalogJ/scrutiny.
- [openSeaChest](https://github.com/Seagate/openSeaChest): Cross platform utilities useful for configuring features and assessing health on SATA, SAS, NVMe, and USB storage devices. - Seagate/openSeaChest.
- [GSmartControl](https://gsmartcontrol.shaduri.dev/): GSmartControl Hard disk drive and SSD health inspection tool SCAM ALERT: gsmartcontrol[.]com is a phishing site! Please don&#39;t download anything...
- [hdparm](https://sourceforge.net/projects/hdparm/): Download hdparm for free. hdparm - get/set ATA/SATA drive parameters under Linux.
- [sg3_utils](https://sg.danny.cz/sg/sg3_utils.html): The sg3_utils package.
- [sdparm](https://sg.danny.cz/sg/sdparm.html): Linux sdparm utility.
- [QDiskInfo](https://github.com/edisionnano/QDiskInfo): QDiskInfo is a frontend for smartctl (part of the smartmontools package). It provides a user experience similar to CrystalDiskInfo. It shows the SMART (Self-Monitoring, Analysis, and Reporting Tech...
- [nwipe](https://github.com/martijnvanbrummelen/nwipe): Nwipe secure disk eraser. Contribute to martijnvanbrummelen/nwipe development by creating an account on GitHub.
- [smartctl_exporter](https://github.com/prometheus-community/smartctl_exporter): Export smartctl statistics to prometheus. Contribute to prometheus-community/smartctl_exporter development by creating an account on GitHub.
- [GNOME Disks](https://www.gnome.org/): An easy and elegant way to use your computer.
- [Bonnie++](https://www.coker.com.au/bonnie++/): Bonnie++ now at 1.03e (last version before 2.0)!
