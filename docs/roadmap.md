# Phased Roadmap

**The build runs in eight phases, each ending in something I can run and test before the next starts.** Each later phase depends on the one above it.

| Phase | Deliverable | Requirements | Done when |
| --- | --- | --- | --- |
| 0. Environment | `docker-compose.yml` with Redis Stack; Python project; provider keys; sample docs (Pro Git) | NFR-10 | PING returns PONG; LLM and embedding calls work |
| 1. Ingestion | Loaders, heading-based chunker, metadata, embeddings stored in a Redis vector index | FR-01, 05 to 09 | Pro Git fully indexed; incremental re-index works |
| 2. RAG answers | Retrieval, grounded answer, citations, "not found" behaviour, CLI `ask` | FR-10 to 14, 33 | Test set meets 85% correct citation |
| 3. Agent loop | Tool-calling loop with the `search_docs` tool, step and cost limits, tool-call trace, untrusted-content labelling, fixed-pipeline fallback | FR-34 to 36, 38 to 40 | 85% correct first tool on the test set; no question exceeds its limits |
| 4. Semantic cache | Cache lookup before the loop, threshold and TTL config, cost log | FR-16 to 19 | 60% hit rate on paraphrases, no wrong hits |
| 5. Memory | Session history in Redis, reload by ID, long-term facts, `recall` and `remember` tools | FR-20 to 23, 35 | Follow-ups survive a restart |
| 6. More sources and Obsidian | Vault parsing, repo docs, metadata filters, `fetch_url` and `save_note` tools with confirmation, safe write-back | FR-02 to 04, 11, 15, 24 to 29, 37 | Vault searchable; 0 unsafe writes; 0 side-effect calls without confirmation in the injection test set |
| 7. Provider switching | Pluggable LLM and embedding adapters, tool-calling flag per adapter, interactive choice, re-index guard | FR-30 to 32, 40 | Same test set runs on cloud and Ollama, in agent or pipeline mode |

After phase 7: polish (README, demo recording, tests in CI) and optional extras such as a small web UI or an Obsidian plugin.
