# 0001. Use Redis Stack as the single data store

- Status: Accepted
- Date: 2026-10-24

## Context

Tome needs a vector index for retrieval, a semantic cache, session memory and metadata filtering. Running a separate vector database, cache and key-value store for one user is heavy, and the project also exists to learn how these pieces fit together.

## Decision

Use Redis Stack, run through Docker Compose, for all four jobs.

## Consequences

Good:

- One container covers vector search, caching, message history and JSON metadata.
- RedisVL provides a vector index, `SemanticCache` and message history out of the box.
- In-memory lookups keep cached answers fast (see NFR-04).
- Metadata filters and vector search combine in one query (FR-11).

Costs:

- Data lives in RAM, which is fine for thousands of notes and a few books but costly at millions of chunks.
- Persistence must be enabled (the Compose file turns on AOF), or a restart can lose the index.
- A Docker container must be running whenever Tome is used.

## Alternatives considered

| Option | Why not now |
| --- | --- |
| SQLite with sqlite-vec | Simpler for a single user, but cache and memory helpers would be written by hand |
| Chroma or LanceDB | Easy local vector search, but cache and memory are separate work |
| Postgres with pgvector | Production-grade, but heavier to set up than the use case needs |

If Tome is later used purely as a daily tool, the store can be revisited. Keep storage behind a small interface so a swap stays possible.
