import streamlit as st
import pandas as pd
from utils.styles import (
    inject_global_css, require_auth, section_break,
    takeaway, bts, step_label, nav_buttons
)
from utils.data_loader import EXPERIMENT_LOG

st.set_page_config(
    page_title="Experiment Tracking — MLOps Part 2",
    page_icon="🧪",
    layout="centered",
    initial_sidebar_state="collapsed",
)

inject_global_css()
require_auth()

# ── Header ───────────────────────────────────────────────────────────────────
st.markdown(
    "<p style='color:#106f8a; font-size:0.85rem; font-weight:600; "
    "text-transform:uppercase; letter-spacing:0.08em;'>Module 1</p>",
    unsafe_allow_html=True,
)
st.markdown("## Experiment Tracking")
st.markdown(
    "Before your model ever goes anywhere near production, you've probably run dozens "
    "of experiments. You tried different parameters, compared approaches, tweaked the "
    "setup and checked whether results improved."
)
st.markdown(
    "Here's the question: **do you remember exactly what you tried?**"
)

section_break()

# ── What is it ────────────────────────────────────────────────────────────────
st.markdown("### What experiment tracking is")
st.markdown(
    "Experiment tracking is the practice of recording every meaningful training run — "
    "what data you used, what parameters you set, and what results you got — so that "
    "you always know where your best model came from and how to reproduce it."
)
st.markdown(
    "Without it, you're building on memory. With it, you're building on evidence."
)

section_break()

# ── Why it matters ────────────────────────────────────────────────────────────
st.markdown("### Why it matters for your rec engine")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="module-tile" style="text-align:center;">
        <div style="font-size:1.6rem; margin-bottom:0.4rem;">🔬</div>
        <h4>Run A</h4>
        <p>50 latent factors<br><strong style="color:#fca5a5;">RMSE 0.940</strong></p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="module-tile" style="text-align:center; border-color:#106f8a;">
        <div style="font-size:1.6rem; margin-bottom:0.4rem;">✅</div>
        <h4>Run B</h4>
        <p>100 latent factors<br><strong style="color:#86efac;">RMSE 0.915</strong></p>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="module-tile" style="text-align:center;">
        <div style="font-size:1.6rem; margin-bottom:0.4rem;">📉</div>
        <h4>Run C</h4>
        <p>100 factors, 6-month window<br><strong style="color:#fca5a5;">RMSE 0.970</strong></p>
    </div>
    """, unsafe_allow_html=True)

st.markdown(
    "Run B is clearly best. But a month later, when you're retraining on fresh data, "
    "do you remember it used 100 latent factors? Do you remember the shorter training "
    "window hurt performance? Experiment tracking means you don't have to remember. "
    "It's all logged."
)

section_break()

# ── What an experiment log contains ──────────────────────────────────────────
st.markdown("### What an experiment log contains")
st.markdown(
    "A well-structured experiment log records four categories of information "
    "for every training run:"
)

c1, c2 = st.columns(2)
with c1:
    st.markdown("""
    <div class="module-tile">
        <h4>⚙️ Parameters</h4>
        <p>What you configured <em>before</em> training — factors, learning rate, epochs, data date range</p>
    </div>
    <div class="module-tile">
        <h4>📦 Artifacts</h4>
        <p>What got saved — the model file, training dataset reference, evaluation plots</p>
    </div>
    """, unsafe_allow_html=True)
with c2:
    st.markdown("""
    <div class="module-tile">
        <h4>📊 Metrics</h4>
        <p>What you measured <em>after</em> training — RMSE, MAE, coverage %, training duration</p>
    </div>
    <div class="module-tile">
        <h4>🗒️ Context</h4>
        <p>Everything else — who ran it, when, why, and any notes about what changed</p>
    </div>
    """, unsafe_allow_html=True)

section_break()

# ── Interactive log viewer ────────────────────────────────────────────────────
st.markdown("### A real experiment log — explore it")
st.markdown(
    "Below are four runs from the movie recommendation engine. This is what a tracked "
    "experiment history actually looks like. Select a run to see its full details."
)

df = pd.DataFrame(EXPERIMENT_LOG)

run_labels = [f"{r['run_id']}  (RMSE {r['rmse']})" for r in EXPERIMENT_LOG]
selected_label = st.selectbox("Select a run to inspect:", run_labels)
selected_idx = run_labels.index(selected_label)
run = EXPERIMENT_LOG[selected_idx]

col_a, col_b = st.columns(2)
with col_a:
    st.markdown("**Parameters**")
    st.markdown(f"""
    <div class="module-tile">
        <table style="margin:0;">
            <tr><td style="color:#64748b; width:50%;">Model type</td><td>{run['model_type']}</td></tr>
            <tr><td style="color:#64748b;">Latent factors</td><td>{run['n_factors']}</td></tr>
            <tr><td style="color:#64748b;">Learning rate</td><td>{run['lr_all']}</td></tr>
            <tr><td style="color:#64748b;">Regularization</td><td>{run['reg_all']}</td></tr>
            <tr><td style="color:#64748b;">Epochs</td><td>{run['n_epochs']}</td></tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

with col_b:
    st.markdown("**Metrics**")
    rmse_color = "#86efac" if run["rmse"] < 0.92 else "#fcd34d" if run["rmse"] < 0.97 else "#fca5a5"
    st.markdown(f"""
    <div class="module-tile">
        <table style="margin:0;">
            <tr><td style="color:#64748b; width:50%;">RMSE</td>
                <td><strong style="color:{rmse_color};">{run['rmse']}</strong></td></tr>
            <tr><td style="color:#64748b;">MAE</td><td>{run['mae']}</td></tr>
            <tr><td style="color:#64748b;">Coverage</td><td>{run['coverage_pct']}%</td></tr>
            <tr><td style="color:#64748b;">Train time</td><td>{run['train_time_s']}s</td></tr>
            <tr><td style="color:#64748b;">Timestamp</td><td>{run['timestamp']}</td></tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

st.markdown(f"""
<div class="bts-box">
    <p>🗒️ <strong>Notes:</strong> {run['notes']}</p>
</div>
""", unsafe_allow_html=True)

section_break()

# ── Hands on ──────────────────────────────────────────────────────────────────
st.markdown("### Try it yourself")

step_label(1, "Spot the best run")
st.markdown(
    "Look at the four runs above. Which one produced the best RMSE? "
    "Which configuration change made the biggest difference — and which one hurt performance?"
)

step_label(2, "Think about reproducibility")
st.markdown(
    "Pick the best run. If you had to retrain that exact model tomorrow — same parameters, "
    "same dataset window — could you do it from memory alone? The log makes that automatic."
)

step_label(3, "Draft your own entry")
st.markdown(
    "Think back to the experiments you ran in Part 1. Using the structure above, "
    "sketch what your own experiment log entry would look like for your best-performing model."
)

with st.expander("See a blank template to fill in"):
    st.code("""Run ID:          run_YYYYMMDD_001
Timestamp:       YYYY-MM-DD HH:MM
Model Type:      SVD (Collaborative Filtering)
Dataset:         MovieLens 100K — [date range]

Parameters:
  n_factors:     [value]
  lr_all:        [value]
  reg_all:       [value]
  n_epochs:      [value]

Metrics:
  RMSE:          [value]
  MAE:           [value]
  Coverage:      [value]%
  Training time: [value]s

Notes:
  [What changed from the previous run? What did you learn?]""", language="text")

bts(
    "In production, tools like MLflow Tracking, Weights & Biases, and Neptune "
    "auto-capture parameters and metrics with just a few lines of code — and give you "
    "a UI to compare runs side by side. The discipline matters more than the tool."
)

takeaway(
    "Experiment tracking is the foundation of everything that comes next. "
    "You can't version a model you can't reproduce. You can't compare models you didn't log. "
    "Start tracking from run one."
)

section_break()

nav_buttons(
    prev_page="pages/2_MLOps_Mindset.py",
    next_page="pages/4_Model_Registry.py",
    module_name="experiment_tracking",
)
