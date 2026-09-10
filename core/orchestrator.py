"""Central orchestrator for coordinating editorial stages and artifacts."""

from typing import Dict, Any, Optional
from .config import EngineConfig
from .state import ProjectState
from .schemas import (
    Brief,
    ResearchResult,
    StrategyResult,
    OutlineResult,
    EvidenceLedger,
    DraftResult,
    FactCheckResult,
    EditorialAuditResult,
    InternalLinksResult,
    FinalPublishPackage,
)

class EditorialOrchestrator:
    """Orchestrates end-to-end execution of the blog editorial pipeline.
    
    Instead of brittle multi-agent sprawl, a single coordinator runs deterministic
    stages, each producing an inspectable JSON/Markdown artifact.
    """

    def __init__(self, state: ProjectState):
        self.state = state

    def run_pipeline(
        self,
        brief: Brief,
        research_pipeline,
        strategy_pipeline,
        outline_pipeline,
        evidence_pipeline,
        writer_pipeline,
        fact_checker_pipeline,
        editorial_pipeline,
        linking_pipeline,
    ) -> FinalPublishPackage:
        """Executes the complete end-to-end editorial pipeline."""
        
        # 1. Save Brief
        self.state.save_json("01_brief.json", brief.to_dict())

        # 2. Research & SERP Matrix
        research: ResearchResult = research_pipeline.run(brief)
        self.state.save_json("02_research.json", research.to_dict())

        # 3. Content Strategy & Entity Mapping
        strategy: StrategyResult = strategy_pipeline.run(brief, research)
        self.state.save_json("03_strategy.json", strategy.to_dict())

        # 4. Article Architecture (Outline)
        outline: OutlineResult = outline_pipeline.run(brief, research, strategy)
        self.state.save_json("04_outline.json", outline.to_dict())

        # 5. Evidence & Claims Ledger
        evidence: EvidenceLedger = evidence_pipeline.run(brief, outline)
        self.state.save_json("05_evidence.json", evidence.to_dict())

        # 6. Section-by-Section Writing
        draft: DraftResult = writer_pipeline.run(brief, outline, evidence)
        self.state.save_text("06_draft.md", draft.draft_markdown)

        # 7. Fact Check & Freshness Verification
        fact_check: FactCheckResult = fact_checker_pipeline.run(draft, evidence)
        self.state.save_json("07_fact_check.json", fact_check.to_dict())

        # 8. Editorial Review & Fluff Removal
        editorial: EditorialAuditResult = editorial_pipeline.run(draft, strategy)
        self.state.save_json("08_editorial_audit.json", editorial.to_dict())

        # 9. Internal Linking Graph
        links: InternalLinksResult = linking_pipeline.run(strategy)
        self.state.save_json("09_internal_links.json", links.to_dict())

        # 10. Assemble Final Publishing Package
        final_package = self._assemble_package(
            brief, strategy, outline, draft, editorial, links
        )
        self.state.save_text("10_final_package.md", self._format_package_markdown(final_package))
        self.state.save_json("10_final_package.json", final_package.to_dict())

        return final_package

    def _assemble_package(
        self,
        brief: Brief,
        strategy: StrategyResult,
        outline: OutlineResult,
        draft: DraftResult,
        editorial: EditorialAuditResult,
        links: InternalLinksResult,
    ) -> FinalPublishPackage:
        # Clean claim tags from draft text
        import re
        clean_text = re.sub(r"\[claim:C-\d{3,}\]", "", draft.draft_markdown)
        clean_text = re.sub(r"\n{3,}", "\n\n", clean_text).strip()

        words = len(clean_text.split())
        title = strategy.suggested_titles[0] if strategy.suggested_titles else outline.title
        slug = strategy.suggested_slug or brief.slug or "article"

        # Schema JSON-LD (FAQPage + Article)
        schema_json_ld = self._generate_schema(title, slug, brief.topic)

        # High-impact social hooks
        social_hooks = {
            "twitter": f"Stop making the #1 mistake with {brief.topic}.\n\nHere is how to calculate real profitability and avoid common traps:\n👉 https://blog.example.com/{slug}",
            "linkedin": f"Most advice on {brief.topic} recycles the same generic checklists.\n\nIn our latest teardown, we analyze the field math, real failure points, and what top operators do differently.\n\nLink in comments.",
        }

        # Key Takeaways
        key_takeaways = [
            f"Focus on practical margins and execution, not surface metrics in {brief.topic}.",
            "Traditional checklists ignore delivery constraints and hidden costs.",
            "Implement step-by-step verification before scaling investment.",
        ]

        # FAQ items
        faq = [
            {
                "question": f"Why does standard advice on {brief.topic} often fail?",
                "answer": f"Most public guides optimize for high-level vanity metrics rather than real contribution margin and unit economics."
            },
            {
                "question": f"How quickly can results be measured for {brief.topic}?",
                "answer": "Measurable signals usually appear within 7 to 14 days when accurate baseline tracking is implemented."
            }
        ]

        return FinalPublishPackage(
            title=title,
            title_variants=strategy.suggested_titles,
            slug=slug,
            meta_description=f"A complete, practical guide to {brief.topic}. Learn the real math, avoid critical failure modes, and apply battle-tested frameworks.",
            excerpt=f"Discover the field-tested strategies and mathematical realities behind {brief.topic}.",
            key_takeaways=key_takeaways,
            content_markdown=clean_text,
            faq=faq,
            schema_json_ld=schema_json_ld,
            social_posts=social_hooks,
            featured_image_prompt=f"Minimalist modern editorial illustration representing {brief.topic}, high contrast, tech editorial aesthetic, dark navy and vivid amber accents, 16:9 aspect ratio.",
            differentiation_score=editorial.differentiation_score,
            total_words=words,
        )

    def _generate_schema(self, title: str, slug: str, topic: str) -> str:
        import json
        schema = {
            "@context": "https://schema.org",
            "@graph": [
                {
                    "@type": "Article",
                    "headline": title,
                    "url": f"https://blog.example.com/{slug}",
                    "datePublished": "2026-09-10T12:00:00Z",
                    "about": topic
                },
                {
                    "@type": "FAQPage",
                    "mainEntity": [
                        {
                            "@type": "Question",
                            "name": f"What is the key factor in {topic}?",
                            "acceptedAnswer": {
                                "@type": "Answer",
                                "text": "Focusing on contribution margins and verified empirical data rather than vanity metrics."
                            }
                        }
                    ]
                }
            ]
        }
        return json.dumps(schema, indent=2)

    def _format_package_markdown(self, pkg: FinalPublishPackage) -> str:
        faq_text = "\n".join([f"### {item['question']}\n{item['answer']}\n" for item in pkg.faq])
        takeaways_text = "\n".join([f"- {t}" for t in pkg.key_takeaways])
        
        return f"""---
title: "{pkg.title}"
slug: "{pkg.slug}"
meta_description: "{pkg.meta_description}"
differentiation_score: {pkg.differentiation_score}
total_words: {pkg.total_words}
---

# {pkg.title}

> [!NOTE]
> **Key Takeaways**:
{takeaways_text}

{pkg.content_markdown}

## Frequently Asked Questions

{faq_text}

---

## Schema JSON-LD

```json
{pkg.schema_json_ld}
```
"""
