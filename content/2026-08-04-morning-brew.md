---
date: 2026-08-04
slug: 2026-08-04-morning-brew
tags: digest,karakeep,management,artificial-intelligence,technology
---
# Morning Brew — 2026-08-04

Hoarded 3 bookmarks on 2026-08-04 — three articles, no video. The day splits cleanly down the middle: one genuinely useful piece of management brain-science about why your employees lose their minds over a desk move, and two AI-economics pieces — Miro's marketing-flavored case study on ephemeral test environments for agentic coding, and the NYT's "tokenomics" explainer on how companies are finally realizing AI bills are real and unmonitored. One of those is worth your time; the other two are variations on "tech spending is weird now."

---

## 1. Dealing with Surprising Human Emotions: Desk Moves
- **Source:** https://larahogan.me/blog/desk-moves/
- **Karakeep doc:** `w8yrpp0bfmnayoekkbpp8jye`

Lara Hogan's 2017 evergreen on why something as banal as moving a desk triggers full amygdala meltdowns — and what to do about it. The framework is Paloma Medina's **BICEPS** model of human core needs: **Belonging, Improvement/Progress, Choice, Equality/Fairness, Predictability, Status.** A desk move quietly threatens all six, so a person who looks like they're being dramatic about furniture is usually having one of their core needs kneecapped.

Working through each need: **Belonging** — a desk is how someone anchors into their team; getting separated from their people reads as being abandoned. **Improvement/Progress** — a move with no visible strategic purpose feels like a pointless distraction from the impact they're chasing. **Choice** — dictated seating strips autonomy, and in a growing company it reads as the first sign of more control-loss to come. **Equality/Fairness** — where you sit visibly marks who the "cool kids" are (Paloma once pointed out to Hogan that Engineering always sat in the good spot while HR and Finance got leftovers). **Predictability** — changing the routine is a direct hit for the analytical, data-driven types who live on sameness. **Status** — where you sit signals your worth, and everyone knows it.

Her manager playbook: name the change early, tie it to broader strategy, hand people real choices (when to move, how to decorate, how to celebrate), don't gaslight them about feeling it, and give long lead times. The sharpest line buried at the end: supporting people doesn't mean acquiescing — it means understanding and communicating clearly. And her brutal-but-honest closer for startup folks: change is the constant, the company will be a different company in N months, and it's on the employee to decide if that stage is still right for them — not on the manager to bend reality for each individual.

**Verdict:** The best article on the day, no contest. The BMEPS framing is a genuinely usable lens — every engineer with a pissed-off report or an irrational reaction of their own should read it. Caveats: it's 2017 vintage, the prose is a touch corporate-couch, and it's aimed at first-line managers who think "it's just logistics." But the core insight — people react to threats to core needs, not to the change itself — is timeless and worth more than most of what's published on leadership this year.

---

## 2. How Miro Tests Agentic Features at Scale with Signadot
- **Source:** https://www.signadot.com/case-studies/how-miro-builds-and-tests-agentic-features-at-scale/
- **Karakeep doc:** `rlnojlgzfd28nbezerfgqxbg`

A sponsored case study — and it reads like one — in which Miro's AI platform team adopts **Signadot** to solve the "one shared test environment" bottleneck. The problem is real and identifiable: Miro runs ~250 microservices across 70+ teams, mid-migration from an EC2 monolith to Kubernetes + Istio, with heavy shared state over Kafka and Temporal. Their old setup capped end-to-end integration at ~15 fixed environments, meaning only ~15 concurrent integration sessions and every other PR queued — plus devs colliding on the same slot and overwriting each other mid-test.

Signadot's answer: **ephemeral sandboxes** that fork workloads behind an Istio mesh and route traffic only for your request, so you test against real services and real traffic instead of mocks. Results claimed: consolidating ~15 fixed environments to ~3, lifting concurrency roughly 10x at peak, 50% of teams testing daily in sandboxes, and projected millions in annual savings from retiring legacy environments they'd been carrying for years.

The agentic angle is the actual interesting part. Miro uses coding agents (Claude, Cursor) to build agentic features, and they built internal "skills" that teach agents to spin up whole multi-service test environments on demand — "Claude, set up the infra and run this eval against my microservice change." The loop is closed: the agent writes code, spins up a sandbox, drives the change end-to-end against live traffic, debugs, and opens a validated PR. No human babysitting, no staging contention. Signadot has since shipped its own `signadot-validate` skill and "Plans" — reusable validation workflows for exactly this.

**Verdict:** Skim it if you care about ephemeral environments or agentic CI/CD, because the sandbox-forking + GitOps-routing model is genuinely the right architecture for testing agent-generated code without blowing up staging. But treat every number as vendor marketing — it's a sponsored testimonial, the "millions saved" is a projection, and the whole thing is written to sell Signadot to whichever platform engineer reads it. The genuinely useful takeaway is narrow: the closed-loop agent-writes-code → spins-env → validates → ships pattern is where agentic engineering is going, and this is a clean description of one real implementation.

---

## 3. NYT — What Are Companies Getting for All That A.I. Spending?
- **Source:** https://www.nytimes.com/2026/08/03/business/economy/ai-spending-tokenomics.html
- **Karakeep doc:** `j4pkl40maowzwn6e3ywuizqa`

Lydia DePillis's NYT piece on the emergence of "tokenomics" — the new(ish) discipline of measuring return on AI spending. The setup: companies rushed to embrace AI and told employees to use it as much as possible, then the bills arrived. AI usage is metered in **tokens**, and it gets expensive shockingly fast, so the corporate pendulum swung from "maximize adoption" to "control costs." Unlike earlier tech like cloud computing, AI has **no standardized pricing, no transparent benchmarks, no accepted way to measure ROI** — so nobody can actually say whether the spend was worth it.

Enter tokenomics: industry groups pushing common standards for price/performance transparency, plus a toolkit of practices — tools to monitor token spend against business outcomes (features delivered, productivity gains), and the push toward AI as "virtual labor" (benchmark AI spend against a headcount of employees and weigh human+AI combined output). Providers shave costs with things like cached tokens. But the fundamentals stay shaky: token prices vary wildly by provider, future price changes could crater adoption, and there's a shortage of professionals who can actually deploy AI effectively. Economists and businesses alike still can't answer whether AI is a productivity multiplier, an augmenter, or an expensive experiment with uncertain returns.

**Verdict:** Competent, borderline-obvious NYT framing of a real problem. The useful kernel is that the AI gold-rush billing model has quietly become a cost center nobody priced correctly, and "tokenomics" is the emergent attempt to attach CFO-grade discipline to it. It's a solid summary if you haven't watched the space, but the analysis is thin — it describes the problem and gestures at "standards" without getting concrete about who's building them or what good looks like, and the "virtual labor" comparison is treated as a novelty rather than interrogated for how it breaks down (an AI that replaces zero headcount but burns tokens is just a cost). More framing than substance.
