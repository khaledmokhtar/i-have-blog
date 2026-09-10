"""Claim Registry for tracking, classifying, and verifying factual statements."""

import re
from typing import List, Dict, Tuple, Optional
from datetime import datetime
from .schemas import ClaimRecord, EvidenceLedger

class ClaimRegistry:
    """Registers and indexes claims embedded as [claim:C-xxx] in drafts."""

    CLAIM_TAG_REGEX = re.compile(r"\[claim:(C-\d{3,})\]")

    def __init__(self):
        self.claims: Dict[str, ClaimRecord] = {}
        self._next_id = 1

    def generate_id(self) -> str:
        cid = f"C-{self._next_id:03d}"
        self._next_id += 1
        return cid

    def register_claim(
        self,
        text: str,
        claim_type: str,
        source: str,
        confidence: float = 0.95,
        verified_at: Optional[str] = None,
        status: str = "VERIFIED",
        note: str = ""
    ) -> ClaimRecord:
        cid = self.generate_id()
        now = verified_at or datetime.now().strftime("%Y-%m-%d")
        record = ClaimRecord(
            claim_id=cid,
            text=text.strip(),
            claim_type=claim_type.upper(),
            source=source.strip(),
            confidence=confidence,
            verified_at=now,
            status=status,
            note=note,
        )
        self.claims[cid] = record
        return record

    def extract_claim_ids(self, text: str) -> List[str]:
        return self.CLAIM_TAG_REGEX.findall(text)

    def strip_claim_tags(self, text: str) -> str:
        """Removes [claim:C-xxx] markers for final clean production output."""
        return self.CLAIM_TAG_REGEX.sub("", text).replace("  ", " ")

    def to_ledger(self) -> EvidenceLedger:
        return EvidenceLedger(claims=list(self.claims.values()))

    @classmethod
    def from_ledger(cls, ledger: EvidenceLedger) -> "ClaimRegistry":
        registry = cls()
        max_id = 0
        for c in ledger.claims:
            registry.claims[c.claim_id] = c
            match = re.match(r"C-(\d+)", c.claim_id)
            if match:
                max_id = max(max_id, int(match.group(1)))
        registry._next_id = max_id + 1
        return registry
