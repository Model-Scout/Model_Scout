---
license: apache-2.0
language:
- en
- zh
size_categories:
- 100K<n<1M
task_categories:
- text-generation
- question-answering
tags:
- reasoning
- chain-of-thought
- instruction-tuning
- sft
- distillation
- kimi
- kimi-k2.5
- cleaned
configs:
  - config_name: General-Distillation
    data_files:
      - split: train
        path: "General-Distillation.jsonl"
  - config_name: PHD-Science
    data_files:
      - split: train
        path: "PHD-Science.jsonl"
  - config_name: General-Math
    data_files:
      - split: train
        path: "General-Math.jsonl"
  - config_name: MultilingualSTEM
    data_files:
      - split: train
        path: "MultilingualSTEM.jsonl"
---

# 🪐 Kimi-K2.5-Reasoning-1M-Cleaned

**Kimi-K2.5-Reasoning-1M-Cleaned** is a cleaned derivative of [ianncity/KIMI-K2.5-1000000x](https://huggingface.co/datasets/ianncity/KIMI-K2.5-1000000x). It preserves the original four-config layout from the source dataset and rewrites each record into a unified reasoning-SFT schema with `id`, `conversations`, `input`, `output`, `domain`, and `meta`.


![image](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/b1-BDXcO8Fn58aqEbIsFb.png)


## Summary

- Source dataset: [`ianncity/KIMI-K2.5-1000000x`](https://huggingface.co/datasets/ianncity/KIMI-K2.5-1000000x)
- Source author: **ianncity**
- Teacher model recorded in `meta.teacher_model`: `KIMI-K2.5`
- Token lengths computed with tokenizer: `moonshotai/Kimi-K2.5`
- Total processed records: **1,003,589**
- Total kept records: **844,388**
- Total removed records: **159,201**
- Original source configs preserved: `General-Distillation`, `PHD-Science`, `General-Math`, `MultilingualSTEM`

## What This Release Fixes

The source JSONL files expose each example as a two-turn `messages` conversation only. This cleaned release standardizes that raw structure into a training-ready schema and removes records with quality issues.

### Transformations applied

1. Renamed the source `messages` field to `conversations`.
2. Split each record into `input` plus tagged `output`.
3. Normalized `output` into `<think>...</think>` followed by the final answer.
4. Rebuilt `id` as a deterministic MD5 hash over `domain + input + reasoning + answer`.
5. Wrote subset-level provenance into the `domain` field because the source data does not provide a finer per-example domain label.
6. Added `meta.input_tokens`, `meta.output_tokens`, and `meta.teacher_model`.
7. Preserved the original four-config subset boundaries instead of merging everything into one file.

### Removed data

The cleaning pipeline filters records with:

- malformed or unparseable reasoning / answer boundaries,
- incomplete or obviously truncated answers,
- refusal-style answers,
- repeated reasoning or duplicated answer segments,
- exact duplicate records after normalization.

## Dataset Structure

```json
{
  "id": "md5-hash-of-domain-input-reasoning-answer",
  "conversations": [
    {"from": "human", "value": "user prompt"},
    {"from": "gpt", "value": "<think>\nreasoning trace\n</think>\n\nfinal answer"}
  ],
  "input": "user prompt",
  "output": "<think>\nreasoning trace\n</think>\n\nfinal answer",
  "domain": "subset-derived label such as General-Math",
  "meta": {
    "input_tokens": 123,
    "output_tokens": 456,
    "teacher_model": "KIMI-K2.5"
  }
}
```

### Field notes

- `conversations[0]`: the user prompt.
- `conversations[1]`: the cleaned assistant response with `<think>` tags.
- `input`: flat prompt view.
- `output`: flat completion view containing reasoning plus final answer.
- `domain`: subset-derived label. The source repository does not include an explicit per-example domain field, so this release uses the source config name as the domain value.
- `meta`: lightweight token-length metadata and teacher model provenance.

## Subset Statistics

| Subset | Processed | Kept | Removed | File Size | Median Input Tokens | Median Output Tokens |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| General-Distillation | 598,366 | 553,313 | 45,053 | 14.20 GB | 49 | 2972 |
| PHD-Science | 103,759 | 103,307 | 452 | 2.80 GB | 45 | 3021 |
| General-Math | 208,426 | 97,771 | 110,655 | 6.16 GB | 56 | 9616 |
| MultilingualSTEM | 93,038 | 89,997 | 3,041 | 2.90 GB | 76 | 3956 |

## Filter Statistics

| Subset | Issue | Removed |
| --- | --- | ---: |
| General-Distillation | repeated_paragraph | 38,925 |
| General-Distillation | incomplete_output | 4,849 |
| General-Distillation | unparseable_output | 748 |
| General-Distillation | refusal_answer | 531 |
| PHD-Science | incomplete_output | 311 |
| PHD-Science | unparseable_output | 101 |
| PHD-Science | repeated_paragraph | 37 |
| PHD-Science | refusal_answer | 3 |
| General-Math | unparseable_output | 99,375 |
| General-Math | repeated_paragraph | 7,448 |
| General-Math | incomplete_output | 3,832 |
| MultilingualSTEM | unparseable_output | 1,841 |
| MultilingualSTEM | incomplete_output | 677 |
| MultilingualSTEM | repeated_paragraph | 522 |
| MultilingualSTEM | refusal_answer | 1 |

## Additional Token Statistics

| Subset | Mean Input Tokens | P95 Input Tokens | Mean Output Tokens | P95 Output Tokens |
| --- | ---: | ---: | ---: | ---: |
| General-Distillation | 115.94 | 506 | 3189.8 | 6761 |
| PHD-Science | 44.98 | 56 | 3213.31 | 5107 |
| General-Math | 57.76 | 81 | 9402.39 | 12485 |
| MultilingualSTEM | 79.22 | 123 | 4555.73 | 9082 |

## Included Content

- `General-Distillation`: the broad mixed-domain reasoning split from the source release.
- `PHD-Science`: science-heavy reasoning traces.
- `General-Math`: math-focused reasoning traces.
- `MultilingualSTEM`: multilingual STEM reasoning traces.

## Usage

```python
from datasets import load_dataset

general = load_dataset("Jackrong/Kimi-K2.5-Reasoning-1M-Cleaned", "General-Distillation")
science = load_dataset("Jackrong/Kimi-K2.5-Reasoning-1M-Cleaned", "PHD-Science")
math_ds = load_dataset("Jackrong/Kimi-K2.5-Reasoning-1M-Cleaned", "General-Math")
multi = load_dataset("Jackrong/Kimi-K2.5-Reasoning-1M-Cleaned", "MultilingualSTEM")
```

## Provenance

- Original dataset: [`ianncity/KIMI-K2.5-1000000x`](https://huggingface.co/datasets/ianncity/KIMI-K2.5-1000000x)
- Original author: **ianncity**
- This release is a cleaned derivative and should not be treated as the original source dataset.

## Citation

Please cite the original dataset:

```bibtex
@misc{kimi_k25_1000000x,
  title={KIMI-K2.5-1000000x},
  author={ianncity},
  year={2026},
  publisher={Hugging Face},
  url={https://huggingface.co/datasets/ianncity/KIMI-K2.5-1000000x}
}
```

You can additionally cite this cleaned derivative release:

```bibtex
@misc{kimi_k25_reasoning_1m_cleaned,
  title={Kimi-K2.5-Reasoning-1M-Cleaned},
  author={Jackrong},
  year={2026},
  publisher={Hugging Face},
  url={https://huggingface.co/datasets/Jackrong/Kimi-K2.5-Reasoning-1M-Cleaned}
}
```
