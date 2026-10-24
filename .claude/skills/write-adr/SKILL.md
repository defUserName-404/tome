---
name: write-adr
description: When and how to write an architecture decision record for Tome. Use when a change affects the data store, dependencies, provider behaviour, the tool set, or any safety rule.
---

# Write an ADR

## Write one when a change

- replaces or adds a data store, service or framework,
- changes how providers are chosen or how the index depends on them,
- adds, removes or changes the permissions of an agent tool,
- relaxes or adds a safety rule (vault writes, confirmation, untrusted content),
- or would be hard to reverse once code depends on it.

Do not write one for a bug fix, a refactor, or a choice that is easy to change later.

## How

1. Run `/new-adr <title>`. It numbers the file, applies the structure and updates the index.
2. Keep it to one page: Context (why now), Decision (what, in short bullets), Consequences (good and costs), Alternatives considered (why not now).
3. Ground it in facts from the requirements and the conversation. Do not invent alternatives or numbers.
4. Link the requirements it affects (FR, NFR) and update them in the same pull request.
5. Status moves `Proposed`, then `Accepted`. To reverse a decision, write a new ADR and mark the old one `Superseded by NNNN`. Never rewrite the Decision section of an accepted ADR.
6. Run `/spec-check`.
