---
date: 2026-08-29
slug: 2026-08-29-morning-brew
tags: 3D Modeling,3D graphics,AI Agents,AI Engineering,AI Orchestration,Agent Orchestration,Agentic Engineering,Artificial Intelligence,Bare Metal,Blender,C++,Calendar and Tasks,Claude,Cloud Computing,Coding Strategy,Containerization,Cryptography,DevOps,Docker,GNOME,GTK+,GUI,Game Development,GitOps,GnuPG,Graphics,Graphics Design,Helm Chart,Inference Engine,JavaScript,Kubernetes,Large Language Models,Link Page,Linux Software,Machine Learning,Mixture of Experts,Model Fusion,Model Stacking,Monitoring,Multi-Agent Systems,Next.js,Node.js,Observability,Open Source AI,Open Source Software,OpenPGP,PBR,PIM,Personal Information Manager,Planning,Productivity,Productivity Software,Programming,Python,Scalability,Security,Self-Hosted,Software Development,Software Engineering,Software Testing,Texture Painting,Tokenomics,Web Development,add-on,encryption,machine learning,monitoring,test automation,texture painting
---

# Morning Brew — 2026-08-29

A 20-item hoard from Saturday, August 29th: 13 YouTube videos (all transcribed) and 7 articles (4 LinuxLinks tool reviews, 2 GitHub repos, 1 Homarr Helm doc). The thread of the day is unmistakably **agentic engineering** — IndyDevDan alone dropped 12 videos on multi-agent orchestration, software factories, model fusion, agent sandboxes, and the (banned-then-unbanned) Fable 5 / Mythos-class models — plus a slab of self-hosted tooling (link-in-bio server, Homarr on k8s, a bare-metal k8s dashboard) and a few Linux desktop utilities.

## 1. This Open Source Tool Makes AI Models 3x Faster (FreeToken) — by Better Stack

![Better Stack](https://i.ytimg.com/vi/8n4Uo47CadY/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=8n4Uo47CadY
**Karakeep doc:** `sjp1z4zl5b1jejajb2mhq599`

⚠️ **Transcript empty** — Parakeet returned nothing for this one (likely a music/voice-over-heavy short the English-only model couldn't latch onto). Title + tags say it's about **FreeToken**, an open-source inference engine that claims ~3x speedup on AI models via Mixture-of-Experts routing. Can't verify the substance from audio; treat as a flagged-for-revisit item. Link + doc id kept so it can be re-checked.

## 2. TestCafe — Node.js framework — by linuxlinks.com

![linuxlinks.com](https://www.linuxlinks.com/wp-content/uploads/2020/08/software-development-testing.png)

**Source:** https://www.linuxlinks.com/testcafe-node-js-framework/
**Karakeep doc:** `yipz9ab6bjwkti8ghyyh5ldu`

LinuxLinks' directory entry for **TestCafe**, DevExpress's end-to-end web-testing framework for Node.js. Tests written in JS or TypeScript run across local, remote, mobile, headless, and cloud-hosted browsers — and crucially, **no Selenium WebDriver required**. It auto-waits for page loads and XHRs, waits for elements before acting/asserting, restarts tests on code change in live mode, detects JS errors on the tested page, and runs tests concurrently across browser instances. High-level API with selectors/actions/assertions, Page Object support, CLI + CI integration, and plugin extensibility (browser providers, selectors, reporters). MIT-licensed. Verdict: a solid, dependency-light alternative to Selenium for JS/TS shops that want browser automation without the WebDriver ceremony.

## 3. Ucupaint — layer-based texture painting for Blender — by linuxlinks.com

![linuxlinks.com](https://www.linuxlinks.com/wp-content/uploads/2020/09/3d-render-light-bulbs.jpg)

**Source:** https://www.linuxlinks.com/ucupaint-layer-based-texture-painting-blender/
**Karakeep doc:** `y1sq259x0nwq6ym31u8uj75p`

LinuxLinks on **Ucupaint**, a Blender add-on (by Yusuf Umar, GPLv3) that brings a **layer-based texture-painting workflow** to Eevee and Cycles materials. Instead of hand-assembling a sprawling shader-node tree, artists get a focused panel in the 3D View or Node Editor managing material channels, layers, groups, masks, and modifiers. It combines image/colour/vertex-colour/procedural sources in an ordered layer stack, with per-layer opacity, blend modes, and non-destructive modifiers (colour, value, normal). Handles bump, tangent-space normal, displacement, and vector-displacement painting; supports UDIMs and image atlases; bakes complete channels (plus curvature/thickness/wireframe) into final images. Data stays inside the Blender project and plays nice with normal painting/shading/sculpting/baking. Notably broad version coverage — current releases plus legacy packages back to 2.76–2.79. Verdict: the go-to if you want Photoshop-style layer painting inside Blender without fighting node spaghetti.

## 4. LXQt Organizer — lightweight personal information manager — by linuxlinks.com

![linuxlinks.com](https://www.linuxlinks.com/wp-content/uploads/2019/04/PIM-Software.jpg)

**Source:** https://www.linuxlinks.com/lxqt-organizer-lightweight-personal-information-manager/
**Karakeep doc:** `yp2pb9hx02bocb8jeab2fvut`

LinuxLinks on **LXQt Organizer**, a lightweight Qt 6 PIM maintained by the LXQt project (usable standalone, no LXQt desktop needed). Built around **local storage** of personal info: it already ships Vdir calendar and address-book storage plus iCalendar (.ics) parsing/serialization, with atomic writes, ETags, and file locking in the storage layer. Still under active development — a broader calendar/task/contact/reminder/import-export feature set is planned. GPLv2. Verdict: early days, but a promising privacy-first, local-only PIM for the LXQt crowd; watch it if you want your calendar/contacts off the cloud without a heavyweight Kontact/Evolution install.

## 5. Keysign — OpenPGP key signing helper — by linuxlinks.com

![linuxlinks.com](https://www.linuxlinks.com/wp-content/uploads/2021/03/encrypted-files.jpg)

**Source:** https://www.linuxlinks.com/keysign-openpgp-key-signing-helper/
**Karakeep doc:** `hqyaqr6v2x8dudnqfcejdywu`

LinuxLinks on **Keysign** (GNOME-Keysign, by Tobias Mueller, GPLv3), a GTK 4 / Libadwaita front-end for GnuPG that makes **in-person OpenPGP key signing** less painful. Two people meeting to verify each other's identity: instead of pulling a key from a public keyserver, Keysign grabs an authenticated copy directly from the other participant over the local network (Avahi discovery) or Bluetooth. A QR code carries a message-authentication code confirming the transfer; the fingerprint can be entered manually if camera scanning isn't suitable. After you check the identities, it certifies each user ID separately, encrypts the certifications for their intended recipients, and opens your configured email client with a prepared message + attachment — no SMTP credentials stored in the app. Verdict: a clean, keyserver-free way to do real key-signing parties; the QR-MAC + manual-fingerprint combo is a nice touch for authenticity.

## 6. littlelink-server — self-hosted Linktree alternative — by GitHub

![GitHub](https://opengraph.githubassets.com/bc94e74a685b8e8debd33725d3715098cf6179e31c7dcac1041c0590961369a8/timothystewart6/littlelink-server)

**Source:** https://github.com/timothystewart6/littlelink-server
**Karakeep doc:** `rqlo5wv4rksz2b3vt6tzfr6f`

**littlelink-server** (1.1k stars, MIT) is a lightweight, self-hosted link-in-bio page — a Linktree alternative in a Docker container. Built with Next.js/React/TypeScript; the image uses Next.js standalone output so the runtime stays small. Everything (profile, avatar, social links, custom buttons, metadata, analytics, health checks) is configured via **environment variables**, evaluated at request time — change an env var, restart the container, no rebuild. Ships a docker-compose and an unofficial k8s-at-home Helm chart. Verdict: dead-simple self-hosted "link page" for homelabbers who want their own links.technotim.com-style page without a SaaS.

## 7. Homarr on Kubernetes (Helm) — by Homarr

![Homarr](https://homarr.dev/favicon.ico)

**Source:** https://homarr.dev/docs/getting-started/installation/helm
**Karakeep doc:** `cl2jy4lh7w6envoipi368acc`

Homarr's official Helm chart docs for deploying the dashboard on Kubernetes (chart v8.28.1, app v1.76.1, no dependencies, k8s >= 1.24). Install via OCI (`helm install homarr oci://ghcr.io/homarr-labs/charts/homarr`) or the classic repo. Covers the DB options (better-sqlite3 on pod disk or PVC, or external MySQL/Postgres), the required `db-encryption` secret, optional OIDC/LDAP secrets, Ingress (traefik example) and the newer **HTTPRoute / Gateway API** path, plus trusted-certificate persistence via ConfigMap or Secret. Verdict: a clean, current reference if you're running Homarr on k8s — the Gateway API section is the forward-looking bit.

## 8. k8s-baremetal-dashboard — production bare-metal k8s + GitOps — by GitHub

![GitHub](https://opengraph.githubassets.com/c35da4910a403abf706b31d43242355dc1a1d015284fec779bd5bdaa40aa59af/catdevops1/k8s-baremetal-dashboard)

**Source:** https://github.com/catdevops1/k8s-baremetal-dashboard
**Karakeep doc:** `d3r43rnwdosbk6w3sngtnqto`

**k8s-baremetal-dashboard** (by Catalin Bot) is a production-grade 5-node bare-metal Kubernetes cluster (v1.35, 1 control-plane + 4 workers, Ubuntu 24.04, containerd, 343+ days uptime) with real-time monitoring and GitOps, fully documented as a repo. Stack: Flannel CNI, MetalLB (L2), Envoy Gateway (Gateway API), Cloudflare Tunnel for external access, cert-manager + Let's Encrypt, Longhorn storage, HashiCorp Vault with AWS KMS auto-unseal, External Secrets Operator, ArgoCD auto-sync, and Netdata (parent-child streaming) for monitoring. The showcase site (catdevops.net) renders live cluster metrics via a sidecar architecture — Netdata children per node, an Nginx reverse proxy, a Python kubectl sidecar for cluster-level data, and frontend JS polling every 5s. Notably **zero secrets in git**: Vault → ESO → k8s Secrets, with an init-container pattern injecting the Netdata streaming key and `upgrade-netdata.sh` pulling real values fresh from Vault at deploy time. Verdict: a great reference architecture for a homelab bare-metal k8s cluster with serious observability and secret hygiene.

## 9. Claude Fable 5 BANNED: The First Model Agentic Engineers DON'T NEED — by IndyDevDan

![IndyDevDan](https://i.ytimg.com/vi/D1BHGv4gB6c/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=D1BHGv4gB6c
**Karakeep doc:** `y7d3otbyivqwmtal9n0z18al`

IndyDevDan's take on the **Fable 5 / Mythos 5** chaos — the model was pulled by a federal export-control order (a government-found jailbreak) after Anthropic already rug-pulled it from subscription plans, and Anthropic claims the same jailbreak techniques work on GPT-5.5 too. Dan sidesteps the mania and gives three observations for agentic engineers. **(1) It's price-per-intelligent-agent-hour, not price-per-token.** In his 15-sandbox benchmark (Fable orchestrating itself + Opus + Sonnet on the same 5 specs), Fable spent ~$200 of tokens vs Opus $91 and Sonnet $55 — it loses on tokens but finishes ~20% faster. The value is *time*: on ~80% of tasks the cheaper siblings did the job fine; Fable only pays off on genuinely hard, complex missions. "If you're centering a div, you're making a donation to Anthropic." **(2) Fable is an orchestrator, not an intern.** Treat it like a principal engineer that delegates — give it a big spec and let it spin up fleets of agents. Anthropic's own system card shows multi-agent orchestration scaling accuracy with agent count. **(3) It's the first model you might not need.** Opus 4.8 is close enough on most work that ~80% of engineers don't need Fable — if you can't write 100+ line specs, Opus is enough. Verdict: a genuinely useful "when to pay for the frontier model" framework — buy agent-hours, not tokens, and only for work complex enough to justify it.

## 10. FORGET Loop Engineering. Agentic Engineering is about THIS — by IndyDevDan

![IndyDevDan](https://i.ytimg.com/vi/VQy50fuxI34/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=VQy50fuxI34
**Karakeep doc:** `vsvwzze9nife9mfaw2s5flz0`

Dan dismantles **"loop engineering"** (the Boris/Peter framing) as a hype-filled rebrand of the software development life cycle. His reframe: there are **three actors of value creation** — engineers, agents, and code — and the name of the game is building **AI developer workflows** (ADWs), not loops. Code is the unsung hero: fast, deterministic, costs nothing. The pattern: engineer prompts → agent builds → deterministic code (linter, formatter, type-check, tests) validates → condition routes back to the build agent → engineer reviews at the end. You show up at the two constraints — planning (prompting) and reviewing (validation) — and let the middle run. He scales it up: worktrees → per-agent sandboxes → kanban/ticket systems → a full software factory with scout/plan/build/test agents, CI/CD, and even a **hot-fix workflow** for production crashes (specialized surgical agent, human approval gate, parallel sandboxes racing to a fix). The thesis: "build the system that builds the system" — the agentic layer, not the app layer, is where the best teams do meta-work. Verdict: a solid mental model that reframes the loop-engineering hype into something concrete — engineers + agents + code composed into repeatable workflows.

## 11. Pi to Pi: Two-Way Agent Orchestration with the Pi Coding Agent — by IndyDevDan

![IndyDevDan](https://i.ytimg.com/vi/PIdETjcXNIk/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=PIdETjcXNIk
**Karakeep doc:** `vmg41xu7wn2gtyedrj3v33tc`

Dan demonstrates **peer-to-peer, two-way agent-to-agent communication** with the Pi coding agent — a flat hierarchy where agents are equals, not orchestrator/worker. The demo: a production DB on his Mac Mini has a bug locking Pro-tier users out; a "Prod Gatekeeper" agent on the production machine and a "dev" agent on his MacBook talk across the network to reproduce the issue locally — with **PII redacted** on the production side before anything crosses. The dev agent sends a message, gets a message ID, awaits the reply; the production agent works with all redactions applied. He contrasts this with subagent delegation (one-way, top-down), message-queue brokers (Claude Code Agent Teams), and agent chains (deterministic, still one-directional) — all of which travel information one way. Peer-to-peer unlocks bidirectional flow and flat information hierarchies, where the best ideas win over titles/politics (Nvidia's flat structure as the analogy). Second demo: using two agents to build a feature-parity skill for **exe.dev** (a new agent-sandbox tool) mirroring his existing E2B skill — the E2B agent answers questions while the exe.dev agent drives, keeping focused context windows (a focused agent is a performant agent). Verdict: a compelling case for bidirectional agent communication as a distinct pattern from delegation — especially for cross-device, security-sensitive workflows.

## 12. I Ranked Cloudflare's Software Factory and Wow… S TIER TOKENOMICS — by IndyDevDan

![IndyDevDan](https://i.ytimg.com/vi/YG4t7aMY81c/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=YG4t7aMY81c
**Karakeep doc:** `tjq6l4y8w4usu86vd9z1ma06`

Dan's first **agentic-engineering tier list**, ranking Cloudflare's AI code-review software factory. The headline stat: **130,000 AI code reviews across 5,000 codebases at ~$1 per merge request** — S-tier tokenomics (use tokens → generate value → arbitrage). The problem they solved: code review is a bottleneck (median first-review wait measured in hours). Their approach: a **CI-native orchestration system** built on **OpenCode** (open-source, has a real SDK for programmatic sessions) that launches up to **7 specialized reviewer agents** (security, performance, code quality, docs, release management, compliance) managed by a **coordinator/orchestrator** that dedupes findings and posts one structured comment. Key engineering choices Dan grades: a **composable plugin architecture** (bootstrap/configure/post-configure hooks) for extensibility; **JSONL** output (always-valid, streamable, real-time observability via step-finish events, retry logic on max-token cutoffs); **shared context** so each sub-reviewer only reads its domain's patch (avoids 7x token multiplication); a **tiered model stack** (state-of-the-art / workhorse / lightweight) instead of Opus-for-everything; and prompt engineering that tells agents both *what to look for* and *what to ignore* (don't nitpick syntax). Verdict: a genuinely instructive teardown of how a big org does code review at scale — the $1/MR tokenomics and the "what to ignore" prompt technique are the standout takeaways.

## 13. SEE CMUX SOLVE Multi-Agent Orchestration (Claude Code and Pi Agent) — by IndyDevDan

![IndyDevDan](https://i.ytimg.com/vi/WAFUMBLOjHo/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=WAFUMBLOjHo
**Karakeep doc:** `s0438pi1lfhj657hm1h2i0mx`

Dan evaluates **CMUX** (a terminal multiplexer) against three multi-agent orchestration problems. **(1) No programmatic access to your agents** — CMUX (like TMUX) gives agentic access to every terminal, so you can send keys, read the screen, and open/close surfaces programmatically. "An agent you can't see is an agent you can't improve" — the core difference between vibe-coding and agentic engineering. **(2) Monitor to improve** — per-workspace colors, roles, icons, tabs, banners let you jump into any agent (Claude Code, Codex, Pi agents) and see what it's doing. **(3) Quick agentic launch** — reusable session files + agentic access mean you can boot a team of agents at agentic speed, not by hand. He walks the CMUX mental model (window → workspace → pane) and shows an orchestration agent pushing/pulling events from the CMUX lifecycle. Verdict: a practical look at why terminal multiplexers are the connective tissue for multi-agent orchestration — visibility and programmatic control beat black-box subagent prompting.

## 14. PLANS For Fable 5: Rebuilding My /Plan Skill for Mythos Class Models — by IndyDevDan

![IndyDevDan](https://i.ytimg.com/vi/DzbqeO_diOQ/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=DzbqeO_diOQ
**Karakeep doc:** `o3znicryvdq3gc91p7vuwkh9`

A slow, in-depth devlog where Dan rebuilds his **/plan meta-skill** ("Plan F3" = Plans for Fable 5) from scratch for the new Mythos-class models. His core argument: **great planning is great engineering** — most engineers hand planning off to the model, which is a mistake because it assumes the model knows what you want. He starts by writing a `raw.md` by hand (not via an agent) to think through the design — the more you'll reuse a skill, the more upfront investment it deserves. The skill is a **meta-skill** (a prompt that creates another prompt/skill): purpose, variables (user prompt), output, instructions, workflow, and the critical **plan format** that changes results across every execution. He frames it around the two constraints of agentic engineering — planning and reviewing — and the trade-off trifecta (performance > speed ≈ cost), deliberately sacrificing speed/cost for optimal performance with state-of-the-art models. Verdict: a thoughtful case for owning your planning prompt rather than outsourcing it — the "property-based engineering" and "write it by hand first" bits are the practical takeaways.

## 15. Top #1 Opportunity for Senior Engineers: Agentic Engineering — by IndyDevDan

![IndyDevDan](https://i.ytimg.com/vi/2KcITKKJikA/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=2KcITKKJikA
**Karakeep doc:** `lpnp5utzkdyople9ju9nf70l`

A raw, message-to-self video after two weeks unplugged in Greece. Dan's answer to "what's the greatest opportunity for senior engineers?" is unchanged — **agentic engineering** — but the window is closing: Karpathy just called it out at Sequoia AI Ascent, and by end of 2026 it'll be the default. He lays out **five pillars** that separate low- from high-performing agentic engineers: **(1) Agent harness** — whoever controls the harness controls your results; he builds a new custom harness every day (Pi coding agent lets you compose skills/agents/commands into a net-new harness; "one tool, many versions"). **(2) Software factory** — build factories, not features, for on-spec results every time. **(3) Extensible software** — systems that adapt. **(4) Always-on agents** — agents that run out-of-loop while you're AFK. **(5) Agentic access** — programmatic control so you move at agentic speed. Verdict: a motivational-but-substantive framing of where senior engineers should focus — the harness-ownership point is the sharpest.

## 16. Engineers… STOP Picking GPT-5.6 Sol OR Claude Fable 5… FUSE THEM — by IndyDevDan

![IndyDevDan](https://i.ytimg.com/vi/AQl5Q-0l7FQ/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=AQl5Q-0l7FQ
**Karakeep doc:** `j2fix0etfhylhfttndv2axvb`

Dan argues the winning mindset is **"and" not "or"** — combine compute, don't select it. The pattern (yesterday: architect/editor, prompt chaining, agent chaining; today: **model fusion**) combines the intelligence and context windows of multiple models. He builds a **fusion harness** with the Pi coding agent and three commands: `/opinion` (get multiple perspectives from agents in parallel), `/fusion` (combine/consolidate the best results), and `/auto-validate` (write a validation gate *before* the work starts). Demo: two workhorse models (Claude Sonnet 5, GPT-5.6 Terra) answer "top 3 scikit-learn models" — Terra did it in 4.5s/9k tokens/3¢ vs Sonnet's double time and ~1¢ more; the fusion agent then shows where they agreed (consensus), diverged (complementary), and what was discarded. The `/auto-validate` bit is the standout: the validator writes a raw validation script with fail-commands *before* the builder starts, then runs it against the work — fighting the reviewing constraint by proving work is done upfront. Verdict: a concrete, reusable pattern for combining models instead of picking one — the pre-written validation gate is the genuinely clever idea.

## 17. GLM-5.2 vs MiniMax-M3: Opus Has REAL COMPETITION (Model Stacking) — by IndyDevDan

![IndyDevDan](https://i.ytimg.com/vi/cFYdiynrxpQ/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=cFYdiynrxpQ
**Karakeep doc:** `id44stfx0vxccyx52h12u191`

Dan's engineering-first take on the open-weights landscape: **GLM-5.2 is the leading open-weights model, MiniMax-M3 right behind**, and Opus finally has real competition. Headline: **GLM wins on performance, MiniMax wins on price** — the only question is whether you need max capability or can optimize for cost. He dehypes the "GLM replaces Opus" chatter: they're competitive on performance and cost but won't beat Opus. Key insight on speed: GLM-5.2 is fast but **thinks a lot** — most of its tokens are reasoning (more than Opus in Max mode, way more than MiniMax), so raw tokens/sec doesn't matter; wall-clock response time does. He frames everything through his **three-tier model stack** (state-of-the-art / workhorse / lightweight) and the resiliency angle — open-weights models can't be killed by a lab or government, which matters when you want true ownership over your AI. Verdict: a useful, hype-free comparison — GLM for capability, MiniMax for price, and the "reasoning tokens ≠ speed" caveat is the insight worth remembering.

## 18. Pi Coding Agent Observability: HTML Specs with Gemini 3.5 Flash and GPT Image 2 — by IndyDevDan

![IndyDevDan](https://i.ytimg.com/vi/o4KZH_KSqYQ/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=o4KZH_KSqYQ
**Karakeep doc:** `a2u0n16zocmx5t8dybg6a0am`

Dan tests **three spec types** (markdown, HTML, enhanced HTML) with three Gemini 3.5 Flash Pi agents, using a **Pi observability dashboard** to measure the trade-off triangle (performance/speed/cost) with identical prompts. The answer: "more *useful* tokens outperform fewer useful tokens" — but you can't know which spec is better without measuring. The observability dashboard streams every event/turn/tool call, so he can see the markdown agent used 29 turns vs HTML's 17 — and that the markdown agent may have just understood the codebase better. He also showcases a **product-focused agent** (a "Steelman" agent that argues the *bear* case against your thesis — here, against Apple as an AI-distribution winner, with 40 references and generative UI components). The Apple analysis is sharp: the Claude-on-Mac-Mini trend proves developers want decentralized local open-source AI, but Mac Mini is <2% of Apple's revenue and a one-time purchase — not the repeat revenue Apple wants. Verdict: a good argument for agent observability as a prerequisite for improving prompts — and the Steelman product-agent pattern is a genuinely useful idea.

## 19. Engineers… Your Software Factory NEEDS Agent Sandboxes to SCALE (exe.dev) — by IndyDevDan

![IndyDevDan](https://i.ytimg.com/vi/SEI_qIW4o2c/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=SEI_qIW4o2c
**Karakeep doc:** `tsdkz4apxxqnh6ub5g04s3qd`

Dan argues your software factory should run **inside an agent sandbox**, not a corner of your own computer or a CI container. Agent sandboxes give three advantages: **true isolation, insane scale, and agency** — "if you're inside the loop, you're the bottleneck." He walks a "best-of-both" architecture: a top-level orchestrator (Claude Code Fable) outside the sandboxes, with the factory itself (using Pi as the agent SDK) placed inside **exe.dev** sandboxes. He runs **five agent configurations** (default, frontier, DeepSeek, open-weights, top-speed) each in its own sandbox, all solving the same problem through a full software-development lifecycle — not just launching agents, but building the factory and placing it in the box. The DeepSeek V4 Flash 0731 model gets a shout-out as "absurd for its price." Verdict: a strong case for sandboxes as the deployment target for agentic systems — isolation + scale + autonomy is the unlock, and "if you're still fixated on models, you're behind" is the punchline.

## 20. My Super Simple Software Factory (For Agentic Engineers) — by IndyDevDan

![IndyDevDan](https://i.ytimg.com/vi/haUfb1ievTE/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=haUfb1ievTE
**Karakeep doc:** `i7zb565hshba3pcdgued5imr`

Dan's **"super simple software factory"** — the core insight: software factories exist for one reason, **more leverage on your prompt**. Three design principles: **observable, customizable, reusable**. It's a system of agents + code (the three actors: engineer, code, agents) where you can click into any AI developer workflow and see a swim-lane view of every event, compiled prompt, tool, and harness config. He runs it with a Pi coding agent on Opus 5, kicking off a scout workflow (Gemini 3.6 Flash as a cheap workhorse) that lazily loads skills and reports results. The point: you're not debating which model is best anymore — you're using the right model at the right cost/speed/performance point from your **model stack**, and the factory is how you orchestrate that. Verdict: a clean, minimal reference implementation of the software-factory idea — observability-first, and "agents + code beats agents alone" is the thesis.
