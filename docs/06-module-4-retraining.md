# 06 — Module 4: Retraining: When and How

---

## What's Happening Here

At some point, your current production model is no longer performing well enough. The question isn't whether you'll need to retrain — it's when, and what triggers that decision.

Retraining is the process of training a new model version on updated data and, if it performs better, promoting it to replace the current production model. Done manually on an ad hoc basis, it's tedious and error-prone. Done well, it becomes an automated part of your operational rhythm.

---

## Why It Matters for Your Rec Engine

Your SVD model from Part 1 learned user taste patterns from historical ratings. Those patterns are real, but they're not permanent. People's tastes change. Movie culture evolves. Seasonal viewing patterns shift.

A model that isn't retrained periodically starts recommending in ways that feel slightly off — surfacing movies the user rated years ago as if they're still top-of-mind, or missing newer films entirely.

The longer you wait to retrain, the wider the gap between what your model knows and what's actually true.

---

## The Three Retraining Triggers

There's no universal rule for when to retrain. In practice, teams use one or more of three trigger types:

**1. Time-based triggers**
Retrain on a fixed schedule — weekly, monthly, quarterly. Simple to implement and reason about. The risk: you might retrain when nothing has changed, or wait too long when things have changed a lot.

*Example:* "Every Sunday at 2am, kick off a retraining run with the past 12 months of ratings."

**2. Performance-based triggers**
Retrain when a monitoring metric crosses a defined threshold. This is more intelligent than time-based triggering but requires a working monitoring system to be in place first.

*Example:* "If RMSE on the weekly evaluation batch rises above 1.05, automatically queue a retraining run."

**3. Data-based triggers**
Retrain when the training dataset has changed significantly — enough new data has accumulated, or the data distribution has shifted measurably.

*Example:* "Retrain when new ratings volume reaches 10,000 since the last training run." Or: "Retrain when genre distribution shifts by more than 15% from the baseline."

---

## Why You Can't Just Retrain Constantly

Retraining isn't free. It consumes compute resources, takes time, and introduces risk — every new model version has to be evaluated before it can replace the current one.

Over-frequent retraining can also destabilize your recommendations. If a user's top recommendation changes every day because the model is retrained daily on tiny increments of new data, the experience feels inconsistent.

The goal is a cadence that keeps the model fresh without being disruptive. For most recommendation engines, weekly or bi-weekly retraining is a reasonable starting point.

---

## What Automated Retraining Looks Like

A fully automated retraining pipeline has these stages:

```
1. Trigger fires (time, performance, or data threshold)
        ↓
2. Fresh training dataset is assembled by the data pipeline
        ↓
3. Model trains with the same architecture and parameters as the current production model
        ↓
4. New model is evaluated against a held-out validation set
        ↓
5. Results are compared to the current production model
        ↓
6a. If better: new model is registered, promoted to staging, then production
6b. If not better: run is logged, production model is unchanged, alert is sent for review
```

Steps 3–6 are where experiment tracking and the model registry become essential. Without them, automation is impossible — you have nowhere to log the run, no registry to promote into, and no baseline to compare against.

---

## The Rollback Plan

Every promotion needs a rollback path. Before you promote a new model to production, you should know the answer to: *what do we do if this model turns out to be worse in production than it was in evaluation?*

Typically this means:
- The previous production model version is archived, not deleted
- Your deployment system can revert to it with a single action
- Your team knows who makes that call and under what conditions

Rollback rarely happens. But the plan needs to exist before you need it — not after.

---

## Hands-On Walkthrough

**Step 1:** For your Part 1 recommendation engine, which retraining trigger would you choose? Time, performance, or data? Write down your reasoning.

**Step 2:** Define a specific threshold for that trigger. Be concrete: not "when RMSE gets worse" but "when RMSE exceeds X on the validation set."

**Step 3:** Trace through the automated retraining pipeline above. Identify which steps require experiment tracking (Module 1) and which steps require the model registry (Module 2). See how they connect?

---

## Key Takeaway

Retraining isn't a one-time event — it's a recurring operation. The teams that do it well have defined triggers, automated pipelines, and rollback plans in place before they ever need them.
