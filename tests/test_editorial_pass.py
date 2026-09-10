"""Tests for Editorial Pass cliché removal, punchiness, and differentiation scoring."""

import unittest
from pipelines.editorial_pass import EditorialPassPipeline
from core.schemas import DraftResult, StrategyResult

class TestEditorialPass(unittest.TestCase):
    def setUp(self):
        self.pipeline = EditorialPassPipeline()
        self.strategy = StrategyResult(
            primary_keyword="test",
            proprietary_frameworks_used=["Contribution Margin Matrix"]
        )

    def test_scrub_banned_phrases(self):
        dirty_text = "In today's digital world, whether you're a beginner or an expert, it is important to remember that profit matters."
        clean_text, found, count = self.pipeline._scrub_banned_phrases(dirty_text)
        self.assertTrue(len(found) >= 2)
        self.assertNotIn("In today's digital world", clean_text)
        self.assertNotIn("whether you're a beginner", clean_text)

    def test_differentiation_scoring(self):
        rich_text = """
        Let us look at the formula:
        $$\\text{Contribution Margin} = \\text{Revenue} - \\text{Costs}$$
        
        | Dimension | Baseline | Field Reality |
        | :--- | :--- | :--- |
        | Margin | 15% | 35% |
        
        Testing with $15,000 budget and 28% delivery rate across 450 transactions.
        Applying our Contribution Margin Matrix.
        """
        draft = DraftResult(draft_markdown=rich_text, word_count=50)
        audit = self.pipeline.run(draft, self.strategy)
        self.assertGreaterEqual(audit.differentiation_score, 75.0)
