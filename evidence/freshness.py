"""Freshness Policy enforcement module."""

from datetime import datetime
from core.schemas import ClaimRecord
from core.config import EngineConfig

class FreshnessPolicy:
    """Evaluates whether a claim or source is within the validity window."""

    @staticmethod
    def is_claim_stale(claim: ClaimRecord) -> bool:
        try:
            date_val = datetime.strptime(claim.verified_at, "%Y-%m-%d")
            months = (datetime.now() - date_val).days // 30
        except Exception:
            return False

        if claim.claim_type == "TIME_SENSITIVE":
            return months > EngineConfig.FRESHNESS_SOFTWARE_MONTHS
        if claim.claim_type == "STATISTIC":
            return months > EngineConfig.FRESHNESS_STATS_MONTHS
        return False
