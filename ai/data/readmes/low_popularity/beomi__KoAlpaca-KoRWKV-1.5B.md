---
language:
- ko
license: apache-2.0
tags:
- KoRWKV
- KoAlpaca
datasets:
- KoAlpaca-v1.0
pipeline_tag: text-generation
base_model: KoRWKV-1.5B
model-index:
- name: KoAlpaca-KoRWKV-1.5B
  results: []
---

> 🚧 Note: this repo is only for demo purpose, current uploaded version is finetuned version of KoRWKV which is ~20% trained ckpt (with ~31Billion tokens) 🚧

# beomi/KoAlpaca-KoRWKV-1.5B (v1.0)

This model is a fine-tuned version of [KoRWKV-1.5B](https://huggingface.co/beomi/KoRWKV-1.5B) on a KoAlpaca Dataset v1.0

Dataset available at [KoAlpaca Github Repository](https://github.com/Beomi/KoAlpaca)

## Training procedure

### Train Device

- A100 80G x2
- ~2hrs

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- seed: 42
- optimizer: Adafactor
- lr_scheduler_type: linear
- num_epochs: 2.0
- mixed_precision_training: Native AMP fp16

### Framework versions

- Transformers 4.30.0.dev0
- Pytorch 2.0.0+cu117
- Datasets 2.10.1
- Tokenizers 0.13.2
