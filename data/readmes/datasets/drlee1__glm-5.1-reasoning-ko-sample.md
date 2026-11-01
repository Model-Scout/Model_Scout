---
license: apache-2.0
language:
- ko
- en
tags:
- reasoning
- translation
- korean
- chain-of-thought
- distillation
size_categories:
- n<1K
source_datasets:
- Jackrong/GLM-5.1-Reasoning-1M-Cleaned
- Kassadin88/GLM-5.1-1000000x
---

# GLM-5.1-Reasoning Korean Translation (Sample)

A small test sample (10 items) translated into Korean from
[Jackrong/GLM-5.1-Reasoning-1M-Cleaned](https://huggingface.co/datasets/Jackrong/GLM-5.1-Reasoning-1M-Cleaned),
which is itself a cleaned derivative of
[Kassadin88/GLM-5.1-1000000x](https://huggingface.co/datasets/Kassadin88/GLM-5.1-1000000x)
(reasoning traces distilled from GLM-5.1).

This sample exists as an early quality check before scaling translation to a
larger subset.

## License & Attribution

Released under **Apache 2.0**, inheriting the license of both upstream sources.

You **must** retain attribution when using or redistributing this dataset.
Please cite the original sources first:

```bibtex
@misc{glm51-1000000x,
  title={GLM-5.1-1000000x: One Million Reasoning Traces Distilled from GLM-5.1},
  author={Kassadin88},
  year={2026},
  publisher={HuggingFace},
  url={https://huggingface.co/datasets/Kassadin88/GLM-5.1-1000000x}
}

@misc{glm51_reasoning_1m_cleaned,
  title={GLM-5.1-Reasoning-1M-Cleaned},
  author={Jackrong},
  year={2026},
  publisher={HuggingFace},
  url={https://huggingface.co/datasets/Jackrong/GLM-5.1-Reasoning-1M-Cleaned}
}
```

## Modifications from upstream

- Sampled 10 items (`seed=42`) from the `main` config
- Translated `input` and `output` fields from English into Korean
- Original English fields are preserved alongside the Korean translations

The teacher model behind the reasoning traces is **GLM-5.1** (this happens
upstream and is unchanged here).

## Schema

Each line in `data/sample_translated.jsonl` contains:

| field | description |
| --- | --- |
| `id` | original sample id |
| `domain` | original domain field |
| `meta` | original meta object (token counts, teacher model) |
| `input_en` | original English prompt |
| `output_en` | original English reasoning + answer (with `<think>` tags) |
| `input_ko` | Korean translation of the prompt |
| `output_ko` | Korean translation of the reasoning + answer |
| `translation_seconds` | wall-clock time to translate this item |

## Translation procedure

- Model: `gpt-5.4-mini`
- `<think>...</think>` reasoning blocks, LaTeX, and markdown structure are
  preserved verbatim
- Code, identifiers, and conventional English proper nouns are left untranslated

Note on translation provider: translations were produced by an OpenAI model.
Downstream users planning to use this data for training models that may
compete with OpenAI should review OpenAI's then-current Terms of Use.
