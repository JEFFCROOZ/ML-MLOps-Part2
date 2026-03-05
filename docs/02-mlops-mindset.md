# 02 — The MLOps Mindset

> **Design note:** This is a pre-module narrative page — not a numbered content module. It sits between the Welcome/Bridge and Module 1. Styled lighter, more conversational. No hands-on section. No key takeaway box. Think of it as the orientation layer — the same role "The Three Roles" played in Part 1.

---

## What's Happening Here

Before we get into any specific technique, we need to talk about a shift in thinking.

When you were building your recommendation engine in Part 1, you were thinking like a builder. You had a goal — train a model that makes good recommendations — and a finish line: a working result.

Operating an ML system requires a fundamentally different mindset. There is no finish line.

Instead, you're running a *system* — one that needs to stay accurate as the world changes, handle new data reliably, and recover gracefully when something breaks. The model you trained is no longer just a project you finished. It's infrastructure you're responsible for.

---

## Why This Matters More Than It Sounds

Think about the model you built in Part 1. It was trained on a snapshot of user preferences at a specific point in time. The moment training finished, that model started aging.

New movies get released. User tastes evolve. Rating patterns shift. The model doesn't know any of this — it's still making recommendations based on data that's growing older every day.

Without an operational mindset, you'd only notice the problem when something feels wrong. With it, you've already anticipated this and built systems to catch it early.

---

## The Core Shift

| Project Thinking | Systems Thinking |
|------------------|------------------|
| Has a start and end date | Runs continuously |
| "Done" when the model trains | "Stable" is the goal, not "done" |
| Failure is an edge case | Failure is an expected event to plan for |
| Accuracy measured once at evaluation | Accuracy monitored continuously |
| Data is static | Data is always changing |

This isn't a criticism of how you approached Part 1. That project mindset was exactly right for learning. But the moment a model is serving real users, the project is over and the operation begins.

---

## The MLOps Loop

MLOps is often described as a loop, not a line. Each module in this course covers one stage of that loop:

```
Track your experiments        →  Module 1
Register and version models   →  Module 2
Keep your data fresh          →  Module 3
Know when to retrain          →  Module 4
Monitor for drift             →  Module 5
Close the loop, repeat        →  Module 6
```

By the time you reach Module 6, you'll see how each piece connects — and why skipping any one of them makes the others less effective.

---

## A Word on Scale

You don't need to build all of this at once, and you don't need a large team to do it well. A solo developer with one model can implement a lightweight version of this loop that's still far better than nothing.

The concepts are the same at every scale. The implementation differs. This course focuses on the concepts — so that when you do sit down to build, you know exactly what you're building toward.
