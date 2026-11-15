---
library_name: transformers
language:
- ko
license: mit
base_model: openai/whisper-large-v3-turbo
tags:
- generated_from_trainer
datasets:
- Bingsu/zeroth-korean
- mozilla-foundation/common_voice_17_0
metrics:
- wer
model-index:
- name: Whisper large v3 turbo Korean - imTak
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Zeroth-Korean
      type: Bingsu/zeroth-korean
      args: 'config: ko, split: test'
    metrics:
    - name: Wer
      type: wer
      value: 5.270290618882698
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper large v3 turbo Korean - imTak

This model is a fine-tuned version of [imTak/whisper_large_v3_ko_ft](https://huggingface.co/imTak/whisper_large_v3_ko_ft) on the Zeroth-Korean dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0670
- Wer: 5.2703

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 4000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Wer    |
|:-------------:|:------:|:----:|:---------------:|:------:|
| 0.1068        | 0.7184 | 1000 | 0.1216          | 8.6132 |
| 0.0388        | 1.4368 | 2000 | 0.0905          | 5.3606 |
| 0.0089        | 2.1552 | 3000 | 0.0707          | 4.7282 |
| 0.0082        | 2.8736 | 4000 | 0.0670          | 5.2703 |


### Framework versions

- Transformers 4.45.0
- Pytorch 2.5.1+cu124
- Datasets 3.1.0
- Tokenizers 0.20.3
