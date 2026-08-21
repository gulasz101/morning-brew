---
date: 2026-08-10
slug: 2026-08-10-morning-brew
tags: digest,karakeep,Cybersecurity
---

# Morning Brew — 2026-08-10
Backfill of 3 bookmarks from my hoard: a meeting-recording platform that left 181k calls wide open, an LLM running inside a PDF file, and a video on the music industry (now transcribed).

## 1. tl;dv — 181,874 meetings wide open, and the CTO ghosted the researcher for six months — by bobdahacker.com

![bobdahacker.com](https://bobdahacker.com/static/images/blogs/tldv/blogHeader.png)

"Too Lazy; Didn't Validate." tl;dv is an AI meeting-recording platform (2M+ users) that drops a bot into your Google Meet/Zoom/Teams call and transcribes + summarizes it — job interviews, sales calls, performance reviews, internal strategy. It's SOC2/GDPR/EU-AI-Act "compliant," hosted in the EU, six compliance badges in a row. The Firestore `meetings` collection has **no tenant isolation**: any authenticated user can enumerate every meeting on the platform — creator email, joinable conference ID, recording status, timestamps. ~1,000 live `recording` calls at any time; an attacker can grab an ID and walk in uninvited. The researcher joined a Malaysian Ministry of Education call (157 participants) and a US university startup session. 181,874 records, 84,312 users, 35,003 domains — government (23 countries), universities, corporate (Mitsui-Soko, HubSpot, Confluent). 1,000+ meetings were public, 715 invitee emails exposed. Even a fun-coded World Cup 2026 "Pick'em" app leaks 19 employee emails with zero auth. Reported Jan 28, the CTO never responded. Six months later, still not fixed — every other collection has tenant isolation, they just *forgot* meetings.

- 🔗 https://bobdahacker.com/blog/tldv-hack
- karakeep id: `yrad8zbl3vbvvap3knvnoxc4`

## 2. llm.pdf — an LLM running inside a PDF — by x.com

![x.com](https://pbs.twimg.com/media/HPIDDh4XEAA0swi.jpg:large)

Dan Kornas's proof-of-concept: a PDF that *runs* an entire LLM instead of just displaying content. Compiles llama.cpp to asm.js via Emscripten, injects the JS into the PDF, and embeds the model as base64 for local inference. Uses a legacy PDF JS injection point. `scripts/generatePDF.py` builds a PDF from a compatible model; GGUF-only, Q8 recommended. Repo: `github.com/EvanZhouDev/llm.pdf`. "Running Doom inside a PDF and now this." It's a stunt — a tiny Q8 GGUF PDF model won't replace your chatbot — but it's a genuinely clever hack of a document format that'll make the right kind of nerd smile.

- 🔗 https://x.com/i/status/2085732944031699242
- karakeep id: `jyns9hrf14pyt4vnuao6e9g4`

## 3. The Music Industry is Broken — every single one of you is the product — by Drew Gooden

![Drew Gooden](https://i.ytimg.com/vi/Yx7baJMQuVA/maxresdefault.jpg)

Drew's hour-long autopsy, and the thesis is bleak enough to make you put down the guitar and pick up a day job: the industry is *more* money than ever and somehow also falling apart. Nobody — not Spotify, not the labels, not Ticketmaster — actually wants the artist to get paid. Based on Liz Pelly's *Mood Machine*, his read is brutal: Spotify has never cared about artists; it's done everything it can to undermine and replace them. The company wasn't even founded as a music service — it was built to sell ads, and if moving more ad units meant streaming pictures of feet, that's what they'd be selling today.

The economics are gross. Spotify's pool model is zero-sum — revenue split by stream share — so every AI slop track bloating the catalog (six of the top fifty trending songs AI-generated, ~40% of daily uploads) is cash pulled straight out of real artists' pockets, and it all runs on music scraped without consent. The smoking gun he keeps circling: fake "artists" (Inley, Breaking Rust, Velvet Sundown) with stock-photo profiles and no bio still land in giant official Spotify playlists the same day they release. Spotify's internal name for the commissioned filler was "perfect fit content." He can't prove Spotify's behind it, but Spotify denied the same thing in 2017 and that was a flat-out lie. Discovery Mode is Payola with extra steps — 30% of revenue on the back end for an algorithm boost that cancels out if everyone opts in. Spotify monetizes the same product in both directions: listeners pay to hear music artists paid to get heard. And the CEO, richer than any musician in history, poured half a billion into military strike drones.

The labels are the kicker. Sony/Universal/Warner own ~70% of all recorded music and craft contracts where artists get a single-digit-to-15% cut, owe money on their own advance, eat made-up "breakage" fees that survived into the MP3 era, and get out-lawyered into pennies when audits go against them. The 2018 IPO gotcha is the most insane detail: with their license expiring right before Spotify went public, the Big Three used total leverage to negotiate their rates *down* — because they owned equity + a Most Favored Nation clause. Lower payouts made Spotify stock worth more, so they cashed out with money their artists have no contractual claim to. Live music is the same disease: the Ticketmaster/Live Nation monopoly controls the venues, the tickets, and the fees, the resale profit never reaches the artist, and a $100 ticket leaves a *successful* touring band $10-20 to split four ways.

Then Drew does the thing that elevates this from rant to reporting: he actually did it. Four years ago he started an instrumental band, recorded an album, released it into the void, and spent $105 on a SubmitHub campaign that returned polite rejections, one playlist, and a ChatGPT summary of his failures — while scam "hit potential" sites scored his song a 74, then gave his hour-long joke track "A Thousand Farts" the highest score yet. His caveats are honest: it's mostly circumstantial on Spotify; one bad SubmitHub campaign isn't an indictment; streaming is genuinely great for *discovery*. His verdict: skip the middlemen, buy direct from artists (Bandcamp, vinyl, CDs), see the free show at the bowling-alley venue. Music's worth making if you want to make it — it's just not easy unless you're a YouTuber with nine years of runway and a hidden band, and even then the payout is 175 monthly listeners. Fuck the industry, but make the art anyway.

- 🎬 Video: "The Music Industry is Broken" — https://youtu.be/Yx7baJMQuVA
- karakeep id: `y42cezlu74akrjmmgljvt6ru`

---

*Morning Brew digest — 2026-08-10. Tags: cybersecurity, LLM, PDF, music industry.*
