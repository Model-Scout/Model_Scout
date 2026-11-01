---
license: mit
language:
- ko
- en
task_categories:
- text-classification
tags:
- routing
- korean
- translation
size_categories:
- n<1K
source_datasets:
- SupraLabs/Prompt-Routing-Dataset
configs:
- config_name: default
  data_files:
  - split: train
    path: train.jsonl
---

# Prompt-Routing-Dataset-ko

Korean translation of [`SupraLabs/Prompt-Routing-Dataset`](https://huggingface.co/datasets/SupraLabs/Prompt-Routing-Dataset).
992 rows.

Only the `prompt` column was translated. Every label was copied verbatim. The English
source is kept as `prompt_en` so any row can be audited.

## Columns

| column | type | |
| --- | --- | --- |
| `prompt` | string | Korean translation |
| `prompt_en` | string | English source, copied unchanged |
| `complexity_score` | int | 1–5 |
| `primary_domain` | string | free text, 338 distinct values |
| `coding_task` | bool | |
| `math_task` | bool | |
| `requires_reasoning` | bool | |
| `routing_choice` | string | `big model` or `small model` |
| `routing_justification` | string | |
| `language` | string | always `ko` |

## Distribution

| `routing_choice` | rows |
| --- | ---: |
| `big model` | 744 |
| `small model` | 248 |

| `complexity_score` | 1 | 2 | 3 | 4 | 5 |
| --- | ---: | ---: | ---: | ---: | ---: |
| rows | 76 | 489 | 327 | 95 | 5 |

Median length is 108 characters in Korean against 197 in English, which is the
usual ratio for the pair.

## How it was translated

A local model served over an OpenAI-compatible endpoint. Code and mathematics are
never sent to it: fenced blocks, inline backticks and LaTeX spans are masked before
the request and restored afterwards, so identifiers and formulas cannot be altered.

Rows whose translation came back empty, unchanged, or wildly out of proportion were
flagged rather than accepted silently. One row is identical to its English source
because it contains no translatable text.

## Licence

MIT, inherited from `SupraLabs/Prompt-Routing-Dataset`. Labels are that dataset's;
only the Korean prompt text is new.
