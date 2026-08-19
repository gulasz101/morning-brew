---
date: 2026-08-03
slug: 2026-08-03-morning-brew
tags: digest,karakeep,apple-silicon,image-generation,stable-diffusion
---
# Morning Brew — 2026-08-03

Hoarded 1 bookmark on 2026-08-03 — one article, no video. A single link on the day, and it's the standard "AI on Apple Silicon is actually good now" argument: run Stable Diffusion locally, skip the cloud, stop paying for credits. Nothing you haven't heard if you've been within earshot of the M-series GPU discourse, but the piece does a clean job of the cost math.

---

## 1. Run Stable Diffusion on Your Mac — No Cloud, No Limits, No Cost
- **Source:** https://www.thinkdifferent.blog/blog/run-stable-diffusion-on-your-mac-no-cloud-no-limits-no-cost/
- **Karakeep doc:** `lvtui85wkz4ecblhb2v4enin`

Jakub Jirák's pitch for local image generation on Apple Silicon, and honestly the three title claims mostly hold up: no cloud (true — it's all on your GPU), no limits (true with the nuance that "no limits" means no content filters, no credit meters — but also no guardrail, so the ethics are your problem), no cost (true if you already own a Mac with enough RAM).

The easy path is **Draw Things** — a free, native Metal-optimized SD studio where a non-technical person is generating in ten minutes, no Python or virtualenv in sight. His starter recipe: Juggernaut XL, 1024×1024, 30 steps, DPM++ 2M Karras, and a prompt that reads like actual photography. Realistic times at that config: 60–90s on an M1/M2 Air (16GB), 25–40s on an M3/M4 Pro, 12–20s on an M4 Max, under 10s on an M3 Ultra Studio. Flux.1 [dev] wants 24GB+ and runs 2–4× SDXL times — a 90-second coffee-sip on his M3 Pro.

The argument that'll make PC people's heads spin: **unified memory beats VRAM for this workload.** A €600 RTX 4060 Ti caps at 16GB VRAM and grinds to a halt when a model doesn't fit; a 36GB MacBook Pro loads Flux at full fp16 plus a refiner plus an upscaler simultaneously — a config that's flat impossible on any consumer NVIDIA card short of a 4090/5090. NVIDIA wins raw speed; the Mac wins capability-per-dollar-at-a-given-memory-size, and in image gen, memory is destiny.

When Draw Things gets boring, **ComfyUI** is the node-based power path — native Metal, drag a workflow PNG onto the canvas and the entire node graph reconstructs itself, and it's where Mac users get bleeding-edge stuff (new samplers, Flux ControlNets, video models like LTX) months before polished apps wrap them. **LoRAs** are the consistency hack cloud services ration: drop a 50–300MB `.safetensors` from Civitai into Draw Things or ComfyUI and reference it at a chosen strength — that's how you get the same style across a blog series. Draw Things even does on-device LoRA training; feed it 15–20 photos and a few hours of compute and you get a personal model no subscription will rent you.

Honest verdict section: out of the box it won't match Midjourney's house aesthetic, but the gap closes fast with the right checkpoint, and **Flux.1 [dev] genuinely beats Midjourney on prompt adherence** — ask for "three cats, the middle one wearing a red collar, text on the sign says OPEN" and it actually delivers. Local wins on consistency (LoRAs), ControlNet composition control, unlimited iteration, and privacy for unreleased designs.

**Verdict:** Solid, honest explainer, and the memory-is-destiny argument is the real insight most people miss. The cost audit is worth quoting: a 30-second SDXL generation on an M3 Pro is ~0.0005 kWh — about a thousand images per cent of electricity, against $10–60/month for Midjourney. Only gripe: it's a 2026 piece retreading ground that was already getting tired in 2024, and the D&D-character-portraits flex is doing a lot of heavy lifting for the "actually good" claim. Recommended hardware floor: 16GB for SDXL, 24GB+ for Flux territory.
