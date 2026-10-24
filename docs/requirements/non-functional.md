# Non-Functional Requirements

**The agent must be private by design, cheap to run, quick to answer, and easy to rebuild from scratch.** Targets are for a single user on a laptop with a vault of up to 5,000 notes.

| ID | Area | Requirement | Target |
| --- | --- | --- | --- |
| NFR-01 | Privacy | Only the retrieved chunks and the question are sent to a cloud LLM; the full vault is never uploaded | Verified by logging the outbound prompt |
| NFR-02 | Privacy | With a local provider selected, no document text leaves the machine | Zero outbound calls except Redis and Ollama |
| NFR-03 | Security | API keys come from environment variables or a git-ignored `.env`; never from code or notes | No secrets in the repo |
| NFR-04 | Latency | Cached answer returned | under 300 ms |
| NFR-05 | Latency | Uncached answer, retrieval plus LLM, first token | under 5 s with a cloud LLM |
| NFR-06 | Cost | Show tokens used and estimated cost per query and per session | Reported on every answer |
| NFR-07 | Cost | Initial ingest of Pro Git plus a 5,000-note vault | under 5 USD in cloud embedding fees, or free with local embeddings |
| NFR-08 | Safety | Vault writes limited to one folder; no deletes; all writes logged | 0 unintended file changes |
| NFR-09 | Reliability | If Redis or the LLM is down, show a clear error and leave data intact | No crash, no data loss |
| NFR-10 | Setup | One command (`docker compose up`) starts Redis Stack; one command ingests; setup documented in the README | New machine ready in under 15 minutes |
| NFR-11 | Testability | Ingestion, retrieval, cache and write-back each have automated tests; a fixed question set measures answer quality | Tests run with one command |
| NFR-12 | Portability | Runs on macOS and Linux with Python 3.11 or newer | Both pass the smoke tests |
