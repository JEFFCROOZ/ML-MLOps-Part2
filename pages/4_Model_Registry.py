import streamlit as st
import pandas as pd
from utils.styles import (
    inject_global_css, require_auth, section_break,
    takeaway, bts, step_label, nav_buttons
)
from utils.data_loader import REGISTRY_ENTRIES

st.set_page_config(
    page_title="Model Registry — MLOps Part 2",
    page_icon="📋",
    layout="centered",
    initial_sidebar_state="collapsed",
)

inject_global_css()
require_auth()

# ── Header ───────────────────────────────────────────────────────────────────
st.markdown(
    "<p style='color:#106f8a; font-size:0.85rem; font-weight:600; "
    "text-transform:uppercase; letter-spacing:0.08em;'>Module 2</p>",
    unsafe_allow_html=True,
)
st.markdown("## The Model Registry")
st.markdown(
    "Once you've been tracking experiments for a while, you have a library of trained models. "
    "Some are experiments. Some are candidates for production. A few are actually running "
    "in production right now."
)
st.markdown("**How do you keep track of which is which?**")

section_break()

# ── What is it ────────────────────────────────────────────────────────────────
st.markdown("### What a model registry is")
st.markdown(
    "A model registry is a central catalog that tracks not just the models you've trained, "
    "but their *status* — where each one is in its lifecycle, who approved it, "
    "and what it replaced."
)
st.markdown(
    "Think of it as version control for your models, the same way Git is version control "
    "for your code."
)

st.markdown("""
<div class="module-tile" style="margin:1.5rem 0;">
    <div style="display:flex; gap:2rem; flex-wrap:wrap; justify-content:space-between;">
        <div style="text-align:center; flex:1; min-width:120px;">
            <div style="font-size:0.75rem; color:#64748b; text-transform:uppercase; letter-spacing:0.05em; margin-bottom:0.3rem;">Without Registry</div>
            <div style="color:#fca5a5; font-size:0.9rem; line-height:1.6;">
                "I think the model in <code>/final_v3_UPDATED</code> is the one we're using.<br>
                Or maybe it was <code>/final_v3</code>?"
            </div>
        </div>
        <div style="color:#475569; display:flex; align-items:center; font-size:1.2rem;">→</div>
        <div style="text-align:center; flex:1; min-width:120px;">
            <div style="font-size:0.75rem; color:#64748b; text-transform:uppercase; letter-spacing:0.05em; margin-bottom:0.3rem;">With Registry</div>
            <div style="color:#86efac; font-size:0.9rem; line-height:1.6;">
                "v2.3 is in production. Promoted March 18th.<br>
                v2.4 is in staging pending sign-off."
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

section_break()

# ── Lifecycle stages ──────────────────────────────────────────────────────────
st.markdown("### The four lifecycle stages")
st.markdown(
    "Every model version lives in exactly one stage at any given time:"
)

stages = [
    ("🔬", "Development", "#1e3448", "#93c5fd",
     "The model has been trained and logged. It's a candidate — not yet vetted for production. "
     "Most models never leave this stage."),
    ("🧪", "Staging", "#1a2c45", "#fcd34d",
     "Selected as a promotion candidate. Being tested more rigorously: checked for regressions, "
     "validated on a held-out dataset, reviewed for unexpected behavior. This is your quality gate."),
    ("🚀", "Production", "#14532d", "#86efac",
     "The model is live, serving real users. There should only ever be one model version in "
     "production for a given use case at a time."),
    ("📦", "Archived", "#1e293b", "#475569",
     "Retired. No longer in use, but preserved in case you need to audit decisions it made "
     "or roll back to a previous version in an emergency."),
]

for icon, title, bg, color, desc in stages:
    st.markdown(f"""
    <div style="background:{bg}; border:1px solid #1e3448; border-radius:8px;
                padding:0.9rem 1.1rem; margin-bottom:0.6rem; display:flex; gap:1rem; align-items:flex-start;">
        <span style="font-size:1.4rem; flex-shrink:0;">{icon}</span>
        <div>
            <div style="color:{color}; font-weight:600; font-size:0.95rem; margin-bottom:0.2rem;">{title}</div>
            <div style="color:#94a3b8; font-size:0.875rem;">{desc}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

section_break()

# ── Interactive registry ──────────────────────────────────────────────────────
st.markdown("### Live registry — explore it")
st.markdown(
    "Below is the model registry for our movie recommendation engine. "
    "Click any version to inspect its full entry."
)

stage_colors = {
    "Production": "#86efac",
    "Staging": "#fcd34d",
    "Archived": "#475569",
    "Development": "#93c5fd",
}

selected_version = st.radio(
    "Select a model version:",
    options=[e["version"] for e in REGISTRY_ENTRIES],
    horizontal=True,
)

entry = next(e for e in REGISTRY_ENTRIES if e["version"] == selected_version)
color = stage_colors.get(entry["stage"], "#e2e8f0")

col_left, col_right = st.columns(2)
with col_left:
    st.markdown(f"""
    <div class="module-tile">
        <table style="margin:0;">
            <tr><td style="color:#64748b; width:45%;">Version</td>
                <td><strong style="color:#e2e8f0;">{entry['version']}</strong></td></tr>
            <tr><td style="color:#64748b;">Stage</td>
                <td><strong style="color:{color};">{entry['stage']}</strong></td></tr>
            <tr><td style="color:#64748b;">Registered</td><td>{entry['registered']}</td></tr>
            <tr><td style="color:#64748b;">Promoted</td><td>{entry['promoted']}</td></tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

with col_right:
    rmse_color = "#86efac" if entry["rmse"] < 0.92 else "#fcd34d" if entry["rmse"] < 0.97 else "#fca5a5"
    st.markdown(f"""
    <div class="module-tile">
        <table style="margin:0;">
            <tr><td style="color:#64748b; width:45%;">RMSE</td>
                <td><strong style="color:{rmse_color};">{entry['rmse']}</strong></td></tr>
            <tr><td style="color:#64748b;">Coverage</td><td>{entry['coverage']}%</td></tr>
            <tr><td colspan="2" style="color:#94a3b8; font-size:0.82rem; padding-top:0.5rem; font-style:italic;">
                {entry['notes']}</td></tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

section_break()

# ── Promotion decision ─────────────────────────────────────────────────────────
st.markdown("### The promotion decision")
st.markdown(
    "Moving a model from staging to production means replacing what users are currently "
    "experiencing. It should never be casual. Promotion should require at least:"
)

checklist = [
    "RMSE on a fresh validation set is better than (or comparable to) the current production model",
    "Coverage hasn't dropped significantly from the production baseline",
    "A human or automated check has reviewed the evaluation results",
    "A rollback plan exists — if the new model underperforms, which archived version do you revert to?",
]
for item in checklist:
    st.markdown(f"- {item}")

section_break()

# ── Versioning ────────────────────────────────────────────────────────────────
st.markdown("### Versioning conventions")
st.markdown(
    "Version numbers aren't arbitrary. A common convention — "
    "consistency matters more than the specific system:"
)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="module-tile" style="text-align:center;">
        <h4>v2 → v3</h4>
        <p style="color:#94a3b8; font-size:0.82rem;">Major version<br>New architecture or feature set</p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="module-tile" style="text-align:center; border-color:#106f8a;">
        <h4>v2.2 → v2.3</h4>
        <p style="color:#94a3b8; font-size:0.82rem;">Minor version<br>Retrained on newer data or tuned params</p>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="module-tile" style="text-align:center;">
        <h4>v2.3.0 → v2.3.1</h4>
        <p style="color:#94a3b8; font-size:0.82rem;">Patch<br>Bug fix or metadata correction</p>
    </div>
    """, unsafe_allow_html=True)

section_break()

# ── Hands on ──────────────────────────────────────────────────────────────────
st.markdown("### Try it yourself")

step_label(1, "Inspect the registry above")
st.markdown(
    "Look at v2.3 (Production) and v2.4 (Staging). v2.4 has a slightly better RMSE "
    "but lower coverage. Should it be promoted? What questions do you ask first?"
)

step_label(2, "Identify the rollback target")
st.markdown(
    "If v2.4 gets promoted and underperforms in production, which version do you roll back to? "
    "How would you know it's safe to use again?"
)

step_label(3, "Write your own registry entry")
st.markdown(
    "Using the experiment log entry you drafted in Module 1, write the corresponding "
    "registry entry. Assign it a version number. What stage is it in right now?"
)

bts(
    "Tools like MLflow Model Registry, Hugging Face Hub, and cloud provider registries "
    "(AWS SageMaker, Azure ML, GCP Vertex AI) all implement this same concept with "
    "different interfaces. The lifecycle stages and promotion logic are universal."
)

takeaway(
    "A model registry turns a collection of trained files into a managed system. "
    "It gives every version a clear identity, a lifecycle stage, and a documented "
    "path from experiment to production."
)

section_break()

nav_buttons(
    prev_page="pages/3_Experiment_Tracking.py",
    next_page="pages/5_Data_Pipelines.py",
    module_name="model_registry",
)
