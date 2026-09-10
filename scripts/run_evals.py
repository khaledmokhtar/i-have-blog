"""Evaluation runner script for testing cases in evals/cases.jsonl."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from core.schemas import Brief
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
        from core.schemas import EvidenceLedger, ClaimRecord
        return EvidenceLedger(claims=[
            ClaimRecord("C-001", "Operational claim", "EXPERT_INTERPRETATION", "Internal Audit", 0.95, "2026-09-01"),
            ClaimRecord("C-002", "Mechanical claim", "FACT", "Documentation", 0.98, "2026-09-01"),
            ClaimRecord("C-003", "Mathematical formula", "CALCULATION", "Accounting standard", 1.0, "2026-09-01"),
            ClaimRecord("C-004", "Attribution drift stat", "STATISTIC", "Benchmark", 0.92, "2026-09-01"),
        ])

def run_evals():
    cases_file = ROOT / "evals" / "cases.jsonl"
    if not cases_file.exists():
        print(f"Error: {cases_file} not found")
        return

    raw_text = cases_file.read_text(encoding="utf-8-sig").strip()
    cases = [json.loads(line) for line in raw_text.split("\n") if line.strip()]
    print(f"Loaded {len(cases)} evaluation test cases.\n")

    passed_count = 0
    for idx, case in enumerate(cases, 1):
        slug = f"eval_{case['id']}"
        state = ProjectState(slug, base_dir=ROOT / "evals" / "runs")
        orchestrator = EditorialOrchestrator(state)
        brief = Brief(
            topic=case["topic"],
            primary_keyword=case["primary_keyword"],
            audience=case["audience"],
            slug=slug,
        )

        package = orchestrator.run_pipeline(
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

        diff = package.differentiation_score
        status = "PASS" if diff >= 70.0 else "FAIL"
        if status == "PASS":
            passed_count += 1

        print(f"[{idx:02d}/{len(cases):02d}] {case['topic']:<45} | Words: {package.total_words:<5} | Diff Score: {diff:<5} | {status}")

    print(f"\nEvaluation Complete: {passed_count}/{len(cases)} cases met quality threshold (Score >= 70).")

if __name__ == "__main__":
    run_evals()
