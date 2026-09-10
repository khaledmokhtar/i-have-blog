# Evaluation & Benchmark Guide

`i-have-blog` adopts the rigorous evaluation philosophy of blind comparison between **Baseline Generic LLMs** and **The Editorial Operating System**.

---

## Evaluation Architecture

```
                       +-------------------+
                       | evals/cases.jsonl | (10 Standardized Scenarios)
                       +---------+---------+
                                 |
                                 v
                +----------------+----------------+
                |                                 |
                v                                 v
        [Condition A: Baseline]        [Condition B: i-have-blog]
                |                                 |
                +----------------+----------------+
                                 |
                                 v
                       +---------+---------+
                       | scripts/judge.py  | (Blind Evaluator)
                       +---------+---------+
                                 |
                                 v
                       [evals/rubric.md]
                                 |
                                 v
                       [Scores & Blocker Rate]
```

---

## The 6 Evaluation Dimensions

1. **Factual Accuracy & Evidence (25%)**: Grounded factual statements, no hallucinations.
2. **Search Intent Fit (20%)**: Directly answers the user's primary dilemma.
3. **Differentiation & Originality (20%)**: Unique framework or contrarian insight.
4. **Actionability & Math (15%)**: Real formulas, worked numbers, and checklists.
5. **Editorial Voice & Concision (10%)**: Clean rhythm, zero AI throat-clearing.
6. **SEO & Semantic Architecture (10%)**: Proper heading hierarchy and Schema.

---

## Running the Benchmark

```bash
# Execute evaluation on all test cases
python scripts/run_evals.py

# Simulate the blind judge with rubric
python scripts/judge.py
```
