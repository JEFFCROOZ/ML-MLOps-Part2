import streamlit as st
from utils.styles import (
    inject_global_css, require_auth, section_break,
    takeaway, bts, step_label, mark_complete
)

st.set_page_config(
    page_title="The Living System — MLOps Part 2",
    page_icon="♻️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

inject_global_css()
require_auth()

# ── Header ───────────────────────────────────────────────────────────────────
st.markdown(
    "<p style='color:#106f8a; font-size:0.85rem; font-weight:600; "
    "text-transform:uppercase; letter-spacing:0.08em;'>Module 6 — Final Module</p>",
    unsafe_allow_html=True,
)
st.markdown("## The Living System")
st.markdown(
    "You've now covered every major piece of an MLOps system for a recommendation engine. "
    "This module is about seeing all of those pieces as one thing — a living system "
    "that sustains and improves itself over time."
)

section_break()

# ── The flywheel ──────────────────────────────────────────────────────────────
st.markdown("### The flywheel")
st.markdown(
    "The reason operational ML is worth building well is compounding. Each iteration of "
    "the loop doesn't just maintain the system — it improves it. "
    "Your team gets better at knowing which experiments are worth running. "
    "Your pipeline gets more reliable. Your monitoring thresholds get calibrated to your "
    "actual system behavior."
)

modules = [
    ("1", "Track your experiments", "Know what you tried and what worked", "#106f8a"),
    ("2", "Register the model", "Version it, stage it, promote it safely", "#106f8a"),
    ("3", "Keep data fresh", "Pipelines deliver current training inputs", "#106f8a"),
    ("4", "Retrain intelligently", "Trigger on time, performance, or data", "#106f8a"),
    ("5", "Monitor for drift", "Watch metrics, catch problems early", "#106f8a"),
    ("↺", "Close the loop", "Repeat with accumulated knowledge", "#0e5f77"),
]

st.markdown("""
<div style="background:#162230; border:1px solid #1e3448; border-radius:12px;
            padding:1.5rem 2rem; margin:1rem 0;">
""", unsafe_allow_html=True)

for num, title, desc, color in modules:
    is_loop = num == "↺"
    st.markdown(f"""
    <div style="display:flex; align-items:center; gap:1rem; margin-bottom:0.6rem;">
        <span style="background:{color}; color:#fff; border-radius:50%;
                     width:1.7rem; height:1.7rem; display:inline-flex;
                     align-items:center; justify-content:center;
                     font-size:0.8rem; font-weight:700; flex-shrink:0;
                     {'font-size:1rem;' if is_loop else ''}">
            {num}
        </span>
        <div>
            <div style="color:{'#94a3b8' if is_loop else '#e2e8f0'};
                        font-weight:{'400' if is_loop else '600'};
                        font-size:0.92rem;
                        font-style:{'italic' if is_loop else 'normal'};">
                {title}
            </div>
            <div style="color:#64748b; font-size:0.8rem;">{desc}</div>
        </div>
    </div>
    {"<div style='border-top:1px dashed #1e3448; margin:0.4rem 0 0.6rem 2.7rem;'></div>" if is_loop else ""}
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

section_break()

# ── What to build first ───────────────────────────────────────────────────────
st.markdown("### What to build first")
st.markdown(
    "You don't have to build all of this at once. "
    "Here's a practical sequence, ordered by the return you'll get on the effort:"
)

priorities = [
    ("🥇", "Experiment tracking — start now",
     "If you're not logging runs, you have no foundation for anything else. "
     "A spreadsheet is fine. The discipline matters more than the tool.",
     "#14532d", "#86efac"),
    ("🥈", "A model registry — even a simple one",
     "A folder structure with consistent naming and a README tracking which version "
     "is in production counts. Build the habit before building the automation.",
     "#1a2c45", "#93c5fd"),
    ("🥉", "A monitoring cadence",
     "Weekly review of RMSE and coverage. Even manual. Even in a spreadsheet. "
     "You'll learn more from watching your own system for a month than from any course.",
     "#1e293b", "#fcd34d"),
    ("4️⃣", "Data pipeline reliability",
     "Once you're monitoring, you'll quickly discover that your biggest threats "
     "come from the data, not the model. Invest here next.",
     "#1e293b", "#e2e8f0"),
    ("5️⃣", "Automated retraining",
     "Once your pipeline is reliable and your monitoring is in place, automation "
     "becomes worthwhile. Before that, it amplifies whatever problems already exist.",
     "#1e293b", "#e2e8f0"),
    ("6️⃣", "Alerting and runbooks",
     "The last piece — not because it's least important, but because it's most "
     "valuable once the other pieces are in place.",
     "#1e293b", "#e2e8f0"),
]

for icon, title, desc, bg, color in priorities:
    st.markdown(f"""
    <div style="background:{bg}; border:1px solid #1e3448; border-radius:8px;
                padding:0.85rem 1.1rem; margin-bottom:0.5rem;
                display:flex; align-items:flex-start; gap:0.9rem;">
        <span style="font-size:1.3rem; flex-shrink:0;">{icon}</span>
        <div>
            <div style="color:{color}; font-weight:600; font-size:0.9rem; margin-bottom:0.2rem;">{title}</div>
            <div style="color:#94a3b8; font-size:0.82rem;">{desc}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

section_break()

# ── The honest part ───────────────────────────────────────────────────────────
st.markdown("### The honest part")
st.markdown(
    "Not every organization needs all six of these pieces at full maturity. "
    "A small team with one model and stable data can run a healthy production system "
    "with a spreadsheet-level implementation of most of this."
)
st.markdown(
    "What they can't afford to do is skip the thinking entirely. "
    "The team that has thought through their retraining triggers, knows what their "
    "RMSE baseline is, and has a one-page runbook for pipeline failures is in a "
    "fundamentally different position than the team that hasn't."
)
st.markdown("**You've now done that thinking. That's what this course was for.**")

section_break()

# ── Connection back to Part 1 ─────────────────────────────────────────────────
st.markdown("### The complete picture")

col_p1, col_arrow, col_p2 = st.columns([5, 1, 5])
with col_p1:
    st.markdown("""
    <div class="module-tile" style="height:100%;">
        <div style="color:#94a3b8; font-size:0.75rem; text-transform:uppercase;
                    letter-spacing:0.06em; margin-bottom:0.5rem;">Part 1</div>
        <h4 style="color:#e2e8f0;">Building the engine</h4>
        <p style="font-size:0.83rem;">Define the goal · Understand the data · Explore and prepare ·
        Train models (content-based, collaborative, hybrid) · Evaluate · Deploy</p>
    </div>
    """, unsafe_allow_html=True)
with col_arrow:
    st.markdown(
        "<div style='display:flex; align-items:center; justify-content:center; "
        "height:100%; font-size:1.5rem; color:#106f8a; padding-top:1rem;'>→</div>",
        unsafe_allow_html=True,
    )
with col_p2:
    st.markdown("""
    <div class="module-tile" style="height:100%; border-color:#106f8a;">
        <div style="color:#106f8a; font-size:0.75rem; text-transform:uppercase;
                    letter-spacing:0.06em; margin-bottom:0.5rem;">Part 2</div>
        <h4 style="color:#e2e8f0;">Keeping it running</h4>
        <p style="font-size:0.83rem;">Track experiments · Register models · Maintain pipelines ·
        Retrain on triggers · Monitor for drift · Alert and respond · Loop again</p>
    </div>
    """, unsafe_allow_html=True)

section_break()

# ── Where to go from here ─────────────────────────────────────────────────────
st.markdown("### Where to go from here")

next_steps = [
    ("🔬", "Try MLflow locally",
     "MLflow is free to run and the tracking API is just a few lines of Python. "
     "Start logging your next experiment — even a simple one."),
    ("📊", "Build the monitoring spreadsheet first",
     "Track RMSE and coverage weekly for one month. You'll learn more from watching "
     "your own system than from any course on the topic."),
    ("🔁", "Apply these concepts to your own domain",
     "Replace movies with whatever your business actually recommends — products, articles, "
     "people, services. The loop is the same."),
    ("📖", "Go deep on data engineering",
     "Of everything covered here, data engineering is the most underestimated skill in ML. "
     "Pipeline reliability is where most production failures actually originate."),
]

cols = st.columns(2)
for i, (icon, title, desc) in enumerate(next_steps):
    with cols[i % 2]:
        st.markdown(f"""
        <div class="module-tile" style="margin-bottom:0.6rem;">
            <div style="font-size:1.4rem; margin-bottom:0.4rem;">{icon}</div>
            <h4 style="font-size:0.9rem;">{title}</h4>
            <p style="font-size:0.82rem;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

section_break()

takeaway(
    "A recommendation engine that nobody operates is a recommendation engine that slowly "
    "stops working. The difference between a proof of concept and a real system is "
    "everything you learned in Part 2."
)

section_break()

# ── Completion ────────────────────────────────────────────────────────────────
completed = st.session_state.get("completed_modules", [])
course_modules = [
    "experiment_tracking", "model_registry", "data_pipelines",
    "retraining", "monitoring", "living_system"
]
all_done = all(m in completed for m in course_modules)

if all_done:
    st.markdown("""
    <div style="text-align:center; padding:2rem; background:#0f2d1a;
                border:1px solid #166534; border-radius:12px; margin:1rem 0;">
        <div style="font-size:2.5rem; margin-bottom:0.75rem;">🎉</div>
        <div style="font-size:1.3rem; font-weight:700; color:#86efac; margin-bottom:0.5rem;">
            Part 2 Complete
        </div>
        <div style="color:#94a3b8; font-size:0.9rem;">
            You've gone from building a recommendation engine to understanding how to operate
            one reliably over time. That's the full loop.
        </div>
    </div>
    """, unsafe_allow_html=True)
else:
    remaining = [m for m in course_modules if m not in completed]
    st.markdown(
        f"<p style='color:#64748b; font-size:0.875rem; text-align:center;'>"
        f"{len(remaining)} module(s) still to complete — head back to the home screen.</p>",
        unsafe_allow_html=True,
    )

col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    if st.button("← Previous", use_container_width=True):
        st.switch_page("pages/7_Monitoring.py")
with col2:
    if st.button("✓ Complete Module 6", use_container_width=True, type="primary"):
        mark_complete("living_system")
        st.success("Module 6 marked complete! You've finished Part 2.")
        st.balloons()
with col3:
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("pages/1_Home.py")
