# Agent Guide for `i-have-blog`

This guide explains how autonomous AI agents, coding assistants, and human contributors should navigate, modify, and extend the **`i-have-blog`** repository.

---

## 1. Ground Rules & Source of Truth

- **The Single Source of Truth**: All editorial rules, prompt instructions, and priority hierarchies originate in `skills/blog-writer/SKILL.md`.
- **Never modify mirrors directly**: The copy at `.cursor/skills/blog-writer/SKILL.md` is a mirror. When updating rules, edit `skills/blog-writer/SKILL.md` first, then run `python scripts/sync_skills.py`.
- **Deterministic Pipeline vs. Agent Sprawl**: Do not introduce independent conversational agents that chat with one another without state persistence. All transitions between stages MUST be mediated by the `EditorialOrchestrator` through inspectable JSON/Markdown artifacts.
- **Claim Registry Requirement**: Any new generative pipeline logic must tag factual or quantitative claims with `[claim:C-xxx]` and resolve them against `EvidenceLedger`.

---

## 2. Repository Map

| Directory / File | Purpose | Rule for Agents |
| :--- | :--- | :--- |
| `skills/blog-writer/SKILL.md` | Canonical editorial rulebook and LLM behavior specification. | Source of truth. Edit here first. |
| `.cursor/skills/blog-writer/` | Cursor IDE skill mirror. | Keep synchronized via script. |
| `.claude-plugin/`, `.codex-plugin/` | Manifests for Claude Code and Codex environments. | Keep version and description synchronized. |
| `gemini-extension.json`, `GEMINI.md` | Gemini CLI integration manifest and context prompt. | Follow Gemini prompt guidelines. |
| `core/` | Central orchestrator, state manager, claim registry, and schemas. | Strictly typed dataclasses. |
| `pipelines/` | The 8 modular stages (Research, Strategy, Outline, Writer, Fact-Checker, Editorial Pass, Internal Links, Refresh). | Each stage must accept schemas and return a typed result. |
| `knowledge/` | Proprietary publisher knowledge base (brand, audience, frameworks, case studies). | Query before drafting to ensure high differentiation. |
| `evidence/` | Persistent claim storage and freshness evaluation. | Enforce freshness intervals. |
| `evals/` | Benchmark cases (`cases.jsonl`), blind rubric (`rubric.md`), and results. | Run evals after any prompt modification. |
| `scripts/` | Tooling for running benchmarks, blind judging, syncing skills, and validating artifacts. | Keep zero external dependencies (Python stdlib). |
| `tests/` | Comprehensive unit tests for orchestrator, claim registry, clichés, and decay logic. | All tests must pass before submitting PRs. |

---

## 3. Standard Verification Commands

Before opening a pull request or concluding a task, run:

```bash
# 1. Run unit test suite
python -m unittest discover -s tests -v

# 2. Validate schema compatibility
python scripts/validate_artifacts.py

# 3. Synchronize skill mirrors
python scripts/sync_skills.py

# 4. Verify benchmark test cases
python scripts/run_evals.py
```
