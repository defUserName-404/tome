# Overview and Purpose

**Tome is a personal assistant that reads my documentation so I don't have to: it answers questions from my Obsidian vault, Pro Git, live web docs and my own project repos, cites where each answer came from, and can save results back into Obsidian.**

It is built to serve two goals at once: a hands-on way to learn retrieval-augmented generation (RAG) on Redis, and a tool I actually use every day.

**The problem today**

- My knowledge is scattered across four places: Obsidian notes, books like Pro Git, official web docs and my own repo READMEs. No single search covers them.
- Keyword search misses notes when I don't remember the exact words I used.
- Asking a general LLM costs tokens every time, even for a question I already asked last week, and it knows nothing about my notes.
- A chat session forgets everything when it ends, so I repeat my context and preferences.
- Answers from a bare LLM are not tied to a source, so I cannot check them.

**Why I need this**

- Find things by meaning, not exact words, across all my sources in one place.
- Get answers grounded in my own material, with a citation I can open.
- Pay for an LLM call only when no similar question was already answered (semantic cache).
- Keep memory across sessions, and push useful answers back into my vault so knowledge compounds.
- Learn the full RAG stack (chunking, embeddings, vector search, caching, memory) by building it, and end with a portfolio project.

**Vision:** a command-line agent that gets more useful the more I use it, runs on a cloud LLM by default, and can switch to local models when I want privacy.
