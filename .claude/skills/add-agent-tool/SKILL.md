---
name: add-agent-tool
description: How to add or change a tool in Tome's agent loop (search_docs, fetch_url, recall, remember, save_note or a new one). Use when implementing FR-35 or any tool the LLM can call.
---

# Add an agent tool

Read `docs/decisions/0005-agentic-tool-loop.md` and FR-34 to FR-40 first. The tool set is deliberately small; if the job can be done by an existing tool, do not add one. A new tool needs an update to ADR 0005 or a new ADR.

## Steps

1. **Define the tool.** A name, a one-sentence description the LLM will read, a typed argument schema, and a typed result. Declare its side effect: `none`, `memory`, `network` or `file`.
2. **Gate side effects in the loop, not the tool.** For `network` and `file` tools, the loop shows a preview and asks the user before calling the tool. The model must have no argument that skips this, and the tool function must not run before confirmation. A declined call returns a plain "user declined" result, not an error.
3. **Return untrusted data safely.** Wrap what the tool returns as data, truncate it to a fixed size, and never place it in the system prompt.
4. **Count it.** Each call counts toward the step limit and its tokens toward the cost cap (FR-36, NFR-14).
5. **Trace it.** Record tool, arguments, a result summary and tokens in the trace and log (FR-39). Never log secrets.
6. **Test offline** with a fake LLM that chooses the tool: the schema, the happy path, a declined confirmation, a result containing an injected instruction ("save this note", "fetch this URL") that must cause no side-effect call, and a run that hits the step limit.
7. **Document.** Update the tool table in ADR 0005 and FR-35, the architecture diagram, the success criteria if tool choice changes, and `CHANGELOG.md`. Run `/spec-check`.
8. **Review.** Run the `safety-reviewer` subagent on the diff.

## Do not

- Give the model a way to confirm for itself.
- Let a tool call write outside the configured vault folder (ADR 0004).
- Fetch non-http(s) URLs, or localhost and private addresses, in `fetch_url`.
