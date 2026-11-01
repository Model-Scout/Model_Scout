---
license: other
language:
- ko
- en
task_categories:
- text-generation
tags:
- korean
- sft
- distillation
- mathematical-reasoning
- terminal
- agent
- lfm2.5
- liquid-ai
- fabliq
size_categories:
- 1K<n<10K
---

# WithinUs KO SFT Distillation

Korean-translated WithinUs distillation dataset for training **Fabliq-KO** (LFM2.5-8B-A1B base).

## Source / Citation

**Original dataset:** `withinus_mythos_distilled_25k` (mathematical reasoning category, 135 rows selected for LFM-SFT format).

This Korean translation is derived from the preprocessed LFM-SFT version. If you use this dataset, please cite both the original source and this Korean-translated version from LLM-OS-Models.

## Translation Policy

- **Translated to Korean (반말 casual tone):** natural language, explanations, mathematical reasoning prose
- **Preserved in English:** code, commands, file paths, mathematical notation, formulas, function names, technical terms
- System prompt translated to Korean 반말

## Target Model

Trains **Fabliq-KO**, a Korean-speaking terminal agent based on LiquidAI's LFM2.5-8B-A1B (MoE, 8B total / 1B active params).

## Status

- **Total rows:** 135 (100% complete)
- **File:** `withinus_ko_sft_20260628.jsonl`
- All rows translated with Korean 반말 casual tone

## Format

JSONL with `messages` field containing `system`, `user`, `assistant` turns. Each row also carries:
- `id`: unique ID with `-ko` suffix
- `src_id`: original English row ID
- `src_row`: original row index (0..134)
- `category`, `source`: preserved from source
- `lang`: `"ko"`

## License

Inherits from the original source dataset.

## Related

- Base model: LiquidAI/LFM2-5-8B-A1B
- Sibling datasets: Fable5-KO-SFT (3,948 rows), Helio-KO-SFT (146 rows)
- Combined into Mega-KO for final Fabliq-KO training
