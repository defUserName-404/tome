# Users and Use Cases

**One primary user: me, a developer who keeps notes in Obsidian, reads technical docs, and works on personal projects.** Eleven use cases define what the agent must do.

| ID | Scenario | Example input | Expected outcome |
| --- | --- | --- | --- |
| UC1 | Ask a git question | "How do I undo my last commit but keep the changes?" | Answer from Pro Git with chapter and section cited |
| UC2 | Search my own notes by meaning | "What did I write about Redis persistence?" | Relevant notes listed with paths and short excerpts, even if the words differ |
| UC3 | Combine notes and official docs | "How do I set up RedisVL, given my notes and the docs?" | One answer using both, with sources labelled; conflicts between them flagged |
| UC4 | Repeat a similar question | "How can I revert my latest commit?" (after UC1) | Served from the semantic cache; no LLM call; visibly faster and free |
| UC5 | Continue in a later session | "Continue what we discussed yesterday about Docker" | Agent recalls prior topics and my stated preferences |
| UC6 | Ingest live web docs | "Index https://redis.io/docs/... and answer from it" | Page fetched, chunked, indexed; re-indexed when it changes |
| UC7 | Ask about my own projects | "How is the AI\_Farming data pipeline structured?" | Answer from that repo's README and docs, with file paths |
| UC8 | Switch provider | "Use local Ollama for this session" | Same features work on a local model, chosen by config or asked at start |
| UC9 | Save results to Obsidian | "Save this answer to my vault" | New note written to a safe folder with tags, date and links to its sources; indexed afterwards |
| UC10 | Answer from a page I paste | "How does semantic caching work here? https://redis.io/docs/..." | Tome proposes fetching the page and asks me to confirm; it indexes the page, then answers with the page cited. If I decline, it says what it could not use |
| UC11 | Multi-step task | "Compare my Docker volume notes with the official docs, then save a summary" | Tome searches my notes and the docs, answers with both cited, then offers to save the summary; the note is written only after I confirm |
