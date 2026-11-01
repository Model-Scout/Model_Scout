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
- glm
- glm-5.1
- cleaned
configs:
  - config_name: main
    default: true
    data_files:
      - split: train
        path: "main.jsonl"
  - config_name: PHD-Science
    data_files:
      - split: train
        path: "PHD-Science.jsonl"
  - config_name: Multilingual-STEM
    data_files:
      - split: train
        path: "Multilingual-STEM.jsonl"
  - config_name: Math
    data_files:
      - split: train
        path: "Math.jsonl"
---

# GLM-5.1-Reasoning-1M-Cleaned

![GLM-5.1](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/Bn6WT4WoRayEe8l-D-_TL.jpeg)

**GLM-5.1-Reasoning-1M-Cleaned** is a cleaned and reformatted derivative of [Kassadin88/GLM-5.1-1000000x](https://huggingface.co/datasets/Kassadin88/GLM-5.1-1000000x). It preserves the original four-subset layout (`main`, `PHD-Science`, `Multilingual-STEM`, `Math`) while converting every example into a unified SFT-ready schema with explicit `conversations`, `input`, `output`, `domain`, and `meta` fields.

This release was prepared from the original dataset published by **Kassadin88**. 

## Summary

![bench_51](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/GtLN3BAse6QsnpvZfBdHv.png)


- Teacher model in the data: **GLM-5.1**
- Total processed records: **766,535**
- Total kept records: **746,321**
- Total removed records: **20,214**
- Subset layout preserved exactly as the source dataset: `main`, `PHD-Science`, `Multilingual-STEM`, `Math`

## Included Content

- `main`: general reasoning and instruction-following data.
- `PHD-Science`: graduate-level physics, chemistry, and biology reasoning traces.
- `Multilingual-STEM`: multilingual STEM reasoning data, including Chinese, English, and other languages present in the source release.
- `Math`: mathematics-heavy reasoning and proof-style responses.

## Cleaning and Reformatting

The raw source dataset mixed two answer layouts:

1. Standard `<think>...</think>` reasoning tags.
2. A non-standard short-dash wrapper around the reasoning section.

This cleaned release normalizes both styles into a single output format:

```json
{
  "id": "md5-hash-of-domain-input-reasoning-answer",
  "conversations": [
    {"from": "human", "value": "user prompt"},
    {"from": "gpt", "value": "<think>\nreasoning trace\n</think>\n\nfinal answer"}
  ],
  "input": "user prompt",
  "output": "<think>\nreasoning trace\n</think>\n\nfinal answer",
  "domain": "subset/domain name from the original _id prefix",
  "meta": {
    "input_tokens": 123,
    "output_tokens": 456,
    "teacher_model": "GLM-5.1"
  }
}
```


### Removed data

The cleaning pipeline removed records with:

- incomplete or obviously truncated answers,
- repeated reasoning paragraphs or duplicated answer segments,
- refusal-style answers,
- unparseable reasoning/answer boundaries,
- exact duplicate records after normalization.

## Subset Statistics

| Subset | Processed | Kept | Removed | File Size | Median Input Tokens | Median Output Tokens |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| main | 547,292 | 527,737 | 19,555 | 18.28 GB | 50 | 3008 |
| PHD-Science | 103,759 | 103,706 | 53 | 3.72 GB | 45 | 3387 |
| Multilingual-STEM | 93,032 | 92,781 | 251 | 3.53 GB | 66 | 4084 |
| Math | 22,452 | 22,097 | 355 | 4.03 GB | 59 | 24498 |

## Filter Statistics

| Subset | Issue | Removed |
| --- | --- | ---: |
| main | incomplete_output | 12,726 |
| main | repeated_paragraph | 6,152 |
| main | refusal_answer | 638 |
| main | unparseable_output | 38 |
| main | duplicate_record | 1 |
| PHD-Science | incomplete_output | 33 |
| PHD-Science | repeated_paragraph | 19 |
| PHD-Science | refusal_answer | 1 |
| Multilingual-STEM | repeated_paragraph | 116 |
| Multilingual-STEM | incomplete_output | 88 |
| Multilingual-STEM | refusal_answer | 28 |
| Multilingual-STEM | unparseable_output | 19 |
| Math | repeated_paragraph | 303 |
| Math | incomplete_output | 26 |
| Math | unparseable_output | 26 |

## Additional Token Statistics

| Subset | Mean Input Tokens | P95 Input Tokens | Mean Output Tokens | P95 Output Tokens |
| --- | ---: | ---: | ---: | ---: |
| main | 118.62 | 515 | 4482.35 | 15041 |
| PHD-Science | 45.05 | 56 | 4387.73 | 10447 |
| Multilingual-STEM | 79.91 | 192 | 5461.45 | 11034 |
| Math | 62.01 | 89 | 28133.4 | 64633 |



## Data Structure

Each example is a single-turn reasoning distillation sample:

- `conversations[0]`: the user prompt.
- `conversations[1]`: the model response with reasoning wrapped in `<think>...</think>` and the final answer after the closing tag.
- `input`: prompt-only view for training pipelines that prefer flat prompt fields.
- `output`: tagged answer-only view for training pipelines that prefer flat completion fields.
- `domain`: original subset/domain name extracted from the source record ID.
- `meta`: lightweight per-example metadata.

## Usage

```python
from datasets import load_dataset

main = load_dataset("Jackrong/GLM5.1-Reasoning-1M-Cleaned", "main")
science = load_dataset("Jackrong/GLM5.1-Reasoning-1M-Cleaned", "PHD-Science")
stem = load_dataset("Jackrong/GLM5.1-Reasoning-1M-Cleaned", "Multilingual-STEM")
math = load_dataset("Jackrong/GLM5.1-Reasoning-1M-Cleaned", "Math")
```

If you publish under a different namespace, replace `Jackrong/` with your actual Hugging Face username or org.

## Provenance

This dataset is derived from:

- Original dataset: [`Kassadin88/GLM-5.1-1000000x`](https://huggingface.co/datasets/Kassadin88/GLM-5.1-1000000x)
- Original author: **Kassadin88**

## Citation

Please cite the original dataset first:

```bibtex
@misc{glm51-1000000x,
  title={GLM-5.1-1000000x: One Million Reasoning Traces Distilled from GLM-5.1},
  author={Kassadin88},
  year={2026},
  publisher={HuggingFace},
  url={https://huggingface.co/datasets/Kassadin88/GLM-5.1-1000000x}
}
```

You can additionally cite this cleaned derivative release as:

```bibtex
@misc{glm51_reasoning_1m_cleaned,
  title={GLM-5.1-Reasoning-1M-Cleaned},
  author={Jackrong},
  year={2026},
  publisher={HuggingFace},
  url={https://huggingface.co/datasets/Jackrong/GLM5.1-Reasoning-1M-Cleaned}
}
```
