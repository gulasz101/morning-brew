---
date: 2026-07-24
slug: 2026-07-24-morning-brew
tags: digest,karakeep,self-hosting,recipes,vegan,gaming,ai,android
---
# Morning Brew — 2026-07-24

Hoarded 26 bookmarks on 2026-07-24 (25 articles + 1 video, now transcribed). Theme of the day: **half the hoard is vegan cooking**, the other half is self-hosting/OSS and retro gaming, with Linus telling AI purists to fork off and the EU pretending batteries will fix everything.

---

## 1. 4 free apps that make a cheap Android tablet worth keeping — by makeuseof.com

![makeuseof.com](https://static0.makeuseofimages.com/wordpress/wp-content/uploads/wm/2025/12/touch-portal-control-screen-showing-apps-icon-on-a-huawei-honor-pad-8.jpg?w=1600&amp;h=900&amp;fit=crop)
- **Source:** https://www.makeuseof.com/make-cheap-android-tablet-worth-using/
- **Karakeep doc:** `gfoagc4p4r14538e6d6d1gr6`

A budget Android tablet gets dug out of a drawer instead of collecting dust, and four free apps justify keeping it. **Fotoo** turns it into a digital photo frame (pulls from Google Photos/Dropbox/OneDrive, $60–80 cheaper than a dedicated frame). **Spacedesk** makes it a wireless second monitor for Windows — Wi-Fi-bound, fine for documents/chat but stutters on video, with ASUS GlideX as the wired alternative. **Touch Portal** is a software Stream Deck (macros, app-launch buttons; free tier caps at a 4×2 grid/two pages, the $13.99 Pro is the real unlock). **Libby** pulls free library e-books/audiobooks — the tablet screen beats phone and Kindle for comfort, e-ink only wins on long reading stamina.

**Verdict:** Gadget-salvage list, but Spacedesk and Touch Portal genuinely earn their keep for anyone with a dead slab lying around.

## 2. These 5 open-source software cost me nothing, but are worth paying for — by xda-developers.com

![xda-developers.com](https://static0.xdaimages.com/wordpress/wp-content/uploads/wm/2025/05/karakeep-running-on-a-mac.jpg?w=1600&amp;h=900&amp;fit=crop)
- **Source:** https://www.xda-developers.com/free-open-source-software-worth-paying-for/
- **Karakeep doc:** `vqgtnzxsmmqf1pr2ccdar2o7`

Five self-hosted tools the writer would happily pay for even though he doesn't have to. **Paperless-ngx** (self-hosted document manager with OCR/tags/full-text search), **Karakeep** (the bookmark manager literally feeding this digest — captures content + metadata, killed his Pocket subscription), **Immich** (self-hosted photo backup that feels like a polished commercial product), **Jellyfin** (Plex alternative with posters/cast/watch-progress and no licensing roulette), and **BentoPDF** (fast local browser-based PDF tool).

**Verdict:** "When software is a daily dependency, its value exceeds its price tag" — the not-so-subtle ask being to donate to projects you rely on. Self-serving, but a genuinely solid list.

---

## 3. Sawyer Merritt (@SawyerMerritt) on X — Tesla shuts down S&X lines for Optimus — by x.com

![x.com](https://pbs.twimg.com/media/HN25vdYXYAA6N2E.jpg:large)
- **Source:** https://x.com/SawyerMerritt/status/2080023099618021646
- **Karakeep doc:** `mxdinm7icbu79qg44pfdv2xb`

Tesla says it has **decommissioned the Model S & X manufacturing lines at Fremont** and is installing **first-generation Optimus production lines**, expecting to start production soon. Initial units go to their **Optimus Academy** program.

**Verdict:** Classic Musk-era robotics theater — kill slow-selling premium cars to chase a humanoid-robot ramp. "Expected to start production soon" is doing a lot of heavy lifting.

---

## 4. OSINT: Find Everything About Anyone! — by CyberFlow

![CyberFlow](https://i.ytimg.com/vi/zhTjzscNLEI/maxresdefault.jpg)
- **Source:** https://m.youtube.com/watch?v=zhTjzscNLEI
- **Karakeep doc:** `e9dzgoqor6ndo07jutsi40o4`

An OSINT tools roundup from the Cyberflow Academy guy (the one who shoves a course down your throat at the end). Framed as "I've gone way deeper since my last OSINT video — the actual tools the FBI uses." The tool list is genuinely real and mostly battle-tested open source; the framing and the sales pitch are where it gets goofy.

**Tools worth your time:**
- **Intel Techniques (inteltechniques.com)** — Michael Bazzell, an ex-FBI cybercrimes investigator running the most respected OSINT training outfit around. His free search-tool collection aggregates username/email/phone lookups into one screen. Same methodology real investigators train on.
- **Sherlock** — a username in, it checks 400+ sites at once for where that handle exists. Open-source CLI. The "your throwaway Reddit just connected you to your real Instagram" trick.
- **Holehe** — an email in, it quietly checks 100+ platforms for registration *without* firing password-reset emails, by exploiting how registration pages reply differently to live vs dead accounts. ~30s to a partial map of someone's digital footprint.
- **Google-services probing (EPOS-style)** — an email surfaces which Google services it's tied to, sometimes a profile photo and a real name pulled from Google's own systems. "You're not anonymous" in about 4 seconds.
- **Hunchly** — a browser extension that auto-captures and timestamps every page you visit during an investigation, building a reconstructible evidence trail as you browse.
- **Overpass Turbo + OpenStreetMap** — cross-reference visual landmarks (street-light style, road markings, building shapes) against geographic data to geolocate a photo or clip to the street. The exact Bellingcat technique for conflict footage.
- **Spiderfoot** — automates nearly all of the above into one local scan: point it at a domain/email/IP and it pulls from dozens of sources including breach databases to build a relationship map. Open source, runs locally.
- **Court records / PACER** — the genuinely underused one. Federal court records, property and business filings — all public, searchable, and often full of addresses, employment history and financial detail no social feed gives you.

**Caveats the video won't give you:** the "FBI tools" framing is mostly theater — Graykey/Cellebrite are hardware phone-forensics you'll never touch, and the "federal tools" on the public list are all free open-source software any YouTuber can name. The "it's all public, nothing's illegal, everything was already leaked" line is doing a lot of work: a big chunk of this pipeline is sifting breach databases, which sits in a genuine legal/ethical grey zone.

**The ad:** pivots to "this is exactly why I built a full OSINT course inside Cyberflow Academy... code CYBER50 for 50% off," and closes on an Andrew Tate engagement-bait geo-challenge (find what country this was filmed in) to win a free month of the private community. Real tools, then a funnel.

**Verdict:** Save it for the tool list — Sherlock, Holehe, Spiderfoot and the Overpass/OSM geolocation trick are worth the hour, and the court-records reminder is genuinely underrated. Ignore everything from "links in the description" onward, and keep your wallet shut.

---

## 5. Chłodnik z melona, ogórka i mięty — by rozkoszny.pl

![rozkoszny.pl](https://www.rozkoszny.pl/wp-content/uploads/2021/08/DSC04724-Duzy.jpg)
- **Source:** https://www.rozkoszny.pl/chlodnik-z-melona-ogorka-i-miety/
- **Karakeep doc:** `rc9cc9s8l7cp6dnwcvroeu7z`

Maciej Korkosz's summer cold soup. Melon rounds out the sweetness, cucumber keeps it fresh, mint holds it together. Two servings: ½ melon, 2 peeled greenhouse cucumbers, ⅔ cup Greek yogurt, half a lime's juice, salt, mint, ice, olive oil — blender, done. Vegan swap: ½ avocado + ⅓ cup plant milk instead of yogurt, more lime.

**Verdict:** The lazy no-heat-required energy summer demands.

---

## 6. Masala Dosa — Rice & Lentil Pancake with Potato Stuffing — by bakinghermann.com

![bakinghermann.com](https://bakinghermann.com/favicon.ico)
- **Source:** https://bakinghermann.com/masala-dosa-rice-lentil-pancake-with-potato-stuffing/
- **Karakeep doc:** `fcn40ccpadjf69hdotb6ezph`

A Bengaluru-style masala dosa from Hermann's cookbook — the Vidyarthi Bhavan legend: a thickish, smaller dosa fried deep-golden, cracked open to a potato-masala core, dunked in coconut chutney. Real recipe: soak idli rice + sona masoori in one bowl, urad dal + chana dal + poha + fenugreek in another (one rinse only, else you strip natural yeasts), grind, mix, and **ferment 8–24 hours** in a warm spot. Masala is boiled, mashed potatoes sauteed with chana dal, mustard, asafoetida, onion, curry leaves, turmeric. Makes eight.

**Verdict:** A patient ferment-and-fold ritual with legit South Indian breakfast payoff. The float-test ("a teaspoon of batter in water should float") is the classic if-it-fermented rite.

---

## 7. The server monitor I run on everything is 5MB — by howtogeek.com

![howtogeek.com](https://static0.howtogeekimages.com/wordpress/wp-content/uploads/2026/04/screenshot_2026-04-12_235132-1.png?w=1600&amp;h=900&amp;fit=crop)
- **Source:** https://www.howtogeek.com/the-server-monitor-i-run-on-everything-is-5mb-and-tracks-every-metric-i-need/
- **Karakeep doc:** `k4i0ziwiysp23s332e64epdo`

**Beszel** — a featherweight self-hostable server monitor that runs as one tiny Docker container. Adding a "system" gives real-time CPU/memory graphs by default, plus disk, network, Docker container usage, and (in binary mode) Systemd services. Alerts on server death or CPU/mem/GPU threshold spikes. Setup is a Docker Compose one-liner plus a per-target snippet (default port 45876).

**Verdict:** The "tiny and it just works" homelab monitor — dramatically lighter than Portainer, and the writer swears it's the only one that works after trying dozens.

---

## 8. Tofu-klopsy z masłem orzechowym — by ervegan.com

![ervegan.com](https://ervegan.com/wp-content/uploads/2014/11/IMG_04741.jpg)
- **Source:** https://ervegan.com/2014/11/tofu-klopsy-z-maslem-orzechowym/
- **Karakeep doc:** `idw633rkiis6dh8xc1c2djmq`

Tofu meatballs with peanut butter — firm, crispy, protein-packed, 20 minutes. Per 2 servings: 300g smoked tofu, 2–3 tbsp peanut butter (unsalted), ½ cup breadcrumbs, 3 oil-drained sun-dried tomatoes, 1 red onion, tamari, herbs de Provence. Mash, mix, roll with wet hands, fry till brown, top with cashew "parmesan."

**Verdict:** Odd-combination-but-works retro recipe that wins over meat-eaters.

---

## 9. Wegan Nerd — Kotolety, sznycle z granulatu sojowego — by wegannerd.com

![wegannerd.com](https://wegannerd.com/favicon.ico)
- **Source:** https://www.wegannerd.com/2018/01/kotlety-sznycle-z-granulatu-sojowego.html
- **Karakeep doc:** `tjkpfe12oqq0042go2ov1dw3`

Soy-granule cutlets from the Wegan Nerd blog. The comments are the real value: multiple readers rave these are *the one* veg-cuttlet recipe that doesn't collapse while frying, and the tip of the thread is grinding rice, quinoa and chia in a coffee grinder instead of chickpea flour to keep them from breaking up.

**Verdict:** A battle-tested plant cutlet recipe with a useful community-proven binding tip.

---

## 10. Markdown + Astro = 🧡 — by css-tricks.com

![css-tricks.com](https://i0.wp.com/css-tricks.com/wp-content/uploads/2026/02/mdx-astro.webp)
- **Source:** https://css-tricks.com/markdown-astro/
- **Karakeep doc:** `nyj58uc4e337dt1mzcu90ito`

Zell Liew's guide to doing Markdown "properly" in Astro via **MDX**. Three patterns: import MDX directly as a component, feed it into a content collection (`glob({ pattern: "**/*.{md,mdx}" })` then render via `getEntry`/`render`), or set a `layout:` in frontmatter. You can pass components (like `Image`) into all MDX via `<Content {components} />`. Caveats: ESLint/Prettier don't format MDX well, and Astro's RSS integration needs containers for MDX.

**Takeaway:** The content-collection component-injection trick is genuinely useful for content-heavy Astro.

---

## 11. Wegańska bomba żelaza — Sałatka z tofu, pieczonym burakiem i pesto z pietruszki — by szczesliwibezcukru.pl

![szczesliwibezcukru.pl](https://szczesliwibezcukru.pl/wp-content/uploads/1-logotyp-szczesliwi-bez-cukru/fundajca-szczesliwi-bez-cukru-no-sugar-logotyp-rgb-500.webp)
- **Source:** https://szczesliwibezcukru.pl/weganska-bomba-zelaza-salatka-z-tofu-pieczonym-burakiem-i-domowym-pesto-z-pietruszki/
- **Karakeep doc:** `jjbp1s3g5jwegufdanew58vn`

A vegan iron-bomb salad that tackles plant-iron *bioavailability* (not amount) by pairing iron with vitamin C. Per serving: ~90g tofu (2.5mg), pumpkin seeds (1.3), spinach (1.2), parsley pesto (1.0), roasted beet + sprouts (0.8) ≈ **6.8mg total** — ~38% of an adult woman's 18mg RDA. The parsley pesto (parsley, peanut butter, olive oil, black seed oil, garlic, lemon) is the clever binder.

**Verdict:** A smart, considered composition that walks the "no deficiency" talk without being preachy.

---

## 12. Żelazna sałatka — przepisy.pl (Access Denied) — by przepisy.pl

![przepisy.pl](https://przepisy.pl/favicon.ico)
- **Source:** https://www.przepisy.pl/przepis/zelazna-salatka
- **Karakeep doc:** `s1evv76r01q1ctvxfxrgsbes`

The przepisy.pl page for "Żelazna sałatka" (iron salad) served "Access Denied" on extraction — blocked, 404, or bot-walled. On the face of it it's the same genre as the Szczęśliwi Bez Cukru iron-bomb salad above (tofu + beetroot + iron greens), so a keeper stub rather than a dead end. Filed to revisit when the site lets a browser through.

---

## 13. Tofucznica — by aniagotuje.pl

![aniagotuje.pl](https://cdn.aniagotuje.com/pictures/articles/2024/04/59246682-v-1500x1500.jpg)
- **Source:** https://aniagotuje.pl/przepis/tofucznica
- **Karakeep doc:** `t2zwesxrilr48hvfc59w6w87`

Egg-free scrambled eggs. 25 min, 2 large servings, 178 kcal/100g, 9g protein, no cholesterol, vegan/gluten-free. Ingredients: 300g natural tofu, 2 onions, olive oil, ~15g nutritional yeast, plant milk, salt, sweet paprika, oregano, pepper, chili. Sauté onion, crumble tofu, add spices, then nutritional yeast + milk, fry 5 min more. Tips: turmeric for colour, more plant milk for creaminess.

**Verdict:** A reliable plant scramble with proper "how to make it taste good" detail.

---

## 14. Zupa krem z groszku z puszki w 5 minut — WegePedia — by wegepedia.pl

![wegepedia.pl](https://wegepedia.pl/wp-content/uploads/2023/06/zupa-krem-z-groszku-z-puszki-w-5-minut-fit.jpg)
- **Source:** https://wegepedia.pl/zupa-krem-z-groszku-z-puszki-w-5-minut-fit-przepis/
- **Karakeep doc:** `gxv4fctidvjfzpteiq62p5lm`

A 5-minute canned-pea cream soup, fit + vegan. Two jars of peas (~500g drained), blend smooth with nutritional yeast, soy sauce, garlic, mustard, dried onion powder, ~300ml water, pepper; warm (don't boil). Add chives, lemon juice, salt. Serve with whole-grain croutons and toasted almonds.

**Verdict:** Almost too lazy to count as a recipe, but the mustard + soy + lemon make it taste like more than blended tinned peas.

---

## 15. Nova Brasilia — by novabrasilia.bg

![novabrasilia.bg](https://www.novabrasilia.bg/siteassets/nova-brasilia-logo.png)
- **Source:** https://www.novabrasilia.bg/
- **Karakeep doc:** `ocjpg9pf6v3r6k1eo2jgyvwe`

A Bulgarian coffee brand site. "Always follow the fire within" — the whole brand is fire/energy cult territory. Line-up: espresso, czajnik (Turkish), Intensyvnie, Klassik, Klasik, Crema, and a roasted-beans "Classic fire blend." Founded 1991 with three containers of good coffee and a dream; 30 years on it's a Balkan giant.

**Verdict:** Classic aggressively-marketed coffee — lifestyle over caffeine science, but a nice example of a corporate coffee rebrand.

---

## 16. 7 Near-Perfect 1990s Anime No One Remembers — by cbr.com

![cbr.com](https://static0.cbrimages.com/wordpress/wp-content/uploads/2020/07/Manga-English-Releases-Ghost-Sweeper.jpg?w=1200&amp;h=675&amp;fit=crop)
- **Source:** https://www.cbr.com/perfect-90s-anime-no-one-remembers/
- **Karakeep doc:** `lxwzbofzuwz50qqrbf0tvrt5`

Seven '90s anime that slipped through the cracks: **Giant Robo** (retro robot), **Martian Successor Nadesico** (2196 mecha-comedy, subversive), **Sakona the Ventriloquist** (puppeteer solves crimes with his puppet — Bunraku-theatre trope), **Those Who Hunt Elves** (isekai takedown), **Key the Metal Idol** (humanoid robot as pop idol), **Future GPX Cyber Formula** (racing + mecha underdog arc), **Ghost Sweeper Mikami** (ghost-of-the-week action/horror/comedy).

**Verdict:** Solid "you forgot these" curation — Nadesico and Cyber Formula are the genuine gems.

---

## 17. OpenClaudeLinux — GitHub — by github.com

![github.com](https://opengraph.githubassets.com/175578c01f7927f29a337b81a5acc21095b5f7ced44d675571bd8c3dc6e5bc1e/AbuZar-Ansarii/OpenClaudeLinux)
- **Source:** https://github.com/AbuZar-Ansarii/OpenClaudeLinux
- **Karakeep doc:** `kgvfoz0xyow2g1csp9c9wl7b`

A "Ultimate AI Agent & Linux for Android (Termux)" setup that bypasses root/Shizuku and streamlines installing open-source AI frameworks on Android. Features: **Claude Code ready**, **OpenClaw integration**, **native Ollama**, Termux DNS/network fixes. Requires 6GB RAM. Install: `termux-setup-storage`, curl a Linux setup script, `pkg install ollama`, npm-install Claude Code, point `ANTHROPIC_BASE_URL` at localhost:11434.

**Verdict:** A curl-the-curl-the-curl tangle, but running Claude Code + Ollama on a phone with no root is exactly pocket-agent energy. 43 stars.

---

## 18. Kao Pad Sapparod — Smażony Ryż Z Ananasem, Krewetkamymi i Nerkowcem — by cookpad.com

![cookpad.com](https://img-global.cpcdn.com/recipes/fcef785e89de4142/1200x630cq80/photo.jpg)
- **Source:** https://cookpad.com/pl/przepisy/16024276
- **Karakeep doc:** `kayp6ioi22eylcp6ejigzx4z`

Thai fried rice with pineapple, shrimp and cashews — "very popular Thai dish without complicated ingredients." 30 min, 4 servings. Cut pineapple in half, hollow the flesh into cubes; fry onion+garlic, scramble eggs dry, add cold cooked rice, then pineapple/shrimp/cashews, finish with curry, salt, pepper, sugar, soy, chive. Serve heaped in the empty pineapple half, top with coriander.

**Why it's good:** Quick and flavourful, and the pineapple-boat presentation carries it.

---

## 19. GitHub user creates open-source Nvidia GeForce Now client alternative — by tomshardware.com

![tomshardware.com](https://cdn.mos.cms.futurecdn.net/KhTsPDzs9nGmtpJvb5xffH-1920-80.png)
- **Source:** https://www.tomshardware.com/video-games/cloud-gaming/github-user-creates-open-source-nvidia-geforce-now-client-alternative-removes-tracking-telemetry-and-afk-limitations
- **Karakeep doc:** `uv95g5cz2hd83w32c` — wait, need check: `uv95g5czfoz2r5hm8d93w32c`

**OpenNOW** — an open-source GeForce Now client that strips tracking/telemetry and **lets you go AFK without being kicked for inactivity**. Streams up to **4K@240FPS** (internet-dependent), adds mouse-sensitivity and clipboard-paste. Open-source so you can fork. Limitations: no flight controls, no Discord integration, no Android/iOS/smart-TV support.

**Verdict:** "I refuse to be told when I'm done gaming" energy. The AFK-kick removal is the selling point.

---

## 20. TapePunk — Cyberpunk 2077 VHS mod — by eurogamer.pl

![eurogamer.pl](https://assetsio.gnwcdn.com/cyberpunk-content-vhs.jpg?width=1200&amp;height=630&amp;fit=crop&amp;enable=upscale&amp;auto=webp)
- **Source:** https://www.eurogamer.pl/to-nie-nagranie-z-kasety-tylko-cyberpunk-2077-nostalgiczny-mod-wyglada-jeszcze-lepiej-w-nowej-wersji
- **Karakeep doc:** `sf2qswmfeegcu5gjdj8jdnno`

The **TapePunk** mod turns Cyberpunk 2077 into a grainy VHS tape recording — raw, slightly blurred, worn-tape effects that bring it *closer to realism*. Started as a hobby, then a praised demo scaled into a real mod. The best line, a comment: *"I can't explain it, but this is exactly how nostalgia feels — like a filter over old memories."* The author now aims for the *idealized* version of the game, the way memories actually work.

**Verdict:** Lovely and melancholic. CDPR said no more CP2077 content, so fan creativity is all we've got.

---

## 21. GBA RPG Re-Releases Fully Remastered — Sigma Star Saga DX — by vice.com

![vice.com](https://www.vice.com/wp-content/uploads/sites/2/2026/04/game-boy-advance.jpg?w=2000)
- **Source:** https://www.vice.com/en/article/game-boy-advance-rpg-re-releases-next-week-fully-remastered-on-modern-consoles/
- **Karakeep doc:** `vdu9ftedfgunxfw8zxc08675`

*Sigma Star Saga*, the 2005 GBA genre-blender that shuffled a top-down sci-fi RPG with a side-scrolling shmup (random encounters drop you seamlessly into space-battle), gets **Sigma Star Saga DX** from Mighty Rabbit Studios on PC, PS5, Switch. Improvements: better map, fewer random encounters, rebalanced EXP, more save points, plus concept-art gallery, music player, rewind, save states. Digital-only at launch, physical later.

**Verdict:** A 20-year-old GBA game revived right — the genre-mashup battles are the genuinely neat part.

---

## 22. Linus Torvalds tells AI haters to fork off — by theregister.com

![theregister.com](https://image.theregister.com/260119.jpg?imageId=260119&x=0&y=0&cropw=100&croph=100&panox=0&panoy=0&panow=100&panoh=100&width=1200&height=683)
- **Source:** https://www.theregister.com/ai-and-ml/2026/07/15/linus-torvalds-tells-ai-haters-to-fork-off/5271894
- **Karakeep doc:** `bgbvrdajgtu2932hytn6p4qa`

In a Linux kernel mailing-list thread on negative sentiment toward AI, Torvalds drew a line: *"Linux is not one of those anti-AI projects… if somebody has issues with that they can do the open-source thing and fork it."* Or walk away. AI is a tool "just like other tools we use — clearly a useful one… anyone who doubts that clearly hasn't used it." That's a shift from October 2024, when he branded 90% of AI marketing hype. Mic-drop: *"It's not like natural intelligence is always all that great either."*

**Verdict:** Classic Linus — blunt, pragmatic, no patience for purism.

---

## 23. Czy baterie rozwiążą największy problem OZE? — by pl.euronews.com

![pl.euronews.com](https://pl.euronews.com/favicon.ico)
- **Source:** https://pl.euronews.com/europa/2026/07/15/czy-magazyny-energii-uratuja-europejska-transformacje
- **Karakeep doc:** `ckvrd0zxshxxu03xnk4cexbr`

A June 26 EU Energy Council deal signed by the Commission, ministers from 22 member states, and business — a non-binding pledge for ~30–35GW (up to 45GW) of new storage by 2028, doubling storage's share of peak demand from ~5% to ~10%. Today the EU has ~55GW of storage; by 2030 it needs ~200GW. Renewables grow so fast grids get negative prices and production curtailment. Battery costs fell ~93% between 2010 and 2024; Europe installed 21.9GWh in 2024. But real obstacles remain: many countries charge storage fees on *both* draws and returns, and the EU is still addicted to Asian cells.

**Verdict:** A real signal, but "in no way enough" to build a home supply chain.

---

## 24. Pieczone bataty z ciecierzycą, szpinakiem i fetą — by kwestiasmaku.com

![kwestiasmaku.com](https://www.kwestiasmaku.com/sites/v123.kwestiasmaku.com/files/pieczone_bataty_z_ciecierzyca_szpinakiem_feta_00.jpg)
- **Source:** https://www.kwestiasmaku.com/przepis/pieczone-bataty-z-ciecierzyca-szpinakiem-i-feta
- **Karakeep doc:** `xs9gep3fv8mrieychaf8ezii`

Baked sweet potatoes with chickpea, spinach and feta — a vegetarian, gluten-free, one-tray dinner. The article body was blocked on extraction, but the premise is clear: roast bataty, heap chickpeas + wilted spinach + feta. Sweet potato sweetness against salty feta, chickpeas for protein, spinach for greens.

**Verdict:** Comfort food meets clean eating.

---

## 25. I Rebuilt My LinkedIn Carousel System — It Looks Designer-Made — by aimaker.substack.com

![aimaker.substack.com](https://substackcdn.com/image/fetch/$s_!KBJW!,w_1200,h_675,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5c5d398c-ea1e-43a2-beee-d83a1b0b26c7_2752x1536.jpeg)
- **Source:** https://aimaker.substack.com/p/linkedin-carousel-paper-design-mcp
- **Karakeep doc:** `sv7ie7tckqrxubrlr2heajj7`

The author rebuilt their LinkedIn carousel workflow around **Paper Desktop**, a design tool whose MCP lets Claude Code read/write the open design file directly. Old flow: Claude generates a single flat HTML slide — one tiny mistake = another prompt. New flow: Claude Code creates 1080×1350 artboards *inside* Paper (`create_artboard`/`write_html`/`duplicate_nodes`/`set_text_content`/`update_styles`), slides stay editable layers. Figma's MCP is more powerful for product design but worse for carousels.

**The insight:** "HTML becomes the editable design object" is a real UX shift vs flat-pixel carousels.

---

## 26. Wegańskie ciasto drożdżowe z kruszką — by jadlonomia.com

![jadlonomia.com](https://jadlonomia.com/wp-content/uploads/2018/06/IMG_7676_duze-1444x443.jpg)
- **Source:** https://jadlonomia.com/przepisy/weganski-placek-drozdzowy-z-kruszonka/
- **Karakeep doc:** `eivvuvr2j7o4zzoqaklgdhcf`

Vegan crumb yeast cake from Jadłonomia — a "how to trust a yeast cake" guide in recipe form. A vegan yeast cake is *easier*: gluten binds, no eggs needed, eggless dough rises faster. Use type 550 flour, neutral oil, warm-but-not-hot milk. Instant yeast goes in like baking powder. Let it rise twice under tight foil — sealing it makes it rise faster, more evenly. The oven-light trick gets it under an hour. 4 cups flour, 1½ cups plant milk, 8g yeast, sugar, salt; crumble: ½ cup flour, ¼ cup sugar, 40g cold plant fat; 300–400g fruit.

**Verdict:** The comment section is the real value — "can I freeze coconut milk" and the author riffing "drożdżówka has to rise twice."
