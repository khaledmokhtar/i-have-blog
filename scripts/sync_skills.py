"""Synchronizes the canonical SKILL.md to platform-specific mirror directories."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def sync_skills():
    canonical = ROOT / "skills" / "blog-writer" / "SKILL.md"
    if not canonical.exists():
        print("Error: Canonical SKILL.md missing!")
        return

    cursor_mirror = ROOT / ".cursor" / "skills" / "blog-writer" / "SKILL.md"
    cursor_mirror.parent.mkdir(parents=True, exist_ok=True)
    cursor_mirror.write_text(canonical.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"Synchronized canonical SKILL.md -> {cursor_mirror}")

if __name__ == "__main__":
    sync_skills()
