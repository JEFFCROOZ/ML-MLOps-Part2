# 03 — Module 1: Experiment Tracking

---

## What's Happening Here

Before your model ever goes anywhere near production, you've probably run dozens of experiments. You tried different training parameters. You compared content-based filtering to collaborative filtering. You tweaked the hybrid weights and checked whether RMSE improved.

Here's the question: do you remember what you tried?

Experiment tracking is the practice of recording every meaningful training run — what data you used, what parameters you set, and what results you got — so that you always know where your best model came from and how to reproduce it.

Without it, you're building on memory. With it, you're building on evidence.

---

## Why It Matters for Your Rec Engine

Imagine you ran three versions of your SVD model:

- Version A: 50 latent factors, RMSE 0.94
- Version B: 100 latent factors, RMSE 0.91
- Version C: 100 latent factors, trained on 6 months of data instead of 12, RMSE 0.97

Version B is clearly best. But a month later, when you're retraining on fresh data, do you remember that Version B used 100 latent factors? Do you remember that reducing the training window hurt performance?

Experiment tracking means you don't have to remember. It's all logged.

---

## What an Experiment Log Contains

A well-structured experiment log records four categories of information for every training run:

**1. Parameters** — What you configured before training
- Number of latent factors (e.g., 100)
- Learning rate (e.g., 0.005)
- Regularization strength (e.g., 0.02)
- Training data date range (e.g., Jan 2023 – Dec 2023)

**2. Metrics** — What you measured after training
- RMSE on the test set (e.g., 0.91)
- MAE (e.g., 0.71)
- Coverage: what percentage of the catalog can be recommended (e.g., 84%)
- Training duration (e.g., 4m 12s)

**3. Artifacts** — What got saved
- The serialized model file
- The training dataset reference
- Evaluation plots (predicted vs. actual scatter)

**4. Context** — Everything else
- Who ran it (or what automated process did)
- When it ran
- Any notes about why it was run

---

## What a Real Experiment Log Entry Looks Like

Here's what a single tracked run might look like in a structured experiment log. The exact format varies by tool, but the information is always the same:

```
Run ID:          run_20240315_001
Timestamp:       2024-03-15 09:42:11
Model Type:      SVD (Collaborative Filtering)
Dataset:         MovieLens 100K — Jan 2023 to Dec 2023

Parameters:
  n_factors:     100
  lr_all:        0.005
  reg_all:       0.02
  n_epochs:      20

Metrics:
  RMSE:          0.9147
  MAE:           0.7183
  Coverage:      84.2%
  Training time: 4m 12s

Artifacts:
  model_file:    svd_v2_20240315.pkl
  eval_plot:     eval_scatter_20240315.png

Notes:
  Increased n_factors from 50 to 100. RMSE improved by 0.03.
  No significant change in training time. Promoting to staging.
```

Nothing here requires a sophisticated tool. You could maintain this in a spreadsheet. The discipline matters more than the format.

---

## Tools Worth Knowing

When your volume of experiments grows, manual logging doesn't scale. Tools like **MLflow Tracking**, **Weights & Biases**, and **Neptune** are purpose-built for this. They auto-capture parameters and metrics, store artifacts, and give you a UI for comparing runs side by side.

We're not prescribing any of them. But knowing they exist — and understanding what problem they solve — is part of being an effective ML practitioner.

---

## Hands-On Walkthrough

**Step 1:** Review the sample experiment log above. Notice what's recorded and why each field matters.

**Step 2:** Think back to the experiments you ran in Part 1. What parameters did you use for your SVD model? What was your final RMSE? Could you reproduce that exact result from memory?

**Step 3:** Sketch what your own experiment log entry would look like for the best-performing model from Part 1. Use the structure above as a template.

This is the exercise. Not running code — building the habit of documentation.

---

## Key Takeaway

Experiment tracking is the foundation of everything that comes next. You can't version a model you can't reproduce. You can't compare models you didn't log. Start tracking from run one.
