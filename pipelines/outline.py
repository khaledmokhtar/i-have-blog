"""Outline Pipeline: Intent-driven architectural blueprint generator."""

from typing import List
from core.schemas import Brief, ResearchResult, StrategyResult, OutlineResult, OutlineSection

class OutlinePipeline:
    """Builds a section-by-section architectural outline mapped to search intent."""

    def run(self, brief: Brief, research: ResearchResult, strategy: StrategyResult) -> OutlineResult:
        h1 = strategy.suggested_titles[0] if strategy.suggested_titles else f"The Definitive Field Guide to {brief.topic}"
        sections = [
            OutlineSection(
                heading=f"The Consensus Trap: What Everyone Gets Wrong About {brief.topic}",
                level=2,
                section_goal="Dismantle generic surface advice and reframe the conversation around unit economics.",
                gap_addressed="Replaces clichéd introductions with contrarian field observations.",
                key_points=[
                    "Why conventional checklists fail in messy real-world scenarios",
                    "The difference between perceived efficiency and contribution margin",
                ],
                evidence_needed=["Field benchmark data", "Calculation methodology"],
                estimated_words=400,
            ),
            OutlineSection(
                heading="The Core Mechanism: How It Actually Works Under The Hood",
                level=2,
                section_goal="Explain the technical or systemic engine clearly without fluff.",
                gap_addressed="Provides deep mechanical clarity rather than superficial marketing bullet points.",
                key_points=[
                    "Signal propagation and data pipeline dynamics",
                    "The feedback loop that determines compounding success",
                ],
                evidence_needed=["Official documentation standards"],
                estimated_words=450,
            ),
            OutlineSection(
                heading="The Real Math: A Concrete Calculation Framework",
                level=2,
                section_goal="Provide exact formulas, numbers, and worked examples.",
                gap_addressed="Fills the widespread lack of quantitative models on Google SERP.",
                key_points=[
                    "The Contribution Margin formula",
                    "Sensitivity analysis: what happens when costs swing by 15%",
                ],
                evidence_needed=["Mathematical proof and worked table"],
                estimated_words=450,
            ),
            OutlineSection(
                heading="3 Costly Failure Modes (And How Senior Teams Prevent Them)",
                level=2,
                section_goal="Walk through realistic failure points and troubleshooting protocols.",
                gap_addressed="Competitors only share rosy success stories; we detail failure engineering.",
                key_points=[
                    "Failure Mode 1: Premature scaling before signal validation",
                    "Failure Mode 2: Ignoring downstream friction",
                    "Failure Mode 3: Disconnected attribution",
                ],
                evidence_needed=["Case study observations"],
                estimated_words=450,
            ),
            OutlineSection(
                heading="The Execution Checklist: Step-by-Step Implementation",
                level=2,
                section_goal="Deliver a sequenced, unambiguous action protocol.",
                gap_addressed="Gives reader immediately actionable steps with time estimates.",
                key_points=[
                    "Phase 1: Baseline Audit (Day 1–3)",
                    "Phase 2: Pilot Deployment (Day 4–10)",
                    "Phase 3: Verification & Scale (Day 11+)",
                ],
                evidence_needed=["Operational milestones"],
                estimated_words=400,
            ),
        ]

        total_words = sum(s.estimated_words for s in sections)
        return OutlineResult(
            title=h1,
            h1=h1,
            sections=sections,
            total_estimated_words=total_words,
        )
