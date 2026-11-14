---
library_name: transformers
base_model: monologg/koelectra-small-finetuned-sentiment
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: koelectra_emotion_v1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# koelectra_emotion_v1

This model is a fine-tuned version of [monologg/koelectra-small-finetuned-sentiment](https://huggingface.co/monologg/koelectra-small-finetuned-sentiment) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8551
- Accuracy: 0.7073
- F1: 0.7022

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
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 1.1554        | 1.0   | 1466 | 0.9218          | 0.6726   | 0.6625 |
| 0.8745        | 2.0   | 2932 | 0.8692          | 0.6967   | 0.6866 |
| 0.795         | 3.0   | 4398 | 0.8422          | 0.6997   | 0.6937 |
| 0.7375        | 4.0   | 5864 | 0.8278          | 0.7069   | 0.7025 |
| 0.6909        | 5.0   | 7330 | 0.8426          | 0.7057   | 0.7037 |
| 0.6516        | 6.0   | 8796 | 0.8551          | 0.7073   | 0.7022 |


### Framework versions

- Transformers 4.56.1
- Pytorch 2.8.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.0
