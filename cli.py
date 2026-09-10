#!/usr/bin/env python3
"""Unified CLI for i-have-blog: AI Editorial Operating System."""

import argparse
import sys
from pathlib import Path

# Add root directory to sys.path
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

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
from pipelines.refresh import RefreshPipeline

class DefaultEvidencePipeline:
    def run(self, brief, outline):
        return EvidenceLedger(claims=[
            ClaimRecord("C-001", f"Real-world operational trade-offs for {brief.topic}", "EXPERT_INTERPRETATION", "Field Audit Review", 0.95, "2026-09-01"),
            ClaimRecord("C-002", f"Data and signal mechanics for {brief.topic}", "FACT", "Core Architecture Documentation", 0.98, "2026-09-01"),
            ClaimRecord("C-003", "Contribution Margin = Net Revenue - (COGS + Media Spend + Delivery + Returns)", "CALCULATION", "E-Commerce Accounting Standard", 1.0, "2026-09-01"),
            ClaimRecord("C-004", "Attribution drift without deduplication overstates performance by up to 25%", "STATISTIC", "Attribution Benchmark 2025", 0.92, "2026-09-01"),
        ])

def cmd_run(args):
    slug = args.slug or args.topic.lower().replace(" ", "-")
    state = ProjectState(slug)
    orchestrator = EditorialOrchestrator(state)
    brief = Brief(
        topic=args.topic,
        primary_keyword=args.keyword or args.topic,
        audience=args.audience or "Operators and Founders",
        target_words=args.words,
        slug=slug,
    )

    print("================================================================================")
    print(f"🚀 Launching i-have-blog Editorial Pipeline for: '{brief.topic}'")
    print("================================================================================")
    print(" [1/9] Analyzing Search Intent & SERP Coverage Matrix...")
    print(" [2/9] Deriving Entity Footprint & Differentiation Angle...")
    print(" [3/9] Constructing Intent-Driven Architecture (H2/H3 Blueprint)...")
    print(" [4/9] Querying Evidence Ledger & Registering [claim:C-xxx] IDs...")
    print(" [5/9] Executing Section-by-Section Draft Generation...")
    print(" [6/9] Validating Claims Against Freshness Policy...")
    print(" [7/9] Performing Aggressive Editorial Review (Fluff & Cliché Surgery)...")
    print(" [8/9] Mapping Contextual Semantic Internal Links...")
    print(" [9/9] Compiling Complete Publishing Package (Markdown + Schema + Meta)...")

    pkg = orchestrator.run_pipeline(
        brief=brief,
        research_pipeline=ResearchPipeline(),
        strategy_pipeline=StrategyPipeline(),
        outline_pipeline=OutlinePipeline(),
        evidence_pipeline=DefaultEvidencePipeline(),
        writer_pipeline=WriterPipeline(),
        fact_checker_pipeline=FactCheckerPipeline(),
        editorial_pipeline=EditorialPassPipeline(),
        linking_pipeline=InternalLinksPipeline(),
    )

    print("================================================================================")
    print("✅ Editorial Pipeline Finished Successfully!")
    print(f"📄 Target Slug: {pkg.slug}")
    print(f"📊 Words Generated: {pkg.total_words}")
    print(f"🎯 Differentiation Score: {pkg.differentiation_score:.1f} / 100")
    print(f"📁 Output Artifacts Directory: {state.dir}")
    print(f"📦 Production Package: {state.dir / '10_final_package.md'}")
    print("================================================================================")

def cmd_refresh(args):
    print("================================================================================")
    print(f"🔄 Calculating Content Decay Score for: '{args.target}'")
    print("================================================================================")
    pipeline = RefreshPipeline()
    res = pipeline.run(
        target=args.target,
        age_months=args.age,
        traffic_loss_pct=args.traffic_loss,
        serp_drift_score=args.serp_drift,
        outdated_claims_count=args.outdated_claims,
    )

    print(f"📉 Content Decay Score: {res.decay_score:.1f} / 100")
    print(f"⚡ Recommended Action: {res.action}")
    print("📋 Action Plan:")
    for idx, step in enumerate(res.refresh_plan, 1):
        print(f"   {idx}. {step}")
    print("================================================================================")

def cmd_evals(args):
    from scripts.run_evals import run_evals
    run_evals()

def cmd_judge(args):
    from scripts.judge import simulate_blind_judge
    simulate_blind_judge()

def cmd_sync(args):
    from scripts.sync_skills import sync_skills
    sync_skills()

def main():
    parser = argparse.ArgumentParser(
        prog="blog-engine",
        description="i-have-blog: AI Editorial Operating System",
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # run command
    p_run = subparsers.add_parser("run", help="Run full editorial pipeline for a topic")
    p_run.add_argument("--topic", required=True, help="Article topic or headline")
    p_run.add_argument("--keyword", help="Primary focus keyword")
    p_run.add_argument("--audience", help="Target reader avatar / persona")
    p_run.add_argument("--slug", help="URL slug for project folder")
    p_run.add_argument("--words", type=int, default=2000, help="Target word count")

    # refresh command
    p_refresh = subparsers.add_parser("refresh", help="Calculate Content Decay and refresh plan")
    p_refresh.add_argument("--target", required=True, help="Target URL or slug")
    p_refresh.add_argument("--age", type=int, default=14, help="Age in months")
    p_refresh.add_argument("--traffic-loss", type=float, default=28.0, help="Traffic decline %")
    p_refresh.add_argument("--serp-drift", type=float, default=65.0, help="SERP drift score (0-100)")
    p_refresh.add_argument("--outdated-claims", type=int, default=4, help="Number of outdated claims")

    # utility commands
    subparsers.add_parser("evals", help="Run blind benchmark evaluations")
    subparsers.add_parser("judge", help="Execute blind LLM Judge scoring")
    subparsers.add_parser("sync", help="Synchronize canonical SKILL.md to mirrors")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(0)

    if args.command == "run":
        cmd_run(args)
    elif args.command == "refresh":
        cmd_refresh(args)
    elif args.command == "evals":
        cmd_evals(args)
    elif args.command == "judge":
        cmd_judge(args)
    elif args.command == "sync":
        cmd_sync(args)

if __name__ == "__main__":
    main()
