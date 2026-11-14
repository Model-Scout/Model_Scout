---
library_name: transformers
language:
- ko
license: apache-2.0
base_model: monologg/koelectra-base-v3-discriminator
tags:
- text_calssification
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

This model is a fine-tuned version of [monologg/koelectra-base-v3-discriminator](https://huggingface.co/monologg/koelectra-base-v3-discriminator) on the klue_ynat dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4085
- Accuracy: 0.8608
- Precision: 0.8485
- Recall: 0.8791
- F1: 0.8626

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
| 0.4121        | 1.0   | 714  | 0.4943          | 0.8372   | 0.8100    | 0.8725 | 0.8364 |
| 0.3046        | 2.0   | 1428 | 0.4012          | 0.8548   | 0.8457    | 0.8677 | 0.8549 |
| 0.2233        | 3.0   | 2142 | 0.4085          | 0.8608   | 0.8485    | 0.8791 | 0.8626 |


### Framework versions

- Transformers 4.54.1
- Pytorch 2.6.0+cu124
- Datasets 4.0.0
- Tokenizers 0.21.4
