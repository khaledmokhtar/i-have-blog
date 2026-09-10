"""Tests for full orchestrator integration."""

import unittest
import tempfile
import shutil
from pathlib import Path
from core.schemas import Brief, EvidenceLedger, ClaimRecord
from core.state import ProjectState
from core.orchestrator import EditorialOrchestrator
from pipelines.research import ResearchPipeline
from pipelines.strategy import StrategyPipeline
from pipelines.outline import OutlinePipeline
from pipelines.writer import WriterPipeline
from pipelines.fact_checker import FactCheckerPipeline
from pipelines.editorial_pass import EditorialPassPipeline
from pipelines.internal_links import InternalLinksPipeline

class MockEvidencePipeline:
    def run(self, brief, outline):
        return EvidenceLedger(claims=[
            ClaimRecord("C-001", "Operational claim", "EXPERT_INTERPRETATION", "Review", 0.95, "2026-09-01"),
            ClaimRecord("C-002", "Mechanical claim", "FACT", "Docs", 0.98, "2026-09-01"),
            ClaimRecord("C-003", "Formula claim", "CALCULATION", "Accounting", 1.0, "2026-09-01"),
            ClaimRecord("C-004", "Attribution stat", "STATISTIC", "Benchmark", 0.92, "2026-09-01"),
        ])

class TestOrchestrator(unittest.TestCase):
    def setUp(self):
        self.temp_dir = Path(tempfile.mkdtemp())
        self.state = ProjectState("test-post", base_dir=self.temp_dir)
        self.orchestrator = EditorialOrchestrator(self.state)

    def tearDown(self):
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_pipeline_execution(self):
        brief = Brief(
            topic="Facebook Ads ROAS",
            primary_keyword="facebook ads roas",
            audience="E-Commerce Operators",
            slug="test-post"
        )

        package = self.orchestrator.run_pipeline(
            brief=brief,
            research_pipeline=ResearchPipeline(),
            strategy_pipeline=StrategyPipeline(),
            outline_pipeline=OutlinePipeline(),
            evidence_pipeline=MockEvidencePipeline(),
            writer_pipeline=WriterPipeline(),
            fact_checker_pipeline=FactCheckerPipeline(),
            editorial_pipeline=EditorialPassPipeline(),
            linking_pipeline=InternalLinksPipeline(),
        )

        self.assertIsNotNone(package.title)
        self.assertGreater(package.total_words, 200)
        self.assertGreaterEqual(package.differentiation_score, 70.0)

        # Verify artifacts exist on disk
        self.assertTrue(self.state.exists("01_brief.json"))
        self.assertTrue(self.state.exists("02_research.json"))
        self.assertTrue(self.state.exists("03_strategy.json"))
        self.assertTrue(self.state.exists("04_outline.json"))
        self.assertTrue(self.state.exists("05_evidence.json"))
        self.assertTrue(self.state.exists("06_draft.md"))
        self.assertTrue(self.state.exists("07_fact_check.json"))
        self.assertTrue(self.state.exists("08_editorial_audit.json"))
        self.assertTrue(self.state.exists("09_internal_links.json"))
        self.assertTrue(self.state.exists("10_final_package.md"))
