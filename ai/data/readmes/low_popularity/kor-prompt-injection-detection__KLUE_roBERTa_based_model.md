---
license: apache-2.0
language:
  - ko
library_name: transformers
pipeline_tag: text-classification
base_model: klue/roberta-base
tags:
  - korean
  - prompt-injection-detection
  - text-classification
  - ai-safety
---

# KLUE RoBERTa Based Prompt Injection Detection Model

This repository contains a fine-tuned KLUE RoBERTa based text classification model for Korean prompt injection detection.

## Intended Use

This model was developed for a university text mining project. It is intended for academic evaluation and research on Korean prompt injection detection.

The model classifies Korean text into two categories:

- `normal`
- `attack`

## Evaluation

| Metric | Value |
| --- | ---: |
| Accuracy | 0.9870 |
| Attack Precision | 0.9752 |
| Attack Recall | 0.9882 |
| Attack F1 | 0.9816 |
| Macro F1 | 0.9858 |
| Weighted F1 | 0.9870 |

Detailed evaluation files:

- `classification_report.txt`
- `summary.csv`

## Project Repository

https://github.com/3recon/prompt-injection-detection

## Limitations

This model is a research artifact for prompt injection detection. It should not be used as a standalone production security system without additional validation.