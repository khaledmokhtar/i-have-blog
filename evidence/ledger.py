"""Persistent Evidence Store for long-term claim cataloging."""

import json
from pathlib import Path
from typing import List, Optional, Dict
from core.schemas import ClaimRecord

class PersistentEvidenceStore:
    """Saves and indexes verified claims across all published articles."""

    def __init__(self, storage_path: Path):
        self.path = storage_path
        self.claims: Dict[str, ClaimRecord] = {}
        self._load()

    def _load(self):
        if self.path.exists():
            try:
                data = json.loads(self.path.read_text(encoding="utf-8"))
                for item in data.get("claims", []):
                    self.claims[item["claim_id"]] = ClaimRecord.from_dict(item)
            except Exception:
                pass

    def save(self):
        data = {"claims": [c.to_dict() for c in self.claims.values()]}
        self.path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

    def add_claim(self, claim: ClaimRecord):
        self.claims[claim.claim_id] = claim
        self.save()

    def get_claim(self, claim_id: str) -> Optional[ClaimRecord]:
        return self.claims.get(claim_id)
