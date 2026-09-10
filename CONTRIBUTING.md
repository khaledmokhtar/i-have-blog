# Contributing to `i-have-blog`

Thank you for your interest in improving the AI Editorial Operating System!

## Guiding Principles
1. **Editorial Quality First**: We prioritize empirical accuracy, differentiation, and utility over generic volume.
2. **Zero Cliché Tolerance**: Changes that introduce AI throat-clearing, generic listicles, or unsubstantiated claims will be rejected.
3. **No Multi-Agent Bloat**: Keep the orchestrator streamlined, deterministic, and inspectable.
4. **Single Source of Truth**: Always edit `skills/blog-writer/SKILL.md` directly. Never edit `.cursor/skills/blog-writer/SKILL.md` by hand.

## Pull Request Checklist
- [ ] Run `python -m unittest discover -s tests -v` and ensure 100% pass rate.
- [ ] Run `python scripts/sync_skills.py` if modifying skill instructions.
- [ ] Ensure `python scripts/run_evals.py` maintains an average Differentiation Score >= 70.
- [ ] Update `CHANGELOG.md` and documentation where relevant.
