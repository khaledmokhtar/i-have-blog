"""Strategy Pipeline: Entities, Topic Clusters, Differentiation Angle, and Titles."""

import re
from typing import List
from core.schemas import Brief, ResearchResult, StrategyResult

class StrategyPipeline:
    """Defines the unique angle, semantic entity footprint, and positioning."""

    def run(self, brief: Brief, research: ResearchResult) -> StrategyResult:
        entities = self._extract_semantic_entities(brief.topic, brief.primary_keyword)
        secondary_kws = self._derive_secondary_keywords(brief.primary_keyword, entities)
        slug = self._generate_slug(brief.primary_keyword or brief.topic)
        titles = self._generate_title_variants(brief.topic, brief.primary_keyword)
        angle = (
            f"Tear down the industry consensus around {brief.topic}. "
            "Expose the hidden operational and financial trade-offs, and provide the exact mathematical "
            "decision framework used by senior operators."
        )

        return StrategyResult(
            primary_keyword=brief.primary_keyword,
            secondary_keywords=secondary_kws,
            semantic_entities=entities,
            competitive_angle=angle,
            target_differentiation_score=85.0,
            suggested_slug=slug,
            suggested_titles=titles,
            proprietary_frameworks_used=[
                "Contribution Margin Matrix",
                "Unit Economic Realism Check",
                "Failure Mode Diagnostic"
            ],
        )

    def _extract_semantic_entities(self, topic: str, kw: str) -> List[str]:
        # High-authority semantic entities
        base_entities = [
            "Unit Economics",
            "Contribution Margin",
            "Baseline Attribution",
            "Signal Quality",
            "Operational Friction",
            "Risk-Adjusted ROI",
        ]
        topic_words = [w.capitalize() for w in re.findall(r"\b\w{4,}\b", f"{topic} {kw}")]
        return list(dict.fromkeys(topic_words[:4] + base_entities))

    def _derive_secondary_keywords(self, primary: str, entities: List[str]) -> List[str]:
        return [
            f"{primary} strategy",
            f"{primary} mistakes",
            f"{primary} benchmarks",
            f"how to calculate {primary}",
            f"{primary} vs alternatives",
        ]

    def _generate_slug(self, text: str) -> str:
        clean = re.sub(r"[^a-zA-Z0-9\s-]", "", text).lower().strip()
        return re.sub(r"[\s-]+", "-", clean)

    def _generate_title_variants(self, topic: str, primary: str) -> List[str]:
        return [
            f"{primary.title()}: The Field Guide Senior Operators Actually Use",
            f"Why Most Advice on {topic.title()} Fails (And The Math That Works)",
            f"{primary.title()}: Stop Optimizing For Vanity Metrics",
        ]
