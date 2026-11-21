---
date: 2026-11-20
slug: 2026-11-20-morning-brew
tags: GNAT Studio, SPARK, Formal Verification, Integrated Development Environment, Ada, Financial Research, Presentation Generation, Hebbia, GPT-6 Astra, AI Citations, Linux, Snooze, Job Scheduling, Cron Alternative
---

Morning Brew for 2026-11-20: 13 items written from 13 hoarded bookmarks and feeds, 0 dropped after a failed retry.

### RSS

## 1. GNAT Studio - IDE for Ada and SPARK development - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2020/01/IDE-Vector.jpg)
**Source:** https://www.linuxlinks.com/gnat-studio-ide-ada-spark-development/ · **Karakeep:** `s2iu7j4704681lw83uekok75`

**In short:** GNAT Studio is AdaCore's IDE for Ada and SPARK, with C and C++ on the side, and I would say it is not worth it for my projects.

**Key points:**
- IDE for Ada and SPARK, with extra support for C and C++
- Built by AdaCore; free and open source under GNU GPL v3.0
- Runs on Linux and Windows
- Language Server Protocol, debugger, refactoring, SPARK analysis, GNATcoverage and static analysis integration
- Plugin system with configurable layouts, themes, shortcuts and perspectives

**Details:** GNAT Studio is AdaCore's IDE for Ada and SPARK, with C and C++ as extras. It brings editing, project files, builds, debugging and analysis into one graphical tool, and it integrates with the GNAT compiler. The feature list is long: LSP completion and diagnostics, navigation, refactoring, breakpoints that survive sessions, dependency and call views, SPARK correctness checks, GNATcoverage, static analysis, compiler fixes where available, version control, plugins and themes. It is GPL v3 and runs on Linux and Windows, so it is easy to try on my Linux box.

For me this is a specialist tool for a language family I do not use. It is clearly aimed at reliability and verification work, and the SPARK side is the interesting part, but it does not connect to my homelab, image pipeline or factory. Yeah, it is a lot of IDE for a language I do not touch. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 2. Hebbia sees improvements in financial research with GPT-6 Astra, by OpenAI
![](https://images.ctfassets.net/kftzwdyauwt9/70gWqYyqb096it9EoD7OqI/5df8cad1c7fdf2a4e942c3183a10f405/hebbia-smoked-depth-social.png?w=1600&h=900&fit=fill)
**Source:** https://openai.com/business/customer-stories/hebbia/ · **Karakeep:** `whd8qjexczmjlcccdguz0t6k`

**In short:** OpenAI's customer story says Hebbia tested a prerelease GPT-6 Astra on financial research and got better source citation and deck-building scores than the best alternative. I would say it is a sales page with one useful number, not something I can run.

**Key points:**
- Hebbia is a startup; its Matrix links research answers to source documents.
- Hebbia tested a prerelease GPT-6 Astra in August-September 2026 on the same financial research cases and grading criteria.
- GPT-6 Astra scored 13.6 percentage points above the best alternative tested on citing required source types.
- 99.5% of the excerpts it cited were relevant to the question.
- It met 97.9% of applicable presentation requirements, 14.4 percentage points ahead of the best alternative tested.
- The example workflow covers roughly 2,000 files, cited cells, peer filings and news, then native PowerPoint slides in the firm template.

**Details:** Unfortunately this is OpenAI selling GPT-6 Astra through a customer, so the useful part is the test setup, not the praise. Hebbia's Matrix is meant to pull financial research together and link answers back to documents. In their August-September 2026 tests, a prerelease build of GPT-6 Astra scored 13.6 percentage points above the best alternative tested on citing required source types, with 99.5% of cited excerpts relevant, and met 97.9% of applicable presentation requirements, 14.4 points ahead on that measure. The example is a banker reviewing roughly 2,000 files, checking customer concentration and contract terms in cited cells, then getting a diligence summary and valuation deck in the firm's template. Kavita Anand says traceability matters because users base large decisions on the output, and that GPT-6 Astra is the first model they saw rank first on both craft and instruction following. There is also talk of background agents surfacing signals before competitors. I read about it, I did not run it, so I can only note the numbers and the vendor framing. Nothing for my projects, since it is API-only finance tooling with no Kubernetes path, backup story or metrics I can check.

**For my projects:** Nothing for my projects.

## 3. snooze - run commands at scheduled times - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2021/11/command-schedulers.png)
**Source:** https://www.linuxlinks.com/snooze-run-commands-scheduled-times/ · **Karakeep:** `tg50n22os7hzuk86n20lp6jo`

**In short:** snooze is a small C command-line scheduler by Leah Neukirchen that waits for a calendar time and then runs a command. I would say it is a neat cron alternative; nothing for my projects.

**Key points:**
- Command-line utility by Leah Neukirchen; waits until a specified time, then executes a command
- Calendar patterns for months, days, weekdays, ISO weeks, hours, minutes and seconds; exact values, ranges, comma-separated alternatives and repeating intervals
- No central scheduling daemon; direct one-off use or with a supervisor such as runit; propagates the executed command's exit status
- Dry-run shows the next five scheduled execution times; verbose mode; randomised delays, jitter and configurable slack periods
- Uses file modification timestamps for minimum intervals; accounts for missed runs after restarts; adjusts for clock changes and suspension
- CC0 1.0 Universal Public Domain; written in C; website github.com/leahneukirchen/snooze

**Details:** snooze is a command-line utility by Leah Neukirchen that waits until a specified time before running a command. It uses calendar patterns for months, days, weekdays, ISO weeks, hours, minutes and seconds, with exact values, ranges, comma-separated alternatives and repeating intervals. It has no central daemon, can be invoked directly for one-off tasks or combined with a supervisor such as runit for recurring jobs, and propagates the executed command's exit status. Features include dry-run showing the next five times, verbose mode, randomised delays and jitter, configurable slack, file modification timestamps for minimum intervals, accounting for missed runs after restarts, clock change adjustments, suspension recalculation, SIGALRM immediate execution and avoiding overlapping executions in serially supervised jobs. It is free and open source under CC0 1.0 Universal and written in C. I would say it is a neat cron alternative for people who want one task per supervisor. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 4. Omacom Foundation to sponsor Aurora Silicon - Omarchy News, by Omarchy
![](https://omarchy.org/brand/social/catppuccin-latte.png)
**Source:** https://omarchy.org/news/2026/11/omacom-foundation-to-sponsor-aurora-silicon · **Karakeep:** `isvo988ne8bsh7el63xaibqt`

**In short:** The Omacom Foundation is sponsoring Aurora Silicon, the independent open-source project bringing Linux to Apple Silicon Macs, with hardware, tokens and three months of full-time pay for two maintainers. I would say it is real upstream work, but it does not touch anything I run.

**Key points:**
- Sponsor: the Omacom Foundation, backing Aurora Silicon, an independent open-source Linux-on-Apple-Silicon project.
- Support: hardware and AI tokens for everyone working on Aurora, plus direct funding for Dj and Ryan Murray for three months.
- Omarchy 4.5 shipped a native installer for M1, M2, M3 and Neo MacBooks.
- Aurora independently brought up the MacBook Neo with display, GPU acceleration, Vulkan 1.4, Touch ID, audio, camera, Wi-Fi and Bluetooth.
- Aurora's bootloader, kernel and installer trees began as forks of Asahi Linux work.
- Fedora, Arch and NixOS setups are coming; M4, M5 and M6 are being worked on now.

**Details:** Omacom is paying for the layer under Omarchy: the kernel, graphics drivers and boot chain that get Linux onto Apple Silicon. Aurora is independent, with its own maintainers and repositories, and Omarchy is its flagship distribution. That is the part I like. The funding is concrete too: Macs for testing, tokens for AI models, and three months of full-time work for Dj and Ryan Murray, starting with M3 and M4.

The progress is also concrete. Omarchy 4.5 already installs alongside macOS on M1, M2, M3 and Neo MacBooks, and Aurora independently brought up the MacBook Neo with display, GPU acceleration, Vulkan 1.4, Touch ID, audio, camera, Wi-Fi and Bluetooth. Asahi Linux did the original reverse engineering. I would say this is worth funding, but I have no Apple Silicon Mac in my homelab, so there is no fit for my projects.

**For my projects:** Nothing for my projects.

## 5. How Cloudflare WAF helps protect against phpAfterShell and other critical PHP flaws | Cloudflare Blog, by Cloudflare Blog
![](https://blog.cloudflare.com/_emdash/api/media/file/01M7X76FEMSF7NE7RCCQQBHCVN.png)
**Source:** https://blog.cloudflare.com/phpaftershell-waf-protection/ · **Karakeep:** `sgvy10air392oexqhgbe4nha`

**In short:** Cloudflare says its WAF now blocks known phpAfterShell patterns for all plans, with extra rules on paid plans, but the real fix is still upgrading PHP. I would say it is a useful patch checklist, not a substitute for updates.

**Key points:**
- Cloudflare WAF blocks known phpAfterShell attack patterns for every customer, including the Free plan.
- Paid plans get new rules for the PHP-FPM and SOAP flaws.
- phpAfterShell turns an interrupted file write in PHP's default session handler into code execution.
- It arrived in the same release as six other critical flaws, so seven critical CVEs in total.
- Mitigations include disabling session upload progress, turning off FastCGI connection reuse, and keeping PHP-FPM listeners off untrusted networks; they reduce exposure but do not fix the flaws.
- On PHP 8.5, set fatal_error_backtraces=0; the post is by Daniele Molteni on the Cloudflare Blog.

**Details:** I read this Cloudflare post rather than testing anything. It explains phpAfterShell: an interrupted file write in PHP's default session handler can lead to code execution, and it shipped alongside six other critical flaws. Cloudflare says its WAF blocks known attack patterns for all customers, including Free, while paid plans get extra rules for PHP-FPM and SOAP issues. The practical advice is still to update every PHP runtime and restart the services using it. The hardening steps are useful but partial: disable session upload progress, limit untrusted session data, turn off FastCGI connection reuse, set fatal_error_backtraces=0 on PHP 8.5, send PHP errors to syslog or fix startup warnings, and keep PHP-FPM listeners off untrusted networks. Cloudflare also points to a Zero Wire page with a prompt for an AI agent to inventory PHP deployments against all seven CVEs. So yeah, WAF is a bandage; patching is the fix.

**For my projects:** Nothing for my projects.

## 6. How Cloudflare WAF protects against ruby2shell (CVE-2026-132825) | Cloudflare Blog, by Cloudflare Blog
![](https://blog.cloudflare.com/_emdash/api/media/file/01M7X91E3PVQ8147SJ7B05N2WK.png)
**Source:** https://blog.cloudflare.com/ruby2shell-waf-protection/ · **Karakeep:** `g9kzkjhjyt06qaxcq9ygu9fl`

**In short:** Cloudflare's WAF post covers ruby2shell (CVE-2026-132825), a Ruby flaw that can turn string case conversion into pre-authentication code execution in default Rails and Sinatra apps. I would say the managed rules help, but the patch window looks short and Ruby still needs upgrading.

**Key points:**
- CVE-2026-132825 is described as an injection in string case conversion leading to pre-authentication code execution in default Rails and Sinatra apps.
- Cloudflare says a public proof of concept is expected within days.
- Free plan users already get blocking ruby2shell rules; paid plans must confirm the Cloudflare Managed Ruleset is deployed and not overridden.
- Patched Ruby versions are 3.3.14, 3.4.13 and 4.0.10, with every Ruby process restarted and container images rebuilt.
- Applications on Ruby 3.2 or earlier need moving to a supported series.
- Self-hosted products bundling Ruby named in the post include GitLab, GitHub Enterprise Server, Mastodon, OpenProject, Chatwoot and Discourse Docker installs.

**Details:** The bad news is plain: this is a pre-authentication code execution bug in default Rails and Sinatra apps, and a public proof of concept is expected within days. Cloudflare's side is that WAF rules are already blocking on Free plans, while paid plans need to check that the Cloudflare Managed Ruleset is actually deployed and that nobody has overridden the rules. The fix side is Ruby 3.3.14, 3.4.13 or 4.0.10, plus restarting every Ruby process including background workers and rebuilding container images. Older Ruby 3.2 or earlier apps need moving to a supported series. Self-hosted products that bundle Ruby are also in scope, with GitLab, GitHub Enterprise Server, Mastodon, OpenProject, Chatwoot and Discourse Docker installs named. Cloudflare also points to a Zero Wire briefing prompt for finding affected runtimes with an AI agent, and says analysts will keep updating protections as new techniques appear. I would say the WAF help is useful, but it is not a substitute for patching. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 7. If you’ve deployed anything since 2015, I have bad news..., by Fireship
![](https://i.ytimg.com/vi/rMaMe32qQkA/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=rMaMe32qQkA · **Karakeep:** `h55wqij1qll0nteeeqnf36m3`

**In short:** Fireship's Code Report rounds up three nasty bugs from one week: an Optimizely supply-chain hit on 178 sites, a Java base64 RCE on Java 17+, and an Nginx HTTP/2 flow-control RCE that has sat there since 2015. I would say it is a good scare video and a weak patch plan.

**Key points:**
- Optimizely signup bug let an attacker write JavaScript into other customers' projects; 178 sites, including GitLab, Salesforce, Equifax and Ledger, served malware from Optimizely's CDN.
- Payload rebuilt 26 times in about 10 hours; older iPhones could be hit by a zero-click exploit chain of six vulnerabilities.
- Hackers reportedly walked away with about $7,500.
- Java 4 Shell affects Java 17+ on newer Intel or AMD chips; bad AVX512 base64 decoding writes 62 bytes past the buffer and gave RCE on Jira, Confluence, Jenkins and Keycloak.
- Nginx bug is in HTTP/2 flow control; Nginx powers more than 225 million websites and the bug has been around for over a decade.
- Public Nginx exploit sends 128 GB over one connection; Zint paired it with a Linux kernel bug for root.

**Details:** I read the transcript, and it is a fast tour of three separate messes. Monday was Optimizely: a signup bug let someone write their own JavaScript into other customers' projects, and Optimizely served it from their own CDN. GitLab, Salesforce, Equifax, Ledger and 174 others were affected, and the payload skimmed cards, stole crypto, texted X, and on older iPhones chained six vulnerabilities for a zero-click takeover. The attackers rebuilt it 26 times in about 10 hours, which is a lot, but crypto being crypto they only made about $7,500.

Tuesday was Java. On Java 17 and up, on newer Intel or AMD server chips, the JVM uses a handwritten AVX512 base64 routine that writes 62 bytes past the buffer on a short malformed string. Khalif says that got RCE without logging in on Jira, Confluence, Jenkins and Keycloak. Wednesday was Nginx, where HTTP/2 flow control credit can be pushed past the two gigabyte cap because cancelled requests are refunded without the check, then an unsigned integer underflows and a negative length turns into a buffer overflow. Zint found it and paired it with a Linux kernel bug for root. The public exploit has to push 128 GB over one connection, so a side project behind Cloudflare is probably fine. Yeah, that is the bit to remember.

**For my projects:** Nothing for my projects.

## 8. 16 Best Free and Open Source Python Data Validation - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2020/11/data-science-software.jpg)
**Source:** https://www.linuxlinks.com/best-free-open-source-python-data-validation/ · **Karakeep:** `u4kv51mb65pzyq7llytdkld0`

**In short:** LinuxLinks lists sixteen free and open source Python data validation tools, from Pydantic to check-jsonschema. I would say it is a skim list, not a comparison.

**Key points:**
- LinuxLinks, dated 20 November 2026, covers 16 free and open source Python data validation tools.
- The named tools include Pydantic, pandera, jsonschema, Cerberus, GX, schema, OpenMetadata, marshmallow, Elementary OSS, Voluptuous, msgspec, Colander, Valideer and Pointblank.
- The descriptions are one line each, such as Pydantic using Python type hints and msgspec doing fast serialisation and structured validation.
- All software is described as free and open source; the article gives no versions, prices, benchmarks or detailed licence notes.
- The page also carries the usual LinuxLinks extras, including a Minisforum Black Friday advert and a long archive list.

**Details:** LinuxLinks has put together a list of sixteen free and open source Python data validation tools. It covers the obvious names, Pydantic and pandera, plus jsonschema, Cerberus, GX, schema, OpenMetadata, marshmallow, Elementary OSS, Voluptuous, msgspec, Colander, Valideer, Pointblank, Frictionless and check-jsonschema. The descriptions are one line each, so you can scan it, but you will not learn much beyond what each tool claims to do. I would say it is useful as a starting list. It does not compare them properly. There are no versions, no install notes, no benchmark, and no licence detail beyond free and open source. The page is also padded with ads and archive links, which is a bummer. So yeah, skim the names, then go to the project pages.

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
- [Colander](https://github.com/Pylons/colander): A serialization/deserialization/validation library for strings, mappings and lists. - Pylons/colander.
- [Valideer](https://github.com/podio/valideer): Lightweight data validation and adaptation Python library. - podio/valideer.
- [Pointblank](https://github.com/posit-dev/pointblank): Data validation toolkit for assessing and monitoring data quality. - posit-dev/pointblank.

## 9. Can AI help scientists identify promising drug candidates?, by link
![](https://images.ctfassets.net/kftzwdyauwt9/37ZvKdwVigsgJ7G3FMr4Nb/12854063a79d19d63278704bf54e3010/introducing-medchembench-social.png?w=1600&amp;h=900&amp;fit=fill)
**Source:** https://openai.com/index/introducing-medchembench/ · **Karakeep:** `ld5b6mn520qz12d4w1tpkoed`

**In short:** OpenAI's MedChemBench is a 99-problem medicinal-chemistry benchmark for its own GPT models; I would say it is mostly benchmark marketing, with strong structure reading and weak compound selection.

**Key points:**
- OpenAI introduced MedChemBench, a benchmark of 99 problems drawn from 117 papers and patents, with 761 distinct molecular structures.
- It grades four components: molecular structures, scientific reasoning, ranking and selection, and property predictions.
- At xhigh, GPT-6.2 Astra scored 84.5%, GPT-6 Astra 83.3%, GPT-6.1 Sol 82.0%, and GPT-5.6 Sol 58.2%.
- GPT-6 Astra earned 95.4% of structure credit at xhigh, but only about half for selection and numerical prediction.
- OpenAI says the results do not establish whether models can discover new drugs, and prior exposure to published sources cannot be ruled out.

**Details:** OpenAI introduced MedChemBench on 20 November 2026. It tests whether models can connect a molecule's structure with experimental evidence, explain results, compare compounds and predict properties. The hard part is the tradeoff: improving one property can make another worse. The benchmark has 99 problems and, for most, gives the model the target, goals, compounds studied so far and selected findings.

The numbers are tidy for OpenAI. At xhigh, GPT-6.2 Astra got 84.5%, GPT-6 Astra 83.3%, GPT-6.1 Sol 82.0% and GPT-5.6 Sol 58.2%. Astra was best at reconstructing structures, at 95.4%, but selection and numerical prediction were only about half. That is the useful bit: the model can read the molecule, then struggles to choose what to test next.

Unfortunately, it does not show a drug being found. OpenAI admits prior exposure to the sources cannot be ruled out and each answer was one attempt without tools or feedback. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 10. Combatting adversarial distillation, by link
![](https://images.ctfassets.net/kftzwdyauwt9/5SUtPGdssrttC7LfP1yoJ1/b6b000846ab3576c1735c29534ab20b0/combatting-adversarial-distillation-social.png?w=1600&amp;h=900&amp;fit=fill)
**Source:** https://openai.com/index/combatting-adversarial-distillation/ · **Karakeep:** `pgc1c9dkgr9gh5a3dznuyrrw`

**In short:** OpenAI's 20 November 2026 post says adversarial distillation can copy frontier cyber capability into a model with weaker safeguards, and that GPT-6.2 Astra's protected-reasoning extraction rate fell from 54.0% to 0.2%. I would say it is a safety announcement, not something I can run.

**Key points:**
- OpenAI published it on 20 November 2026 and frames unauthorised distillation as a safety risk, not only an IP issue.
- The concern is that a student model learns cyber or biology capability without inheriting the teacher model's safeguards.
- GPT-6.2 Astra and GPT-6.2 Sol received stronger defences against protected-reasoning extraction.
- Internal adaptive red-teaming put attack success at 54.0% for GPT-6 Astra and 0.2% for GPT-6.2 Astra.
- An internal cyber study found students trained on exact reasoning traces outperformed summary-trained students after supervised fine-tuning.
- Defences include request-level model behaviour, classifier checks and API controls, plus campaign-level investigation and disruption.

**Details:** OpenAI's post is about stopping people from copying a frontier model's capabilities into a weaker-safeguarded model. The part I find concrete is the cyber study: a student trained on exact reasoning traces beat the one trained on reasoning summaries after supervised fine-tuning, and still scored higher at the largest inference budget after reinforcement learning. That is awkward, because it says the hidden chain-of-thought is the valuable training data, so protecting it is the point.

The headline number is the red-team result: 54.0% attack success on GPT-6 Astra down to 0.2% on GPT-6.2 Astra. That is a big drop, but it is OpenAI's own internal adaptive evaluation, and the article keeps the operational details private while saying it shares with government channels. So I would treat the number as a claim, not proof.

For my setup, this is mostly a policy page. It does not give me a tool, a model I can run, or a gate I can add to a repo. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 11. BambooTracker - Yamaha YM2608 music tracker - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2021/12/Music-Trackers.png)
**Project:** [BambooTracker](https://github.com/BambooTracker/BambooTracker)
**Source:** https://www.linuxlinks.com/bambootracker-yamaha-ym2608-music-tracker/ · **Karakeep:** `utwu3vm3suvs1t5vip418fgb`

**In short:** BambooTracker is a free C++ music tracker built around the Yamaha YM2608 chip used in PC-88 and PC-98 machines, with detailed FM instrument editing and pattern-based composition. It looks like a serious chiptune tool, but it has no place in any of my current projects.

**Key points:**
- Free and open source under GPL v2.0, written in C++ by the BambooTracker contributors.
- Targets the Yamaha YM2608 (OPNA) chip used in NEC PC-8801 and PC-9801 computers.
- Supports FM synthesis, SSG, rhythm channels and ADPCM playback.
- Includes an FM instrument editor plus BTM modules, BTI instruments and WOPN instrument and bank formats.
- Cross-platform on Linux, macOS and Windows, with English, Japanese, French, Polish and Spanish translations.
- Optional support for communicating with compatible real OPNA hardware through supported interfaces.

**Details:** I read about it on LinuxLinks, I did not try it. It is a tracker in the old sense: patterns hold notes, instrument changes and effect commands, then multiple patterns become a full piece. The draw is that it is built around the YM2608, so the focus is chip-specific sounds rather than general sample playback, with operator and envelope control for FM instruments, SSG, rhythm and ADPCM in one place. Audio and MIDI go through RtAudio and RtMidi, and it can optionally speak to real OPNA hardware. That is a lot of chip-specific depth for a free GPL v2 tool. For me, though, it is a music niche with no link to riffradar, the homelab or the factory. Nothing for my projects. I would say it is interesting if you make PC-98 style chiptune, not worth chasing for anything I run.

**For my projects:** Nothing for my projects.

## 12. Advancing Science Together: Highlights From the Open Source AI For Science Summit, by Meta Newsroom
![](https://about.fb.com/wp-content/uploads/2026/11/Highlights-From-the-Open-Source-AI-For-Science-Summit_Social-Share-1.jpg?w=1200)
**Source:** https://about.fb.com/news/2026/11/advancing-science-together-highlights-from-the-open-source-ai-for-science-summit/ · **Karakeep:** `ulttcyw3nlslq61aaybd19ad`

**In short:** Meta's Fundamental AI Research team ran a two-day open source AI for science summit in Menlo Park, with brain data, assistive robotics, chemistry models and classroom tools. It is interesting science, but nothing I can plug into my own stack.

**Key points:**
- FAIR hosted researchers from universities, hospitals and industry at Meta's Menlo Park headquarters over two days.
- The Digital Brain Project target rose from 15,000 to 25,000 hours of de-identified brain data.
- The University of Pittsburgh demoed assistive robotics built on DINOv3 and SAM 3, including a robot that can help a person eat.
- UMA Nitro, a faster Universal Model for Atoms, was released; UMA models identified many crystal forms of drug molecules without extra training data.
- UMA can simulate entire enzymes atom by atom, and UMA Playground is now available to high school chemistry teachers via Discovery Education.
- Discovery Education reaches more than 4 million educators and 45 million students; RealChem is used by nearly 100 institutions.

**Details:** Meta's Fundamental AI Research team brought researchers from universities, hospitals and industry to Menlo Park for a two-day Open Source AI for Science Summit. The pitch is open models, tools and data for healthcare, neuroscience, chemistry, materials science and maths. The concrete bits are better: the Digital Brain Project now targets 25,000 hours of de-identified brain data, up from 15,000; Pittsburgh showed assistive robotics on DINOv3 and SAM 3, including a robot that can help a person eat; and UMA Nitro, a faster Universal Model for Atoms, was released. In a Carnegie Mellon and UC Riverside study, UMA models identified many crystal forms of drug molecules without extra training data, and with the University of Chicago it simulated entire enzymes atom by atom. The same chemistry stack reaches classrooms: UMA Playground is available to high school chemistry teachers through Discovery Education, which reaches more than 4 million educators and 45 million students, while RealChem is used by nearly 100 institutions. I did not try any of it. It is a science showcase, and I would say it is interesting but I have no concrete use for it yet.

**For my projects:** Nothing for my projects.

## 13. OpenAI is Cooked, by The PrimeTime
![](https://i.ytimg.com/vi/pAGwvAWV4bk/maxresdefault.jpg)
**Source:** https://www.youtube.com/watch?v=pAGwvAWV4bk · **Karakeep:** `v37tbfoh7rxjunt58jaj4uam`

**In short:** A rant about the backlash to OpenAI's Astra 6.2 and Soul 6.2, with one demo of a 45-minute app build and a plea to test models yourself. I would say it is more useful as a reminder about taste than as a review.

**Key points:**
- The PrimeTime argues the universal backlash to Astra 6.2 and Soul 6.2 is overblown and cites Artificial Index showing 6.2 performing worse on both.
- In the video's demo, Soul on ultra fast built a multi-service app in 45 minutes from one prompt, with computer use described as very good.
- It claims a $200 subscription could run about 60 hours of that fast computer use, and that the run used little of the allowance.
- It compares the backlash to Gemini's many versions and says models are good at different things.
- It also includes a WorkOS/AuthKit sponsor segment and a personal story about adapting from PlayStation 3 JavaScript to Groovy and Objective C.

**Details:** Unfortunately the video is mostly a rant about influencers and Twitter pile-ons, with the actual model talk arriving late. The useful bit is the demo: one prompt to Soul on ultra fast, then 45 minutes later a Twitch, Kick, Google, X and Cloudflare app with local tests and a WorkOS email gate, plus OBS and embedded Chrome checks. The computer use is praised, and the cost is described as low for a $200 subscription with roughly 60 hours of fast use. The broader point is that benchmarks and 280-character opinions are not your domain, and the video leans hard on adaptability: computing is only 70 to 80 years old, and the speaker says they have programmed for over 20 years. I would say the demo is the only part worth keeping, and the rest is a reminder to test things yourself. Yeah, that is the whole video. Nothing for my projects.

**For my projects:** Nothing for my projects.
