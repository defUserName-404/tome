---
description: Create the next architecture decision record from the template
argument-hint: <short decision title>
---

Create an ADR titled "$ARGUMENTS". If the title is empty, ask me for it.

1. List `docs/decisions/` and use the next four-digit number. The file name is `NNNN-kebab-case-title.md`.
2. Use `docs/decisions/0005-agentic-tool-loop.md` as the model. Sections: title line `# NNNN. <Title>`, then Status (`Proposed`), Date (today), Context, Decision, Consequences (Good and Costs), Alternatives considered (a table with a "Why not now" column). Keep it to one page.
3. Ask me for any context or reasons you do not already have. Do not invent alternatives or trade-offs.
4. Add a row to the ADR table in `docs/README.md`.
5. Add a line under Unreleased in `CHANGELOG.md`.
6. If the decision changes a requirement, update `docs/requirements/` in the same change.
7. Run `python scripts/check_spec.py` and fix anything it reports.

Never edit the Decision of an accepted ADR. To reverse one, write a new ADR and mark the old one `Superseded by NNNN`.
