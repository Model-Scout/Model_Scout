---
library_name: transformers
language:
- ko
license: apache-2.0
base_model: monologg/koelectra-base-v3-discriminator
tags:
- text-classification
- koELECTRA
- Korean-NLP
- topic-classification
- news-classification
- generated_from_trainer
metrics:
- accuracy
- f1
- precision
- recall
model-index:
- name: ynat-model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ynat-model

This model is a fine-tuned version of [monologg/koelectra-base-v3-discriminator](https://huggingface.co/monologg/koelectra-base-v3-discriminator) on the klue-ynat dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4131
- Accuracy: 0.8601
- F1: 0.8614
- Precision: 0.8477
- Recall: 0.8773

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

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     | Precision | Recall |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|:---------:|:------:|
| 0.3952        | 1.0   | 714  | 0.4250          | 0.8523   | 0.8525 | 0.8336    | 0.8755 |
| 0.2963        | 2.0   | 1428 | 0.3992          | 0.8574   | 0.8583 | 0.8454    | 0.8746 |
| 0.2176        | 3.0   | 2142 | 0.4131          | 0.8601   | 0.8614 | 0.8477    | 0.8773 |


### Framework versions

- Transformers 4.54.1
- Pytorch 2.6.0+cu124
- Datasets 4.0.0
- Tokenizers 0.21.4
