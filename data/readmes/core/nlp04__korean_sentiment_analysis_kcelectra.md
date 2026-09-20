---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: korean_sentiment_analysis_kcelectra
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# korean_sentiment_analysis_kcelectra

This model is a fine-tuned version of [beomi/KcELECTRA-base-v2022](https://huggingface.co/beomi/KcELECTRA-base-v2022) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9718
- Micro f1 score: 70.7183
- Auprc: 68.4562
- Accuracy: 0.7072

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 256
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 10.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Micro f1 score | Auprc   | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------------:|:-------:|:--------:|
| 1.0543        | 1.0   | 391  | 0.9923          | 65.3061        | 49.6906 | 0.6531   |
| 0.8573        | 2.0   | 782  | 0.8229          | 69.9901        | 64.4071 | 0.6999   |
| 0.7217        | 3.0   | 1173 | 0.7961          | 71.0600        | 67.4640 | 0.7106   |
| 0.6305        | 4.0   | 1564 | 0.8163          | 71.1229        | 68.5191 | 0.7112   |
| 0.5294        | 5.0   | 1955 | 0.8205          | 71.0150        | 68.7334 | 0.7102   |
| 0.4689        | 6.0   | 2346 | 0.8716          | 71.1679        | 68.7751 | 0.7117   |
| 0.433         | 7.0   | 2737 | 0.9086          | 70.9880        | 68.3653 | 0.7099   |
| 0.419         | 8.0   | 3128 | 0.9290          | 70.6734        | 68.4606 | 0.7067   |
| 0.3766        | 9.0   | 3519 | 0.9619          | 70.6464        | 68.5132 | 0.7065   |
| 0.3395        | 10.0  | 3910 | 0.9718          | 70.7183        | 68.4562 | 0.7072   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.6.0
- Datasets 2.7.1
- Tokenizers 0.13.2
