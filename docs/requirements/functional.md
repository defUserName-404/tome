# Functional Requirements

**The system has 33 functional requirements in eight groups; 22 are Must-have for v1.** Priority uses MoSCoW: M = must, S = should, C = could. The last column links each requirement to the use cases in [use-cases.md](use-cases.md).

## Ingestion

| ID | Requirement | Priority | Use cases |
| --- | --- | --- | --- |
| FR-01 | Load markdown, plain text and HTML files from a folder, recursively | M | UC1, UC2, UC7 |
| FR-02 | Parse Obsidian notes: read frontmatter, tags and `[[wikilinks]]`; skip `.obsidian/`, templates and attachment folders | M | UC2, UC3 |
| FR-03 | Fetch a web page by URL, convert it to clean text, and store its URL and fetch date | M | UC6 |
| FR-04 | Index documentation files (README, docs/) from local git repositories | S | UC7 |
| FR-05 | Split documents into chunks by heading, with overlap, keeping the heading path with each chunk | M | all |
| FR-06 | Store metadata per chunk: source type, path or URL, heading, tags, modified time | M | UC2, UC3 |
| FR-07 | Re-index only files whose modified time or content hash changed; remove chunks of deleted files | M | UC2, UC6 |
| FR-08 | Report ingestion progress and a summary (files, chunks, errors) | S | all |

## Retrieval and answering

| ID | Requirement | Priority | Use cases |
| --- | --- | --- | --- |
| FR-09 | Embed chunks and queries with the selected embedding model and store vectors in a Redis vector index | M | all |
| FR-10 | Return the top-k most similar chunks for a query (k configurable) | M | all |
| FR-11 | Filter retrieval by metadata (source type, tag, folder) before or during vector search | S | UC2, UC3 |
| FR-12 | Generate the answer with the LLM using only the retrieved chunks as context | M | all |
| FR-13 | Cite every answer with source, path or URL, and section heading | M | all |
| FR-14 | When retrieved chunks do not support an answer, say so instead of guessing | M | all |
| FR-15 | Flag conflicts when notes and official docs disagree | C | UC3 |

## Semantic cache

| ID | Requirement | Priority | Use cases |
| --- | --- | --- | --- |
| FR-16 | Before retrieval, look up the query in a semantic cache; on a hit above the similarity threshold, return the stored answer without an LLM call | M | UC4 |
| FR-17 | Similarity threshold and time-to-live are configurable | M | UC4 |
| FR-18 | Clear cached answers that depend on a source when that source is re-indexed | S | UC4, UC6 |
| FR-19 | Show whether an answer came from cache, and log tokens and estimated cost saved | S | UC4 |

## Memory

| ID | Requirement | Priority | Use cases |
| --- | --- | --- | --- |
| FR-20 | Keep conversation history within a session so follow-up questions work | M | UC5 |
| FR-21 | Persist session history in Redis and reload it by session ID in a later run | M | UC5 |
| FR-22 | Store long-term facts and preferences (for example preferred language, projects) and include them in context | S | UC5 |
| FR-23 | Let me view and delete stored memories | C | UC5 |

## Obsidian write-back

| ID | Requirement | Priority | Use cases |
| --- | --- | --- | --- |
| FR-24 | On request, create a markdown note in the vault from an answer or conversation | M | UC9 |
| FR-25 | Write only inside one configured folder (default `Inbox/AI/`); refuse any other path | M | UC9 |
| FR-26 | Never overwrite an existing note; create a new file or append, after confirmation | M | UC9 |
| FR-27 | Show a preview of the note and ask for confirmation before writing; support a dry-run flag | M | UC9 |
| FR-28 | Add frontmatter to every written note: `source: ai`, date, tags, and `[[links]]` to the cited notes | S | UC9 |
| FR-29 | Index written notes automatically, labelled as AI-generated so they rank below my own notes | S | UC9 |

## Provider abstraction

| ID | Requirement | Priority | Use cases |
| --- | --- | --- | --- |
| FR-30 | Select LLM and embedding provider by config file or environment; cloud is the default | M | UC8 |
| FR-31 | Offer to choose the provider interactively at start when none is set; local models (Ollama) are optional, never required | S | UC8 |
| FR-32 | Detect an embedding-model change (different name or dimensions) and require a re-index instead of failing silently | M | UC8 |

## Interface

| ID | Requirement | Priority | Use cases |
| --- | --- | --- | --- |
| FR-33 | Provide a CLI with commands `ingest`, `ask`, `chat`, `sources`, `reindex`, `save`, `memory` | M | all |

## Coverage check

Every use case is covered by at least one Must requirement: UC1 and UC7 by FR-01, FR-05, FR-12 and FR-13; UC2 by FR-02 and FR-09; UC3 by FR-02 and FR-12; UC4 by FR-16 and FR-17; UC5 by FR-20 and FR-21; UC6 by FR-03 and FR-07; UC8 by FR-30 and FR-32; UC9 by FR-24 to FR-27.
