---
name: add-ingestion-loader
description: How to add a document loader to Tome's ingestion pipeline (markdown, text, HTML, Obsidian vault, web page, git repo, PDF). Use when implementing FR-01 to FR-08 or supporting a new source type.
---

# Add an ingestion loader

Read FR-01 to FR-08 in `docs/requirements/functional.md` and `docs/architecture.md` first.

## Steps

1. **One job per loader.** A loader turns a source into documents, nothing more. Chunking, embedding and storage are separate stages shared by all loaders.
2. **Document shape.** Each document carries: source type (`obsidian`, `docs`, `web`, `repo`, `pdf`), path or URL, title, tags, modified time and a content hash. Chunks add the heading path.
3. **Chunk by heading** with overlap, and keep the heading path with every chunk (FR-05). Fall back to size-based splitting for text with no headings.
4. **Source rules.**
   - Obsidian: read frontmatter, tags and `[[wikilinks]]`; skip `.obsidian/`, templates and attachment folders; detect `source: ai` frontmatter and label those notes so they rank lower (FR-02, FR-29).
   - Web: store the URL and fetch date; convert to clean text; only http and https.
   - PDF: extract text per page, keep the page number for citations, and report scanned PDFs as unsupported until OCR exists.
   - Repo: only README and `docs/` files, never source code or `.env`.
5. **Incremental runs.** Re-index only files whose modified time or hash changed, and remove chunks of deleted files (FR-07). Re-indexing a source must clear cached answers that depend on it (FR-18).
6. **Report.** Print files, chunks and errors at the end (FR-08). A bad file is reported and skipped, never silently dropped.
7. **Test offline** with small fixtures in `tests/fixtures/`: headings, no headings, frontmatter, a skipped folder, a changed file, a deleted file. Never copy real notes into fixtures.
8. **Document.** Update the requirement rows, the README source list and `CHANGELOG.md`. Run `/spec-check`.
