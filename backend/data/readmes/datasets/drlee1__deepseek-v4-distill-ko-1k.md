---
license: mit
language:
- ko
- en
tags:
- reasoning
- chain-of-thought
- translation
- korean
- distillation
- supervised-fine-tuning
size_categories:
- 1K<n<10K
source_datasets:
- Jackrong/DeepSeek-V4-Distill-8000x
- Jackrong/GLM-5.1-Reasoning-1M-Cleaned
task_categories:
- text-generation
- translation
configs:
- config_name: default
  data_files:
    - split: train
      path: data/translated_1000.jsonl
---

# DeepSeek-V4-Distill — Korean Translation (1K Sample)

A 1,000-item Korean translation derived from
[**Jackrong/DeepSeek-V4-Distill-8000x**](https://huggingface.co/datasets/Jackrong/DeepSeek-V4-Distill-8000x),
which itself contains reasoning traces distilled from **DeepSeek-V4-Flash**.

This is an early-stage **test sample** intended to validate the translation
pipeline (model, prompt, schema) before scaling to the full 7,716-item
dataset. The translations preserve the original `<think>...</think>` reasoning
blocks and structural formatting.

> 🛈 **Status**: experimental sample, not production-ready.

## Quick start

```python
from datasets import load_dataset

ds = load_dataset("drlee1/deepseek-v4-distill-ko-1k", split="train")
print(ds[0]["input_ko"])
print(ds[0]["output_ko"])
```

## How the data was produced

1. **Sample**: 1,000 rows drawn deterministically from the `train` split
   (`seed=42`, HuggingFace `datasets.shuffle().select(range(1000))`).
2. **Translate**: each sample's `input` and `output` fields were translated
   independently from English into Korean using
   `gpt-5.4-nano-2026-03-17`.
3. **Token annotation**: every English/Korean field is tokenized with
   `tiktoken` `o200k_base` and counts are stored alongside the text.

### Translation prompt

The translator was instructed to:

- Translate prose into natural, fluent Korean.
- **Preserve** `<think>...</think>` tags, markdown, numbered lists, code
  blocks, LaTeX, and inline formatting verbatim.
- **Not translate** code, identifiers, math symbols, or proper nouns that are
  conventionally kept in English.
- **Not summarize or restructure** the reasoning steps inside `<think>...</think>`.

## Schema

Each line is a JSON object with the following fields:

| Field | Type | Description |
| --- | --- | --- |
| `id` | string | Original sample id (32-char hex). |
| `domain` | string | Original domain field. All `main` in this sample. |
| `meta` | object | Original metadata: `input_tokens`, `output_tokens` (DeepSeek-V4-Flash counts), `teacher_model`. |
| `input_en` | string | Original English prompt. |
| `output_en` | string | Original English reasoning + answer (with `<think>...</think>`). |
| `input_ko` | string \| null | Korean translation of `input_en`. Null only on policy-rejected items. |
| `output_ko` | string \| null | Korean translation of `output_en`. Null only on policy-rejected items. |
| `tokens` | object | `tokenizer` (`o200k_base`), per-field token counts (`input_en`, `output_en`, `input_ko`, `output_ko`), `en_total`, `ko_total`, `ko_en_ratio`. |
| `translation` | object | `model` (`gpt-5.4-nano-2026-03-17`), `api_input_tokens`, `api_output_tokens`. |

## Statistics (n=1,000)

### Coverage

| | Count |
| --- | --: |
| Total rows | 1,000 |
| Both `input_ko` + `output_ko` present | 999 |
| Partial (1 field null) | 1 |
| Missing both | 0 |
| Unique `id`s | 1,000 |

The single partial row is item `3d29d5b47d4cfd291b036c6cf5a60aac`. Its
English `output` (an HTML/CSS code-snippet completion task) was rejected by
the OpenAI moderation layer with `invalid_prompt`, so `output_ko` is `null`
while `input_ko` is filled normally.

### Token length distributions

Counts are computed with the `o200k_base` tokenizer.

| Field | min | median | mean | p95 | max |
| --- | --: | --: | --: | --: | --: |
| `input_en` | 3 | 48 | 111 | 482 | 1,541 |
| `output_en` | 52 | 1,815 | 2,000 | 4,278 | 8,025 |
| `input_ko` | 6 | 88 | 145 | 529 | 2,991 |
| `output_ko` | 4 | 2,168 | 2,492 | 5,385 | 8,439 |

`ko_en_ratio` (combined Korean tokens / combined English tokens):

- mean ≈ **1.29**, median ≈ **1.31**, p95 ≈ **1.61**

Korean tends to use ~30% more tokens than the English original under
`o200k_base`.

### Translation cost telemetry (this sample)

- API input tokens used: **2,400,603**
- API output tokens used: **2,640,402**
- Approximate cost (mixed batch+real-time): **≈ $3.78 USD**

## Limitations

- **Sample scale**: 1,000 items. Not large enough for full-distribution
  conclusions on rare categories.
- **Single translator model**: outputs reflect the lexical and stylistic
  preferences of `gpt-5.4-nano-2026-03-17`. Some technical phrasing may
  drift from native Korean academic conventions.
- **Moderation gaps**: 1 row has a null `output_ko` due to the OpenAI policy
  filter, leaving an asymmetry. Consumers should either drop that row or
  re-translate it with a different provider.
- **No human review**: translations have not been validated by a Korean
  bilingual reviewer.
- **Test pipeline**: sub-batches were cancelled mid-flight; this is acceptable
  for a sample, but is not the recommended path for production.

## Citations

Please cite **all** upstream sources when using this dataset:

```bibtex
@misc{deepseek_v4_distill_8000x,
  title={DeepSeek-V4-Distill-8000x},
  author={Jackrong},
  year={2026},
  publisher={HuggingFace},
  url={https://huggingface.co/datasets/Jackrong/DeepSeek-V4-Distill-8000x}
}

@misc{glm51_reasoning_1m_cleaned,
  title={GLM-5.1-Reasoning-1M-Cleaned},
  author={Jackrong},
  year={2026},
  publisher={HuggingFace},
  url={https://huggingface.co/datasets/Jackrong/GLM-5.1-Reasoning-1M-Cleaned}
}

@misc{deepseek_v4_distill_ko_1k,
  title={DeepSeek-V4-Distill — Korean Translation (1K Sample)},
  author={drlee1},
  year={2026},
  publisher={HuggingFace},
  url={https://huggingface.co/datasets/drlee1/deepseek-v4-distill-ko-1k}
}
```

Translations were produced by the OpenAI `gpt-5.4-nano-2026-03-17` model.
Downstream users planning to train models that compete with OpenAI should
review OpenAI's then-current Terms of Use.
