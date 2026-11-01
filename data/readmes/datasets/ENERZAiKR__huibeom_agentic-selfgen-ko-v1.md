---
license: cc-by-4.0
task_categories:
  - text-generation
language:
  - ko
  - en
tags:
  - function-calling
  - tool-use
  - agent
  - reasoning
  - korean
  - multi-turn
  - cross-app
  - synthetic
  - verified
size_categories:
  - 10K<n<100K
configs:
  - config_name: default
    data_files:
      - split: train
        path: "data/*.jsonl"
  - config_name: single_app
    data_files:
      - split: train
        path: "data/single-*.jsonl"
  - config_name: cross_app
    data_files:
      - split: train
        path: "data/cross-*.jsonl"
---

# agentic-selfgen-ko-v1

**24,515 Korean agentic trajectories, generated inside a live executable environment and kept only
when every turn passed a deterministic state check.** Nothing here is imagined: a user-simulator LLM
speaks Korean, the agent LLM calls tools, the tools **actually execute** against AppWorld's app
backends (SQLite state), observations come from the environment — never from a model — and after each
user turn a runner-side check verifies the database state (or the reply's facts) against the goal. A
turn that fails is retried once with the environment intact; if it still fails, the whole episode is
dropped. What remains is behaviour that verifiably worked.

The corpus now has **two complementary parts**:

| part | rows | shape | config |
|---|---:|---|---|
| **single-app** | 5,835 | deep single-domain episodes, 6–9 user sub-goals (mean 7.49) | `single_app` |
| **cross-app** | 18,680 | two apps woven together: read a value in app A, act on it in app B (mean 2.81 user turns) | `cross_app` |
| **total** | **24,515** | | `default` |

Load everything with the `default` config, or either part on its own:

```python
from datasets import load_dataset
ds  = load_dataset("HBKenerzai/agentic-selfgen-ko-v1", split="train")                      # all 24,515
sgl = load_dataset("HBKenerzai/agentic-selfgen-ko-v1", "single_app", split="train")        # 5,835
crs = load_dataset("HBKenerzai/agentic-selfgen-ko-v1", "cross_app",  split="train")        # 18,680
```

## Part 1 — single-app (5,835)

Deep episodes inside one app, 6–9 user sub-goals planned one at a time from the **live** environment
state, spoken by a persona-conditioned Korean user simulator (존댓말/반말 mix across episodes). The
agent discovers credentials itself (supervisor app → profile/passwords → login; phone uses the phone
number as username), so realistic auth flows — including 401-and-recover — appear naturally.

| file | rows | domain | verified by |
|---|---:|---|---|
| `single-simple_note.jsonl` | 2,084 | notes: create, append, pin, delete, content/count Q&A | note records and contents |
| `single-todoist.jsonl` | 1,673 | projects/tasks: create, complete, delete, count | task & project records, completion flags |
| `single-phone.jsonl` | 1,365 | SMS to real in-world contacts, contacts, alarms, number Q&A | sent-message / contact / alarm records |
| `single-venmo.jsonl` | 713 | money transfers, payment requests, balance Q&A | transaction record (receiver name + amount) **and** exact balance delta |

## Part 2 — cross-app (18,680)

Each episode weaves **two apps**: the agent reads a concrete value in one app (a contact's number, a
balance, a task count, a note's items) and must use it in another — e.g. look up a task that says
"send Gina 7.5 dollars", then actually send 7.5 dollars in the money app. The runner checks **both
apps' state** deterministically (the note now contains the number; the transaction exists with the
right receiver and amount **and** the balance moved by exactly that much).

| file | rows | pattern |
|---|---:|---|
| `cross-todoist_venmo.jsonl` | 3,998 | a task "send N dollars to X" → an actual money transfer to X |
| `cross-venmo_note.jsonl` | 3,994 | read the balance → record it in a note |
| `cross-todoist_note.jsonl` | 3,882 | count open tasks → write the count into a note |
| `cross-note_todoist.jsonl` | 3,437 | read a note's items → create the matching Todoist tasks |
| `cross-phone_note.jsonl` | 3,369 | look up a contact's number → save it in a note |

Two things the single-app part does not have:

- **Pre-login variety.** 40% of cross episodes start **already authenticated** — the relevant
  `access_token`s are provided in the system prompt and the agent calls the feature functions
  directly, instead of repeating the full supervisor login dance every time. The other 60% perform
  the login flow. (`meta.prelogin` marks which.)
- **De-duplicated sub-goals.** Repeated identical user utterances are blocked at generation
  (`seen_utt`), so no episode asks the same thing twice.

## What an episode looks like

- Every assistant round carries Korean reasoning in `reasoning_content` (prefill-enforced,
  quoted-content-aware style gate), alongside `content` and `tool_calls`. Reasoning coverage is 100%.
- Tool catalog per episode is distractor-augmented (supervisor + the episode's apps' functions plus
  unrelated functions, shuffled), so the model must select the right tool, not just fill arguments.
- Natural-language surfaces (user messages, reasoning, replies, user-composed argument strings) are
  Korean; the API layer (function names, parameter names, enum values, ids, tool observations) stays
  English, matching real deployments.

## Schema

| field | type | description |
|---|---|---|
| `id` | str | `kotraj_aw-{app}-…` (single) or `kotraj_xaw-{scenario}-…` (cross) |
| `source` | str | `kotraj_appworld_{app}` or `kotraj_appworld_cross_{scenario}` |
| `tools` | str (JSON) | OpenAI-style function catalog, distractor-augmented, English |
| `messages` | str (JSON) | chat messages; assistant messages carry `reasoning_content` (Korean) alongside `content` and `tool_calls`; `tool` messages are the environment's real JSON observations |
| `think_source` | str | `selfgen_ko` (single) / `selfgen_ko_cross` (cross) |
| `meta` | dict | `persona`, `world_task`, apps, `scenario`/`primary`, `prelogin`, goal/sub-goal counts, `kinds` |

## Method

- Environment: [AppWorld](https://appworld.dev) (9 apps / 457 APIs), deterministic SQLite state checks.
- User simulator + agent: Qwen3.8-27B-FP8. Korean reasoning is prefilled and style-gated; one retry
  per failed turn, whole-episode drop on repeated failure.
- No LLM sits in the pass/fail decision — every kept row is a trajectory whose effect on the
  environment was verified by reading the app databases back.

## Access

This dataset is gated: access is granted on request after manual review.

## 2026-10-29 품질 개선 (필터링, 24,515 → 17,314행)
행 단위 규칙 필터 (`LLM_Hard_STE/data_gen/ko/filter_kotraj_ko.py`):
- 앞서 나온 적 없는 이메일 인자(날조) 3,628 · 자격증명 환각('12345', 'your_access_token' 등) 3,542 · 상태 변경 호출 중복 633
- 동일 실패 호출 반복 187 · 소수점 원화 표기 158 · 한자 80 (괄호 한자 "(姓)" 341건은 삭제 후 유지)
- 형식: `tool_calls` 를 파이썬 repr 문자열에서 JSON 리스트로 정규화.
