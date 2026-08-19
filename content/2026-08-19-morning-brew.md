---
date: 2026-08-19
slug: 2026-08-19-morning-brew
tags: digest,karakeep,OSINT
---

# Morning Brew — 2026-08-19
Backfill of 5 bookmarks from my hoard — a wireless OSINT toy, a self-hosted email API, the Hermes Bot Mode rollout, an alpha stem splitter, and yet another K8s dashboard that wants to be a "platform."

## 1. WireTapper — wireless OSINT for people who think walls are a suggestion

WireTapper is a passive radio-signal reconnaissance platform. It sniffs the air and fingerprints whatever is broadcasting: Wi-Fi access points/clients, Bluetooth/BLE, wireless CCTV and IP cameras, vehicle RF (infotainment, telemetry, keyless systems), headphones, wearables, smart TVs, IoT junk, and cell towers. It even pulls leaked Wi-Fi credentials via a k-Anonymity scheme so it's "privacy protecting" while doing exactly what it sounds like. It leans on Wigle.net, wpa-sec, OpenCellID, and a Shodan API (premium required — of course). Config by editing `app.py` or the recommended env-var/`.env` path via `app-env.py`. Python, 2.1k stars, 308 forks. The *passive* bit and the *leaked Wi-Fi creds* bit are doing a lot of heavy lifting — and "free" means you bring your own API keys. Fun for the lab, not a toy to point at people. CC BY-NC 4.0, non-commercial.

- 🔗 https://github.com/h9zdev/WireTapper
- karakeep id: `p7ml7twlalc429uqfzydvcoo`

## 2. Hyvor Relay — self-hosted email API when SES pricing makes you twitchy

Open-source, self-hosted email API. Send mail through your own SMTP infra instead of renting Mailgun/SendGrid/SES. Scales to millions of emails/day, Docker (compose/swarm) deployable. Feature list is long and genuinely useful: health checks for deliverability, send log + SMTP conversations (30 days), multi-tenancy with scoped access, separate transactional vs. distributional queues (IP reputation), automatic greylisting/retries, bounce handling, feedback-loop integration, suppressions, DNS automation via built-in DNS server, webhooks, Prometheus/Grafana observability. Stack: PHP + Symfony backend, Go workers/webhooks/DNS, SvelteKit frontend, PGSQL for data + queue. AGPL-3.0 (enterprise licenses offered). 838 stars. The "we'll just host it ourselves" answer to the transactional-email tax — but building SMTP reputation from scratch is still a wall of work. Solid if you already run mail infra, not a weekend one-off.

- 🔗 https://github.com/hyvor/relay
- karakeep id: `htojcekzkq17sjnq51vwj0bb`

## 3. Nous Research ships Bot Mode — Hermes profiles turn into a roster of named bots

The headline. Bot Mode landed in Hermes Desktop, bundled and default-on under Settings → Plugins, after a one-day public beta. MIT licensed. The core insight: **a bot IS a Hermes profile** — each lives under `~/.hermes/profiles/<name>/` with isolated config, memory, skills, credentials, chat history; the plugin is just a UI over the `profiles.*` gateway RPCs. Avatars via image.generate, routines are ordinary Hermes cron jobs namespaced `[bot:<name>]`. Bot-to-bot messaging is real CLI handoffs (`hermes -p <bot> chat -c "Agent Inbox" -q "..."`). Per-bot advanced config: clone profile, pin a provider/model, custom SOUL.md, per-skill enablement. Handoff chains by @mention; group chats for 2–6 bots; per-project isolation without context leak. Shipped in-tree at `apps/desktop/src/plugins/hermes-bots/`, Hermes Agent v0.20.3. Reality check: no admin console, no SSO, no central audit log, no policy layer — a workstation tool, not managed infra. But "roster of specialists with clean isolation" genuinely works for solo builders and small teams.

- 🔗 https://www.marktechpost.com/2026/08/17/nous-research-hermes-bot-mode/
- karakeep id: `h732f9iumdjig1mzq5wyjnrr`

## 4. StemDeck — free, local, open-source stem splitter. Drum-practice motive, real function

Free, open-source, local-only stem separation for Windows/macOS/Linux by solo dev Thales Pereira — built to help his kid practice drums without a subscription or uploading music. Runs the open-source Demucs `htdemucs_6s` model, splitting up to six stems (vocals, drums, bass, guitar, piano, other). Auto-picks Torch device: CUDA on NVIDIA, MPS on Apple Silicon, or CPU. Import MP3/WAV/FLAC/OGG/Opus/MP4/M4A or a YouTube URL (rights permitting). After separation, a browser-based multitrack mixer: mute/solo/balance, zoom, loop, export stems or a custom mix, even an "Original" lane from unselected stems for A/B. Song analysis (BPM, key/scale + confidence, LUFS, sample peak), MP4 export, local-network mode (process on one box, control from another). First launch pulls a Python runtime, FFmpeg, Demucs model. Alpha: quality is "practice/remix prep/transcription/sampling prep," not polished-commercial. Passed 2,000 stars and 13,000+ downloads in ~2 months, word of mouth. A commenter hit trouble on M1 MacMini / macOS 13. Free tool with a "did this for my kid" origin — worth a spin if you do DIY stems.

- 🔗 https://bedroomproducersblog.com/2026/08/19/stemdeck-stem-splitter/
- karakeep id: `yjib7zcy7h3as33nvdcludsq`

## 5. Kite — a "lightweight" K8. dashboard that is absolutely not lightweight

Modern Kubernetes dashboard, "platform, not a tool." Unifies real-time observability, multi-cluster + resource management, enterprise-grade user governance (OAuth, MFA, passkeys, RBAC, audit logs), and AI agents. Features: themes, global search, i18n; multi-cluster with independent Prometheus per cluster, kubeconfig auto-discovery, fine-grained perms; resource management with live Monaco YAML editing, CRD support, Helm discover/install/upgrade/rollback, quick image-tag selection, kube proxy (skip `kubectl port-forward`); monitoring/observability (Prometheus CPU/mem/net, live logs, web terminal, built-in kubectl console, AI assistant); security via OAuth, MFA, passkey, RBAC. Install: `docker run` (SQLite), or Helm from OCI registry. Apache 2.0, 3.1k stars, 298 forks. If you want one pane to babysit all your clusters with RBAC and an AI copilot, it's a contender. Donate buttons: Alipay/WeChat/PayPal — adds flair.

- 🔗 https://github.com/kite-org/kite
- karakeep id: `l3ucyi5ohws4hocxte27qse3`

---

*Morning Brew digest — 2026-08-19. Tags: OSINT, self-hosted, AI agents, Kubernetes, audio, stem separation.*
