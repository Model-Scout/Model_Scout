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
pretty_name: "OpenPII Nano: Multilingual PII Masking Sample"
size_categories:
  - 1K<n<10K
configs:
  - config_name: default
    data_files:
      - split: train
        path: data/train.jsonl
      - split: validation
        path: data/validation.jsonl
---

# OpenPII Nano: Multilingual PII Masking Sample

<p align="center">
  <img src="assets/pii_masking_3m_coverage.png" alt="PII-Masking-3M Coverage" width="500"/>
</p>

A **nano-sized** stratified sample of [OpenPII 1.5M](https://huggingface.co/datasets/ai4privacy/pii-masking-openpii-1.5m),
perfect for quick prototyping, smoke tests, and CI fixtures. Every locale and every
label that exists in the parent dataset is represented in proportion.

📖 **More information:** [www.ai4privacy.com/datasets/pii-masking-3m-asia-pacific](https://www.ai4privacy.com/datasets/pii-masking-3m-asia-pacific/)

## Dataset Details

| Total Examples | Train | Validation | Labels | Languages | Regions | Annotations | Format | License |
|---:|---:|---:|---:|---:|---:|---:|:---:|:---:|
| **1,000** | 900 | 100 | 19 | 30 | 37 | 7,089 | JSONL | CC-BY-4.0 |

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
| `GIVENNAME` | 855 | `AGE` | 354 | `GENDER` | 192 |
| `DATE` | 838 | `STREET` | 325 | `SOCIALNUM` | 175 |
| `SURNAME` | 721 | `BUILDINGNUM` | 319 | `SEX` | 175 |
| `EMAIL` | 534 | `ZIPCODE` | 290 | `TAXNUM` | 173 |
| `TITLE` | 480 | `IDCARDNUM` | 228 | `PASSPORTNUM` | 143 |
| `CITY` | 468 | `CREDITCARDNUMBER` | 216 |  |  |
| `TELEPHONENUM` | 407 | `DRIVERLICENSENUM` | 196 |  |  |

## Usage

```python
from datasets import load_dataset
ds = load_dataset("ai4privacy/openpii-masking-nano-1k")
```

## Related Datasets (PII-Masking-3M Family)

| Tier | Size | Link |
|:---|:---|:---|
| Nano | 1k | [openpii-masking-nano-1k](https://huggingface.co/datasets/ai4privacy/openpii-masking-nano-1k) |
| Micro | 100k | [openpii-masking-micro-100k](https://huggingface.co/datasets/ai4privacy/openpii-masking-micro-100k) |
| Full | 1.5M | [pii-masking-openpii-1.5m](https://huggingface.co/datasets/ai4privacy/pii-masking-openpii-1.5m) |

## License

CC-BY-4.0. Copyright © 2026 Ai Suisse SA. Contains **synthetic PII only**, no real personal data.

## Legal Disclaimer

Provided "as is" without warranties of any kind. Users are responsible for compliance with all
applicable data privacy laws (GDPR, CCPA, PDPA, APPI, PIPA, UU PDP) and AI regulations.
