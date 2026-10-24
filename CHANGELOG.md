# Changelog

All notable changes are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project aims to follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added

- Requirements specification split into `docs/requirements/`: overview, goals, use cases, functional and non-functional requirements, success criteria.
- Architecture overview, risks, roadmap and glossary.
- Architecture decision records for Redis Stack, Python with RedisVL, pluggable providers and vault write-back safety.
- Project scaffold: Docker Compose for Redis Stack, Python package stub, smoke test, CI workflow, issue and pull request templates.
- ADR 0005 and FR-34 to FR-40: an agentic tool-calling loop with step and cost limits, confirmation for side effects, untrusted-content handling and a fixed-pipeline fallback.
- Use cases UC10 and UC11, NFR-13 to NFR-15, and matching success criteria and risks.

### Changed

- Roadmap is now eight phases, with the agent loop as phase 3.
- Architecture diagram shows the tool loop.
- FR-12, FR-16, NFR-01 and NFR-05 reworded for the agent loop.
