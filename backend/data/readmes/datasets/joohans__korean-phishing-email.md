---
license: apache-2.0
language:
  - ko
  - en
task_categories:
  - text-classification
tags:
  - phishing
  - email
  - security
  - korean
  - sample
size_categories:
  - n<1K
---

# Korean Phishing Email Detection Dataset (Sample Preview)

> **Note**: This is a **sample preview** (114 samples) of the full dataset (20,000+ samples) to be released in July 2026 as part of the NIPA Open Source AI/SW Development Support Program.

## Dataset Description

| Split | File | Samples | Description |
|-------|------|---------|-------------|
| train | `email_train.jsonl` | 67 | English spam/legitimate emails (Enron-based) |
| test | `email_test.jsonl` | 17 | English spam/legitimate test set |
| korean | `korean_phishing_samples.jsonl` | 30 | Korean phishing email samples |

- **Languages**: Korean, English
- **Labels**: `phishing`/`spam` (1) vs `legitimate`/`not spam` (0)
- **Sources**: Public corpora (Enron, Nazario, PhishTank) + Korean augmentation

## PoC Results (using this data)

| Metric | Before Fine-tuning | After LoRA Fine-tuning |
|--------|-------------------|----------------------|
| Accuracy | 57.7% (Zero-shot) | **100%** |
| False Positive Rate | 98.2% | **0%** |
| Test samples | 230 | 230 |

## Full Dataset Roadmap (July 2026)

- 20,000+ samples: public corpora + LLM-augmented Korean phishing emails
- PII auto-removal + expert cross-validation
- Comprehensive Dataset Card with detailed statistics

## Usage

```python
from datasets import load_dataset
ds = load_dataset("joohans/korean-phishing-email")
```

## Citation

NIPA 2026 Open Source AI/SW Development Support Program
Developed by (주)씨피랩스 | [Live Demo](https://huggingface.co/spaces/joohans/caion-phishing-demo) | [Fine-tuned Model](https://huggingface.co/joohans/mistral-7b-phishing-ko)
