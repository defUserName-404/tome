@AGENTS.md

## Claude Code specifics

- Project slash commands live in `.claude/commands/`, subagents in `.claude/agents/`, skills in `.claude/skills/`. Shared permissions are in `.claude/settings.json`; personal overrides go in `.claude/settings.local.json`, which is git-ignored.
- For a change that touches more than one module, write or update a plan in `docs/plans/` first (template: `docs/plans/TEMPLATE.md`) and get approval before coding.
- Run `/spec-check` after editing anything under `docs/`.
- Run the `safety-reviewer` subagent before you finish a change in a safety area (see AGENTS.md rule 4).
- Prefer `/implement-fr FR-xx` for requirement work, so planning, tests and review happen in order.
