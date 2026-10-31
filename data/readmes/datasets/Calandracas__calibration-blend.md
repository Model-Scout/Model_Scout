---
configs:
- config_name: default
  data_files:
  - split: train
    path:
    - data/train-*.parquet
  - split: test
    path:
    - data/test-*.parquet
license: ["apache-2.0", "bsd-2-clause", "bsd-3-clause", "cc-by-4.0", "cc-by-sa-4.0", "mit", "odc-by"]
language:
- en
- zh
- de
- es
- fr
- it
- ja
- ko
- hi
- pt
task_categories:
- text-generation
tags:
- calibration
- quantization
- llm-compressor
- vllm
- multi-turn
- tool-use
- reasoning
size_categories:
- 10K<n<100K
---

# Calibration Dataset

## Description

This dataset contains **32107** calibration examples for LLM quantization using [LLM-Compressor](https://github.com/vllm-project/llm-compressor).

## Schema

| Column | Type | Description |
|--------|------|-------------|
| `messages` | `list[dict]` | Conversation turns with `role`, `content`, optional `reasoning_content`/`tool_calls` |
| `tools` | `json (list)` | JSON list of tool definitions (function schemas); `null` when absent |
| `source` | `str` | Source dataset identifier |
| `license` | `list[str]` | SPDX license identifiers (multiple may apply) |
| `subset` | `str` | Source subset name |
| `record_id` | `str` | Unique record identifier (`{source}::{subset}::{index}`) |
| `extraction_timestamp` | `str` | ISO 8601 extraction timestamp |

## Source Attribution

- **Sources**: Bingguang/HardGen, FreedomIntelligence/medical-o1-reasoning-SFT, HuggingFaceH4/Multilingual-Thinking, ianncity/KIMI-K2.5-1000000x, nvidia/Nemotron-RL-Multichallenge-v1, nvidia/Nemotron-SFT-Instruction-Following-Chat-v3, nvidia/Nemotron-SFT-Math-v4, nvidia/Nemotron-SFT-Multilingual-v1, nvidia/Nemotron-SFT-Multilingual-v2, nvidia/Nemotron-SFT-SWE-v3, nvidia/Nemotron-SFT-Science-v2
- **Subsets**: English, French, General-Distillation, General-Math, German, Italian, MultilingualSTEM, PHD-Science, Spanish, advanced, code_de, code_es, code_fr, code_hi, code_it, code_ja, code_ko, code_pt, code_zh, default, en, instruction_following, math_de, math_es, math_fr, math_hi, math_it, math_ja, math_ko, math_pt, math_zh, rqa, stem_de, stem_es, stem_fr, stem_hi, stem_it, stem_ja, stem_ko, stem_pt, stem_zh, train, zh
- **Licenses**: CC BY-SA 4.0, apache-2.0, bsd-2-clause, bsd-3-clause, cc-by-4.0, cc-by-sa-4.0, mit, odc-by

## Intended Use

This dataset is designed for calibration in LLM quantization workflows,
particularly with the vLLM LLM-Compressor framework.

## Usage

```python
from datasets import load_dataset

dataset = load_dataset("Calandracas/calibration-blend")
```

## License

This dataset contains data from multiple sources. See the `license` column for per-record license information.
