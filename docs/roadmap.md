# Phased Roadmap

**The build runs in seven phases, each ending in something I can run and test before the next starts.** Each later phase depends on the one above it.

| Phase | Deliverable | Requirements | Done when |
| --- | --- | --- | --- |
| 0. Environment | `docker-compose.yml` with Redis Stack; Python project; provider keys; sample docs (Pro Git) | NFR-10 | PING returns PONG; LLM and embedding calls work |
| 1. Ingestion | Loaders, heading-based chunker, metadata, embeddings stored in a Redis vector index | FR-01, 05 to 09 | Pro Git fully indexed; incremental re-index works |
| 2. RAG answers | Retrieval, grounded answer, citations, "not found" behaviour, CLI `ask` | FR-10 to 14, 33 | Test set meets 85% correct citation |
| 3. Semantic cache | Cache lookup before retrieval, threshold and TTL config, cost log | FR-16 to 19 | 60% hit rate on paraphrases, no wrong hits |
| 4. Memory | Session history in Redis, reload by ID, long-term facts | FR-20 to 23 | Follow-ups survive a restart |
| 5. More sources and Obsidian | Vault parsing, web fetch, repo docs, metadata filters, safe write-back | FR-02 to 04, 11, 15, 24 to 29 | Vault searchable; 0 unsafe writes in test |
| 6. Provider switching | Pluggable LLM and embedding adapters, interactive choice, re-index guard | FR-30 to 32 | Same test set runs on cloud and Ollama |

After phase 6: polish (README, demo recording, tests in CI) and optional extras such as a small web UI or an Obsidian plugin.
