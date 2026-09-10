"""Tests for Content Decay calculation and action logic."""

import unittest
from pipelines.refresh import RefreshPipeline

class TestDecayScore(unittest.TestCase):
    def setUp(self):
        self.pipeline = RefreshPipeline()

    def test_fresh_article_keeps(self):
        res = self.pipeline.run(
            target="my-evergreen-post",
            age_months=2,
            traffic_loss_pct=0.0,
            serp_drift_score=10.0,
            outdated_claims_count=0
        )
        self.assertEqual(res.action, "KEEP")
        self.assertLess(res.decay_score, 25.0)

    def test_decayed_article_triggers_rewrite(self):
        res = self.pipeline.run(
            target="outdated-2022-post",
            age_months=36,
            traffic_loss_pct=65.0,
            serp_drift_score=85.0,
            outdated_claims_count=7
        )
        self.assertEqual(res.action, "EXPAND_AND_REWRITE")
        self.assertGreaterEqual(res.decay_score, 75.0)
