import streamlit as st
from utils.styles import inject_global_css, require_auth, section_break, takeaway

st.set_page_config(
    page_title="The MLOps Mindset — Part 2",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed",
)

inject_global_css()
require_auth()

# ── Header ───────────────────────────────────────────────────────────────────
st.markdown(
    "<p style='color:#106f8a; font-size:0.85rem; font-weight:600; "
    "text-transform:uppercase; letter-spacing:0.08em;'>Before We Begin</p>",
    unsafe_allow_html=True,
)
st.markdown("## The MLOps Mindset")
st.markdown(
    "Before we get into any specific technique, we need to talk about a shift in thinking. "
    "It's small. But it changes everything about how you approach your work."
)

section_break()

# ── Section 1 ────────────────────────────────────────────────────────────────
st.markdown("### From builder to operator")
st.markdown(
    "When you were building your recommendation engine in Part 1, you were thinking like a "
    "**builder**. You had a goal — train a model that makes good recommendations — and a "
    "finish line: a working result."
)
st.markdown(
    "Operating an ML system requires a fundamentally different mindset. "
    "**There is no finish line.**"
)
st.markdown(
    "Instead, you're running a *system* — one that needs to stay accurate as the world "
    "changes, handle new data reliably, and recover gracefully when something breaks. "
    "The model you trained is no longer just a project you finished. "
    "It's infrastructure you're responsible for."
)

section_break()

# ── Section 2 ────────────────────────────────────────────────────────────────
st.markdown("### Why this matters more than it sounds")
st.markdown(
    "Think about the model you built in Part 1. It was trained on a snapshot of user "
    "preferences at a specific point in time. The moment training finished, that model "
    "started aging."
)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="module-tile" style="text-align:center;">
        <div style="font-size:1.8rem; margin-bottom:0.5rem;">🎬</div>
        <h4>New releases</h4>
        <p>New movies arrive every week. Your model doesn't know they exist.</p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="module-tile" style="text-align:center;">
        <div style="font-size:1.8rem; margin-bottom:0.5rem;">👤</div>
        <h4>Evolving tastes</h4>
        <p>Users' preferences shift. The model is still using their old behavior.</p>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="module-tile" style="text-align:center;">
        <div style="font-size:1.8rem; margin-bottom:0.5rem;">📊</div>
        <h4>Rating patterns</h4>
        <p>What people rate — and how — changes with culture and trends.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown(
    "Without an operational mindset, you'd only notice these problems when something "
    "feels wrong. With it, you've already anticipated them and built systems to catch "
    "them early."
)

section_break()

# ── Section 3: comparison table ──────────────────────────────────────────────
st.markdown("### The core shift")

st.markdown("""
<table>
    <thead>
        <tr><th>Project Thinking</th><th>Systems Thinking</th></tr>
    </thead>
    <tbody>
        <tr><td>Has a start and end date</td><td>Runs continuously</td></tr>
        <tr><td>"Done" when the model trains</td><td>"Stable" is the goal, not "done"</td></tr>
        <tr><td>Failure is an edge case</td><td>Failure is an expected event to plan for</td></tr>
        <tr><td>Accuracy measured once at evaluation</td><td>Accuracy monitored continuously</td></tr>
        <tr><td>Data is static</td><td>Data is always changing</td></tr>
    </tbody>
</table>
""", unsafe_allow_html=True)

st.markdown(
    "This isn't a criticism of how you approached Part 1. That project mindset was "
    "exactly right for learning. But the moment a model is serving real users, "
    "the project is over and the operation begins."
)

section_break()

# ── Section 4: the loop ───────────────────────────────────────────────────────
st.markdown("### The MLOps loop")
st.markdown(
    "MLOps is often described as a loop, not a line. Each module in this course covers "
    "one stage of that loop — and by the end, you'll see how they connect into a system "
    "that sustains itself over time."
)

st.markdown("""
<div style="background-color:#162230; border:1px solid #1e3448; border-radius:10px; padding:1.5rem 2rem; margin:1rem 0;">
    <div style="display:flex; flex-direction:column; gap:0.6rem;">
        <div style="display:flex; align-items:center; gap:1rem;">
            <span style="background:#106f8a; color:#fff; border-radius:50%; width:1.5rem; height:1.5rem; display:inline-flex; align-items:center; justify-content:center; font-size:0.75rem; font-weight:700; flex-shrink:0;">1</span>
            <span style="color:#e2e8f0;">Track your experiments — know what you tried and what worked</span>
        </div>
        <div style="display:flex; align-items:center; gap:1rem;">
            <span style="background:#106f8a; color:#fff; border-radius:50%; width:1.5rem; height:1.5rem; display:inline-flex; align-items:center; justify-content:center; font-size:0.75rem; font-weight:700; flex-shrink:0;">2</span>
            <span style="color:#e2e8f0;">Register and version your models — promote them safely</span>
        </div>
        <div style="display:flex; align-items:center; gap:1rem;">
            <span style="background:#106f8a; color:#fff; border-radius:50%; width:1.5rem; height:1.5rem; display:inline-flex; align-items:center; justify-content:center; font-size:0.75rem; font-weight:700; flex-shrink:0;">3</span>
            <span style="color:#e2e8f0;">Keep your data fresh — pipelines deliver current inputs</span>
        </div>
        <div style="display:flex; align-items:center; gap:1rem;">
            <span style="background:#106f8a; color:#fff; border-radius:50%; width:1.5rem; height:1.5rem; display:inline-flex; align-items:center; justify-content:center; font-size:0.75rem; font-weight:700; flex-shrink:0;">4</span>
            <span style="color:#e2e8f0;">Retrain intelligently — on time, performance, or data triggers</span>
        </div>
        <div style="display:flex; align-items:center; gap:1rem;">
            <span style="background:#106f8a; color:#fff; border-radius:50%; width:1.5rem; height:1.5rem; display:inline-flex; align-items:center; justify-content:center; font-size:0.75rem; font-weight:700; flex-shrink:0;">5</span>
            <span style="color:#e2e8f0;">Monitor for drift — watch metrics, catch problems early</span>
        </div>
        <div style="display:flex; align-items:center; gap:1rem;">
            <span style="background:#0e5f77; color:#fff; border-radius:50%; width:1.5rem; height:1.5rem; display:inline-flex; align-items:center; justify-content:center; font-size:0.75rem; font-weight:700; flex-shrink:0;">↺</span>
            <span style="color:#94a3b8; font-style:italic;">Close the loop — repeat with accumulated knowledge</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

section_break()

# ── Section 5: scale note ─────────────────────────────────────────────────────
st.markdown("### A word on scale")
st.markdown(
    "You don't need a large team or enterprise infrastructure to operate an ML system well. "
    "A solo developer with one model can implement a lightweight version of this loop that's "
    "still far better than nothing."
)
st.markdown(
    "The concepts are the same at every scale. The implementation differs. "
    "This course focuses on the concepts — so that when you do sit down to build, "
    "you know exactly what you're building toward."
)

takeaway(
    "Building the model was the beginning. Operating it reliably over time — "
    "with fresh data, monitored performance, and a plan for when things go wrong — "
    "is the actual job."
)

section_break()

# ── Navigation ────────────────────────────────────────────────────────────────
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("← Back to Home", use_container_width=True):
        st.switch_page("pages/1_Home.py")
with col2:
    if st.button("Module 1: Experiment Tracking →", use_container_width=True, type="primary"):
        st.switch_page("pages/3_Experiment_Tracking.py")
