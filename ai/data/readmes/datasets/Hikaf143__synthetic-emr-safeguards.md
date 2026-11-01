---
license: apache-2.0
language:
- en
- ko
task_categories:
- question-answering
- summarization
size_categories:
- n<1K
tags:
- synthetic
- clinical-text
- patient-level-splits
- de-identification-demo
- evidence-grounding
dataset_info:
  features:
  - name: patient_id
    dtype: string
  - name: record_id
    dtype: string
  - name: split
    dtype: string
  - name: language
    dtype: string
  - name: note
    dtype: string
  - name: redaction_audit
    sequence: string
  - name: synthetic
    dtype: bool
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train.jsonl
  - split: validation
    path: data/validation.jsonl
  - split: test
    path: data/test.jsonl
---

# Synthetic EMR Safeguards · v1.0

**48 entirely invented Korean/English records for testing software safeguards.
No real patients, hospital exports, or external source datasets are used.**
This is not a clinical benchmark, not a model-training corpus of meaningful scale,
and not evidence of medical accuracy or certified privacy protection.

## Purpose

A reproducible fixture set for patient-level splitting, explicit identifier redaction,
extractive summaries, evidence citations, and missing-information refusals.
[Interactive demo and generator](https://huggingface.co/spaces/Hikaf143/synthetic-emr-safeguards)
include the source, tests, and evaluation report.

## Construction and provenance

Template generator `emr_core.py` version 1.0.0, prepared with AI coding assistance.
24 synthetic patient groups have two encounters each. Odd-numbered groups use English,
even-numbered groups use Korean. The content consists of invented symptoms, observations,
explicitly absent medications, allergy documentation, and imaging-report availability.
Exactly one of six fields is deliberately omitted per encounter.
Values are demonstration fixtures, not clinical recommendations.

Before export, synthetic identity labels, example email/phone strings, dates, and
ID-shaped strings are redacted using format-specific regular expressions. Raw fixture
identifiers remain reconstructable from the public generator because they are invented.
No claim of anonymizing real records is made.

## Splits and leakage controls

| Split | Patients | Records |
|---|---:|---:|
| train | 16 | 32 |
| validation | 4 | 8 |
| test | 4 | 8 |

Patient IDs are ranked by SHA256 of `emr-demo-v1:{patient_id}`. The first 16 groups
are train, next 4 validation, last 4 test. Both visits remain in the same partition.
Tests assert no patient overlap. Templates and vocabularies are intentionally shared
across splits, so this dataset does not measure clinical generalization or linguistic
novelty. No LLM is fine-tuned on these fixtures.

## Schema and use

- `patient_id`: invented grouping key (not an actual patient identifier).
- `record_id`: invented encounter key.
- `split`: patient-level partition.
- `language`: `en` or `ko`.
- `note`: synthetic note after identifier redaction.
- `redaction_audit`: rule names and match counts, without matched values.
- `synthetic`: always `true`.

```python
from datasets import load_dataset
data = load_dataset('Hikaf143/synthetic-emr-safeguards')
print(data['test'][0]['note'])
```

## Evaluation and limitations

`evaluation.json` reports deterministic checks of exact evidence spans, missing-field
refusals, unsupported requests, fixture redaction, and partition disjointness.
These tests are constructed alongside the templates. They do not estimate performance
on independent records or evaluate any general-purpose LLM.
The redactor does not cover all PHI/PII categories or free-form names and is unsuitable
for processing real EMRs. The fixtures omit longitudinal reasoning, complex temporal
relations, abbreviations, and clinician disagreement.

## License and intended use

Apache-2.0 for these new synthetic fixtures and accompanying code. Research and
software testing only; not diagnosis, treatment, or deployment with real patient records.
Existing MKD model and dataset licenses are separate and are not changed by this project.
