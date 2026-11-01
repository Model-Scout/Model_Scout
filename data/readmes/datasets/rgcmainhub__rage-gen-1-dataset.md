---
license: mit
task_categories:
  - text-generation
language:
  - en
  - es
  - fr
  - de
  - pt
  - it
  - tl
  - ja
  - ko
  - zh
  - ru
  - ar
  - hi
  - tr
  - nl
  - sv
tags:
  - rage-ai
  - rage-gen-1
  - synthetic
  - sft
  - chat
---

# rage-gen-1-dataset

Training corpus for [**rage-gen-1**](https://huggingface.co/rgcmainhub/rage-gen-1) — the AI agent programming model by **DevNameGelo** (RGC engine).

## Contents

| File | Description |
|---|---|
| `train.jsonl` | ~17,750 examples / ~9 MB, message-format SFT data |
| `corpus_stats.json` | category counts + sizes |
| `build_corpus.py` | deterministic generator (seeded, `--scale` to resize) |

## Format

Each line:

```json
{"messages": [{"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}], "meta": {"category": "coding", "language": "Python"}}
```

Assistant content embeds the full rage-gen-1 chat protocol: `<|think_start|>…<|think_end|>` reasoning blocks (short chains for `low`, step-by-step for `high`) and `<|tool_call|>{json}` tool rounds with `<|tool_response|>` feedback turns.

## Categories

| Category | ~Examples | Covers |
|---|---|---|
| coding | 3,750 | Next.js, HTML/CSS/JS, Three.js, Python, Luau, Java, C++ |
| chat | 2,750 | greetings, small talk, tone |
| identity | 2,250 | who/what rage-gen-1 is, DevNameGelo, RGC, specs |
| reasoning | 2,250 | math + logic, low/high think chains |
| tools | 1,750 | calculator / get_time / echo JSON tool rounds |
| knowledge | 1,750 | ML + web tech facts (cutoff Sept 2026) |
| agent | 1,750 | multi-step plans, tool loops |
| multilingual | 1,500 | 15 languages, English-primary |

## Regenerate

```bash
python build_corpus.py --scale 2.5   # deterministic, seed 1337
```

License: MIT.
