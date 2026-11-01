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
  - synthetic
  - verified
size_categories:
  - 10K<n<100K
configs:
  - config_name: default
    data_files:
      - split: train
        path: "data/*.jsonl"
  - config_name: workspace
    data_files:
      - split: train
        path: "data/workspace.jsonl"
  - config_name: travel
    data_files:
      - split: train
        path: "data/travel.jsonl"
  - config_name: banking
    data_files:
      - split: train
        path: "data/banking.jsonl"
  - config_name: slack
    data_files:
      - split: train
        path: "data/slack.jsonl"
---

# huibeom_agentic-dojo-ko-v1-draft

**Draft.** 18,567 Korean multi-turn agentic trajectories generated inside the executable
[AgentDojo](https://github.com/ethz-spylab/agentdojo) (v1.2.2, MIT) environments, kept only when every
user turn passed a deterministic state check. A Korean user simulator speaks, the agent calls tools that
**actually execute** against the environment, and after each user turn the runner reads the environment
state (or checks the reply against a rule-computed fact). No LLM takes part in the pass/fail decision.

| config | rows | domain |
|---|---:|---|
| `workspace` | 6,306 | email, contacts, calendar, cloud drive |
| `travel` | 5,050 | hotels, restaurants, car rental, flights, reservations, calendar, email |
| `slack` | 3,940 | channels, direct messages, members, web pages |
| `banking` | 3,271 | transfers, scheduled transfers, transactions, account files, user info |
| **total** | **18,567** | |

Each episode has 6–8 user turns (mean 7.0) and 9.6–13.8 tool calls on average.

## Goals

49 goal types over the four domains: actions (send, create, reschedule, share, reserve, transfer…),
queries answered from tool results (counts, owners, prices, members…), and cross-step goals that require
reading one result and acting on it (event participants → email, file content → email, best-rated hotel
→ reservation, bill file → payment, past transaction → repeat payment, last channel poster → DM,
web page fact → channel post). User-composed text (subjects, bodies, messages, payment notes) is Korean;
proper names, file names and API values stay as in the environment. Place names are often spoken in
Korean (파리, 런던), so the agent has to map them to the API values.

Each goal type ships a reference solver; before generation, every type was checked to fail with no
action and pass with the reference solver (49 types × 10 seeds).

## Environment adjustments

- Two upstream behaviours were corrected in the runner: `send_money` now lowers the balance, and
  `reserve_car_rental` now stores the requested end time.
- Six spam / fake-notice items that the original benchmark uses for its robustness tests were removed
  from the default workspace world.
- Banking and Slack worlds are randomized per episode (transaction history, scheduled transfers, bill
  files / users, channels, memberships, messages, web pages). Workspace and travel use the default worlds.
- Distractor tools from other domains are added to each catalog and shuffled; any call to a tool outside
  the episode's own domain fails the turn, so kept rows contain correct tool selection only.

## Quality gates (all rows)

Korean user turns with the required names/values, persona register kept (존댓말/반말, 0 mismatches),
no Chinese characters, no emoji or Chinese in tool arguments, Korean reasoning in every assistant
round (`reasoning_content`), and no truncated tool results (35 such rows removed).

## Known limitation (draft)

User utterances repeat across episodes: 67.6% of user turns are unique strings, because the default
workspace and travel worlds are small (e.g. 18 contacts, 3 hotel cities). Every episode as a whole is
distinct. A paraphrasing pass for repeated turns is planned before a non-draft release.

## Schema

| field | type | description |
|---|---|---|
| `id` | str | `kotraj_dojo-{suite}-{idx}` |
| `source` | str | `kotraj_agentdojo_{suite}` |
| `tools` | str (JSON) | OpenAI-style function catalog (domain tools + distractors) |
| `messages` | str (JSON) | system / user / assistant / tool; assistant messages carry `reasoning_content` |
| `think_source` | str | `selfgen_ko_dojo` |
| `meta` | dict | `suite`, `persona`, `world_seed`, `today`, `n_goals`, `kinds`, `gen_ver` |

Generated with Qwen3.8-27B-FP8 (user simulator and agent).

## Access

Gated: access is granted on request after manual review.

## 2026-10-29 품질 개선 (필터링, 18,567 → 13,323행)
행 단위 규칙 필터 (`LLM_Hard_STE/data_gen/ko/filter_kotraj_ko.py`):
- 파일명×문구 슬롯 조합 불일치 3,546 · 같은 user 턴 안 상태 변경 호출 중복(같은 메시지 반복 게시 등) 2,029 · 동일 실패 호출 반복 1,975
- 정형 칭찬 오프너 2턴 이상 856 · reasoning 에 앞서 나온 적 없는 IBAN 123 · reasoning "함수 없음" 자기모순 45 · 한자 2
- 형식: `tool_calls` 를 파이썬 repr 문자열에서 JSON 리스트로 정규화.
