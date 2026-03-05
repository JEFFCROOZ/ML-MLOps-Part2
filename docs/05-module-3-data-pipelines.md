# 05 — Module 3: Data Pipelines & Freshness

---

## What's Happening Here

Your model is only as good as the data it was trained on. And that data has an expiration date.

The MovieLens dataset you used in Part 1 is a snapshot — ratings collected up to a certain point in time, frozen there. In a real production system, new ratings come in every day. New users sign up. New movies get released. The landscape is constantly shifting.

A data pipeline is the infrastructure that keeps your training data current. It's the plumbing that moves raw data from wherever it's collected into the form your model can learn from.

---

## Why It Matters for Your Rec Engine

Imagine your movie recommendation engine was trained in January. It's now September. Here's what's changed:

- 50+ new films have been released — none of them in your training data
- Your most active users have rated 200+ new movies since January
- A few older movies have had a resurgence (a sequel released, or a director won an award) and user ratings have shifted

Your model can't recommend any of those new movies. It doesn't know they exist. And the users who have changed their tastes are still being served recommendations based on their January preferences.

Fresh data fixes this. But fresh data only helps if your pipeline is reliably delivering it.

---

## What a Data Pipeline Does

At its core, a data pipeline moves data through a sequence of transformations:

```
Raw source data  (new ratings, user events, content metadata)
       ↓
Ingestion layer  (collect and store the raw data as-is)
       ↓
Transformation   (clean, join, normalize — the work you did in Part 1, automated)
       ↓
Feature store    (ready-to-use inputs for model training)
       ↓
Training dataset (the final, versioned snapshot the model learns from)
```

In Part 1, you did all of this manually — you loaded CSVs, merged them, built the user-item matrix. A data pipeline automates every one of those steps on a schedule.

---

## Batch vs. Streaming

There are two broad approaches to data pipelines, and which one you need depends on how fresh your data needs to be:

**Batch pipelines** run on a schedule — hourly, daily, weekly. They collect everything that happened since the last run and process it together. This is appropriate for most recommendation engines: you don't need real-time ratings to make good recommendations.

**Streaming pipelines** process data as it arrives, in near real-time. This is necessary when freshness is critical — for example, if a user rates a movie and you want that preference reflected in their next recommendation within minutes.

For a movie recommendation engine, batch is almost always sufficient. For something like a news feed, streaming becomes necessary.

---

## Data Freshness Metrics

Freshness isn't binary. It's a spectrum, and you should be able to measure it. Common freshness metrics:

| Metric | What It Measures | Healthy Threshold (example) |
|--------|------------------|-----------------------------|
| Data lag | Time since last successful pipeline run | < 25 hours for daily batch |
| New item coverage | % of recently released movies in the training data | > 90% within 7 days of release |
| Active user recency | % of users whose latest rating is within 90 days | > 70% |
| Rating volume trend | # of new ratings per week — is it stable? | Baseline ± 15% |

If your pipeline hasn't run in 48 hours and your threshold is 25, that's a signal. If new movie coverage drops to 60%, your recommendations for current releases are unreliable.

---

## What Can Go Wrong

Data pipelines are frequently the most fragile part of an ML system. Common failure modes:

- **Source data changes format** — The upstream system adds a column, renames a field, or changes how genres are encoded. Your transformation step breaks silently.
- **Pipeline runs but delivers empty data** — A bug in your ingestion step means the table is updated but contains no new rows. Your training data looks current but isn't.
- **Schema drift** — The shape of your data changes gradually over time in ways that aren't caught until they cause a downstream failure.
- **Late data** — Some events are logged with delays (mobile apps sync when connected). Your pipeline may cut off data that arrives 2 hours after the scheduled run.

None of these are edge cases. They're regular occurrences in production systems.

---

## Hands-On Walkthrough

**Step 1:** Look at the data freshness metrics table above. For each metric, answer: how would you actually measure this for your MovieLens-based system? What would you query? What would trigger an alert?

**Step 2:** Trace through the pipeline diagram. Identify which step you handled manually in Part 1. What would automating that step require?

**Step 3:** Consider the failure modes listed. Which one do you think is most likely to happen in a real system you build? How would you detect it before it affects your model?

---

## Key Takeaway

A model trained on stale data makes stale recommendations. Data pipelines are what keep your system connected to reality — and pipeline reliability is just as important as model accuracy.
