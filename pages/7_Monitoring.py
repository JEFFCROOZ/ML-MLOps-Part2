import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from utils.styles import (
    inject_global_css, require_auth, section_break,
    takeaway, bts, step_label, nav_buttons, alert_card
)
from utils.data_loader import get_monitoring_data, get_alert_level, get_alert_copy

st.set_page_config(
    page_title="Monitoring, Drift & Response — MLOps Part 2",
    page_icon="📡",
    layout="centered",
    initial_sidebar_state="collapsed",
)

inject_global_css()
require_auth()

CHART_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="#162230",
    font=dict(color="#e2e8f0", family="Inter, sans-serif", size=12),
    margin=dict(l=10, r=10, t=30, b=10),
    xaxis=dict(gridcolor="#1e3448", linecolor="#1e3448"),
    hovermode="x unified",
)
YAXIS_BASE = dict(gridcolor="#1e3448", linecolor="#1e3448")

df_full = get_monitoring_data()

# ── Header ───────────────────────────────────────────────────────────────────
st.markdown(
    "<p style='color:#106f8a; font-size:0.85rem; font-weight:600; "
    "text-transform:uppercase; letter-spacing:0.08em;'>Module 5</p>",
    unsafe_allow_html=True,
)
st.markdown("## Monitoring, Drift & Response")
st.markdown(
    "Your model is in production. Users are receiving recommendations. Everything looks fine. "
    "**But is it?** Use the dashboard below to watch what actually happens as weeks go by."
)

section_break()

# ══════════════════════════════════════════════════════════════════════════════
# INTERACTIVE DRIFT DASHBOARD
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("### Live drift simulation")
st.markdown(
    "Drag the slider forward in time. Watch how the model's health changes — "
    "and notice when the alerts start firing."
)

week = st.slider(
    "Weeks since deployment",
    min_value=1,
    max_value=16,
    value=1,
    step=1,
    help="Drag right to simulate the passage of time and watch drift accumulate.",
)

df = df_full[df_full["week"] <= week].copy()
current = df_full[df_full["week"] == week].iloc[0]

rmse_now = current["rmse"]
mae_now = current["mae"]
coverage_now = current["coverage"]
pipeline_now = current["pipeline_status"]
ratings_now = int(current["new_ratings"])
alert_level = get_alert_level(rmse_now, coverage_now)
alert_info = get_alert_copy(alert_level, week, rmse_now, coverage_now)

# ── Alert card ────────────────────────────────────────────────────────────────
alert_card(alert_level, alert_info["title"], alert_info["body"])

# ── Metric summary row ────────────────────────────────────────────────────────
m1, m2, m3, m4 = st.columns(4)

rmse_delta = rmse_now - 0.914
coverage_delta = coverage_now - 84.2

with m1:
    st.metric(
        "RMSE",
        f"{rmse_now:.3f}",
        delta=f"{rmse_delta:+.3f}",
        delta_color="inverse",
    )
with m2:
    st.metric(
        "MAE",
        f"{mae_now:.3f}",
        delta=f"{mae_now - 0.718:+.3f}",
        delta_color="inverse",
    )
with m3:
    st.metric(
        "Coverage",
        f"{coverage_now:.1f}%",
        delta=f"{coverage_delta:+.1f}%",
        delta_color="normal",
    )
with m4:
    st.metric(
        "Pipeline",
        pipeline_now,
        delta="On schedule" if pipeline_now == "OK" else "Delayed",
        delta_color="normal" if pipeline_now == "OK" else "inverse",
    )

st.markdown("<div style='margin-top:1rem;'></div>", unsafe_allow_html=True)

# ── RMSE Trend ────────────────────────────────────────────────────────────────
col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    st.markdown("**RMSE over time**")
    fig_rmse = go.Figure()
    fig_rmse.add_trace(go.Scatter(
        x=df["week_label"], y=df["rmse"],
        mode="lines+markers",
        name="RMSE",
        line=dict(color="#38bdf8", width=2),
        marker=dict(size=5),
    ))
    # Warning threshold line
    fig_rmse.add_hline(
        y=1.0, line_dash="dash", line_color="#fcd34d",
        annotation_text="Warning (1.0)", annotation_position="top right",
        annotation_font_color="#fcd34d",
    )
    # Critical threshold line
    fig_rmse.add_hline(
        y=1.05, line_dash="dash", line_color="#fca5a5",
        annotation_text="Critical (1.05)", annotation_position="top right",
        annotation_font_color="#fca5a5",
    )
    fig_rmse.update_layout(
        **CHART_LAYOUT,
        yaxis={**YAXIS_BASE, "range": [0.88, 1.18]},
        showlegend=False,
        height=240,
    )
    st.plotly_chart(fig_rmse, use_container_width=True)

# ── Coverage Trend ────────────────────────────────────────────────────────────
with col_chart2:
    st.markdown("**Catalog coverage %**")
    fig_cov = go.Figure()
    cov_colors = []
    for _, row in df.iterrows():
        if row["coverage"] < 70:
            cov_colors.append("#fca5a5")
        elif row["coverage"] < 80:
            cov_colors.append("#fcd34d")
        else:
            cov_colors.append("#86efac")

    fig_cov.add_trace(go.Scatter(
        x=df["week_label"], y=df["coverage"],
        mode="lines+markers",
        name="Coverage",
        line=dict(color="#86efac", width=2),
        marker=dict(size=5, color=cov_colors),
    ))
    fig_cov.add_hline(
        y=80, line_dash="dash", line_color="#fcd34d",
        annotation_text="Warning (80%)", annotation_position="bottom right",
        annotation_font_color="#fcd34d",
    )
    fig_cov.add_hline(
        y=70, line_dash="dash", line_color="#fca5a5",
        annotation_text="Critical (70%)", annotation_position="bottom right",
        annotation_font_color="#fca5a5",
    )
    fig_cov.update_layout(
        **CHART_LAYOUT,
        yaxis={**YAXIS_BASE, "range": [60, 88]},
        showlegend=False,
        height=240,
    )
    st.plotly_chart(fig_cov, use_container_width=True)

# ── Genre drift chart ─────────────────────────────────────────────────────────
st.markdown("**Genre distribution — baseline vs. now**")
st.markdown(
    "<span style='color:#64748b; font-size:0.82rem;'>"
    "Watch Action grow as weeks pass — this is data drift in action.</span>",
    unsafe_allow_html=True,
)

genres = ["Action", "Drama", "Comedy", "Thriller", "Other"]
baseline_vals = [18.1, 22.3, 16.8, 12.4, 30.4]
current_vals = [
    current["action_pct"], current["drama_pct"],
    current["comedy_pct"], current["thriller_pct"], current["other_pct"],
]

fig_genre = go.Figure(data=[
    go.Bar(
        name="Baseline (Week 1)",
        x=genres,
        y=baseline_vals,
        marker_color="#475569",
    ),
    go.Bar(
        name=f"Week {week}",
        x=genres,
        y=current_vals,
        marker_color="#106f8a",
    ),
])
fig_genre.update_layout(
    **CHART_LAYOUT,
    barmode="group",
    legend=dict(orientation="h", y=1.15, x=0),
    height=260,
    yaxis={**YAXIS_BASE, "title": "% of ratings"},
)
st.plotly_chart(fig_genre, use_container_width=True)

# ── Weekly health card ────────────────────────────────────────────────────────
with st.expander(f"📋 Full health report — Week {week}"):
    action_drift = current["action_pct"] - 18.1
    drift_flag = "⚠️ Drift detected" if abs(action_drift) > 3 else "✅ Stable"
    pipeline_flag = "⚠️ DELAYED" if pipeline_now == "DELAYED" else "✅ OK"

    st.markdown(f"""
```
Movie Recommender — Weekly Health Report (Week {week})

Model Version:       v2.3 (deployed Week 1)

Performance
  RMSE (this week):   {rmse_now:.3f}     [baseline: 0.914]
  MAE  (this week):   {mae_now:.3f}     [baseline: 0.718]

Data Quality
  New ratings:        {ratings_now:,}   [expected: ~8,000–10,000]
  Pipeline status:    {pipeline_flag}
  Action genre:       {current['action_pct']:.1f}%  [baseline: 18.1%]  {drift_flag}

Recommendation Quality
  Catalog coverage:   {coverage_now:.1f}%    [launch: 84.2%]

Alert level:         {alert_level.upper()}
Next scheduled retrain: Week {min(week + (7 - week % 7), 16)} (Sunday)
```
    """)

section_break()

# ── Concept explainers ────────────────────────────────────────────────────────
st.markdown("### Understanding what you just saw")

tab_dd, tab_cd, tab_alert = st.tabs(["📊 Data Drift", "🔄 Concept Drift", "🔔 Alerting & Response"])

with tab_dd:
    st.markdown("#### Data drift — when the inputs change")
    st.markdown(
        "The genre distribution chart shows **data drift**: action movies are making up "
        "a growing share of ratings. This means your model is being asked to make "
        "predictions in territory it wasn't trained on as heavily."
    )
    st.markdown(
        "The model still produces predictions. They're formatted correctly. No errors are "
        "thrown. But they're less reliable for action fans — because the model's internal "
        "understanding of action movies is now based on stale data."
    )
    st.markdown(
        "**Data drift is the most common type** and the easiest to detect — "
        "because you can measure the distribution of your inputs directly."
    )

with tab_cd:
    st.markdown("#### Concept drift — when the relationship changes")
    st.markdown(
        "Concept drift is subtler. It happens when the underlying relationship between "
        "your model's inputs and the correct output changes — even if the data distribution "
        "looks similar."
    )
    st.markdown(
        "**Example:** Five years ago, a high average rating strongly predicted that a user "
        "would enjoy a film. Today, users weight recent reviews and word-of-mouth more heavily. "
        "The model optimizes for a signal that no longer maps cleanly to satisfaction."
    )
    st.markdown(
        "Concept drift is harder to detect — you need user behavior signals "
        "(engagement, post-recommendation ratings) to catch it, not just input distributions."
    )

with tab_alert:
    st.markdown("#### What makes a good alert")
    cols = st.columns(2)
    properties = [
        ("✅ Actionable", "Tells you something you can respond to — not just a raw number"),
        ("🎯 Specific", "Names the metric, the value, the threshold, and the likely cause"),
        ("🔇 Low noise", "Only fires when something genuinely needs attention"),
        ("📬 Routed correctly", "Reaches the right person at the right time"),
    ]
    for i, (title, desc) in enumerate(properties):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="module-tile" style="margin-bottom:0.5rem;">
                <h4 style="font-size:0.88rem;">{title}</h4>
                <p style="font-size:0.82rem;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("#### Alert levels")
    levels = [
        ("✅ Info", "#14532d", "#86efac", "Within normal range. Log it and watch the trend."),
        ("⚠️ Warning", "#451a03", "#fcd34d", "Outside normal range. Review within 48 hours."),
        ("🔴 Critical", "#450a0a", "#fca5a5", "Something may be broken. Needs prompt attention."),
    ]
    for icon_label, bg, color, desc in levels:
        st.markdown(f"""
        <div style="background:{bg}; border-radius:6px; padding:0.6rem 0.9rem;
                    margin-bottom:0.4rem; display:flex; gap:0.75rem; align-items:center;">
            <span style="color:{color}; font-weight:600; font-size:0.88rem; min-width:90px;">{icon_label}</span>
            <span style="color:#94a3b8; font-size:0.82rem;">{desc}</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("#### The runbook concept")
    st.markdown(
        "A runbook documents response steps for known alert types. "
        "It answers: *someone got notified at 2am — what do they do?*"
    )
    with st.expander("See a sample runbook entry: Pipeline has not run in 24+ hours"):
        st.code("""
Alert: Pipeline has not run in 24+ hours

1. Check pipeline scheduler — is the job still enabled?
2. Review error logs from the last failed run
3. Verify source data is available and accessible
4. If source is healthy → restart the pipeline manually
5. If source is down → notify upstream data owner, log the incident
6. Once pipeline runs → confirm data freshness metric recovers
7. If retrain is overdue → trigger manually after freshness restored
        """, language="text")

section_break()

# ── Hands on ──────────────────────────────────────────────────────────────────
st.markdown("### Try it yourself")

step_label(1, "Find the inflection point")
st.markdown(
    "Drag the slider to find the exact week where RMSE first crosses the **warning** threshold "
    "and then the **critical** threshold. What else changed in those same weeks?"
)

step_label(2, "Investigate the pipeline incident")
st.markdown(
    "One week in the simulation had a pipeline delay. Find it by watching the 'New ratings' "
    "metric in the health report. What effect did the delay have on the following week's metrics?"
)

step_label(3, "Write your own alert rule")
st.markdown(
    "For your own recommendation engine: define one alert rule. "
    "What metric? What threshold? What level (info / warning / critical)? "
    "What's the first step in your runbook for that alert?"
)

bts(
    "Monitoring tools like Grafana, Datadog, and cloud-native dashboards can be configured "
    "to watch these exact metrics in production. The logic — thresholds, alert levels, "
    "runbooks — is identical regardless of which tool renders the dashboard."
)

takeaway(
    "Drift is silent and gradual. Monitoring catches it. Alerting gets the right person's "
    "attention. A runbook gives them a path forward. All three are necessary — and none "
    "require sophisticated infrastructure to start."
)

section_break()

nav_buttons(
    prev_page="pages/6_Retraining.py",
    next_page="pages/8_Living_System.py",
    module_name="monitoring",
)
