# Working with AI coding agents

This repo is set up so AI coding agents and humans follow the same rules. The rules live in [AGENTS.md](../../AGENTS.md), the cross-tool standard that most agents read. [CLAUDE.md](../../CLAUDE.md) imports it and adds Claude Code specifics.

## Slash commands

| Command | Use it to |
| --- | --- |
| [`/smoke`](../../.claude/commands/smoke.md) | Run the Step Zero smoke test and read the result |
| [`/new-adr <title>`](../../.claude/commands/new-adr.md) | Create the next decision record |
| [`/spec-check`](../../.claude/commands/spec-check.md) | Check links, IDs, counts and contradictions in the docs |
| [`/phase-status`](../../.claude/commands/phase-status.md) | See roadmap progress against the code |
| [`/implement-fr <FR-id>`](../../.claude/commands/implement-fr.md) | Plan, build, test and review one requirement |

## Subagents

| Subagent | Role | Edits files |
| --- | --- | --- |
| [`spec-reviewer`](../../.claude/agents/spec-reviewer.md) | Finds contradictions and gaps in the spec | No |
| [`safety-reviewer`](../../.claude/agents/safety-reviewer.md) | Reviews vault writes, side-effect tools, prompts, URL fetching and secrets | No |
| [`test-writer`](../../.claude/agents/test-writer.md) | Writes offline tests for a requirement | Tests only |

## Skills

| Skill | Use it when |
| --- | --- |
| [`add-agent-tool`](../../.claude/skills/add-agent-tool/SKILL.md) | Adding or changing a tool in the agent loop |
| [`add-provider-adapter`](../../.claude/skills/add-provider-adapter/SKILL.md) | Adding an LLM or embedding provider |
| [`add-ingestion-loader`](../../.claude/skills/add-ingestion-loader/SKILL.md) | Adding a source type to ingestion |
| [`write-adr`](../../.claude/skills/write-adr/SKILL.md) | Deciding whether a change needs an ADR, and writing it |

## Plans

Work that touches more than one module starts with a plan in [docs/plans/](../plans/), copied from the [template](../plans/TEMPLATE.md). The first plan covers [phase 0, the environment](../plans/000-phase-0-environment.md).

## Typical flow for one requirement

1. `/phase-status` to confirm the phase.
2. `/implement-fr FR-05` to plan, implement and test it.
3. `safety-reviewer` if the change touches a safety area.
4. `/spec-check`, then open a pull request.

## Permissions

[.claude/settings.json](../../.claude/settings.json) allows the lint, test and read-only git commands used above, and denies reading `.env` and force-pushing. Put personal changes in `.claude/settings.local.json`, which is git-ignored.
