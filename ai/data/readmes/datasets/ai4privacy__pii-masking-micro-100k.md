---
license: other
license_name: cc-by-4.0
language:
  - en
  - fr
  - de
  - es
  - it
  - nl
  - pt
  - bg
  - cs
  - da
  - el
  - et
  - fi
  - hr
  - hu
  - lt
  - lv
  - pl
  - ro
  - sk
  - sl
  - sr
  - sv
  - id
  - ja
  - ko
  - ms
  - tl
  - vi
  - zh
task_categories:
  - token-classification
  - text-generation
tags:
  - privacy
  - pii
  - ner
  - synthetic
  - multilingual
  - ai4privacy
  - openpii
  - asia-pacific
pretty_name: "PII Masking Micro: Multilingual Sample"
size_categories:
  - 10K<n<100K
configs:
  - config_name: default
    data_files:
      - split: train
        path: data/train.jsonl
      - split: validation
        path: data/validation.jsonl
---

# PII Masking Micro: Multilingual Sample

<p align="center">
  <img src="assets/pii_masking_3m_coverage.png" alt="PII-Masking-3M Coverage" width="500"/>
</p>

A **micro-sized** stratified sample of [pii-masking-openpii-1.5m](https://huggingface.co/datasets/ai4privacy/pii-masking-openpii-1.5m),
the flagship release of the **PII-Masking-3M** family. Sampled proportionally by
`(source_dataset, language)` so every locale and label gets representation.
Asia Pacific rows appear first.

📖 **More information:** [www.ai4privacy.com/datasets/pii-masking-3m-asia-pacific](https://www.ai4privacy.com/datasets/pii-masking-3m-asia-pacific/)

## Dataset Details

| Total Examples | Train | Validation | Labels | Languages | Regions | Annotations | Format | License |
|---:|---:|---:|---:|---:|---:|---:|:---:|:---:|
| **99,990** | 90,000 | 9,990 | 19 | 30 | 37 | 725,798 | JSONL | CC-BY-4.0 |

## Language Coverage

<p align="center">
  <img src="assets/language_distribution.png" alt="Language Distribution" width="800"/>
</p>

## Label Taxonomy (19 Labels)

<p align="center">
  <img src="assets/label_distribution.png" alt="Label Distribution" width="800"/>
</p>

| Label | Count | Label | Count | Label | Count |
| :---|---: | :---|---: | :---|---: |
| `GIVENNAME` | 85,682 | `AGE` | 36,229 | `GENDER` | 19,710 |
| `DATE` | 84,582 | `STREET` | 34,171 | `TAXNUM` | 19,362 |
| `SURNAME` | 72,604 | `BUILDINGNUM` | 33,649 | `SEX` | 18,572 |
| `EMAIL` | 54,095 | `ZIPCODE` | 30,528 | `SOCIALNUM` | 17,092 |
| `CITY` | 49,804 | `IDCARDNUM` | 23,956 | `PASSPORTNUM` | 14,757 |
| `TITLE` | 47,043 | `CREDITCARDNUMBER` | 23,295 |  |  |
| `TELEPHONENUM` | 40,698 | `DRIVERLICENSENUM` | 19,969 |  |  |

## Usage

```python
from datasets import load_dataset
ds = load_dataset("ai4privacy/pii-masking-micro-100k")
```

## PII-Masking-3M Tiers

| Tier | Size | Link |
|:---|:---|:---|
| Nano | 1k | [pii-masking-nano-1k](https://huggingface.co/datasets/ai4privacy/pii-masking-nano-1k) |
| Mini | 10k | [pii-masking-mini-10k](https://huggingface.co/datasets/ai4privacy/pii-masking-mini-10k) |
| Micro | 100k | [pii-masking-micro-100k](https://huggingface.co/datasets/ai4privacy/pii-masking-micro-100k) |
| Full | 1.5M | [pii-masking-openpii-1.5m](https://huggingface.co/datasets/ai4privacy/pii-masking-openpii-1.5m) |

## License

CC-BY-4.0. Copyright © 2026 Ai Suisse SA. Contains **synthetic PII only**, no real personal data.

## Legal Disclaimer

Provided "as is" without warranties of any kind. Users are responsible for compliance with all
applicable data privacy laws (GDPR, CCPA, PDPA, APPI, PIPA, UU PDP) and AI regulations.
