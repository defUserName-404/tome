# Tome

[![CI](https://github.com/defUserName-404/tome/actions/workflows/ci.yml/badge.svg)](https://github.com/defUserName-404/tome/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

**Tome is a personal assistant that reads your documentation so you don't have to.** It answers questions from your Obsidian vault, books like Pro Git, live web docs and your own project repos. Every answer cites its source, repeat questions are served from a semantic cache, and results can be saved back into your vault.

> **Status: planning.** The requirements are written and the project scaffold is in place. No application logic exists yet. The build starts at [phase 0 of the roadmap](docs/roadmap.md).

## Why

- Notes, books, web docs and repo READMEs live in different places, and no single search covers them.
- Keyword search misses notes when you don't remember the exact words you used.
- A bare LLM costs tokens on every repeat question, forgets you between sessions, and cites nothing.

## Planned features

- **Agentic answers:** the model decides which tool to use (search docs, fetch a page, recall memory, save a note) within step and cost limits, and asks you before it fetches or writes anything.
- **Retrieval-augmented answers** with a source and section for every claim, and an honest "not found" when the sources don't support an answer.
- **Many sources:** Obsidian vault (frontmatter, tags, wikilinks), markdown and HTML docs, PDF books, web pages by URL, local git repos.
- **Semantic cache:** a reworded question reuses an earlier answer without an LLM call.
- **Memory:** session history and long-term preferences that survive restarts.
- **Safe Obsidian write-back:** save an answer as a new note in one configured folder, with a preview and confirmation, never overwriting anything.
- **Pluggable providers:** cloud LLM by default, local models (Ollama) optional, chosen by config.

The full list is in the [requirements](docs/requirements/functional.md).

## Use cases

| ID | Scenario |
| --- | --- |
| UC1 | Ask a git question, get an answer from Pro Git with the chapter cited |
| UC2 | "What did I write about X?" across my notes, matched by meaning |
| UC3 | Combine my notes with official docs, flagging conflicts |
| UC4 | Ask a similar question again and get it from the cache |
| UC5 | Continue in a later session with context remembered |
| UC6 | Index a web docs page by URL and keep it fresh |
| UC7 | Ask about my own projects from their READMEs |
| UC8 | Switch between a cloud and a local model |
| UC9 | Save an answer to my Obsidian vault |
| UC10 | Paste a URL and get an answer from that page, after confirming the fetch |
| UC11 | Compare my notes with the official docs, then save a summary |

Details and expected outcomes: [use-cases.md](docs/requirements/use-cases.md).

## Architecture

Python and [RedisVL](https://github.com/redis/redis-vl-python) on Redis Stack. Ingestion fills one Redis index; every question checks the semantic cache first, then an LLM-driven tool loop searches the index, fetches pages and saves notes, asking you before it does either of the last two. See [architecture](docs/architecture.md) and the [decision records](docs/decisions/).

## Quickstart (phase 0: environment only)

Requirements: Docker with Compose, Python 3.11 or newer.

```bash
# 1. Start Redis Stack
docker compose up -d

# 2. Install the package with dev tools
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"

# 3. Configure
cp .env.example .env   # then fill in the provider you chose

# 4. Verify the environment
python scripts/smoke_test.py
```

The smoke test currently checks Redis (`PING` and the search module). LLM and embedding checks arrive with the provider adapters in phase 0.

## Documentation

Start at the [docs index](docs/README.md).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). AI coding agents should start with [AGENTS.md](AGENTS.md).

## License

[MIT](LICENSE)
