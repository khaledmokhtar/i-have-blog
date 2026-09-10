"""Tests for schemas serialization and round-trip fidelity."""

import unittest
from core.schemas import (
    Brief,
    ResearchResult,
    StrategyResult,
    OutlineResult,
    OutlineSection,
    ClaimRecord,
    EvidenceLedger,
    ContentDecayResult,
)

class TestSchemas(unittest.TestCase):
    def test_brief_roundtrip(self):
        b = Brief(topic="Meta Ads", primary_keyword="meta ads", audience="Growth Teams")
        d = b.to_dict()
        b2 = Brief.from_dict(d)
        self.assertEqual(b.topic, b2.topic)
        self.assertEqual(b.audience, b2.audience)

    def test_outline_roundtrip(self):
        sec = OutlineSection("Intro", 2, "Goal", "Gap", ["Point 1"], ["Evidence 1"], 300)
        outline = OutlineResult("Title", "H1", [sec], 300)
        d = outline.to_dict()
        outline2 = OutlineResult.from_dict(d)
        self.assertEqual(len(outline2.sections), 1)
        self.assertEqual(outline2.sections[0].heading, "Intro")

    def test_claim_record(self):
        claim = ClaimRecord("C-001", "Factual text", "FACT", "Google Docs", 0.99, "2026-09-01")
        d = claim.to_dict()
        claim2 = ClaimRecord.from_dict(d)
        self.assertEqual(claim2.claim_id, "C-001")
        self.assertEqual(claim2.confidence, 0.99)
