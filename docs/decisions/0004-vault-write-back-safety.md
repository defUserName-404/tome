# 0004. Constrain how Tome writes to an Obsidian vault

- Status: Accepted
- Date: 2026-10-24

## Context

Tome can save answers as notes in an Obsidian vault (use case UC9). A vault is personal and often unbacked-up, so a bug or a bad path must not damage it. Notes written by Tome could also be retrieved later and mistaken for the user's own thinking.

## Decision

All vault writes follow these rules:

1. Write only inside one configured folder, `Inbox/AI/` by default. Refuse any other path (FR-25).
2. Never overwrite an existing note. Create a new file, or append after confirmation (FR-26).
3. Show a preview and ask for confirmation before writing. Support a dry-run flag (FR-27).
4. Add frontmatter to every written note: `source: ai`, date, tags, and links to the cited notes (FR-28).
5. Index written notes, labelled as AI-generated so they rank below the user's own notes (FR-29).
6. Write new files with unique, timestamped names, so sync tools such as iCloud or Obsidian Sync do not create conflicts.
7. Log every write.

Writes use direct file access, which works with Obsidian closed. An Obsidian MCP or Local REST API can be added later as an option, under the same rules.

## Consequences

- Safe by default, at the cost of one confirmation step per save.
- Retrieval needs a rule to down-rank notes with `source: ai`.
- Success criterion: 0 overwrites and 0 writes outside the folder across 20 test saves.

Related: NFR-08, risks "Write-back overwrites or clutters my vault" and "AI-written notes are retrieved later as if they were my own thinking".
