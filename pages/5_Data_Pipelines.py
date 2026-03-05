import streamlit as st
from utils.styles import (
    inject_global_css, require_auth, section_break,
    takeaway, bts, step_label, nav_buttons
)

st.set_page_config(
    page_title="Data Pipelines — MLOps Part 2",
    page_icon="🔁",
    layout="centered",
    initial_sidebar_state="collapsed",
)

inject_global_css()
require_auth()

# ── Header ───────────────────────────────────────────────────────────────────
st.markdown(
    "<p style='color:#106f8a; font-size:0.85rem; font-weight:600; "
    "text-transform:uppercase; letter-spacing:0.08em;'>Module 3</p>",
    unsafe_allow_html=True,
)
st.markdown("## Data Pipelines & Freshness")
st.markdown(
    "Your model is only as good as the data it was trained on. "
    "And that data has an expiration date."
)

section_break()

# ── The freshness problem ─────────────────────────────────────────────────────
st.markdown("### The freshness problem")
st.markdown(
    "The MovieLens dataset from Part 1 is a snapshot — ratings collected up to a specific "
    "point in time, frozen there. In a real production system, new ratings arrive every day. "
    "New users sign up. New films get released. The landscape is constantly shifting."
)
st.markdown("**Imagine your model was trained in January. It's now September.**")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="module-tile" style="text-align:center;">
        <div style="font-size:1.8rem; margin-bottom:0.5rem;">🎬</div>
        <h4>50+ new films</h4>
        <p>Released since January. Your model can't recommend any of them — it doesn't know they exist.</p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="module-tile" style="text-align:center;">
        <div style="font-size:1.8rem; margin-bottom:0.5rem;">⭐</div>
        <h4>200+ new ratings</h4>
        <p>Your most active users have evolved. The model is still using their January preferences.</p>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="module-tile" style="text-align:center;">
        <div style="font-size:1.8rem; margin-bottom:0.5rem;">📈</div>
        <h4>Shifting trends</h4>
        <p>A sequel launched. A director won an award. Older films have new relevance the model can't see.</p>
    </div>
    """, unsafe_allow_html=True)

section_break()

# ── What a pipeline does ──────────────────────────────────────────────────────
st.markdown("### What a data pipeline does")
st.markdown(
    "At its core, a data pipeline moves data through a sequence of transformations. "
    "In Part 1, you did all of this manually. A pipeline automates every step on a schedule."
)

pipeline_steps = [
    ("📥", "Raw source data", "New ratings, user events, movie metadata — collected as-is"),
    ("🗄️", "Ingestion layer", "Store the raw data exactly as it arrived — no transformations yet"),
    ("🔧", "Transformation", "Clean, join, normalize — the work you did manually in Part 1, now automated"),
    ("📐", "Feature store", "Ready-to-use inputs for model training — user-item matrix, genre vectors"),
    ("🎯", "Training dataset", "The final, versioned snapshot the model learns from"),
]

for i, (icon, title, desc) in enumerate(pipeline_steps):
    st.markdown(f"""
    <div style="display:flex; align-items:center; gap:0; margin-bottom:0;">
        <div style="background:#162230; border:1px solid #1e3448; border-radius:8px;
                    padding:0.7rem 1rem; flex:1; display:flex; align-items:center; gap:0.75rem;">
            <span style="font-size:1.2rem;">{icon}</span>
            <div>
                <div style="color:#e2e8f0; font-weight:600; font-size:0.9rem;">{title}</div>
                <div style="color:#64748b; font-size:0.8rem;">{desc}</div>
            </div>
        </div>
    </div>
    {"<div style='text-align:center; color:#475569; font-size:1rem; margin:0.1rem 0;'>↓</div>" if i < len(pipeline_steps)-1 else ""}
    """, unsafe_allow_html=True)

section_break()

# ── Batch vs streaming ────────────────────────────────────────────────────────
st.markdown("### Batch vs. streaming")
st.markdown(
    "There are two broad approaches to data pipelines. Which one you need depends on "
    "how fresh your data needs to be:"
)

col_b, col_s = st.columns(2)
with col_b:
    st.markdown("""
    <div class="module-tile">
        <h4>⏱️ Batch pipelines</h4>
        <p>Run on a schedule — hourly, daily, or weekly. Collect everything that happened since
        the last run and process it together.</p>
        <p style="color:#86efac; font-size:0.82rem; margin-top:0.5rem;">
        ✓ Right for most recommendation engines. You don't need real-time ratings to make
        good recommendations.</p>
    </div>
    """, unsafe_allow_html=True)
with col_s:
    st.markdown("""
    <div class="module-tile">
        <h4>⚡ Streaming pipelines</h4>
        <p>Process data as it arrives, in near real-time. Necessary when freshness is
        critical — for example, if a user rates a film and you want that reflected
        in their next recommendation within minutes.</p>
        <p style="color:#fcd34d; font-size:0.82rem; margin-top:0.5rem;">
        ✓ Right for news feeds, live event recommendations, trading systems.</p>
    </div>
    """, unsafe_allow_html=True)

section_break()

# ── Freshness metrics ─────────────────────────────────────────────────────────
st.markdown("### Freshness metrics — what to measure")
st.markdown(
    "Freshness isn't binary. It's a spectrum, and you should be able to measure it:"
)

st.markdown("""
<table>
    <thead>
        <tr>
            <th>Metric</th>
            <th>What it measures</th>
            <th>Healthy threshold</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Data lag</td>
            <td>Time since last successful pipeline run</td>
            <td>< 25 hours for daily batch</td>
        </tr>
        <tr>
            <td>New item coverage</td>
            <td>% of recently released films in training data</td>
            <td>> 90% within 7 days of release</td>
        </tr>
        <tr>
            <td>Active user recency</td>
            <td>% of users whose latest rating is within 90 days</td>
            <td>> 70%</td>
        </tr>
        <tr>
            <td>Rating volume trend</td>
            <td>New ratings per week — is volume stable?</td>
            <td>Baseline ± 15%</td>
        </tr>
    </tbody>
</table>
""", unsafe_allow_html=True)

section_break()

# ── What can go wrong ─────────────────────────────────────────────────────────
st.markdown("### What can go wrong")
st.markdown(
    "Data pipelines are frequently the most fragile part of an ML system. "
    "These aren't edge cases — they're regular occurrences in production:"
)

failures = [
    ("💥", "Source data changes format",
     "The upstream system renames a field or changes how genres are encoded. "
     "Your transformation step breaks — sometimes silently."),
    ("👻", "Pipeline runs but delivers empty data",
     "A bug in your ingestion step means the table is updated but contains no new rows. "
     "Your training data looks current but isn't."),
    ("📐", "Schema drift",
     "The shape of your data changes gradually over time in ways that aren't caught "
     "until they cause a downstream failure."),
    ("⏳", "Late data",
     "Some events are logged with delays — mobile apps sync when connected. "
     "Your pipeline may cut off data that arrives hours after the scheduled run."),
]

for icon, title, desc in failures:
    st.markdown(f"""
    <div style="background:#1a1a2e; border-left:3px solid #991b1b; border-radius:0 8px 8px 0;
                padding:0.75rem 1rem; margin-bottom:0.6rem;">
        <div style="color:#fca5a5; font-weight:600; margin-bottom:0.2rem;">{icon} {title}</div>
        <div style="color:#94a3b8; font-size:0.875rem;">{desc}</div>
    </div>
    """, unsafe_allow_html=True)

section_break()

# ── Hands on ──────────────────────────────────────────────────────────────────
st.markdown("### Try it yourself")

step_label(1, "Measure the freshness gap")
st.markdown(
    "The movie rec engine from Part 1 was trained on a static CSV. "
    "Using the freshness metrics table above — if today is 6 months after your model was trained, "
    "which metrics are most likely to be out of range? Why?"
)

step_label(2, "Trace the pipeline")
st.markdown(
    "Walk through the pipeline diagram above. Identify which step you handled manually "
    "in Part 1. What would automating that step require — a script, a scheduler, a database?"
)

step_label(3, "Pick the failure mode most likely to affect you")
st.markdown(
    "From the four failure modes listed, which one would be hardest to catch before "
    "it affects your model? How would you detect it?"
)

bts(
    "Tools like Apache Airflow, Prefect, and dbt are commonly used to build and schedule "
    "data pipelines. Cloud providers offer managed equivalents. The step-by-step logic "
    "is the same regardless of the tool running it."
)

takeaway(
    "A model trained on stale data makes stale recommendations. Data pipelines are what "
    "keep your system connected to reality — and pipeline reliability is just as important "
    "as model accuracy."
)

section_break()

nav_buttons(
    prev_page="pages/4_Model_Registry.py",
    next_page="pages/6_Retraining.py",
    module_name="data_pipelines",
)
