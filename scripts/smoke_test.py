"""Step Zero smoke test: verify the environment before building on it.

Checks Redis Stack (PING and the search module). LLM and embedding checks are
added with the provider adapters (see docs/roadmap.md, phase 0).
"""

import os
import sys

import redis


def check_redis(url: str) -> bool:
    client = redis.Redis.from_url(url)
    try:
        client.ping()
    except redis.RedisError as exc:
        print(f"FAIL redis: cannot PING {url} ({exc})")
        return False
    print("ok   redis: PING -> PONG")

    try:
        client.execute_command("FT._LIST")
    except redis.ResponseError as exc:
        print(f"FAIL redis: search module not available ({exc})")
        return False
    print("ok   redis: search module loaded")
    return True


def main() -> int:
    url = os.environ.get("REDIS_URL", "redis://localhost:6379")
    results = [check_redis(url)]
    print("skip llm: no provider adapter yet")
    print("skip embeddings: no provider adapter yet")
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
