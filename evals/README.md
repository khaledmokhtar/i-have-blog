# Evaluation Framework Guide

This directory contains the automated and blind evaluation suite for `i-have-blog`.

## Files
- `cases.jsonl`: 10 standardized test prompts spanning commercial, technical, and operational topics.
- `rubric.md`: The single-source judging rubric with weighted dimensions and blocker criteria.
- `RESULTS.md`: Empirical comparison table between baseline generic LLMs and `i-have-blog`.

## Running the Benchmark
```bash
# Run evaluations across test cases
python scripts/run_evals.py

# Run blind LLM Judge
python scripts/judge.py
```
