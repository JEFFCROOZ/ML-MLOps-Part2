# ML Flow — Part 2: Maintaining Your Recommendation Engine

This is the central workspace for developing, reviewing, and approving all written content for **Part 2 of the ML Recommendation Engine Learning Series** before it is built into code.

Part 1 taught learners how to build a recommendation engine from scratch. **Part 2 teaches them how to keep it alive.**

Copy is written here first, reviewed, then implemented in Streamlit.

---

## How This Workspace Is Organized

- **Site Overview & Voice Guide (Part 2)** — Audience shift, tone continuity, updated navigation map
- **Welcome / Bridge** — Handoff from Part 1, what this course covers, module tiles
- **Modules 1–6** — One page per MLOps stage, with explanations, examples, and hands-on copy
- **Copy QA Checklist** — Final review before any page goes live

---

## Module Structure

| # | Module | Status |
|---|--------|--------|
| 00 | Site Overview & Voice Guide (Part 2) | Draft |
| 01 | Welcome / Bridge from Part 1 | Draft |
| 02 | The MLOps Mindset | Draft |
| 03 | Module 1 — Experiment Tracking | Draft |
| 04 | Module 2 — The Model Registry | Draft |
| 05 | Module 3 — Data Pipelines & Freshness | Draft |
| 06 | Module 4 — Retraining: When and How | Draft |
| 07 | Module 5 — Monitoring, Drift & Response | Draft |
| 09 | Module 6 — The Living System | Draft |
| 10 | Copy QA Checklist | Pending |

---

## Design Principles Carried Forward from Part 1

- Same color palette: `#0e1b26` background · `#106f8a` teal accent · `#e2e8f0` text
- Same fonts: Inter (body) · JetBrains Mono (code)
- Same module structure: What's happening → Why it matters → Example → Hands-on → Key takeaway
- Same voice: knowledgeable friend, not professor
- MovieLens recommendation engine from Part 1 remains the running example

---

## Confirmed Design Decisions

| Decision | Resolution |
|----------|------------|
| Monitoring & Alerting | **Merged** into one module: "Monitoring, Drift & Response" |
| Interactivity style | **Slider-driven simulation.** "Weeks since deployment" slider drives RMSE creep, coverage drop, and badge escalation from warning → critical. |
| MLOps Mindset page | **Pre-module narrative** — lighter, no hands-on section |
| Module count | **6 content modules** |
| Authentication | **Same login as Part 1** — `learner / buildit2024`, independent progress tracking |
| Part 1 link placement | **Callout block at top of Welcome/Bridge page** — teal accent |

---

## Key Decisions Made Before Writing

1. **No tool lock-in.** Concepts are taught first. Tools (MLflow, Airflow, etc.) are named only as examples, never as requirements.
2. **Audience has shifted.** Part 2 readers have already built something. We can use terms like RMSE and SVD without re-explaining them.
3. **Interactivity = slider-driven simulation.** The monitoring dashboard is driven by a "weeks since deployment" slider. Pre-built fake data, no infrastructure required.
4. **Part 1 is assumed.** A teal callout block at the top of the Welcome page links back to Part 1.
5. **6 content modules.** Focus over comprehensiveness. Monitoring and alerting are one page.
