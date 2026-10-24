# Architecture Overview

**Two flows share one Redis Stack: ingestion fills it, and every question reads from it, checking the cache before anything else.**

```mermaid
flowchart LR
    subgraph Ingest["Ingest: runs when files change or a page is fetched"]
        S["Sources<br/>notes, docs, repos, pages"] --> C["Chunk<br/>split by heading"]
        C --> E["Embed<br/>text to vectors"]
        E --> R[("Redis index<br/>vectors + metadata")]
    end

    subgraph Ask["Ask: runs on every question"]
        Q["Question<br/>CLI: ask / chat"] --> K{"Check cache<br/>similar question?"}
        K -- hit --> A["Answer<br/>with citations"]
        K -- miss --> G["Agent loop<br/>LLM picks a tool, reads the result, repeats<br/>step and cost limits"]
        G --> A
    end

    G <-->|search_docs| R
    G <-->|recall / remember| MEM[("Memory<br/>session + facts")]
    G -. "fetch_url (I confirm)" .-> W["Web page"]
    W --> C
    G -. "save_note (I confirm)" .-> O["Obsidian note"]
    A --> CM["Cache + memory<br/>reuse next time"]
```

A cache hit returns at once. On a miss the agent loop starts: the LLM picks a tool, reads what it returns, and repeats until it can answer, within a step and cost limit. `fetch_url` and `save_note` run only after I confirm. The final answer is stored in the cache and memory. If the provider cannot call tools reliably, Tome skips the loop and runs the fixed pipeline: retrieve chunks, ask the LLM, answer ([ADR 0005](decisions/0005-agentic-tool-loop.md)).

## Technology choices

| Layer | Choice | Reason |
| --- | --- | --- |
| Language | Python 3.11 or newer | Best-supported path for RedisVL ([ADR 0002](decisions/0002-python-and-redisvl.md)) |
| Store | Redis Stack in Docker Compose | Vector search, JSON and caching in one container ([ADR 0001](decisions/0001-use-redis-stack.md)) |
| Redis library | RedisVL | Ready-made vector index, semantic cache and message history |
| LLM and embeddings | Provider adapters; cloud default, Ollama optional | Swap by config without code changes ([ADR 0003](decisions/0003-pluggable-providers.md)) |
| Agent loop | Hand-written tool-calling loop over the provider adapter | Five tools, full control, no framework dependency ([ADR 0005](decisions/0005-agentic-tool-loop.md)) |
| Obsidian access | Direct read and write of the vault folder | Works with Obsidian closed; an Obsidian MCP can be added later ([ADR 0004](decisions/0004-vault-write-back-safety.md)) |
| Web docs | HTTP fetch plus HTML-to-text conversion | Simple, no browser needed for most documentation sites |
| Interface | Command-line program | Fast to build and test; a UI is out of scope for v1 |
