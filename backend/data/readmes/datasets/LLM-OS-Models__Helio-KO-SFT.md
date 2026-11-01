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
- reasoning
- deep-research
- terminal
- agent
- lfm2.5
- liquid-ai
- fabliq
size_categories:
- 1K<n<10K
---

# Helio KO SFT Distillation

Korean-translated Helio deep-reasoning distillation dataset for training **Fabliq-KO** (LFM2.5-8B-A1B base).

## Source / Citation

**Original dataset:** `helio_fable5_distill_reasoning_462x` (146 rows of deep-reasoning traces covering security audits, mathematical proofs, biomedical analyses, philosophical treatises, and more).

This Korean translation is derived from the preprocessed LFM-SFT version. If you use this dataset, please cite both the original source and this Korean-translated version from LLM-OS-Models.

## Translation Policy

- **Translated to Korean (반말 casual tone):** natural language, `<think>` reasoning blocks, explanations, descriptions
- **Preserved in English:** code, bash commands, file paths, tool names, function names, JSON syntax, mathematical notation, gene/protein names, chemical names, CVE IDs, CVSS vectors, technical acronyms
- System prompt translated to Korean 반말

## Target Model

Trains **Fabliq-KO**, a Korean-speaking terminal agent based on LiquidAI's LFM2.5-8B-A1B (MoE, 8B total / 1B active params).

## Status

- **Total rows:** 146 (100% complete)
- **File:** `helio_ko_sft_20260628.jsonl` (~37MB)
- Large rows (avg ~250KB) chunked at code-block and paragraph boundaries for translation
- Each row undergoes segment-aware translation: prose translated, code preserved verbatim

## Format

JSONL with `messages` field containing `system`, `user`, `assistant` turns. Each row also carries:
- `source`: preserved from source
- `src_row`: original row index (0..145)
- `lang`: `"ko"`

## License

Inherits from the original source dataset.

## Related

- Base model: LiquidAI/LFM2-5-8B-A1B
- Sibling datasets: Fable5-KO-SFT (3,948 rows), WithinUs-KO-SFT (135 rows)
- Combined into Mega-KO for final Fabliq-KO training
