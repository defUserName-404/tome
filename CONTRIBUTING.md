# Contributing to Tome

Thanks for your interest. Tome is early: the requirements are written and the implementation is starting. Read [docs/requirements](docs/requirements/) first so changes line up with the spec.

## Setup

```bash
docker compose up -d
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env
```

## Before you open a pull request

```bash
ruff check .
pytest
```

CI runs the same two commands on Python 3.11 and 3.12.

## Workflow

- Branch from `main`; one topic per pull request.
- Write commit messages in the imperative: `Add heading-based chunker`.
- Reference the requirement you are implementing, for example `FR-05`, in the pull request description.
- Add or update tests with the change. Tests must not need network access or a running Redis unless they are marked as integration tests.

## Changing the spec

- Requirements live in `docs/requirements/`. Edit them in the same pull request as the code that changes behaviour.
- A significant technical decision gets a short record in `docs/decisions/`, numbered in order (`0006-...`). Say what was decided, why, and what you gave up.

## Safety rules for the Obsidian write-back

Anything that writes to a vault must follow [ADR 0004](docs/decisions/0004-vault-write-back-safety.md): one configured folder, never overwrite, preview and confirm first. Tools with side effects follow [ADR 0005](docs/decisions/0005-agentic-tool-loop.md): the user confirms every call.

## Secrets

Never commit API keys or `.env`. Use `.env.example` to document new settings.
