---
description: Plan, implement and test one functional requirement (for example FR-05)
argument-hint: <FR-id>
---

Implement requirement $ARGUMENTS. If no ID is given, ask which one.

1. **Read.** Find the row in `docs/requirements/functional.md`, the use cases it links, related NFRs, and any ADR it cites. Check `docs/roadmap.md`: if the requirement belongs to a later phase than the current one, stop and tell me.
2. **Plan.** Copy `docs/plans/TEMPLATE.md` to `docs/plans/NNN-<slug>.md` and fill it in. Show it to me and wait for approval when more than one file will change.
3. **Implement** in `src/tome/` following `AGENTS.md`. Use the matching skill when one applies: `add-agent-tool`, `add-provider-adapter`, `add-ingestion-loader`.
4. **Test.** Delegate offline tests to the `test-writer` subagent, then run `ruff check .` and `pytest`.
5. **Review.** If the change touches vault writes, tools with side effects, prompts or secrets, run the `safety-reviewer` subagent and fix what it finds.
6. **Docs.** Update affected docs and `CHANGELOG.md`, then run `python scripts/check_spec.py`.
7. **Report** what changed, what you verified, and what you could not verify.
