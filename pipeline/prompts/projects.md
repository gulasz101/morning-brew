# Projects

One short paragraph per project. The writer gets this text verbatim and uses it to decide
whether an item has a real fit. The owner corrects it in the PR.

The lists name what runs in the thing today. An item fits when it would replace, sit next to
or extend one of those, or close one of the gaps a project lists. The full inventory of boards,
repos and services is in `inventory.md`, and a spark may start from anything in it.

## riffradar

RiffRadar is my private guitar practice and riff-learning project: it tracks what I am
working on, breaks a song into the parts I actually need to drill, and keeps the practice
history. The repository is private, so this description is the only thing the writer knows
about it. Nothing from its code, data or roadmap may be quoted or inferred.

## homelab-2nd

My homelab: a k3s cluster on `homelab-2nd` with three workers, an OMV box as the only
durable storage, everything delivered by Flux from the public `gulasz101/homelab-2nd` repo.
Postgres runs on CloudNativePG with backups and WAL to MinIO on OMV, secrets are SOPS and
age, and every public service gets its own Cloudflare Tunnel. These are the things that
actually run in it, so an article can be matched to a real service:

- media and files: arr-stack (Sonarr, Radarr, Prowlarr, Bazarr, qBittorrent, a homepage),
  Karakeep for bookmarks, Nextcloud for files and photos.
- agents: Paperclip for the issue board and agent runs, the Hermes gateway profiles,
  Hindsight for long term memory, docs-mcp for the documentation index, llm-hub (LiteLLM)
  as the model gateway, gpu-embedding on Ollama, freellmapi.
- home and network: Pi-hole behind oauth2-proxy for DNS level ad blocking, Mattermost for
  chat, Shlink for short links, Opengist for gists, an Excalidraw whiteboard, Node-RED with
  InfluxDB for Zigbee sensors, Speaches for speech to text, Voicebox for text to speech.
- operations: a status page built by a small Python checker, host-watch, mail-archiver,
  firecrawl, a ghcr-pull helper, star-office and openchamber as small web apps.

Gaps I want to close: monitoring and alerting I trust, proof that a restore actually works,
SSO in front of everything, a photo library that survives, and cheaper ways to run small
models. If a tool has no Kubernetes path, no backup story or no metrics, it is not going in
without a fight. So for server software, name the service it would replace, sit next to or
extend, and name the gap it closes.

## ideogram4-local

Local image generation on the M1 Max: ComfyUI and stable-diffusion style workers run at
home, pinned by image tag, fed from the homelab, with the output going into my own image
studio. That studio feeds Matejko, my image agent, which makes the pictures for the blog and
LinkedIn. Anything that makes a local image model cheaper to run, easier to control or
better at references and text rendering is interesting, and so is anything that gets a large
model to fit in 64 GB of unified memory without a cloud. Anything that is API-only and
cloud-locked is not.

## code-factory

My software factory, the way code gets written now. A work order goes in, my PM writes the
spec, a Tester writes the failing test, a Builder makes it pass, a Reviewer reads the diff
and a Verifier runs the repo's own `check`, and the merge is mine. The rules are ADR-093 in
the homelab-2nd repo, and Paperclip is the board that runs the orders. Anything that makes one
of those stages stricter, cheaper or harder to fake is interesting: skill files, test
generation, review automation, CI babysitting, merge gates, sandboxes for untrusted code.
Another dashboard that shows me a diff I still have to read myself is not.

## agent-fleet

The agents I run as colleagues: a PM that never sleeps, an ops one for the homelab, a blog
one, an image one, and a few more Hermes profiles sharing one gateway on an M1 Air on the
shelf, with long term memory in Hindsight, a docs server that indexes the manuals before
anyone answers from memory, and Mattermost and email as their two front doors. Interesting:
agent skills, review and PR automation, memory, tool permissions and approval gates, and
local models small enough to run on that same machine. Not interesting: another chat wrapper,
a seat licence per agent, autonomy with no audit trail, or a research paper that could
theoretically help one of them somewhere. I want a tool I can run this month, not an
algorithm to admire.

## morning-brew

This pipeline itself: a day of Karakeep bookmarks becomes this post, Parakeet transcribes
the videos, one writer call per item, a lint that rejects hype and dashes, then a marmite
site published to GitHub Pages. The repo is `gulasz101/morning-brew` and the writer runs
through llm.voitech.dev behind Cloudflare, where a 100 second edge cut is a real constraint.
Anything that makes the fetch, transcript or writer step cheaper, faster or less flaky is
interesting, and so is anything that improves the project matching in this very post.
Anything that wants a hosted SaaS in the middle of that chain is not.
