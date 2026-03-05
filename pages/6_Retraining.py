import streamlit as st
from utils.styles import (
    inject_global_css, require_auth, section_break,
    takeaway, bts, step_label, nav_buttons
)

st.set_page_config(
    page_title="Retraining — MLOps Part 2",
    page_icon="🔄",
    layout="centered",
    initial_sidebar_state="collapsed",
)

inject_global_css()
require_auth()

# ── Header ───────────────────────────────────────────────────────────────────
st.markdown(
    "<p style='color:#106f8a; font-size:0.85rem; font-weight:600; "
    "text-transform:uppercase; letter-spacing:0.08em;'>Module 4</p>",
    unsafe_allow_html=True,
)
st.markdown("## Retraining: When and How")
st.markdown(
    "At some point, your current production model is no longer performing well enough. "
    "The question isn't *whether* you'll need to retrain — it's *when*, and what triggers "
    "that decision."
)

section_break()

# ── Why retrain ───────────────────────────────────────────────────────────────
st.markdown("### Why models need retraining")
st.markdown(
    "Your SVD model from Part 1 learned user taste patterns from historical ratings. "
    "Those patterns are real — but they're not permanent."
)
st.markdown(
    "A model that isn't retrained periodically starts recommending in ways that feel "
    "slightly off. It surfaces movies the user rated years ago as if they're still top-of-mind. "
    "It misses newer releases entirely. The longer you wait, the wider the gap between "
    "what your model knows and what's actually true."
)

section_break()

# ── Three triggers ────────────────────────────────────────────────────────────
st.markdown("### The three retraining triggers")
st.markdown(
    "There's no universal rule for when to retrain. In practice, teams use one or more "
    "of three trigger types:"
)

trigger_tab1, trigger_tab2, trigger_tab3 = st.tabs(
    ["⏱️ Time-based", "📊 Performance-based", "📦 Data-based"]
)

with trigger_tab1:
    st.markdown("#### Retrain on a fixed schedule")
    st.markdown(
        "Simple to implement and easy to reason about. The risk: you might retrain when "
        "nothing meaningful has changed, or wait too long when things have changed a lot."
    )
    st.markdown("""
    <div class="module-tile">
        <p style="color:#e2e8f0; font-style:italic; margin-bottom:0.5rem;">Example trigger:</p>
        <p>"Every Sunday at 2am, kick off a retraining run with the past 12 months of ratings."</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("**Best for:** Stable datasets where you're comfortable with weekly or monthly staleness.")

with trigger_tab2:
    st.markdown("#### Retrain when a metric crosses a threshold")
    st.markdown(
        "More intelligent than time-based triggering — but requires a working monitoring "
        "system to be in place first. The alert fires; the retrain kicks off."
    )
    st.markdown("""
    <div class="module-tile">
        <p style="color:#e2e8f0; font-style:italic; margin-bottom:0.5rem;">Example trigger:</p>
        <p>"If RMSE on the weekly evaluation batch rises above 1.05, automatically queue a retraining run."</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("**Best for:** Production systems where performance degradation has a real cost.")

with trigger_tab3:
    st.markdown("#### Retrain when the data has changed significantly")
    st.markdown(
        "Retrain when your training dataset has grown or shifted enough to justify it — "
        "not based on time or performance, but on how much the data has actually moved."
    )
    st.markdown("""
    <div class="module-tile">
        <p style="color:#e2e8f0; font-style:italic; margin-bottom:0.5rem;">Example triggers:</p>
        <p>"Retrain when new ratings volume reaches 10,000 since the last training run."</p>
        <p style="margin-top:0.5rem;">"Retrain when genre distribution shifts more than 15% from the training baseline."</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("**Best for:** Fast-moving data environments — rapidly growing user bases or seasonal content.")

section_break()

# ── Why not constantly ────────────────────────────────────────────────────────
st.markdown("### Why you can't just retrain constantly")
st.markdown(
    "Retraining isn't free. It consumes compute resources, takes time, and introduces "
    "risk — every new model version has to be evaluated before it can replace the current one."
)
st.markdown(
    "Over-frequent retraining can also destabilize your recommendations. If a user's top "
    "recommendation changes every day because the model is retrained daily on tiny increments "
    "of new data, the experience feels inconsistent."
)
st.markdown(
    "The goal is a cadence that keeps the model fresh without being disruptive. "
    "For most recommendation engines, **weekly or bi-weekly retraining** is a reasonable "
    "starting point."
)

section_break()

# ── Automated pipeline ────────────────────────────────────────────────────────
st.markdown("### What automated retraining looks like")
st.markdown(
    "A fully automated retraining pipeline runs these stages in sequence — "
    "notice how it depends on Modules 1, 2, and 3 being in place first:"
)

pipeline_steps = [
    ("🔔", "Trigger fires", "Time schedule, performance threshold, or data volume trigger"),
    ("📥", "Fresh dataset assembled", "Data pipeline (Module 3) delivers current training inputs"),
    ("🎓", "Model trains", "Same architecture and parameters as the current production model"),
    ("📊", "Evaluation runs", "New model evaluated against a held-out validation set"),
    ("⚖️", "Results compared", "New RMSE and coverage measured against production baseline"),
    ("✅", "If better → promote", "Registered in registry (Module 2), staged, then promoted to production"),
    ("⚠️", "If not better → hold", "Run logged (Module 1), production unchanged, alert sent for review"),
]

for i, (icon, title, desc) in enumerate(pipeline_steps):
    is_branch = i >= len(pipeline_steps) - 2
    border_color = "#166534" if title.startswith("If better") else "#991b1b" if title.startswith("If not") else "#1e3448"
    bg_color = "#0f2d1a" if title.startswith("If better") else "#2d0f0f" if title.startswith("If not") else "#162230"

    if is_branch and i == len(pipeline_steps) - 2:
        st.markdown("""
        <div style="display:flex; gap:0.5rem; margin-bottom:0.1rem;">
        """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="background:{bg_color}; border:1px solid {border_color}; border-radius:8px;
                padding:0.7rem 1rem; margin-bottom:0.4rem;
                display:flex; align-items:center; gap:0.75rem;">
        <span style="font-size:1.2rem; flex-shrink:0;">{icon}</span>
        <div>
            <div style="color:#e2e8f0; font-weight:600; font-size:0.88rem;">{title}</div>
            <div style="color:#64748b; font-size:0.8rem;">{desc}</div>
        </div>
    </div>
    {"<div style='text-align:center; color:#475569; margin:0.1rem 0;'>↓</div>" if i < len(pipeline_steps)-3 else ""}
    """, unsafe_allow_html=True)

section_break()

# ── Rollback ─────────────────────────────────────────────────────────────────
st.markdown("### The rollback plan")
st.markdown(
    "Every promotion needs a rollback path. Before you promote a new model, "
    "you should know the answer to: *what do we do if this model turns out to be worse "
    "in production than it was in evaluation?*"
)

st.markdown("""
<div class="module-tile" style="border-color:#106f8a;">
    <p>✓ The previous production model is archived — not deleted</p>
    <p>✓ Your deployment system can revert to it with a single action</p>
    <p>✓ Your team knows who makes that call and under what conditions</p>
    <p style="color:#64748b; font-size:0.82rem; margin-top:0.5rem; font-style:italic;">
    Rollback rarely happens. But the plan needs to exist before you need it — not after.</p>
</div>
""", unsafe_allow_html=True)

section_break()

# ── Interactive trigger selector ──────────────────────────────────────────────
st.markdown("### Design your retraining strategy")
st.markdown(
    "Use the controls below to think through what a retraining strategy would look like "
    "for your movie recommendation engine:"
)

trigger_type = st.selectbox(
    "Which trigger type fits your use case best?",
    ["Time-based", "Performance-based", "Data-based", "Combination of multiple triggers"],
)

if trigger_type == "Time-based":
    frequency = st.select_slider(
        "Retrain frequency:",
        options=["Daily", "Weekly", "Bi-weekly", "Monthly", "Quarterly"],
        value="Weekly",
    )
    st.markdown(f"""
    <div class="takeaway-box">
        <p>Your strategy: Retrain <strong>{frequency.lower()}</strong> on a fixed schedule.
        Make sure your data pipeline delivers fresh training data before each scheduled run.</p>
    </div>
    """, unsafe_allow_html=True)

elif trigger_type == "Performance-based":
    rmse_threshold = st.slider("RMSE threshold to trigger retrain:", 0.95, 1.20, 1.05, 0.01)
    st.markdown(f"""
    <div class="takeaway-box">
        <p>Your strategy: Trigger a retrain when RMSE on the weekly evaluation batch exceeds
        <strong>{rmse_threshold:.2f}</strong>. Requires monitoring (Module 5) to be in place first.</p>
    </div>
    """, unsafe_allow_html=True)

elif trigger_type == "Data-based":
    new_ratings_threshold = st.slider(
        "New ratings needed to trigger retrain:", 1000, 50000, 10000, 1000,
        format="%d ratings"
    )
    st.markdown(f"""
    <div class="takeaway-box">
        <p>Your strategy: Trigger a retrain once <strong>{new_ratings_threshold:,} new ratings</strong>
        have been collected since the last training run. Stable and predictable, tied directly to data growth.</p>
    </div>
    """, unsafe_allow_html=True)

else:
    st.markdown("""
    <div class="takeaway-box">
        <p>Your strategy: Use <strong>time-based triggers as a safety net</strong> (e.g., monthly at minimum)
        combined with <strong>performance-based triggers</strong> for faster response when RMSE degrades.
        Most mature ML teams use a combination.</p>
    </div>
    """, unsafe_allow_html=True)

section_break()

# ── Hands on ──────────────────────────────────────────────────────────────────
st.markdown("### Try it yourself")

step_label(1, "Choose your trigger")
st.markdown(
    "Using the selector above, commit to a retraining strategy for your movie rec engine. "
    "Write down a specific threshold — not 'when RMSE gets worse' but 'when RMSE exceeds X.'"
)

step_label(2, "Trace the dependencies")
st.markdown(
    "Walk through the automated retraining pipeline diagram above. "
    "Mark which steps require experiment tracking (Module 1) and which require "
    "the model registry (Module 2). Notice how removing either one breaks the pipeline."
)

step_label(3, "Define your rollback target")
st.markdown(
    "Which archived model would you roll back to if your next production promotion fails? "
    "How long would the rollback take? Who makes that decision?"
)

bts(
    "Automated retraining pipelines are built with orchestration tools like Airflow, "
    "Prefect, or cloud-native schedulers. The logic is the same regardless of the tool — "
    "trigger, assemble, train, evaluate, promote or hold."
)

takeaway(
    "Retraining isn't a one-time event — it's a recurring operation. The teams that do "
    "it well have defined triggers, automated pipelines, and rollback plans in place "
    "before they ever need them."
)

section_break()

nav_buttons(
    prev_page="pages/5_Data_Pipelines.py",
    next_page="pages/7_Monitoring.py",
    module_name="retraining",
)
