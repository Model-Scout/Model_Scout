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
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: ynat-model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ynat-model

This model is a fine-tuned version of [monologg/koelectra-base-v3-discriminator](https://huggingface.co/monologg/koelectra-base-v3-discriminator) on the klue-ynat dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4073
- Accuracy: 0.8602
- Precision: 0.8507
- Recall: 0.8716
- F1: 0.8606

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.3947        | 1.0   | 714  | 0.4222          | 0.8506   | 0.8421    | 0.8679 | 0.8536 |
| 0.297         | 2.0   | 1428 | 0.3969          | 0.8564   | 0.8474    | 0.8668 | 0.8558 |
| 0.2189        | 3.0   | 2142 | 0.4073          | 0.8602   | 0.8507    | 0.8716 | 0.8606 |


### Framework versions

- Transformers 4.54.1
- Pytorch 2.6.0+cu124
- Datasets 4.0.0
- Tokenizers 0.21.4
