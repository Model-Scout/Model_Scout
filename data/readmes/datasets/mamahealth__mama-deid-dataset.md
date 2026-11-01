---
license: cc-by-4.0
task_categories:
- token-classification
tags:
- de-identification
- pii
- medical
- synthetic
language:
- en
- de
- it
- fr
- es
- nl
- pt
- pl
- tr
- el
- ru
- uk
- ar
- he
- fa
- hi
- id
- vi
- th
- zh
- ja
- ko
configs:
- config_name: default
  data_files:
  - split: train
    path: train.jsonl
  - split: validation
    path: validation.jsonl
---

# Medical de-identification, multilingual

Synthetic patient messages, short answers to app questions, documents (letters, reports,
prescriptions, OCR output), longer posts and conversations in 22 languages, labelled for
de-identification that keeps clinical context: identifiers are masked, while conditions, treatments,
tests, clinical dates, ages, care places and care institutions are kept. No real patient data.

Built by [mama health](https://mamahealth.io); main contributor Lorenzo Famiglini. The model trained on it
is described in its model card.

## How it was made

- Every record follows one labelling policy, LABELLING.md, with its decided edge cases.
- Rows were written from per-row briefs (language, shape, writer, age, register, care setting, the
  kinds of identifier, a condition), so the data covers rare settings, identifier types and conditions
  on purpose rather than by chance.
- Training data was written by Claude Sonnet and Claude Fable and, in the last round, by two GPT
  models through Codex; validation and test by Claude Opus and, in the last round, by a third GPT model
  that wrote no training data, each from its own prompts. Every batch was reviewed by a model other
  than its writer, evaluation data by Claude Opus, and the remaining identifier error rate was measured
  on a sample (sources/batches.json in the code repository records writer, prompt, reviewers and rate
  for each batch). Test files named `*-probe-x10-*` hold minimal pairs, two rows that differ in a few
  words so that one label flips.
- Identifier values follow their real formats; checks reject placeholder numbers and text, template or
  distinctive identifiers shared between splits.
- The training split includes 852 records of NVIDIA Nemotron-PII (CC BY 4.0), relabelled to this policy.

Each record: `id` (source file and position), `text`, `spans` (character offsets `start`, `end` and
a `label`) and `shape`. `context` records are messages preceded by the message before them, so a
model learns to use it.

The test split is kept private, so that it stays a clean test for future versions.

## Limitations

The text is machine-written: real messages are messier and harder. Labels were checked by models,
not by human annotators; the measured residual rate is about 0 to 0.1 identifier errors per record.

| split | records | message | context | answer | document | text | conversation | no identifier |
|---|---|---|---|---|---|---|---|---|
| train | 31557 | 17888 | 1999 | 2757 | 5215 | 3633 | 65 | 9223 |
| validation | 1714 | 938 | 0 | 210 | 299 | 222 | 45 | 793 |

## Labels in train

| label | spans |
|---|---|
| PERSON | 16474 |
| CLINICIAN | 9459 |
| ADDRESS | 3049 |
| CONTACT | 5553 |
| ID | 9159 |
| DOB | 2327 |
| RESIDENCE_LOCALITY | 3324 |
| ORG | 2675 |
| URL | 688 |
| NRP | 1840 |
| AGE | 7896 |
| CLINICAL_INTERVENTION | 65076 |
| CLINICAL_STATE | 75749 |
| CARE_INSTITUTION | 19257 |
| CARE_LOCALITY | 3592 |
| CLINICAL_DATE | 14139 |
| CLINICAL_DURATION | 6099 |
| RESIDENCE_COUNTRY | 669 |

Masked: PERSON, CLINICIAN, ADDRESS, CONTACT, ID, DOB, RESIDENCE_LOCALITY, ORG, URL, NRP. Kept: every other label.

## Licence

CC BY 4.0. The Nemotron-PII records are from NVIDIA's Nemotron-PII dataset, CC BY 4.0.
