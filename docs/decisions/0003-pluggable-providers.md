# 0003. Make LLM and embedding providers pluggable, cloud by default

- Status: Accepted
- Date: 2026-10-24

## Context

Answer quality is best with a cloud LLM, but some notes are private and some users want to run fully local. The embedding model also decides the vector size of the Redis index, so changing it affects stored data.

## Decision

- LLM and embedding providers are separate adapters selected by config or environment (`TOME_LLM_PROVIDER`, `TOME_EMBEDDING_PROVIDER`), or asked for at start when unset.
- Cloud is the default. Local models (Ollama) are optional and never required.
- Only the question and the retrieved chunks are sent to a cloud LLM. The full vault is never uploaded.
- The index stores the embedding model name and dimensions. If they change, Tome requires a re-index instead of failing silently.

## Consequences

- Same features work on cloud and local models, which the test set verifies (see success criteria).
- Switching embedding model costs a full re-index.
- Each adapter needs its own tests and optional dependency.

Related requirements: FR-30, FR-31, FR-32, NFR-01, NFR-02.
