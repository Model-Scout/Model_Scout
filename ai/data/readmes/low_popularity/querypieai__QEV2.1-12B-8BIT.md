---
library_name: transformers
license: other
license_name: querypie-ai-research-license-v1.0
base_model: google/gemma-4-12B-it
base_model_revision: 707f0a3b8a3c7ad586ed01e27eafbad8a27dd0f7
language: [en, ko, ja]
pipeline_tag: text-classification
tags: [qev, dlp, typed-decision, japanese, 8bit]
---

# QEV2.1-12B-8BIT

[English](README.md) · [한국어](README.ko.md) · [日本語](README.ja.md)

Inference-only release · merged LoRA · 8bit LLM.int8

## Overview

QEV2 multilingual typed-decision DLP model with Japanese-focused augmentation. It evaluates `is_dlp` and direct `is_*` type questions while retaining the QEV `choice`, `noul`, and `score` interface. It returns option probabilities, not generated text.

Base: `google/gemma-4-12B-it` · revision: `707f0a3b8a3c7ad586ed01e27eafbad8a27dd0f7` · format: `8bit LLM.int8`

## Training data

The project training corpus combines publicly available general-purpose data with internal corporate DLP data and multilingual augmentation. The released repository does not include raw training, calibration, validation, or test rows, labels, generated examples, optimizer state, or adapter files. Dataset names, internal paths, sample counts, and generation rules are intentionally not disclosed.

## Self-contained package

This inference-only release contains the complete merged backbone, tokenizer, FP32 pointer head, calibration metadata, and custom Transformers loader. It does not require a private or Dev repository, a separate adapter, or an external base-model download. Training scripts, adapter files, optimizer state, conversion tools, and datasets are not distributed. Publishing full weights does not technically prevent further fine-tuning; applicable license terms still govern use.

## Usage

```python
from transformers import AutoModel
model = AutoModel.from_pretrained("querypieai/QEV2.1-12B-8BIT", trust_remote_code=True, device="cuda:0")
print(model.decide("This is a public operational notice.", {"dlp": {"type": "noul", "instructions": "Does this contain sensitive data?", "criteria": {"false": "No", "true": "Yes"}}}))
```

Use the complete repository with `AutoModel` and `decide()`. Generic text-generation pipelines and hosted inference are not validated. LoRA is merged before bitsandbytes LLM.int8 conversion (threshold 6.0). Pointer head, embeddings, normalization and outlier paths remain floating point; CUDA is required.

## Evaluation (historical source reference)

These are recorded direct type-question results for the unmerged BF16 source checkpoint, not a new full benchmark of this merged/8bit package. `validation.json` records serialized reload and nine-question smoke checks.

| Metric | Result |
|---|---:|
| Overall Macro-F1 (biometric excluded) | 97.77% |
| EN Macro-F1 | 97.79% |
| KO Macro-F1 | 97.83% |
| JA Macro-F1 | 98.13% |
| Evaluation records | 6,281 |

`is_biometric` has zero positive rows and is excluded from macro summaries. See `EVALUATION.md`, `evaluation.json`, and `evaluation/` for details. Raw training/evaluation rows, optimizer state, and adapters are not distributed.

## Limits and intended use

The package is self-contained: backbone, tokenizer, pointer head, custom loader, serving example, evaluation metadata, and quantization/training guidance are included. `MANIFEST.sha256`, `provenance.json`, and `validation.json` record the contents. The interface performs document-level decisions and does not extract finding spans or counts. Validated hardware is NVIDIA H200/CUDA; custom code requires `trust_remote_code=True`.

## License and attribution

The QueryPie-trained modifications, merged LoRA update, pointer head, calibration metadata, and custom code use QueryPie AI Research License v1.0. Foundation weights and tokenizer assets retain their upstream licenses. See `LICENSE`, `LICENSES/Apache-2.0.txt`, `THIRD_PARTY_LICENSES.md`, and `NOTICE` for scope and attribution. Training data is not relicensed or distributed.

Personal non-commercial research and experimentation, and non-commercial academic research and evaluation are permitted. Commercial use requires prior written permission from QueryPie or a separate commercial license agreement. For commercial use, [contact QueryPie](https://www.querypie.com/en/contact-us). Business operations, product development and commercially motivated proofs of concept are not covered by the free research permission. Third-party foundation components retain their original licenses.
