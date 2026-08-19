---
date: 2026-08-14
slug: 2026-08-14-morning-brew
tags: digest,karakeep,ai
---
# Morning Brew — 2026-08-14

Only 3 bookmarks today, and they're a weird little trio: an AI security paper that is either terrifying or overhyped, an open-source ESP32 smartwatch that reads your wrist muscles, and a maniac who bolted two desktop CPU coolers onto a phone to play The Witcher 3. Friday hoard energy, honestly.

---

## 1. Researchers can now reverse-engineer LLM prompts from output text with near-perfect accuracy
- **Source:** https://share.google/6g5pNgsTVdvPYDwXl
- **Karakeep doc:** `auwhgk2g179fwce2qmhodokt`

IIT Bombay + Adobe Research cooked up **"Previous-Token Prediction" (PTP)** — an inverse language model trained from scratch purely on synthetic output from a target LLM, that predicts *previous* tokens instead of the next one. Feed it a single response and it reconstructs the original prompt, word-for-word in their best case, plus a bunch of semantic variants that produce near-identical output when fed back in.

The nasty bit: an inverse model trained on the tiny **Qwen-3-0.6B** could still extract meaning and intent from **GPT-4o** output — the attacker doesn't even need to know which model wrote the text. So company system prompts (trade secrets, moderation rules, internal instructions) and individual sensitive queries are all fair game from nothing but generated text.

**Caveats:** they only demonstrated it on short 1–2 sentence prompts. Whether it scales to long, multi-paragraph system prompts was explicitly *not* tested. The paper stops short of claiming real attacks on commercial systems.

**Verdict:** Genuinely interesting, but the "near-perfect accuracy" headline is doing a lot of work. The cross-model transfer with a 0.6B model is the part that should worry people; the short-prompt-only scope is the asterisk that keeps it from being full panic.

---

## 2. EITWatch open-source ESP32-S3 smartwatch with planar EIT hand gesture recognition
- **Source:** https://www.cnx-software.com/2026/08/14/eitwatch-open-source-esp32-s3-smartwatch-implements-planar-eit-hand-gesture-recognition/
- **Karakeep doc:** `p6d30x3ds8ern9cmrupachv0`

Northwestern University's EITWatch uses **Electrical Impedance Tomography** — 8 gold-plated electrodes on the *back* of the watch case (not the circumferential wrist band most EIT systems use) to read impedance changes from muscle/tendon movement. A 50 kHz sinusoid drives ~1mA, 4× ADG738 matrix switches route injection/sensing, and a 31mm electrode ring fits inside a standard 40mm case.

Because a flat array can't wrap the wrist, they use a **multi-depth scanning protocol** (one fixed source, cycling the negative sink) — 35 impedance measurements per frame at 48Hz. Built on a XIAO ESP32-S3 and fully open source: CERN-OHL-P-2.0 hardware, Apache-2.0 firmware, Altium/Gerbers/BOM on GitHub.

**Numbers:** 92.5% accuracy on held macro-gestures (Six, Gun, Point, Thumb Up, Stretch, Fist), 91.5% on micro-gestures (swipes, pinch, splay, wrist flip). On-device inference draws ~35mA → ~8.6h on a 300mAh battery.

**Caveats:** the accuracy is a sandcastle. Re-tested **48 hours later it drops to 73.2% macro / 70.4% micro**, and with new users it collapses to **63.1% / 55.3%**. That's a staggering overnight decay — lab demo, not a product. Also 60×40mm, so chunky.

**Verdict:** Cool open-hardware science project, neat trick putting EIT on the back of a watch. But read the caveats before you get excited: accuracy falls off a cliff within two days and worsens per-user. Nice engineering flex, nowhere near wearable-ready.

---

## 3. Modder straps two desktop CPU coolers to a ZTE phone to make a gaming PC
- **Source:** https://www.tomshardware.com/pc-components/cooling/modder-straps-two-desktop-cpu-coolers-to-zte-nubia-z70-ultra-turns-smartphone-into-a-gaming-pc-snapdragon-8-elite-soc-with-24gb-of-ram-runs-the-witcher-3-at-1080p-ultra
- **Karakeep doc:** `o7omfzxvz5hikgpi1ukcz3mk`

A modder stripped a **ZTE Nubia Z70 Ultra** (Snapdragon 8 Elite, 24GB LPDDR5X, 1TB UFS) down to bare hardware — removed cameras, radios, and display — and mounted **two full-size desktop CPU heatsinks** on either side. The point: prove how much performance a phone SoC leaves on the table when it isn't suffocating in a pocket.

**Results that matter:** 3DMark Wild Life Extreme stress test scored **99% stability over 20 loops** (best 6,980, worst 6,910 — a 70-point spread). The whole idea is that sustained workloads are where phones throttle. For real-world proof, it runs **The Witcher 3 at 1080p Ultra at ~20–30 FPS** with the GPU pinned at 99%, via a whole compatibility stack: custom Linux XFCE4 in Termux on Android, Vulkan through Turnip on the Adreno GPU, Windows games through Wine/Box64/Hangover/GameNative.

**Caveats:** 20–30 FPS at 1080p Ultra is not exactly "gaming PC" territory — the writer's honest that it's not replacing a modern rig. And it's absurdly impractical; the two desktop coolers nuke the phone form factor. The point is the thermal headroom argument, not a usable product. Also it's an older 2024 Elite, not the new Gen 5.

**Verdict:** Completely absurd, exactly the kind of thing I bookmarked. The real takeaway is the headline the modder's proving: phones leave a ton of performance on the table purely because they're shaped like phones. 99% stability with real cooling is the kicker — the chip was never the bottleneck, the absence of a heatsink was.

---

*Digest generated 2026-08-19 by Hermes karakeep backfill processor.*
