---
license: cc-by-4.0
language:
  - ko
task_categories:
  - text-classification
pretty_name: Natural Innocent
size_categories:
  - 1K<n<10K
tags:
  - legal
  - korean
  - criminal-law
---

# Natural Innocent

Natural Innocent is a Korean criminal-case dataset for classifying the legal
stage at which a charged act was resolved. This public release contains 3,200
case descriptions and their legal-stage labels.

Access is gated. The dataset is released under CC BY 4.0.

## Data fields

| Field | Type | Description |
|---|---|---|
| `id` | string | Stable identifier for the released record. |
| `source_document_id` | string | Identifier for the source document. |
| `text` | string | Korean case description. |
| `label` | integer | Legal-stage label defined below. |
| `split` | string | One of `train`, `validation`, or `test`. |
| `decision_year` | string | Year of the source decision. |

## Labels

| Label | Name | Description |
|---:|---|---|
| 0 | Guilty | The charged conduct resulted in a guilty determination. |
| 1 | Offense elements | One or more offense elements were not established, including the required subjective element. |
| 2 | Unlawfulness | Unlawfulness was negated by a justification or equivalent ground. |
| 3 | Culpability | Criminal responsibility was negated or excused. |

## Splits and label distribution

The original study was training-free and used the full dataset for evaluation.
The public release additionally provides a deterministic, label-stratified
80/10/10 split for researchers who may need predefined partitions in future
work; these partitions were not used as training splits in the original study.

| Split | Label 0 | Label 1 | Label 2 | Label 3 | Total |
|---|---:|---:|---:|---:|---:|
| Train | 979 | 1,183 | 319 | 79 | 2,560 |
| Validation | 122 | 148 | 40 | 10 | 320 |
| Test | 123 | 148 | 40 | 9 | 320 |
| **Total** | **1,224** | **1,479** | **399** | **98** | **3,200** |

The 3,200 records correspond to 3,200 distinct source documents. Decision
years range from 2004 through 2025.
