---
license: other
language: [en, ar, zh, fr, de, it, ja, ko, pt, es, pl, vi, th, id, hi, ru]
task_categories: [text-generation]
tags: [function-calling, tool-use, agents, on-device, grpo, reinforcement-learning]
size_categories: [1K<n<10K]
configs:
  - config_name: default
    data_files:
      - {split: train, path: train.parquet}
      - {split: test, path: test.parquet}
      - {split: test_unseen, path: test_unseen.parquet}
      - {split: showcase, path: showcase.parquet}
---
# Phone Assistant Tools

> [!Note]
> 📓 **Tutorial**: This is the dataset used in [GRPO with TRL](https://colab.research.google.com/github/Liquid4All/cookbook/blob/main/finetuning/notebooks/lfm3_grpo_with_trl.ipynb)

Requests to a phone assistant with the gold tool calls, for a fixed catalog of 108 tools. Depending on the request, the right behavior is one or more calls, a clarifying question, or an answer without any tool. 16 languages.

## Files

| File | Rows | Content |
|---|---:|---|
| `tools.json` | 108 | tool catalog, as function schemas |
| `scoring.json` | 108 | for each tool argument, how a predicted value is compared with the gold one |
| `train` | 2,500 | requests for 98 of the tools |
| `test` | 499 | requests for the same 98 tools |
| `test_unseen` | 300 | requests for the 10 tools that never appear in `train` or `test` calls |
| `showcase` | 8 | examples from `test_unseen` |

## Fields

| Field | Description |
|---|---|
| `id` | row identifier |
| `language` | ISO 639-1 code of the request |
| `category` | `single`, `multi`, `lookalike`, `no_tool`, `clarify` or `partial` |
| `context` | `{datetime, timezone, locale}` of the phone |
| `request` | user request |
| `calls` | gold calls as a JSON string, in any order, or `[]` when no call should be made |

## Conventions

- Dates and times are local and resolved from `context.datetime`: `YYYY-MM-DDTHH:MM:SS`, `YYYY-MM-DD`, `HH:MM`.
- Optional arguments appear only when the user states them.
- Argument keys and enum values are English. Free text stays in the user's language.
