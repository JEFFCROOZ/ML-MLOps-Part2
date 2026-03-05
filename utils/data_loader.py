import pandas as pd


# ── Monitoring simulation data ──────────────────────────────────────────────

def get_monitoring_data() -> pd.DataFrame:
    """
    Pre-seeded 16-week monitoring dataset for the drift simulation dashboard.
    Represents a recommendation engine that was deployed healthy and gradually
    experiences data drift as action-movie ratings grow in the user base.
    """
    data = {
        "week": list(range(1, 17)),
        "week_label": [f"Week {i}" for i in range(1, 17)],
        # Performance metrics — gradual RMSE/MAE degradation
        "rmse": [
            0.914, 0.919, 0.923, 0.931,   # Weeks 1–4:  healthy
            0.941, 0.952, 0.963, 0.971,   # Weeks 5–8:  mild drift
            0.982, 0.998, 1.012, 1.031,   # Weeks 9–12: warning zone
            1.052, 1.071, 1.089, 1.112,   # Weeks 13–16: critical
        ],
        "mae": [
            0.718, 0.722, 0.725, 0.731,
            0.738, 0.745, 0.751, 0.758,
            0.765, 0.774, 0.783, 0.795,
            0.808, 0.821, 0.834, 0.849,
        ],
        # Catalog coverage — slowly eroding
        "coverage": [
            84.2, 83.8, 83.5, 83.1,
            82.4, 81.8, 81.1, 80.3,
            79.1, 77.8, 76.4, 74.9,
            73.2, 71.1, 68.9, 65.7,
        ],
        # Genre distribution — action overtaking the catalog
        "action_pct": [
            18.1, 18.4, 18.9, 19.5,
            20.2, 21.1, 21.8, 22.7,
            23.6, 24.5, 25.8, 27.1,
            28.4, 29.8, 31.2, 32.7,
        ],
        "drama_pct": [
            22.3, 22.1, 21.9, 21.6,
            21.2, 20.8, 20.5, 20.1,
            19.8, 19.4, 19.0, 18.6,
            18.2, 17.8, 17.4, 17.0,
        ],
        "comedy_pct": [
            16.8, 16.7, 16.6, 16.5,
            16.3, 16.1, 15.9, 15.8,
            15.6, 15.4, 15.2, 14.9,
            14.7, 14.5, 14.2, 13.9,
        ],
        "thriller_pct": [
            12.4, 12.4, 12.3, 12.3,
            12.2, 12.1, 12.1, 12.0,
            11.9, 11.8, 11.7, 11.6,
            11.5, 11.4, 11.3, 11.2,
        ],
        "other_pct": [
            30.4, 30.4, 30.3, 30.1,
            30.1, 29.9, 29.7, 29.4,
            29.1, 28.9, 28.3, 27.8,
            27.2, 26.5, 25.9, 25.2,
        ],
        # Pipeline health — week 8 had a delay (simulated incident)
        "pipeline_status": [
            "OK", "OK", "OK", "OK",
            "OK", "OK", "OK", "DELAYED",
            "OK", "OK", "OK", "OK",
            "OK", "OK", "OK", "OK",
        ],
        # Raw rating volume — drops sharply during the week-8 pipeline delay
        "new_ratings": [
            8421, 8756, 8234, 9102,
            8567, 8823, 9145, 3241,
            8934, 9012, 8678, 8891,
            9234, 8956, 9102, 9445,
        ],
    }
    return pd.DataFrame(data)


def get_alert_level(rmse: float, coverage: float) -> str:
    """
    Determine alert level based on current RMSE and coverage metrics.
    Returns: 'healthy' | 'warning' | 'critical'
    """
    if rmse >= 1.05 or coverage < 70.0:
        return "critical"
    elif rmse >= 1.0 or coverage < 80.0:
        return "warning"
    else:
        return "healthy"


def get_alert_copy(level: str, week: int, rmse: float, coverage: float) -> dict:
    """Return title and body copy for the alert card based on alert level."""
    if level == "healthy":
        return {
            "title": "All Systems Healthy",
            "body": (
                f"RMSE is {rmse:.3f} (baseline 0.914) and coverage is {coverage:.1f}%. "
                "No action required. Continue monitoring on schedule."
            ),
        }
    elif level == "warning":
        issues = []
        if rmse >= 1.0:
            issues.append(f"RMSE {rmse:.3f} has crossed the 1.0 threshold")
        if coverage < 80.0:
            issues.append(f"Coverage {coverage:.1f}% has dropped below 80%")
        return {
            "title": f"Warning — Week {week}",
            "body": (
                f"{' · '.join(issues)}. "
                "Review manually. Consider accelerating the next scheduled retrain."
            ),
        }
    else:  # critical
        issues = []
        if rmse >= 1.05:
            issues.append(f"RMSE {rmse:.3f} exceeds critical threshold of 1.05")
        if coverage < 70.0:
            issues.append(f"Coverage {coverage:.1f}% has dropped below 70%")
        return {
            "title": f"Critical — Week {week} — Action Required",
            "body": (
                f"{' · '.join(issues)}. "
                "Automated retrain should be triggered immediately. "
                "If retrain does not resolve metrics within one week, escalate."
            ),
        }


# ── Experiment log sample data ──────────────────────────────────────────────

EXPERIMENT_LOG = [
    {
        "run_id": "run_20240115_001",
        "timestamp": "2024-01-15 09:12",
        "model_type": "SVD (Collaborative)",
        "n_factors": 50,
        "lr_all": 0.005,
        "reg_all": 0.02,
        "n_epochs": 20,
        "rmse": 0.9401,
        "mae": 0.7381,
        "coverage_pct": 81.4,
        "train_time_s": 198,
        "notes": "Baseline run. 50 latent factors.",
    },
    {
        "run_id": "run_20240212_001",
        "timestamp": "2024-02-12 14:33",
        "model_type": "SVD (Collaborative)",
        "n_factors": 100,
        "lr_all": 0.005,
        "reg_all": 0.02,
        "n_epochs": 20,
        "rmse": 0.9147,
        "mae": 0.7183,
        "coverage_pct": 84.2,
        "train_time_s": 252,
        "notes": "Increased n_factors from 50 → 100. RMSE improved by 0.025.",
    },
    {
        "run_id": "run_20240212_002",
        "timestamp": "2024-02-12 16:05",
        "model_type": "SVD (Collaborative)",
        "n_factors": 100,
        "lr_all": 0.005,
        "reg_all": 0.02,
        "n_epochs": 20,
        "rmse": 0.9701,
        "mae": 0.7512,
        "coverage_pct": 79.8,
        "train_time_s": 244,
        "notes": "Same config but trained on 6-month window only. Shorter window hurt RMSE.",
    },
    {
        "run_id": "run_20240315_001",
        "timestamp": "2024-03-15 09:42",
        "model_type": "SVD (Collaborative)",
        "n_factors": 100,
        "lr_all": 0.005,
        "reg_all": 0.02,
        "n_epochs": 20,
        "rmse": 0.9147,
        "mae": 0.7183,
        "coverage_pct": 84.2,
        "train_time_s": 252,
        "notes": "Retrain on Jan–Dec 2023 data. Same perf as Feb run. Promoting to staging.",
    },
]


# ── Model registry sample data ───────────────────────────────────────────────

REGISTRY_ENTRIES = [
    {
        "version": "v2.1",
        "stage": "Archived",
        "registered": "2024-01-15",
        "promoted": "2024-01-18",
        "rmse": 0.9401,
        "coverage": 81.4,
        "notes": "First production model. Retired when v2.2 outperformed.",
    },
    {
        "version": "v2.2",
        "stage": "Archived",
        "registered": "2024-02-12",
        "promoted": "2024-02-15",
        "rmse": 0.9147,
        "coverage": 84.2,
        "notes": "100 latent factors. Replaced v2.1. Retired when v2.3 released.",
    },
    {
        "version": "v2.3",
        "stage": "Production",
        "registered": "2024-03-15",
        "promoted": "2024-03-18",
        "rmse": 0.9147,
        "coverage": 84.2,
        "notes": "Retrained on Jan–Dec 2023 data. Currently serving all users.",
    },
    {
        "version": "v2.4",
        "stage": "Staging",
        "registered": "2024-04-01",
        "promoted": "—",
        "rmse": 0.9031,
        "coverage": 83.1,
        "notes": "Candidate. Pending sign-off. Coverage slightly lower — under review.",
    },
]
