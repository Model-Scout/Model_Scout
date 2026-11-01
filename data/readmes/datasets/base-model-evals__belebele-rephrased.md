---
dataset_info:
- config_name: all
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: original_question
    dtype: string
  - name: original_choices
    list: string
  - name: correct_index
    dtype: int64
  - name: context
    dtype: string
  - name: rephrased_prefix
    dtype: string
  - name: rephrased_choices
    list: string
  - name: rephrasing_model
    dtype: string
  - name: judge_overall_score
    dtype: float64
  splits:
  - name: train
    num_bytes: 159584
    num_examples: 157
  download_size: 119436
  dataset_size: 159584
- config_name: high_quality
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: original_question
    dtype: string
  - name: original_choices
    list: string
  - name: correct_index
    dtype: int64
  - name: context
    dtype: string
  - name: rephrased_prefix
    dtype: string
  - name: rephrased_choices
    list: string
  - name: rephrasing_model
    dtype: string
  - name: judge_overall_score
    dtype: float64
  splits:
  - name: train
    num_bytes: 126451
    num_examples: 125
  download_size: 97232
  dataset_size: 126451
- config_name: low_quality
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: original_question
    dtype: string
  - name: original_choices
    list: string
  - name: correct_index
    dtype: int64
  - name: context
    dtype: string
  - name: rephrased_prefix
    dtype: string
  - name: rephrased_choices
    list: string
  - name: rephrasing_model
    dtype: string
  - name: judge_overall_score
    dtype: float64
  splits:
  - name: train
    num_bytes: 33133
    num_examples: 32
  download_size: 33098
  dataset_size: 33133
configs:
- config_name: all
  data_files:
  - split: train
    path:
    - high_quality/train-*
    - low_quality/train-*
- config_name: high_quality
  data_files:
  - split: train
    path: high_quality/train-*
- config_name: low_quality
  data_files:
  - split: train
    path: low_quality/train-*
language:
- en
- fr
- ko
- tr
license: cc-by-nc-sa-4.0
task_categories:
- multiple-choice
- text-generation
tags:
- base-model-evaluation
- completion-format
---
# belebele (rephrased for base-model evaluation)

Belebele reading-comprehension items rewritten from question format into completion/cloze format for base (non-instruction-tuned) language model evaluation.

Base (non-instruction-tuned) language models often can't follow question-style
prompts like "What is the capital of Turkey?" -- that phrasing is suited to
instruction-tuned models. Each item here has been rewritten into a natural
completion prefix (e.g. "The capital of Turkey is ...") that a base model can
be scored on via loglikelihood over the candidate continuations, while
preserving the original choices, correct answer, and meaning.

## Configs

Every item is kept (nothing is silently dropped), split into three configs by
judge-model quality score (mean of {faithfulness, fluency, naturalness,
clean, overall} judge scores, `judge_overall_score` column, 1-5 scale) so you
can pick the tradeoff that fits your use:

- **`all`** (157 items): everything, unfiltered.
- **`high_quality`** (125 items): `judge_overall_score >= 3.0`.
- **`low_quality`** (32 items): `judge_overall_score < 3.0` -- kept for
  transparency/error-analysis, not recommended for actual evaluation use.

```python
from datasets import load_dataset
ds = load_dataset("base-model-evals/belebele-rephrased", "high_quality")
```

- **Source benchmark**: [facebook/belebele](https://huggingface.co/datasets/facebook/belebele) (license: cc-by-sa-4.0)
- **Rephrasing model**: [CohereForAI/aya-expanse-8b](https://huggingface.co/CohereForAI/aya-expanse-8b) (license: cc-by-nc-4.0)
- **Languages**: en, fr, ko, tr

## License

This dataset is licensed **cc-by-nc-sa-4.0**, combining the source
benchmark's license with the rephrasing model's license (the rephrased text
is that model's output):

CohereForAI/aya-expanse-8b is licensed CC-BY-NC-4.0 (NonCommercial). Its Acceptable Use Policy (https://docs.cohere.com/docs/cohere-labs-acceptable-use-policy) specifically restricts generating synthetic benchmark data commercially, so this NonCommercial restriction is carried through to the rephrased text here regardless of the source benchmark's own license.

## Citation

If you use this dataset, please cite both the original benchmark and the
rephrasing model:

```bibtex
@inproceedings{bandarkar-etal-2024-belebele,
    title = "The Belebele Benchmark: a Parallel Reading Comprehension Dataset in 122 Language Variants",
    author = "Bandarkar, Lucas and Liang, Davis and Muller, Benjamin and Artetxe, Mikel and Shukla, Satya Narayan and Husa, Donald and Goyal, Naman and Krishnan, Abhinandan and Zettlemoyer, Luke and Khabsa, Madian",
    booktitle = "Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = aug,
    year = "2024",
    address = "Bangkok, Thailand and virtual meeting",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.acl-long.44",
    pages = "749--775",
}
```

```bibtex
@misc{cohereforai2024ayaexpanse,
      title={Aya Expanse: Combining Research Breakthroughs for a New Multilingual Frontier},
      author={{Cohere For AI}},
      year={2024},
      url={https://huggingface.co/CohereForAI/aya-expanse-8b},
}
```

## Fields

- `id`: source item id
- `language`: ISO 639-1 language code
- `original_question`, `original_choices`, `correct_index`: the source item, unmodified
- `context`: supporting passage, if any (Belebele only)
- `rephrased_prefix`, `rephrased_choices`: the completion-format rewrite -- `rephrased_prefix + " " + rephrased_choices[correct_index]` is the correct continuation
- `rephrasing_model`: which model produced the rewrite
- `judge_overall_score`: mean judge-model quality score (1-5), if available
