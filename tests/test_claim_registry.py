"""Tests for ClaimRegistry tagging, classification, and stripping."""

import unittest
from core.claim_registry import ClaimRegistry

class TestClaimRegistry(unittest.TestCase):
    def setUp(self):
        self.registry = ClaimRegistry()

    def test_register_and_extract(self):
        c1 = self.registry.register_claim("GA4 is event-based", "FACT", "Google Documentation", 0.98)
        self.assertEqual(c1.claim_id, "C-001")

        text = f"Here is a claim [claim:{c1.claim_id}] in text."
        extracted = self.registry.extract_claim_ids(text)
        self.assertEqual(extracted, ["C-001"])

        clean = self.registry.strip_claim_tags(text)
        self.assertNotIn("[claim:C-001]", clean)
        self.assertIn("Here is a claim in text.", clean)

    def test_multiple_claims(self):
        c1 = self.registry.register_claim("Claim 1", "STATISTIC", "Source 1")
        c2 = self.registry.register_claim("Claim 2", "CALCULATION", "Source 2")
        self.assertEqual(c1.claim_id, "C-001")
        self.assertEqual(c2.claim_id, "C-002")
