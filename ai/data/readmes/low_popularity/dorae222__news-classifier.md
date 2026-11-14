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
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: news-classifier
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# news-classifier

This model is a fine-tuned version of [monologg/koelectra-base-v3-discriminator](https://huggingface.co/monologg/koelectra-base-v3-discriminator) on the klue-ynat dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4045
- Accuracy: 0.8580
- Precision: 0.8488
- Recall: 0.8763
- F1: 0.8616

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
- train_batch_size: 128
- eval_batch_size: 128
- seed: 42
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.3898        | 1.0   | 357  | 0.5086          | 0.8196   | 0.8186    | 0.8635 | 0.8352 |
| 0.3121        | 2.0   | 714  | 0.4012          | 0.8536   | 0.8476    | 0.8727 | 0.8584 |
| 0.2433        | 3.0   | 1071 | 0.4045          | 0.8580   | 0.8488    | 0.8763 | 0.8616 |


### Framework versions

- Transformers 4.54.1
- Pytorch 2.6.0+cu124
- Datasets 2.19.2
- Tokenizers 0.21.4-dev.0
