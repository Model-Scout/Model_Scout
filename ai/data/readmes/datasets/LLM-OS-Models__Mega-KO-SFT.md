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
- terminal
- agent
- lfm2.5
- liquid-ai
- fabliq
- mega
- composite
size_categories:
- 1K<n<10K
---

# Mega KO SFT (Fabliq-KO Training Dataset)

Combined Korean SFT distillation dataset for training **Fabliq-KO** (LFM2.5-8B-A1B base, LiquidAI MoE 8B/1B active).

## Composition

| Source | Rows | Description |
|--------|------|-------------|
| Fable5-KO | 3,948 | Glint-Research/Fable-5-traces (multi-turn agent traces, tool use) |
| WithinUs-KO | 135 | withinus_mythos_distilled_25k (mathematical reasoning) |
| Helio-KO | 146 | helio_fable5_distill_reasoning_462x (deep-reasoning, security/math/biomedical) |
| **Total** | **4,229** | |

## Translation Policy

All three sources translated with consistent policy:
- **Korean 반말 casual tone** (`~해`, `~야`): natural language, `<think>` reasoning, explanations, descriptions
- **Preserved in English**: code, bash commands, file paths, tool names, function names, JSON syntax, mathematical notation, gene/protein names, chemical names, CVE IDs, CVSS vectors, technical acronyms

## Format

JSONL. Each row:
```json
{
  "dataset": "fable5_ko" | "withinus_ko" | "helio_ko",
  "src_row": <int>,
  "lang": "ko",
  "messages": [{"role": "system|user|assistant", "content": "..."}],
  "meta": {...}  // original metadata from source dataset
}
```

`messages` schema varies across sources:
- **fable5_ko**: multi-turn (system + multi user/assistant), real agent traces with tool calls
- **withinus_ko**: single user/assistant turn (no system)
- **helio_ko**: system + user + assistant (deep reasoning with `<think>` blocks)

## Sources / Citation

This is a combined dataset. Please cite all three component datasets:
- [LLM-OS-Models/Fable5-KO-SFT](https://huggingface.co/datasets/LLM-OS-Models/Fable5-KO-SFT)
- [LLM-OS-Models/WithinUs-KO-SFT](https://huggingface.co/datasets/LLM-OS-Models/WithinUs-KO-SFT)
- [LLM-OS-Models/Helio-KO-SFT](https://huggingface.co/datasets/LLM-OS-Models/Helio-KO-SFT)

And the original English sources they were derived from.

## Target Model

Trains **Fabliq-KO**, a Korean-speaking terminal agent based on LiquidAI's LFM2.5-8B-A1B (MoE, 8B total / 1B active params).

## License

Inherits from the original source datasets.

## Related

- Base model: [LiquidAI/LFM2-5-8B-A1B](https://huggingface.co/LiquidAI/LFM2-5-8B-A1B)
- Build script: `scripts/build_mega_ko.py` (deterministic combine, preserves source metadata)
