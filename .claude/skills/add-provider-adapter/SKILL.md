---
name: add-provider-adapter
description: How to add an LLM or embedding provider adapter (Anthropic, OpenAI, Gemini, Ollama or another) to Tome. Use when implementing FR-30 to FR-32 or supporting a new provider.
---

# Add a provider adapter

Read `docs/decisions/0003-pluggable-providers.md` first. Cloud is the default; local models are optional and never required.

## Steps

1. **Pick the kind.** LLM and embedding providers are separate adapters. A provider may offer both, but each is selected on its own (`TOME_LLM_PROVIDER`, `TOME_EMBEDDING_PROVIDER`).
2. **Implement the interface.**
   - LLM adapter: a chat call that accepts messages and optional tool definitions, and reports token usage. Declare `supports_tool_calling`. Tome uses the fixed pipeline when it is false (FR-40).
   - Embedding adapter: an embed call for a batch of texts. Expose the model name and the vector dimensions.
3. **Keep the SDK inside the adapter.** No provider import anywhere else. Add the SDK as an optional extra in `pyproject.toml`, for example `anthropic = ["anthropic"]`.
4. **Configuration.** Read keys and hosts from environment variables, and add them, blank, to `.env.example`. Never print or log them.
5. **Index guard.** The index stores the embedding model name and dimensions. If they differ from the adapter, fail with a clear message that asks for a re-index (FR-32).
6. **Errors and limits.** Retry with backoff on rate limits and timeouts, surface other errors clearly, and report an estimated cost per call (NFR-06, NFR-09).
7. **Test offline.** Use recorded or hand-written fake responses. No network, no real keys. Cover tool-calling on and off, token accounting, and the dimension mismatch.
8. **Smoke test.** Add the provider's check to `scripts/smoke_test.py`.
9. **Document.** Update `.env.example`, the README quickstart, and ADR 0003 if behaviour changes. Run `/spec-check`.

## Privacy

A cloud adapter receives only the question and what tools return (NFR-01). A local adapter must make no outside network calls (NFR-02).
