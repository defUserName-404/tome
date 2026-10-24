---
description: Report roadmap progress, meaning which phase is current and what has code and tests
allowed-tools: Read, Grep, Glob, Bash(git log:*)
---

Report where the project stands against `docs/roadmap.md`.

1. Read `docs/roadmap.md` and list each phase with its requirements.
2. For each requirement, look in `src/tome/` and `tests/` for an implementation and a test that names it. Use `git log --oneline` for context.
3. Output a table: Phase, Status (`not started`, `in progress`, `done`), Evidence (file paths). A phase is `done` only when its "Done when" condition has a passing test or a recorded result.
4. Name the current phase and the next one or two tasks, linking the plan in `docs/plans/` if one exists.
5. Say which statuses you inferred rather than verified.

Do not edit files.
