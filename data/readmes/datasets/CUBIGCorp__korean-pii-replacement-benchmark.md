---
license: cc-by-4.0
language:
- ko
pretty_name: Korean PII Replacement Benchmark
size_categories:
- 1K<n<10K
task_categories:
- question-answering
tags:
- pii
- privacy
- masking
- korean
- benchmark
configs:
- config_name: all
  default: true
  data_files:
  - split: test
    path:
    - data/openpii/test.jsonl
    - data/kdpii/test.jsonl
- config_name: openpii
  data_files:
  - split: test
    path: data/openpii/test.jsonl
- config_name: kdpii
  data_files:
  - split: test
    path: data/kdpii/test.jsonl
dataset_info:
- config_name: all
  features:
  - name: id
    dtype: string
  - name: source
    dtype: string
  - name: source_id
    dtype: string
  - name: source_index
    dtype: int64
  - name: source_split
    dtype: string
  - name: text
    dtype: string
  - name: pii_spans
    list:
    - name: end
      dtype: int64
    - name: label
      dtype: string
    - name: start
      dtype: int64
    - name: value
      dtype: string
  - name: lookup_category
    dtype: string
  - name: task_id_single
    dtype: string
  - name: question_single
    dtype: string
  - name: answer_single
    dtype: string
  - name: task_id_multi
    dtype: string
  - name: question_multi
    dtype: string
  - name: answer_multi
    list: string
  - name: text_blackout
    dtype: string
  - name: text_hash
    dtype: string
  - name: text_typed
    dtype: string
  - name: hash_mapping
    list:
    - name: label
      dtype: string
    - name: masked
      dtype: string
    - name: original
      dtype: string
  - name: typed_mapping
    list:
    - name: label
      dtype: string
    - name: masked
      dtype: string
    - name: original
      dtype: string
  - name: aliases
    list:
    - name: native_value
      dtype: string
    - name: value
      dtype: string
- config_name: openpii
  features:
  - name: id
    dtype: string
  - name: source
    dtype: string
  - name: source_id
    dtype: string
  - name: source_index
    dtype: int64
  - name: source_split
    dtype: string
  - name: text
    dtype: string
  - name: pii_spans
    list:
    - name: end
      dtype: int64
    - name: label
      dtype: string
    - name: start
      dtype: int64
    - name: value
      dtype: string
  - name: lookup_category
    dtype: string
  - name: task_id_single
    dtype: string
  - name: question_single
    dtype: string
  - name: answer_single
    dtype: string
  - name: task_id_multi
    dtype: string
  - name: question_multi
    dtype: string
  - name: answer_multi
    list: string
  - name: text_blackout
    dtype: string
  - name: text_hash
    dtype: string
  - name: text_typed
    dtype: string
  - name: hash_mapping
    list:
    - name: label
      dtype: string
    - name: masked
      dtype: string
    - name: original
      dtype: string
  - name: typed_mapping
    list:
    - name: label
      dtype: string
    - name: masked
      dtype: string
    - name: original
      dtype: string
  - name: aliases
    list:
    - name: native_value
      dtype: string
    - name: value
      dtype: string
- config_name: kdpii
  features:
  - name: id
    dtype: string
  - name: source
    dtype: string
  - name: source_id
    dtype: string
  - name: source_index
    dtype: int64
  - name: source_split
    dtype: string
  - name: text
    dtype: string
  - name: pii_spans
    list:
    - name: end
      dtype: int64
    - name: label
      dtype: string
    - name: start
      dtype: int64
    - name: value
      dtype: string
  - name: lookup_category
    dtype: string
  - name: task_id_single
    dtype: string
  - name: question_single
    dtype: string
  - name: answer_single
    dtype: string
  - name: task_id_multi
    dtype: string
  - name: question_multi
    dtype: string
  - name: answer_multi
    list: string
  - name: text_blackout
    dtype: string
  - name: text_hash
    dtype: string
  - name: text_typed
    dtype: string
  - name: hash_mapping
    list:
    - name: label
      dtype: string
    - name: masked
      dtype: string
    - name: original
      dtype: string
  - name: typed_mapping
    list:
    - name: label
      dtype: string
    - name: masked
      dtype: string
    - name: original
      dtype: string
  - name: aliases
    list:
    - name: native_value
      dtype: string
    - name: value
      dtype: string
---

# Korean PII Replacement Benchmark

This benchmark measures how the **form of replacement** affects an LLM's
ability to look up and extract identifiers from Korean text. It contains
**1,000 source items: 500 OpenPII documents and 500 KDPII dialogues**.
Each item has two questions evaluated under four conditions. The saved
answers therefore contain 8,000 scored responses, not 8,000 independent documents.

PII locations and types are supplied by the source annotations. This is a
controlled replacement experiment, **not a PII detection benchmark or an
end-to-end evaluation of the LLM Capsule product**. Typed tokens reproduce
the typed, entity-indexed replacement principle associated with LLM Capsule.

## Files

```text
README.md
VERSION
LICENSE
benchmark.json
data/
  openpii/test.jsonl         # 500 documents, questions, gold, masks and restoration tables
  kdpii/test.jsonl           # 500 dialogues in the same schema
results/
  answers.jsonl             # 8,000 saved answer strings and completion status
  reference-scores.jsonl    # frozen per-answer scoring results
  reference-summary.json   # 16 aggregate cells, each with n=500
scoring/
  score.py                  # offline standard-library scorer
  README.md                 # commands, schemas and exact scoring rules
```

The repository contains no model inference runner, API request/response
envelopes, authentication configuration or model weights. Saved answer text
is included so the published scores can be recomputed offline.

## Load the data

JSONL is UTF-8 JSON, with one source item per line. The explicit YAML
configurations above keep saved results out of the dataset viewer.

```python
from datasets import load_dataset

data = load_dataset("CUBIGCorp/korean-pii-replacement-benchmark", "all", split="test")
# The two individual configurations are "openpii" and "kdpii".
```

For a local copy, the same JSONL files can be read with Python's standard
library; the scorer does not require the `datasets` package.

```python
import json

with open("data/openpii/test.jsonl", encoding="utf-8") as handle:
    documents = [json.loads(line) for line in handle]
```

`test` names this derived evaluation sample, not an official source split.
OpenPII items came from its Korean validation data; KDPII Revised was
distributed as one integrated set, without official train/dev/test splits.

## Tasks and conditions

- **Single-value lookup:** return one requested identifier. Exact match after
  restoration and the frozen normalization/alias rules receives 1; otherwise 0.
- **Multi-value extraction:** return all identifiers requested by the prompt
  as a JSON array of strings. The score is value-set F1 for each item, averaged
  across 500 items per source. This is not a span-level NER F1.

Read each question's exact identifier scope. Extraction prompts exclude names,
addresses, dates and several other PII types even though their annotated spans
are masked. KDPII account/card/driver-license answers use the number portion,
excluding bank, issuer or region names. The supplied aliases preserve that rule.

| Condition | Text field | Answer handling |
| --- | --- | --- |
| `raw` | `text` | no restoration |
| `blackout` | `text_blackout` | `***`, no restoration |
| `hash_restore` | `text_hash` | restore with `hash_mapping` |
| `typed_restore` | `text_typed` | restore with `typed_mapping` |

Within an item, the same value and type receive the same token. Hash tokens
are the frozen 12-character SHA-256 prefixes; typed tokens look like
`[전화번호_A]`. All masked conditions use the same gold PII spans, excluding
TITLE (honorifics). Restoration tables and original values stay local and
must not be sent to the answering model. Do not include the gold answers or
aliases in a model prompt.

## Results

Answering model: `gpt-6-luna`, one response per item/task/condition.

Original-text answers were reused from an earlier run with identical settings (model, system prompt, reasoning effort, seed and token limit); 385 of its OpenPII requests were routed through OpenRouter to the same OpenAI model (384 responses, one timeout).
Scores below are percentages, rounded to one decimal; stored scores use 0–1.

| Source | Task | Original | Stars | Hash + restore | Typed + restore |
| --- | --- | --- | --- | --- | --- |
| OpenPII | Lookup accuracy | 97.4 | 0.0 | 72.6 | 99.4 |
| OpenPII | Extraction F1 | 98.0 | 0.0 | 76.7 | 99.3 |
| KDPII | Lookup accuracy | 85.8 | 0.0 | 71.0 | 93.6 |
| KDPII | Extraction F1 | 96.3 | 0.0 | 67.4 | 96.3 |

Each of the 16 cells averages exactly 500 saved responses. Failures are retained
as zero scores. KDPII extraction means round to the same number but differ
before rounding: original 96.3457142857143, typed 96.3329725829726.

## Recompute the published scores

From this repository's root, using Python 3.9 or later:

```bash
python3 -S -B scoring/score.py \
  --samples data/openpii/test.jsonl data/kdpii/test.jsonl \
  --predictions results/answers.jsonl \
  --reference-scores results/reference-scores.jsonl \
  --reference-summary results/reference-summary.json
```

The command succeeds only if all 8,000 per-answer results and all 16 aggregate
cells reproduce the frozen references. See [scoring/README.md](scoring/README.md)
to score another model's saved answers or check error handling.

## Sample construction and limitations

- The samples were selected from 2,003 task-eligible OpenPII items and 2,184
  task-eligible KDPII items (5,273 and 4,981 Korean source items respectively).
  Sampling used at least 50 items per lookup category, with remaining slots
  allocated by source category frequency, and stratification by length and PII
  count. This is not a prevalence-weighted sample of all source content.
- Questions and gold answers were generated by code from the source annotations,
  rather than newly labeled by an LLM. Included spans, masks, questions and gold
  retain the frozen experiment's definitions and annotation limitations.
- Gold PII spans and types are supplied; no detector is evaluated here.
- One answering model and one run per condition; only lookup and extraction
  tasks are covered. These results do not establish statistical equivalence
  to original text or generalize to all LLM tasks.
- Typed tokens explicitly provide type information. Slightly higher observed
  scores are not evidence that masking generally improves model quality.
- Stars cannot recover original values; their zero scores apply to these
  original-value tasks, not to every possible use of masking.
- This is an openly released evaluation sample with visible gold answers;
  do not treat it as a hidden test set after training on it.

## Source data, attribution and license

- **OpenPII 1.5M**, Ai4Privacy / Ai Suisse SA:
  [source dataset](https://huggingface.co/datasets/ai4privacy/pii-masking-openpii-1.5m),
  licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
- **KDPII DATASET REVISED**, creators and contributors listed in the
  [Zenodo source record](https://zenodo.org/records/16759166), Yonsei University HamSaeM Kim's Lab; TSCIENTIFIC Co.,Ltd; KIM, HANSAEM; Li, Fei; KANG, YEJEE; PARK, SEOYOON; YEONJI, YEONJI:
  [DOI 10.5281/zenodo.16759166](https://doi.org/10.5281/zenodo.16759166),
  licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

CUBIG modifications: sample selection, source IDs, task-specific question/gold
generation, identifier-number aliases, gold-span replacement text and restoration
tables, saved model answers, and scoring results. Original source text is retained.
Source creators do not endorse this benchmark. Credit both original datasets
when redistributing this derived sample. This release is distributed under
CC BY 4.0; see [LICENSE](LICENSE).

## Evaluate your own masking tool

To test your own masking tool or documents under the same setup, [request a demo](https://llmcapsule.ai/ko/request-a-demo/?utm_source=huggingface&utm_medium=referral&utm_campaign=korean-pii-benchmark&utm_content=dataset_card). Built by [CUBIG](https://www.cubig.ai), the team behind [LLM Capsule](https://llmcapsule.ai/ko/?utm_source=huggingface&utm_medium=referral&utm_campaign=korean-pii-benchmark&utm_content=dataset_card).

## Citation

```bibtex
@misc{cubig2026koreanpiireplacement,
  title  = {Korean PII Replacement Benchmark},
  author = {CUBIG},
  year   = {2026},
  url    = {https://huggingface.co/datasets/CUBIGCorp/korean-pii-replacement-benchmark}
}
```

Release: v0.13. Dataset repository and results-page publication are separate
deployment steps; this folder contains the dataset repository contents.
