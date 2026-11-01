---
language:
- ko
license: apache-2.0
task_categories:
- text-generation
tags:
- korean
- tool-calling
- agentic
- function-calling
- synthetic
size_categories:
- 1K<n<10K
configs:
- config_name: default
  data_files:
  - split: train
    path: train.jsonl
---

# ko-agentic-sft

**2,369 Korean agent-training conversations, fully synthetic, generated at zero cost.**
Built for teaching small models *when* to call a tool — not just *how*.

[![GitHub](https://img.shields.io/badge/GitHub-kogemma--e2b-181717?logo=github)](https://github.com/waylake/kogemma-e2b)
[![Model](https://img.shields.io/badge/model-KoGemma--E2B-4285F4)](https://huggingface.co/waylake/KoGemma-E2B)

## Why this dataset exists

Most tool-use datasets contain only positive examples: every prompt leads to a tool call. Train a
small model on that and it learns *"tools visible ⇒ call a tool"* — we measured exactly this
failure (tool restraint dropped from 1.00 to 0.00 on held-out cases).

This dataset therefore ships **786 no-action conversations under the same tool-bearing system
prompt** alongside 1,583 action trajectories.

## Composition

| `kind` | Records | What it teaches |
|---|---|---|
| `single` | 490 | one `web_search` → observation → sourced answer |
| `direct` | 480 | **no action needed** — answer directly (restraint) |
| `chain` | 404 | `web_search` → `fetch_page` two-step chain |
| `calc` | 330 | `calculator` action with matching arithmetic |
| `qa` | 315 | plain Korean QA |
| `fail` | 160 | empty/unusable search results → say so, offer alternatives |
| `mtool` | 147 | multi-turn where a later turn triggers a new search |
| `refuse` | 25 | private/unknowable → refuse without calling tools |
| `multiturn` | 18 | 5–7 turn dialogue |
| **total** | **2,369** | action 1,583 · no-action 786 |

## Schema

```json
{
  "messages": [
    {"role": "system", "content": "너는 한국어로 정확하게 답하고, 필요하면 도구를 쓰는 AI 비서다."},
    {"role": "user", "content": "요즘 서울 지하철 기본요금 얼마야?"},
    {"role": "assistant", "content": "{\"action\": \"web_search\", \"args\": {\"query\": \"서울 지하철 기본요금\"}}"},
    {"role": "user", "content": "[도구 결과] {\"results\": [{\"title\": \"운임 안내\", \"url\": \"https://example.kr/fare\", \"text\": \"카드 기준 성인 1,550원\"}]}"},
    {"role": "assistant", "content": "카드 기준 성인 기본요금은 1,550원입니다. ... (출처: https://example.kr/fare)"}
  ],
  "kind": "single",
  "has_action": true
}
```

- Tools: `web_search{query}`, `fetch_page{url}`, `calculator{expr}`, `now{}`
- Observations arrive as a `user` turn prefixed with `[도구 결과]` followed by JSON.
- Actions are always a **single-line JSON object** — easy to parse and to score.
- URLs are `example.kr` placeholders: the trajectories are structurally realistic but do not
  claim real facts.

## Generation & filtering

- Teacher: `ox-alpha-free` (free endpoint), 6–22 parallel workers on a MacBook, cost **$0**
- Diversity matrix: 9 trajectory shapes × 60+ Korean domains × repeated batches
- Every shard was validated before acceptance: JSON parseable, `system`-first / `assistant`-last,
  role alternation, action-schema whitelist, observation JSON parseable, no emoji / HTML /
  markdown headers, no truncated sentences
- Units failing validation were regenerated up to 3 times; **JSON validity of the released set is 100%**

## Known limitations

- Observations are synthetic; do not use them as a factual knowledge source.
- Korean only.
- `refuse` is under-represented (25) because that axis was descoped mid-project.
- Facts inside answers are only as good as the free teacher — treat as *format* supervision,
  not as ground truth.

## Citation

```bibtex
@misc{kogemma-agentic-sft-2026,
  title  = {ko-agentic-sft: Korean tool-use SFT data with negative examples},
  author = {waylake},
  year   = {2026},
  url    = {https://huggingface.co/datasets/waylake/ko-agentic-sft}
}
```
