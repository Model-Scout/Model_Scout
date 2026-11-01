---
license: cc-by-4.0
language:
- ko
task_categories:
- text-generation
tags:
- benchmark
- tool-use
- function-calling
- agent
- korean
size_categories:
- n<1K
configs:
- config_name: test
  data_files:
  - split: test
    path: tasks/test.jsonl
- config_name: dev
  data_files:
  - split: dev
    path: tasks/dev.jsonl
---

# kotraj-bench

A Korean agentic tool-use benchmark. 340 tasks across three domains, evaluated against a deterministic mock environment with a fixed user simulator.

Scoring is entirely code — no LLM judge. A task succeeds only if the required tool calls were made, in the required order, with arguments matching the specification, and the environment reached the required terminal state.

## Splits

| Split | Tasks | Purpose |
| --- | --- | --- |
| `test` | 290 | Reporting |
| `dev` | 50 | Prompt and harness tuning |

| Domain | test | | Case pattern | test |
| --- | --- | --- | --- | --- |
| travel | 100 | | multi_turn | 101 |
| calendar | 99 | | sequential | 90 |
| commerce | 91 | | parallel | 40 |
| | | | no_call | 30 |
| | | | single | 29 |

`no_call` tasks are ones where the correct behavior is to **not** call a tool — out-of-scope requests, or questions answerable directly. See the warning under Results.

## Baselines

290 tasks × 3 runs = 870 rollouts per model, against the same frozen environment and user simulator (`env_lock.json`). All four measured 2026-08-29 – 08-31.

| Model | Params | pass@1 | pass^3 | pass_any | Avg turns | Tool precision |
| --- | --- | --- | --- | --- | --- | --- |
| [kotraj-qwen3.5-2B](https://huggingface.co/drlee1/kotraj-qwen3.5-2B) | 1.9B | **0.746** | **0.597** | **0.869** | 4.61 | **0.941** |
| Qwen3.5-2B | 1.9B | 0.514 | 0.307 | 0.707 | 4.94 | 0.916 |
| gemma-4-E2B-it | ~2B | 0.288 | 0.172 | 0.441 | 7.15 | 0.476 |
| LFM2.5-1.2B-Instruct | 1.2B | 0.262 | 0.214 | 0.331 | 7.00 | 0.792 |

`pass^3` = correct on all three runs. `pass_any` = correct on at least one.

McNemar's test against Qwen3.5-2B on `pass^3`:

| Model | gained | lost | p |
| --- | --- | --- | --- |
| kotraj-qwen3.5-2B | 102 | 18 | **3.5e-14** |
| gemma-4-E2B-it | 27 | 66 | 8.1e-05 (worse) |
| LFM2.5-1.2B-Instruct | 31 | 58 | 5.9e-03 (worse) |

`env_lock.json` holds hashes of the schemas, mock implementation, and prompts. Verify it before comparing against these numbers — if any hash differs, you are measuring a different benchmark. Note that it does **not** hash the harness code; see Limitations.

### Read `no_call` separately

| Case | kotraj-qwen3.5-2B | Qwen3.5-2B | gemma-4-E2B-it | LFM2.5-1.2B |
| --- | --- | --- | --- | --- |
| single | **0.782** | 0.586 | 0.172 | 0.529 |
| multi_turn | **0.706** | 0.409 | 0.181 | 0.158 |
| sequential | **0.767** | 0.496 | 0.207 | 0.070 |
| parallel | **0.842** | 0.600 | 0.325 | 0.267 |
| **no_call** | 0.656 | 0.733 | **0.956** | 0.922 |

gemma-4 scores 0.956 on `no_call` and 0.181 on `multi_turn`; LFM2.5 scores 0.922 and 0.158. Both rarely call tools — their conversations average 7.0–7.2 turns against kotraj's 4.61, answering in text instead of acting. **A model that never calls a tool scores near-perfectly on `no_call` and near zero everywhere else.**

`no_call` is also the one case where the base model beats the fine-tuned one (0.733 vs 0.656), and at 30/290 tasks it moves the headline number.

**Do not report a single aggregate without the case breakdown.**

### By domain

| Domain | kotraj-qwen3.5-2B | Qwen3.5-2B | gemma-4-E2B-it | LFM2.5-1.2B |
| --- | --- | --- | --- | --- |
| calendar | **0.694** | 0.512 | 0.343 | 0.229 |
| commerce | **0.667** | 0.407 | 0.205 | 0.275 |
| travel | **0.870** | 0.613 | 0.310 | 0.283 |

### Failure composition

| | kotraj | Qwen3.5-2B | gemma-4 | LFM2.5 |
| --- | --- | --- | --- | --- |
| `parse_failure` | 0.005 | 0.014 | 0.000 | 0.017 |
| `schema_violation` | 0.002 | 0.003 | 0.000 | **0.071** |
| `sim_fault` | 0.028 | 0.048 | **0.106** | 0.063 |

LFM2.5's `schema_violation` rate is 20–35× the Qwen-family models' — genuine argument errors, not a parser artifact. gemma-4's `sim_fault` is highest because it so often answers in text that the user simulator runs out of turns.

## What a task contains

```json
{
  "id": "s1_20260803-1250_b0069_3",
  "domain": "commerce",
  "case_pattern": "single",
  "task": "기존 주문 ORD0001의 취소 가능 여부를 확인하고 취소 진행을 원한다.",
  "initial_message": "나 예전에 삼다수 시켰던 거 있잖아, ORD0001. 그거 아직 취소 되나?",
  "persona": {"연령대": "30대", "격식": "반말", "스타일": "급함", "지역 맥락": "대전·충청 생활권"},
  "hidden_info": {},
  "success_criteria": {"required_calls": [{"name": "get_order_status", "args_subset": {"order_id": "ORD0001"}}]},
  "tools_subset": ["search_products", "get_order_status", "cancel_order"],
  "seed": 1434659138,
  "split": "test"
}
```

| Field | Description |
| --- | --- |
| `initial_message` | The user simulator's opening turn |
| `persona` | Register, urgency, region, digital literacy — drives how the simulator responds |
| `hidden_info` | Facts the simulator reveals only when asked |
| `success_criteria` | Required calls, argument constraints, ordering, terminal-state conditions |
| `tools_subset` | Tools exposed for this task |
| `seed` | Mock environment seed — the environment is reproducible from this alone |

## Contamination control

The benchmark was curated from a task pool disjoint from the [training data](https://huggingface.co/datasets/drlee1/kotraj), then filtered in both directions.

| | |
| --- | --- |
| Method | char-5gram MinHash (num_perm=128), Jaccard similarity |
| Near-duplicate threshold | 0.85 |
| Structural + text threshold | 0.60 |
| Benchmark tasks checked | 340 |
| Training tasks checked | 11,744 |
| **Collisions** | **0** |
| Max similarity observed | 0.25 |
| Similarity p50 / p90 / p99 | 0.086 / 0.148 / 0.203 |

484 candidates were generated; 340 kept. One was dropped for exact text match against training data; the rest were dropped to hold the domain and case-pattern quotas.

MinHash was chosen over embedding similarity deliberately: it is reproducible without a model dependency, so anyone can re-run the audit and get identical numbers. `contamination_audit.json` contains the full record, including the dropped sample.

A reverse filter also runs during data synthesis, so new training data cannot drift into the benchmark.

## Metrics

| Metric | Definition |
| --- | --- |
| `goal_success` | All `required_calls` satisfied, in order, with matching arguments, and terminal state matches |
| `pass@1` | Fraction of (task, run) pairs that succeed |
| `pass^k` | Fraction of tasks correct on **all** k runs — reliability, not best-of |
| `tool_precision` | Successful calls / total calls |
| `format_violation` | Union of the two below, kept for comparability with earlier reports |
| `parse_failure` | Model output could not be parsed as a tool call |
| `schema_violation` | Call parsed, but arguments failed JSON Schema validation |
| `sim_fault` | Failure attributable to the user simulator, not the agent |

`sim_fault` ran 0.028–0.106 across the four baselines. Treat it as the harness noise floor: differences smaller than that are not meaningful.

Truncation (turn or call cap reached) and repeated format failures count as hard failures regardless of criteria satisfaction. A conversation cut off mid-task is not a success.

## Limitations

- **Three domains, 30 mock tools.** Results do not predict behavior on unseen tool schemas.
- **Synthetic tasks.** Generated with an Upstage-family model, then filtered by rule gates. Not sampled from real user traffic.
- **The user simulator is an LLM.** It is pinned to temperature 0 and hashed in `env_lock.json`, but it is not a real user, and `sim_fault` is not zero.
- **`no_call` rewards inaction** (see above).
- **Not saturated.** The best baseline reaches pass^3 0.597. Headroom remains, but the benchmark is no longer in the regime where every model looks equally bad.
- **Tool-call formats differ by model family.** Each model emits calls in the format it was trained on, and untyped formats (Qwen's `<parameter=K>V</parameter>`, Gemma 4's `k: v`) carry no type information — you must coerce values back to the schema-declared type. A harness that gets either wrong measures itself, not the model.
- **`env_lock.json` does not hash the harness code.** It pins the schemas, mock environment, and prompts, so it cannot detect a scoring or parsing change. Pin the harness commit alongside the lock.
- **The per-turn tool-round cap is a hard failure, and it penalises tool-using models only.** Six consecutive tool rounds within one user turn terminates the trajectory and fails it regardless of criteria satisfaction. This costs `Qwen3.5-2B` 129 rollouts (14.8%) and `kotraj-qwen3.5-2B` 54 (6.2%) that had met every success criterion — and costs gemma-4 and LFM2.5 **nothing**, because they rarely chain calls at all. `sequential` tasks require up to 6 calls, so the cap binds exactly where the tasks are hardest. Raise it if you are measuring long chains.

## License

CC-BY-4.0.

## Citation

```bibtex
@misc{kotrajbench2026,
  title  = {kotraj-bench: A Korean Agentic Tool-Use Benchmark},
  author = {DONGRYEOL LEE},
  year   = {2026},
  url    = {https://huggingface.co/datasets/drlee1/kotraj-bench}
}
```

## Related

- **[drlee1/kotraj](https://huggingface.co/datasets/drlee1/kotraj)** — the training dataset this benchmark is filtered against
- **[drlee1/kotraj-qwen3.5-2B](https://huggingface.co/drlee1/kotraj-qwen3.5-2B)** — a model fine-tuned on that dataset, evaluated above
