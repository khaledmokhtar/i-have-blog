"""Loader for proprietary brand guidelines, expertise, and frameworks."""

import json
from pathlib import Path
from typing import Dict, Any, List

class KnowledgeLoader:
    """Loads publisher memory and proprietary frameworks to fuel the Originality Engine."""

    def __init__(self, knowledge_dir: Path):
        self.dir = knowledge_dir

    def load_brand_voice(self) -> Dict[str, Any]:
        p = self.dir / "brand.json"
        if p.exists():
            return json.loads(p.read_text(encoding="utf-8"))
        return {}

    def load_audience(self) -> Dict[str, Any]:
        p = self.dir / "audience.json"
        if p.exists():
            return json.loads(p.read_text(encoding="utf-8"))
        return {}

    def load_expertise_docs(self) -> List[Dict[str, str]]:
        docs = []
        exp_dir = self.dir / "expertise"
        if exp_dir.exists():
            for f in exp_dir.glob("*.md"):
                docs.append({"name": f.stem, "content": f.read_text(encoding="utf-8")})
        return docs
