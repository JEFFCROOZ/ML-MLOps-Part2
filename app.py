import streamlit as st
from utils.styles import inject_global_css

st.set_page_config(
    page_title="MLOps for Rec Engines — Part 2",
    page_icon="⚙️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

inject_global_css()

# If already authenticated, go straight to home
if st.session_state.get("authenticated"):
    st.switch_page("pages/1_Home.py")

# ── Hero ────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align: center; padding: 3.5rem 0 2rem 0;">
    <div style="font-size: 3rem; margin-bottom: 0.75rem;">⚙️</div>
    <div style="font-size: 2.2rem; font-weight: 700; color: #e2e8f0; margin-bottom: 0.4rem;">
        MLOps for Rec Engines
    </div>
    <div style="font-size: 1.05rem; color: #94a3b8; margin-bottom: 0.4rem;">
        Part 2 of the ML Recommendation Engine Series
    </div>
    <div style="display: flex; justify-content: center; gap: 1.5rem; margin-top: 1rem; flex-wrap: wrap;">
        <span style="color: #475569; font-size: 0.85rem;">⚙️ 6 modules</span>
        <span style="color: #475569; font-size: 0.85rem;">💡 Concept-first</span>
        <span style="color: #475569; font-size: 0.85rem;">🎬 Movie rec engine example</span>
        <span style="color: #475569; font-size: 0.85rem;">☁️ No cloud accounts needed</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Login form ───────────────────────────────────────────────────────────────
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown('<div class="login-card">', unsafe_allow_html=True)
    st.markdown("#### Sign in to continue")
    st.markdown(
        "<p style='color:#64748b; font-size:0.85rem; margin-top:-0.5rem;'>"
        "Same credentials as Part 1</p>",
        unsafe_allow_html=True,
    )

    username = st.text_input("Username", placeholder="learner")
    password = st.text_input("Password", type="password", placeholder="••••••••••••")

    if st.button("Sign In →", use_container_width=True, type="primary"):
        if username == "learner" and password == "buildit2024":
            st.session_state.authenticated = True
            st.session_state.username = username
            if "completed_modules" not in st.session_state:
                st.session_state.completed_modules = []
            st.switch_page("pages/1_Home.py")
        else:
            st.error("Incorrect credentials. Try: learner / buildit2024")

    st.markdown(
        "<div style='text-align:center; margin-top:1rem; color:#475569; font-size:0.8rem;'>"
        "Demo: <code>learner</code> / <code>buildit2024</code></div>",
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)
