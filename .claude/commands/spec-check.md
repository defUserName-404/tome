---
description: Check the docs for broken links, bad IDs and contradictions
allowed-tools: Bash(python scripts/check_spec.py:*), Bash(git diff:*), Read, Grep, Glob
---

Check that the spec is consistent.

1. Run `python scripts/check_spec.py`. It checks links, FR, NFR and UC numbering, the counts in the lead sentences, the use-case coverage check, references to IDs that do not exist, and that every ADR is listed in `docs/README.md`.
2. Then check what a script cannot:
   - Every FR named in `docs/roadmap.md` exists in `docs/requirements/functional.md`, and a phase does not depend on a requirement from a later phase.
   - Each ADR agrees with the requirements it cites (priorities, defaults, limits).
   - Every Must requirement has a matching success criterion or a test plan.
3. Report problems as a table: file, problem, suggested fix. Do not edit anything unless I ask.
4. If everything is consistent, say so in one line.
