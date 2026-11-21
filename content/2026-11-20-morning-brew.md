---
date: 2026-11-20
slug: 2026-11-20-morning-brew
tags: GNAT Studio, SPARK, Formal Verification, Integrated Development Environment, Ada, Financial Research, Presentation Generation, Hebbia, GPT-6 Astra, AI Citations, Linux, Snooze, Job Scheduling, Cron Alternative
---

Morning Brew for 2026-11-20: 13 items written from 13 hoarded bookmarks and feeds, 0 dropped after a failed retry.

### RSS

## 1. GNAT Studio - IDE for Ada and SPARK development - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2020/01/IDE-Vector.jpg)
**Project:** [GNAT Studio](https://github.com/AdaCore/gnatstudio)
**Source:** https://www.linuxlinks.com/gnat-studio-ide-ada-spark-development/ · **Karakeep:** `s2iu7j4704681lw83uekok75`

**In short:** GNAT Studio is AdaCore's IDE for Ada and SPARK, free under GPL v3 and cross-platform. It is not something I would reach for in my own stack.

**Key points:**
- IDE for Ada and SPARK, with additional C and C++ support, from AdaCore.
- Free and open source under GNU GPL v3.0.
- Runs on Linux and Windows.
- Includes LSP support, a graphical debugger, refactoring and SPARK verification integration.
- Extensible through plugins.

**Details:** It bundles source editing, project management, compilation, debugging and analysis in one place, and it works with GNAT project files. The feature list is broad: syntax highlighting, completion, navigation, breakpoints, expression evaluation, renaming, dependency and call analysis, plus GNATcoverage and GNAT Static Analysis Suite integration. The SPARK part is the interesting bit if you care about verification, because it brings correctness checks into the same workflow. For me it stops there. I do not write Ada or SPARK, and an IDE is not going to make my code factory or agent fleet stricter on its own. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 2. Hebbia sees improvements in financial research with GPT-6 Astra, by OpenAI
![](https://images.ctfassets.net/kftzwdyauwt9/70gWqYyqb096it9EoD7OqI/5df8cad1c7fdf2a4e942c3183a10f405/hebbia-smoked-depth-social.png?w=1600&h=900&fit=fill)
**Source:** https://openai.com/business/customer-stories/hebbia/ · **Karakeep:** `whd8qjexczmjlcccdguz0t6k`

**In short:** OpenAI's Hebbia case study sells GPT-6 Astra as better at citing sources and building PowerPoint slides; the numbers are tidy, but it is still vendor theatre.

**Key points:**
- OpenAI, 20 Nov 2026: Hebbia startup, North America, technology, API.
- GPT-6 Astra tested in Aug-Sep 2026 on financial research cases.
- 13.6 percentage points ahead of best alternative on required source types; 99.5% cited excerpts relevant.
- 97.9% of applicable presentation requirements met; 14.4 percentage points ahead of best alternative.
- Hebbia Matrix links answers to documents and turns research into PowerPoint slides.

**Details:** OpenAI has published another customer story, this time about Hebbia using GPT-6 Astra in financial research. The pitch is that Matrix can load a data room, answer questions with citations, and turn the work into PowerPoint slides in a firm's template. Hebbia says a prerelease build was tested in August and September 2026 on the same cases and grading criteria, with domain experts writing or auditing the criteria.

The headline numbers are the 13.6 percentage point lead on citing required source types, 99.5% relevant cited excerpts, 97.9% of presentation requirements met, and a 14.4 point lead on those requirements. Kavita Anand from Hebbia is quoted saying traceability matters because users base millions of dollars on the answers.

I would say it is a polished sales page, not a benchmark I can check. The future bit is agents watching in the background for signals, which is the usual promise. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 3. snooze - run commands at scheduled times - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2021/11/command-schedulers.png)
**Project:** [snooze](https://github.com/leahneukirchen/snooze)
**Source:** https://www.linuxlinks.com/snooze-run-commands-scheduled-times/ · **Karakeep:** `tg50n22os7hzuk86n20lp6jo`

**In short:** snooze is a small C scheduler that waits for a calendar time and then runs a command, with no central daemon. I would say it is a neat cron alternative for one-off or supervised tasks, but not a whole scheduling estate.

**Key points:**
- C command-line tool by Leah Neukirchen, licensed CC0 1.0 Universal
- Runs one command after a calendar match; no central scheduling daemon
- Patterns cover months, days, weekdays, ISO weeks, hours, minutes and seconds
- Dry-run shows next five execution times; verbose mode reports adjustments
- Handles jitter, slack, missed runs, clock changes, suspension and SIGALRM
- Integrates with service supervisors such as runit; avoids overlapping serial jobs

**Details:** snooze is Leah Neukirchen's small C utility, under CC0, that waits for a calendar time and then runs a command. It covers months, days, weekdays, ISO weeks, hours, minutes and seconds, with exact values, ranges, comma lists and repeats. All supplied conditions must match. There is dry-run for the next five times, verbose mode, jitter, slack, file-mtime tracking for minimum gaps, missed-run catch-up, clock-change handling and SIGALRM to run now. It has no central daemon, so recurring work needs runit or similar supervision, and serial supervision avoids overlaps. I would say it is a tidy cron alternative for people who want the schedule in the command itself, but it is not a drop-in for a whole estate. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 4. Omacom Foundation to sponsor Aurora Silicon - Omarchy News, by Omarchy
![](https://omarchy.org/brand/social/catppuccin-latte.png)
**Source:** https://omarchy.org/news/2026/11/omacom-foundation-to-sponsor-aurora-silicon · **Karakeep:** `isvo988ne8bsh7el63xaibqt`

**In short:** Omacom Foundation is sponsoring Aurora Silicon to bring Linux to Apple Silicon Macs for three months. I would say it is good upstream work, but nothing I can run on my own machines yet.

**Key points:**
- By DHH on 20 November 2026.
- Omacom Foundation sponsors Aurora Silicon, an independent open-source Linux on Apple Silicon project.
- Direct funding for two maintainers, Dj and Ryan Murray, for three months.
- Hardware and AI tokens for everyone working on Aurora.
- Omarchy 4.5 already installs on M1, M2, M3 and Neo MacBooks; Aurora works on the kernel, graphics drivers and boot chain.
- MacBook Neo has display, GPU acceleration, Vulkan 1.4, Touch ID, audio, camera, Wi-Fi and Bluetooth working.

**Details:** Omacom is funding Aurora Silicon so it can keep pushing Linux onto Apple's Macs. Aurora is independent, its maintainers set the direction, and Omarchy is the flagship distribution. The work sits under Omarchy's installer: kernel, graphics drivers and boot chain. They brought up the MacBook Neo on their own, with display, GPU acceleration, Vulkan 1.4, Touch ID, audio, camera, Wi-Fi and Bluetooth working. That is a lot of progress on a new machine.

The sponsorship is practical: hardware for the team, tokens for AI models, and three months of full-time pay for Dj and Ryan Murray, starting with M3 and M4. Aurora began from Asahi Linux's forks, and Fedora, Arch and NixOS setups are coming too. M4, M5 and M6 are in progress, and a Mac counts as done when it ships in an Omarchy release.

I would say it is worth supporting, but it is upstream work for me. Nothing for my projects this time.

**For my projects:** Nothing for my projects.

## 5. How Cloudflare WAF helps protect against phpAfterShell and other critical PHP flaws | Cloudflare Blog, by Cloudflare Blog
![](https://blog.cloudflare.com/_emdash/api/media/file/01M7X76FEMSF7NE7RCCQQBHCVN.png)
**Source:** https://blog.cloudflare.com/phpaftershell-waf-protection/ · **Karakeep:** `sgvy10air392oexqhgbe4nha`

**In short:** Cloudflare's WAF team describes managed rules that block known phpAfterShell patterns, plus extra rules on paid plans for PHP-FPM and SOAP flaws. I would say it is useful cover while patching, but the fix is still upgrading PHP.

**Key points:**
- Cloudflare WAF blocks known phpAfterShell attack patterns for every customer, including the Free plan.
- Paid plans get new rules for the PHP-FPM and SOAP flaws.
- phpAfterShell turns an interrupted file write in PHP's default session handler into a path to code execution.
- It arrived in the same release as six other critical flaws, so seven CVEs are in scope.
- Mitigations include disabling session.upload_progress, limiting untrusted session data, turning off FastCGI connection reuse, and keeping PHP-FPM listeners off untrusted networks.
- Those mitigations reduce exposure but do not fix the flaws; the advice is to upgrade PHP and restart the services that use it.

**Details:** The post is by Daniele Molteni on the Cloudflare Blog. It explains phpAfterShell plainly: an interrupted file write in PHP's default session handler can become a route to code execution. Cloudflare says technical details are now public, so exploit attempts are expected, and its WAF blocks known attack patterns for all customers, with extra rules for paid plans covering PHP-FPM and SOAP issues.

The practical part is the hardening list. Set session.upload_progress.enabled=0, keep untrusted session data small, turn off FastCGI connection reuse, set fatal_error_backtraces=0 on PHP 8.5, fix startup warnings or send PHP errors to syslog, and keep PHP-FPM listeners off untrusted networks. Cloudflare is clear that these steps reduce exposure and do not fix the flaws.

There is also a prompt for an AI agent to inventory PHP deployments and check them against all seven critical CVEs, linked from the phpAfterShell page. The closing advice is blunt: upgrade every PHP runtime and restart the services that use it. Nothing for my projects here; none of my repos are PHP runtimes, so this is just a patching reminder.

**For my projects:** Nothing for my projects.

## 6. How Cloudflare WAF protects against ruby2shell (CVE-2026-132825) | Cloudflare Blog, by Cloudflare Blog
![](https://blog.cloudflare.com/_emdash/api/media/file/01M7X91E3PVQ8147SJ7B05N2WK.png)
**Source:** https://blog.cloudflare.com/ruby2shell-waf-protection/ · **Karakeep:** `g9kzkjhjyt06qaxcq9ygu9fl`

**In short:** Cloudflare's WAF rules already block ruby2shell on Free plans, but the bug is pre-auth code execution in default Rails and Sinatra apps, so patching Ruby is the real fix. I would say treat the WAF as a stopgap.

**Key points:**
- CVE-2026-132825, called ruby2shell, turns string case conversion into pre-authentication code execution in default Rails and Sinatra apps.
- A public proof of concept is expected within days.
- On the Free plan, the ruby2shell WAF rules are already blocking; on paid plans, confirm the Cloudflare Managed Ruleset is deployed and not overridden.
- Upgrade to Ruby 3.3.14, 3.4.13 or 4.0.10, restart every Ruby process including background workers, and rebuild container images.
- Move applications on Ruby 3.2 or earlier to a supported series.
- Update self-hosted products that bundle Ruby, such as GitLab, GitHub Enterprise Server, Mastodon, OpenProject and Chatwoot, as fixes ship; rebuild Discourse Docker installs now.

**Details:** ruby2shell is not just a request-filtering problem. It is a bug in string case conversion that becomes code execution before authentication in default Rails and Sinatra apps, and a public proof of concept is expected within days. Cloudflare says its Free plan already blocks the ruby2shell rules, while paid plans need the Cloudflare Managed Ruleset deployed and not overridden. The WAF rule is a stopgap; patching Ruby is the fix.

The actual fix is boring and unavoidable: upgrade Ruby to 3.3.14, 3.4.13 or 4.0.10, restart every Ruby process including background workers, rebuild container images, and move anything still on Ruby 3.2 or earlier to a supported series. Self-hosted products that bundle Ruby also need updates as vendors ship them, with Discourse Docker installs needing a rebuild now. The Zero Wire briefing includes a prompt for an AI agent to inventory affected runtimes, and Cloudflare says its WAF analysts will keep updating protections, with changes tracked in the WAF changelog.

For my projects, nothing here is a fit. I do not run Ruby services in the homelab, and this is a patch-and-inventory job rather than something to build around.

**For my projects:** Nothing for my projects.

## 7. If you’ve deployed anything since 2015, I have bad news..., by Fireship
![](https://i.ytimg.com/vi/rMaMe32qQkA/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=rMaMe32qQkA · **Karakeep:** `h55wqij1qll0nteeeqnf36m3`

**In short:** Fireship covers three bugs that landed in one week: an Optimizely supply-chain hit on 178 sites, a Java 17+ base64 RCE, and a decade-old Nginx HTTP/2 flaw. I would say the Nginx one is the scary headline, but the 128GB single-connection requirement makes it less useful against anything behind a proxy.

**Key points:**
- Optimizely signup-flow bug let an attacker write JavaScript into other customers' projects; 178 websites including GitLab, Salesforce, Equifax and Ledger were affected.
- Payloads were rebuilt 26 times in about 10 hours; the reported take was about $7,500.
- Java bug called Java 4 Shell affects Java 17 and up on newer Intel or AMD chips using an AVX512 assembly base64 path; Khalif got unauthenticated RCE on Jira, Confluence, Jenkins and Keycloak.
- Nginx bug is in HTTP/2 flow control, has been around for over a decade, and Nginx powers more than 225 million websites.
- Public Nginx exploit needs 128GB over a single connection and is likely to fail behind a proxy.
- Zint paired the Nginx bug with a second Linux kernel bug to reach root on the whole machine.

**Details:** Bad news first: the Optimizely bug is the kind of supply-chain mess that makes marketing tooling everyone's problem. A signup-flow bug let an attacker write JavaScript into other customers' projects, and Optimizely served it from its own CDN, so 178 sites including GitLab, Salesforce, Equifax and Ledger got the payload. They rebuilt it 26 times in about 10 hours, which is efficient, but the haul was only about $7,500, which is not much. Then came Khalif's Java 4 Shell: Java 17 and up, on newer Intel or AMD chips, swaps in an AVX512 assembly base64 path with a math bug, and that got unauthenticated RCE on Jira, Confluence, Jenkins and Keycloak. The Nginx one is older and uglier: HTTP/2 flow control credit refunds are not checked against the two gigabyte cap, so the counter underflows, then overflows, and a negative length makes a copy run past a buffer. It has been around for over a decade across more than 225 million sites. Zint paired it with a Linux kernel bug to get root. The saving grace is the public exploit has to push 128GB down one connection, which will probably fail behind a proxy, so a Cloudflare-fronted side project is likely fine. What is still missing is any patch status or affected version list in the text, so this is a read-the-advisory job, not a checklist. Yeah, I would say the headline is worse than the practical risk for most homelabs.

**For my projects:**
- homelab-2nd: Check whether any public service reaches Nginx with HTTP/2 directly instead of through its Cloudflare Tunnel, and whether any workload runs Java 17 or newer on an internet-facing node; treat both as patch now items.

## 8. 16 Best Free and Open Source Python Data Validation - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2020/11/data-science-software.jpg)
**Source:** https://www.linuxlinks.com/best-free-open-source-python-data-validation/ · **Karakeep:** `u4kv51mb65pzyq7llytdkld0`

**In short:** LinuxLinks rounds up sixteen free and open source Python data validation tools, from Pydantic to Frictionless. I would say it is a useful map, and that is all.

**Key points:**
- LinuxLinks lists 16 free and open source Python data validation tools.
- Names include Pydantic, pandera, jsonschema, Cerberus, GX, schema, OpenMetadata, marshmallow, Elementary OSS, Voluptuous, msgspec, Colander, Valideer, Pointblank, Frictionless and check-jsonschema.
- The article says data validation checks format, type, range or consistency.
- Python was created by Guido van Rossum in 1991, per the page.
- It does not include versions, prices or benchmark results.

**Details:** It is a roundup, not a test, so it names tools rather than running them. I read about it, I did not try it. Sixteen tools, which that's a lot to read before picking one, but the descriptions are short and plain. Pydantic leans on type hints, pandera is for data testing, jsonschema and check-jsonschema cover JSON Schema, Cerberus and Voluptuous are lighter validators, GX and Elementary OSS sit nearer data observability, OpenMetadata is the metadata platform, marshmallow handles serialisation, msgspec is fast, schema and Colander and Valideer cover Python structures, Pointblank does quality checks, Frictionless handles tabular datasets. Unfortunately it does not give versions, benchmarks or a clear ranking, and it says all are free and open source without much else. I would say it is a useful map, and that is all. Nothing for my projects. This time I can call it a day.

**For my projects:** Nothing for my projects.

**Projects:**
- [Pydantic](https://docs.pydantic.dev/latest/): Pydantic Validation | Pydantic Docs.
- [pandera](https://github.com/unionai-oss/pandera): A light-weight, flexible, and expressive statistical data testing library - unionai-oss/pandera.
- [jsonschema](https://github.com/python-jsonschema/jsonschema): An implementation of the JSON Schema specification for Python - python-jsonschema/jsonschema.
- [Cerberus](https://github.com/pyeve/cerberus): Lightweight, extensible data validation library for Python - pyeve/cerberus.
- [GX](https://github.com/fivetran/great_expectations): Always know what to expect from your data. Contribute to fivetran/great_expectations development by creating an account on GitHub.
- [schema](https://github.com/keleshev/schema): Schema validation just got Pythonic. Contribute to keleshev/schema development by creating an account on GitHub.
- [OpenMetadata](https://github.com/open-metadata/openmetadata): The Open Context Layer for Data and AI , OpenMetadata is the open platform for building trusted data context and business semantics for humans, AI assistants, and agents. - open-metadata/OpenMetadata.
- [marshmallow](https://github.com/marshmallow-code/marshmallow): A lightweight library for converting complex objects to and from simple Python datatypes. - marshmallow-code/marshmallow.
- [Elementary OSS](https://element.io/): Matrix collaboration client
- [Voluptuous](https://github.com/alecthomas/voluptuous): CONTRIBUTIONS ONLY: Voluptuous, despite the name, is a Python data validation library. - alecthomas/voluptuous.
- [msgspec](https://github.com/msgspec/msgspec): A fast serialization and validation library, with builtin support for JSON, MessagePack, YAML, and TOML - msgspec/msgspec.
- [Pointblank](https://github.com/posit-dev/pointblank): Data validation toolkit for assessing and monitoring data quality. - posit-dev/pointblank.
- [Frictionless](https://github.com/frictionlessdata/frictionless-py): Data management framework for Python that provides functionality to describe, extract, validate, and transform tabular data - frictionlessdata/frictionless-py.
- [check-jsonschema](https://github.com/python-jsonschema/check-jsonschema): A CLI and set of pre-commit hooks for jsonschema validation with built-in support for GitHub Workflows, Renovate, Azure Pipelines, and more! - python-jsonschema/check-jsonschema.

## 9. Can AI help scientists identify promising drug candidates?, by link
![](https://images.ctfassets.net/kftzwdyauwt9/37ZvKdwVigsgJ7G3FMr4Nb/12854063a79d19d63278704bf54e3010/introducing-medchembench-social.png?w=1600&amp;h=900&amp;fit=fill)
**Source:** https://openai.com/index/introducing-medchembench/ · **Karakeep:** `ld5b6mn520qz12d4w1tpkoed`

**In short:** OpenAI's MedChemBench is a 99-problem medicinal-chemistry benchmark; the headline numbers look tidy, but the page itself says this does not show whether models can discover drugs or improve lab decisions. I would say it is a measurement exercise, not evidence.

**Key points:**
- OpenAI, published 20 November 2026; MedChemBench has 99 problems drawn from 117 papers and patents, with 761 distinct molecular structures.
- Four graded components: molecular structures, scientific reasoning, ranking and selection, property predictions.
- At xhigh: GPT-6.2 Astra 84.5%, GPT-6 Astra 83.3%, GPT-6.1 Sol 82.0%, GPT-5.6 Sol 58.2%.
- GPT-6 Astra got 95.4% of structure credit at xhigh but about half for selecting compounds and predicting numerical properties.
- GPT-6 Astra reached 83.8% at max effort; 11 models were evaluated across reasoning settings.
- The page says results do not establish whether models can discover new drugs or improve laboratory decisions; prior exposure cannot be ruled out and each response was one attempt without tools or feedback.

**Details:** OpenAI frames this as helping scientists develop better medicines, but the actual content is a benchmark over historical medicinal-chemistry tasks. One example is a PRMT5 inhibitor problem where the model gets structures and earlier results, predicts behaviour of three related compounds, and the withheld later experiments show the usual tradeoff: one compound blocks PRMT5 at lower concentration, another crosses the cell barrier more readily and breaks down more slowly. That is the interesting bit, because it is the actual medicinal-chemistry problem: improving one property can make another worse. The numbers are less exciting. Astra is strong at reading molecules and explaining evidence, then about half credit when it has to choose compounds and predict numbers. So yeah, the model can reconstruct an 18-atom ring, but that is not the same as picking a drug. The caveat is the honest part: no tools, no feedback, no new experiments, and prior exposure to the sources cannot be ruled out. I would treat the score as a ceiling on reading comprehension, not a promise about the lab.

**For my projects:** Nothing for my projects.

## 10. Combatting adversarial distillation, by link
![](https://images.ctfassets.net/kftzwdyauwt9/5SUtPGdssrttC7LfP1yoJ1/b6b000846ab3576c1735c29534ab20b0/combatting-adversarial-distillation-social.png?w=1600&amp;h=900&amp;fit=fill)
**Source:** https://openai.com/index/combatting-adversarial-distillation/ · **Karakeep:** `pgc1c9dkgr9gh5a3dznuyrrw`

**In short:** OpenAI argues that unauthorised distillation can copy frontier capabilities without the original safeguards, and it is now making protected reasoning traces much harder to extract. I would say the trace-extraction number is the interesting part, while the rest is OpenAI framing its own controls.

**Key points:**
- Published by OpenAI on 20 November 2026.
- Adversarial distillation means using a frontier model's outputs without authorisation to train another model with similar capabilities.
- The focus is protected reasoning, the chain-of-thought, because traces can contain information the final answer leaves out.
- GPT-6.2 Astra and GPT-6.2 Sol received strengthened defenses against protected reasoning extraction.
- An internal adaptive red-team test cut average attack success from 54.0% on GPT-6 Astra to 0.2% on GPT-6.2 Astra.
- An internal cyber study used ExploitBench and SEC-bench Pro; exact-trace students generally beat summary-trained students after supervised fine-tuning.

**Details:** OpenAI says distillation is ordinary machine learning, but unauthorised distillation is a safety problem because a second model can pick up frontier skills without the original safeguards. The post puts the spotlight on protected reasoning traces, the chain-of-thought, because those traces can carry information the final answer leaves out. In its internal study, a student trained on exact traces generally beat one trained on reasoning summaries after supervised fine-tuning, and still scored higher at the largest inference budget after reinforcement learning on ExploitBench and SEC-bench Pro. The headline safeguard number is the drop in average attack success from 54.0% to 0.2% for protected reasoning extraction. I would say the trace result is the interesting bit, and the rest is a familiar safety story about keeping the valuable intermediate steps behind request and campaign controls. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 11. BambooTracker - Yamaha YM2608 music tracker - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2021/12/Music-Trackers.png)
**Project:** [BambooTracker](https://github.com/BambooTracker/BambooTracker)
**Source:** https://www.linuxlinks.com/bambootracker-yamaha-ym2608-music-tracker/ · **Karakeep:** `utwu3vm3suvs1t5vip418fgb`

**In short:** BambooTracker is a free GPL v2.0 tracker for the Yamaha YM2608 OPNA chip, written in C++ and running on Linux, macOS and Windows. I would say it is niche but quite good job for PC-98 style chiptune work, and nothing for my projects.

**Key points:**
- Targets the Yamaha YM2608 (OPNA) chip used in NEC PC-8801 and PC-9801 machines.
- Edits FM, SSG, rhythm and ADPCM channels, with detailed FM operator and envelope control.
- Uses BTM songs, BTI instruments and WOPN banks; audio and MIDI go through RtAudio and RtMidi.
- Optional support for compatible real OPNA hardware; five interface translations including English, Japanese, French, Polish and Spanish.
- Licensed GPL v2.0, written in C++, with cross platform support.

**Details:** Unfortunately it is tied to one chip, so it is not a general music tool. It is a traditional tracker with patterns of notes, instruments, volume and effects, and multiple patterns can be arranged into a full song. Effects include pitch slides, vibrato, arpeggios and rhythm controls, and there is optional support for communicating with compatible real OPNA hardware. I read about it, I did not try it, so the verdict is just that it looks dedicated and specific rather than general purpose. It is free and open source, but it is a chip music tool, so nothing for my projects. So yeah, that's that.

**For my projects:** Nothing for my projects.

## 12. Advancing Science Together: Highlights From the Open Source AI For Science Summit, by Meta Newsroom
![](https://about.fb.com/wp-content/uploads/2026/11/Highlights-From-the-Open-Source-AI-For-Science-Summit_Social-Share-1.jpg?w=1200)
**Source:** https://about.fb.com/news/2026/11/advancing-science-together-highlights-from-the-open-source-ai-for-science-summit/ · **Karakeep:** `ulttcyw3nlslq61aaybd19ad`

**In short:** Meta's write-up of its Open Source AI for Science Summit, covering brain data, assistive robotics and UMA chemistry tools; I would say it is worth skimming for the model names, not for the event.

**Key points:**
- Meta's FAIR team hosted the Open Source AI for Science Summit at Menlo Park for researchers from universities, hospitals and industry.
- The Digital Brain Project target rose from 15,000 to 25,000 hours of de-identified brain data, with the Rothschild Hospital Foundation and the University of Montreal.
- The University of Pittsburgh showed an assistive-robotics system built on DINOv3 and SAM 3, with plans for a robot that can help a person eat.
- UMA Nitro is a faster version of Meta's Universal Model for Atoms; UMA models identified many crystal forms of drug molecules in a Carnegie Mellon and UC Riverside study.
- UMA Playground is available to high school chemistry teachers through Discovery Education, which reaches more than 4 million educators and 45 million students.

**Details:** I read this one rather than running anything, so treat it as a report. Unfortunately it is a Meta event write-up, so the useful detail sits between the marketing: the Digital Brain Project is moving from 15,000 to 25,000 hours of de-identified brain data, the University of Pittsburgh is building assistive robotics on DINOv3 and SAM 3, and UMA Nitro is a faster version of Meta's Universal Model for Atoms. UMA Playground is the part that sounds practical, with Discovery Education putting it in front of more than 4 million educators and 45 million students. The chemistry examples are concrete too, since UMA identified many crystal forms of drug molecules in a study with Carnegie Mellon and UC Riverside, and the University of Chicago work simulates whole enzymes atom by atom. Nothing for my projects. I would say it is worth skimming for UMA Nitro and the assistive robotics note, and skipping the rest.

**For my projects:** Nothing for my projects.

## 13. OpenAI is Cooked, by The PrimeTime
![](https://i.ytimg.com/vi/pAGwvAWV4bk/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=pAGwvAWV4bk · **Karakeep:** `v37tbfoh7rxjunt58jaj4uam`

**In short:** The PrimeTime argues the universal hate for OpenAI's Astra 6.2 and Soul 6.2 is echo-chamber noise, backed by his own Soul 6.2 run that built a full app in 45 minutes from one prompt. My read: the computer use sounds genuinely good, but one creator's demo is not a benchmark.

**Key points:**
- Astra 6.2 and Soul 6.2 are OpenAI's latest, both rated worse by Artificial Index on release day
- Every influencer reportedly hated them; the creator calls it a universal pile-on
- Creator ran Soul 6.2 on ultra fast: one prompt, 45 minutes, app with Twitch, Kick, Google and X auth, Cloudflare deploy, WorkOS gating, OBS embedded Chrome
- Computer use described as out of this world; $200 subscription, roughly 60 hours of fast-mode use possible
- Creator has 20+ years programming and argues adaptability beats model rankings
- Gemini cited as a model line that went from bad to possibly best in months

**Details:** The PrimeTime's latest is a rant about how fast people form opinions about new models. OpenAI shipped Astra 6.2 and Soul 6.2, every influencer on earth called them horse crap on the same day, and Artificial Index showed both scoring lower than before. His counter is that nobody actually tested them against their own work. He then shows his own test: one prompt to Soul 6.2 on ultra fast, and 45 minutes later he had an app wired into Twitch, Kick, Google and X, deployed on Cloudflare, gated behind WorkOS, and working inside OBS's embedded Chrome. He did not read the code. The computer use, he says, is out of this world, and on a $200 plan he reckons 60 hours of fast-mode use would not break the subscription.

The wider point is that model rankings swing wildly month to month, Gemini being his example of a line that went from forgettable to possibly the best. His conclusion is that adaptability and actually trying things beats parroting 280-character takes. I would say that is fair as far as it goes, but it is still one anecdote from a creator who clearly likes OpenAI, and one good demo does not tell me whether 6.2 is stable for boring work. Nothing for my projects, I am not paying $200 a month to find out.

**For my projects:** Nothing for my projects.
