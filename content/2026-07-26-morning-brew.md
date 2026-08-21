---
date: 2026-07-26
slug: 2026-07-26-morning-brew
tags: digest,karakeep,open-source
---
# Morning Brew — 2026-07-26
Four bookmarks on 2026-07-26: a self-hosted file-processing swiss army knife, a neural video codec Microsoft finally open-sourced, a "natural Ozempic" health claim that deserves a heavy dose of skepticism, and one Instagram cooking reel (transcribed). Theme of the day: **self-hosted infrastructure and AI, plus a side of diet-marketing BS.**

---

## 1. SnapOtter — a self-hosted file-processing swiss army knife — by snapotter.com

![snapotter.com](https://snapotter.com/og-image.png)

SnapOtter is a self-hosted, open-source (AGPL-3.0) platform for processing image, video, audio, PDF, and documents entirely on your own infrastructure — the pitch being "private file processing for data that can't leave your network." Air-gap capable, compliance-friendly, and deployable via Docker, Kubernetes, or bare metal on ARM and x86. It bundles 200+ tools across 5 modalities (image, video, audio, PDF, files) — resize, crop, compress, OCR, transcribe, strip metadata, convert formats, blur faces/PII, AI colorization, video→GIF, PDF merge/split/protect, you name it. It also runs 19 local AI tools and exposes a full REST API with OpenAPI docs plus pipeline automation and batch processing. Multi-user with role-based access, OIDC/SSO login, 21 languages, and a live demo. Free forever in the open-source edition; the Enterprise tier adds SAML SSO, SCIM, multi-tenancy, per-tool permissions, S3 storage, webhooks + audit export, and a commercial license (no AGPL). Positioning is the self-hosted answer to cloud image editors — useful when files can't leave your network.

- 🔗 https://snapotter.com/
- karakeep id: `iwzoyma2kqyuyturwwbjwigq`

---

## 2. Microsoft open-sources MLVC — a neural video codec that actually deploys — by github.com

![github.com](https://opengraph.githubassets.com/9dc98c72545406b2791c521e67d61f53ba3d0f75343ff7f52f359362bbc08d90/microsoft/mlvc)

Microsoft open-sourced its ML (MLVC) video codec under MIT license on its Linux/Open Source blog (24 July 2026), putting code + trained weights + training scripts + NPU conversion tooling on GitHub (`microsoft/mlvc`). This isn't a lab demo — it's the productized descendant of the DCVC research line Microsoft has published since 2021, already rolling out in **Microsoft Teams** for peer-to-peer calls with telemetry, A/B testing, and fallback to conventional codecs.

Headline numbers (at equal subjective quality, ITU-T P.910 MOS): up to **87.8% bitrate savings vs H.264** and **75.5% vs hardware H.265** at 360p; measured with PSNR across the wider test set the real gain lands closer to **52%**. The more interesting engineering story: neural codecs historically failed because entropy coding needs encoder and decoder to compute identical probabilities — run the same net on an Apple Neural Engine and Qualcomm Hexagon and you get divergent floating-point results, so the bitstream decodes to garbage. MLVC fixes this by transmitting scale parameters explicitly through the hyperprior, and by ditching exotic activations and INT8 quant (INT8 convolution isn't reproducible across vendors) in favor of FP16 and ReLU/LeakyReLU with ReGLU gating. That discipline costs ~6 points of BD-rate vs a perceptually-trained DCVC, but buys decodability on hardware Microsoft doesn't own.

Reality check: there's no bitstream standard (the trained weights ARE the format), no MIME type, no DRM/packaging story, and nothing in a TV/browser can play it today. Real-time 540p at 30fps holds on Apple M3/M4, Intel Lunar Lake, and Qualcomm Snapdragon X Elite NPUs at under half the NPU; 1080p real time only on the cut-down MLVC-S on Apple, one direction. The repo is a recent code drop (single "Hello MLVC" commit), and it's Python 3.12/3.13 + uv only — no linkable C++ library yet (that's a follow-up). For streaming ladders nothing changes this year; for peer-to-peer conferencing on hardware you control, worth an afternoon.

- 🔗 https://github.com/microsoft/mlvc
- karakeep doc: `qugzr9teygy0371u6pvhtit5`

---

## 3. "Naturalny Ozempic" — a clickbait name for some genuinely interesting black elderberry data — by well.pl

![well.pl](https://pliki.well.pl/i/09/04/81/090481_r2_940.jpg)

The Well.pl article (recovered via the syndicated path — the original saved URL 404s) is classic diet-marketing bait: elderberry juice = "natural Ozempic." The actual study is from **Washington State University**, published in *Nutrients*, and it's small — **18 overweight participants, one week**, drinking ~350ml of black elderberry juice or a placebo-matched drink on a standardized diet. Results: a shift in gut microbiome toward beneficial bacteria, ~**24% lower post-carb blood glucose** and **9% lower insulin**, plus the body appearing to burn more fat as energy after both carb meals and exercise. The authors attribute it to high **anthocyanin** content — you'd need ~4 cups of blackberries to match ~180ml of juice.

The honest parts: it's a tiny cohort and a single week, more research is needed, and the "natural Ozempic" framing is pure media shorthand — the juice does **not** work like a GLP-1 agonist and can't replace the drug. They do want to test whether elderberry bioactives help people who've finished GLP-1 therapy maintain weight. Cute data, tempting title, and a strong dose of "don't throw out your Ozempic." Worth reading as a sanity check, not as a weight-loss fix.

- 🔗 https://www.well.pl/life/148/dziala_jak_naturalny_ozempic_to_spalanie_tluszczu_w_wersji_turbo,25303.html
- karakeep doc: `ra5vbqn8nsitdm3i4qriotyg`

---

## 4. Ola | Dom • Ogród • UGC — "giga pancake" from the oven — by instagram.com

🎬 **Video.** The audio transcript is useless — the mic caught a cheery "sweet summer day" jingle, not the recipe. The actual content lives in the caption, and it's a one-gimmick lifehack: don't babysit a pan one pancake at a time, bake a giant monster pancake in the oven. Real trick: crank the oven to 220°C with the baking sheet inside to heat up; meanwhile mix 300ml milk, 4 eggs, a pinch of salt, 160g flour, plus a little sugar/vanilla; pull the hot sheet out, oil it, pour the batter straight onto the hot metal so the bottom sets immediately; bake 10–15 min at 220°C, keeping an eye on it. Pitch: everyone gets a warm pancake at once, no stove babysitting, "better than pan pancakes." The hot-sheet bit is the genuinely clever part — skip it and you get a floppy sad oven crepe. Worth it if you're feeding a crowd; overkill for a solo breakfast. A cute weekend weekday hack.

- 🔗 https://www.instagram.com/reel/DbOgClhOUJn/?igsh=MW5vaDR6YzN5d3Fsbw==
- karakeep doc: `h8bk25aourenjrfdk26bwyaf`

---

*Daily digest generated 2026-08-19 by Hermes nightly karakeep processor.*
