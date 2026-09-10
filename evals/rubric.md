# Editorial Quality Rubric

<!-- judge:begin -->
Judge candidate responses blind (labeled Condition A vs Condition B) without disclosing which system produced them. Score each dimension on a scale from 1 (poor/generic) to 5 (world-class editorial standard).

| Dimension | Weight | Criteria & Measurement |
| :--- | :---: | :--- |
| **Factual Accuracy & Evidence** | 25% | Every factual and statistical claim is grounded; zero hallucinations or fabricated consensus. |
| **Search Intent & Problem Solving** | 20% | Directly solves the searcher's core dilemma immediately with high clarity. |
| **Differentiation & Originality** | 20% | Provides non-obvious angles, proprietary frameworks, or contrarian field reality. Does not repeat generic SERP copy. |
| **Actionability & Quantitative Rigor** | 15% | Includes concrete formulas, worked numerical examples, step-by-step checklists, or failure modes. |
| **Editorial Voice & Concision** | 10% | Zero AI clichés ("In today's digital world...", "Whether you're..."). Punchy, direct, and authoritative rhythm. |
| **SEO & Semantic Architecture** | 10% | Logical heading hierarchy, deep semantic entity coverage, structured FAQ, and clean Schema markup. |

### Blocker Criteria
Mark `blocker: true` if:
1. Contains dangerous or blatantly false financial/technical claims.
2. Relies on banned AI throat-clearing openings or clichéd transitions.
3. Produces unstructured walls of generic text without headers, tables, or math.
4. Fails to satisfy search intent or fabricates source citations.
<!-- judge:end -->

## Gating Rules for Production Release

A candidate version is approved for production only when:
1. It records **zero blockers** across all test cases.
2. Its overall weighted score surpasses the Baseline by at least **0.50 points**.
3. Its Differentiation & Originality dimension scores >= **4.2 / 5.0**.
4. The Differentiation Score on all test outputs exceeds **70/100**.
