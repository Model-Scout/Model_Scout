---
language:
- ko
- en
license: other
task_categories:
- text-generation
- question-answering
pretty_name: Keural SFT Dataset v2
size_categories:
- 100K<n<1M
tags:
- instruction-tuning
- sft
- korean
- english
- math
- code
---

# Keural SFT Dataset v2

A Korean-first supervised fine-tuning dataset prepared for Keural by MKD.

## Dataset Summary

- Total examples: **151,500**
- Format: JSONL
- Schema: conversational `messages`
- Korean share: **55.0%**
- English and other share: **45.0%**
- SHA-256: `8DCD281C0F3B654B2F371EA039F3DA1D55EC57F5B1159A88B5559AEF5F14B690`

## Category Composition

| Category | Description | Rows |
|---|---|---:|
| A | Korean conversation and instruction | 50,000 |
| B | Korean multiple-choice knowledge | 15,000 |
| C | English multiple-choice knowledge | 10,000 |
| D | Math reasoning: 13,600 Korean and 6,400 English | 20,000 |
| E | Code with validated Python blocks | 25,000 |
| F | General English replay | 25,000 |
| G | Long-form Korean answers | 5,000 |
| H | Keural identity and persona | 1,500 |

## Data Format

Each line is one JSON object:

```json
{
  "messages": [
    {"role": "user", "content": "User instruction"},
    {"role": "assistant", "content": "Assistant response"}
  ],
  "source_name": "source identifier",
  "license": "per-row license"
}
```

Every example ends with an assistant message and includes its source and license.

## Loading

```python
from datasets import load_dataset

dataset = load_dataset(
    "min2ju2/sft_dataset_v2",
    data_files="FINAL_v2_dataset.jsonl",
    split="train",
)
```

## Sources

The dataset includes commercially usable data derived from sources such as:

- KULLM v2
- KMMLU train and dev splits
- MMLU auxiliary train
- GSM8K train
- MetaMathQA
- MKD Korean math data
- Original upstream Magicoder datasets
- UltraChat
- Internally authored Keural identity examples

Benchmark test and prohibited validation splits were excluded.

## Licenses

This is a mixed-license dataset. Every row includes its own `license` field. Included licenses may include MIT, Apache-2.0, CC BY 4.0, CC BY-SA 4.0, and Internal.

Users must comply with each row's source license.

## Validation

The final dataset passed the automated delivery checklist:

- Valid JSON and `messages` schema
- Exact category and total row counts
- No forbidden benchmark test-split markers
- All fenced Python blocks pass `ast.parse`
- No detected incorrect AI-vendor identity claims
- Correct Korean and English MCQ answer markers
- No exact duplicate rows
- Korean share within the 55-60% target
- Per-row source and license metadata

## Intended Use

This dataset is intended for supervised fine-tuning of Korean-English conversational language models.

## Limitations

- Automated validation cannot guarantee semantic correctness for every example.
- Multiple-choice rationales are concise and may not contain detailed reasoning.
- Long-form Korean examples were selected using structural and length heuristics.
- Users should perform their own sample review before training or redistribution.
- This dataset must not be used as a benchmark evaluation set.

## Build Pipeline

https://github.com/mkd-minju/sft_dataset_v2

## License and Copyright Notice / 라이선스 및 저작권 표시

This dataset is a mixed-license compilation as described above; each row's underlying source license must be respected. **"Keural SFT Dataset v2" is a dataset produced by 주식회사 MKD (MKD Inc.).** The collection, filtering, and validation pipeline (§Build Pipeline) was carried out by MKD Inc.; underlying source data retains the licenses of its original upstream publishers as listed above.