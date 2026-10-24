# Risks and Open Questions

**The biggest risks are a wrong cache hit, a damaged vault, and being locked into one embedding model.** Each has a planned control.

| Risk | Likelihood | Impact | Mitigation |
| --- | --- | --- | --- |
| Cache returns an answer to a question that only looks similar | Medium | High | Conservative threshold; test with near-miss questions; show "from cache" label; easy cache clear |
| Write-back overwrites or clutters my vault | Low | High | Single write folder, no overwrite, preview and confirm, vault in git or backed up (FR-25 to FR-27) |
| AI-written notes are retrieved later as if they were my own thinking | Medium | Medium | `source: ai` frontmatter; rank below my notes; label in citations (FR-28, FR-29) |
| Switching embedding model changes vector size and breaks the index | High | Medium | Store model name and dimensions with the index; force a re-index on change (FR-32) |
| Private notes sent to a cloud provider | Medium | High | Send only retrieved chunks; local provider option; exclude folders by config (NFR-01, NFR-02) |
| Web docs change or go stale | Medium | Low | Store fetch date; re-fetch on demand; invalidate related cache (FR-07, FR-18) |
| Poor chunking of long or unstructured notes lowers answer quality | Medium | Medium | Chunk by heading; tune size and overlap against the test set |
| API rate limits or outages slow ingest | Medium | Low | Batch embeddings, retry with backoff, resume where it stopped |
| Sync tools (iCloud, Obsidian Sync) create conflicts with written notes | Low | Medium | Write new files only; unique filenames with timestamps |

**Open questions**

- [ ] Which cloud LLM and embedding provider is the default (Anthropic, OpenAI, Gemini, other)?
- [ ] How large is the vault today (note count), and are any folders private and to be excluded?
- [ ] Which web docs sites and which repos come first?
- [ ] Is the vault in git or backed up before write-back is switched on?
- [ ] Should the interface stay a CLI, or later also expose an Obsidian plugin or local API?
