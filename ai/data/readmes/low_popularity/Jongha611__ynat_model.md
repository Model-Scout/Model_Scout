---
library_name: transformers
language:
- ko
license: apache-2.0
base_model: monologg/koelectra-base-v3-discriminator
tags:
- text-classification
- KoELECTRA
- Korean-NLP
- topic-classification
- news-classification
- generated_from_trainer
model-index:
- name: ynat_model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ynat_model

This model is a fine-tuned version of [monologg/koelectra-base-v3-discriminator](https://huggingface.co/monologg/koelectra-base-v3-discriminator) on the klue-ynat dataset.
It achieves the following results on the evaluation set:
- eval_loss: 2.0522
- eval_accuracy: 0.0917
- eval_precision: 0.0131
- eval_recall: 0.1429
- eval_f1: 0.0240
- eval_runtime: 14.6861
- eval_samples_per_second: 620.111
- eval_steps_per_second: 38.812
- epoch: 1.0
- step: 2855

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3

### Framework versions

- Transformers 4.54.1
- Pytorch 2.6.0+cu124
- Datasets 4.0.0
- Tokenizers 0.21.4
