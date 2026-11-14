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

**In short:** TideMail is a Go terminal email client with IMAP/SMTP, a local SQLite cache and a three-pane UI; I would say it looks handy for terminal mail, but it has nothing for my projects.

**Key points:**
- Three-pane TUI: accounts and folders on the left, message list above, selected message below.
- IMAP and SMTP with a local SQLite cache for retrieval and search.
- Optional AI summaries, proofreading and filtering; experimental plugins including PGP via GnuPG.
- MIT licence, written in Go, by Allison Bayless and contributors.
- Runs on Linux and macOS, with experimental Windows support.

**Details:** It tries to mix terminal mail with graphical conveniences: mouse support, formatted rendering, delayed send with undo, a persistent outbox with retries, global search, attachments, vCard contacts and HTML rendering with inline images on Kitty terminals. Account setup is through interactive screens rather than config files, and there are headless search, draft and send commands with JSON output. The AI features are optional, and plugin support is experimental. I have only read about it. For my homelab I would want a Kubernetes path, backups and metrics, and this is a client, so nothing for my projects. For riff practice and local image work it is not a fit either.

**For my projects:** Nothing for my projects.

## 2. Gitblit - self-hosted Git repository management server - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2020/01/Git-Clients.jpg)
**Project:** [gitblit](https://github.com/gitblit-org/gitblit)
**Source:** https://www.linuxlinks.com/gitblit-self-hosted-git-repository-management-server/ · **Karakeep:** `rlxsgjpht47cnhs696zvl87e`

**In short:** Gitblit is a self-hosted, Java-based Git repository management server with a web UI, tickets and mirroring; I would say it is feature-rich but heavier and less obvious a fit than Gitea or Forgejo.

**Key points:**
- Self-hosted Git server for small teams, written in Java and released under the Apache License 2.0.
- Hosts repositories over Git, HTTP, HTTPS and SSH, with a responsive web UI for files, branches, tags, history, syntax highlighting, blame and comparisons.
- Authentication covers LDAP, PAM, Windows authentication and external providers, with repository-level access restrictions and user/team permissions.
- Includes ticket tracking with comments, milestones, notifications, patchsets and branch-based change proposals, plus server-side merging, voting and watching.
- Also does repository mirroring, personal repositories, forks, federation between Gitblit installs, hooks, indexing and search.
- Runs standalone or in a Java servlet container, can act as a repository viewer only, and ships a separate graphical management client.

**Details:** Gitblit is aimed at small development teams and workgroups that want to host their own source code. It can serve repositories over several transports, browse them in a web UI, and manage accounts, teams and permissions. It also has ticket tracking, patchset collaboration, mirroring, federation and hooks, plus Markdown rendering, RSS, email notifications and JSON RPC. Cross-platform support covers Linux, macOS and Windows.

Unfortunately, it is a Java application and the article gives no Kubernetes, backup or metrics story. It can run standalone or inside a servlet container, and it can be configured as a read-only viewer, but that still leaves the operational questions open. I would say it is a capable Git server if a Java stack is already normal for you, but not worth it for me when lighter self-hosted forges exist.

**For my projects:** Nothing for my projects.

## 3. IvorySQL - Oracle-compatible PostgreSQL database - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2019/03/online-business-database.jpg)
**Source:** https://www.linuxlinks.com/ivorysql-oracle-compatible-postgresql-database/ · **Karakeep:** `oze6keypzgmpbw3xzwxf4kzt`

**In short:** IvorySQL is a PostgreSQL-based database with Oracle compatibility modes, PL/iSQL and Oracle-style packages. It is free under Apache 2.0, but it solves no problem in my stack.

**Key points:**
- PostgreSQL-based relational database with added Oracle compatibility features.
- Separate PostgreSQL and Oracle compatibility modes, plus PL/iSQL with stored procedures and packages.
- Keeps PostgreSQL transaction processing, indexing, query optimisation and extension support.
- Apache License 2.0, written in C, developed by the IvorySQL community.
- The article gives no version number, pricing or benchmark figures.

**Details:** It is built for the dull migration case: an Oracle application that needs to move to PostgreSQL without rewriting everything. The compatibility layer covers Oracle-style SQL syntax, data types, expressions, functions and procedural constructs, while still leaving PostgreSQL facilities available. I would say that is a sensible migration tool rather than a database I would choose for a new project. For my homelab there is no Oracle anywhere in the stack, and CloudNativePG already covers normal Postgres, so this is nothing for my projects. So yeah, that's that.

**For my projects:** Nothing for my projects.

## 4. Kitesurf is now open source, by Cloudflare Blog
![](https://blog.cloudflare.com/_emdash/api/media/file/01M7B8M86AWYDHNF9C7R2V0CXH.png)
**Source:** https://blog.cloudflare.com/kitesurf-open-source/ · **Karakeep:** `hn4654pzhag8bk0qplzvcmz3`

**In short:** Kitesurf is Cloudflare's open-source browser for agents, tagged with Rust and WebAssembly; unfortunately it is still under heavy development, so I would say watch it rather than adopt it.

**Key points:**
- Open-sourced by Cloudflare; the post is by Celso Martinho.
- Described as a browser for agents, with tags including Rust, WebAssembly and Workers.
- Still under heavy development, focused on compatibility, reliability and efficiency.
- Contributors must open an issue, get vouched by a maintainer, then open a pull request.
- Non-code help counts: reproduction pages, failing workflows and documentation fixes.
- Community chat is on Discord, with updates via the blog, changelog and landing page.

**Details:** Unfortunately, Kitesurf is still under heavy development, and Cloudflare is focused on compatibility, reliability and efficiency rather than polish. It is an open-source browser for agents, posted by Celso Martinho, with tags for Rust, WebAssembly and Workers. The contribution path is gated: open an issue, get vouched by a maintainer, then open a pull request. Focused fixes with tests are preferred, and non-code reports such as a small reproduction page or documentation correction also help. There is Discord for chat, plus blog, changelog and landing page updates. I have not tried it. Nothing for my projects: I do not have an agent browser workload, and this is not a local image tool.

**For my projects:** Nothing for my projects.

## 5. Lets move typecraft to planetscale!, by YouTube
![](https://i.ytimg.com/vi/fkFSWG9oyxE/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=fkFSWG9oyxE · **Karakeep:** `d5k904vdt16viyw75tq80z1p`

**In short:** A YouTube video about moving typecraft to PlanetScale, but only the title was available, so I cannot say what the migration actually involved.

**Key points:**
- Title only: "Lets move typecraft to planetscale!"
- No source text was fetched for this item.
- No candidate links were supplied.
- PlanetScale is named in the title, but no version, price, migration step or result is given.

**Details:** This one is a YouTube video and the body did not come through, so I am working from the title alone. It sounds like a migration story for something called typecraft onto PlanetScale, but that is all I can honestly take from it. I did not watch it, so I cannot say whether it is a database move, a hosting move, or just a discussion. If the video is public, the useful part would be the before and after: what broke, what the bill looked like, and whether the app stayed simple. Without that, there is not much to judge. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 6. Adapting to AI penetration testing orchestrators: The Modern Security Model, by Cloudflare Blog
![](https://blog.cloudflare.com/_emdash/api/media/file/01M7B3YCV0VN7GFCA6VK7EE9RR.png)
**Source:** https://blog.cloudflare.com/adapting-to-ai-penetration-testing-orchestrators/ · **Karakeep:** `n2tz4onwsup8nxv051vyu2v7`

**In short:** Cloudflare argues that AI penetration-testing orchestrators make old defence-in-depth look tired, and pitches identity-gated access plus micro-segmentation as the modern answer. I would say it is a sales-tinged security model, not a tool I can run.

**Key points:**
- Cloudflare post tagged Attacks, LLM, Penetration Testing and Security.
- Says legacy defence-in-depth, with a classic network DMZ, falls short in complex architectures.
- Proposes identity-gated access for legacy and on-premises devices.
- Uses micro-segmentation to make lateral movement slower or noisier.
- Frames the result as a containment-first Modern Security Model.
- Points readers to Cloudforce One for active incidents and Solutions Engineering for implementation help.

**Details:** Cloudflare's argument is that AI penetration testing orchestrators are becoming normal, so the old model with a classic DMZ is not enough. They want legacy and on-premises gear made unreachable without identity, then micro-segmentation to make lateral movement slower or noisier. The whole thing is framed as containment-first, which is fair enough, but it reads like a position paper with a contact form at the end. There are no versions, prices or benchmarks in the supplied text, so I cannot judge cost or effort. For my homelab it is mostly a reminder to keep public tunnels identity-gated and namespaces separated, not a project I need to adopt this week. So yeah, that's that.

**For my projects:** Nothing for my projects.

## 7. 7 Best Free and Open Source Supply Chain Integrity Tools - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2025/12/117-security.png)
**Source:** https://www.linuxlinks.com/best-free-open-source-supply-chain-integrity-tools/ · **Karakeep:** `o3cw1nrhmnzh2zgi3jbn653y`

**In short:** LinuxLinks lists seven free and open source supply chain integrity tools, from cosign to gittuf. It is a useful index of names, but it does not tell me which one to actually deploy.

**Key points:**
- Steve Emms's roundup names seven tools: cosign, in-toto, Connaisseur, Witness, SLSA verifier, Notation and gittuf.
- Only free and open source software is eligible for the LinuxLinks ratings chart.
- The tools cover signing and verifying artifacts, build attestations, provenance checks and Git repository tamper evidence.
- Connaisseur is the one with a direct Kubernetes angle: it enforces container image signature verification in the cluster.
- The article gives one-line descriptions, not install steps, versions, licences or benchmark numbers.

**Details:** This is a LinuxLinks roundup dated 13 November 2026, so it reads like a catalogue more than a review. I would say it is handy for names and categories: cosign for signing container images and artifacts, in-toto for verifiable build steps, Witness for attestations, SLSA verifier for provenance, Notation for OCI artifacts, gittuf for Git policies, and Connaisseur for Kubernetes admission checks. The page is short on detail though. There are no versions, no setup notes and no failure modes, so I cannot tell how heavy any of these would be in a real pipeline. The useful bit is the Kubernetes mention, because an admission check would be the natural place to enforce image signatures in my cluster. Still, this list alone is not enough to pick one. I would treat it as a starting index and go read each project's own docs before touching production.

**For my projects:**
- homelab-2nd: Connaisseur could act as the admission check in my k3s cluster so Flux-deployed images are rejected unless they carry a valid signature.

**Projects:**
- [cosign](https://github.com/sigstore/cosign): Code signing and transparency for containers and binaries - sigstore/cosign.
- [in-toto](https://github.com/in-toto/in-toto): In-toto is a framework to protect supply chain integrity. - in-toto/in-toto.
- [Connaisseur](https://github.com/sse-secure-systems/connaisseur): An admission controller that integrates Container Image Signature Verification into a Kubernetes cluster.
- [Witness](https://github.com/in-toto/witness): Witness is a pluggable framework for software supply chain risk management. It automates, normalizes, and verifies software artifact provenance. - in-toto/witness.
- [SLSA verifier](https://github.com/slsa-framework/slsa-verifier): Verify provenance from SLSA compliant builders. Contribute to slsa-framework/slsa-verifier development by creating an account on GitHub.
- [Notation](https://github.com/notaryproject/notation): A CLI tool to sign and verify artifacts. Contribute to notaryproject/notation development by creating an account on GitHub.
- [gittuf](https://github.com/gittuf/gittuf): A security layer for Git repositories. Contribute to gittuf/gittuf development by creating an account on GitHub.
