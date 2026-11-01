---
pretty_name: Meddies PII v2
language:
- de
- en
- es
- fr
- id
- ja
- ko
- lo
- ms
- my
- pt
- ru
- ta
- th
- tl
- vi
- zh
license: cc-by-nc-4.0
annotations_creators:
- machine-generated
language_creators:
- machine-generated
multilinguality:
- multilingual
size_categories:
- 100K<n<1M
source_datasets:
- original
viewer: true
task_categories:
- token-classification
tags:
- medical
- healthcare
- pii
- phi
- de-identification
- ner
- multilingual
configs:
- config_name: burmese
  data_files:
  - split: train
    path: burmese/train-*
- config_name: chinese
  data_files:
  - split: train
    path: chinese/train-*
- config_name: english
  data_files:
  - split: train
    path: english/train-*
- config_name: eval
  data_files:
  - split: train
    path: eval/train-*
- config_name: eval-challenge
  data_files:
  - split: train
    path: eval-challenge/train-*
- config_name: eval-v2
  data_files:
  - split: train
    path: eval-v2/train-*
- config_name: filipino
  data_files:
  - split: train
    path: filipino/train-*
- config_name: french
  data_files:
  - split: train
    path: french/train-*
- config_name: german
  data_files:
  - split: train
    path: german/train-*
- config_name: indonesian
  data_files:
  - split: train
    path: indonesian/train-*
- config_name: japanese
  data_files:
  - split: train
    path: japanese/train-*
- config_name: korean
  data_files:
  - split: train
    path: korean/train-*
- config_name: laos
  data_files:
  - split: train
    path: laos/train-*
- config_name: malay
  data_files:
  - split: train
    path: malay/train-*
- config_name: portuguese
  data_files:
  - split: train
    path: portuguese/train-*
- config_name: russian
  data_files:
  - split: train
    path: russian/train-*
- config_name: spanish
  data_files:
  - split: train
    path: spanish/train-*
- config_name: tamil
  data_files:
  - split: train
    path: tamil/train-*
- config_name: thai
  data_files:
  - split: train
    path: thai/train-*
- config_name: vietnamese
  data_files:
  - split: train
    path: vietnamese/train-*
dataset_info:
  config_name: eval-v2
  features:
  - name: text
    dtype: string
  - name: label
    list:
    - name: category
      dtype: string
    - name: end
      dtype: int64
    - name: start
      dtype: int64
    - name: text
      dtype: string
  - name: info
    struct:
    - name: document_type
      dtype: string
    - name: generated_at
      dtype: string
    - name: generation_fallback
      dtype: bool
    - name: generation_model
      dtype: string
    - name: generation_provider
      dtype: string
    - name: id
      dtype: string
    - name: language
      dtype: string
    - name: language_bucket
      dtype: string
    - name: source
      dtype: string
    - name: split_purpose
      dtype: string
    - name: supplement
      dtype: bool
    - name: template_id
      dtype: string
  splits:
  - name: train
    num_bytes: 1967364
    num_examples: 850
  download_size: 673335
  dataset_size: 1967364
---

# Meddies PII v2 Dataset

<p align="left">
  <a href="https://huggingface.co/Meddies/meddies-pii-v2"><img alt="Meddies PII v2 model" src="https://img.shields.io/badge/Model-024C6F?style=flat&logo=huggingface&logoColor=white"></a>
  <a href="https://huggingface.co/Meddies/meddies-pii-v2-onnx"><img alt="ONNX model" src="https://img.shields.io/badge/ONNX-1ABBC7?style=flat&logo=huggingface&logoColor=white"></a>
  <a href="https://huggingface.co/spaces/Meddies/meddies-pii-extractor"><img alt="Try the browser demo" src="https://img.shields.io/badge/Demo-0F172A?style=flat&logo=googlechrome&logoColor=white"></a>
  <a href="https://creativecommons.org/licenses/by-nc/4.0/"><img alt="CC BY-NC 4.0" src="https://img.shields.io/badge/license-CC--BY--NC--4.0-475569"></a>
</p>

Character-level PII annotations for training and evaluating multilingual de-identification systems across 17 languages and nine entity families.

> [!IMPORTANT]
> This is a research artifact for privacy and healthcare AI teams. It is not medical advice, not a redaction tool, and not a substitute for local validation before any clinical deployment, compliance workflow, or high-stakes privacy claim. If you want to use this dataset in commercial work, please contact us at [contact@meddies.ai](mailto:contact@meddies.ai).

<p align="center">
  <img src="https://huggingface.co/Meddies/meddies-pii-v2-onnx/resolve/main/assets/dataset/hero-meddies-pii-v2-dataset.png" alt="Meddies PII v2 provides exact character spans for nine PII entity families across 17 languages" width="100%" />
</p>

## Why this dataset

PII datasets often stop at names, addresses, and contact details. Clinical text also carries hospital identifiers, signed portal links, credentials, local date formats, and language-specific boundary cases. Those gaps become brittle rules or silent misses in a de-identification pipeline.

Meddies PII v2 keeps the source annotation simple. Each identifier is stored as an exact character span that remains readable across tokenizers. Training code derives BIOES tags later without changing the original text or boundaries.

## What is inside

The repository has 17 language-specific training configs and three evaluation configs. Every config uses the physical split name `train`. The config name tells you whether the rows belong to training or evaluation.

| Config group | Purpose | Rows |
| --- | --- | ---: |
| 17 language configs | Training and domain adaptation | 317,846 |
| `eval` | Pinned checkpoint selection | 1,700 |
| `eval-challenge` | Harder boundary and formatting cases | 3,400 |
| `eval-v2` | Fresh-form development evidence | 850 |

`eval-v2` contains 50 synthetic documents per language across referral letters, discharge summaries, invoices, lab reports, HL7 messages, and chat transcripts. It is published development evidence, so use a separate blinded corpus for headline claims.

The nine labels are `address`, `company_name`, `date`, `email_address`, `human_name`, `id_number`, `phone_number`, `private_url`, and `secret`.

A `private_url` is an access-bearing link such as a signed patient portal URL. A `secret` is a credential, token, password, or key.

## Training distribution

<p align="center">
  <img src="https://huggingface.co/Meddies/meddies-pii-v2-onnx/resolve/main/assets/dataset/training-distributions-meddies-pii-v2.png" alt="Training-only distributions for language rows, document types, and entity spans in Meddies PII v2" width="100%" />
</p>

*This figure uses only the 317,846 rows in the 17 language-specific training configs. It excludes `eval`, `eval-challenge`, and `eval-v2`.*

Three things matter when reading it.

- Vietnamese and English are the largest language configs. The other 15 stay within a narrower range of roughly 15,000 to 20,500 rows.
- The training set spans 45 document-type values. Pharmacy refill requests, discharge summaries, lab notifications, triage notes, and portal logs are the largest groups.
- Secrets and ID numbers are intentionally common. The entity mix is shaped for model learning and does not estimate clinical prevalence.

## Row format

Each row contains the source text, its character spans, and generation metadata.

```json
{
  "text": "Patient Nguyễn Văn A called 0912 345 678",
  "label": [
    {
      "category": "human_name",
      "start": 8,
      "end": 20,
      "text": "Nguyễn Văn A"
    }
  ],
  "info": {
    "language": "Vietnamese",
    "document_type": "telehealth triage note",
    "split_purpose": "train"
  }
}
```

The recorded span must reproduce the source text exactly with `text[start:end]`.

## Where it fits

Character spans remain the source of truth between data generation and model-specific tokenization. Rows pass schema, boundary, and label checks before publication. Training code then derives tokenizer-specific BIOES tags.

<p align="center">
  <img src="https://huggingface.co/Meddies/meddies-pii-v2-onnx/resolve/main/assets/dataset/pipeline-meddies-pii-v2-dataset.png" alt="Meddies PII v2 dataset pipeline from generation through span validation to training and evaluation configs" width="100%" />
</p>

The release contains Meddies-generated data. External public corpora used by the model are rebuilt from their original sources and are not rehosted here.

## Quick start

Load one config explicitly.

```python
from datasets import load_dataset

training = load_dataset(
    "Meddies/meddies-pii-v2",
    "vietnamese",
    split="train",
    token=True,
)

row = training[0]
print(row["text"])
print(row["label"])
```

Load evaluation data by config name and keep it separate from training.

```python
control = load_dataset(
    "Meddies/meddies-pii-v2",
    "eval",
    split="train",
    token=True,
)
```

## Good fits

- Training span-based PII detectors for multilingual clinical and general text.
- Deriving tokenizer-specific BIOES labels while keeping character spans auditable.
- Testing annotation tools, constrained decoders, and redaction interfaces.
- Studying hard labels and boundary cases before collecting local evaluation data.

## Limits

- Machine-generated text does not behave exactly like real clinical records.
- Language coverage does not equal hospital coverage. Local names, identifiers, templates, and optical character recognition errors will differ.
- The training distribution is deliberately shaped for learning and is not a prevalence estimate.
- The nine-label taxonomy is closed. Downstream teams must decide how to handle unsupported identifiers.
- A held-out, human-reviewed evaluation from the intended deployment environment is still required.
- [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) does not permit commercial use without separate permission.

## Feedback

Found an invalid offset, ambiguous label, duplicated pattern, or language-specific boundary problem? Include the config name and row ID when possible. Never post real patient data or credentials.

Open a thread in the Community tab or email [contact@meddies.ai](mailto:contact@meddies.ai).

## Collaboration

We are looking for hospitals, research groups, and privacy teams that can contribute safe failure patterns, independent audits, or language review. Email [contact@meddies.ai](mailto:contact@meddies.ai) to work with us.

## Citation

```bibtex
@misc{meddies-pii-v2-dataset,
  title={Meddies PII v2 multilingual character-span annotations for PII detection},
  author={MeddiesAI},
  year={2026},
  url={https://huggingface.co/datasets/Meddies/meddies-pii-v2}
}
```
