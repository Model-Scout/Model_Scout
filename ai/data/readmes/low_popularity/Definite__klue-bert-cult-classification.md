---
license: cc-by-sa-4.0
base_model: Definite/klue-bert-mlm-bible
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: klue-bert-cult-classification
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# klue-bert-cult-classification

This model is a fine-tuned version of [Definite/klue-bert-mlm-bible](https://huggingface.co/Definite/klue-bert-mlm-bible) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0816
- Accuracy: 0.988

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 6

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 313  | 0.1386          | 0.984    |
| 0.0203        | 2.0   | 626  | 0.0910          | 0.9853   |
| 0.0203        | 3.0   | 939  | 0.0745          | 0.989    |
| 0.0031        | 4.0   | 1252 | 0.0900          | 0.9877   |
| 0.0004        | 5.0   | 1565 | 0.0823          | 0.988    |
| 0.0004        | 6.0   | 1878 | 0.0816          | 0.988    |


### Framework versions

- Transformers 4.35.2
- Pytorch 2.1.0+cu118
- Datasets 2.15.0
- Tokenizers 0.15.0
