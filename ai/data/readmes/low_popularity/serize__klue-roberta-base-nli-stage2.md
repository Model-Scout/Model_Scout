---
library_name: transformers
base_model: klue/roberta-base
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: klue-roberta-base-nli-stage2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# klue-roberta-base-nli-stage2

This model is a fine-tuned version of [klue/roberta-base](https://huggingface.co/klue/roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5985
- Accuracy: 0.86

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
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 0.1
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.4494        | 1.0   | 1563 | 0.4498          | 0.838    |
| 0.2826        | 2.0   | 3126 | 0.5092          | 0.8473   |
| 0.1520        | 3.0   | 4689 | 0.5985          | 0.86     |


### Framework versions

- Transformers 5.0.0
- Pytorch 2.11.0+cu128
- Datasets 4.0.0
- Tokenizers 0.22.2
