# 0005. Answer through an agentic tool-calling loop

- Status: Accepted
- Date: 2026-10-24

## Context

A fixed pipeline (check cache, retrieve, answer) handles one-shot questions well, but several use cases need the model to decide what to do next: fetch a page the user pasted (UC10), or search notes and docs, compare them, then offer to save a summary (UC11). Letting a model choose tools also adds risks: runaway loops, wrong tool choices, and instructions hidden in notes or web pages (prompt injection) steering side effects such as writing files.

## Decision

- Answer cache misses with a **single tool-calling loop**: the LLM picks a tool, reads the result, and repeats until it can answer (FR-34).
- The tool set is small and fixed (FR-35):

  | Tool | Purpose | Side effect |
  | --- | --- | --- |
  | `search_docs` | Vector search with metadata filters | none |
  | `recall`, `remember` | Read and write long-term memory | memory only |
  | `fetch_url` | Fetch a page and index it | network, index |
  | `save_note` | Write a note to the vault | file write |

- Tools with side effects outside Redis, `fetch_url` and `save_note`, require user confirmation on every call. The model cannot skip it (FR-37). `save_note` also keeps every rule from [ADR 0004](0004-vault-write-back-safety.md).
- Each question has a step limit (default 6) and a cost cap. When one is hit, the loop stops and answers from what it gathered (FR-36, NFR-14).
- Retrieved chunks and fetched pages are marked as untrusted data in the prompt, and instructions inside them are never followed as if they came from the user (FR-38, NFR-15).
- The semantic cache stays in front of the loop, so repeat questions never start it (FR-16).
- Every tool call is shown and logged (FR-39).
- Providers that cannot call tools reliably, such as small local models, use the fixed pipeline instead, and Tome says which mode is active (FR-40). Each LLM adapter declares whether it supports tool calling ([ADR 0003](0003-pluggable-providers.md)).
- The loop is hand-written on top of the provider adapters. No agent framework is required.

## Consequences

Good:

- UC10 and UC11 work, and new tools can be added without changing the pipeline.
- Side effects stay under the user's control, so a bad tool choice or an injected instruction cannot write to the vault by itself.
- The loop is small enough to read and test end to end, which suits the learning goal.

Costs:

- More LLM calls per question, so higher latency and cost than the fixed pipeline (NFR-13, NFR-14).
- Answer quality now depends on tool choice, which needs its own test set (see success criteria).
- Two modes (agent and fixed pipeline) must both be maintained and tested.

## Alternatives considered

| Option | Why not now |
| --- | --- |
| Fixed pipeline only | Cannot do UC10 or UC11 without hard-coded rules for each case |
| Agent framework (PydanticAI, LangChain, LlamaIndex) | Useful later, but hides the loop that this project exists to teach. Revisit if the tool set grows |
| Multiple cooperating agents | Far more complexity than five tools need |
