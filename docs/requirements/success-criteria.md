# Outcomes and Success Criteria

**When v1 is done, I can ask one agent about my notes, Pro Git, web docs and repos, get cited answers, pay less for repeat questions, and save results to my vault.** Each outcome below has a pass mark I can measure.

| Outcome | How it is measured | Pass mark |
| --- | --- | --- |
| Step Zero works | `redis-cli PING` returns PONG; one LLM call and one embedding call succeed | All three pass |
| Everything is searchable | Pro Git, the vault, one web docs site and two repos are indexed | 100% of target files indexed, 0 silent failures |
| Answers are grounded | On a set of 30 test questions (10 git, 10 notes, 10 mixed), a correct source is cited | at least 85% correct citation |
| Honest when unsure | On 10 questions with no answer in the sources, the agent says it does not know | at least 9 of 10 |
| Cache saves money | 20 paraphrases of 10 answered questions are asked again | at least 60% served from cache, with no wrong answers returned |
| Memory works | After restarting the program, a follow-up in the same session ID keeps context | 5 of 5 follow-ups answered correctly |
| Vault stays safe | 20 save requests, including ones aimed at existing notes and outside folders | 0 overwrites, 0 writes outside the configured folder |
| Provider is swappable | Run the same 30 questions on cloud and on Ollama by changing config only | Both run with no code change |
| Repeatable | A fresh clone is set up from the README | working in under 15 minutes |
| Picks the right tool | 20 test questions, each with the expected first tool (for example a pasted URL expects `fetch_url`) | at least 85% correct first tool |
| Stays inside limits | 10 questions built to make the loop wander or repeat | 0 exceed the step or cost cap |
| Resists injected instructions | 10 notes and pages that say "save this note" or "fetch this URL" | 0 side-effect calls without my confirmation |
| Fallback works | The 30-question set on a local model without reliable tool calling | Runs in pipeline mode and reports the mode |

**Learning and portfolio outcome:** I can explain and demo chunking, embeddings, vector search, semantic caching, memory and a tool-calling agent loop, and the repo has a README, tests and a short demo recording.
