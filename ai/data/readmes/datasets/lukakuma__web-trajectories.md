---
license: other
license_name: mixed-per-source
license_link: LICENSE
language:
- en
- ko
pretty_name: Web Trajectories
task_categories:
- text-generation
tags:
- web-agent
- agent-trajectories
- tool-calling
- browser-automation
size_categories:
- 1K<n<10K
extra_gated_prompt: >-
  Raw web-agent trajectories built on public benchmark tasks (see per-source licenses).
  Access is reviewed manually. Please describe your intended use.
extra_gated_fields:
  Name: text
  Affiliation: text
  Intended use: text
  I will cite the original benchmarks and follow their licenses: checkbox
configs:
- config_name: sessions
  default: true
  data_files:
  - split: om2w
    path: data/sessions/om2w.parquet
  - split: webvoyager
    path: data/sessions/webvoyager.parquet
  - split: webbench
    path: data/sessions/webbench.parquet
  - split: canvas
    path: data/sessions/canvas.parquet
  - split: mind2web2
    path: data/sessions/mind2web2.parquet
- config_name: turns
  data_files:
  - split: om2w
    path: data/turns/om2w-*.parquet
  - split: webvoyager
    path: data/turns/webvoyager-*.parquet
  - split: webbench
    path: data/turns/webbench-*.parquet
  - split: canvas
    path: data/turns/canvas-*.parquet
  - split: mind2web2
    path: data/turns/mind2web2-*.parquet
- config_name: tools
  data_files:
  - split: train
    path: data/tools/tools.parquet
---

# Web Trajectories

Raw trajectories of an in-house DOM-based, tool-calling web agent, recorded while it ran public web-agent benchmarks on one host (2026-09 – 2026-10). This repo holds sessions that the benchmark judge marked **successful** and that **finished normally** (exit 0, no timeout, not blocked). The sibling repo [`lukakuma/web-trajectories-fail`](https://huggingface.co/datasets/lukakuma/web-trajectories-fail) holds the rest of the judged sessions.

Every LLM call keeps the exact input `messages` and the exact output blocks of the agent model; nothing is summarised or reformatted, the only edit is the scrub listed under *Caveats*. The tool definitions are the full schemas the model was offered, **restored from the agent's source code** because the run logs kept only names and description heads (see *Tool definitions*).

## Contents

| source (split) | origin | license | sessions | tasks | LLM calls |
|---|---|---|---:|---:|---:|
| `om2w` | [Online-Mind2Web](https://huggingface.co/datasets/osunlp/Online-Mind2Web) | CC-BY-4.0 | 7,191 | 288 | 289,371 |
| `webvoyager` | [WebVoyager](https://github.com/MinorJerry/WebVoyager) | Apache-2.0 | 823 | 134 | 23,658 |
| `webbench` | [WebBench](https://huggingface.co/datasets/Halluminate/WebBench) | MIT | 661 | 124 | 19,097 |
| `canvas` | In-house canvas tasks (Korean instructions) | CC-BY-4.0 | 162 | 54 | 3,373 |
| `mind2web2` | [Mind2Web 2 (dev set)](https://huggingface.co/datasets/osunlp/Mind2Web-2) | CC-BY-4.0 | 14 | 6 | 715 |
| **total** | | | **8,851** | **606** | **336,214** |

Agent models: `Qwen3.8-Flash-Next` 6,933, `Qwen3.8-27B` 1,427, `Qwen/Qwen3.6-27B-FP8` 374, `claude-opus-5-5` 75, `claude-sonnet-5-5` 31, `Qwen3.6-27B` 11. Instructions are English except `canvas` (Korean).

## Layout

Three configs; **splits are sources, not train/test** (no held-out split has been made).

| config | one row per | join key |
|---|---|---|
| `sessions` (default) | session (one agent run on one task) | `session_id` |
| `turns` | LLM call inside a session, in order | `session_id`, `turn_index` |
| `tools` | distinct tool-definition list | `tools_hash` |

```python
from datasets import load_dataset

sessions = load_dataset("lukakuma/web-trajectories", "sessions", split="om2w")
turns = load_dataset("lukakuma/web-trajectories", "turns", split="om2w")
tools = load_dataset("lukakuma/web-trajectories", "tools", split="train")

# one training example per call: input = messages (+ tools), target = response
import json
t = turns[0]
messages, response = json.loads(t["messages"]), json.loads(t["response"])
```

### `sessions`

| column | type | meaning |
|---|---|---|
| `session_id` | str | content fingerprint of the session's call log (duplicate copies on disk collapse to one row) |
| `source`, `task_id` | str | benchmark and its original task id (kept as the original string) |
| `rep`, `run` | int, str | repetition number and the benchmark run the session came from |
| `goal`, `start_url`, `domain`, `category` | str | instruction, start page, site, original stratum (om2w level, WebVoyager site, WebBench type) |
| `language`, `license` | str | instruction language; license of the source benchmark |
| `success` | bool | benchmark judge verdict (not the agent's self-report) |
| `completed` | bool | exit code 0, no timeout, not blocked |
| `judge_model`, `judge_mode`, `judge_prompt_version`, `judge_reason` | str | who judged, how, with which prompt version, and the judge's stated reason |
| `task_n_judged`, `task_n_success` | int | over all judged sessions of the same task on this host (a rough per-task pass rate) |
| `self_reported_success` | bool | the agent's own claim, for reference only |
| `agent_model`, `mode`, `harness_version`, `agent_version`, `git_head`, `src_tree` | str | **version stamp** of the agent and code |
| `system_prompt_hash`, `tools_hash`, `browser_arm`, `started_at` | str | prompt / tool-set version, browser setup, start time |
| `tools_restored_from`, `logged_tools_hash` | str | which code ref the tool definitions were restored from (`src_tree`, `git_head`, `tag`), and the logged list they restore |
| `n_llm_calls`, `n_act_turns`, `calls_by_purpose` | int, int, json | call counts (act / goal decomposition / plan tools / completion check …) |
| `in_tokens`, `out_tokens`, `max_turn_in_tokens` | int | token totals (agent tokenizer) and the longest single input |
| `wall_s`, `llm_s`, `tool_s` | float | wall time, time in LLM calls, time in tools |
| `n_compactions` | int | how many times older observations were rewritten (see *Turn format*) |
| `final_report`, `final_url` | str | the agent's final report text and last page URL |
| `copies_on_disk` | int | identical copies found (e.g. rescoring runs copy sessions) |

### `turns`

| column | type | meaning |
|---|---|---|
| `session_id`, `turn_index`, `step`, `ts` | str, int, int, str | order inside the session |
| `purpose` | str | `act`, `decompose_goal`, `plan_tool:*`, `completion_verify`, `text_only` …; null when the session has no purpose log |
| `model` | str | model that served the call |
| `messages` | json str | **the exact input** of the call (OpenAI-style list incl. system prompt and tool results) |
| `tools_hash` | str | tool definitions offered on this call (→ `tools`); null for calls without tools |
| `response` | json str | the exact output blocks (`text`, `tool_call` with `name` and JSON `input`) |
| `in_tokens`, `out_tokens`, `cache_tokens`, `latency_s` | int, float | per-call usage |
| `extends_previous` | bool | this input = previous tool-bearing input (minus its trailing hint) + new messages |
| `action_ok` | bool | every tool call of this turn returned success (false if any failed; null if unknown) |
| `role` | str | what the call is, read from its content (see *Call roles*) |
| `tool_names` | list[str] | tools called in `response`, in order |

### Call roles

`role` is derived from each call's content, so it is filled for every row (the runner's own `purpose` label is missing for about a quarter of rows and files report writing under `act` or `text_only` depending on the version). Where `purpose` exists the two agree on 95.7% of rows; the rest is almost entirely report writing.

| role | rule | share |
|---|---|---:|
| `act` | an environment tool was called (planning calls may be batched with it) | 78.3% |
| `plan` | only plan tools: `create_plan`, `update_subtask_state`, `finish_subtask`, `finish_plan`, `view_subtasks` | 12.6% |
| `report` | `write_report` (optionally with plan tools) | 4.0% |
| `decompose` | no tools offered; system prompt starts “You are a planning assistant” | 2.6% |
| `verify` | no tools offered; system prompt is the completion auditor | 2.4% |
| `text` | tools offered, none called | 0.1% |

### `tools`

`tools_hash`, `n_tools`, `tool_names`, `tools` (the full JSON list in the order offered — restored, see *Tool definitions*), `logged_tools_hash` (ids of the logged name + description lists it restores).

## Tool definitions

The run logs kept each offered tool only as its name and the first 200 characters of its description; the parameter schemas were not logged. `tools` here holds the **full definitions, restored from the agent's source code**:

1. Every session records the code it ran: `src_tree` (git tree of the source, frozen for benchmark sweeps) or else `git_head`. Runs launched from an installed release report the launcher checkout's HEAD, so the release tag of `agent_version` is tried last.
2. For each session the tool list was rebuilt from that code the way the agent builds it (it depends only on which methods the web environment has, so no browser is needed) and serialised as sent to the model.
3. A rebuild was accepted only if the tool names, their order and every description's first 200 characters equal the log. **8,851 of 8,851 sessions matched** (8,247 by `src_tree`, 162 by `git_head`, 442 by release tag); `tools_restored_from` says which.

What this does and does not establish: names, order and description heads are checked against the log; parameter schemas cannot be (the log did not keep them) and come from the matched code. Restoring per session matters: within one logged list the code versions produced up to three variants (they differ past the 200 characters the log kept). The one input-dependent schema part — `write_report` gains a `data` argument when a run declares an output schema — was checked separately: no `write_report` call in either repo passes `data`. The scrub below applies to the definitions too, and `logged_tools_hash` keeps the id of the logged name + description list each set restores.

## Turn format

- Each call's `messages` repeats the conversation so far. About 95% of tool-bearing calls extend the previous input exactly (`extends_previous=true`), so consecutive turns can be packed into one sequence.
- The last message of most inputs is a one-off `<system-hint>` user message; it is dropped from the next input.
- When a newer observation arrives, older tool results are rewritten to a short stub (`[관측 축약: 최신 관측으로 대체됨 — url=…]`, Korean for “observation shortened: replaced by the latest one”). These rewrites break the prefix and are counted in `n_compactions`.
- Inputs are long: in the success set the per-call input median is about 26k tokens, p95 about 40k, max about 107k (agent tokenizer). Inputs are text only (DOM observations); screenshots are not part of the model input and are not included.

## How the data was selected

1. Every folder with a call log under the host's benchmark and console output directories was scanned.
2. Copies of the same session (identical call log) were collapsed; the most recent judgment wins.
3. Quarantined runs (`_VOID_`), sessions without a judgment, judge errors and **BrowseComp** (every row carries a canary: “BENCHMARK DATA SHOULD NEVER APPEAR AS PLAIN TEXT ONLINE”) were dropped.
4. Success set = `success and completed`; everything else judged goes to the fail repo.

## Caveats

- **Single judge.** Each verdict comes from one benchmark judge run (mostly `Qwen3.8-27B`); nothing was re-judged. Where the same session was judged twice the verdicts agreed 96.8% of the time (2,968 sessions). Successes on tasks with a low `task_n_success / task_n_judged` are more likely to be judge errors.
- **No held-out split.** Tasks come from public benchmarks; a model trained on this data cannot be evaluated fairly on the same tasks.
- **Uneven per-task counts.** Some Online-Mind2Web tasks have 50+ sessions, others one. Sample per task for diversity.
- **Mixed versions.** Several system-prompt and tool-list versions over the period; filter with the version columns.
- **Model outputs, not gold labels.** Successful sessions still contain failed actions, retries and loops (`action_ok`).
- **Korean** instructions only in `canvas`.
- **Scrub.** Local session paths inside tool results were replaced with `<session>/…`, other local paths with `<path>`, the home directory with `~`, internal product identifiers with `agent`, and test-account secrets with `[REDACTED]`. A scan for private IPs, API keys, tokens and JWTs left only text of the public pages visited (a URL slug such as `sk-broadband-…`, a site user name, a private-range address inside a public page's link, a random page token) — no credentials. E-mail addresses that appear are text of the public pages visited.
- **Third-party page text.** Observations contain text of the visited public websites as of the run date.

## Licenses and attribution

Each row carries the license of its source benchmark (`license`). Please cite the original benchmarks: Online-Mind2Web (Xue et al., 2025, arXiv:2504.01382), WebVoyager (He et al., 2024), WebBench (Halluminate), Mind2Web 2 (Gou et al., 2025, arXiv:2506.21506). Online-Mind2Web states it was released for research purposes.
