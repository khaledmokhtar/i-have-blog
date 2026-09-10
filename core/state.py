"""State management and file artifact persistence for individual projects."""

import json
from pathlib import Path
from typing import Any, Dict, Optional
from .config import EngineConfig

class ProjectState:
    """Manages inspectable stage artifacts stored under projects/<slug>/."""

    def __init__(self, slug: str, base_dir: Optional[Path] = None):
        self.slug = slug
        self.dir = (base_dir or EngineConfig.PROJECTS_DIR) / slug
        self.dir.mkdir(parents=True, exist_ok=True)

    def artifact_path(self, filename: str) -> Path:
        return self.dir / filename

    def save_json(self, filename: str, data: Dict[str, Any]) -> Path:
        path = self.artifact_path(filename)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return path

    def load_json(self, filename: str) -> Optional[Dict[str, Any]]:
        path = self.artifact_path(filename)
        if not path.exists():
            return None
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_text(self, filename: str, content: str) -> Path:
        path = self.artifact_path(filename)
        path.write_text(content, encoding="utf-8")
        return path

    def load_text(self, filename: str) -> Optional[str]:
        path = self.artifact_path(filename)
        if not path.exists():
            return None
        return path.read_text(encoding="utf-8")

    def exists(self, filename: str) -> bool:
        return self.artifact_path(filename).exists()
