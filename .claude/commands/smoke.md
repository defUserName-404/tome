---
description: Run the Step Zero smoke test and report what passed, failed or was skipped
allowed-tools: Bash(python scripts/smoke_test.py:*), Bash(docker compose ps:*)
---

Check that the local environment works.

1. Run `docker compose ps`. If the `tome-redis` container is not running, say so and tell me to run `docker compose up -d`; do not continue.
2. Run `python scripts/smoke_test.py`.
3. Report each line as ok, FAIL or skip, in a short table. For every FAIL, give the likely cause and the fix (for example the Redis URL in `.env`, or the search module missing because a plain Redis image is running).
4. Remind me which checks are still skipped (LLM and embeddings until the provider adapters exist).

Do not edit files and do not print the contents of `.env`.
