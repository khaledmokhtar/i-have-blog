"""Refresh Pipeline: Content Decay Score calculator and update action planner."""

from typing import List
from core.schemas import ContentDecayResult

class RefreshPipeline:
    """Quantifies content decay and prescribes surgical refresh actions."""

    def run(
        self,
        target: str,
        age_months: int = 14,
        traffic_loss_pct: float = 28.0,
        serp_drift_score: float = 65.0,
        outdated_claims_count: int = 4
    ) -> ContentDecayResult:
        # Calculate compound decay score (0 to 100)
        # Weights: Traffic loss (35%), SERP drift (30%), Outdated claims (25%), Age (10%)
        decay = (
            (traffic_loss_pct * 0.35)
            + (serp_drift_score * 0.30)
            + (min(outdated_claims_count * 12.0, 100.0) * 0.25)
            + (min(age_months * 3.0, 100.0) * 0.10)
        )
        decay_score = round(min(100.0, max(0.0, decay)), 1)

        # Determine action
        if decay_score >= 75.0:
            action = "EXPAND_AND_REWRITE"
            plan = [
                "Full architectural rewrite: SERP has completely evolved.",
                "Recalculate all benchmarks and replace outdated 2024/2025 statistics.",
                "Update Schema markup and add modern FAQPage entities.",
                "Add interactive calculator snippet or downloadable sheet.",
            ]
        elif decay_score >= 50.0:
            action = "UPDATE"
            plan = [
                f"Surgically update {outdated_claims_count} outdated claims and pricing tiers.",
                "Inject fresh 2026 case study data.",
                "Check external links for 404s or redirects.",
                "Re-audit internal linking anchors.",
            ]
        elif decay_score >= 25.0:
            action = "KEEP_MONITOR"
            plan = [
                "Content is stable. Re-verify in 90 days.",
                "Add 1–2 internal links from newly published high-performing posts.",
            ]
        else:
            action = "KEEP"
            plan = ["Top-performing evergreen asset. No modification required."]

        return ContentDecayResult(
            target=target,
            age_months=age_months,
            traffic_loss_pct=traffic_loss_pct,
            serp_drift_score=serp_drift_score,
            outdated_claims_count=outdated_claims_count,
            decay_score=decay_score,
            action=action,
            refresh_plan=plan,
        )
