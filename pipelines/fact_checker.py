"""Fact Checker Pipeline: Claim validation, verification status, and freshness policy."""

import re
from datetime import datetime
from typing import List, Dict, Any
from core.schemas import DraftResult, EvidenceLedger, FactCheckResult, ClaimRecord
from core.config import EngineConfig

class FactCheckerPipeline:
    """Verifies all claims tagged in the draft against evidence ledger and freshness rules."""

    def run(self, draft: DraftResult, evidence: EvidenceLedger) -> FactCheckResult:
        claims_map = {c.claim_id: c for c in evidence.claims}
        tagged_ids = draft.claims_tagged
        
        verified = 0
        modified = 0
        rejected = 0
        audit_records: List[Dict[str, Any]] = []
        warnings: List[str] = []

        for cid in tagged_ids:
            claim = claims_map.get(cid)
            if not claim:
                rejected += 1
                warnings.append(f"Untracked claim found: {cid} lacks evidence entry.")
                audit_records.append({"claim_id": cid, "status": "REJECTED", "reason": "Missing from ledger"})
                continue

            # Freshness evaluation
            is_fresh, freshness_reason = self._check_freshness(claim)
            if not is_fresh:
                modified += 1
                warnings.append(f"Claim {cid} warning: {freshness_reason}")
                audit_records.append({"claim_id": cid, "status": "FLAGGED_FRESHNESS", "reason": freshness_reason})
            else:
                verified += 1
                audit_records.append({
                    "claim_id": cid,
                    "type": claim.claim_type,
                    "status": "VERIFIED",
                    "confidence": claim.confidence,
                    "source": claim.source
                })

        passed = (rejected == 0 and verified > 0)
        return FactCheckResult(
            verified_count=verified,
            modified_count=modified,
            rejected_count=rejected,
            claims_audit=audit_records,
            warnings=warnings,
            passed=passed,
        )

    def _check_freshness(self, claim: ClaimRecord) -> tuple[bool, str]:
        # Parse verification date
        try:
            v_date = datetime.strptime(claim.verified_at, "%Y-%m-%d")
            age_months = (datetime.now() - v_date).days // 30
        except Exception:
            return True, "Valid date format"

        if claim.claim_type == "TIME_SENSITIVE" and age_months > EngineConfig.FRESHNESS_SOFTWARE_MONTHS:
            return False, f"Time-sensitive claim is {age_months} months old (max allowed: {EngineConfig.FRESHNESS_SOFTWARE_MONTHS})"
        if claim.claim_type == "STATISTIC" and age_months > EngineConfig.FRESHNESS_STATS_MONTHS:
            return False, f"Statistic is {age_months} months old (max allowed: {EngineConfig.FRESHNESS_STATS_MONTHS})"
        return True, "Fresh"
