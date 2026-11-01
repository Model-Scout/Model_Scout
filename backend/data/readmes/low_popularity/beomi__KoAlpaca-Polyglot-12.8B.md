---
language:
- ko
license: apache-2.0
tags:
- generated_from_trainer
- polyglot-ko
- gpt-neox
- KoAlpaca
datasets:
- KoAlpaca-v1.1b
pipeline_tag: text-generation
base_model: EleutherAI/polyglot-ko-12.8b
model-index:
- name: KoAlpaca-Polyglot-12.8B
  results: []
---

Update @ 2023.06.01

- Add Safetensor sharded model weight (max shard = 1GB)


# KoAlpaca-Polyglot-12.8B (v1.1b)

This model is a fine-tuned version of [EleutherAI/polyglot-ko-12.8b](https://huggingface.co/EleutherAI/polyglot-ko-12.8b) on a KoAlpaca Dataset v1.1b

Detail Codes are available at [KoAlpaca Github Repository](https://github.com/Beomi/KoAlpaca)


## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 1
- seed: 42
- distributed_type: multi-GPU (A100 80G)
- num_devices: 4
- gradient_accumulation_steps: 64
- total_train_batch_size: 256
- total_eval_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2.0

### Framework versions

- Transformers 4.28.1
- Pytorch 2.0.0+cu117
- Datasets 2.11.0
- Tokenizers 0.13.3