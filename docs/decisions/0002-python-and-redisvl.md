# 0002. Build in Python with RedisVL

- Status: Accepted
- Date: 2026-10-24

## Context

Redis has client libraries for many languages. RedisVL, the high-level library for vector search, caching and message history, is most mature in Python, and the LLM and embedding provider SDKs are best supported there too.

## Decision

Write Tome in Python 3.11 or newer and use RedisVL for the vector index, semantic cache and session history. Use `ruff` for linting and `pytest` for tests.

## Consequences

- Less glue code: the index, cache and history come from one library.
- Provider SDKs (Anthropic, OpenAI, Ollama) are optional extras in `pyproject.toml`, so users install only what they use.
- Python 3.11 is the minimum; CI runs 3.11 and 3.12.
- A TypeScript or Java port would need to rebuild the cache and history layers.
