# 00 — Site Overview & Voice Guide (Part 2)

> **Internal reference document.** Not published to the website. Defines how we write for Part 2, who we're writing for now, and what has changed from Part 1.

---

## What This Site Is

An interactive, self-paced learning platform that walks users through the operational side of machine learning — what happens *after* the model is built. Part 2 assumes the learner has completed Part 1 or has equivalent experience building a recommendation engine.

Every concept is grounded in the same MovieLens recommendation engine built in Part 1. No new dataset is introduced. The focus shifts from construction to stewardship.

---

## How This Site Differs from Part 1

| Dimension | Part 1 | Part 2 |
|-----------|--------|--------|
| Primary goal | Build a working rec engine | Keep that engine reliable over time |
| Audience assumption | No ML experience required | Has built something; knows RMSE, SVD, train/test splits |
| Interactivity | Live code against real data | Realistic artifacts — logs, dashboards, registry views |
| Tone baseline | Fully welcoming, zero jargon | Still warm, slightly more peer-level |
| Tool stance | No tools assumed | Tools named as examples, never required |

---

## Who We're Writing For (Updated)

**Primary audience:** Aspiring data engineers and data scientists who have built or are building a recommendation engine and now want to understand how to manage it as a living system.

**What they know now:** They've run through a full ML workflow at least once. They understand data preparation, model training, evaluation metrics like RMSE, and the basic idea of deployment.

**What they don't know yet:** How to version models, track experiments systematically, detect when a model is degrading, automate retraining, and build the operational infrastructure that makes ML sustainable.

**What they want:** To feel like a practitioner, not just a student. To understand the operational side of ML without being overwhelmed by enterprise tooling.

---

## Voice & Tone (Continuity)

The voice does not change. Same knowledgeable friend. Same warmth. Same clarity.

What changes is the assumed starting point. We no longer explain what a rating matrix is. We do not re-define RMSE. We treat the learner as someone who has done the work — because they have.

**Tone pillars (unchanged):**
- **Warm** — Users are still welcome, still encouraged
- **Clear** — One idea per sentence
- **Honest** — We say when something is genuinely complex
- **Encouraging** — Progress still gets celebrated
- **Practical** — Every concept connects back to the model they already built

**New in Part 2:**
- **Peer-level** — We can say "you already know" without it feeling like a test
- **Systems-thinking** — We talk about pipelines, cycles, and feedback loops — not just individual steps

---

## What We Do NOT Do

- Re-teach what Part 1 already covered (ratings, SVD, cosine similarity, RMSE)
- Require learners to sign up for any paid tool
- Advocate for any specific vendor or platform
- Suggest that the concepts here only apply to large organizations — they apply at any scale
- Use the word "simply" or "just" to describe anything that requires actual engineering judgment

---

## Color Palette (Unchanged from Part 1)

| Role | Hex | Used For |
|------|-----|----------|
| Background | `#0e1b26` | Page background |
| Surface | `#162230` | Cards, panels, code blocks |
| Accent (Teal) | `#106f8a` | Buttons, links, highlights |
| Success (Green) | `#166534` | Completed steps, correct outputs |
| Alert (Red) | `#991b1b` | Warnings, drift alerts |
| Text | `#e2e8f0` | All body copy |

---

## Site Navigation Map

```
Login (same as Part 1)
  └── Home / Bridge
        ├── The MLOps Mindset
        ├── Module 1: Experiment Tracking
        ├── Module 2: The Model Registry
        ├── Module 3: Data Pipelines & Freshness
        ├── Module 4: Retraining — When and How
        ├── Module 5: Monitoring, Drift & Response
        └── Module 6: The Living System
```

---

## Module Design Pattern (Same as Part 1)

1. **What's happening here** — Plain-language explanation of the stage
2. **Why it matters for your rec engine** — Grounded in the movie example
3. **Example** — A realistic artifact (log entry, registry view, alert message)
4. **Hands-on** — Guided walkthrough or conceptual exercise
5. **Key takeaway** — One sentence that captures the main lesson

---

## Legal & Compliance (Unchanged)

- No offensive, discriminatory, or disparaging language
- No financial or medical advice
- No claims that the site's output is production-ready without user validation
- All datasets referenced are publicly available and properly attributed
- No tool or vendor is presented as the only valid choice
