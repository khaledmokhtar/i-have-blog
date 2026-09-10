# Practical AI Systems & Agent Architecture

## Avoiding Multi-Agent Sprawl
- Disconnected multi-agent loops create compounding hallucination and 5x token overhead.
- Prefer a Single Deterministic Orchestrator with Modular Pipeline Stages.
- Every stage must output an inspectable JSON/Markdown artifact.
- Use Claim Registries with explicit IDs to ground generation in verified facts.
