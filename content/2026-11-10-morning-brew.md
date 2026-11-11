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

**In short:** OceanBase is Ant Group's open source distributed relational database with MySQL compatibility and HTAP in one engine. Apache 2.0, written in C++. I would say it is overkill for a small homelab, and there is nothing for my projects.

**Key points:**
- Originally developed by Ant Group and contributors, Apache License 2.0
- Shared-nothing distributed architecture with Paxos-based replication
- MySQL-compatible SQL, handles OLTP and OLAP in a single engine (HTAP)
- Horizontal scalability, distributed transactions, multi-tenancy, automatic partitioning
- Written in C++, source at github.com/oceanbase/oceanbase

**Details:** OceanBase is a distributed relational database from Ant Group, Apache 2.0, written in C++. It spreads data across nodes with a shared-nothing layout and Paxos replication, and it runs MySQL-compatible SQL for both transactional and analytical workloads in one engine.

The feature list is long: horizontal scaling, distributed transactions, automatic partitioning, multi-tenancy, HTAP. That is a lot of machinery for one database, and it is aimed at high-volume OLTP with analytics on top, which is more than a three-node k3s cluster needs.

For my setup it does not fit. I run Postgres on CloudNativePG with backups to MinIO, and OceanBase brings a MySQL dialect and a distributed footprint I do not need. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 2. 13 Best Free and Open Source Hard Disk Utilities for System Tweakers - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2018/10/Harddiskimage.jpg)
**Source:** https://www.linuxlinks.com/harddiskutilities/ · **Karakeep:** `iekigkzriummnu9u2xrlym84`

**In short:** LinuxLinks rounded up 13 free and open source hard disk tools, from SMART health monitoring to tuning, benchmarking and secure wiping. I would say it is a useful shopping list, not a replacement for backups.

**Key points:**
- 13 free and open source tools for SMART health, performance tuning, SCSI and NVMe commands, wiping and benchmarking.
- SMART tools include smartmontools, scrutiny, GSmartControl, QDiskInfo and smartctl_exporter.
- hdparm tunes hard disk parameters and Bonnie++ tests hard drive and file system performance.
- openSeaChest covers SATA, SAS, NVMe and USB storage; nwipe is the secure disk eraser.
- The article states SMART is not an alternative to making regular backups.

**Details:** It is a roundup rather than a deep review, and the useful split is health monitoring versus tuning versus wiping. SMART tools dominate, with smartmontools as the obvious base and scrutiny or GSmartControl as friendlier faces. smartctl_exporter is the one that matters to me because it turns SMART into Prometheus metrics. hdparm and Bonnie++ are for tuning and benchmarking, while nwipe is for wiping disks before disposal. I would not treat any of this as a backup plan, and the article says that plainly. For my homelab, the only piece with a real hook is smartctl_exporter, and even then it needs a sane way to run against the OMV box or inside k3s. The rest are standard sysadmin tools I would read about first and use only when a disk actually needs attention.

**For my projects:**
- homelab-2nd: Use smartctl_exporter to expose SMART metrics from the OMV box, if it can be deployed cleanly in k3s or on OMV.

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
