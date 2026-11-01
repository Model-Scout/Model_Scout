---
language:
  - ko
  - en
license: other
tags:
  - dpo
  - preference
  - instruction-tuning
  - korean
  - english
  - bilingual
  - rlhf
size_categories:
  - 100K<n<1M
task_categories:
  - text-generation
---

# Keural DPO Dataset

A merged bilingual Korean-English preference dataset compiled for DPO (Direct Preference Optimization) training of the [Keural 14.8B](https://huggingface.co/mkd-hossain/keural-14.8b-sft) language model.

---

## Dataset Summary

| Field | Value |
|---|---|
| **Total samples** | 233,227 |
| **Languages** | Korean, English |
| **Format** | Prompt + Chosen + Rejected |
| **Sources** | 3 curated datasets |
| **Purpose** | DPO alignment training |

### Source Breakdown

| Source | Language | Samples | Description |
|---|---|---|---|
| `HuggingFaceH4/ultrafeedback_binarized` | English | 60,630 | High-quality AI feedback preference pairs |
| `Anthropic/hh-rlhf` | English | 159,872 | Helpful and harmless preference pairs |
| `Ja-ck/Orca-DPO-Pairs-KO` | Korean | 12,725 | Korean instruction preference pairs |
| **Total** | **Korean + English** | **233,227** | |

---

## Dataset Fields

| Field | Type | Description |
|---|---|---|
| `prompt` | string | The user question or instruction |
| `chosen` | string | The preferred (better) assistant response |
| `rejected` | string | The dispreferred (worse) assistant response |
| `language` | string | Language of the sample (`en` or `ko`) |

---

## Sample Format

```json
{
  "prompt": "What is the capital of South Korea?",
  "chosen": "The capital of South Korea is Seoul. It is the largest city in Korea with a population of about 10 million people.",
  "rejected": "South Korea is a country in Asia. The capital is Busan which is a port city.",
  "language": "en"
}
```

```json
{
  "prompt": "부산은 어디에 있나요?",
  "chosen": "부산은 대한민국 남동부에 위치한 항구 도시입니다. 서울 다음으로 두 번째로 큰 도시이며, 해운대 해수욕장과 자갈치 시장으로 유명합니다.",
  "rejected": "부산 부산 부산은 부산입니다. 부산은 한국의 도시입니다.",
  "language": "ko"
}
```

---

## What is DPO?

DPO (Direct Preference Optimization) is a training method that teaches a language model to **prefer better responses over worse ones** using pairs of (chosen, rejected) answers for the same prompt.

Unlike RLHF which requires a separate reward model, DPO directly optimizes the language model using preference pairs — making it simpler, more stable, and computationally efficient.

### What DPO fixes:
- Hallucination (making up false facts) ✓
- Repetitive responses ✓
- Harmful or unsafe outputs ✓
- Low quality or vague answers ✓
- Wrong language responses ✓

---

## Usage

### Load the dataset

```python
from datasets import load_from_disk

ds = load_from_disk("data/dpo_dataset")
print(len(ds))           # 233227
print(ds.column_names)   # ['prompt', 'chosen', 'rejected', 'language']
print(ds[0])
```

### Load from HuggingFace

```python
from datasets import load_dataset

ds = load_dataset("mkd-hossain/keural-dpo-dataset", split="train")
print(len(ds))
```

### Filter by language

```python
korean_ds  = ds.filter(lambda x: x["language"] == "ko")
english_ds = ds.filter(lambda x: x["language"] == "en")
print(f"Korean:  {len(korean_ds):,}")
print(f"English: {len(english_ds):,}")
```

---

## Training Context

This dataset was compiled specifically for DPO training of the **Keural 14.8B MoE** bilingual language model:

| Stage | Details |
|---|---|
| Base model | Keural 14.8B MoE (Mixtral architecture) |
| Pretraining | ~64.56B tokens, Korean + English web text |
| Annealing | ~5.16B tokens, clean filtered data |
| SFT | 1,134,119 ChatML samples, `mkd-chanwoo/keural-SFT` |
| **DPO (this dataset)** | **233,227 preference pairs** |

---

## Language Distribution

| Language | Samples | Percentage |
|---|---|---|
| English | 220,502 | 94.5% |
| Korean | 12,725 | 5.5% |

---

## License

This dataset is a compilation of multiple sources with different licenses:

| Source | License |
|---|---|
| `HuggingFaceH4/ultrafeedback_binarized` | MIT |
| `Anthropic/hh-rlhf` | MIT |
| `Ja-ck/Orca-DPO-Pairs-KO` | Apache 2.0 |

---

## Citation

```bibtex
@misc{keural-dpo-2026,
  title  = {Keural DPO Dataset: Bilingual Korean-English Preference Data},
  author = {MKD Hossain},
  year   = {2026},
  url    = {https://huggingface.co/datasets/mkd-hossain/keural-dpo-dataset}
}
```

---

*Compiled for the Keural project — a bilingual Korean-English MoE language model trained from scratch on KT Cloud NIPA2-H200 infrastructure.*
