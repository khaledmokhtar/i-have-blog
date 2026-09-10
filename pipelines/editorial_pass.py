"""Editorial Pass Pipeline: Cliché removal, punchiness audit, and Differentiation Scoring."""

import re
from typing import List, Tuple
from core.schemas import DraftResult, StrategyResult, EditorialAuditResult
from core.config import EngineConfig

class EditorialPassPipeline:
    """Performs rigorous editorial surgery: deletes AI throat-clearing, calculates differentiation."""

    def run(self, draft: DraftResult, strategy: StrategyResult) -> EditorialAuditResult:
        text = draft.draft_markdown
        orig_words = len(text.split())

        # 1. Detect and remove banned clichés
        cleaned_text, banned_found, removed_count = self._scrub_banned_phrases(text)

        # 2. Calculate punchiness score
        punchiness = self._calculate_punchiness(cleaned_text)

        # 3. Calculate Differentiation Score
        diff_score = self._calculate_differentiation(cleaned_text, strategy)

        clean_words = len(cleaned_text.split())
        ratio = round(clean_words / max(orig_words, 1), 3)

        recommendations = []
        if diff_score < EngineConfig.MIN_DIFFERENTIATION_SCORE:
            recommendations.append(
                f"Differentiation Score ({diff_score:.1f}) is below minimum {EngineConfig.MIN_DIFFERENTIATION_SCORE}. "
                "Inject more proprietary publisher data and practical failure examples."
            )
        else:
            recommendations.append(f"Excellent differentiation ({diff_score:.1f}/100). Content is distinctive and authority-driven.")

        return EditorialAuditResult(
            banned_phrases_found=banned_found,
            clichés_removed=removed_count,
            differentiation_score=diff_score,
            punchiness_score=punchiness,
            original_word_count=orig_words,
            clean_word_count=clean_words,
            compression_ratio=ratio,
            recommendations=recommendations,
        )

    def _scrub_banned_phrases(self, text: str) -> Tuple[str, List[str], int]:
        all_patterns = (
            EngineConfig.BANNED_INTRO_PATTERNS
            + EngineConfig.BANNED_TRANSITION_PATTERNS
            + EngineConfig.BANNED_CONCLUSION_PATTERNS
        )
        found = []
        count = 0
        cleaned = text

        for pattern in all_patterns:
            matches = re.findall(pattern, cleaned)
            if matches:
                found.append(pattern)
                count += len(matches)
                cleaned = re.sub(pattern, "", cleaned)

        # Clean multiple whitespace or empty lines
        cleaned = re.sub(r" +", " ", cleaned)
        cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
        return cleaned, found, count

    def _calculate_punchiness(self, text: str) -> float:
        """Measures sentence length variety and direct sentence structure."""
        sentences = [s.strip() for s in re.split(r"[.!?]+", text) if len(s.strip().split()) > 2]
        if not sentences:
            return 80.0
        
        lengths = [len(s.split()) for s in sentences]
        avg_len = sum(lengths) / len(lengths)
        
        # Optimal average length for high-authority reading: 12-18 words
        score = 100.0 - abs(avg_len - 15.0) * 2.5
        return max(50.0, min(100.0, round(score, 1)))

    def _calculate_differentiation(self, text: str, strategy: StrategyResult) -> float:
        """Scores uniqueness vs generic top-10 search results.
        
        Evaluates presence of:
        - Math formulas and LaTeX ($$)
        - Concrete tables and tabular data
        - Specific numbers, percentages, and dollar amounts
        - Proprietary framework mentions
        """
        score = 50.0  # Baseline
        
        if "$$" in text or "\\text{" in text:
            score += 15.0  # Formula presence
        if "| --- |" in text:
            score += 12.0  # Structured comparison matrix
        
        # Check for numbers / percentages
        numbers_count = len(re.findall(r"\b\d+(\.\d+)?%?|\$\d+", text))
        if numbers_count >= 10:
            score += 12.0
        elif numbers_count >= 5:
            score += 6.0

        # Check for frameworks
        for fw in strategy.proprietary_frameworks_used:
            if fw.lower() in text.lower():
                score += 4.0

        return max(0.0, min(100.0, round(score, 1)))
