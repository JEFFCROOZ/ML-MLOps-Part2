import streamlit as st
from utils.styles import inject_global_css, require_auth, badge, part1_callout

st.set_page_config(
    page_title="Home — MLOps Part 2",
    page_icon="⚙️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

inject_global_css()
require_auth()

username = st.session_state.get("username", "learner")
completed = st.session_state.get("completed_modules", [])

MODULES = [
    {
        "key": "mlops_mindset",
        "title": "The MLOps Mindset",
        "desc": "How your thinking shifts from building to maintaining",
        "page": "pages/2_MLOps_Mindset.py",
        "numbered": False,
    },
    {
        "key": "experiment_tracking",
        "title": "Module 1 — Experiment Tracking",
        "desc": "Keeping a systematic record of what you tried and what worked",
        "page": "pages/3_Experiment_Tracking.py",
        "numbered": True,
    },
    {
        "key": "model_registry",
        "title": "Module 2 — The Model Registry",
        "desc": "Versioning, staging, and promoting models safely",
        "page": "pages/4_Model_Registry.py",
        "numbered": True,
    },
    {
        "key": "data_pipelines",
        "title": "Module 3 — Data Pipelines & Freshness",
        "desc": "Making sure your model's inputs don't go stale",
        "page": "pages/5_Data_Pipelines.py",
        "numbered": True,
    },
    {
        "key": "retraining",
        "title": "Module 4 — Retraining: When and How",
        "desc": "Knowing when to retrain — and automating it when you can",
        "page": "pages/6_Retraining.py",
        "numbered": True,
    },
    {
        "key": "monitoring",
        "title": "Module 5 — Monitoring, Drift & Response",
        "desc": "Catching model degradation and acting on it before users notice",
        "page": "pages/7_Monitoring.py",
        "numbered": True,
    },
    {
        "key": "living_system",
        "title": "Module 6 — The Living System",
        "desc": "Putting it all together as a flywheel, not a one-time project",
        "page": "pages/8_Living_System.py",
        "numbered": True,
    },
]

numbered_modules = [m for m in MODULES if m["numbered"]]
completed_count = sum(1 for m in numbered_modules if m["key"] in completed)

# ── Part 1 callout ──────────────────────────────────────────────────────────
part1_callout("https://ml-model-flow-app-h6snwfqezqbbuhhhkcvjdg.streamlit.app")

# ── Header ──────────────────────────────────────────────────────────────────
st.markdown(f"""
<div style="margin-bottom: 0.25rem;">
    <span style="color: #64748b; font-size: 0.875rem;">Welcome back, {username}</span>
</div>
""", unsafe_allow_html=True)

st.markdown("## You built it. Now let's keep it running.")
st.markdown(
    "If you made it through Part 1, you know how to build a recommendation engine. "
    "Part 2 is everything that happens after — the operational thinking, the systems, "
    "and the instincts that keep your model accurate and reliable over time."
)

# ── Progress bar ─────────────────────────────────────────────────────────────
st.markdown("<div style='margin: 1.5rem 0 0.5rem 0;'>", unsafe_allow_html=True)
col_p, col_c = st.columns([4, 1])
with col_p:
    progress_val = completed_count / len(numbered_modules) if numbered_modules else 0
    st.progress(progress_val)
with col_c:
    st.markdown(
        f"<div style='text-align:right; color:#64748b; font-size:0.85rem; padding-top:0.4rem;'>"
        f"{completed_count} / {len(numbered_modules)} modules</div>",
        unsafe_allow_html=True,
    )
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# ── Module tiles ─────────────────────────────────────────────────────────────
for mod in MODULES:
    status = "complete" if mod["key"] in completed else "pending"
    badge_html = badge(status)

    col_info, col_btn = st.columns([4, 1])
    with col_info:
        st.markdown(f"""
        <div class="module-tile">
            <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:0.4rem;">
                <h4 style="margin:0;">{mod["title"]}</h4>
                {badge_html}
            </div>
            <p>{mod["desc"]}</p>
        </div>
        """, unsafe_allow_html=True)
    with col_btn:
        st.markdown("<div style='margin-top:0.85rem;'>", unsafe_allow_html=True)
        if st.button("Open →", key=f"open_{mod['key']}", use_container_width=True):
            st.switch_page(mod["page"])
        st.markdown("</div>", unsafe_allow_html=True)

# ── Sign out ──────────────────────────────────────────────────────────────────
st.markdown("---")
col_so1, col_so2, col_so3 = st.columns([3, 1, 3])
with col_so2:
    if st.button("Sign Out", use_container_width=True):
        for key in ["authenticated", "username", "completed_modules"]:
            st.session_state.pop(key, None)
        st.switch_page("app.py")
