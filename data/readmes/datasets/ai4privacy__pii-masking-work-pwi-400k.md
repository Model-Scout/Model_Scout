---
license: other
license_name: ai4privacy-commercial
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
  - feature-extraction
tags:
  - pii
  - privacy
  - ner
  - synthetic-data
  - gdpr
  - pdpa
  - appi
  - pipa
  - european
  - asia-pacific
  - ai4privacy
pretty_name: "PII Masking, Work & HR Information (PWI) with Asia Pacific"
size_categories:
  - 100K<n<1M
source_datasets:
  - extended
configs:
  - config_name: default
    data_files:
      - split: train
        path: data/train.jsonl
      - split: validation
        path: data/validation.jsonl
extra_gated_prompt: >-
  This dataset is part of the PII-Masking-3M enterprise family.
  Access is granted to bona fide researchers and partners. Please indicate your
  affiliation and intended use.
extra_gated_fields:
  Company: text
  Use case: text
  I agree to the Ai4Privacy licensing terms: checkbox
---

> 👉 **Looking for the open multilingual baseline?** Start with
> [ai4privacy/pii-masking-openpii-1.5m](https://huggingface.co/datasets/ai4privacy/pii-masking-openpii-1.5m)
> (1.5M samples, 30 languages, open-PII taxonomy).

# 🇪🇺🌏 Personal Work & HR Information, Global PII Dataset

<p align="center">
  <img src="assets/pii_masking_3m_coverage.png" alt="PII-Masking-3M Coverage" width="500"/>
</p>

Part of **PII-Masking-3M** by [Ai4Privacy](https://ai4privacy.com), the global
(2M base + Asia Pacific) PII-masking corpus.

📖 **More information:** [www.ai4privacy.com/datasets/pii-masking-3m-asia-pacific](https://www.ai4privacy.com/datasets/pii-masking-3m-asia-pacific/)

| Entries | PII Annotations | Labels | Languages | Regions |
|---------|----------------|--------|-----------|---------|
| **418,580** | **2,305,517** | **26** | **30** | **37** |

---

## PII Label Distribution

![Bar chart showing PII label distribution across entity types](assets/label_distribution.png)

Full label inventory:

| Label | Count | Label | Count | Label | Count |
| :---|---: | :---|---: | :---|---: |
| `DATE` | 303,005 | `JOBTYPE` | 124,620 | `BUILDINGNUM` | 1,055 |
| `TIME` | 240,892 | `SEX` | 115,759 | `STREET` | 807 |
| `JOBTITLE` | 218,251 | `SURNAME` | 114,718 | `SOCIALNUM` | 753 |
| `ORGANISATION` | 213,840 | `TAXNUM` | 92,359 | `IDCARDNUM` | 652 |
| `SALARY` | 181,878 | `TELEPHONENUM` | 86,283 | `PASSPORTNUM` | 350 |
| `JOBAREA` | 164,043 | `EMAIL` | 15,542 | `CREDITCARDNUMBER` | 86 |
| `DOCNUM` | 144,824 | `AGE` | 5,664 | `ZIPCODE` | 64 |
| `GIVENNAME` | 143,389 | `CITY` | 2,932 | `DRIVERLICENSENUM` | 55 |
| `GENDER` | 130,768 | `TITLE` | 2,928 |  |  |

---

## Coverage

**New Asia Pacific locales** (added in 3M): Vietnamese (vi-VN), Indonesian (id-ID),
Malay (ms-MY), Filipino (tl-PH), Chinese (zh-CN), Japanese (ja-JP), Korean (ko-KR),
plus English variants in Singapore (en-SG) and India (en-IN).

---

## Language Distribution

![Bar chart showing entry distribution across 30 languages](assets/language_distribution.png)

---

## Data Format

```json
{
  "source_text": "Original text with synthetic PII values",
  "masked_text": "Text with [LABEL_N] placeholders",
  "privacy_mask": [{"label": "GIVENNAME", "start": 0, "end": 5, "value": "Alice"}],
  "uid": 12345,
  "language": "de", "region": "DE", "script": "Latn",
  "mbert_tokens": ["Alice", "hat"],
  "mbert_token_classes": ["B-GIVENNAME", "O"]
}
```

---

## PII-Masking-3M Collection

| Dataset | Size | Link |
|---------|------|------|
| Health (PHI) | 400k | [link](https://huggingface.co/datasets/ai4privacy/pii-masking-health-phi-400k) |
| Financial (PFI) | 400k | [link](https://huggingface.co/datasets/ai4privacy/pii-masking-financial-pfi-400k) |
| Location (PLI) | 400k | [link](https://huggingface.co/datasets/ai4privacy/pii-masking-location-pli-400k) |
| Work (PWI) | 400k | [link](https://huggingface.co/datasets/ai4privacy/pii-masking-work-pwi-400k) |
| Digital (PDI) | 350k | [link](https://huggingface.co/datasets/ai4privacy/pii-masking-digital-pdi-350k) |
| Open PII | 1.5M | [link](https://huggingface.co/datasets/ai4privacy/pii-masking-openpii-1.5m) |

---

## Usage

```python
from datasets import load_dataset
dataset = load_dataset("ai4privacy/pii-masking-work-pwi-400k")
```

## Commercial Licensing

This is an enterprise dataset under the **PII-Masking-3M** programme. Contact
[Ai4Privacy](https://ai4privacy.com) for licensing terms covering production use.

---

## Access & Partnerships

- 🔓 **Request data access**: [Open Data Access Form](https://forms.gle/iU5BvMPGkvvxnHBa7)
- 🤝 **Commercial partnerships**: [Enterprise Contact Form](https://forms.gle/oDDYqQkyoTB93otHA)

---

## p5y Data Analytics

This dataset is built on the [p5y](https://p5y.org) framework, think of it as i18n but for privacy.
Just as i18n (internationalization) translates content into different locales, p5y translates
sensitive data into privacy-safe formats through a standardized 3-step approach:

1. **Awareness**, Scan and markup private entities in unstructured text, producing a structured privacy mask with entity types, distribution, density, and risk assessment.
2. **Protection**, Control identified personal data through masking, pseudonymization, or k-anonymization, tailored to the specific use case and regulatory requirements.
3. **Quality Assurance**, Measure remaining privacy risk after anonymization, evaluating de-anonymization risks through expert annotation and automated assessment.

Learn more at [p5y.org](https://p5y.org)

---

## Legal Disclaimer

The dataset is provided **"as is"** without any guarantees or warranties, express or implied.
Ai4Privacy and Ai Suisse SA make no representations regarding accuracy, completeness, or
suitability for any specific purpose. Users utilize the dataset **at their own risk** and bear
full responsibility for any outcomes. Under no circumstances shall Ai4Privacy, Ai Suisse SA,
or affiliates be held liable for any damages arising from use of the dataset. Users are
responsible for ensuring compliance with all applicable laws, regulations, and ethical guidelines,
including GDPR, CCPA, Singapore PDPA, Japan APPI, Korea PIPA, Indonesia UU PDP, and AI-related
legislation.

---

[ai4privacy.com](https://ai4privacy.com) · [Discord](https://discord.gg/FmzWshaaQT) · [Ai Suisse SA](https://www.aisuisse.com/)
