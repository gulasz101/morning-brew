# Inventory

Everything I actually have running, opened or half built. The six project paragraphs above say
what each lane is for. This file is the raw material: repos, boards and services a spark can
start from. Use the real names. Never invent a repo, a service or a board that is not here.

## Paperclip boards (12, 9 in progress)

- Homelab: homelab-2nd k3s and Flux GitOps, OMV storage, observability, security.
- Star Office UI: the pixel-art agent dashboard fork plus its reporters (pi, openchamber, hermes,
  claude-code).
- Blog: gulasz101.github.io, posts grown from the homelab tracking notes.
- Personal Brand: job search for EM and Tech Lead roles in Warsaw, CV, cover letters, LinkedIn.
- Agent Fleet: Hermes profiles, the gateway, crons and digests, Paperclip itself.
- Image Studio: blog and personal-brand images with Ideogram 4 and FLUX.2-klein, review loop in
  Paperclip.
- Code Factory: the Pi code factory, stage agents in a dedicated checkout (ADR-093).
- Factory Canary: scratch board proving the factory write paths per stage agent.
- Morning Brew: this digest, one Karakeep day per post.
- Riff Radar: RiffRadar v2, a music guessing game in a Bun workspace (apps/api, apps/web,
  apps/admin, packages).
- OpenPharaoh Web: Pharaoh (1999) in the browser, Rust and WebAssembly, from the owner's own GOG
  files.
- Osiris Web: Pharaoh plus Cleopatra in the browser, porting the Osiris engine to wasm32.

## GitHub: things I built or run (public unless marked private)

- homelab-2nd: the GitOps repo behind the cluster.
- morning-brew: this pipeline, fetch, transcribe, one writer call per item, marmite site.
- star-office-ui-fork: The Lodge, an agent-agnostic pixel-art dashboard.
- pi-star-office-reporter, openchamber-star-office-reporter, hermes-star-office-reporter,
  claude-code-star-office-reporter: the four plugins that feed it.
- paperclip: the agent work board (fork of the upstream app).
- osiris: open-source Rust engine for Sierra's Pharaoh (1999).
- OpenPharaoh: an older C# implementation of the Pharaoh, Caesar 3 and Zeus engine.
- ideogram4-local: local Ideogram 4 image generator for Apple Silicon.
- DeChord: real-time chord and key recognition from audio files (TypeScript).
- zwhisper: Linux PipeWire recorder with tray control, profiles and transcription (Rust).
- honcho: a memory library for stateful agents (Python).
- arr-stack: the media stack as code.
- riff_radar (private): the v1 riff practice tool.
- setlistrs (Rust), trackrs (private), wodoo (Python), gettype (PHP), devtooling-cli (private):
  small tools I keep around.
- vrr-departure-board (HTML) and vrr-departure-android (Kotlin): live public-transport departure
  boards for VRR.
- models_frontend_benchmark: a small benchmark of frontends against local models.
- jekyll-docker, symfony-*, laravel-*, swagger-php, bypass, zero-connection-attempt,
  vanilla-php-docker-compose, php-childprocess-example, python-repo-template,
  app-template-cli, codecrafters-http-server-python, rust-minigrep-example,
  rust-amqp-to-mysql-consumer, laravel-test-project (private), lara-otel-service,
  basic-laravel-horizon-example, symfony-carbon-example, symfony-barebones-messenger,
  yet-another-farm (private), 2g-receipts-server (private), 2g-receipts-docs (private):
  work repos and learning repos, mostly PHP and Rust examples. Rarely worth a spark.
- dotfiles, nvim-config (private), Neovim-from-scratch: the editor setup.
- openHAB-conf (private): home automation config.
- Lychee: photo management I have looked at for the photo gap.
- Youtube-dl-WebUI: a web front end for youtube-dl.
- euro_rails.skill.md, travel_planner.skill.md: skill files I wrote for trip planning.
- wojtek.second.brain.obsidian.vault (private): the notes vault, including this digest.
- temp_collector (private), surface-stomp (private), pi-kubecraft1, ds-fluxcd-test,
  deploy_piwogo_to_mikr_us, deploy_photoview_to_mikr_us (private),
  hermes-careerguide-backup (private), otel-extended-slides: scratch and one-off repos.

## Homelab services (what runs in the cluster today)

arr-stack (Sonarr, Radarr, Prowlarr, Bazarr, qBittorrent, homepage), Karakeep, Nextcloud,
Paperclip, the Hermes gateway profiles, Hindsight, docs-mcp, llm-hub (LiteLLM), gpu-embedding
(Ollama), freellmapi, Pi-hole behind oauth2-proxy, Mattermost, Shlink, Opengist, Excalidraw,
Node-RED with InfluxDB for Zigbee, Speaches, Voicebox, the status page, host-watch,
mail-archiver, firecrawl, ghcr-pull, star-office, openchamber.

Wanted and not running yet: monitoring and alerting I trust, proof that a restore works, SSO in
front of everything, a photo library that survives, cheaper local model serving.

## Image and model stack

ComfyUI and stable-diffusion workers on the M1 Max, pinned by image tag, output into the Image
Studio board and Matejko, the image agent. Local models on the M1 Air behind llm-hub, plus
gpu-embedding on Ollama. Anything that makes a local model cheaper to run or better at
references and text rendering is fair game.

## Memory and agent experiments

Hindsight as long-term memory, docs-mcp indexing manuals before anyone answers, honcho as an
experiment, the Hermes profiles with Mattermost and email as front doors, Paperclip running the
boards. Half-finished ideas live here: memory quality, tool permissions, approval gates,
per-agent audit trails, local models small enough for the M1 Air.
