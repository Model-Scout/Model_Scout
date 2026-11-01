---
license: other
license_name: mixed-per-source
license_link: LICENSE
language:
- en
- ko
pretty_name: Web Trajectories SFT
task_categories:
- text-generation
tags:
- web-agent
- agent-trajectories
- tool-calling
- sft
size_categories:
- 100K<n<1M
extra_gated_prompt: >-
  Training selections of raw web-agent trajectories built on public benchmark tasks (see per-source licenses).
  Access is reviewed manually. Please describe your intended use.
extra_gated_fields:
  Name: text
  Affiliation: text
  Intended use: text
  I will cite the original benchmarks and follow their licenses: checkbox
configs:
- config_name: cap3
  default: true
  data_files:
  - split: train
    path: data/cap3/*.parquet
  - split: test
    path: data/test/*.parquet
- config_name: cap1
  data_files:
  - split: train
    path: data/cap1/*.parquet
  - split: test
    path: data/test/*.parquet
- config_name: all
  data_files:
  - split: train
    path: data/all/*.parquet
  - split: test
    path: data/test/*.parquet
- config_name: tasks
  data_files:
  - split: tasks
    path: data/index/tasks.parquet
- config_name: sessions
  data_files:
  - split: sessions
    path: data/index/sessions.parquet
---

# Web Trajectories SFT

Supervised fine-tuning selections built from [`lukakuma/web-trajectories`](https://huggingface.co/datasets/lukakuma/web-trajectories) (judged-successful, completed sessions of a DOM-based, tool-calling web agent). One row = one LLM call: the exact input (`messages`, with the full `tools` definitions restored from the agent's source code — see the raw repo's *Tool definitions*) and the exact output (`response`). The agent's own calls of every kind are included (actions, planning tools, goal decomposition, completion check), because the target model is meant to take all of them over.

## Configs

| config | what is in `train` | tasks | sessions | rows (LLM calls) | rows with `train_target=false` |
|---|---|---:|---:|---:|---:|
| `cap1` | best session per task | 496 | 496 | 14,986 | 379 |
| `cap3` (default) | best + up to 2 more that took a different path | 496 | 1,291 | 45,680 | 3,145 |
| `all` | every session that passed the filter | 496 | 7,187 | 265,946 | 22,664 |
| `test` split (shared) | held-out tasks, picked like `cap3` | 85 | 234 | 8,250 | 649 |

Four training variants come out of three configs:

| variant | config | loss |
|---|---|---|
| A | `cap1` | all assistant outputs |
| B | `cap3` | all assistant outputs |
| C | `all` | all assistant outputs |
| D | `cap3` | skip outputs of rows with `train_target = false` (the turn's tool call failed, or it repeated the previous call exactly) — the row stays in context |

Index configs: `tasks` (every task with `split` and `held_out_by`) and `sessions` (each selected session with its pick rank and the quality numbers used to rank it).

```python
from datasets import load_dataset
import json

train = load_dataset("lukakuma/web-trajectories-sft", "cap3", split="train")
test = load_dataset("lukakuma/web-trajectories-sft", "cap3", split="test")
row = train[0]
messages, tools, target = json.loads(row["messages"]), json.loads(row["tools"] or "[]"), json.loads(row["response"])
use_loss = row["train_target"]  # variant D only
```

## Columns

| column | type | meaning |
|---|---|---|
| `session_id`, `turn_index` | str, int | session (join key to the raw repo) and call order |
| `segment_id` | int | consecutive rows of a session whose inputs extend each other (see *Packing*) |
| `source`, `task_id`, `domain`, `category`, `language` | str | benchmark, task, start site, original stratum, instruction language |
| `purpose` | str | `act`, `decompose_goal`, `plan_tool:*`, `completion_verify`, `text_only` …; null where the source session had no purpose log |
| `messages` | json str | exact model input (system prompt, task, history, tool results, one-off hint) |
| `tools` | json str | full tool definitions offered on this call (restored from the code the session ran; the logs kept only names + description heads); null for calls without tools |
| `response` | json str | exact model output blocks (`text`, `tool_call` with `name` and JSON `input`) |
| `train_target` | bool | false if this turn's tool call failed or exactly repeated the previous call |
| `action_ok` | bool | every tool call of this turn returned success (null = unknown) |
| `in_tokens`, `out_tokens` | int | usage recorded at run time (agent tokenizer) |
| `role` | str | `act` / `plan` / `report` / `decompose` / `verify` / `text`, read from the call's content (see below) |
| `tool_names` | list[str] | tools called in `response`, in order |

### Call roles

`role` is derived from each call's content, so it is filled for every row (the runner's own `purpose` label is missing for about a quarter of rows and files report writing under `act` or `text_only` depending on the version). Where `purpose` exists the two agree on 95.7% of rows; the rest is almost entirely report writing.

| role | rule | share |
|---|---|---:|
| `act` | an environment tool was called (planning calls may be batched with it) | 77.7% |
| `plan` | only plan tools: `create_plan`, `update_subtask_state`, `finish_subtask`, `finish_plan`, `view_subtasks` | 12.9% |
| `report` | `write_report` (optionally with plan tools) | 4.1% |
| `decompose` | no tools offered; system prompt starts “You are a planning assistant” | 2.7% |
| `verify` | no tools offered; system prompt is the completion auditor | 2.6% |
| `text` | tools offered, none called | 0.1% |

To train on one role only, filter rows by `role` (e.g. `decompose` alone, or everything except `verify`).

## How the selections were made

1. **Test tasks first.** Whole start sites with at most 5 tasks were held out until about 5% of tasks (English web sources only; 32 tasks), then every 10th task per source in category order (57 tasks). Test tasks never appear in any `train` split.
2. **Session filter** (applied to train and test): drop a success that is the only one on a task whose success rate is below 20% (likely judge error), sessions with more than 2x the task's median action turns, and sessions with more than 25% failed actions.
3. **Per task.** Rank by failed-action share + repeated-call share, then closeness to the task's median length. `cap1` takes the first; `cap3` adds up to two more by farthest-point selection on the set of tools and URLs used (Jaccard distance ≥ 0.2).
4. **Site balance** (`cap1`, `cap3` train): at most 30 sessions per start site; later picks are dropped first, never a task's first pick.
5. `all` keeps every filtered session (no cap, no balance).

## Packing

Within a `segment_id`, each row's input is the previous row's input minus its trailing one-off `<system-hint>`, plus the previous response and its tool results. Rows can be trained one by one (exact), or a segment can be packed into one sequence (the last row's `messages` + `response`, loss on every assistant turn); packing drops the one-off hints the earlier rows saw unless they are kept with attention masking. `cap3` has 9,143 segments for 45,680 rows. Inputs run up to about 107k tokens (agent tokenizer), so a 128k context holds every row.

## Caveats

- Everything listed in the raw repo's card applies (single judge, scrub rules, third-party page text).
- Test tasks come from the same public benchmarks; they are held out from training here, not unseen by the agent that produced them.
- Prompt versions: the action-turn policy is one version for all English sessions and one for the Korean `canvas` sessions; the tool list varies by 1–4 tools over the period (54 tools are in every version); across code versions `open_url` has two parameter schemas and `observe_more` / `fill_input` have several descriptions.
- `canvas` (Korean) is small; it is not up-weighted.

## Licenses and attribution

| source | origin | license | train rows (`cap3`) |
|---|---|---|---:|
| `om2w` | [Online-Mind2Web](https://huggingface.co/datasets/osunlp/Online-Mind2Web) | CC-BY-4.0 | 28,484 |
| `webvoyager` | [WebVoyager](https://github.com/MinorJerry/WebVoyager) | Apache-2.0 | 7,870 |
| `webbench` | [WebBench](https://huggingface.co/datasets/Halluminate/WebBench) | MIT | 7,451 |
| `canvas` | In-house canvas tasks (Korean instructions) | CC-BY-4.0 | 1,279 |
| `mind2web2` | [Mind2Web 2 (dev set)](https://huggingface.co/datasets/osunlp/Mind2Web-2) | CC-BY-4.0 | 596 |

Please cite the original benchmarks: Online-Mind2Web (Xue et al., 2025, arXiv:2504.01382), WebVoyager (He et al., 2024), WebBench (Halluminate), Mind2Web 2 (Gou et al., 2025, arXiv:2506.21506).
