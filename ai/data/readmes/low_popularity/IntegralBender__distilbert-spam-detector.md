---
library_name: transformers
license: apache-2.0
language:
  - en
  - tr
  - ar
  - bn
  - zh
  - nl
  - fr
  - de
  - hi
  - id
  - it
  - ja
  - jv
  - ko
  - mr
  - no
  - pa
  - pt
  - ru
  - es
  - sv
  - uk
  - ur
pipeline_tag: text-classification
tags:
  - spam-detection
  - text-classification
  - distilbert
  - multilingual
  - security
  - generated_from_trainer
datasets:
  - M-Arjun/SpamShield-Datasets
  - SetFit/enron_spam
  - ucirvine/sms_spam
  - Deysi/spam-detection-dataset
  - zefang-liu/phishing-email-dataset
base_model: distilbert/distilbert-base-multilingual-cased
metrics:
  - accuracy
  - f1
  - precision
  - recall
  - loss
widget:
  - text: "Değerli müşterimiz, banka hesabınızda şüpheli işlem tespit edilmiştir. Güvenliğiniz için hemen giriş yapın: https://bank-security-verify.com"
    example_title: "Turkish Phishing Spam"
  - text: "URGENT: Your Netflix subscription has been suspended due to billing failure. Update your payment details here: http://netflix-secure-update.com"
    example_title: "English Phishing Spam"
  - text: "Hi team, please find attached the updated architecture review report for our upcoming deployment on Friday."
    example_title: "English Professional Ham"
  - text: "ACİL! 50.000 TL'ye kadar faizsiz anında nakit kredi fırsatı için tıklayın: http://kredi-kampanya-2026.net"
    example_title: "Turkish Promotional Spam"
  - text: "WICHTIG: Ihr Paket konnte nicht zugestellt werden. Bitte zahlen Sie die Zollgebühr von 2,99€ unter folgendem Link: http://paket-lieferung-zoll.com"
    example_title: "German Phishing Spam"
  - text: "Bonjour à tous, veuillez trouver ci-joint le compte-rendu de notre réunion de ce matin concernant le nouveau projet de développement."
    example_title: "French Professional Ham"    
model-index:
  - name: distilbert-spam-detector
    results:
      - task:
          type: text-classification
          name: Multilingual Spam & Phishing Detection
        dataset:
          name: SpamShield, Enron, SMS Spam and Phishing Aggregation
          type: custom
        metrics:
          - type: accuracy
            value: 0.9916
            name: Accuracy
          - type: f1
            value: 0.9915
            name: F1 Score
          - type: precision
            value: 0.9932
            name: Precision
          - type: recall
            value: 0.9897
            name: Recall
          - type: loss
            value: 0.0434
            name: Validation Loss
---

# DistilBERT Multilingual Spam & Phishing Detector

**DistilBERT Multilingual Spam & Phishing Detector** is a high-performance, fine-tuned model engineered for real-time detection of spam, phishing emails and unsolicited malicious messages across multiple languages.

Built via an automated MLOps pipeline, this model merges general spam sources with phishing benchmarks to achieve robust generalization and low inference overhead.

An **INT8 Quantized ONNX** variant optimized for low-latency CPU and edge deployments is available at [`IntegralBender/distilbert-spam-detector-onnx`](https://huggingface.co/IntegralBender/distilbert-spam-detector-onnx).

# Table of Contents

1. [Model Overview](#model-overview)
2. [Intended Uses & Limitations](#intended-uses--limitations)
3. [Usage & Integration](#usage--integration)
4. [Dataset & Preprocessing Pipeline](#dataset--preprocessing-pipeline)
5. [Training & Evaluation](#training--evaluation)
6. [Framework Versions & Environment](#framework-versions--environment)

# Model Overview

- **Architecture:** `DistilBERTForSequenceClassification`
- **Base Model:** [`distilbert/distilbert-base-multilingual-cased`](https://huggingface.co/distilbert/distilbert-base-multilingual-cased)
- **Primary Task:** Binary Text Classification (`HAM: 0`, `SPAM: 1`)
- **Max Sequence Length:** 512 tokens
- **License:** Apache 2.0
- **Supported Languages:** Multilingual (Supports 20+ primary training languages and inherits base cased vocabulary)

# Intended Uses & Limitations

## Primary Use Cases
* **Inbox Security:** Real-time filtering and pre-screening of incoming email payloads.
* **Content Moderation:** Automated detection of spam in comments, chat applications and online form submissions.
* **Phishing Defense:** Flagging unauthorized link-injection attacks and social engineering text patterns.

## Out-of-Scope & Limitations
* **Decision Authority:** Should be utilized as an automated flagging system rather than a sole arbiter for permanent email deletion.
* **Slang & Obfuscation:** While highly effective against standard spam vectors, heavy leetspeak or unusual character obfuscations may occasionally lead to false negatives.

# Usage & Integration

Because the model was trained with native `id2label` mappings, prediction outputs are returned directly as `HAM` or `SPAM`.

## Standard Inference (PyTorch)

```python
from transformers import pipeline

# Load pipeline directly from Hugging Face Hub
classifier = pipeline(
    "text-classification", 
    model="IntegralBender/distilbert-spam-detector"
)

# Test with multilingual inputs
samples = [
    "Verify your bank account immediately by clicking this secure link: http://bit.ly/fake-link",
    "Lütfen yarınki toplantı notlarını sisteme yüklemeyi unutmayın.",
    "WICHTIG: Ihr Konto wurde vorübergehend gesperrt. Bitte aktualisieren Sie Ihre Daten hier: http://bank-sicherheit-de.com",
    "Bonjour, la réunion de demain est décalée à 14h. Merci de confirmer votre présence."
]

results = classifier(samples)

for text, res in zip(samples, results):
    print(f"[{res['label']}] (Confidence: {res['score']:.4f}) -> {text}")
```

# Dataset & Preprocessing Pipeline

The training corpus was dynamically aggregated, standardized, concatenated and globally shuffled from five open-source datasets to ensure robust class distribution:

- [`M-Arjun/SpamShield-Datasets`](https://huggingface.co/datasets/M-Arjun/SpamShield-Datasets)
- [`SetFit/enron_spam`](https://huggingface.co/datasets/SetFit/enron_spam)
- [`ucirvine/sms_spam`](https://huggingface.co/datasets/ucirvine/sms_spam)
- [`Deysi/spam-detection-dataset`](https://huggingface.co/datasets/Deysi/spam-detection-dataset)
- [`zefang-liu/phishing-email-dataset`](https://huggingface.co/datasets/zefang-liu/phishing-email-dataset)

## Preprocessing & Data Cleaning

- **Validation:** Rows containing `None` values or empty string payloads are strictly filtered out during streaming.
- **Label Normalization & Feature Alignment:** Labels are dynamically matched against a defined set of indicators and cast to binary `int64` (`0` for HAM, `1` for SPAM). Features across all five datasets are strictly mapped to uniform `text` and `label` columns to prevent schema conflicts.
- **Strict Deduplication & Leakage Prevention:** After concatenation, the unified corpus undergoes a fast, index-based deduplication process on the text payloads. This critical step removes overlapping entries across the different dataset sources, effectively preventing data leakage between the train and test sets and mitigating overfitting.
- **Data Partitioning & Reproducibility:** The deduplicated dataset is globally shuffled and split into train/test partitions. A fixed initialization seed (`seed=42`) is rigorously enforced across the pipeline to guarantee exact reproducibility of the dataset state and evaluation metrics for anyone retraining from source.

# Training & Evaluation

## Training Configuration & Hardware

- **Hardware Requirements:** The pipeline includes a strict hardware check, requiring a dedicated CUDA-enabled GPU for acceleration.
- **Optimization:** Trained using native automatic mixed precision (FP16) on CUDA, orchestrated through Hydra configuration files.

## Training Hyperparameters

The model was fine-tuned using the following configuration:

- **Learning Rate:** `2e-05`
- **Train Batch Size:** `32`
- **Eval Batch Size:** `64`
- **Seed:** `42`
- **Optimizer:** AdamW Fused (`adamw_torch_fused`) with `betas=(0.9, 0.999)` and `epsilon=1e-08`
- **Learning Rate Scheduler:** Linear
- **Number of Epochs:** `3`
- **Mixed Precision:** Native AMP (FP16)

## Training Progression & Results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy | F1     | Precision | Recall |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:------:|:---------:|:------:|
| 0.0245        | 1.0   | 5673  | 0.0553          | 0.9843   | 0.9839 | 0.9932    | 0.9748 |
| 0.0169        | 2.0   | 11346 | 0.0374          | 0.9901   | 0.99   | 0.9905    | 0.9894 |
| 0.0077        | 3.0   | 17019 | 0.0434          | 0.9916   | 0.9915 | 0.9932    | 0.9897 |

# Framework Versions & Environment

The model pipeline was built and validated within the following software environment:

- **Transformers:** `4.57.6`
- **PyTorch:** `2.11.0+cu130`
- **Datasets:** `4.8.5`
- **Tokenizers:** `0.22.2`
