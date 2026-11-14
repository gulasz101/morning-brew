---
date: 2026-11-13
slug: 2026-11-13-morning-brew
tags: Open Source Software, TideMail, Go Programming Language, IMAP SMTP, Terminal Email Client, selfhosted, Git, Source Code Management, Open Source, opensource, open-source, Java, Self-Hosted, PostgreSQL
---

Morning Brew for 2026-11-13: 7 items written from 7 hoarded bookmarks and feeds, 0 dropped after a failed retry.

### RSS

## 1. TideMail - keyboard-first terminal email client - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2021/05/email-text-keyboard-button.jpg)
**Source:** https://www.linuxlinks.com/tidemail-keyboard-first-terminal-email-client/ · **Karakeep:** `b6gdrgkhwd3d6gt3rlxhr9nb`

**In short:** TideMail is a Go, MIT-licensed terminal email client with IMAP, SMTP and a local SQLite cache, and the feature list is long for a TUI. I would say it looks quite good for terminal mail, but the optional AI bits and experimental plugins make it sound a bit busy.

**Key points:**
- Three-pane terminal UI: accounts and folders, message list, selected message.
- IMAP and SMTP with a local SQLite cache for retrieval and searching.
- MIT licensed, written in Go, by Allison Bayless and contributors.
- Linux and macOS supported, with experimental Windows support.
- Optional AI summaries, proofreading and filtering; experimental plugin support including PGP via GnuPG.
- Headless commands with JSON output for automation.

**Details:** I read about this, I did not run it. TideMail is a keyboard-driven email client that runs in a terminal, with account configuration handled through interactive settings screens rather than config files. The article lists a lot: a unified inbox, IMAP sync of read status, stars, archived messages, moves and deletions, account-specific SMTP settings, signatures, draft folders, delayed sending with undo, a persistent outbox with failed-delivery retries, global search, attachments, address completion, vCard contacts, HTML rendering with inline images on Kitty terminals, customisable themes and optional mouse navigation. That is a lot for a terminal client. The AI features are optional, which is good, but I would keep them off until proven. Experimental plugin support and experimental Windows support both point to unfinished edges. It is not a service for my homelab, and I do not see a real fit for the other projects, so nothing for my projects.

**For my projects:** Nothing for my projects.

## 2. Gitblit - self-hosted Git repository management server - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2020/01/Git-Clients.jpg)
**Project:** [gitblit](https://github.com/gitblit-org/gitblit)
**Source:** https://www.linuxlinks.com/gitblit-self-hosted-git-repository-management-server/ · **Karakeep:** `rlxsgjpht47cnhs696zvl87e`

**In short:** Gitblit is a Java self-hosted Git server for small teams, with a web UI, tickets and mirroring. I would say it is capable, but it is not an obvious fit for my cluster.

**Key points:**
- Self-hosted Git repository management server aimed at small development teams and workgroups.
- Serves repositories over Git, HTTP, HTTPS and SSH.
- Web interface for browsing files, branches, tags, commit history, blame and comparisons.
- Authentication via LDAP, PAM, Windows authentication and external providers.
- Includes ticket tracking with comments, milestones, notifications, patchsets and branch-based proposals.
- Apache License 2.0; runs on Linux, macOS and Windows.

**Details:** Gitblit is written in Java and can run standalone or inside a Java servlet container. It offers repository-level permissions, mirroring, federation between Gitblit installs, hooks, indexing and Markdown documentation rendering. There is also a separate graphical client for remote administration and JSON RPC for integration. For my homelab, the missing pieces are the boring ones: the article gives no Kubernetes path, backup story or metrics, and it is Java on top of that. I would treat it as a capable self-hosted Git option for a small team, not something I would drag into Flux. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 3. IvorySQL - Oracle-compatible PostgreSQL database - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2019/03/online-business-database.jpg)
**Source:** https://www.linuxlinks.com/ivorysql-oracle-compatible-postgresql-database/ · **Karakeep:** `oze6keypzgmpbw3xzwxf4kzt`

**In short:** IvorySQL is a Postgres-based database with an Oracle compatibility layer on top. I would say it is useful only for Oracle migrations, and nothing for my projects.

**Key points:**
- PostgreSQL-based relational database with Oracle SQL syntax, procedural constructs and database objects
- Separate PostgreSQL and Oracle compatibility modes
- PL/iSQL supports Oracle-style stored procedures, functions and packages
- Keeps Postgres transaction processing, indexing and query optimisation
- Postgres extensions and administration tools can be used alongside IvorySQL features
- Apache License 2.0, written in C, developed by the IvorySQL community

**Details:** IvorySQL extends Postgres rather than replacing it, so the interesting part is the compatibility layer: Oracle-style SQL, PL/iSQL, packages, extra data types and expressions. It also keeps the normal Postgres bits, including transaction processing, indexing and query optimisation, and you can still use Postgres extensions and admin tools. The separate compatibility modes are sensible, because not every app wants Oracle behaviour.

The catch for me is that it is still a database to run and care for, and the article says nothing about Kubernetes, backups or metrics. My homelab already runs Postgres on CloudNativePG with WAL to MinIO, so swapping in an Oracle-compatible fork would be work for no clear gain. Apache 2.0 is permissive, but that does not fix the operational gap. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 4. Kitesurf is now open source, by Cloudflare Blog
![](https://blog.cloudflare.com/_emdash/api/media/file/01M7B8M86AWYDHNF9C7R2V0CXH.png)
**Source:** https://blog.cloudflare.com/kitesurf-open-source/ · **Karakeep:** `hn4654pzhag8bk0qplzvcmz3`

**In short:** Kitesurf is now open source, and Cloudflare describes it as a browser for agents; it is still under heavy development, so I would treat it as something to watch rather than depend on.

**Key points:**
- Cloudflare has open-sourced Kitesurf.
- The post describes it as a browser for agents.
- It is under heavy development, with focus on engine compatibility, reliability and efficiency.
- Compatibility progress is tracked through Web Platform Tests.
- Contributors need an issue and maintainer vouching before opening a pull request.
- Non-code contributions are welcome, including reproduction pages, failing workflows and documentation fixes.

**Details:** Kitesurf is now open source, and Cloudflare frames it as a browser for agents. From the post, it is under heavy development, with the focus on making the engine more compatible, more reliable and more efficient, including Web Platform Test progress. Contributions are welcome, but the process is guarded: open an issue with a minimal reproduction or proposed approach, get vouched by a maintainer, then open a pull request. Focused fixes with tests and clear scope are preferred over large rewrites. Non-code help counts too, like a small page that reproduces a rendering bug, a failing automation workflow, or a documentation correction. They also point to the blog, changelog, landing page, Web Platform Tests page and benchmarks, and Discord. I would say it is interesting if you want to watch a browser engine for agents take shape, but it is too early to depend on. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 5. Lets move typecraft to planetscale!, by YouTube
![](https://i.ytimg.com/vi/fkFSWG9oyxE/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=fkFSWG9oyxE · **Karakeep:** `d5k904vdt16viyw75tq80z1p`

**In short:** A YouTube video about moving Typecraft to PlanetScale, but I only have the title and no transcript. I would say there is not enough here to judge.

**Key points:**
- Title only: 'Lets move typecraft to planetscale!'.
- No transcript or description was fetched.
- No candidate links were supplied.
- Typecraft and PlanetScale specifics are not in the supplied text.
- I did not watch, install, or run anything.

**Details:** This one is a YouTube video, and the body was not available, so I am working from the title alone. The title says someone is moving Typecraft to PlanetScale, but I do not know what Typecraft means in this context, what moved, or whether it is a database migration, a hosting change, or just a channel update. That is the whole problem with a title-only item. I would say it is not useful for a verdict yet. If there is a real migration in there, I would want the steps, the data size, the downtime, and what broke. Nothing for my projects until I have that. So yeah, that's that.

**For my projects:** Nothing for my projects.

## 6. Adapting to AI penetration testing orchestrators: The Modern Security Model, by Cloudflare Blog
![](https://blog.cloudflare.com/_emdash/api/media/file/01M7B3YCV0VN7GFCA6VK7EE9RR.png)
**Source:** https://blog.cloudflare.com/adapting-to-ai-penetration-testing-orchestrators/ · **Karakeep:** `n2tz4onwsup8nxv051vyu2v7`

**In short:** A Cloudflare post about AI penetration-testing orchestrators and its 'Modern Security Model', built on identity gating and micro-segmentation. I would say it is vendor framing with a sales call at the end, but the containment-first point is sensible.

**Key points:**
- By Blake Darché and Myles Sloan on the Cloudflare Blog
- AI penetration-testing orchestrators and automated attack frameworks are framed as a challenge to legacy defence models
- Legacy defence-in-depth with a classic network DMZ is described as falling short in complex architectures
- Legacy and on-premises equipment should be identity-gated and unreachable from the Internet
- Micro-segmentation aims to slow lateral movement or make it noisier
- The model is containment-first, aimed at cases where users keep losing keys

**Details:** The post argues that AI-driven penetration testing changes the threat model enough to break old defence-in-depth habits. The replacement it offers is identity-gated access for legacy and on-premises gear, plus micro-segmentation to make lateral movement slower or noisier, under a containment-first framing. It also says the historical DMZ model is not enough for complex architectures and that attacks will get worse as orchestration tools become normal. Fair enough, yeah, but the piece ends by pointing at Cloudforce One and Solutions Engineering, so it is selling a model as much as explaining one. Nothing for my projects. I run a small k3s homelab with Cloudflare Tunnels, but this is enterprise security positioning rather than a tool I can drop in.

**For my projects:** Nothing for my projects.

## 7. 7 Best Free and Open Source Supply Chain Integrity Tools - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2025/12/117-security.png)
**Source:** https://www.linuxlinks.com/best-free-open-source-supply-chain-integrity-tools/ · **Karakeep:** `o3cw1nrhmnzh2zgi3jbn653y`

**In short:** LinuxLinks lists seven free and open source supply chain integrity tools, from cosign and in-toto to Connaisseur and gittuf. It is a useful index, but it is a directory page rather than a test report.

**Key points:**
- Seven tools are named: cosign, in-toto, Connaisseur, Witness, SLSA verifier, Notation and gittuf.
- The listed jobs include signing, signature verification, build attestations, policy enforcement, provenance checks and tamper evidence.
- The article highlights CI/CD, containers and Kubernetes as the main use cases.
- Only free and open source software is eligible for the LinuxLinks chart.
- Connaisseur is the Kubernetes-specific entry, enforcing container image signature verification.

**Details:** This is a LinuxLinks roundup, so it is a list with one-line jobs rather than a deep review. The useful part for me is the spread: cosign signs and verifies container images and other artifacts, in-toto records verifiable build steps, Witness handles attestations, SLSA verifier checks provenance, Notation signs OCI artifacts, gittuf adds policy and tamper evidence to Git, and Connaisseur enforces image signature verification in Kubernetes. That last one is the closest thing to my world, because homelab-2nd is a k3s cluster, but the page does not say how any of these behave in a Flux-driven setup or what they cost in day-to-day maintenance. I would say the page is a decent starting index, and the tools themselves are only worth judging one at a time. Nothing for my projects right now.

**For my projects:** Nothing for my projects.

**Projects:**
- [cosign](https://github.com/sigstore/cosign): Code signing and transparency for containers and binaries - sigstore/cosign.
- [in-toto](https://github.com/in-toto/in-toto): In-toto is a framework to protect supply chain integrity. - in-toto/in-toto.
- [Connaisseur](https://github.com/sse-secure-systems/connaisseur): An admission controller that integrates Container Image Signature Verification into a Kubernetes cluster.
- [Witness](https://github.com/in-toto/witness): Witness is a pluggable framework for software supply chain risk management. It automates, normalizes, and verifies software artifact provenance. - in-toto/witness.
- [SLSA verifier](https://github.com/slsa-framework/slsa-verifier): Verify provenance from SLSA compliant builders. Contribute to slsa-framework/slsa-verifier development by creating an account on GitHub.
- [Notation](https://github.com/notaryproject/notation): A CLI tool to sign and verify artifacts. Contribute to notaryproject/notation development by creating an account on GitHub.
- [gittuf](https://github.com/gittuf/gittuf): A security layer for Git repositories. Contribute to gittuf/gittuf development by creating an account on GitHub.
