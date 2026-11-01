---
license: mit
source_datasets:
- boradorish/STAGE-eval
language:
- en
- ko
tags:
- json-extraction
- evaluation
- sob
- fine-tuning
---

# SOB-FT-STAGE-Eval

Mapped standalone corpus from [boradorish/STAGE-eval](https://huggingface.co/datasets/boradorish/STAGE-eval).

## What changed from the source

| | Source | This repo |
|---|---|---|
| **Format** | `stem`, `user_prompt`, `gold_json`, `json_schema`, token counts | SOB FT schema (null columns removed) |
| **Splits** | HF `train` + `test` | Combined into one split; original split preserved in `question_type` |
| **Prompt** | Single `user_prompt` | Split at `=== Report ===` / `=== 보고서 ===` → `question` + `context` |
| **Target** | `gold_json` | `ground_truth` |
| **Schema** | `json_schema` | unchanged (Draft 7 valid) |
| **IDs** | `stem` | `source_id=stem`, `record_id=stage-eval-{stem}` |
| **Tokens** | `total_tokens` (often -1) | `question_difficulty` when ≥0 |
| **Rows** | 19,411 | 19,302 (109 dropped >65k chars) |

All-null reserved columns are **dropped**. `source_id`, `question_type`, and `question_difficulty` are kept.

## Regenerate

```bash
python3 merge_stage_eval.py --dry-run
python3 merge_stage_eval.py
```

## Merge into extract

```bash
python3 merge_ft_corpus.py --corpus mariem123kfg/sob-ft-stage-eval --source-prefix boradorish/STAGE-eval
```
