import streamlit as st


def inject_global_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #0e1b26;
        color: #e2e8f0;
    }

    /* Hide default Streamlit UI chrome */
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { visibility: hidden; }
    .stDeployButton { display: none; }

    /* Scrollbar */
    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: #0e1b26; }
    ::-webkit-scrollbar-thumb { background: #106f8a; border-radius: 3px; }

    /* Main content area */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 4rem;
        max-width: 860px;
    }

    /* Headings */
    h1, h2, h3, h4 {
        color: #e2e8f0;
        font-family: 'Inter', sans-serif;
        font-weight: 600;
    }

    h1 { font-size: 2rem; margin-bottom: 0.5rem; }
    h2 { font-size: 1.4rem; margin-top: 2rem; margin-bottom: 0.75rem; border-bottom: 1px solid #1e3448; padding-bottom: 0.4rem; }
    h3 { font-size: 1.1rem; margin-top: 1.5rem; }

    /* Body text */
    p, li { color: #cbd5e1; line-height: 1.75; font-size: 0.97rem; }

    /* Code blocks */
    code {
        font-family: 'JetBrains Mono', monospace;
        background-color: #162230;
        color: #7dd3fc;
        padding: 0.15rem 0.4rem;
        border-radius: 4px;
        font-size: 0.85rem;
    }

    pre code {
        display: block;
        padding: 1rem;
        overflow-x: auto;
        line-height: 1.6;
        color: #e2e8f0;
    }

    /* Buttons */
    .stButton > button {
        background-color: #106f8a;
        color: #ffffff;
        border: none;
        border-radius: 6px;
        font-family: 'Inter', sans-serif;
        font-weight: 500;
        padding: 0.5rem 1.25rem;
        transition: background-color 0.2s ease;
    }
    .stButton > button:hover {
        background-color: #0e5f77;
        color: #ffffff;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #0e1b26;
        border-right: 1px solid #1e3448;
    }
    [data-testid="stSidebar"] .stMarkdown p { color: #94a3b8; font-size: 0.875rem; }

    /* Module tile cards */
    .module-tile {
        background-color: #162230;
        border: 1px solid #1e3448;
        border-radius: 10px;
        padding: 1.25rem;
        margin-bottom: 0.75rem;
        transition: border-color 0.2s ease;
    }
    .module-tile:hover { border-color: #106f8a; }
    .module-tile h4 { margin: 0 0 0.3rem 0; font-size: 0.95rem; color: #e2e8f0; }
    .module-tile p { margin: 0; font-size: 0.82rem; color: #64748b; }

    /* Status badges */
    .badge-complete {
        background-color: #14532d;
        color: #86efac;
        padding: 0.2rem 0.6rem;
        border-radius: 99px;
        font-size: 0.75rem;
        font-weight: 500;
    }
    .badge-progress {
        background-color: #1e3a5f;
        color: #93c5fd;
        padding: 0.2rem 0.6rem;
        border-radius: 99px;
        font-size: 0.75rem;
        font-weight: 500;
    }
    .badge-pending {
        background-color: #1e293b;
        color: #475569;
        padding: 0.2rem 0.6rem;
        border-radius: 99px;
        font-size: 0.75rem;
        font-weight: 500;
    }

    /* Alert badges for monitoring */
    .alert-healthy {
        background-color: #14532d;
        color: #86efac;
        border: 1px solid #166534;
        padding: 0.75rem 1rem;
        border-radius: 8px;
        font-size: 0.9rem;
        font-weight: 500;
    }
    .alert-warning {
        background-color: #451a03;
        color: #fcd34d;
        border: 1px solid #92400e;
        padding: 0.75rem 1rem;
        border-radius: 8px;
        font-size: 0.9rem;
        font-weight: 500;
    }
    .alert-critical {
        background-color: #450a0a;
        color: #fca5a5;
        border: 1px solid #991b1b;
        padding: 0.75rem 1rem;
        border-radius: 8px;
        font-size: 0.9rem;
        font-weight: 500;
    }

    /* Login card */
    .login-card {
        background-color: #162230;
        border: 1px solid #1e3448;
        border-radius: 12px;
        padding: 2rem;
    }

    /* Part 1 callout */
    .part1-callout {
        background-color: #0c3547;
        border-left: 4px solid #106f8a;
        border-radius: 0 8px 8px 0;
        padding: 1rem 1.25rem;
        margin-bottom: 2rem;
    }
    .part1-callout p { color: #93c5fd; margin: 0; font-size: 0.92rem; }
    .part1-callout strong { color: #e2e8f0; }

    /* Narrative callout (takeaway) */
    .takeaway-box {
        background-color: #0c3547;
        border-left: 4px solid #106f8a;
        border-radius: 0 8px 8px 0;
        padding: 1rem 1.25rem;
        margin: 1.5rem 0;
    }
    .takeaway-box p { color: #cbd5e1; margin: 0; font-size: 0.92rem; }

    /* BTS (behind the scenes) note */
    .bts-box {
        background-color: #1a2535;
        border: 1px dashed #334155;
        border-radius: 8px;
        padding: 0.85rem 1.1rem;
        margin: 1rem 0;
    }
    .bts-box p { color: #94a3b8; margin: 0; font-size: 0.875rem; font-style: italic; }

    /* Step label */
    .step-label {
        display: inline-flex;
        align-items: center;
        gap: 0.6rem;
        margin: 1.25rem 0 0.5rem 0;
    }
    .step-num {
        background-color: #106f8a;
        color: #ffffff;
        font-weight: 700;
        font-size: 0.8rem;
        width: 1.6rem;
        height: 1.6rem;
        border-radius: 50%;
        display: inline-flex;
        align-items: center;
        justify-content: center;
    }
    .step-text { color: #e2e8f0; font-weight: 600; font-size: 0.95rem; }

    /* Horizontal divider */
    .section-break {
        border: none;
        border-top: 1px solid #1e3448;
        margin: 2rem 0;
    }

    /* Metric cards for monitoring */
    .metric-card {
        background-color: #162230;
        border: 1px solid #1e3448;
        border-radius: 8px;
        padding: 1rem;
        text-align: center;
    }
    .metric-label { color: #64748b; font-size: 0.78rem; font-weight: 500; text-transform: uppercase; letter-spacing: 0.05em; }
    .metric-value { color: #e2e8f0; font-size: 1.5rem; font-weight: 700; margin: 0.25rem 0; }
    .metric-delta-pos { color: #86efac; font-size: 0.8rem; }
    .metric-delta-neg { color: #fca5a5; font-size: 0.8rem; }

    /* Tables */
    table { width: 100%; border-collapse: collapse; margin: 1rem 0; }
    th {
        background-color: #162230;
        color: #94a3b8;
        font-size: 0.8rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        padding: 0.6rem 0.75rem;
        text-align: left;
        border-bottom: 1px solid #1e3448;
    }
    td {
        padding: 0.6rem 0.75rem;
        border-bottom: 1px solid #1a2535;
        color: #cbd5e1;
        font-size: 0.875rem;
    }
    tr:last-child td { border-bottom: none; }

    /* Streamlit native overrides */
    .stTextInput > div > div > input {
        background-color: #162230;
        border: 1px solid #1e3448;
        color: #e2e8f0;
        border-radius: 6px;
    }
    .stTextInput > div > div > input:focus {
        border-color: #106f8a;
        box-shadow: 0 0 0 2px rgba(16, 111, 138, 0.25);
    }
    .stSlider > div { color: #e2e8f0; }
    [data-testid="stMetricValue"] { color: #e2e8f0; }
    [data-testid="stMetricLabel"] { color: #94a3b8; }

    /* Streamlit expander */
    .streamlit-expanderHeader {
        background-color: #162230;
        border: 1px solid #1e3448;
        border-radius: 6px;
        color: #cbd5e1;
    }
    </style>
    """, unsafe_allow_html=True)


def takeaway(text):
    st.markdown(f"""
    <div class="takeaway-box">
        <p>💡 <strong>Key Takeaway:</strong> {text}</p>
    </div>
    """, unsafe_allow_html=True)


def bts(text):
    st.markdown(f"""
    <div class="bts-box">
        <p>🔧 <em>{text}</em></p>
    </div>
    """, unsafe_allow_html=True)


def section_break():
    st.markdown('<hr class="section-break">', unsafe_allow_html=True)


def step_label(n, text):
    st.markdown(f"""
    <div class="step-label">
        <span class="step-num">{n}</span>
        <span class="step-text">{text}</span>
    </div>
    """, unsafe_allow_html=True)


def badge(status):
    classes = {
        "complete": "badge-complete",
        "in_progress": "badge-progress",
        "pending": "badge-pending"
    }
    labels = {
        "complete": "✓ Complete",
        "in_progress": "→ In Progress",
        "pending": "Not Started"
    }
    css = classes.get(status, "badge-pending")
    label = labels.get(status, "Not Started")
    return f'<span class="{css}">{label}</span>'


def part1_callout(part1_url="#"):
    st.markdown(f"""
    <div class="part1-callout">
        <p>
            <strong>Haven't built your recommendation engine yet?</strong><br>
            This is Part 2. Start with Part 1 first — it makes everything here click.
            &nbsp;&nbsp;<a href="{part1_url}" target="_blank" style="color: #38bdf8; font-weight: 600; text-decoration: none;">→ Go to Part 1</a>
        </p>
    </div>
    """, unsafe_allow_html=True)


def alert_card(level, title, body):
    css_class = {
        "healthy": "alert-healthy",
        "warning": "alert-warning",
        "critical": "alert-critical"
    }.get(level, "alert-healthy")

    icon = {"healthy": "✅", "warning": "⚠️", "critical": "🔴"}.get(level, "✅")

    st.markdown(f"""
    <div class="{css_class}" style="margin: 1rem 0;">
        <div style="font-weight: 700; margin-bottom: 0.3rem;">{icon} {title}</div>
        <div style="font-size: 0.85rem; opacity: 0.9;">{body}</div>
    </div>
    """, unsafe_allow_html=True)


def require_auth():
    """Check authentication and redirect to login if not authenticated."""
    if not st.session_state.get("authenticated"):
        st.switch_page("app.py")


def mark_complete(module_name):
    """Add a module to the completed list in session state."""
    if "completed_modules" not in st.session_state:
        st.session_state.completed_modules = []
    if module_name not in st.session_state.completed_modules:
        st.session_state.completed_modules.append(module_name)


def nav_buttons(prev_page=None, next_page=None, module_name=None):
    """Render previous / mark complete / next navigation row."""
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if prev_page:
            if st.button("← Previous", use_container_width=True):
                st.switch_page(prev_page)
    with col2:
        if module_name:
            if st.button("✓ Mark Complete", use_container_width=True, type="primary"):
                mark_complete(module_name)
                st.success("Module marked complete!")
    with col3:
        if next_page:
            if st.button("Next →", use_container_width=True):
                st.switch_page(next_page)
