# 04 — Module 2: The Model Registry

---

## What's Happening Here

Once you've been tracking experiments for a while, you have a library of trained models. Some are better than others. Some were experiments. Some are candidates for production. A few are actually running in production right now.

How do you keep track of which is which?

A model registry is a central catalog that tracks not just the models you've trained, but their *status* — where each one is in its lifecycle, who approved it, and what it replaced.

Think of it as version control for your models, the same way Git is version control for your code.

---

## Why It Matters for Your Rec Engine

Without a registry, your deployment process looks like this: "I think the model in the `/models/final_v3` folder is the one we're using. Or maybe it was `final_v3_UPDATED`. Let me check with whoever deployed it last."

With a registry, it looks like this: "Version 2.3 is in production. It was promoted on March 15th. Version 2.4 is currently in staging and will replace it after sign-off."

One of these processes scales. The other doesn't.

---

## Model Lifecycle Stages

A model registry typically tracks four lifecycle stages. Every model version exists in exactly one stage at any given time:

**Development**
The model has been trained and logged. It's a candidate — not yet vetted for production. Most models never leave this stage.

**Staging**
The model has been selected as a promotion candidate. It's being tested more rigorously: checked for regressions, validated against a held-out dataset, reviewed for any unexpected behavior. This is your quality gate.

**Production**
The model is live. It's serving real users or downstream systems. There should only ever be one model version in production for a given use case at a time.

**Archived**
The model has been retired. It's no longer in use, but it's preserved in case you need to audit decisions it made or roll back to a previous version in an emergency.

---

## What a Registry Entry Looks Like

```
Model Name:      movie-recommender-svd
Version:         2.3
Stage:           Production
Registered:      2024-03-15
Promoted:        2024-03-18 (from Staging)
Promoted by:     automated pipeline (passed RMSE threshold)

Source Run:      run_20240315_001
RMSE:            0.9147
MAE:             0.7183
Coverage:        84.2%

Artifact Path:   /registry/movie-recommender-svd/v2.3/model.pkl

Description:
  Trained on Jan–Dec 2023 ratings. 100 latent factors.
  Replaced v2.2 (RMSE 0.9401). Improvement confirmed on
  held-out Feb 2024 validation set.

Status History:
  Development   →  2024-03-15
  Staging       →  2024-03-16
  Production    →  2024-03-18
```

---

## The Promotion Decision

Moving a model from staging to production should never be casual. It means replacing what users are currently experiencing.

Promotion should require at least:
- RMSE on a fresh validation set is better than (or comparable to) the current production model
- Coverage hasn't dropped significantly
- A human or automated check has reviewed the evaluation results
- A rollback plan exists: if the new model underperforms, which archived version do you revert to?

---

## Versioning Conventions

Version numbers aren't arbitrary. A common convention:

- **Major version** (v2 → v3): Significant change — new model architecture, new feature set, fundamentally different training approach
- **Minor version** (v2.2 → v2.3): Same architecture, retrained on newer data or with tuned parameters
- **Patch** (v2.3.0 → v2.3.1): Bug fix, metadata correction, no change to model weights

Consistency matters more than the specific convention. Pick one and stick with it across your team.

---

## Hands-On Walkthrough

**Step 1:** Review the sample registry entry above. Identify: what run produced this model? What replaced it? What would you roll back to if v2.3 failed?

**Step 2:** Using the experiment log entry you sketched in Module 1, write a registry entry for that model. Assign it a version number. What stage would it be in right now?

**Step 3:** Think through a promotion scenario: your new model (v2.4) has RMSE 0.903 compared to production v2.3 at RMSE 0.9147. RMSE improved. Coverage dropped from 84% to 79%. Do you promote? What questions do you ask first?

---

## Key Takeaway

A model registry turns a collection of trained files into a managed system. It gives every model version a clear identity, a lifecycle stage, and a documented path from experiment to production.
