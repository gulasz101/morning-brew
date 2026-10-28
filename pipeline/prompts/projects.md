# Projects

One short paragraph per project. The writer gets this text verbatim and uses it to decide
whether an item has a real fit. The owner corrects it in the PR.

## riffradar

RiffRadar is my private guitar practice and riff-learning project: it tracks what I am
working on, breaks a song into the parts I actually need to drill, and keeps the practice
history. The repository is private, so this description is the only thing the writer knows
about it. Nothing from its code, data or roadmap may be quoted or inferred.

## homelab-2nd

My homelab: a k3s cluster on `homelab-2nd` with three workers, an OMV box as the only
durable storage, everything delivered by Flux from the public `gulasz101/homelab-2nd` repo.
Postgres runs on CloudNativePG with backups and WAL to MinIO on OMV, secrets are SOPS and
age, and every public service gets its own Cloudflare Tunnel. If a tool has no Kubernetes
path, no backup story or no metrics, it is not going in without a fight.

## ideogram4-local

Local image generation on the M1 Max: ComfyUI and stable-diffusion style workers run at
home, pinned by image tag, fed from the homelab, with the output going into my own image
studio. Anything that makes a local image model cheaper to run, easier to control or
better at references and text rendering is interesting. Anything that is API-only and
cloud-locked is not.
