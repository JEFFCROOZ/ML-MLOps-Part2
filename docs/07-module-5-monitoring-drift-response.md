# 07 — Module 5: Monitoring, Drift & Response

> **Design note:** This is the merged version of the former "Monitoring & Drift" and "Alerting & Response" modules. The interactive artifact for this page is a simulated Streamlit monitoring dashboard — pre-built with realistic fake data. No live infrastructure required.

---

## What's Happening Here

Your model is in production. Users are receiving recommendations. Everything looks fine.

But is it?

Monitoring is the practice of continuously measuring your model's health — not just once at evaluation time, but every day it's running. The goal is to catch problems early, before they become visible to users.

And when something does need attention, alerting is what compresses the time between "something went wrong" and "someone is fixing it."

This module covers both: how to watch your system, how to recognize when something's wrong, and what to do about it.

---

## What Is Drift?

Drift is when the relationship between your model's inputs and its expected outputs changes over time in ways the model wasn't trained to handle. It comes in two forms:

**Data drift (input drift)**
The distribution of incoming data changes. Users are rating different genres than they used to. New movies skew toward categories that were underrepresented in training data.

*Movie example:* Your model trained on data where action movies were 18% of ratings. A year later, action is 31% of all ratings. The model's recommendations for action fans become increasingly unreliable.

**Concept drift (label drift)**
The underlying relationship between inputs and the right answer has changed — even if the data distribution looks similar. What users *want* from a recommendation has shifted in ways the model's signals no longer capture.

*Movie example:* Five years ago, high average ratings strongly predicted that a user would enjoy a film. Today, users weight recent reviews and social signals more heavily. The model optimizes for a target that no longer maps to satisfaction.

---

## Why Drift Is Dangerous

Neither type causes your model to crash. Both cause it to quietly become less useful.

The predictions keep coming. The format is correct. No errors are thrown. But they're wrong more often — and by the time users notice, the problem has usually been building for weeks.

---

## What to Monitor

A practical monitoring setup for a recommendation engine tracks four categories:

**Model performance**
- RMSE and MAE on a fresh weekly evaluation batch
- Prediction distribution (are predictions becoming more uncertain over time?)

**Data quality**
- Rating volume per period — is the expected volume arriving?
- Feature distribution snapshots — is the genre mix, rating scale, or user activity pattern shifting?
- Pipeline freshness — is your data pipeline still running?

**Recommendation quality**
- Coverage: what percentage of the catalog is being recommended?
- Diversity: are recommendations spreading across genres or clustering?
- Novelty: is the system surfacing new things, or repeating itself?

**User behavior** (when available)
- Engagement after following a recommendation
- Rating behavior post-recommendation

---

## Simulated Monitoring Dashboard

*Interactive Streamlit artifact — slider controls time progression.*

**The interaction:** A single slider labeled "Weeks since deployment" (range: 1–16). As the learner drags it forward, all metrics update in real time. The experience of drift is felt, not just described.

**What changes as the slider moves:**

| Week Range | RMSE | Coverage | Genre Drift | Alert Status |
|------------|------|----------|-------------|--------------|
| Weeks 1–3 | 0.91–0.93 | 84–83% | Minimal | ✅ Healthy |
| Weeks 4–6 | 0.94–0.97 | 82–80% | Action +4% | ⚠️ Warning |
| Weeks 7–9 | 0.98–1.02 | 79–76% | Action +8% | ⚠️ Warning |
| Weeks 10–13 | 1.03–1.08 | 74–70% | Action +12% | 🔴 Critical |
| Weeks 14–16 | 1.09–1.14 | 68–63% | Action +18% | 🔴 Critical + retrain triggered |

**Charts rendered:**
1. **RMSE Trend** — Line chart, 1 data point per week up to current slider position. Threshold line at 1.05 drawn in red.
2. **Coverage %** — Line chart with threshold at 80% (warning) and 70% (critical). Color fills change as thresholds are crossed.
3. **Genre Distribution Drift** — Grouped bar: baseline distribution vs. current week distribution. Action bar grows visibly as slider advances.
4. **Alert Status Card** — Container block that changes color and copy based on alert level. Green → yellow → red.
5. **Weekly Health Summary** — Metric blocks showing RMSE, Coverage, Pipeline Status, and Last Retrain date. Delta values show change from baseline.

**Implementation notes:**
- All data pre-seeded in a pandas DataFrame — 16 rows, one per week, hardcoded realistic values
- Slider position = DataFrame row index for current metrics
- Charts use `.loc[:slider_week]` to show progressive history
- Alert logic: simple `if/elif` on RMSE and coverage values to set badge level and copy
- Color system: `#166534` green, `#991b1b` red, `#106f8a` teal, warning uses amber `#92400e`

---

## What Makes a Good Alert

When a metric crosses a threshold, the alert that fires should be:

**Actionable** — It tells you something you can respond to. "RMSE is 0.923" is information. "RMSE has exceeded the threshold for 3 consecutive weeks and automated retrain has not resolved it" is an alert.

**Specific** — It names the metric, the current value, the threshold, and the most likely responsible component.

**Low noise** — If every minor fluctuation fires an alert, people stop reading them. Alert fatigue is real.

**Routed correctly** — The right person receives it. A 3am pipeline failure needs a message — not necessarily a wake-up call to the whole team.

---

## Alert Levels

| Level | Meaning | Example |
|-------|---------|---------|
| Info | Within normal range, logged for visibility | RMSE at 0.921 vs. baseline 0.915 — slightly elevated |
| Warning | Outside normal range, review within 48 hours | Coverage dropped to 78% for second consecutive week |
| Critical | Something may be actively broken, needs prompt attention | Pipeline hasn't run in 36 hours |
| Emergency | Production is impacted, escalate immediately | Model endpoint returning errors on 15% of requests |

---

## What a Real Alert Looks Like

```
[WARNING] movie-recommender — Coverage Degradation
Triggered: 2024-03-20 08:15 UTC

Metric:     Catalog coverage
Current:    76.4%
Threshold:  80% (warning level)
Baseline:   84.2% (at v2.3 launch)
Trend:      Declining for 3 consecutive weeks

Suggested actions:
  1. Check data pipeline — are new movie metadata records being ingested?
  2. Review genre distribution — are new releases in underrepresented genres?
  3. If pipeline is healthy, consider accelerating next scheduled retrain.

Next scheduled retrain: 2024-03-24 (Sunday)
This alert will escalate to CRITICAL if coverage falls below 70%.
```

---

## The Runbook

A runbook documents the response steps for known alert types. It answers: "someone got notified at 2am — what do they do?"

Runbooks don't need to be long. A basic one for a recommendation engine might cover five or six failure modes. Here's one entry:

**Alert: Pipeline has not run in 24+ hours**
1. Check pipeline scheduler — is the job still enabled?
2. Check error logs from the last failed run
3. Verify source data is available and accessible
4. If source is healthy, restart the pipeline manually
5. If source is down, notify the upstream data owner and log the incident
6. Once pipeline recovers, confirm data freshness metric restores to normal
7. If retrain is overdue, trigger manually after freshness is confirmed

The goal isn't to document everything. It's to document the things that happen most often, so whoever responds has a starting point instead of a blank page.

---

## Hands-On Walkthrough

**Step 1:** Explore the simulated monitoring dashboard. Find the week where RMSE first crossed the warning threshold. What else changed that week?

**Step 2:** Read the sample alert. Evaluate it: is it actionable? Specific? Would you act on it or file it away?

**Step 3:** Write a one-line alert definition for the top three things most likely to go wrong in your own recommendation engine. For each: what metric, what threshold, what level?

**Step 4:** Write a two-step runbook entry for one of those alerts. What's the first thing you check? What's the second?

---

## Key Takeaway

Drift is silent and gradual. Monitoring catches it. Alerting gets the right person's attention. A runbook gives them a path forward. All three are necessary — and none of them require sophisticated infrastructure to start.
