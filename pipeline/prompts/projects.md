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

## code-factory

My software factory, the way code gets written now. A work order goes in, my PM writes the
spec, a Tester writes the failing test, a Builder makes it pass, a Reviewer reads the diff
and a Verifier runs the repo's own `check`, and the merge is mine. The rules are ADR-093 in
the homelab-2nd repo. Anything that makes one of those stages stricter, cheaper or harder
to fake is interesting: skill files, test generation, review automation, CI babysitting,
merge gates. Another dashboard that shows me a diff I still have to read myself is not.

## agent-fleet

The agents I run as colleagues: a PM that never sleeps, an ops one for the homelab, and
Hermes profiles sharing one gateway on an M1 Air on the shelf, with long term memory in
Hindsight and a docs server that indexes the manuals before anyone answers from memory.
Interesting: agent skills, review and PR automation, memory, and local models small enough
to run on that same machine. Not interesting: another chat wrapper, a seat licence per
agent, autonomy with no audit trail, or a research paper that could theoretically help one
of them somewhere. I want a tool I can run this month, not an algorithm to admire.

## morning-brew

This pipeline itself: a day of Karakeep bookmarks becomes this post, Parakeet transcribes
the videos, one writer call per item, a lint that rejects hype and dashes, then a marmite
site published to GitHub Pages. Anything that makes the fetch, transcript or writer step
cheaper, faster or less flaky is interesting. Anything that wants a hosted SaaS in the
middle of that chain is not.
