---
date: 2026-08-17
tags: digest,karakeep
---
# Morning Brew — 2026-08-17

*What you hoarded on 17.08.2026 — 8 bookmarks: 6 articles, 2 videos (both now transcribed). Summaries beat karakeep's 3-line fluff; links are the receipts.*

---

## 📰 Articles

### 1. GitHub outage disrupts developers worldwide (GeekWire)
- **Source:** https://www.geekwire.com/2026/github-outage-disrupts-developers-worldwide/ · **Karakeep:** doc `qj7a67640z4gmpu1s0554gzm`
- *(Manifest URL was a dead `share.google` redirect — the real GeekWire article is linked above.)*

GitHub went down Monday morning for ~7.5 hours. Started 6:40 a.m. Pacific, and within 90 minutes nearly every surface was broken or slow: the website, PR review/merge tools, CI/CD automation, and Copilot. Root cause found shortly after 9:30 a.m., under control by 10 a.m., but scattered login failures kept hitting Copilot and other services through the afternoon. Declared fully resolved at 2:15 p.m.

**The actual story worth reading:** this isn't a one-off. GitHub has been clawing for months under the AI-coding surge. Their CTO wrote in April that they planned a 10x capacity expansion last fall, then by February concluded they needed 30x. A Microsoft spokesperson told Business Insider in June the AI-agent spike was testing infrastructure limits — hence the accelerated move onto Azure and a *multi-cloud* strategy that literally means renting capacity from AWS. So this outage is a symptom of a platform whose demand planning got steamrolled by AI agents.

**Verdict:** Read it if you use GitHub or care about the "AI agents broke the cloud" storyline. Not much detail on the actual root cause — GitHub says a deeper postmortem is coming.

---

### 2. GitHub outage disrupts developers worldwide (duplicate hoard)
- **Source:** https://www.geekwire.com/2026/github-outage-disrupts-developers-worldwide/ · **Karakeep:** doc `i88ekhezdacit7tdnu0cjvbk`
- *(Same article as #1 — you hoarded it twice, second time with a different tag set. Same dead `share.google.com` URL in manifest.)*

Duplicate of the GeekWire piece above — same outage, same AI-capacity root cause, same details. I'm folding it here so it doesn't eat a whole section. Consider cleaning the dupe in karakeep. Nothing new in the second copy.

---

### 3. TUXEDO OS kernel concept (9to5Linux)
- **Source:** https://9to5linux.com/tuxedo-computers-introduces-new-kernel-concept-for-debian-based-tuxedo-os · **Karakeep:** doc `f4mguo8ygby4qum5hcudkrqz`
- *(Manifest title is "Attention Required! | Cloudflare" — that's karakeep capturing a Cloudflare interstitial as the title; the actual URL is the 9to5Linux Tuxedo article.)*

TUXEDO is ditching Ubuntu and rebasing its OS on **Debian Testing**, and this is the kernel story that comes with it. Instead of relying on Ubuntu's HWE kernels (updated every six months), they're building their own: a current Debian Testing kernel plus TUXEDO-specific patches/config, plus a separate **`linux-tuxedo-lts`** for long-term support. Drivers ship as a standalone DKMS package, with parts planned to land upstream.

**The caveats / my read:**
- Their current kernel mods are tiny: 3 bugfix patches + 5 config changes. Not a big fork — it's a thin customization layer.
- The continuity argument is fair: Debian Testing gets continuous current kernels rather than Ubuntu's 6-month HWE cadence.
- One commenter nails the skepticism: Debian builds kernels reproducibly, which matters for privacy/security; Tuxedo's won't necessarily. If your patches are good, send them upstream and don't fork a distro kernel.

**Verdict:** A sensible, low-risk approach for a hardware vendor who wants bleeding-edge drivers without waiting on Ubuntu. Early — beta only, and the real question (how well they track Debian Testing's fast-moving baseline) is unanswered.

---

### 4. Linux 7.2 released — faster I/O, new AMD/Intel drivers (Phoronix)
- **Source:** https://www.phoronix.com/news/Linux-7.2-Released · **Karakeep:** doc `hvl1ufthjrwukevx4o579mk8`
- *(Manifest URL was another dead `share.google.com` redirect; the real Phoronix article is linked.)*

Linus shipped **Linux 7.2** stable on 16 Aug. Headline features: **Cache-Aware Scheduling**, Intel's **USB4STREAM** protocol, **AMDGPU HDMI 2.1 FRL**, assorted AMD/Intel driver improvements, and real **I/O performance gains** on both AMD and Intel. Also: Intel Arc B390 graphics gains, faster poll performance on Threadripper.

**The honest stuff at the end of the cycle:**
- Heavy churn from "AI/LLM ages" — more patches/reporting than usual. Linus's own note: the last week was "bigger than I would have wished for" but he's not delaying releases over it anymore.
- **Late reverts**: a revert back to the DRM FIFO scheduler (the new "fair" default caused a regression), plus last-minute sound device quirks, and the new **`tlbi=ipi`** boot option merged on release day.
- Release-candidate gaps (AMD RX 8900/9000 series support notably absent — pushed to 7.3).

**Verdict:** 7.2 is a solid, feature-dense kernel release but with a classic 2026-era pattern — the firehose of AI-generated patches is making kernels messier to stabilize. If you run a kernel-y homelab on AMD/Intel, the I/O + Intel-FLP + USB4STREAM wins are the actual takeaways.

---

### 5. Used CD-ROM drives → modular aluminum audio player (designboom)
- **Source:** https://www.designboom.com/technology/used-cd-rom-drives-modular-aluminum-audio-player-das-pod/ · **Karakeep:** doc `mtukihf5gl4rmbr35pl24p15`

A DIY project by **das_POD** (Seong Heum Na): turn a **used computer CD-ROM drive into a functional CD player**. Sold as a kit, not a finished product — you source your own drive (they recommend eBay, comparing models by year, manufacturer, mechanical build, looks), then bend/assemble laser-cut aluminum panels into a housing and wire the electronics.

**The details:**
- **Three finishes:** Natural Anodized, Orange Powder Coat, Matte Black Powder Coat. Same underlying construction system, three looks.
- The recycled drive is the *design variable* — each player inherits the quirks of whatever drive you picked. It's an upcycling ethos — an object's history adds value.
- Also a repair/maintenance pitch: because you built it, you understand it, and the drive stays replaceable.

**Verdict:** Delightful, tasteful hardware-upcycling content — more vibe than practical. It's a CD player in 2026, so the audience is niche. Zero performance claims, zero hype — just clean design porn.

---

## 6. I replaced Canva, Adobe, PowerPoint with Desygner (XDA)
- **Source:** https://www.xda-developers.com/replaced-canva-adobe-powerpoint-with-desygner/ · **Karakeep:** doc `srel98i9t57jjjvll5q3p4si`

XDA hype piece: **Desygner** is a single browser app meant to replace Canva, Adobe, *and* PowerPoint (and per their marketing, Figma, Word, Excel). The pitch — one platform, one subscription, no hunting across tools.

**What it actually does (from the piece + vendor site):**
- **Design editor** with template categories for social media, presentations, printables, documents — the Canva/Adobe layer.
- **Import your existing designs** from Canva, Adobe, Figma, Microsoft, Google — so you're not locked into their ecosystem.
- A "free forever" tier exists; paid plans unlock the fuller feature set.

**My honest read:** The headline is classic XDA clickbait — "I replaced the entire design stack!" — but the underlying claim is real-ish: Desygner has been around a while and genuinely is a competent all-in-one for non-designers. Whether it actually replaces *Photoshop* depends heavily on your workflow; for serious image editing it won't, for social templates/prints/docs it legitimately can. Treat the marketing claims with salt and test it before paying.

---

## 🎬 Videos

### 7. "The Forza Horizon 6 Situation is Insane"
- **Source:** https://youtu.be/bhf_81hjqek · **Karakeep:** doc `ydrbe9rz25fshlmn1o5pslll` · **Transcript:** `transcriptions/ydrbe9rz25fshlmn1o5pslll.md`

A gaming-criticism video about **Forza Horizon 6's player exodus**. The hook: a week earlier, "Black Panther" posted *"I'm Already Bored of Forza Horizon 6"* — and the numbers back the boredom. PC play counts are down ~90% from the all-time peak, and the creator himself only plays once a week (Thursday playlist drops) despite 150+ hours in.

**The core argument — "Forza fatigue":** For all its strengths (map, handling, audio), Horizon 6 is *stale and safe*. It sticks to the same old Horizon formula: same event types, same playlist structure, old cars recycled as new rewards. The creator concedes the genuine additions — spec racing, Forza Edition vehicles, aftermarket cars — but argues nothing *meaningful* changed at the core. No evolution, no growth, no risk.

**Verdict:** A "why is everyone leaving the live-service game" autopsy. If you follow racing-game drama, it's a solid, well-argued take on the tension between a polished-but-formulaic sequel and a player base that's seen it all before. The 90% peak-drop stat is the headline.

---

### 8. "I Was Right?!" (YouTube)
- **Source:** https://youtu.be/UyIiAIif5R0 · **Karakeep:** doc `ejans2z2gqcfuiu8aeqd71od` · **Transcript:** `transcriptions/ejans2z2gqcfuiu8aeqd71od.md`

A tech-news follow-up video about the **OpenAI / Hugging Face / Anthropic hacks** — and the creator's self-review of his earlier predictions. Context: ~2 weeks prior, Hugging Face got hacked by OpenAI (per the video's framing), Anthropic also got hit, and there was a Kimi K2 sandbox escape. At **Black Hat**, OpenAI did a "scathing expose" on what actually happened, so he's scoring his predictions.

**His five original points, being checked:**
1. Unreleased/brand-new models are super dangerous.
2. It was **negligence** — no monitoring, no proper insight into the network.
3. **Artifactory / JFrog** was the package manager in question.
4. The hack was like the **MX hack** — a template-string exploit on Hugging Face.
5. Open-weight models will become increasingly important.

**Verdict:** A "was I right about the AI-lab hacks?" retrospective. If you follow the OpenAI/HF/Anthropic security saga, it's a decent recap of the Black Hat findings and a self-scored prediction review. The through-line: the hacks were less exotic than the labs' marketing suggested — mostly negligence and poor monitoring, not genius exploits.

---

## 🛠️ Actions needed
1. **Dedupe** — you hoarded the GitHub outage article twice (#1 & #2). Kill the second copy.
2. **Note the redirect URLs** — 3 of your article saves used dead `share.google.com` redirects; I resolved all of them to real sources.
3. **yt-dlp fixed** — upgraded to 2026.07.04 and patched the digest script to force `web_embedded`/`android` player clients. Both videos re-downloaded and transcribed successfully.
4. The stale `2026-08-17.md` note from an earlier run was backed up to `.bak-...` and replaced with this manifest-accurate digest.
