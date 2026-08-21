---
date: 2026-08-07
slug: 2026-08-07-morning-brew
tags: digest,karakeep,linux
---
# Morning Brew — 2026-08-07

Hoarded 5 bookmarks on 2026-08-07: 4 articles and 1 video (transcribed). Theme of the day: **the terminal and the people who make it a lifestyle.** A kitty system panel, a free Linux CLI book, a vi shell-integration guide, a DevOps novel, and Stuff Made Here peeling food with explosives.

---

## 1. Clowder — Kitty terminal system panel — by github.com

![github.com](https://opengraph.githubassets.com/b95fa2bab1774645ce2f35bc443254c4f8f859f979224ac0f2f94649a1223041/5hubham5ingh/clowder)
- **Source:** https://github.com/5hubham5ingh/clowder
- **Karakeep doc:** `e5mkg4uerju3nnhn9bi8gj6b`

A system panel that lives inside the Kitty terminal, driven by Kitty's remote-control API. It launches `btop` for system metrics, `cava` for real-time audio visualization, and a pane of live system info (bluetooth, volume, brightness, wifi, mic, screenshare, weather, calendar). Two modes: a full dashboard or a collapsible bottom-edge bar via `kitty +kitten panel`, plus a Hyprland setup with keybinds and a screensaver. Prereqs read like a proper Arch shopping list — btop, cava, brightnessctl, pactl, iwconfig, yay, pw-dump, and its own `js` interpreter. 131 stars, MIT.

**Verdict:** the `kitty +kitten panel` bar concept is genuinely slick, and it's a fun flex of what a terminal can become. But the "needs a custom js interpreter and half the AUR" energy is pure tinker-toy. Play with it, don't bet your desktop on it.

---

## 2. The Unicorn Project — DevOps, but from the devs' side of the trench — by oreilly.com

![oreilly.com](https://oreilly.com/favicon.ico)
- **Source:** https://www.oreilly.com/library/view/the-unicorn-project/9781098124175/
- **Karakeep doc:** `q8noh7jgv70c2d8coh8g9vmh`

Gene Kim's companion to *The Phoenix Project*, set at Parts Unlimited on the same timeline but told from the developers' perspective. Senior engineer Maxine is scapegoated for a payroll disaster and dumped onto the broken Phoenix project, where red tape and a big-bang release before it's even done make it a nightmare. She falls in with "the Rebellion" — a bar-cellar of misfit engineers — and the bartender Dr. Erik Reid (same mentor as before) hands them the book's real payload: the **Five Ideals** — locality & simplicity (don't "complect" systems together), focus/flow/joy (small batches, fast feedback), improvement of daily work (pay down tech debt as routine), psychological safety (the Toyota andon cord), and customer focus.

**Verdict:** same ideas as *Phoenix* but from the devs' perspective, so it gets predictable if you read the first one. Reviews knock MaxEngine as not very relatable. But as a picture of what healthy engineering culture looks like, it's required reading for anyone leading engineers.

---

## 3. The Linux Command Line — the free book that taught a generation to talk to a prompt — by linuxcommand.org

![linuxcommand.org](https://linuxcommand.org/favicon.ico)
- **Source:** https://linuxcommand.org/tlcl.php
- **Karakeep doc:** `p4gzycisph3gsyk3xi1k85u5`

William Shotts's *The Linux Command Line*, Seventh Internet Edition, 596 pages — same ground as linuxcommand.org but much deeper, including the common CLI programs you actually hit day to day. Released under CC BY-NC-ND, so the PDF is **free to download**, with example scripts alongside. Print edition from No Starch Press, plus a sequel/supplement *Adventures with the Linux Command Line*. Translations include Polish via Helion.

**Verdict:** one of the best free Linux resources that's still alive and maintained. If you only read one command-line book, make it this one.

---

## 4. Integrate Shell Commands Into Vi Workflow — `!` is your wizard wand — by rwx.gg

![rwx.gg](https://rwx.gg/favicon.ico)
- **Source:** https://rwx.gg/tools/editors/vi/how/magic/
- **Karakeep doc:** `nyewfjnachwntjsnrcvp1va7`

The single most underrated Vi feature: full shell integration via `!`. The "magic wands" mnemonic — send a line/section/page to any shell command and let its output replace those lines. The line wand `!!` pipes the current line to `bash`/`bc`/`python3`; the section wand `!}sort` sorts a block; the line-number wand `!:<lineafter>` sends an exact range (e.g. `pandoc` to render markdown in place). Beyond one-offs, write small filter scripts to PATH (a `cmt` script comments out a selection via `!}cmt`) — no vimrc bloat needed. The core pitch: the ex command line's automatic range inference plus any executable beats Vimscript macros.

**Verdict:** genuinely useful if you live in vi and still copy-paste between editor and terminal like an animal.

---

## 5. 🎬 I made an apple peel itself — by Stuff Made Here

![Stuff Made Here](https://i.ytimg.com/vi/RpslsMqPFWA/maxresdefault.jpg)
- **Source:** https://www.youtube.com/watch?v=RpslsMqPFWA
- **Karakeep doc:** `ly8mre1zcjoxy12zc69aqbr4`

The title is a lie — this is Stuff Made Here building a **steam potato peeler**, because legend says a potato under extreme pressure and heat will peel itself when you explosively release the pressure. To film it in slow motion he builds the whole pressure-vessel rig himself, storing the energy of three sticks of dynamite in his workshop. Obviously. The physics is sound: steam heats the skin surface faster than air, superheating the water just under it pressure-cooker style; vent at ~150–200 psi and the water flashes to steam, trapped under the skin, popping it off like a balloon.

The engineering is the real show: a thick stainless pipe boiler, water-jet-cut flat parts, a two-kilowatt immersion heater, air-operated valves run remotely, a welded chamber with a glass viewing door, and — the genuinely clever bit — **Bellville spring washers** on the threaded rods so the boiler's thermal expansion doesn't snap the bolts at 80% of failure stress. He hydro-tests everything with incompressible water first (a steam failure is a bomb, a water failure is a damp *ploink*). Welding leak failures, a shorted wire splice, a leaking safety valve, endless retries — classic maker grind.

The payoff: a fully naked potato with near-perfect yield preservation. Then the food gauntlet: an apple that looks Voldemort-cursed (smells like apple pie), a skinned creepy tomato, "high society" grapes, a blackberry that explodes into a fleshy blob, and a strawberry that turns into "strawberries and cream" so weird even he can't explain it — the part-two hook is that the machine raised more questions than it answered. Wife rates it 6/10 and later admits she has no idea why; daughter's popcorn idea pops 70% and needs a boiler fix for part two.

**Verdict:** pure Stuff Made Here fuel — wild, over-engineered, physically sound, dramatically fun. It's a prototype built to peel exactly one potato on camera and it nails that. The title lies (it's a potato peeler; the apple is one test subject), the machine never gets a clean max-pressure run (heater leak), and it ends on a shameless part-two cliffhanger. Watch it; don't build it.

---

*Digest generated 2026-08-07 by the Hermes nightly karakeep processor.*
