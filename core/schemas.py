"""Data schemas for all stage artifacts in the editorial pipeline."""

from dataclasses import dataclass, field, asdict
from typing import List, Dict, Any, Optional
import json

@dataclass
class Brief:
    topic: str
    primary_keyword: str
    audience: str
    publisher_notes: str = ""
    target_words: int = 2000
    brand_voice: str = "Analytical, direct, practical, contrarian"
    slug: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Brief":
        return cls(**data)

@dataclass
class ResearchResult:
    topic: str
    primary_keyword: str
    search_intent: str
    intent_category: str  # Informational, Commercial Investigation, Transactional, Navigational
    dominant_serp_patterns: List[str] = field(default_factory=list)
    competitor_matrix: List[Dict[str, Any]] = field(default_factory=list)
    information_gaps: List[str] = field(default_factory=list)
    unaddressed_questions: List[str] = field(default_factory=list)
    opportunity_summary: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ResearchResult":
        return cls(**data)

@dataclass
class StrategyResult:
    primary_keyword: str
    secondary_keywords: List[str] = field(default_factory=list)
    semantic_entities: List[str] = field(default_factory=list)
    competitive_angle: str = ""
    target_differentiation_score: float = 75.0
    suggested_slug: str = ""
    suggested_titles: List[str] = field(default_factory=list)
    proprietary_frameworks_used: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "StrategyResult":
        return cls(**data)

@dataclass
class OutlineSection:
    heading: str
    level: int  # 2 for H2, 3 for H3
    section_goal: str
    gap_addressed: str
    key_points: List[str] = field(default_factory=list)
    evidence_needed: List[str] = field(default_factory=list)
    estimated_words: int = 350

@dataclass
class OutlineResult:
    title: str
    h1: str
    sections: List[OutlineSection] = field(default_factory=list)
    total_estimated_words: int = 2000

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        return d

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "OutlineResult":
        sections = [OutlineSection(**s) for s in data.get("sections", [])]
        return cls(
            title=data.get("title", ""),
            h1=data.get("h1", ""),
            sections=sections,
            total_estimated_words=data.get("total_estimated_words", 2000),
        )

@dataclass
class ClaimRecord:
    claim_id: str
    text: str
    claim_type: str  # FACT, STATISTIC, TIME_SENSITIVE, EXPERT_INTERPRETATION, OPINION, CALCULATION
    source: str
    confidence: float
    verified_at: str
    status: str = "VERIFIED"  # UNVERIFIED, VERIFIED, MODIFIED, REJECTED
    note: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ClaimRecord":
        return cls(**data)

@dataclass
class EvidenceLedger:
    claims: List[ClaimRecord] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {"claims": [c.to_dict() for c in self.claims]}

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "EvidenceLedger":
        claims = [ClaimRecord.from_dict(c) for c in data.get("claims", [])]
        return cls(claims=claims)

@dataclass
class DraftResult:
    draft_markdown: str
    claims_tagged: List[str] = field(default_factory=list)
    word_count: int = 0
    section_count: int = 0

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DraftResult":
        return cls(**data)

@dataclass
class FactCheckResult:
    verified_count: int
    modified_count: int
    rejected_count: int
    claims_audit: List[Dict[str, Any]] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    passed: bool = True

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "FactCheckResult":
        return cls(**data)

@dataclass
class EditorialAuditResult:
    banned_phrases_found: List[str] = field(default_factory=list)
    clichés_removed: int = 0
    differentiation_score: float = 0.0
    punchiness_score: float = 0.0
    original_word_count: int = 0
    clean_word_count: int = 0
    compression_ratio: float = 1.0
    recommendations: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "EditorialAuditResult":
        return cls(**data)

@dataclass
class InternalLinksResult:
    suggested_links: List[Dict[str, str]] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "InternalLinksResult":
        return cls(**data)

@dataclass
class FinalPublishPackage:
    title: str
    title_variants: List[str]
    slug: str
    meta_description: str
    excerpt: str
    key_takeaways: List[str]
    content_markdown: str
    faq: List[Dict[str, str]]
    schema_json_ld: str
    social_posts: Dict[str, str]
    featured_image_prompt: str
    differentiation_score: float
    total_words: int

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "FinalPublishPackage":
        return cls(**data)

@dataclass
class ContentDecayResult:
    target: str
    age_months: int
    traffic_loss_pct: float
    serp_drift_score: float
    outdated_claims_count: int
    decay_score: float
    action: str  # KEEP, UPDATE, EXPAND, REMOVE, MERGE, REDIRECT
    refresh_plan: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ContentDecayResult":
        return cls(**data)
