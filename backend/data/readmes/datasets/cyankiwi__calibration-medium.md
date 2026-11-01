---
pretty_name: cyankiwi calibration (medium)
license: other
license_name: mixed-source-licenses
language:
  - en
  - zh
  - es
  - de
  - ar
  - fr
  - hi
  - ja
  - ko
  - ru
  - id
  - pt
  - th
  - vi
  - it
  - tr
task_categories:
  - text-generation
size_categories:
  - 10K<n<100K
tags:
  - calibration
  - multilingual
  - agentic
  - tool-use
  - reasoning
configs:
  - config_name: default
    data_files:
      - split: train
        path: data/train-*.parquet
---

# cyankiwi/calibration-medium

A 16-language, 6-domain **calibration dataset**: **12,800 conversations ≈
268.7M tokens**, prioritizing agentic / tool-use traces, then code, math, stem,
and structured output.

## Schema

Four columns:

| column | type | description |
|---|---|---|
| `conversations` | `list<struct>` | the chat transcript, one struct per message |
| `language` | `string` | ISO 639-1 code (16 values, table below) |
| `language_type` | `string` | domain: `agentic`, `code`, `math`, `stem`, `general`, `structured_output` |
| `source` | `string` | origin HF dataset repo id |

Each message struct carries all five fields (null where absent):

```
role               : "system" | "user" | "assistant" | "tool"
content            : message text (tool output for role="tool")
reasoning_content  : assistant thinking trace (null when absent)
id                 : on role="tool" messages, the id of the tool_call it answers
tool_calls         : list<struct{id, type, function: struct{name, arguments}}>
                     (arguments is a JSON-encoded string; non-null only on
                      assistant turns that call tools)
```

Every `role="tool"` message's `id` matches a `tool_calls[].id` from a preceding
assistant turn in the same conversation (validated over all 198,052 tool calls /
181,173 tool messages).

## Loading

```python
import json
from datasets import load_dataset

ds = load_dataset("cyankiwi/calibration-medium", split="train")

def preprocess(example, tokenizer):
    conv = []
    for m in example["conversations"]:
        msg = {"role": m["role"], "content": m["content"]}
        if m["tool_calls"]:
            msg["tool_calls"] = [
                {"id": tc["id"], "type": tc["type"],
                 "function": {"name": tc["function"]["name"],
                              "arguments": json.loads(tc["function"]["arguments"])}}
                for tc in m["tool_calls"]
            ]
        if m["role"] == "tool" and m["id"]:
            msg["tool_call_id"] = m["id"]
        conv.append(msg)
    return tokenizer.apply_chat_template(
        conv, tokenize=True, max_length=1024, truncation=True, return_dict=True)
```

Stratified subsets come directly from the columns, e.g.
`ds.filter(lambda r: r["language_type"] == "agentic")` or
`ds.filter(lambda r: r["language"] == "ru")`.

## Composition

Totals: **12,800 samples, 268,659,229 tokens** (counted with the Qwen3-8B
tokenizer over all text fields — content, reasoning, tool-call arguments).

### Languages

Sample shares are exact quotas; token shares skew English because full-length
agentic traces are kept unsplit (mean ~35k tokens).

| lang | samples | sample share | token share | mean tok | p50 | p90 | max |
|---|---|---|---|---|---|---|---|
| en | 5,376 | 42.0% | 71.6% | 35,765 | 34,832 | 69,234 | 185,073 |
| zh | 1,408 | 11.0% | 6.1% | 11,581 | 7,533 | 25,712 | 109,803 |
| es | 768 | 6.0% | 3.8% | 13,175 | 9,484 | 27,089 | 114,495 |
| de | 768 | 6.0% | 4.0% | 14,102 | 10,312 | 29,145 | 100,536 |
| ar | 512 | 4.0% | 0.5% | 2,822 | 2,644 | 4,609 | 15,221 |
| fr | 512 | 4.0% | 2.4% | 12,829 | 9,453 | 26,879 | 84,841 |
| hi | 512 | 4.0% | 1.9% | 9,735 | 6,312 | 22,814 | 113,897 |
| ja | 512 | 4.0% | 2.4% | 12,773 | 9,228 | 27,126 | 116,969 |
| ko | 512 | 4.0% | 2.0% | 10,490 | 7,023 | 22,718 | 62,713 |
| ru | 512 | 4.0% | 2.9% | 15,185 | 3,662 | 81,191 | 142,452 |
| id | 384 | 3.0% | 0.2% | 1,170 | 849 | 1,806 | 32,409 |
| pt | 384 | 3.0% | 1.4% | 9,667 | 7,235 | 20,952 | 47,382 |
| th | 192 | 1.5% | 0.04% | 596 | 452 | 818 | 4,839 |
| vi | 192 | 1.5% | 0.1% | 1,549 | 1,373 | 2,189 | 6,236 |
| it | 128 | 1.0% | 0.6% | 13,584 | 6,997 | 38,443 | 70,109 |
| tr | 128 | 1.0% | 0.1% | 1,088 | 722 | 2,061 | 8,571 |

### Domains (`language_type`)

| domain | samples | share | soft target | token share |
|---|---|---|---|---|
| agentic | 3,680 | 28.7% | 28.0% | 64.0% |
| code | 2,688 | 21.0% | 24.0% | 13.8% |
| math | 2,062 | 16.1% | 16.0% | 13.1% |
| stem | 1,856 | 14.5% | 14.0% | 2.9% |
| general | 1,746 | 13.6% | 12.0% | 5.2% |
| structured_output | 768 | 6.0% | 6.0% | 1.1% |

Language quotas are hard; domain shares are soft targets. Code sits ~3pt under
target (and general ~1.6pt over) because the floor-tier languages (th, vi, tr,
id) only have general-domain sources.

### Sources

| samples | source | languages | domain(s) |
|---|---|---|---|
| 3,520 | [nvidia/Nemotron-SFT-Multilingual-v1](https://huggingface.co/datasets/nvidia/Nemotron-SFT-Multilingual-v1) | de, es, fr, it, ja, zh | code, math, stem |
| 1,760 | [nvidia/Open-SWE-Traces](https://huggingface.co/datasets/nvidia/Open-SWE-Traces) | en | agentic |
| 1,600 | [nvidia/Nemotron-SFT-SWE-v3](https://huggingface.co/datasets/nvidia/Nemotron-SFT-SWE-v3) | en | agentic |
| 1,568 | [nvidia/Nemotron-SFT-Multilingual-v2](https://huggingface.co/datasets/nvidia/Nemotron-SFT-Multilingual-v2) | hi, ja, ko, pt | code, math, stem |
| 1,376 | [openbmb/UltraData-SFT-2605](https://huggingface.co/datasets/openbmb/UltraData-SFT-2605) | en, zh | code, math, general, structured_output |
| 1,152 | [allenai/Dolci-Instruct-SFT](https://huggingface.co/datasets/allenai/Dolci-Instruct-SFT) | ar, id, th, tr, vi | general |
| 512 | [SupraLabs/agentic-reasoning-trace-summaries-40k](https://huggingface.co/datasets/SupraLabs/agentic-reasoning-trace-summaries-40k) | en | structured_output |
| 416 | [Jackrong/Kimi-K2.5-Reasoning-1M-Cleaned](https://huggingface.co/datasets/Jackrong/Kimi-K2.5-Reasoning-1M-Cleaned) | ar, ru | stem |
| 303 | [MauroPello/multilingual-reasoning-gym-sft](https://huggingface.co/datasets/MauroPello/multilingual-reasoning-gym-sft) | hi, it, ru | math |
| 256 | [AletheiaResearch/GLM-5.2-Agent](https://huggingface.co/datasets/AletheiaResearch/GLM-5.2-Agent) | en | agentic |
| 144 | [HelioAI/Fable-5-Distill-Reasoning-462x](https://huggingface.co/datasets/HelioAI/Fable-5-Distill-Reasoning-462x) | en, ru | general |
| 127 | [HelioAI/Claude-Fable-5-5500x](https://huggingface.co/datasets/HelioAI/Claude-Fable-5-5500x) | en, ru | math |
| 64 | [Glint-Research/Fable-5-traces](https://huggingface.co/datasets/Glint-Research/Fable-5-traces) | en | agentic |
| 2 | [kaist-ai/Multilingual-CoT-Collection](https://huggingface.co/datasets/kaist-ai/Multilingual-CoT-Collection) | ru | general |

Notes on specific sources:

- **Open-SWE-Traces**: only trajectories synthesized by **MiniMax-M2.5**
  (`minimax_m25` split), preferring `resolved == 1` runs.
- **GLM-5.2-Agent / Fable-5-traces**: event-log agent sessions reconstructed
  into linear conversations (parentId chains; thinking blocks →
  `reasoning_content`, tool calls/results correlated by id).
- **Kimi-K2.5**: `<think>…</think>` blocks extracted into `reasoning_content`;
  ar/ru selected by script detection from the `MultilingualSTEM` subset.
- **Fable-5-Distill-Reasoning-462x**: the source has no answer field; the
  trace's closing conclusion was split out of the thinking trace into assistant
  `content` (marker-based with trailing-block fallback).
- **Dolci-Instruct-SFT**: ar/id/th/tr/vi selected by language ID (script ranges
  for ar/th; fastText lid.176 for id/tr/vi, with Indonesian accepting combined
  id+ms mass). None of the selected rows carry tool calls.

## Construction

- **Selection**: streamed sampling (seed 42) with a **minimum length of 1,024
  tokens** per conversation; full conversations kept unsplit (no truncation at
  build time). Global exact dedupe over message content.
- **Backfill**: when a language×domain×source bucket underfilled (source too
  small or too short), it was filled from same-language surplus in domain-
  priority order (agentic > code > math > stem > general > structured_output),
  then from the longest below-threshold rows. Below-1,024-token fills: id 217,
  th 179, tr 94, ru 31 — long rows in those languages are scarce in the
  available sources (e.g. only 1 of 60,570 scanned kaist ru rows passed the
  bar, hence its 2-sample contribution).
- Full per-bucket accounting (requested vs collected vs backfilled, token
  percentiles) is in `composition_report.md` / `composition_report.json`.

## Caveats

- **Token-share skew**: English carries 71.6% of tokens despite 42% of samples
  — agentic SWE traces are long and kept whole. If samples are
  truncated to ~1k tokens (typical), effective language balance follows the
  *sample* shares, not token shares.
- **Floor-tier lengths**: th/id/tr samples are mostly below 1,024 tokens
  (th p50 = 452); they contribute genuine script/typology coverage but little
  long-context signal.
- **Licensing**: mixed — each row's `source` column points at its origin
  dataset; consult the source repos (CC-BY-4.0 / CC-BY-SA-4.0 for the Nemotron
  sets, Apache-2.0 for UltraData and SupraLabs, ODC-BY for Dolci, others vary).

## Intended use

Calibration data. Not intended as an SFT corpus: sampling optimizes
activation-statistics coverage (language × domain × rare-token mix), not answer
quality.
