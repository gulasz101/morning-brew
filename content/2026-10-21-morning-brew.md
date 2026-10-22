---
date: 2026-10-21
slug: 2026-10-21-morning-brew
tags: Open Source Software, Command Line Tools, Internet Technology, Cybersecurity, Cloud Computing, Software Development, Artificial Intelligence, Web Development, AI Agents, Linux, Open Source, open-source, Linux Software, Cloudflare
---

# Morning Brew — 2026-10-21

Wednesday was an OpenAI week, and the two halves are worth taking separately. The product half is the company turning itself into an ad platform: ChatGPT Ads is now in 89 countries after opening 26 more, past 100,000 advertisers and 1.2 billion weekly users, and the pitch to any CFO with a cheap-tier problem is that advertising is what funds it. Ads stay out of Plus, Pro and Enterprise, and the promises are the standard set — conversations are not shared with advertisers, data is not sold, ads are labelled and never influence the answer. The difference from Google is that Google's ad load was visible on the page, and this one is injected into a transcript you are reading.

The engineering half is the part that actually matters. OpenAI ran a two-month coordinated disclosure drill, and the output was two PHP flaws, CVE-2026-109618 and CVE-2026-109619, both CVSS 9.2, found by an agent reading a whole-brain CRISPR atlas. PHP powers roughly 70% of the web, so pre-auth remote code execution against WordPress, Drupal and Joomla is not a footnote. Fixes are in 8.2.35, 8.3.36, 8.4.27 and 8.5.12, and affected releases reach all the way back to PHP 5.4. Cloudflare had WAF rules live about nine hours before the disclosure went public, free tier included. The rest of their blog is a full transaction detection primitive for the WAF and the note that eight eMudhra intermediate certificates were compromised because the CA generated the private keys wrong, so anyone can recover them from the public certs.

The other thread is the one running all week: small models on your own silicon. Haku took Google's EmbeddingGemma 2, an embedding model never trained for speech, and made it transcribe by freezing the audio encoder and training a 19.6-million-parameter reader that drags each 40ms slice of audio into the model's text space and picks the nearest of roughly 229,000 English words. No language model, greedy CTC decoding, an hour of audio in about 13 seconds on a base MacBook Air. There is a Haku Lab landing page, a small-models-on-your-own-hardware pitch, a reader v2 on Hugging Face, an independent Android and iOS rebuild in a repo, and a research note in the vault, all pointing at the same trick.

Videos are the useful counterweight. Brodie Robertson is unimpressed that the Linux kernel is dropping the "Assisted by:" commit tag, and he has the Maintainer Summit detail to back it up. Theo eats his own two-year-old prediction that AI stops improving, then explains why Opus 5.5 broke it. Better Stack has the Ledger wallet implant that never touched the crypto, the supermarket fridges rewired to run a 50C defrost cycle, and the Rust memory-safety bug that sat unsound for eleven years. The PrimeTime ran the Dream manhunt scandal as a group quiz show.

Bottom is the furniture, and today there is a lot of it: 25 audio analyzers, 16 fractal tools, 6 Matrix servers, 3 scientific workflow engines, 5 Docker containers for developers, and a list of 100 GUI applications that is explicitly a selection and not a ranking. All with live links to every named project.

### Hand-bookmarked

## 1. Embedding Gemma Transcribe (Haku) — research note — by keep.voitech.dev

![keep.voitech.dev](https://keep.voitech.dev/favicon.ico)

**Source:** https://keep.voitech.dev/bookmarks/f5aulz0j9qtmy5cqqg7iwob0
**Karakeep doc:** `f5aulz0j9qtmy5cqqg7iwob0`
**Project:** [Embedding Gemma Transcribe](https://eg2.haku.sh/) — a free macOS app that turns Google's EmbeddingGemma 2 into an on-device speech-to-text engine

Haku took Google's EmbeddingGemma 2, an embedding model never trained for speech, and made it transcribe: freeze the audio encoder, train a tiny reader that drags each 40 ms slice of audio into the model's text space, and let the nearest of roughly 229,000 English words win. There is no language model anywhere in the loop. Haku trained the reader in under two hours on 8×H100, and the open reproduction (john-rocky/eg2-transcribe, Apache-2.0) trained its own 19.6 M-parameter CTC reader on 960 hours of LibriSpeech. Speed is the flex: 288× realtime on a base M3 MacBook Air, so an hour of audio in 12.6 seconds, and 548× on an M4 Max via Core AI, with a Pixel 8a chewing through the same 54-minute LibriVox book in 276.8 seconds at 5.78% WER. Accuracy is where it stings. Vendor WER is about 5% against 2-3% for leading models, the reproduction measures 4.21% on test-clean but 10.42% on test-other, and homophones make up 12.9% of substitutions because nothing in the stack can break the tie. The lexicon is closed and English-only, so Polish, German, names and product jargon are guaranteed errors, and training data was read audiobooks, so meetings and YouTube remain unmeasured territory. It is also a macOS GUI app with no CLI, no server and no API, so it cannot be dropped into a pipeline as-is. The two most interesting things sit in the decoding contract. The word table is a real file, word_table.npy plus vocab.txt, one normalised 768-d row per word, regenerated by make_table.py, so you can append your own proper nouns and re-embed them. The scoring rule exposes a per-token margin between top word, runner-up and blank, which is precisely the per-word confidence signal that keeps resurfacing as greenfield. Neither exists in the shipped app, and the Core AI build of the reproduction wants macOS 27 while the PyTorch path is what runs on an older machine. Verdict: a reference implementation rather than anything to fork, but the frozen-encoder-plus-one-small-specialist-per-stage design is the pattern worth stealing, and the editable in-model dictionary is the first one that is both English-capable and user-extensible.

## 2. FluidAudio/Documentation/Benchmarks.md at main · FluidInference/FluidAudio — by GitHub

![GitHub](https://repository-images.githubusercontent.com/1006258471/3acb1b56-89f2-481f-a706-1f5af2839849)

**Source:** https://github.com/FluidInference/FluidAudio/blob/main/Documentation/Benchmarks.md
**Karakeep doc:** `h3x8imxvnw8kjp1mv98l4jy4`
**Project:** [FluidAudio](https://github.com/FluidInference/FluidAudio) — Swift SDK for on-device CoreML audio models (ASR, TTS, VAD, diarization) on the Apple Neural Engine

FluidAudio is a Swift SDK for running speech models on-device through CoreML, and this benchmarks file is the receipt for how well the Apple Neural Engine path actually performs. The headline transcription numbers come from a 2024 M4 Pro with 48GB of RAM on macOS Tahoe 26. Parakeet TDT v3 across 25 European languages on FLEURS averages 14.7% WER, 4.7% CER and 209.8x real-time, with English (US) at 5.4% WER, Italian at 4.0% and Greek at 36.9%, which tells you exactly where the model is weak. On LibriSpeech test-clean (2,620 files, 19,452 seconds of audio) it averages 2.5% WER and chews through the whole set in 125 seconds, 155.6x real-time, while the English-only v2 model drops that to 2.1% WER at 145.8x. The v3 family comparison on an M5 Pro is the part worth bookmarking. v3 is 480MB and 2.27% WER on test-clean, ultra is 630MB and the most accurate at 2.13%, and phonon2 is 360MB and the fastest at 159x, hitting 480x on a 60-minute file, so on the same silicon you are picking between accuracy and speed. The unified English checkpoint does batch at 2.15% WER and 123.3x real-time but streaming collapses to 29.1x, because streaming re-encodes a 7.68 second window for every 1.04 second of audio, and the doc's own advice is batch for files, streaming for live audio. Nemotron streaming tiers land at 2.58% aggregate WER and 24.3x at the 1120ms chunk, and 6-bit palettization already beats int8 (2.24% WER, 422MB versus 564MB), though that is only a planned follow-up. TTS is where the CoreML work pays off. Kokoro ANE v3 needs 49.45ms median to emit 3.35 seconds of English audio, and the same model measured 511ms when the author naively put CPU+ANE on every graph, with .all and CPU+GPU aborting outright in Apple's GPU RNN path. Diarization reaches 10.6% average DER on the AMI SDM set against roughly 11-12% published for pyannote-community-1, at 323x real-time, with 12 of 16 meetings getting the speaker count right, and the author admits streaming diarization is substantially worse. The caveats are honest but sizeable. These are self-reported numbers, one machine per table, no whisper.cpp or mlx-whisper comparison in the same run, absolute RTFx is load-dependent, SenseVoice's int4 path is wrecked (31% WER, so it is not shipped), and the CUA-S1 decision-scoring section shows CoreML numerics failing probability-sum checks until a Swift stable-softmax fix took it to 73,110 of 73,110 calls completing. The verdict is that if you run parakeet locally this is the file to bookmark, because it tells you which checkpoint to pick and what your M-series box can actually chew through.

## 3. EmbeddingGemma 2 Transcribe — reader v2 — by Hugging Face

![Hugging Face](https://cdn-thumbnails.huggingface.co/social-thumbnails/models/mlboydaisuke/EmbeddingGemma-2-Transcribe-Reader.png)

**Source:** https://huggingface.co/mlboydaisuke/EmbeddingGemma-2-Transcribe-Reader
**Karakeep doc:** `phbrvpza3w3cttz0wbfm02au`

**Project:** [john-rocky/eg2-transcribe](https://github.com/john-rocky/eg2-transcribe) — the training code for this reader, an independent reproduction of Haku's non-public Embedding Gemma Transcribe Mac app

A 19.6-million-parameter decoder that turns Google's EmbeddingGemma 2 audio soft tokens into English words, one 40 ms token at a time, by mapping each into the model's 768-dimensional text-embedding space and reading out the closest of 200,000 words, or blank. No language model, greedy CTC decoding, no punctuation, no casing. The EmbeddingGemma 2 encoder stays frozen; only the reader is trained. Test-clean WER is 4.21% and test-other 10.42%, down from reader v1's 6.81% and 15.10% (v1 was 4 layers, 13.3M parameters, trained on 100 hours of LibriSpeech; v2 uses all three training sets, 960 hours). A long-audio check on The Adventure of the Speckled Band (3,257 seconds, 125 windows of 30 s with 3.84 s overlap) scores 3.81% through the PyTorch float32 path and 3.80% through the Core AI build, where the encoder runs on the GPU and the reader in float16 on the Neural Engine of an M4 Max. Training was cheap: one A100-SXM4-80GB, 4.38 hours, 9 epochs, 147,087 steps, AdamW at a 3e-4 peak learning rate. The interesting trick is the vocabulary. Instead of a token or character vocabulary, the reader scores every word by cosine similarity against the text encoder's own 200,000-word embedding table, with a learned scale of 216.351 and a separate blank class. That table is 307 MB of the roughly 385 MB download. The honest limits are printed in the card: 6.1% WER on words longer than five tokens, 12.9% of all substitutions are homophones, the most frequent errors are function words like and, in and a, and the model reads English audiobooks only. Against Whisper-class ASR, 10.42% on test-other is not competitive. The interesting claim is architectural. You can read speech out of an embedding model with a 20M-parameter head and no decoder LM at all. Independent reproduction of a Mac app whose code was never published, the weights sit in the HF repo and the training code in the eg2-transcribe repo, Apache-2.0, and the sibling build worth stealing is the Core AI one. Verdict: lovely research, not a drop-in transcription stack.

## 4. GitHub - john-rocky/eg2-transcribe: Speech-to-text built on the EmbeddingGemma 2 audio encoder with a trained reader: Android on LiteRT, iOS and macOS on Core AI — by GitHub

![GitHub](https://opengraph.githubassets.com/661f04fff7cab91e501cf25c242615403e5bc519f6d4483b2d033c66656caacc/john-rocky/eg2-transcribe)

**Source:** https://github.com/john-rocky/eg2-transcribe
**Karakeep doc:** `r5ylzgjjt2o6tv0e8695bbo6`
**Project:** [john-rocky/eg2-transcribe](https://github.com/john-rocky/eg2-transcribe) — on-device speech-to-text on the frozen EmbeddingGemma 2 audio encoder, Android via LiteRT and iOS/macOS via Core AI, Apache-2.0

This is the phone-side rebuild of a speech-to-text app whose code nobody can see. The idea comes from Shahir's post of 13 October and the Embedding Gemma Transcribe Mac app at eg2.haku.sh, whose code and weights are not public, so this repo is an independent reproduction and is not affiliated with Google. The trick is to take the frozen EmbeddingGemma 2 audio encoder, leave it alone, and train a small reader that maps each 40 ms audio token into the model's text space, then read out the nearest English word. Reader v2 is a 6-layer transformer with 19.6M parameters, trained with CTC on 960 hours of LibriSpeech against a fixed table of EmbeddingGemma 2 word embeddings, and only the reader is trained. Word error rate is 4.21% on test-clean and 10.42% on test-other, against 6.81% and 15.10% for the 4-layer, 13.3M-parameter v1. Decoding is greedy with no language model, and the vocabulary is the 200,000-word LibriSpeech lexicon. The iOS and macOS app is SwiftUI on Core AI, log-mel computed in Swift with a float64 FFT within 4.77e-7 of the transformers extractor, 30-second windows through two fp16 bundles. On an M4 Max a 54-minute recording takes 5.95 seconds, 548x real time, at 3.82% WER, and an iPhone 18 Pro does the same in 12.01 seconds at 271x. Android runs on LiteRT from Android 8.0 up, the encoder on GPU, CPU or a Qualcomm NPU, and a Pixel 8a grinds through the same 54 minutes in 276.8 seconds at fp32 with 5.78% WER. Apache-2.0, four stars, started 13 October. The honest catch is that a fixed 200,000-word lexicon with greedy decoding cannot say a name, a number or a term it never saw, and 10.42% on noisy audio is not Whisper. A very good demo, not a drop-in replacement.

## 5. Haku Lab — by Haku Lab

![Haku Lab](https://lab.haku.sh/favicon.ico)

**Source:** https://lab.haku.sh/
**Karakeep doc:** `wox5vkm4jq18699o15ad4wvq`

Haku Lab is a tiny outfit doing research on small language models that run on-device, currently only on Macs, across the GPU and Neural Engine, using their own Metal engine. The unifying trick is ternary weights, every parameter forced to −1, 0 or +1 at about 1.58 bits each, trained with quantization-aware training so the constraint is learned rather than rounded in afterwards. The clearest number on the site: a 10 MB date parser, 10M parameters, beats macOS's own NSDataDetector, which handles roughly 72% of realistic phrasings and drops sub-day relatives, holidays and fiscal periods. Five web-element classifiers, 1.5M parameters each and about 550 KB per model, classify a page element in under a millisecond on the Neural Engine.

Quantization-aware training is the part worth stealing: post-training rounding cost 3 to 8 F1 points on their classifiers, while QAT recovered them, and on `is_login` the ternary model actually beat full precision, 0.909 against 0.896. Training a general ternary base from scratch went up a deliberate ladder, 50M parameters and about $15, then 99M and $26, then 335M and roughly $100 total, with tool-call intent accuracy jumping from near 0% to 50% to 90% and 243 ms on an M3 MacBook Air's Neural Engine. The pattern they settled on is one frozen ternary base plus small LoRA adapters, and a 2.5%-of-base adapter lifted grammar accuracy from 93.7% to 96.8%.

They also stress-tested Prism ML's ternary Bonsai 27B, 7.17 GB on disk against 51.25 GB for bf16, scoring 74 on the BFCL function-calling benchmark but failing all three reconciliation traps, where it anchors to the first document it reads and never reconciles it with a newer one. Their TTS experiment cut fifteen sequential passes of fine audio codes down to one, 1.7× over the whole decode, with word-error-rate unchanged at 0.352 and a faint texture artifact still in there.

The awkward parts are the caveats. It is Mac and Apple silicon only, the Haku-Labs GitHub org has zero public repos, so there is no code to run, and most benchmarks are their own on their own models. Some of the models they test belong to other people, and some timings come from a rented A100 rather than a Mac. Still, the QAT-versus-rounding table and the end-of-turn detector that plateaued at 30% recall, then hit 60% after LoRA-fine-tuning LiquidAI's 230M LFM2.5, are worth the read. A research blog with numbers instead of vibes, and nothing to install yet.

## 6. Haku — Small models. Real work. All on your own hardware. — by Haku

![Haku](https://haku.sh/favicon.ico)

**Source:** https://haku.sh/
**Karakeep doc:** `coxy8ur1tk117yqpsq0f73ao`

Haku is betting that a few million parameters on your own Mac beat a rented giant model behind an API, and the landing page argues that case decently. The lab publishes its work either way, shipped or not, at lab.haku.sh, and the three shipped models are tiny and single-purpose: a 60M parameter formatter that cleans up dictation in under 100ms, a 26M parameter model that turns plain requests into structured tool calls, and a 14M parameter date resolver that turns "next Tuesday at 6pm" into an actual timestamp. Everything is quantised for Apple silicon and split across GPU and Neural Engine. The product side is four apps: Dictate at $19 and Terminal at $19.99 are out, Browse and Code are "coming soon", macOS 14+ only, with Windows, iOS and Android promised later. Payment is one-time, lifetime updates, no accounts, no subscription, and your voice never uploads. So the honest trade is this: $19 buys a dictation tool that works offline, and the company behind it has to survive on one-time sales while two of its four apps do not exist yet. The bigger open question is what the tiny models do on messy real input, because the published numbers are the lab grading its own homework on tidy demos. Worth a look if you are tired of paying per keystroke to a cloud model, and worth remembering that no public repo for the apps turned up, so closed. Where the cloud still wins, they say so themselves: for your agent, use the big model you already have.

## 7. Embedding Gemma Transcribe — by Haku

![Haku](https://eg2.haku.sh/speed-table.png)

**Source:** https://eg2.haku.sh/
**Karakeep doc:** `nc1bo6a20laz4cxf96hjvh1j`
**Project:** [Embedding Gemma Transcribe](https://eg2.haku.sh/) — on-device Mac speech-to-text built by hijacking Google's EmbeddingGemma 2 as a decoder

Somebody took Google's EmbeddingGemma 2, an embedding model, and turned it into a speech-to-text engine by abusing it. Haku's tool claims an hour of audio in roughly 13 seconds on a base MacBook Air, fully on device, free, v1.6, macOS 14+, Apple Silicon, with 715 MB of models pulled on first launch.

EmbeddingGemma 2 is multimodal, so text, images, audio and video already share one vector space, and the audio of a spoken word lands near the written word. The audio encoder stays untouched. A small reader moves each short slice of audio into the model's text space, the closest of roughly 229,000 English words wins, and a second tiny model adds punctuation and capitals. Only the reader was trained, for under two hours on 8xH100 using openly licensed English speech. The base model was never trained for STT.

Speed is the headline. 288x real time on the Neural Engine of a base M3 MacBook Air with 8 GB, which is an hour of audio in 12.6 seconds. On the same machine, IBM Granite Speech 5.0 TurboCTC running on the GPU via MLX manages about 150x, or 25.7 seconds for an hour. FluidAudio's published numbers for NVIDIA Parakeet TDT 0.6B v3 run from 156x on an M4 Pro to 335x on an M5 Pro, and their Phonon-2 Parakeet fine-tune hits 480x on an M5 Pro. The author is upfront that those are different, newer Macs and different audio, so it is a rough guide, not a like-for-like race.

Accuracy is where it bleeds. Word error rate sits at about 5%, against 2-3% for leading speech models. The plan is a better-trained reader closing that gap next iteration, which is a promise, not a result. You can drop in an audio file, or hold Right Option, speak and release to dictate into any app; the audio never leaves the machine.

No public repo surfaced, so the free download and the write-up are all there is. Worth a try for private dictation. Not worth it if you need publish-grade transcripts.

## 8. GitHub - blakeblackshear/frigate: NVR with realtime local object detection for IP cameras — by GitHub

![GitHub](https://repository-images.githubusercontent.com/167694194/7e73b000-3ab3-11eb-9a3a-bb923650172b)

**Source:** https://github.com/blakeblackshear/frigate
**Karakeep doc:** `zxql5s4n8xm6dy8k95gzz98h`
**Project:** [Frigate](https://github.com/blakeblackshear/frigate) — self-hosted NVR with realtime local object detection for IP cameras, built around Home Assistant

Frigate is a self-hosted NVR that runs object detection locally on your own IP camera feeds, and the repo is one of the genuinely mature self-hosted projects: 36,809 stars, 3,735 forks, MIT, 6,466 commits, and a dedicated custom component for Home Assistant so the detection events land in the same place as everything else on the box. Detection is OpenCV and TensorFlow on the local hardware rather than in someone else's cloud, which is the entire pitch, and it is why a GPU or Coral TPU is strongly recommended over a CPU. The design is unusually careful about not burning resources: cheap motion detection first to decide where to look, object detection in separate processes for maximum FPS, MQTT for integration, RTSP re-streaming to cut the number of camera connections, and 24/7 recording with retention driven by what was detected rather than by the clock. The live view supports both WebRTC and MSE for low latency, there is a built-in mask and zone editor, and translations run through Weblate. The important part is what happened on 15 October 2026, when v0.18.2 shipped with three security advisories that are worth understanding because they are not theoretical. GHSA-93xj-hg88-ffg7 is the bad one, a critical 9.9: three nginx-proxied websocket paths, /live/mse/api/ws among them, were never passed through the go2rtc source filter, and the default configuration exempted every built-in role including the lowest-privilege viewer, so any authenticated account could get root code execution inside the container and a byte-exact arbitrary file write. GHSA-qjjw-3v66-279f is the same bug class in the admin path, where the denylist blocked echo:, expr: and exec: but not ffmpeg:, which go2rtc expands internally into exec:. Both need admin or viewer auth respectively, and both run as root in the published image, which is documented as deployed privileged with host paths mounted, so container escape is the obvious follow-on. If you run Frigate 0.18.0 or 0.18.1, upgrade today, and if you exposed it to the internet, treat the credentials as burned. The honest caveat nobody mentions: the trademark on the name and logo is separate from the MIT code, the project is a company (Frigate, Inc.) not a foundation, and the 0.x version number still means the config schema will move under you. Verdict for Wojtek: the NVR to run if you want camera AI without shipping your footage to someone else's inference API, and the 0.18.0 to 0.18.1 window is a good argument for not exposing a security-sensitive service directly to the internet.

## 9. 5 Docker Containers for Devs — by KDnuggets

![KDnuggets](https://www.kdnuggets.com/wp-content/uploads/kdn-5-docker-containers-for-devs-feature.png)

**Source:** https://www.kdnuggets.com/5-docker-containers-for-devs
**Karakeep doc:** `rrymnxvtc52cv5b7rb4bvie2`

Nahla Davies makes a decent argument for a boring thing: pasting a JWT, a hex-wrapped gzip blob or a HEIC screenshot into a public paste box hands internal data to a stranger's web server, and nobody planned that, the alternative was fifteen minutes of setup for a five-second job. The five containers are IT-Tools for inspection, CyberChef for chained transforms, ConvertX for file conversion, Hoppscotch CE for API testing and Kroki for diagrams, each with a real one-liner. IT-Tools is one image (corentinth/it-tools, port 8080) holding JSON, JWT, Base64, hashes, UUIDs, regex and cron helpers, and the caution is honest: it is a convenience layer, not a vault. CyberChef (ghcr.io/gchq/cyberchef, port 8080) is entirely client-side with no backend, and the saved recipe is the real asset, so From Hex, Gunzip, Decode text as UTF-16, JSON Beautify is a shareable URL instead of four guesses. ConvertX (ghcr.io/c4illin/convertx, port 3000, JWT_SECRET, /app/data mounted) puts one upload page in front of FFmpeg, ImageMagick, LibreOffice, Pandoc, Calibre and Inkscape for 1,000-plus formats, with 24-hour auto-delete as the sane default. Two caveats there: local is not safe, since the converters parse whatever you feed them, and anyone who reaches the page before you create the first account can register it, so keep ACCOUNT_REGISTRATION off. Hoppscotch CE is the heavy one, three containers plus a Postgres you supply, a .env with a 32-character DATA_ENCRYPTION_KEY and a Prisma migration before the first login works, so budget an afternoon. Kroki (yuzutech/kroki, port 8000) renders PlantUML, GraphViz, D2, Structurizr and Ditaa, with Mermaid, BPMN, Excalidraw and diagrams.net needing companion images. The advice is sound: one Compose file, named volumes, pin tags, keep them off the public internet. The blind spot is that five containers means five third-party services you now patch, and pinning tags is weaker than pinning digests. Verdict: right idea, wrong amount of yak shaving for a JWT, but the paste box should be gone.

**Projects:**

- **[IT-Tools](https://github.com/CorentinTh/it-tools)** — IT-Tools.
- **[CyberChef](https://github.com/gchq/CyberChef)** — CyberChef.
- **[ConvertX](https://github.com/C4illin/ConvertX)** — ConvertX.
- **[Hoppscotch](https://docs.hoppscotch.io/documentation/self-host/community-edition/install-and-build)** — Hoppscotch.
- **[Kroki](https://docs.kroki.io/kroki/setup/install/)** — Kroki.
- **[FFmpeg](https://github.com/FFmpeg/FFmpeg)** — Mirror of https://git.ffmpeg.org/ffmpeg.git.
- **[ImageMagick](https://github.com/ImageMagick/ImageMagick)** — ImageMagick (9to5Linux roundup 2026-09-27).
- **[LibreOffice](https://github.com/LibreOffice/core)** — Read-only LibreOffice core repo - no pull request (use gerrit instead https://gerrit.libreoffice.org/) - don't download zip, use https://dev-www.li...
- **[Pandoc](https://github.com/jgm/pandoc)** — Universal markup converter.
- **[Calibre](https://github.com/kovidgoyal/calibre)** — The official source code repository for the calibre ebook manager.
- **[Inkscape](https://github.com/inkscape/inkscape)** — Project Website: https://inkscape.org - Code Repository: https://gitlab.com/inkscape/inkscape - Draw freely. 🖌.
- **[PlantUML](https://github.com/plantuml/plantuml)** — Generate diagrams from textual description.
- **[GraphViz](https://www.graphviz.org/)** — Open source graph visualization software.
- **[D2](https://github.com/d2lang/d2)** — D2 is a modern diagram scripting language that turns text to diagrams.
- **[Structurizr](https://github.com/structurizr/java)** — Structurizr for Java.
- **[Ditaa](https://github.com/stathissideris/ditaa)** — ditaa is a small command-line utility that can convert diagrams drawn using ascii art ('drawings' that contain characters that resemble lines like...
- **[Mermaid](https://mermaid.js.org/)** — Diagramming and charting tool — generates diagrams from text.
- **[BPMN](https://github.com/bpmn-io/bpmn-js)** — A BPMN 2.0 rendering toolkit and web modeler.
- **[Excalidraw](https://github.com/excalidraw/excalidraw)** — Virtual whiteboard for sketching hand-drawn like diagrams.
- **[diagrams.net](https://github.com/DaveRuijter/diagrams.net)** — DaveRuijter/diagrams.net.

### RSS — YouTube

## 10. Linux Kernel Just Abandoned AI Disclosure — by Brodie Robertson

![Brodie Robertson](https://i.ytimg.com/vi/lBCWjJslSc8/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=lBCWjJslSc8
**Karakeep doc:** `vqihnuqjt0oxx9hgumc6eqse`

Brodie Robertson walks through the kernel's decision to dump the "Assisted by:" commit tag, and he is not happy about it. The Maintainer Summit met on October 8 in Prague, roughly 30 maintainers were invited, a majority backed deprecating the tag, and Sasha Levin (Nvidia, co-maintainer of stable and LTS) submitted the patch stripping the requirement out of the docs. Jonathan Corbet has merged it into docs-next, so it is not in mainline yet. The replacement: describe your AI use in the cover letter, below the scissors line, and keep the commit message clean.

Robertson's own argument is boring and honest. He wanted the tag for data collection: how many incoming commits use AI, which developers use it, whether the curve is going up. The numbers say it was never much of either. Only about 10% of the 18,533 commits in Linux 7.3 through -rc7 carry it, while Robertson's own estimate is that over 20% of new submissions use AI, climbing every month. The paperwork was already mostly fiction, and the removal changes the record-keeping, not the code.

Linus Torvalds' position has not moved, and he has started proving it. In July he told the summit that Linux is not an anti-AI project, that anybody who disagrees can fork it or walk away, that AI is a tool like any other tool, and that the project does open source "because it results in better technology, not because of religious reasons". Two days before this video he landed his own commit in the tools section noting the code, the test programs and the first draft of the text were done with an LLM coding assistant, Claude Code, under his direction, with measurements run on his machine. The patch speeds up page-cache reads when many threads read small blocks from the same file. His reductio about rules that ban tools is the best line in the whole argument: if you cannot show you understand the machine by writing your code in assembly, do not submit kernel code, and do not use an editor for the commit message either, since editors exist to hide typing mistakes. What he actually expects is that people understand what they are doing, and that has very little to do with which tools they used. As long as he is around, AI gets used in the kernel, and individual subsystems are free to opt out.

Greg Kroh-Hartman is the one who flipped. He originally wanted the signal so he could review patches accordingly and ask for proper attribution, then accepted documentation is a good thing, with one gripe: naming specific commercial models in kernel commits reads as advertising, he would rather the word "LLM" do the work. Laurent Pinchart is losing something real. He says the absence of the tag is what lets him push back on review, because he can ask submitters if they forgot it and, in many cases, they never reply, which tells him they were being dishonest. "I'm not happy removing the tag without adding another mechanism for required disclosure." He wanted the cover letter route, few people backed it, and he is blunt that LLM commit messages are more verbose than human ones, so demanding a human-written message would let reviewers "quickly ignore patches submitted by meat proxies". Keith Cook notes it was just as unenforceable before, that his own logs are half him and half LLM trimmed by hand, and maybe now too verbose. Robertson's favourite bit is his own failure: he once mistook a maintainer's legitimately wordy commit log for machine output. The art community has the same disease, accusing human painters of AI because their mistakes look AI-ish.

Pinchart's real grievance is not the tag. He says the kernel's value is its contributors, that a handful of loud maintainers suddenly sound like they never cared about the people who write the code, and that hearing proposals about AI-flavoured reputation ranking where contributors get called collateral damage is "borderline sickening". Robertson's closing position is that the kernel is already a heavily AI-driven project and that is not going to reverse, so if you are anti-AI and you use Linux, decide what that means for you, and if you decide to leave, remember this follows you everywhere.

Two caveats the video skips. The tag arrived with Linux 7.0 in January 2026 off the 2025 summit consensus, and a first removal attempt in July died with Kroh-Hartman backing the tag, so the policy has been swinging for a year. More importantly, the commit message was the only machine-readable place this lived. Once it is gone, git history will never say which patches were AI-assisted, and the cover letter sits in a mailing list archive that nobody greps. Sign-off responsibility is unchanged, and AI agents still must not add a Signed-off-by line. Wojtek cares because this is the largest shared code base most of us ship on, and the direction of travel is settled: upstream stopped wanting to say out loud which parts were machine-written.

## 11. Programmers vs Dream's Fake Manhunts | TheStandup — by The PrimeTime

![The PrimeTime](https://i.ytimg.com/vi/y2C0Zpnl6p0/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=y2C0Zpnl6p0
**Karakeep doc:** `xy38sy6yp7mqkk5b51syk0e8`

TJ turns the Minecraft "Dream faked his manhunt videos" scandal into a group quiz show, with Prime, Trash and game engine dev Casey Muratori guessing how the 46 hidden cuts across Dream's three "uncut" manhunt videos were detected. A team using new tooling claims they can spot hidden cuts in any Minecraft video by reconstructing the session timer from the game's internals, since Minecraft never shows a stopwatch. Dream's own clip gives it away, a stopwatch jumps from two minutes to three during a cut, and a second one jumps backwards because he quit for a day and restarted the session from zero.

Then it turns into a genuinely good engineering explainer. Casey walks through why a "lag spike" in a client/server game is not a frame drop: your client simulates its own world, the server simulates the authoritative one, the two constantly diverge, so what you see is rubber banding or teleports when the client interpolates. Frame budget is 16.666 ms for 60fps, and the failure is client code running slow, the GPU drowning in work, or the server and network being late. Prime still loses sleep over the Apex version, where you run and the game keeps dragging you back.

The detection tricks are the good stuff: torch particles vanishing, the HUD disappearing, the hot bar changing, the debug menu closing, an achievement popping late, aim jumping with a still mouse, and iron ore smelting in 200 ticks (10 seconds) when the footage shows more ingots than 10 seconds of furnace could produce. Leila cross-checked the furnace timings and found 9.3 seconds of missing footage. A furnace opened at 14:20 and 9 frames produced 0.56 ingots, and 15.1 seconds after that first open a third ingot pops out. Casey scored six of nine rounds.

Two proofs that a cut happened rather than a settings change. The GUI scale test: at scale 2 every texture pixel becomes a 2x2 block so the inventory should get sharper, but it got blurrier, so you have resampling. And the enchantment glint, which Minecraft drives off wall-clock time (millis divided by 110,000 to make a 0..1 float). Glint is not game time, so a splice shows up as a jump in the animation.

Casey has a hard rule, learned the hard way on Mordoria. Game code should never touch the wall clock. You feed a timing struct forward (wall clock, game clock, audio samples) and treat it as authoritative, so replays are reproducible. Randomness has to be an input you control, not ambient entropy.

Best bit is the "boat clutch". Minecraft has a bug where entering a boat fast enough skips fall damage. Dream gets knocked off his tower, crafts a boat mid-air, and it saves him. The bottom hot bar shows the post-splice state, which is the opposite of what YouTube compression would do, so that one is a splice, not a codec artifact.

Caveat, and it is a real one. The transcript on disk covers only the first 60 minutes of a 64-minute episode, so the final reveal, the actual mechanism for reconstructing that timer from Minecraft internals, is not in what I could read. Nobody has shown the underlying tooling publicly either, and the 46-cut claim still comes from a fan group with infinite free time and a grudge. Verdict: best gaming-drama video I've seen this year, because it accidentally teaches netcode, animation timing and reproducible builds. 🎮

## 12. Hackers Hid a Cellular Spy Inside a Ledger Wallet #hack #security #crypto — by Better Stack

![Better Stack](https://i.ytimg.com/vi/vUmU8l4fCKs/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/vUmU8l4fCKs
**Karakeep doc:** `uyiupq2tewv6jq9qtcp9pd8c`

Fifty seconds of transcript, and the whole story fits: the attackers never broke the crypto, they added hardware around it. Researchers at Tibane Labs (the auto-transcript mangles it as "Tobain Labs") opened tampered Ledger Nano X units. In one, the battery was swapped for a smaller cell to make room, and underneath sat a microcontroller, a 2x2mm eSIM and a shielded LTE module. The implant watches what the screen shows and which buttons you press, which is enough to reconstruct the seed phrase, then ships the words out over LTE. Ledger's genuine-device check only verifies the secure element chip, so an extra board on the board passes attestation like nothing happened.

Where the units came from is the ugly part. They were traced to CryptoBilis, an authorised Ledger reseller operating in Malaysia, Indonesia and the Philippines. The researchers bought tampered units on Amazon Japan and on Yahoo! Auctions, some listed at nearly half price. The clip's headline number is BitQuery estimating about $93 million in suspected thefts from 315 wallets. Ledger's advice: if you bought from that reseller, do not set the device up; if you already did, move your funds to a new device with a new seed.

The researchers' own write-up fills in the part the clip skips, and it is worse than the clip makes it sound. Three generations. The first was a prototype Joe Grand of Grand Idea Studio took apart and presented at hardwear.io USA 2026: unmarked Cortex-M0+, a Luat Air700E LTE modem, a 5x6mm MFF2 eSIM, an 8cm hand-wound coil antenna, a 70mAh battery, and the fuel gauge bypassed so the charge always reads 100%. Their specimen A, from Yahoo Japan, replaced the loose wires with a Kapton flex soldered onto the board's factory test pads for ground, battery and the display SPI lines, carrying an STM32G431KBU6 and that tiny 2x2mm eSIM, with a flat antenna taped over a cell that has no protection circuit at all. Specimen B, bought on Amazon Japan from a China-based seller and shipped from Malaysia, is the one that should make your stomach drop: the flex is painted the same black as the Ledger board, the MCU and eSIM markings are scraped off, the original battery is untouched because the room was taken from the foam padding behind the OLED, and the whole thing is cut to the exact outline of Ledger's own surface-mount parts, so it drops into place with no measuring and no soldering skill. Someone ordered a custom antenna part-numbered AC-A2016-NANO-V1.1, already at revision 1.1. That is a production run.

The mechanism is the part worth keeping: the tap sits on the OLED's SPI bus, where the 24 words travel in plain, unencrypted screen traffic. The secure element is never touched, so the wallet genuinely is genuine. Ledger confirmed the investigation on October 9, 2026, asked CryptoBilis to halt sales and shipments, and told buyers from the past 90 days not to set up their device.

Caveats, because the numbers do not agree. The researchers' page cites on-chain investigator Specter at above $86 million and tanuki42 at more than $72 million across eight addresses; Ledger has confirmed neither a figure nor a cause, and says there are no reports involving devices bought directly from Ledger. The clip's $93 million across 315 wallets is BitQuery's estimate and I could not find it corroborated on the research page, so treat it as the loudest number rather than the best one. Tibane also states plainly that specimen B was not bought from CryptoBilis, and that the August ownership change it hints at rests on an unverified X post. One more thing the clip gets wrong-ish: it credits the screen-and-button reading to a former Mt. Gox CEO, a quote I could not match to the write-up, which credits the teardown to Joe Grand.

Verdict: the clip's closing line is the right one, unhackable only covers the part being checked, and the real attack is usually somewhere around it. If you own a Nano X bought from a marketplace reseller, treat the seed as burned and move your coins.

## 13. Rust Had a Memory Safety Bug for 11 Years #rust #programming #security — by Better Stack

![Better Stack](https://i.ytimg.com/vi/RxHSYzm2bXY/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/RxHSYzm2bXY
**Karakeep doc:** `s7gkhu6n0amcdexyfo1t3lzj`

A compiler bug let safe Rust hold a reference to freed memory for eleven years, and it is the good kind of Rust story. Unsound, not exploitable in practice, and only found because someone ran a ten-line program on Godbolt and asked a basic question.

The bug is rust-lang/rust issue 164250, filed recently and labelled unsound, which is the worst category a compiler bug can have. The shape of it is simple. You define a struct with a 'static bound, meaning whatever it holds must live forever, and you write a Drop impl that trusts that promise. Then in main you create an ordinary String that lives a couple of lines, create the struct empty, and assign a reference to that String into its field. The borrow checker should reject that assignment. It does not, because the compiler never checks the struct's lifetime bound on that field write.

So when the struct gets dropped, your Drop code holds a 'static reference to a String that is about to be freed. One variant hands that reference to a thread which prints it a second later, and now you are reading freed memory. Textbook use-after-free, in about ten lines that look completely safe to the borrow checker.

The timing is the story. A compiler contributor ran it on Godbolt and found the same program is unsound since Rust 1.4, back in 2015. The finder's own reaction was "how on earth has this not been found before".

Two caveats the headline skips. First, you will not hit this by accident: you have to deliberately write a Drop impl that abuses the bound, which is why the issue is tagged high priority and not critical. Second, Rust's memory safety guarantee holds everywhere except this one hole, which sits exactly where people write tricky code, and the hole is old enough that nobody noticed for a decade. Same family as the older `set_len` and lifetime-soundness screwups, and it says as much about the review process as about the compiler.

What to actually do: treat 'static bounds plus Drop as a sharp edge, keep lifetimes explicit in structs you own, and read the issue thread before assuming the compiler has your back on anything unsound-adjacent. Rust's whole pitch is that the compiler stops you from shooting your foot, and this is the compiler failing to ask the right question. Worth your attention. 🦀

## 14. AI Just Made Physics Interactive. This Is Insane. (Anatomy) — by Better Stack

![Better Stack](https://i.ytimg.com/vi/lyGYidIZK4I/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=lyGYidIZK4I
**Karakeep doc:** `joobq77nd72knfbiet2lnomz`
**Project:** [Anatomy](https://github.com/wheresryan22/anatomy) — agent skill that turns a technical idea into an interactive isometric figure of a real machine (SVG, optional WebGL, beta 3D, MIT)

Better Stack's Josh walks into a Claude skill with one rule at the top of its instructions: do not draw boxes and arrows. A boxes-and-arrows diagram tells you the part exists, it never tells you what the parts do, so the skill makes the agent invent a physical machine whose mechanism is your concept. The examples in the repo: a cache key becomes a pin tumbler lock where every pin has to line up before the door opens, an LRU cache becomes a mechanism that actually runs the cache, a dial indicator where the carriage slides and the needle reads each block, a Raptor engine that explodes into 11 assemblies with a WebGL exhaust plume, and a desk computer you can type on and watch the screen change.

The plumbing is deliberately boring. It is a normal agent skill, a SKILL.md full of instructions plus a drawing kit, an isometric camera, solids, tubes and an optional WebGL layer. Node 20.10 or newer, zero dependencies, no API keys, and it opens Chrome to show its work. It runs in Claude Code, Codex, OpenCode and Antigravity. Output lands in your project as a standalone HTML page, an SVG or a React component, and you steer it with a few words: interactive, WebGL, 3D, dark mode. The figures are MIT licensed, so you can ship them on your own site, and one dev on X already used it to explain their end-to-end testing product.

The part worth knowing is the order of work, because step one is literally called "truth first". Collect the real numbers, build a small pure model of how the thing behaves, and only then draw. The readout on screen is wired into that model, not typed by hand. Then it opens Chrome and audits its own geometry, checking that nothing passes through anything and that parts sit where they belong. Josh's own run was a figure for database connection pooling: a pool of 10 connections, a request borrows one and gives it back, and when they are all busy new requests wait in a queue. He also lists hash map collisions, binary search, DNS resolution, a bloom filter as a fruit machine, debounce and throttle as a music box, and LLM temperature as a wheel.

This is not Mermaid, D2 or Excalidraw, and Josh is explicit about the difference. Those draw topology, what connects to what, in seconds. Anatomy explains one mechanism and how one thing behaves. The README says it is not a chart library: no axes, no series, no plots, and it draws machines, instruments, tools and furniture, not people or exact maps.

The catch is time and tokens, and Josh does not bury it. There are size tiers: a normal figure takes 30 to 90 minutes, a hero piece two to four hours, and in one GitHub issue the maintainer said some renders take over 48 hours and burn all your tokens. Estimates swing wildly in both directions depending on which model you run it with. It also cannot fully check itself, which the project itself admits: Claude is very good at building these and not always good at seeing them, so treat the first figure as a draft or use the Claude browser extension so it can actually look. And the self-checks only prove the picture, not the facts. They verify that nothing passes through anything and that lines end where they should, but the metaphor itself is invented, so the explanation is only as true as the analogy the agent chose. The skill was about a week old when he recorded this, and the author turned down a pull request claiming it works with any compatible agent, preferring to name the four it actually supports.

Wojtek cares if he writes docs, blog posts or landing pages, because the output quality is a level up from anything an LLM can draw on its own. Start with the normal figure tier, read the metaphor before you trust the drawing, and if you are on a metered plan, keep your distance unless you enjoy watching tokens evaporate.

## 15. Hackers Turned Supermarket Fridges Into Ovens #hack #security #programming — by Better Stack

![Better Stack](https://i.ytimg.com/vi/WAPM0NouOwg/maxresdefault.jpg)

**Source:** https://www.youtube.com/shorts/WAPM0NouOwg
**Karakeep doc:** `hkvnztlk4umzjiip0h9qexgt`

Refrigeration controllers in French supermarkets were remotely rewired to run a continuous defrost cycle at 50°C, so the attackers didn't steal data, they cooked the stock. On October 12th, the French chains Intermarche, Leclerc and Cooperative U found that the refrigeration controls in some stores had been hit by a cyber attack. The controls were made by Dan Foss, a maker of commercial refrigeration systems. Every commercial fridge runs a defrost cycle to melt the ice off the coils, normally about two hours a day. The attackers turned that into continuous forced defrost with the temperature set to 50 degrees Celsius, about 122°F, inside a fridge full of fresh food.

Staff described a wave of heat coming out of the fridges and freezers. Early losses were already exceeding 300,000 euros and reports said it could reach several million nationwide. The president of Cooperative U confirmed it publicly, called it extremely serious and said nothing like this has ever happened before.

The same weekend, in the Netherlands, Albert Heijn, Eitos and Galengal had their websites taken down, deliveries stopped and the electronic shelf labels in stores started showing the wrong prices. Belgium's Delhaize reported problems too. Nobody has said whether the two attacks are even linked, and that is the honest answer, which the clip keeps rather than hides. The Dutch side looks like a separate availability attack, and wrong shelf prices could just as easily be a broken label system as deliberate price manipulation.

The takeaway is old and still true. A fridge used to run a dumb thermostat, now the controller sits on a network, and a setting as boring as defrost can wipe out a store's stock overnight. Anything you can configure remotely is part of your attack surface, and somebody found the setting that destroys food.

Caveats: no attribution, no ransomware mentioned, no detail on how the controllers were reachable in the first place, and no word from Dan Foss in the clip. "Hit by a cyber attack" is doing a lot of heavy lifting when the confirmed damage is spoiled stock plus a website outage. Still, the lesson lands cleanly, because the vulnerability was a defrost schedule and not a firewall.

Verdict: this is the IoT security pitch in its purest form, and it is genuinely funny. Refrigeration-as-a-service, with the defrost timer as the attack surface. 🧊

## 16. Opus 5.5 is proof that we do need smarter models — by Theo - t3․gg

![Theo - t3․gg](https://i.ytimg.com/vi/3OshsLm3_OQ/maxresdefault.jpg)

**Source:** https://www.youtube.com/watch?v=3OshsLm3_OQ
**Karakeep doc:** `ant55o3brjpnk87orrnhjp9e`

Theo opens by eating his own prediction. Two years ago he made a video called AI Isn't Going to Keep Improving and confidently argued we would hit a plateau where each new model bought less and less, and he made it before Opus 4.5 was even in training. He is here to say he was wrong, twice over. Progress went from autocomplete while you type to asking real questions about your codebase, to telling the model which files to edit, to handing it a screenshot of a bug and trusting it to work it out, test it and get it merged. He had reached a second, weirder conclusion: that we might not need models to be smarter at all, which he felt with Fable 5. Opus 5.5 changed his mind, and not because it is faster or cheaper. It is smarter.

The part that flipped him is the silliest possible one: Halo and Call of Duty, game mashups where things get reverse engineered, decompiled and mashed together into something new. From there a sharp observation. He always assumed model improvements would only benefit developers already on the bleeding edge. No. Smarter models benefit three tiers, and the tiers move at different speeds. Professional devs get more done, obviously, and he claims to be shipping more code in a week than in all of last year, with a lot of it better than yours. The second tier is technical people who never became developers, the Linus Tech Tips archetype, who know their way around a computer and have good intuition for what software can do but none for what is realistic to build. They used to tweak a tool for themselves and nothing more. Now they can fork code, debug systems they do not understand, and ship. The third tier, non-technical people, has barely moved yet.

The unlock was a single well-priced, accessible model on a subscription tier, which pushed the second tier deep into building things they do not understand. People who never coded and never opened Blender are paying $200 a month and porting maps out of old games into new reverse-engineered ones. His own example is a service he calls lawn, an open source alternative to Frame.io he rebuilt in a few days with Gemini 3 Pro and Opus 4.6, now with a few hundred people using it for video review pipelines, which he notes was a $1.3 billion company when Adobe bought it in October 2021. He claims roughly 70% of that functionality plus things Frame.io still does not have.

There is a sponsor break in the middle, BrowserBase, and it carries his argument. He frames three eras: AI that answers questions from what it knows, then agents editing files on your machine with tools like Claude Code, then a third era where agents stop being boxed inside the website and start doing real work on the web. That needs a platform, and the pieces he points at are authentication without handing your credentials to a browser you spun up yourself, session management so the agent is not logging in again every request, and a Search and Fetch API that beats curl because 85% of web APIs cannot be reached by curl at all.

Then the spice, and the reason to watch. Theo's take is that devs are not creative. His channel works because he is a 6 out of 10 at communication in a space where the average is a 3. Which is why dev teams keep a designer or product manager who cannot code but is paid over $100k a year, because devs are good at linking two libraries together in a novel way and bad at everything else. Meanwhile the people who cannot code are the creative ones, the Zapier generation who wired impossible things together because they did not know the rules, the woman with 40,000 OBS scenes used as dynamic layers. The unlock for them is that they do not know what is not possible, so they combine a game made in IW4 with a game made in UE3 and it works, and they do not know the difference between Java and JavaScript, so they build things that should not exist and turn out to be good.

He wants devs to unlearn the fear of failing, and he uses his own most popular short against us: why can't we commit our environment files. Decoupling source keys, letting the company see code it cannot run. The comment that gets him is "you want me to think? No, I am not paying you to think, I am paying you to write code, boil the ocean, but we cannot even find the ocean". His answer: dev PRs get merged so reliably that we feel bad closing them, and that expectation of a warm merge is now a liability, because the people who never coded do not expect their work to land and are therefore free to try insane things. He keeps the React Native app over the SwiftUI rewrite he prefers, because the agents move faster on the one he has.

The proof of concept is his rewrite of the TypeScript compiler in Rust. A few months ago he called it the unobtainium of AI. Now it works, in under 20 hours, two to three times faster than TSGO, compiles to WASM, and hits 99.99% accuracy against real TypeScript on the projects he cares about. He also built T3OS, a customised Ubuntu image for his agents rather than for him: headless, no GUI at boot, spawning XFCE forks for the agents to drive, and on bash instead of zsh because more than 30% of the errors his agents hit came from zsh formatting newlines differently and Claude then mangling the ripgrep commands. The last word belongs to the person you used to mock in high school for answering every problem with install Ubuntu, even though they had never programmed. That person is about to lap you.

The context matters. Anthropic shipped Opus 5.5 on September 22, 2026, its first release since the "pace the frontier" post, at $4 and $20 per million input and output tokens with cache reads at $0.20, roughly 40% cheaper per task than Opus 5, and 66.4% on Terminal-Bench 4.0 against Fable 5.1's 55.8% and GPT-6 Astra's 57.9%. Anthropic's own launch post warns that benchmark margins are getting less reliable at this level and that the real gap to Fable 5.1 is narrower than the scores suggest, which is roughly Theo's point in more careful language. The caveat he misses: his tiers are a personal taxonomy with a sample size of his group chat and his DMs, the creativity argument is an opinion dressed as a thesis, and the people Theo calls creators are shipping binaries and plugins into places they cannot audit, which is a security problem wearing a victory lap.

### 9to5Linux (RSS)

## 17. Debian-Based siduction 2026.1 &quot;Big Crime&quot; Released with Linux 7.2, KDE Plasma 6.7 — by 9to5Linux

![9to5Linux](https://9to5linux.com/wp-content/uploads/2026/10/sid261.webp)

**Source:** https://9to5linux.com/debian-based-siduction-2026-1-big-crime-released-with-linux-7-2-kde-plasma-6-7
**Karakeep doc:** `ubadbjavdqw3n6gv3smrhemh`

siduction 2026.1 "Big Crime" landed today, two years after 2024.1, and the pitch is the usual one: rolling Debian Sid with the latest of everything. Packages come from Sid as of October 18, 2026, the kernel is a customised Linux 7.2.11, and you get KDE Plasma 6.7.4 with Frameworks 6.30 and Gear 26.08.2, or Xfce 4.20 if you want less shininess.

The real work is the revamped command-line installer, now in every edition and wired into systemd-boot, which the devs recommend for anyone with straightforward hardware. It walks through configuration, suggests actions, checks dependencies, explains the settings it picked, and can be cancelled at any point. It also brings updated commands and dialogs, a consistent UI across screens, full UEFI/GPT support, opt-in non-free sources, and Btrfs support including creating siduction's standard subvolumes.

Btrfs gets a dedicated Btrfs Assistant app, and siduction-btrfs now handles a separate boot partition under GRUB and the Snapper plugin directory. Then there is "onoff", a new script replacing the init command that systemd 258~rc1-1 removed, restoring init 0 through init 6 so you can switch system states on a running machine.

Live ISOs come in KDE Plasma, Xfce, Xorg and noX editions, and existing installs just need apt update && apt full-upgrade. A reader points out that Debian 14 (Forky), the testing branch of Debian 13, also ships Linux 7.2 and Plasma 6.7.4, so the differentiators are the rolling base and the installer, not the version numbers. Since siduction is rolling, Plasma 6.8 should arrive on its own.

Worth it if you want Sid rolling with desktops that work out of the box. Less so if stability is the point, because Unstable does not care about your production server.

## 18. COSMIC 1.11 Desktop Environment Released with New Touchpad Settings — by 9to5Linux

![9to5Linux](https://9to5linux.com/wp-content/uploads/2026/07/cos13.webp)

**Source:** https://9to5linux.com/cosmic-1-11-desktop-environment-released-with-new-touchpad-settings
**Karakeep doc:** `lgtt1denlc622hulij20njco`

**Project:** [COSMIC](https://github.com/pop-os/cosmic-epoch) — System76's Rust desktop environment, tagged epoch-1.11.0

System76 shipped COSMIC 1.11 on 20 October 2026, tagged epoch-1.11.0, and the headline is a pair of touchpad toggles. Tap and drag lets you double-tap an item and move it, drag lock lets you lift a finger mid-drag without dropping what you are holding. That is most of the release, plus COSMIC Edit learning MIME type associations for JSON files, the compositor implementing xdg-dialog-v1 so modal dialogs stop hiding behind other windows, and hybrid-graphics machines finally using the right GPU for games.

Then the bug list: the close button in applets after a window is closed from app-list previews, mouse wheel and touchpad scroll changing volume, a blur region in the launcher overlapping the panel, a notification applet that refused to start, and closed windows not being removed when no outputs are connected. Input methods using the virtual keyboard protocol got fixed, the on-screen keyboard now receives activation over a private D-Bus signal, and the Pop!_OS launcher searches better inside parentheses. Three weeks after 1.10, by the way.

The release cadence is the caveat here. Three weeks after 1.10 means something in your session breaks roughly monthly, and the desktop is still a moving target even when System76 calls it stable. The comments already show the packaging lag, with one user reporting 1.11 missing from the Pop!_OS repositories on day one and another replying that it had landed. The screenshot 9to5Linux used is the COSMIC 1.3 image from July, which tells you how little the visuals have moved. xdg-dialog-v1 is the part with downstream value, because modal dialogs are exactly what makes Wayland apps feel wrong, and other distros will carry it over. Track it, install it when your distro ships it, and if you are on GNOME today keep your expectations low.

### Open-source Projects (RSS)

## 19. Paste in a company URL and get funding, LinkedIn, and news data back — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/exa-labs/company-researcher)

**Source:** https://www.opensourceprojects.dev/post/84334d58-99b0-4860-ac4a-441e15a9650b
**Karakeep doc:** `kg9a9uufeu0mtm9p6jf3ixsc`
**Project:** [company-researcher](https://github.com/exa-labs/company-researcher) — one URL in, a company dossier out, assembled through Exa's search API

Company Researcher from Exa's labs does one thing: you paste a company URL, it assembles a dossier. Website content plus subpages (About, FAQ, Pricing, Blog), the LinkedIn company profile and its founders, funding details, Crunchbase, PitchBook and Tracxn profiles, 10-K filings where they exist, and news coverage. One pass instead of ten browser tabs, which is a fair description of everyone's afternoon.

Everything goes through Exa's search API rather than a pile of custom scrapers, so there is nothing to maintain when a site redesigns. Each data source maps to a discrete documented call, and the README links every single one straight to Exa's playground, so you can see the request and the response before you write a line of code. That makes the README an actual tutorial, which is rarer than it should be.

The clever bit is the funding query. Instead of searching for "company funding" and dumping whatever comes back, it asks a summary model to "tell me all about the funding (and if available, the valuation) of this company in detail", and to reply with the single word "NO" when there is nothing. A tiny decision, and you get a clean signal instead of a page to sift through. The funding, news, 10-K and subpage lookups all request live crawling, which matters for data that moves.

The README is also honest about scope: the repository is out of scope for Exa's vulnerability disclosure program and not eligible for bounty rewards. Read that as "demo and utility, not hardened production infrastructure". There are no install commands either, and you need Exa API access to run it.

For Wojtek: 1,519 stars, MIT, TypeScript, last pushed September 27, 2026. It will not replace an analyst. It is a clean, well-documented starting point where each piece can be lifted on its own, and the query design is the part worth stealing.

## 20. A fast web fuzzer in Go for directory, vhost, and parameter discovery — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/ffuf/ffuf)

**Source:** https://www.opensourceprojects.dev/post/5442b075-3651-47ac-a558-7d6117938100
**Karakeep doc:** `x4b2b5a3riq2zy6m3j1028rr`
**Project:** [ffuf](https://github.com/ffuf/ffuf) — a fast Go web fuzzer for directory, vhost and parameter discovery

ffuf is the old-school Go web fuzzer: you hand it a wordlist, mark the spot with the FUZZ keyword, and it fires the requests. The keyword can go at the end of a URL path, inside a Host header, or into a GET or POST parameter name or value, so directory discovery, vhost hunting and parameter fuzzing all share one tool and one syntax. 16,926 stars, MIT, Go, last push 2026-09-26, and the maintainers still ship prebuilt binaries plus brew, scoop and winget packages, or `go install github.com/ffuf/ffuf/v2@latest`. Filtering is where the real work sits. The canonical vhost example throws out every 4242-byte default page with -fs, which is an honest admission that fuzzing produces mostly false positives, and size matching alone will still drown you whenever that default page changes size between requests. There is a practice target, the ffufme Docker container and a hosted ffuf.me with lessons, plus external mutators, config files and an interactive mode, and the wiki links Michael Skelton's "Everything you need to know about FFUF". The Open-source Projects write-up is mostly a README paraphrase with a newsletter pitch stapled to the end, so the source worth reading is the repo itself. The caveat nobody mentions: this is a weapon, and pointing it at hosts you are not authorised to test is a crime with a command line. Verdict for Wojtek: the one tool in this batch that will outlive the digest, and the one to point at an application you have just inherited, with written permission and a sane rate limit. It also survives contact with a real workflow, because a saved config file and an external mutator mean the same scan can be re-run after a new wordlist lands, which is more than most one-liner fuzzers bother with. Nothing about it is clever, which is exactly why it has outlived every fancier scanner that came after it.

## 21. A curated list of open-source cloud native tools, software, and tutorials — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/rootsongjc/awesome-cloud-native)

**Source:** https://www.opensourceprojects.dev/post/4718f103-f926-4058-9990-6e9cc5bedd1d
**Karakeep doc:** `weir6ij5ci9bsyp6z9s9twfs`
**Project:** [rootsongjc/awesome-cloud-native](https://github.com/rootsongjc/awesome-cloud-native) — a curated list of open-source cloud native tools, software and tutorials.

The Open-source Projects post calls this "a map" rather than another tool list, and the thing it maps is rootsongjc/awesome-cloud-native, a curated list of open-source cloud native tools that has been running since July 2017 and now has 2,462 stars, 439 forks, 100 watchers, a CC0 licence and a 30-contributor history. The taxonomy is the actual product. Instead of one undifferentiated wall of links, the README splits into 35 categories, and the categories that most awesome-lists skip are the ones that decide whether a platform survives contact with production: cost and governance, data protection and backup, testing and conformance, and diagnostics and troubleshooting all get their own sections. The scope is honest about what cloud native means now, with AI and machine learning platforms, edge and IoT, and developer workspaces sitting alongside the usual orchestration and networking categories, which reflects an ecosystem that grew past the Kubernetes monoculture. Every entry is a GitHub link plus one line of description, so it works as a discovery index and a reading list at the same time, and the whole thing is a markdown file you can clone and grep, which is a better search experience than most directories. There is a maintained companion site at awesome.jimmysong.io with a project status board showing 544 active, 98 archived, 16 deleted and 135 inactive projects, which is more honesty than most lists manage, and the repo is still being updated daily, with entries added through pull requests in the last week. The caveats are real. Entries are one-line descriptions with no stars, no license and no maintenance signal, so a 2021 project and a 2026 one look identical. The status board exists precisely because the README does not carry that information, and 98 archived plus 16 dead repos out of 793 tracked means the list carries dead weight unless you check. A list is only as current as its last merge, and with 810 entries across 35 categories, curation is a losing battle against project churn. Verdict for Wojtek: keep it bookmarked as the vocabulary reference, not as a shortlist, because the day you need to know what a category is called is the day you need to grep this file, and the 35-way taxonomy is the part that is genuinely hard to reproduce.


## 22. An open-source AI agent that mixes Claude Code and Codex mid-task — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/makecindy/cindy)

**Source:** https://www.opensourceprojects.dev/post/72234a8e-5561-4b49-ac66-3a4198bfd4ef
**Karakeep doc:** `r9cgoajumlvwhkz29hiex6vg`
**Project:** [Cindy](https://github.com/makecindy/cindy) — Local-first open-source AI agent that switches between Claude Code and Codex mid-task (Apache-2.0, TypeScript)

Cindy is an open-source agent that lets you swap between Claude Code and Codex in the middle of a task, keeping one workspace, one memory and one set of tools while the model underneath changes. The repo is makecindy/cindy, 3,243 stars, TypeScript, Apache-2.0, last pushed 2026-10-22. It runs on your own machine against your real files and your logged-in apps. The client is an Electron desktop app plus an Expo/React Native mobile app in a pnpm monorepo with shared packages for auth, device linking, agent orchestration and model providers. The backend service lives in a separate repository and is not part of the monorepo, so what you can audit is the client and not the part that routes the work. Node 22.x and pnpm 10 are the requirements. One task can be planned by one model, executed in parallel by another and reviewed by a third, across different model and CLI combinations, with no context lost at the switch. Billing stays yours: sign in to the official service, authorise the Claude Code or Codex plan you already pay for, plug in your own API keys, or run local models. Memory, skills and MCP tools are shared across both, so you correct it once and it remembers, teach a skill once and it works everywhere, and scheduled recurring jobs report back on their own. The README also claims it can drive your browser, your computer and your phone and pull work from IM, which is a lot of access to hand a tool that mixes vendors. Plugins, team skill sharing and a native agent are roadmap, not shipped, so treat the open source claim as changeable client code rather than a self-hosted stack. Packaging is tidy. The claude-code, codex and ripgrep binaries are fetched per platform during pnpm install, and the Android platform-tools are pinned with sha256 verification. Prebuilt builds are on cindy.app/download, with a Linux guide covering Ubuntu, Arch and Omarchy. The honest caveat is the second half of that deal, where authorising your existing plan into a third-party service hands someone else's agent your keys, and whether that traffic flows through their backend is not something the Apache-2.0 client answers. Wojtek cares because multi-model orchestration is the actual ask in most agent threads, and this one lets you keep the subscriptions you already have.

## 23. A torrent finder in your terminal with nothing to configure — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/baairon/torlink)

**Source:** https://www.opensourceprojects.dev/post/dbeaf395-119d-4cb9-94eb-33e92f97fb65
**Karakeep doc:** `mg4md466onz4c43ych1eh2rj`
**Project:** [torlink](https://github.com/baairon/torlink) — TypeScript TUI torrent finder and downloader with zero configuration (MIT)

torlink is a terminal torrent finder with a deliberately tiny surface. One npm package, a curated list of indexers, and a TUI you drive entirely with keystrokes. It ships as `npx torlnk`, note the swapped letters, the repo is torlink but the npm package is torlnk, so `npx torlink` gets you nothing. The source list is short and opinionated. FitGirl alone for games, because games are the one category that can execute code, and YTS, The Pirate Bay, 1337x and BitTorrented for movies and TV, EZTV, Nyaa and SubsPlease for anime. Results stream in from every source with size and seeder count, and if one source is down the search carries on and tells you which one died. It handles magnet links, bare infohashes, dragged .torrent files, and can browse a curated library on an empty query, and it drops a playlist.m3u into any folder holding more than one video or track unless you pass --no-playlist. Downloads run in the background, survive being interrupted, and keep seeding when they finish, with a Seeding tab and a `p` key to stop. For seedboxes there is a headless mode. JSON search output, `seed`, `watch` a folder, `serve` magnets over HTTP, `files` to stream finished downloads, `attach` to keep the TUI alive across SSH, and a --daemon flag for staying up after logout. The GitHub numbers are 5,940 stars, 390 forks, 5 open issues, MIT, TypeScript, created 2026-06-25, last push 2026-10-15. The caveats are the ones the cheerful README skips. It breaks the moment an indexer changes its HTML, it is not a full client, so no private trackers, no ratio maths and no RSS, and auto-seeding by default is a legal exposure that a privacy section about nothing routing through a central server does not really address. The verdict is that it is fun, tiny, does one job well, and it will outlive the web by about as long as 1337x keeps its layout.

## 24. Open source password manager for Nextcloud where vault keys never touch the serv... — by Open-source Projects

![Open-source Projects](https://opengraph.githubassets.com/1/nextcloud/passman)

**Source:** https://www.opensourceprojects.dev/post/6dff30dd-fddb-4ccb-926f-8f6737b9df39
**Karakeep doc:** `kmbhzduq9mkjvkg4ot6bk5ls`
**Project:** [Passman](https://github.com/nextcloud/passman) — Nextcloud app password manager that keeps vault keys client-side, 256-bit AES, AGPL-3.0, 825 stars

Passman is a password manager that runs as a Nextcloud app, and its whole pitch is that the vault key never goes to the server: credentials are encrypted with 256-bit AES client-side, so the server stores ciphertext nobody can read. That is the correct instinct, and the feature list is respectable for a side project. Multiple vaults, user-defined custom credential fields, a built-in OTP generator, a password analyzer, sharing inside the instance or via link, and experimental importers for KeePass, LastPass, Dashlane, ZOHO, Clipperz.is, EnPass and ocPasswords, which matters if you are migrating a decade of logins instead of retyping them. There is a rewritten browser extension for Chrome and Firefox and a native Android app on Google Play, IzzyOnDroid and F-Droid. The repo is nextcloud/passman, JavaScript, AGPL-3.0, 825 stars, and it was pushed to within hours of this post, so it is alive rather than a screenshot. The catch the post mentions in passing and then forgets: the README's security section is truncated, so read it in full before you put real credentials in it. The bigger catch is architectural. "The server never sees your keys" protects you from a curious sysadmin, not from someone who owns the box. Anyone who can patch the Nextcloud PHP, hook the app, or slip code into the extension walks away with the decrypted vault, and a Nextcloud instance exposed to the internet is a large, frequently-patched attack surface that now holds your master credentials. Autofill also depends on that extension, so the browser half of the security story is a browser add-on. Verdict: a good fit if you already run Nextcloud and treat it as trusted infrastructure, a bad idea if you adopted Nextcloud just to host your passwords, in which case KeePassXC plus Syncthing still wins on blast radius.

### LinuxLinks (RSS)

## 25. rulc - terminal calculator with mathematical plotting - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/01/035-calculator.png)

**Source:** https://www.linuxlinks.com/rulc-terminal-calculator-mathematical-plotting/
**Karakeep doc:** `u3bfbjjkxaez114ccgrpbdgf`
**Project:** [rulc](https://github.com/imizgun/rulc) — Rust terminal calculator with a TUI that plots functions and finds their intersections

LinuxLinks profiled rulc, a Rust terminal calculator that plots functions inside the TUI instead of sending you to a graphing calculator on another machine. It gives you three ways in. A REPL evaluates expressions as you type, a full text user interface handles the graphs, and one-shot expression evaluation drops into shell scripts over stdin. The maths covers arithmetic and exponentiation, trigonometry and inverse trigonometry, logarithms, square roots and rounding, with pi and Euler's number available as constants. You can define variables, do compound assignment, and write your own functions in expression syntax. The plotting part is the reason to look. Ranges are set with numerical expressions, up to five curves share one graph in separate colours, and the axes rescale to fit whatever you plotted. It also finds intersections between two functions by numerical sampling and interpolation, prints the coordinates, and marks the crossing points on the graph. Undefined values and extreme spikes near asymptotes get filtered instead of wrecking the render, and there are commands to clear variables, functions, plots and history. It is GPLv3, written in Rust, and lives at github.com/imizgun/rulc. Compared with the usual crowd on LinuxLinks' own calculator roundup (qalc, kalker, Numbat, bc, calc) it trades away symbolic algebra and unit handling in exchange for graphs, so if you wanted exact decimals or dimensional analysis this is the wrong tool. The intersection finder samples numerically, so a tangent or a near-miss crossing may simply refuse to show up. GPLv3 also makes it a nuisance to embed in anything closed-source. Worth a look for anyone who lives on a remote box and plots things in ASCII.

## 26. edamame - terminal Markdown editor with live rendering - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/09/Markdown-logo.png)

**Source:** https://www.linuxlinks.com/edamame-terminal-markdown-editor-live-rendering/
**Karakeep doc:** `oka07s84mchvxdeykkqfsb2o`
**Project:** [edamame](https://github.com/mijowi/edamame) — Rust terminal Markdown editor that stays rendered while you edit

edamame is a Rust terminal Markdown editor that keeps the whole document rendered and only exposes the raw syntax on the line you are editing. The LinuxLinks post is a feature list rather than a review, but the list is unusually specific. Tables render as grids with individually editable cells, you get row and column operations plus mouse resizing, and inline images, Mermaid diagrams and LaTeX show up in terminals that can handle them. The editor adapts its display to what the terminal actually supports, which is the right call, since inline images in an 80x24 xterm are a punchline. Editing bits include search and replace with smartcase matching, optional Vim mode with motions, operators and text objects, a fuzzy command palette, jump-to-heading, automatic list continuation and renumbering, 27 built-in colour themes, and HTML export. It also reviews changes made by files outside the editor and lets you accept or reject each one individually, which matters more than it sounds when some script is rewriting your notes underneath you. Apache 2.0, Linux and macOS only, and the repo shows 94 stars, 3 forks and 14 open issues on a project created in April 2026, so this is very young. The obvious counterpoint is that a rendered editor in a terminal fights its own medium. Cell-level edits and mouse resizing are GUI habits bolted onto a text buffer, and for a long document plain nvim with a Markdown plugin, or Mark Text or Zettlr on the desktop, still wins. What tips it slightly in favour is that 94 stars in six months says terminal people are starved for anything that is not a pager. The verdict is that it is worth 20 minutes of curiosity and not worth migrating your notes. 🙂

## 27. 3 Best Free and Open Source Scientific Workflow and Job Management Tools — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/09/Chemistry-Workflow-banner.png)

**Source:** https://www.linuxlinks.com/best-free-open-source-scientific-workflow-job-management-tools/
**Karakeep doc:** `rk7k773kxmg06cnfp30tx9q6`

LinuxLinks picked three tools for people who run real simulations instead of writing shell scripts by hand, and the shortlist is deliberately small: quacc, pyiron_atomistics and MoleQueue. The page draws a useful line between a scientific workflow, which fixes the order of tasks and the data moving between them, and job management, which is only about submitting, monitoring and collecting results. The workflow layer is quacc, a Python framework from the Rosen Research Group at Princeton that wraps quantum chemistry and materials-science calculations in recipes and dispatches them to a workstation, an HPC cluster, the cloud or any mix of those. It sits on the Atomic Simulation Environment and the Materials Project ecosystem, and it refuses to impose one workflow engine, which matters on a day when your laptop and your cluster queue disagree. The heavier, older option is pyiron_atomistics from the Max Planck Institute for Sustainable Materials, also Python, with LAMMPS and VASP interfaces and HDF5 or SQL storage for calculation provenance. It drags in the whole pyiron ecosystem whether you want it or not, and it carries 148 open issues against quacc's 14. MoleQueue is the odd one out, a C++/Qt desktop app from Kitware and the Open Chemistry project. It submits to SGE, PBS and SLURM over SSH, stages input files, tracks queued, running, completed and failed jobs, and exposes JSON-RPC 2.0 over local sockets plus ZeroMQ for Python. It is also the one with a sleepy repository, last pushed to GitHub in May 2026, while quacc got commits yesterday. The article itself is a portal page with a ratings chart and one-line descriptions, so there are no benchmarks and no analysis here. Start with quacc, poke MoleQueue if you genuinely live on a cluster, and treat the ratings chart as decorative wallpaper.

**Projects:**

- **[quacc](https://github.com/Quantum-Accelerators/quacc)** — quacc - automate quantum chemistry and materials science workflows - LinuxLinks.
- **[pyiron_atomistics](https://github.com/pyiron/pyiron_atomistics)** — pyiron_atomistics - atomistic simulation and workflow environment - LinuxLinks.
- **[MoleQueue](https://github.com/OpenChemistry/molequeue)** — MoleQueue - manage local and remote computing jobs - LinuxLinks.

## 28. Warpgate - transparent bastion for secure infrastructure access - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/11/028-distribution-network.png)

**Source:** https://www.linuxlinks.com/warpgate-transparent-bastion-secure-infrastructure-access/
**Karakeep doc:** `cckapju6ajwmp7ca8otlsd2i`

**Project:** [Warpgate](https://github.com/warp-tech/warpgate) — Rust bastion host fronting SSH, HTTPS, Kubernetes, MySQL, PostgreSQL, RDP and VNC

Warpgate is a self-hosted bastion host written in Rust, and the pitch is that nobody on your side has to change how they connect. SSH, HTTPS, Kubernetes, MySQL, PostgreSQL, RDP and VNC go through one gateway while the client stays vanilla, and the twist is that it is protocol-aware rather than a plain jump box: an admin hands a user one specific destination, so the contractor gets exactly one database instead of the whole subnet. Sessions get recorded for playback, and a browser-based SSH terminal plus RDP and VNC viewers cover the cases where the far end has no client installed.

Two-factor is TOTP, SSO is OpenID Connect, and command-level auditing sits on top. It brute-force protects itself with IP blocking and account lockout, temporary access tickets let you grant time-boxed access, state lives in SQLite, and it ships as a single Rust binary with no runtime dependencies. Apache 2.0, maintained by Eugene Pankov; the repo sits at 8.1k stars and 424 forks, with v0.30.0 released on 19 October 2026.

That 0.x version is the tell: expect config churn and bet on a young project. Every session that goes through the gateway is a recording you now own, including who typed what into a production database, and IP blocking will one day lock out your entire office behind a single NAT address, which you will enjoy explaining in a support call. It also has to live in your DMZ, which makes it a famous, well-funded target.

Teleport and a plain OpenSSH jump box are the competition: Warpgate wins on transparency and loses on ecosystem and scale. Worth it for contractor access with a trail; overkill if a jump host and a text file would do.

## 29. 100 Great Free and Open Source GUI Applications for Linux - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2026/10/linux-gui-apps-banner-700x350-1.png)

**Source:** https://www.linuxlinks.com/100-great-gui-applications-linux/
**Karakeep doc:** `kydtu9wh37tpzxjfsj8mvymw`

LinuxLinks dumped a hundred GUI applications into one list and made a point of saying it is a selection, not a ranking, with a poll asking how many of them you actually use. The editorial rule is clean: only free and open source software qualifies, and where a project also ships a commercial edition, the open source one is the one that got in. Each entry lists website, developer and license, which quietly turns a link dump into a reference table.

The spread is wide: GIMP, Inkscape, Krita, darktable and RawTherapee cover graphics; Ardour, Audacity, Rosegarden, MusE, Surge XT and fooyin cover audio. The odd corners are the interesting part, with QDirStat, Photini, Qalculate!, Zeal, Shortwave, Déjà Dup, Scilab, fre:ac and Zim all earning a slot. Half the list is what you already have installed, including Firefox, VLC, Thunderbird, VirtualBox, Blender and OBS Studio. The other half is the actual argument, which is that a Linux desktop in 2026 has more than enough choice for anything you would want.

Quality control here is per entry and uneven. Konversation is an IRC client, DVDStyler still authors DVDs, and Heroic and DBeaver Community are community editions of commercial products. The license column also does real work, since Cura is LGPL while GIMP and Blender are GPL. The poll is cute and will be forgotten by Friday.

Keep it open on a boring Saturday: two or three entries will be new to you, and fooyin, Photini and QDirStat are the ones to try first.

**Projects:**

- **ONLYOFFICE Desktop Editors** — _no verified public repo found_
- **[Thunderbird](https://www.thunderbird.net/)** — Full-featured open-source mail client (the one lightweight clients are measured against).
- **[Firefox](https://github.com/mozilla-firefox/firefox)** — Mozilla Firefox (9to5Linux roundup 2026-09-27).
- **[GIMP](https://www.gimp.org/)** — GNU Image Manipulation Program — raster image editor.
- **[Wireshark](https://www.wireshark.org/)** — The world's foremost network protocol analyzer.
- **[Inkscape](https://github.com/inkscape/inkscape)** — Project Website: https://inkscape.org - Code Repository: https://gitlab.com/inkscape/inkscape - Draw freely. 🖌.
- **[Kodi](https://github.com/xbmc/xbmc)** — Kodi is an award-winning free and open source home theater / media center software.
- **[OBS Studio](https://github.com/obsproject/obs-studio)** — OBS Studio (9to5Linux roundup 2026-09-27).
- **[VirtualBox](https://www.virtualbox.org/)** — VirtualBox (9to5Linux roundup 2026-09-27).
- **[RStudio](https://github.com/rstudio/rstudio)** — RStudio is an integrated development environment (IDE) for R.
- **[Stellarium](https://github.com/Stellarium/stellarium)** — Stellarium is a free GPL software which renders realistic skies in real time with OpenGL. It is available for Linux/Unix, Windows, macOS and Haiku....
- **[Blender](https://www.blender.org/)** — The Freedom to Create.
- **[VLC](https://github.com/videolan/vlc)** — VLC (9to5Linux roundup 2026-09-27).
- **[Ardour](https://github.com/Ardour/ardour)** — Mirror of Ardour Source Code.
- **Gaia Sky** — _no verified public repo found_
- **[Audacity](https://github.com/audacity/audacity)** — Audio Editor.
- **[fooyin](https://github.com/fooyin/fooyin)** — A customisable music player.
- **[Cura](https://github.com/Ultimaker/Cura)** — 3D printer / slicing GUI built on top of the Uranium framework.
- **[darktable](https://github.com/darktable-org/darktable)** — darktable is an open source photography workflow application and raw developer.
- **[FreeCAD](https://www.freecad.org/)** — FreeCAD, the open source 3D parametric modeler.
- **[BleachBit](https://github.com/bleachbit/bleachbit)** — BleachBit system cleaner for Windows and Linux.
- **[feh](https://github.com/derf/feh)** — a fast and light image viewer.
- **[digiKam](https://github.com/KDE/digikam)** — Advanced KDE photo management suite with tagging, RAW support and batch processing.
- **[Foliate](https://github.com/johnfactotum/foliate)** — Read e-books in style.
- **[Element](https://github.com/element-hq/element-web)** — A glossy Matrix collaboration client for the web.
- **[GParted](https://github.com/GNOME/gparted)** — Read-only mirror of https://gitlab.gnome.org/GNOME/gparted.
- **[FileZilla](https://github.com/basvodde/filezilla)** — Clone from https://svn.filezilla-project.org/svn/FileZilla3/trunk.
- **[Spectacle](https://apps.kde.org/spectacle/)** — KDE's screen capture utility for Linux.
- **PDF Arranger** — _no verified public repo found_
- **Surge XT** — _no verified public repo found_
- **[Kdenlive](https://kdenlive.org/en/)** — Non-linear video editor for KDE.
- **[GnuCash](https://github.com/Gnucash/gnucash)** — GnuCash (9to5Linux roundup 2026-09-27).
- **[KeePassXC](https://github.com/keepassxreboot/keepassxc)** — KeePassXC (9to5Linux roundup 2026-09-27).
- **[Heroic Games Launcher](https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher)** — A games launcher for GOG, Amazon and Epic Games for Linux, Windows and macOS.
- **[Okular](https://github.com/KDE/okular)** — KDE document viewer.
- **Mattermost Desktop** — _no verified public repo found_
- **[Konversation](https://github.com/KDE/konversation)** — User-friendly and fully-featured IRC client.
- **[HandBrake](https://github.com/HandBrake/HandBrake)** — HandBrake's development repository.
- **[Krusader](https://github.com/KDE/krusader)** — Advanced twin panel (commander style) file manager.
- **[CopyQ](https://github.com/hluk/CopyQ)** — Clipboard manager with advanced features.
- **[Lutris](https://github.com/lutris/lutris)** — Lutris desktop client.
- **[Qalculate!](https://github.com/Qalculate/libqalculate)** — Qalculate! library and CLI.
- **[Spyder](https://github.com/spyder-ide/spyder)** — Official repository for Spyder - The Scientific Python Development Environment.
- **[MusE](https://muse-sequencer.github.io/)** — MusE is a digital audio workstation with support for both Audio and MIDI.
- **[calibre](https://github.com/kovidgoyal/calibre)** — The official source code repository for the calibre ebook manager.
- **[Krita](https://github.com/KDE/krita)** — Professional free raster painting and animation studio.
- **[Joplin](https://github.com/laurent22/joplin)** — Joplin - the privacy-focused note taking app with sync capabilities for Windows, macOS, Linux, Android and iOS.
- **[Tabby](https://github.com/Eugeny/tabby)** — A terminal for a more modern age.
- **[draw.io Desktop](https://github.com/jgraph/drawio-desktop)** — Official electron build of draw.io.
- **[Photini](https://github.com/jim-easterbrook/Photini)** — Easy-to-use digital photo metadata editor (Python, exiv2/GExiv2 backend).
- **[MusicBrainz Picard](https://picard.musicbrainz.org/)** — Cross-platform music tagger powered by the MusicBrainz database.
- **[QCAD Community Edition](https://qcad.org/en/)** — QCAD is a free, open source 2D CAD system for Windows, Linux and Mac.
- **[Ulauncher](https://github.com/Ulauncher/Ulauncher)** — Feature-rich application launcher for Linux.
- **QDirStat** — _no verified public repo found_
- **[RawTherapee](https://github.com/RawTherapee/RawTherapee)** — A powerful cross-platform raw photo processing program.
- **[PSPP](https://www.gnu.org/software/pspp/)** — GNU PSPP — free replacement for IBM SPSS, for sampling and statistical analysis.
- **[Shortwave](https://github.com/maunalinux/shortwave)** — Find and listen to internet radio stations.
- **Déjà Dup** — _no verified public repo found_
- **[Rosegarden](https://github.com/tedfelix/rosegarden-official)** — MIDI Sequencer for Linux.
- **[Scilab](https://github.com/scilab/scilab)** — Read only copy of https://gitlab.com/scilab/scilab.
- **[Scribus](https://github.com/scribusproject/scribus)** — Community mirror of the official Scribus SVN svn://scribus.net. Please submit PRs & Bugs to https://bugs.scribus.net .
- **[Gramps](https://github.com/gramps-project/gramps)** — Source code for Gramps Genealogical program.
- **[Cryptomator](https://github.com/cryptomator/cryptomator)** — Cryptomator for Windows, macOS, and Linux: Secure client-side encryption for your cloud storage, ensuring privacy and control over your data.
- **[Kasts](https://github.com/KDE/kasts)** — Kirigami-based podcast player.
- **[VSCodium](https://github.com/VSCodium/vscodium)** — binary releases of VS Code without MS branding/telemetry/licensing.
- **[KiCad](https://www.kicad.org/)** — A Cross Platform and Open Source PCB Design Suite.
- **[PeaZip](https://github.com/peazip/PeaZip)** — PeaZip (9to5Linux roundup 2026-09-27).
- **[ProjectLibre](https://github.com/smartqubit/projectlibre)** — The Open Source replacement of Microsoft Project.
- **[GNU Octave](https://github.com/gnu-octave/octave)** — GNU Octave Mirror (https://www.octave.org/hg/octave). Report bugs and submit pull requests (patches) at https://bugs.octave.org.
- **[Arduino IDE](https://github.com/arduino/Arduino)** — Arduino IDE 1.x.
- **[Zeal](https://github.com/zealdocs/zeal)** — Offline documentation browser. Your personal reference library, searchable in an instant.
- **[Nextcloud Desktop](https://github.com/nextcloud/server)** — Self-hosted file sync, share, and collaboration platform.
- **[RustDesk](https://github.com/rustdesk/rustdesk)** — An open-source remote desktop application designed for self-hosting, as an alternative to TeamViewer.
- **Synfig Studio** — _no verified public repo found_
- **[Telegram Desktop](https://github.com/telegramdesktop/tdesktop)** — Telegram Desktop messaging app.
- **[FocusWriter](https://github.com/gottcode/focuswriter)** — Simple fullscreen word processor.
- **[TeXstudio](https://github.com/texstudio-org/texstudio)** — Full-featured cross-platform LaTeX editor with built-in PDF viewer and reference browser.
- **[Timeshift](https://github.com/teejee2008/timeshift)** — System restore tool for Linux. Creates filesystem snapshots using rsync+hardlinks, or BTRFS snapshots. Supports scheduled snapshots, multiple backu...
- **[QGIS](https://github.com/qgis/QGIS)** — QGIS is a free, open source, cross platform (lin/win/mac) geographical information system (GIS).
- **[dupeGuru](https://github.com/arsenetar/dupeguru)** — Find duplicate files.
- **[KDE Connect](https://github.com/KDE/kdeconnect-kde)** — Multi-platform app that allows your devices to communicate.
- **[Godot](https://github.com/godotengine/godot)** — Godot Engine – Multi-platform 2D and 3D game engine.
- **[Signal Desktop](https://github.com/signalapp/Signal-Desktop)** — A private messenger for Windows, macOS, and Linux.
- **[Resources](https://github.com/nokyan/resources)** — GNOME app that keeps an eye on system resources.
- **[Webcamoid](https://github.com/webcamoid/webcamoid)** — Webcamoid is a full featured and multiplatform camera suite.
- **[Sonic Visualiser](https://github.com/sonic-visualiser/sonic-visualiser)** — Visualisation, analysis, and annotation of music audio recordings.
- **[Zotero](https://github.com/zotero/zotero)** — Zotero is a free, easy-to-use tool to help you collect, organize, annotate, cite, and share your research sources.
- **[Zim Desktop Wiki](https://github.com/zim-desktop-wiki/zim-desktop-wiki)** — Main repository of the zim desktop wiki project.
- **[Mandelbulber](https://github.com/buddhi1980/mandelbulber2)** — Official repository for Mandelbulber v2.
- **[gretl](https://gretl.sourceforge.net/)** — GNU gretl — econometrics and time-series analysis package.
- **[3D Slicer](https://www.slicer.org/)** — 3D Slicer image computing platform for medical visualization and image computing.
- **[Remmina](https://github.com/FreeRDP/Remmina)** — Mirror of https://gitlab.com/Remmina/Remmina The GTK+ Remmina Remote Desktop Client.
- **[NewsFlash](https://gitlab.com/news-flash/news_flash_gtk)** — Modern GTK RSS feed reader for Linux.
- **[DVDStyler](https://www.dvdstyler.org/)** — DVDStyler - Free DVD Authoring Application.
- **DBeaver Community** — _no verified public repo found_
- **[KMyMoney](https://github.com/KDE/kmymoney)** — Personal finance manager.
- **[LocalSend](https://github.com/localsend/localsend)** — An open-source cross-platform alternative to AirDrop.
- **[LyX](https://www.lyx.org/)** — What-you-see-is-what-you-mean document processor — a graphical front-end to LaTeX.
- **[fre:ac](https://github.com/enzo1982/freac)** — The fre:ac audio converter project.
- **[Gajim](https://github.com/gajim/gajim)** — Mirror.

## 30. Moonlight Qt - stream games and applications from another computer - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2018/10/RemoteDisplay.jpg)

**Source:** https://www.linuxlinks.com/moonlight-qt-stream-games-applications/
**Karakeep doc:** `jr07mknm6qo3eindjt7qyico`
**Project:** [Moonlight Qt](https://github.com/moonlight-stream/moonlight-qt) — Open source GameStream client for streaming games and apps from a Sunshine host

LinuxLinks' writeup of Moonlight Qt is really a writeup of the idea that your games machine can live in another room. Moonlight is the open source GameStream client, C++ and Qt, GPLv3, 19.2k stars, 1.5k forks and 3,400 commits, and it needs a host: Sunshine, which runs on Linux, Windows and macOS, does the encoding and keeps the workload, while Moonlight sends back keyboard, mouse and controller input. The feature list is the interesting part, because it reaches far past gaming: hardware accelerated decode through VA-API, VDPAU and Vulkan Video, H.264, HEVC and AV1, HDR, 7.1 surround sound, up to 16 gamepads with force feedback and motion controls, 10-point multitouch, pointer capture for games versus direct mouse control for remote desktop, and system-wide shortcuts like Alt+Tab passed to the host. YUV 4:4:4 works with Sunshine only, and AV1 needs a compatible Sunshine host with a supported GPU. LinuxLinks frames it as gaming on weak hardware, but the remote desktop use is the real payoff: heavy GUI apps on a beefier box, or a machine you reach over the internet. Packaging is unusually complete for a Linux client, with Snap, Flatpak, AppImage, Raspberry Pi 4 and 5 images, ARM 32/64-bit debs, experimental RISC-V debs and Jetson plus Switch builds. Building from source wants Qt 6.11 or newer, Visual Studio 2026 and MSVC, because MinGW is not supported, which is one more argument for grabbing the Flatpak instead. The catch nobody mentions: Moonlight is only the client half of a two-project system, so every Sunshine encoder bug is your bug too, and latency still depends on your network being kind. Sunshine is the piece people forget, since Moonlight on its own just decodes a stream somebody else has to produce. The verdict lands like this: Moonlight is a much nicer way to play a game sitting in the other room, or to sit at the desk of a rig that can actually run the thing. Set the bitrate and resolution you want, point it at a Sunshine host, and stop thinking about it.

## 31. ZacOS 9 - Debian-based Linux distribution inspired by classic Mac OS - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2024/04/Linux-Distributions.png)

**Source:** https://www.linuxlinks.com/zacos-9-debian-based-linux-distribution/
**Karakeep doc:** `xpqp0te5stucjoizfu5mlm3e`
**Project:** [ZacOS 9](https://sourceforge.net/projects/zac-os-9) — a Debian-based Linux distribution that rebuilds the classic Mac OS 8/9 Platinum desktop from scratch

ZacOS 9 is a Debian-based distribution that rebuilds the classic Mac OS 8 and 9 Platinum desktop from scratch, and it is not a theme. The Wayland compositor, the window manager, the Sniffer file browser, the menu bar and every control panel were written for the project, down to the scroll arrows, so the behaviour matches the look instead of being skin over someone else's desktop. It also runs old Macintosh software through SheepShaver emulation, and the ChromaSystem build adds read-only mounting of HFS, HFS+ and APFS volumes plus Disk Copy, DMG, sparseimage and sparsebundle images, with FileVault and some APFS features explicitly unsupported. The version history on SourceForge is the real story. Sixty-odd 0.1.x releases in six weeks turned a skin into a desktop: the Collar control strip, a Picture Viewer, a Keychain module so apps like ChatGPT can open, RustDesk and RDP sharing through WayVNC, an Apple menu that actually looks like an Apple menu, a Finder that does aliases and network mounts, and a login window in Platinum instead of a text prompt. Then v1.0.0 shipped on 19 October 2026 as a 3.0 GB bootable ISO, amd64 only, with a published SHA256 and 150 downloads in its first week. The caveats are honest because the author keeps saying them out loud: APFS mounting is still read-only, physical-disk mounting still needs hardware verification, custom-renamed APFS helper volumes cannot be identified automatically, and the RustDesk video path has not been verified end to end. It is also not affiliated with Apple, which is why the boot logo is a happy boot face rather than a bitten apple. A nostalgia project with a 2.99 GB download and a beta-quality disk subsystem has no business in a server room. For anyone who wants a period-correct desktop on a current Debian base, though, this is further along than any of the other Mac OS clones. Verdict for Wojtek: a weekend project, not infrastructure, and the SheepShaver route to old Mac software is the feature that makes it more than a screenshot.

## 32. 25 Best Free and Open Source Audio Analyzers - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2021/09/image-multitrack-sound-audio-wave-monitor-recording-mixing-mastering-studio2.jpg)

**Source:** https://www.linuxlinks.com/best-free-open-source-audio-analyzers/
**Karakeep doc:** `xkeat7i27fkpq33p433us0on`

LinuxLinks rounded up 25 free and open source audio analyzers for Linux, with the usual ratings chart serving as the verdict. The scope is audio spectrum visualisation for live and recorded signals, mostly in FFT spectrum, 2D spectrogram and octave spectrum modes, and several tools also cover amplitude and phase. The stated use cases are the serious ones: reading a signal's fundamental frequency, harmonics and feedback, describing room and receiver behaviour such as reverberation and gain peaks, and driving room equalisation preprocessing. The list also folds in song identification, so Shazam clones share a table with measurement tools. The heavy hitters are Sonic Visualiser for viewing and analysing music files, Friture for real-time analysis, MasVisGtk and AudMeS for measurement through a sound card, and Open Sound Meter for tuning sound systems in real time. On the visualiser side projectM carries the Milkdrop lineage, Cava is the cross-platform favourite, and Cava's forks Cavalier and Cavasik appear as separate entries, which tells you more about Linux software than any review could. SongRec, Mousai and Music Radar are the three song ID apps, Spek and Spek-rs are near-duplicates splitting the same acoustic spectrum job, Wolf Spectrum is a realtime spectrogram plugin for monitoring and production, Beskope is PipeWire-native, and spectroterm does it in a terminal with curses. The title says 25 and the table lists 25, so no bait and switch. The honest caveat is that several entries are music visualisers that look lovely and measure nothing, and a couple of the tools are old enough that PipeWire users should check the last commit before trusting them. LinuxLinks rates these on its own scale, which is a popularity poll with screenshots attached. For Wojtek the interesting ones are the measurement tools, because tuning a PA with a scope in a terminal beats squinting at VU meters.

**Projects:**

- **[Sonic Visualiser](https://www.sonicvisualiser.org/)** — Sonic Visualiser - analyse and annotate audio recordings - LinuxLinks.
- **[Friture](https://github.com/tlecomte/friture)** — Friture - real-time audio analysis and visualisation - LinuxLinks.
- **[Spek](https://github.com/alexkay/spek)** — Spek – acoustic spectrum analyser - LinuxLinks.
- **[projectM](https://github.com/projectM-visualizer/projectm)** — projectM - Cross-platform Music Visualization Library. Open-source and Milkdrop-compatible.
- **[SongRec](https://github.com/marin-m/SongRec)** — An open-source Shazam client for Linux, written in Rust.
- **[Cava](https://github.com/karlstav/cava)** — Cava - terminal and desktop audio visualiser - LinuxLinks.
- **[sndpeek](https://www.gewang.com/software/sndpeek/)** — sndpeek - real-time audio analysis and 3D visualisation - LinuxLinks.
- **[MasVisGtk](https://github.com/itprojects/MasVisGtk)** — MasVisGtk - audio loudness and mastering analysis - LinuxLinks.
- **[Mousai](https://github.com/SeaDve/Mousai)** — Mousai - recognise songs from audio - LinuxLinks.
- **[AudMeS](https://sourceforge.net/projects/audmes/)** — AUDio MEasurement System - audio measurement and signal generation - LinuxLinks.
- **[Cavalier](https://github.com/NickvisionApps/Cavalier)** — Cavalier - customisable audio visualiser - LinuxLinks.
- **[Open Sound Meter](https://github.com/psmokotnin/osm)** — Open Sound Meter - real-time sound system measurement - LinuxLinks.
- **[Le Biniou](https://gitlab.com/lebiniou/lebiniou)** — Le Biniou - music visualisation and VJing tool - LinuxLinks.
- **[Cavasik](https://github.com/TheWisker/Cavasik)** — Cavasik - configurable audio visualiser - LinuxLinks.
- **[Spek-rs](https://github.com/patryk-ku/spek-rs)** — Spek-rs - acoustic spectrum analyser - LinuxLinks.
- **[Soundscope](https://github.com/bananaofhappiness/soundscope)** — Soundscope - terminal audio analysis and loudness metering - LinuxLinks.
- **[Partiels](https://github.com/Ircam-Partiels/Partiels)** — Partiels - audio analysis and feature extraction - LinuxLinks.
- **[rtspeccy](https://movq.de/git/rtspeccy/)** — rtspeccy - real-time audio spectrum analyser - LinuxLinks.
- **[FMIT](https://github.com/gillesdegottex/fmit)** — FMIT - graphical musical instrument tuner - LinuxLinks.
- **[Vibe](https://github.com/TornaxO7/vibe)** — Vibe - Wayland music visualizer and shader player - LinuxLinks.
- **[Wolf Spectrum](https://github.com/wolf-plugins/wolf-spectrum)** — Wolf Spectrum - spectrogram plugin for Linux - LinuxLinks.
- **[OpenMeters](https://github.com/httpsworldview/openmeters)** — OpenMeters - audio metering and visualisation application - LinuxLinks.
- **[Beskope](https://github.com/jturcotte/beskope)** — Beskope - music visualizer for Linux and PipeWire - LinuxLinks.
- **[spectroterm](https://github.com/sparklost/spectroterm)** — spectroterm - terminal audio spectrum analyser - LinuxLinks.
- **[Music Radar](https://github.com/keshavbhatt/music-radar)** — Music Recognition application for Linux Desktop.

## 33. Mitos - modal terminal text editor based on Helix - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2020/08/text-editor-tools.jpg)

**Source:** https://www.linuxlinks.com/mitos-modal-terminal-text-editor/
**Karakeep doc:** `dj0n9cvp93ibssnm0z8qmxqe`
**Project:** [Mitos](https://github.com/mitos-editor/mitos) — a Rust fork of Helix with built-in LSP, debug adapter and tree-sitter support in a terminal UI

Mitos is a Helix fork that keeps the selection-first modal model and bolts IDE features onto it: built-in Language Server Protocol for completion and diagnostics, Debug Adapter Protocol integration, tree-sitter incremental highlighting, all wrapped in a Ratatui terminal UI written in Rust. LinuxLinks sells it as a different approach to editor development, and the repo tells a similar story: forked from Helix at commit f9928f57f with the full upstream history kept, 8,282 commits in, 262 stars, 12 forks, MPL-2.0. Install is a curl script (mitos.computer/install.sh) or a release archive where the binary is `ms` and the `runtime/` directory has to sit next to it, and building from source wants Rust 1.97.1 or newer. The honest caveat is in their README: expect less stability and occasional breaking changes, because the entire point of the fork is moving faster than upstream Helix can. A 262-star fork of a mature editor is a young project, and every upstream Helix release is a merge you avoid, along with the features it ships. There is also an AI policy file that welcomes AI-assisted contributions provided you understand and test what you submit, which is nicer than the usual vibe. The catch nobody states outright: Helix users already have LSP working through their own config, so the real difference is packaging and integration convenience, not capability. For Wojtek it depends on which side of the fence you sit on. If Helix plus a language server already works for you, Mitos is a toy with a nicer onboarding story. If you want an IDE in a terminal and enjoy being early, it deserves 20 minutes. The Ratatui UI and the `ms` binary also mean it drops into a scripted workflow over SSH without an X server, which is exactly where Helix tends to fall short on a headless box.

## 34. 16 Best Free and Open Source Linux Fractal Tools - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2019/02/red-circular-wave-fractal.jpg)

**Source:** https://www.linuxlinks.com/fractaltools/
**Karakeep doc:** `ekc7l9ml48mjk6e6sbyc6hmd`

LinuxLinks put together 16 free and open source fractal tools for Linux, again letting its ratings chart decide the winners. Only free and open source software is eligible for inclusion, so the commercial Fractal Explorer and Apophysis are out of scope. The framing is chaos theory with real-world payoffs, since self-similar geometry shows up in crystals, coastlines, blood vessels, turbulence and river networks, which is a decent excuse to spend a weekend rendering. The list covers every flavour: Mandelbulber v2 for 3D fractals, JWildfire, Qosmic, Fractorium and FLAM3 for cosmic recursive flame editing, XaoS as a real-time zoomer, and Gnofract 4D doing four-dimensional Mandelbrot and Julia sets with interrelations. NextFractal, Fraqtive, FractGen, Fractalshades and fractal-generator cover the standard 2D set, Par Fractal pushes rendering onto the GPU, and Rsfrac is the terminal-based explorer written in Rust. Electric Sheep is in there as a screensaver showing the collective dream of sleeping computers, which is the most Linux sentence in the article. The title says 16 and the table lists 16. The ratings chart is LinuxLinks' own opinion, and the comment thread is a better guide. One reader asked what made the image at the top of the article, the author admitted he was not sure, and four people turned out to be right about which tool it was. So the list itself is solid, the "best" ordering is a vibe, and a few entries (Fractorium, FLAM3) have sat untouched for years. If you want one to try, XaoS or Fractalshades for stills, and Par Fractal if the GPU is otherwise idle and you want to watch a fractal render at 8K.

**Projects:**

- **Mandelbulber v2** — _no verified public repo found_
- **[JWildfire](https://github.com/thargor6/JWildfire)** — JWildfire - powerful and flexible fractal flame editor - LinuxLinks.
- **[Gnofract 4D](https://github.com/fract4d/gnofract4d)** — Gnofract 4D - create and explore fractal images - LinuxLinks.
- **[XaoS](https://xaos-project.github.io/)** — XaoS - real-time interactive fractal zoomer - LinuxLinks.
- **NextFractal** — _no verified public repo found_
- **[Rsfrac](https://github.com/SkwalExe/rsfrac)** — rsfrac - terminal-based fractal explorer - LinuxLinks.
- **[Fraqtive](https://github.com/mimecorg/fraqtive)** — Fraqtive - interactive Mandelbrot family fractal generator - LinuxLinks.
- **[Electric Sheep](https://electricsheep.org/)** — Electric Sheep — crowdsourced evolving fractal art screensaver.
- **[Qosmic](https://github.com/bitsed/qosmic)** — Qosmic - fractal flame editor for FLAM3 - LinuxLinks.
- **[Fractals Explorer](https://github.com/leoraclet/fractals-generator)** — Fractals Explorer - real-time GPU-accelerated fractal explorer - LinuxLinks.
- **[Par Fractal](https://github.com/paulrobello/par-fractal)** — Par Fractal - GPU-accelerated 2D and 3D fractal renderer - LinuxLinks.
- **[Fractorium](https://github.com/mfeemster/fractorium)** — Fractorium - Qt-based fractal flame editor and animator - LinuxLinks.
- **[FractGen](https://github.com/dreibh/fractgen)** — FractGen - extensible fractal generator - LinuxLinks.
- **[Fractalshades](https://github.com/GBillotey/Fractalshades)** — Fractalshades - create static and interactive fractal visualisations - LinuxLinks.
- **[fractal-generator](https://github.com/nicolarevelant/fractal-generator)** — fractal-generator - explore Mandelbrot and Julia fractals - LinuxLinks.
- **[FLAM3](https://github.com/scottdraves/flam3)** — FLAM3 - fractal flame renderer and genetic language - LinuxLinks.

## 35. AuthPass - KeePass-compatible password manager - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/06/006-password.png)

**Source:** https://www.linuxlinks.com/authpass-keepass-compatible-password-manager/
**Karakeep doc:** `p20iv06ccgl0qbsph3ocyypz`
**Project:** [AuthPass](https://github.com/authpass/authpass) — Flutter password manager that reads and writes KeePass KDBX 3.x and 4.x databases

AuthPass is a Flutter password manager built around the KeePass database format, reading and writing KDBX 3.x and 4.x so your existing vaults open without migration. It handles master passwords and key files, ships a password generator with configurable length and character sets, generates TOTP codes and imports them from Google Authenticator exports, and searches across configurable fields. Vaults can live on disk or in Dropbox, Google Drive, OneDrive or WebDAV, with conflict detection so a remote copy does not silently overwrite a newer local one, and the Linux keyring can hold the credentials for those cloud providers. It is written in Dart by Herbert Poul under GPLv3, and the GitHub numbers are respectable for a side project with 2,804 stars, 292 forks and a flat site at authpass.app. The org also ships an Android autofill service and a biometric storage plugin, so somebody is still building in that direction. The catch is that the last push to the main repo was 2026-09-15, and 171 open issues sit behind those 2.8k stars, so this smells like slow maintenance rather than active development. The other gap is browser integration, since the write-up never mentions an extension. The reason people stay on KeePassXC is the extension that fills forms and auto-types into sites, and AuthPass does not have that piece. LinuxLinks lines up a dozen alternatives in the same family, and the ones competing on features rather than simplicity (KeePassXC, Bitwarden, Buttercup) all have a browser story. The verdict is that AuthPass is a solid pick if you want KDBX on desktop and mobile, unexciting if you live in the browser, and worth reading the issue tracker before you migrate your vault into it. 🙂

## 36. 6 Best Free and Open Source Matrix Servers — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2018/06/male-operator-staff-with-team-working-call-center.jpg)

**Source:** https://www.linuxlinks.com/best-free-open-source-matrix-servers/
**Karakeep doc:** `wmg612gibmi1dsganp5bc7xq`

Six Matrix homeservers, and the list quietly tells you the protocol's whole story: three of the six are the same code at different points in its life. Conduit, in Rust under Apache-2.0, is the ancestor everybody started on; upstream it became conduwuit, which got archived, which forked two ways into continuwuity and Tuwunel. Conduit itself is beta, its repo lives on GitLab under famedly, and parts of the protocol are still incomplete. continuwuity is the community continuation, Rust, Apache-2.0, hosted on a Forgejo instance rather than GitHub, and it will migrate a database from conduwuit only, not from Conduit, Synapse or Dendrite. Tuwunel is the rival successor, also Rust and Apache-2.0, 2655 stars, the official conduwuit successor with a real admin API, OAuth2, OIDC, LDAP, JWT, Matrix RTC so Element Call works, and in-place RocksDB migration from Conduit or conduwuit. Synapse is the reference implementation from Element, Python, AGPL-3.0, 4718 stars and 2084 open issues, still what most software assumes. Dendrite, Element's Go rewrite, is in maintenance mode, still beta, missing Simplified Sliding Sync and newer OIDC so Element X clients hurt, last push 17 September. Palpo is the newcomer, Rust on the Salvo framework with PostgreSQL, Complement-tested, 139 stars, built for horizontal scale. The caveats that matter: listing an ancestor right next to two of its descendants is a mess, Dendrite is not a serious choice in 2026, and the page offers a ratings chart where benchmarks should be. Matrix's real problem is clients and bridges, not servers. Synapse if you want compatibility, Tuwunel if you want Rust and less RAM, Palpo if you run PostgreSQL everywhere.

**Projects:**

- **[Synapse](https://github.com/element-hq/synapse)** — Synapse - Matrix homeserver - LinuxLinks.
- **[Tuwunel](https://github.com/matrix-construct/tuwunel)** — Tuwunel - high performance Matrix homeserver - LinuxLinks.
- **[Dendrite](https://github.com/element-hq/dendrite)** — Dendrite - second-generation Matrix homeserver - LinuxLinks.
- **[continuwuity](https://github.com/continuwuity/continuwuity)** — A community-driven Matrix homeserver.
- **[Conduit](https://gitlab.com/famedly/conduit)** — Conduit - lightweight Matrix homeserver - LinuxLinks.
- **[Palpo](https://github.com/palpo-im/palpo)** — Palpo - high-performance Matrix homeserver - LinuxLinks.

## 37. HPN-SSH - high-performance SSH implementation - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/05/049-network.png)

**Source:** https://www.linuxlinks.com/hpn-ssh-high-performance-ssh-implementation/
**Karakeep doc:** `n9fy0asn8j27disl9fjjic63`

**Project:** [HPN-SSH](https://github.com/rapier1/hpn-ssh) — OpenSSH fork tuned for long fat networks, from the Pittsburgh Supercomputing Center

HPN-SSH is a fork of OpenSSH, maintained by Chris Rapier at the Pittsburgh Supercomputing Center, that exists for one reason: moving large data over long, fat links where stock SSH leaves bandwidth on the table. It is BSD 2-clause, written in C, and current at hpn-18.12.0 from 8 October 2026, with 489 stars, 56 forks and 14,747 commits on master. That branch is mid-port to OpenSSH 10.6, which is a detail worth staring at for a moment.

The optimizations are specific: application-level receive buffers are sized to match TCP's, AES-CTR encryption is spread across cores, ChaCha20-Poly1305 runs in parallel, and SCP transfers are resumable because hashes identify what already made it across. Optional Multipath TCP lets one connection ride several paths, on Linux and macOS only, default off, marked experimental since 18.7.0. The client also asks the kernel for TCP_INFO metrics, round-trip time, retransmits, packet loss, polled every five seconds, and falls back from port 2222 to 22 when no hpnsshd is listening. Installs are prefixed with `hpn-` so it sits next to OpenSSH instead of trampling it, and there are PPA and COPR packages for Ubuntu and Fedora.

The caveats are not small. A fork of the most deployed SSH on earth means you own the security-patch merge forever, and the upstream port is not always immediate. The optional NONE cipher, which strips payload encryption after authentication, is a footgun with a warning label, and parallel AES-CTR is not FIPS certified, so it will make RHEL's FIPS mode error out while LibreSSL 3.5 and 3.6 force a fallback to serial AES-CTR. On a LAN or a 100 Mbit line none of this matters; the gains live on high-BDP paths, and SSH2 is being replaced anyway. Install it if you routinely push multi-terabyte datasets between continents, otherwise leave your distro's OpenSSH alone.

## 38. Bridge - PipeWire crossfade mixer and audio router — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/09/021-sound-mixer.png)

**Source:** https://www.linuxlinks.com/bridge-pipewire-crossfade-mixer-audio-router/
**Karakeep doc:** `gzt4objxwjsurcq1fi2he19d`
**Project:** [arulan/bridge](https://github.com/arulan/bridge) — Rust/GTK4 PipeWire crossfade mixer that routes apps to two virtual outputs, GPL-3.0, 55 stars

Bridge is a two-output crossfader for PipeWire and it does one trick very well. Applications get routed to one of two virtual outputs, and a crossfader slides the balance between them, so chat lands on one side and a game on the other. The genuinely useful part is that the routing is persistent. You write pattern-matching rules, and when a matching app starts, Bridge sends its audio to the right output by itself instead of making you redo the arrangement every time you relaunch Discord. It also has output presets you can switch with a global shortcut, a background mode that keeps running with the window closed, and optional headphone virtual surround if you feed it a HeSuVi HRIR file. Written in Rust with GTK4 and libadwaita, GPL-3.0-or-later, 55 stars, zero forks, one open issue, created in June, last commit 1 October, and the flatpak is the easy path: flatpak install --user ./bridge.flatpak. Building from source wants GTK4, libadwaita, PipeWire, Meson 1.1 or newer and rustc 1.96 on edition 2024. The caveats are honest enough. It only crossfades, so it sits next to pwvucontrol instead of replacing it. It is PipeWire only, with no PulseAudio fallback. And a solo maintainer with zero forks and one open issue is a project that can vanish between two flatpak updates. If the Discord-versus-game-rumble fight is your problem, twenty minutes of Flatpak is a fair price. If you actually want mixing, use a real mixer.

## 39. volctl - per-application volume control and OSD - LinuxLinks — by LinuxLinks

![LinuxLinks](https://www.linuxlinks.com/wp-content/uploads/2025/09/047-music-mixer.png)

**Source:** https://www.linuxlinks.com/volctl-per-application-volume-control-osd/
**Karakeep doc:** `kh3nbjjrg2yrhreibvzbrthm`
**Project:** [volctl](https://github.com/buzz/volctl) — Per-application volume control and OSD tray icon for Linux desktops, written in Rust

volctl is a small Rust tray icon that does the one thing PulseAudio mixers make annoying: per-application volume you can actually reach. The author, buzz, wrote it because no existing tray icon gave him multiple application sliders, and the current code is a Rust rewrite of his own Python version, which still lives on a legacy-python branch. It controls master volume and each application separately, shows real application icons and names, gives every app its own VU meter, mutes independently, and takes mouse-wheel input, with an on-screen display for when the tray is out of reach. The OSD is a GTK4 window styled by a plain CSS file at ~/.config/volctl/osd.css that reloads on save, no restart needed, and the whole thing runs on both X11 and Wayland. GPLv3, 97 commits, 159 stars, 18 forks, packaged in the AUR as volctl or volctl-bin, or cargo install straight from git. The catch is the tray host: it needs a StatusNotifierItem implementation, so KDE, Xfce, Cinnamon, MATE, LXQt, GNOME with an extension, or waybar on Hyprland are fine, while dwm and friends need a bridge like snixembed. Without a tray host it still runs, but the mixer popup and preferences live behind the icon that is not there. And the README says outright it is not a pavucontrol replacement, which is fair, because it is a ten-second slider instead of a spreadsheet. Preferences live in GSettings, so the schema has to be installed by hand or the settings will not stick, which is the one genuinely annoying step in the install. For a home lab with three audio apps and one of them always too loud, it is exactly enough. And on Wayland, where every DE now hides its own mixer behind three menus, having the volume wheel on the desktop do the obvious thing is worth the two minutes.

### RSS — Other

## 40. How AT&T is rethinking in-house legal work with OpenAI — by OpenAI News

![OpenAI News](https://openai.com/favicon.ico)

**Source:** https://openai.com/index/att-legal/
**Karakeep doc:** `k0kk6g3xv8j1gcvk6q8525n0`

Another OpenAI customer story, this time with a legal department wearing the straitjacket of its own compliance culture. AT&T's in-house legal team is hundreds of lawyers and legal professionals worldwide, and the friction sits upstream of the lawyering: intake. Before anyone can advise the business they have to assemble the facts, dig out the documents, and locate whatever precedent somebody else established three years ago. The people who hold that precedent are scattered across teams, so the plumbing is the bottleneck. AT&T has a unit for this already, LegalEdge, mixing attorneys, legal professionals, technologists and project managers to push AI into major legal matters, and now that unit is wiring itself to OpenAI. General Counsel David McAtee calls the goal "the plumbing that powers the knowledge layer throughout the company", which is a lot of enterprise poetry for "search our own archives harder". Chief Compliance Officer Bill Ryan is blunter about the first slice: a natural-language intake front door that classifies and prioritises incoming requests, attaches relevant precedent, research and past work, and hands the lawyer a recommended first step. The obvious win is triage speed. The obvious risk is a triage engine that confidently routes a matter to the wrong precedent, and the post says nothing at all about evaluation, citation or hallucination handling. It says nothing else either. No model, no price, no rollout date, no number of matters handled, no measured time saved, no accuracy figure. McAtee's caveat is the one decent line in the piece: "The decision making will always remain with the lawyers." Fair, and also the only sentence that is not marketing. A CTO's plumbing metaphor plus a "Contact sales" button adds up to a pilot announcement with zero measurable payoff, and the same day OpenAI published three more posts, from OpenAI models heading to Google Cloud to coordinated disclosure of critical vulnerabilities. Verdict: plausible, boring and unmeasurable from the outside. Worth watching if a real intake product ships with citation-grade audit trails; if it ships as a chat box, it is a very expensive search box.

## 41. Patch the Planet: global response coordination as agents uncover critical vulnerabilities — by OpenAI News

![OpenAI News](https://openai.com/favicon.ico)

**Source:** https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/
**Karakeep doc:** `wsot38qvk0l2s0w3gihturih`

OpenAI spent two months running a fire drill and now wants everyone else to copy the paperwork. The concrete result is two critical PHP flaws, CVE-2026-109618 (out-of-memory corruption) and CVE-2026-109619 (stale global state surviving across requests), both CVSS 9.2, found by Calif using GPT-5.6 Sol, with Wiz independently reporting both. PHP powers roughly 70% of the web, so a Hello World on an affected runtime was already a target: the researchers demonstrated pre-auth remote code execution on WordPress, Drupal and Joomla, plus application-agnostic memory disclosure that can leak other requests' passwords, tokens, API keys and certificates. Fixes landed in 8.2.35, 8.3.36, 8.4.27 and 8.5.12, and affected releases reach back to PHP 5.4. Then the press release thickens into a proposed five-stage global response: validate and fix upstream, give affected organisations a window to prepare, loop in governments, prepare downstream updates, publish guidance and support deployment. The OpenAI extras are a $1 billion subsidy for Daybreak access aimed at frontline defenders, Codex subscriptions for maintainers, a Rust Foundation platinum sponsorship, and a PHP version checker shipped as a Codex skill. The genuinely useful stuff sits elsewhere in the post: the Defenders' Window, php2shell.com with interim mitigations (memory_limit = -1, lower post_max_size, display_errors = 0, smaller pm.max_requests), and CISA directive BOD-26-04 for prioritising the patch queue. Every finding still goes through a human reviewer and maintainers keep control of their own releases, which is the part of the pitch that actually matters. The uncomfortable bit is the balance OpenAI admits to: the same capability that found these bugs in PHP also shortens an attacker's path, so this is a defender playbook and an offensive toolkit shipped in the same box, with a Google Form asking the security community to grade the premise. Patch first, read the framework second.

## 42. How we built ChatGPT’s novel ad stack for user trust and relevance — by OpenAI News

![OpenAI News](https://openai.com/favicon.ico)

**Source:** https://openai.com/index/building-chatgpt-ad-stack/
**Karakeep doc:** `s5e1epcc3xec3cmidfkt612a`

OpenAI published the internals of its ChatGPT ad stack, and the pitch is that a conversation is not a search query. A user in classic demand-response ads fires one event, the system matches an ad. In ChatGPT intent smears across turns, so the old retrieve-rank-auction pipeline does not fit.

The fix is a separate service running a custom post-trained LLM they call the orchestrator. It reads the conversation, rewrites it into several intent queries, embeds them, and runs approximate-nearest-neighbour retrieval across multiple ad indices, one of them tuned for product reviews, positive and negative. It has to resolve anaphora, tell hypotheticals from shopping intent, and avoid treating every product mention as a purchase request.

Then the usual machinery, driven by that model: eligibility filtering on budget, pacing, locale, policy, placement compatibility and advertiser dedup, then scoring on semantic relevance, predicted engagement and historical performance, then a real auction with admission thresholds, bid computation, quality-adjusted ranking and pricing. The orchestrator only nominates candidates. It never sets the price.

Two ways an ad dies. The orchestrator decides it feels wrong in this conversation, or the request times out because ChatGPT already has its answer ready. ChatGPT never waits for ads, and the ad service shares no code and no model with the answer path, so a broken ad stack cannot delay a reply. Returning no ad counts as success, which is a suspiciously generous thing for an ads team to say out loud.

The rest is plumbing worth stealing: a separate model-written preamble so the ad reads neutrally, server-side delivery tracked apart from actual impressions, and granular logs recording every stage where the flow bailed out. Their strongest models grade the stack and retrain the smaller workers. Humans still set taste through clicks, hides, surveys and Ads Manager feedback.

A year ago this was a few people thinking about the problem. Now it is over $1B in annualised run rate, hit in under 200 days, with more than 100,000 advertisers. Codex gets credited as the force multiplier, complete with guardrails and data infrastructure plugins. Next up: ad formats where you can talk to a business directly, which is a fun sentence to end an ads engineering post on.

Why Wojtek should care: this is the reference implementation for conversational ads, and the hard separation between the ad path and the answer path is the part worth copying and the part worth distrusting.

## 43. Using thousands of AI agents to uncover new leads in biological data — by OpenAI News

![OpenAI News](https://openai.com/favicon.ico)

**Source:** https://openai.com/index/scaling-ai-research-for-complex-biological-data/
**Karakeep doc:** `loe1xon9nmsdwv3y5digdvkx`

OpenAI, PerturbAI and Scripps Research fed a whole-brain CRISPR atlas to thousands of GPT-Rosalind agents and cleared it in 32 minutes, a job their own paper says a human team would need months to a year for. The setup is deliberately dumb and parallel: one agent per gene disruption, each one reading the cellular response, digging through literature and proposing a mechanism, with the reports merged into a reasoning atlas that is now public on GitHub. Two leads get the press. Tsc1 and Tsc2, the twin mTOR regulators, behave alike in most neuron types but diverge sharply in the cerebellum, where Tsc2 disruption rewires dozens of neuronal communication genes, and cerebellar abnormality is strongly tied to TSC2 mutations in tuberous sclerosis. Then DCTN1, whose mutations cause Perry syndrome, turned up as raising cholesterol-synthesis genes, which the agents tied to the idea that broken cholesterol transport makes neurons crank out more cholesterol. Now the fine print. Every lead is a hypothesis in mouse tissue, nothing was validated in a lab, and "novel, consequential and worth following up" is what a friendly blinded panel says when an idea sounds plausible. The 75% preference for distributed over single-agent reports is about writing quality and says nothing about truth, and "the agents reproduced findings from human analyses" hides how much of the work was literature cross-referencing. It is also a launch post for GPT-Rosalind, so the demo doubles as product marketing with a biorxiv DOI attached. The press release would like you to believe biology just got a new engine; what actually happened is that a fleet of agents read papers faster than one person could, which is the same trick an index and a grep have been pulling since the 1990s. Worth it anyway, because the atlas is downloadable and the pattern (fan out one agent per unit of work, merge the reports) ports to any job where a human reading documents is the bottleneck.

## 44. ChatGPT Ads expands to 26 new countries as over 100,000 advertisers have used the platform — by OpenAI News

![OpenAI News](https://openai.com/favicon.ico)

**Source:** https://openai.com/index/chatgpt-ads-expands-26-new-countries/
**Karakeep doc:** `yarn556qorjpvseovcchokcq`

OpenAI has spent the last eight months turning ChatGPT into an advertising platform, and on October 21 it opened 26 more countries, taking the total to 89. The headline number is that over 100,000 advertisers have now run campaigns, and 1.2 billion people use ChatGPT every week, so the inventory argument writes itself. The new markets are 14 more Latin American countries after Mexico and Brazil, including Argentina, Chile, Colombia and Peru, plus Nigeria, South Africa, Serbia, Ukraine, Cambodia, Bangladesh and Pakistan, which is a deliberate grab at the places Google and Meta monetise hardest and where OpenAI's local-language coverage is thinnest. Ads run only on Free and Go, Plus, Pro and Enterprise stay ad-free, and the pitch to the CFO is that advertising is what funds the cheap tier, which is a cleaner way to say that the people who will never pay are the inventory. The principles section is the part worth reading carefully: conversations are not shared with advertisers, user data is not sold, ads are visibly labelled and physically separate from the answer, and ads do not influence what ChatGPT says. Those are the same claims Google made for years, and the difference is that Google's ad load was visible in the page while this one is injected into a transcript you are having with a machine that tells you it does not have an agenda. Also in the fine print: the under-18 exclusion is a prediction, not a guarantee, ads are withheld from health, mental health and politics, and the whole thing is still eight months old and unproven at scale. The next phase is new formats, objectives, buying options and measurement, which is a polite way of saying that the current formats do not measure well yet. CNBC puts the money at $1 billion annualised revenue run rate in August, up from $100 million in March, so the curve is steep and the question is what happens when the ad load stops being a novelty. Anthropic, which has made ad-free Claude the centre of its Super Bowl campaign, now has a very specific thing to point at. Worth watching for Wojtek because the line between "ChatGPT recommended this" and "ChatGPT was paid to mention this" is about to get blurry, and the answer independence claim is the only thing standing between a research tool and a sponsored search engine.

## 45. OpenAI models are coming to Google Cloud — by OpenAI News

![OpenAI News](https://openai.com/favicon.ico)

**Source:** https://openai.com/index/openai-models-google-cloud/
**Karakeep doc:** `olg01i937p98ip3xdjyi1a9i`

OpenAI and Google Cloud announced a partnership putting OpenAI's frontier models and Codex into Google Cloud's Model Garden, billed through the Google Cloud Marketplace, with existing GCP spend commitments usable to pay for them. General availability is "in the coming weeks", which in corporate time usually means nobody knows. There is no pricing, no model list, no latency numbers, no quality benchmarks, and no date beyond that hand-wave. The press release leans hard on regulated-industry procurement language, and that is the actual story. Google Cloud gets OpenAI models inside the perimeter it already sells, and OpenAI gets a second hyperscaler storefront to push volume through. The more interesting part is that the models also land in Google Antigravity and the Gemini Agent, putting them inside Google's own agent stack. Brockman calls it a step toward making "our most capable models and Codex available where customers are already building", and Kurian promises customers model choice and lower costs. Neither quote commits to anything a finance team can drop into a spreadsheet. The one honest line in the post says Microsoft remains OpenAI's primary cloud partner, which quietly marks this as a distribution experiment rather than a new home. Recent OpenAI posts covered the Oracle cloud deal and zero data retention for frontier models. Nothing here says whether that zero-retention story travels to Model Garden, and for a regulated buyer that is the question that matters. Wojtek cares because a second hyperscaler channel changes how model pricing gets negotiated, and he cares more that "soon" is doing a lot of work in this announcement.

## 46. Cloudflare deploys protections against php2shell vulnerability | Cloudflare Blog — by Cloudflare Blog

![Cloudflare Blog](https://blog.cloudflare.com/_emdash/api/media/file/01M5FBPSP6GA0RRJ5FDQ68S476.png)

**Source:** https://blog.cloudflare.com/php-vulnerabilities-waf-protection/
**Karakeep doc:** `k7nkcilt1406alxdoica33ye`

Cloudflare says it had WAF rules in place for php2shell roughly nine hours before the coordinated disclosure went public, with every customer on a WAF plan including the free tier protected by default from October 21 at 03:02 UTC. The two bugs are CVE-2026-109618 and CVE-2026-109619, disclosed by Calif.io, Wiz, OpenAI and Quarkslab with the PHP foundation in the room, and they hit every PHP install from 5.4 onwards. PHP runs something like 70% of the web, so the blast radius is most of the internet, with WordPress and Magento sitting right in the path. The mechanism is memory handling during error cleanup. CVE-2026-109618 is an out-of-memory condition where PHP tears down a request using data it never finished initialising, and CVE-2026-109619 is a fatal error that leaves references to memory which was already freed, something a later request in the same process can follow and leak. That gives you denial of service, remote code execution and data exposure. Because the flaw lives in the runtime, updating your site code or your plugins fixes nothing, you need the PHP patch, and if a host runs PHP for you then you ask them. The interesting engineering is "full transaction detection", a new WAF mode that inspects the origin response as well as the request inside the same HTTP transaction and can block a matching response before it reaches the requester, which is what let Cloudflare keep up when attackers started mutating payloads to slip past request-only rules. Seven "Generic Rules - Anomalous Execution" rules landed in the free managed ruleset (77454fe2d30c4220b5701f6fdfb893ba), seven more in the paid one, plus a default high-confidence signature block in the Managed Response Firewall. Two caveats are worth keeping in mind. This is defence in depth, not a patch, and the rules were tuned against attack traffic Cloudflare happened to see. The verdict is that you patch today, keep the WAF on, and if you self-host PHP, stop reading this and go update.

## 47. Introducing full transaction detection for Cloudflare WAF — by Cloudflare Blog

![Cloudflare Blog](https://blog.cloudflare.com/_emdash/api/media/file/01M5E1HV25GV2PKJHWP2MM8HGH.png)

**Source:** https://blog.cloudflare.com/full-transaction-waf/
**Karakeep doc:** `qnih5825t32x207e1rwe81h6`

Two new WAF primitives from Cloudflare, and the second one is genuinely new. Full transaction detection evaluates a request together with the response the origin returned, so a rule can ask two questions at once: does this request look malicious, and what happened when the app handled it. Response rules then let you block that response before it reaches the requester, replacing it with a WAF block page and HTTP 403. The canonical example is a traversal attempt for ../../config/database.ini that comes back 200 with a text/plain body holding a username and a password. Request inspection alone cannot prove the leak happened, because the app might have rejected the traversal; a matching response can prove it. The motive is the current mess. Cloudflare shipped WAF protection for php2shell about nine hours ahead of public disclosure, and that flaw, CVE-2026-109618 and CVE-2026-109619, disclosed by Calif.io, Wiz, OpenAI and Quarkslab, hits PHP 5.4 and later, which underpins roughly 70% of websites, with denial of service, remote code execution and data exposure all on the menu. Detection and mitigation stay separate by design, so teams can watch detections in Security Analytics before writing policy, and three new response fields (cf.waf.signature.response.confidence, .categories, .ref) expose what matched. Everything ships to every plan including Free, and the first managed ruleset, Cloudflare Managed Response Firewall Default, runs on every request unless you narrow its scope. Caveats: everyone gets only three custom response rules, response-body matching does not exist yet, and the "cannot undo actions already performed at the origin" line matters more than it reads, because a blocked response stops the data leak while the remote code execution that produced it has already run. Verdict: this WAF feature can actually prevent exfiltration, which request-level inspection never could, and it arrives as a band-aid over unpatched PHP. Patch the runtime, then let the firewall watch the response.

## 48. How Commerce.com and Cloudflare are getting storefronts ready for AI agents — by Cloudflare Blog

![Cloudflare Blog](https://blog.cloudflare.com/_emdash/api/media/file/01M5AYSBKT78Q7W6234MGTKVKA.png)

**Source:** https://blog.cloudflare.com/webmcp-commerce/
**Karakeep doc:** `ubm4y6emc80rucxa64j6bkqt`

Cloudflare and Commerce.com are trying to make agentic shopping actually work, and the plumbing is the interesting part. WebMCP is Google's proposed browser standard that hands an AI agent structured tools on a page, things like search_products and add_to_cart, instead of the agent guessing which button does what and burning tokens while it fails. It is still experimental: behind a Chrome flag, Chrome Origin Trials, a few agentic browsers and Cloudflare's own Kitesurf. Cloudflare's edge implementation has been in beta since August and injects a small script so site owners write no code. Commerce.com, which runs almost 100,000 domains on Cloudflare, wanted it switched on for every storefront with a per-merchant opt-out, so Cloudflare hooked it into Configuration Rules and custom hostname metadata. An opted-out store gets no injected script, no remote lookups and no extra latency. Two fixes came out of the pilot: the bridge assumed every MCP server lived at /mcp while Commerce.com's sits at /api/mcp, now a zone-level setting passed into the script tag, and the script exits quietly when the MCP server is down or the browser has no WebMCP. The security argument is sound enough: tools run inside the shopper's own session on the merchant's domain, no credentials leave, and the merchant keeps checkout. The caveats are bigger. The standard is not shipped, so real traffic today is rounding error. Nobody says what merchants pay for this. The 100,000 figure is domains, not shops. And nothing addresses prompt injection through product descriptions, which is where this idea will get eaten. Worth reading as a preview of plumbing.

## 49. Terminal X matches senior investor judgment 88.6% with GPT-6.1 — by OpenAI News

![OpenAI News](https://openai.com/favicon.ico)

**Source:** https://openai.com/index/terminal-x/
**Karakeep doc:** `d6vgqiws68vk5y46k41475ls`

OpenAI customer stories have a house style: a logo, four big numbers, a quote from the CEO, and a lot of "capital memory". This one is Terminal X, a finance startup selling what it calls a Capital Memory operating system, where former JPMorgan and Blackstone people sit onsite with an investment team and encode how the firm invests into agents that run on-premise or in the firm's own cloud. The Eval Agent grades those agents against a 54-criterion rubric, and the headline figure is 88.6% agreement with senior human reviewers against 86.4% for the next-best model, a 220 basis point gap. Across 500 scored judgments that gap is eleven judgments, which is a sample size you could lose in a lift. The claims that survive closer reading: about 25% more mandate deviations caught, mostly style drift such as a buyout fund sliding into distressed credit when scenario models turn; roughly 30% lower cost per query at similar speed, which matters because long-context runs are the expensive part; and $2.4M in annualised savings at one private equity firm, self-reported, no methodology published. Their own operating numbers are more telling than the comparison: 1,700 firm Memories, over a million custom workflows, and weekly actives at 81% of monthly actives, which reads like a small number of very heavy users rather than a wide rollout. Also worth naming plainly: the benchmark pits an OpenAI model against unnamed "next-best" rivals, graded by an agent built on OpenAI models, published by OpenAI, so 88.6% is a marketing number wearing a lab coat. The whole thing runs on a 54-point checklist, with each failure carrying a one-line reason and a corrected source, and every correction quietly becoming a new test case for that desk. The product idea is genuinely good, the arithmetic is thin. If you are running a research or diligence workflow and care about a defensible audit trail, the Memory concept is the bit worth stealing, whatever you think of the benchmark.

## 50. 8 eMudhra certificates are compromised. Here’s what you need to know — by Cloudflare Blog

![Cloudflare Blog](https://blog.cloudflare.com/_emdash/api/media/file/01M5DK5EH8PE8PVBNH2XNFEF7Y.png)

**Source:** https://blog.cloudflare.com/emudhra-certificate-compromise/
**Karakeep doc:** `ij35ajj40ns7kstr4loe1ra6`

Cloudflare disclosed on October 19 that private keys for eight eMudhra intermediate certificates were compromised, and the reason matters. The CA generated those keys incorrectly, so anyone can recover them from the public certificates. This has been possible since the intermediates were created in April 2025, and nobody noticed for eighteen months. Weak keys plus universal trust equals a forged certificate for any domain you care about, and a man-in-the-middle to go with it. Cloudflare found no active exploitation on its own services.

Cloudflare's own patch list: Cloudflare One Client v2.5.7 on Android, v1.12.7 on iOS, and 2026.8.2115.0 on Windows, macOS and Linux; the 1.1.1.1 app at v6.38.11 and v6.31.8 on mobile with the same desktop build; and cloudflared 2026.10.2, where container deployments need the image redeployed. Zero Trust with Gateway and an up-to-date client is protected automatically. What is left for you: mutual-TLS trust stores, custom origin certificates under Full (strict) or Strict, container images bundling their own trust stores, and anything using HTTPS egress interception, which moves validation into Cloudflare's infrastructure. Automatic SSL/TLS now warns you if you still hold a distrusted certificate. The timeline runs from detection at 17:00 UTC on the 19th to full CDN and server-side Zero Trust mitigations by 19:20 UTC on the 20th.

The break is in certificate authentication. The TLS encryption algorithms themselves are fine. The upstream tracker lists patched builds across NSS 3.131.1, Go 1.27.3 and 1.26.10, Java 8u511 through 27.0.1.0.2, Node 22.23.4, curl's 2026-10-20 CA bundle, Python certifi 2026.10.19, Debian ca-certificates 20260816+nmu1, Alpine 20261020-r0 and Arch's 3.131.1-1. Browsers and operating systems got the bad news quickly through CRLSets, CRLite and OneCRL, and no Certificate Transparency entries existed for those intermediates during the vulnerable window, so browsers were never exploitable. Non-browser clients that skip CT enforcement are the exposed ones, and Cloudflare's advice is to test through the real TLS path of each app, because a green browser check proves nothing about a background service. Do not "fix" the resulting cert errors by turning verification off.

Worth a look if you run custom trust stores, base images or appliances that update slowly.
