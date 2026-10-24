# Glossary

| Term | Meaning |
| --- | --- |
| RAG | Retrieval-augmented generation: find relevant text first, then have the LLM answer using only that text |
| Embedding | A list of numbers (a vector) that captures the meaning of a piece of text |
| Vector index | A Redis index that finds the stored vectors closest to a query vector |
| Chunk | A slice of a document, here one heading section, that is embedded and retrieved on its own |
| Semantic cache | A cache keyed by meaning, so a reworded question can reuse an earlier answer |
| Similarity threshold | The minimum closeness for a cached answer to count as a match |
| Session memory | Conversation history kept for one chat, reloadable by session ID |
| Long-term memory | Facts and preferences kept across sessions |
| Redis Stack | Redis bundled with vector search and JSON support |
| RedisVL | Python library for Redis vector search, caching and message history |
| Ollama | Tool for running LLMs and embedding models locally |
| Vault | An Obsidian folder of markdown notes |
| MoSCoW | Priority labels: Must, Should, Could |
| Agent loop | The cycle where the LLM picks a tool, reads the result and repeats until it can answer |
| Tool calling | An LLM feature where the model asks the program to run a named function with arguments |
| Prompt injection | Text in a note or web page that tries to give the LLM instructions of its own |
