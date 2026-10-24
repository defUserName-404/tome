# 000. Phase 0: environment

- Status: Draft
- Date: 2026-10-24
- Roadmap phase: 0
- Requirements: NFR-10, NFR-12
- Decisions: [ADR 0001](../decisions/0001-use-redis-stack.md), [ADR 0002](../decisions/0002-python-and-redisvl.md), [ADR 0003](../decisions/0003-pluggable-providers.md)

## Goal

A fresh clone can start Redis Stack, install the package, and pass a smoke test that proves Redis, one LLM call and one embedding call all work.

## Scope

In scope:

- Redis Stack through Docker Compose, with persistence on.
- Python package install with dev tools.
- A smoke test with Redis, LLM and embedding checks.
- Sample documentation to test with: the Pro Git markdown source.

Out of scope:

- Chunking, indexing and retrieval (phase 1 and 2).
- Provider switching and the interactive provider prompt (phase 7).

## Approach

The Compose file, package stub and Redis checks already exist. This phase picks the default cloud providers, adds one LLM check and one embedding check to `scripts/smoke_test.py` behind a minimal adapter each (see the `add-provider-adapter` skill), and documents getting the sample docs.

## Tasks

- [ ] Choose the default cloud LLM and embedding provider and record it in ADR 0003 and the README
- [ ] Verify `docker compose up -d` and `redis-cli PING` return PONG on a clean machine
- [ ] Add the LLM call check to the smoke test
- [ ] Add the embedding call check, printing the model name and vector dimensions
- [ ] Clone `progit/progit2` into `data/progit2` (git-ignored) and document the command in the README
- [ ] Offline tests for the new checks, using fakes
- [ ] Docs and CHANGELOG updated
- [ ] `python scripts/check_spec.py` passes

## Done when

`python scripts/smoke_test.py` reports ok for Redis (PING and search module), the LLM call and the embedding call, and a fresh clone reaches that point in under 15 minutes (NFR-10).

## Risks and open questions

- Which cloud provider is the default? Tracked as an open question in [risks.md](../risks.md).
- Embedding dimensions depend on the chosen model, so the index in phase 1 must read them from the adapter and not hard-code them.
