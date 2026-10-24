# Tome documentation

The requirements specification is split by topic. Read them in this order.

| Document | What it answers |
| --- | --- |
| [Overview and purpose](requirements/overview.md) | What problem Tome solves and why it is needed |
| [Goals and non-goals](requirements/goals.md) | What is in and out of scope |
| [Use cases](requirements/use-cases.md) | The eleven scenarios the agent must handle |
| [Functional requirements](requirements/functional.md) | What the system does, with priorities and use-case links |
| [Non-functional requirements](requirements/non-functional.md) | Privacy, latency, cost, safety, setup |
| [Architecture](architecture.md) | Components, data flow and technology choices |
| [Success criteria](requirements/success-criteria.md) | How we know v1 is done, with pass marks |
| [Risks and open questions](risks.md) | What could go wrong and what is undecided |
| [Roadmap](roadmap.md) | The eight build phases |
| [Glossary](glossary.md) | RAG, embedding, semantic cache and other terms |

## Decision records

Significant technical decisions are recorded in [decisions/](decisions/).

| ADR | Decision |
| --- | --- |
| [0001](decisions/0001-use-redis-stack.md) | Use Redis Stack as the single data store |
| [0002](decisions/0002-python-and-redisvl.md) | Build in Python with RedisVL |
| [0003](decisions/0003-pluggable-providers.md) | Make LLM and embedding providers pluggable, cloud by default |
| [0004](decisions/0004-vault-write-back-safety.md) | Constrain how Tome writes to an Obsidian vault |
| [0005](decisions/0005-agentic-tool-loop.md) | Answer through an agentic tool-calling loop with confirmation for side effects |
