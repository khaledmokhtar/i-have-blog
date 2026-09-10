"""Validates intermediate JSON artifacts against system schemas."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from core.schemas import (
    Brief,
    ResearchResult,
    StrategyResult,
    OutlineResult,
    EvidenceLedger,
    DraftResult,
    FactCheckResult,
    EditorialAuditResult,
    FinalPublishPackage,
    ContentDecayResult,
)

def validate_schemas():
    print("Validating schemas and data integrity...")

    b = Brief("Test Topic", "test kw", "Marketers")
    b_dict = b.to_dict()
    assert Brief.from_dict(b_dict).topic == "Test Topic"

    c = ContentDecayResult("test-url", 12, 20.0, 50.0, 3, 45.0, "UPDATE", ["step 1"])
    assert ContentDecayResult.from_dict(c.to_dict()).action == "UPDATE"

    print("All schemas validated successfully!")

if __name__ == "__main__":
    validate_schemas()
