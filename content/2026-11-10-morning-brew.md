---
date: 2026-11-10
slug: 2026-11-10-morning-brew
tags: 
---

Morning Brew for 2026-11-10: 2 items written from 2 hoarded bookmarks and feeds, 0 dropped after a failed retry.

### RSS

## 1. OceanBase - distributed relational database - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2019/03/online-business-database.jpg)
**Source:** https://www.linuxlinks.com/oceanbase-distributed-relational-database/ · **Karakeep:** `vqdtx7s351ktjcc3ho36kr04`

**In short:** OceanBase is Ant Group's distributed relational database with MySQL compatibility and HTAP support. I would say it is impressive, but too much for my cluster.

**Key points:**
- Distributed relational database with SQL support and MySQL compatibility.
- Shared-nothing architecture with horizontal scalability and Paxos-based replication.
- Hybrid transactional and analytical processing in one database.
- Multi-tenancy, distributed transactions and automatic partition management.
- Apache License 2.0; written in C++; developer is Ant Group and contributors.
- The listing gives no version number.

**Details:** OceanBase spreads data and processing across multiple servers, combines OLTP and OLAP workloads in one engine, and keeps strong consistency while nodes fail. It also offers MySQL-compatible SQL interfaces, which should make migration easier for existing applications.

I would say the missing pieces matter more for me. The page does not give a Kubernetes path, backup story or metrics, and my k3s has three workers, which that's small for a distributed database. Nothing for my projects.

So yeah, that's that.

**For my projects:** Nothing for my projects.

## 2. 13 Best Free and Open Source Hard Disk Utilities for System Tweakers - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2018/10/Harddiskimage.jpg)
**Source:** https://www.linuxlinks.com/harddiskutilities/ · **Karakeep:** `iekigkzriummnu9u2xrlym84`

**In short:** A LinuxLinks roundup of 13 free and open source hard disk tools covering SMART health, tuning, wiping and performance testing. Useful as a checklist, but most of it is familiar Linux kit.

**Key points:**
- 13 tools listed, all free and open source, in an article by Steve Emms dated 10 November 2026.
- SMART monitoring tools include Smartmontools, scrutiny, GSmartControl and QDiskInfo.
- Tuning and device control tools include hdparm, sg3_utils, sdparm, openSeaChest and NVMe-CLI.
- Also covers nwipe, smartctl_exporter, GNOME Disks and Bonnie++.
- The article warns that SMART is not a replacement for regular backups.

**Details:** The list splits into a few clear jobs. For health checks there is Smartmontools, scrutiny, GSmartControl and QDiskInfo. For tuning and low-level device work there is hdparm, sg3_utils, sdparm, openSeaChest and NVMe-CLI. nwipe handles secure erasing, smartctl_exporter exposes SMART metrics to Prometheus, GNOME Disks covers partitions and basic management, and Bonnie++ is there for performance testing. The useful warning is up front: SMART is not an alternative to backups, and disks fail without much warning. I would say the roundup is handy if you want names to look up later, but it does not tell you which one to pick for a given setup. For my homelab, smartctl_exporter is the one with a real path in, because it feeds metrics into Prometheus. The rest are either desktop tools or command line utilities I would only reach for during maintenance.

**For my projects:**
- homelab-2nd: Run smartctl_exporter as a DaemonSet so SMART metrics from each node land in Prometheus with the rest of the cluster monitoring.

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
