"""Configuration constants and path resolvers for i-have-blog."""

import os
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]

class EngineConfig:
    """Global engine configuration and threshold parameters."""
    
    # Paths
    PROJECTS_DIR = ROOT_DIR / "projects"
    KNOWLEDGE_DIR = ROOT_DIR / "knowledge"
    CONTENT_DIR = ROOT_DIR / "content"
    EVIDENCE_DIR = ROOT_DIR / "evidence"
    SKILLS_DIR = ROOT_DIR / "skills"
    EVALS_DIR = ROOT_DIR / "evals"
    
    # Quality & Editorial Thresholds
    MIN_DIFFERENTIATION_SCORE = 70.0
    MIN_FACT_CONFIDENCE = 0.85
    MAX_AI_CLICHE_TOLERANCE = 0
    TARGET_READING_LEVEL = "Clear, Direct, Analytical"
    
    # Freshness Policies (in months)
    FRESHNESS_SOFTWARE_MONTHS = 4
    FRESHNESS_STATS_MONTHS = 12
    FRESHNESS_POLICIES_MONTHS = 6
    FRESHNESS_EVERGREEN_MONTHS = 60
    
    # Banned Clichés and Fluff Patterns
    BANNED_INTRO_PATTERNS = [
        r"(?i)in today's (fast-paced|rapidly changing|digital|modern) world",
        r"(?i)in recent years,?\s+(we have seen|there has been)",
        r"(?i)whether you('re| are) a beginner or (an? )?(expert|seasoned)",
        r"(?i)it('s| is) important to (note|remember|keep in mind) that",
        r"(?i)have you ever wondered (how|why|what)",
        r"(?i)as technology continues to evolve",
        r"(?i)look no further",
    ]
    
    BANNED_TRANSITION_PATTERNS = [
        r"(?i)moreover,?\s+it is worth noting",
        r"(?i)furthermore,?\s+one must consider",
        r"(?i)delving (deeper|into)",
        r"(?i)in a nutshell",
        r"(?i)at the end of the day",
        r"(?i)it goes without saying",
    ]
    
    BANNED_CONCLUSION_PATTERNS = [
        r"(?i)in conclusion,?\s+only time will tell",
        r"(?i)ultimately,?\s+the choice is yours",
        r"(?i)hope this (helps|article was useful)",
    ]
