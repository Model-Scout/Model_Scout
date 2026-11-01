---
language:
- ko
license: apache-2.0
tags:
- hf-asr-leaderboard
- whisper-event
- generated_from_trainer
datasets:
- kresnik/zeroth_korean
metrics:
- wer
model-index:
- name: Whisper Medium Korean
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Zeroth Korean
      type: kresnik/zeroth_korean
      config: clean
      split: test
      args: 'split: test'
    metrics:
    - name: Test Wer
      type: wer
      value: 3.6440295136274656
---

적지 않은 분들이 다운로드하셔서 사용하는 걸로 보입니다. https://huggingface.co/seastar105/whisper-medium-komixv2 에 더 좋은 정확도를 기대 가능한 파인튜닝 모델이 있으므로 이쪽을 추천합니다.

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Medium Korean

This model is a fine-tuned version of [openai/whisper-medium](https://huggingface.co/openai/whisper-medium) on the Zeroth Korean dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0727
- Wer: 3.6440
- Cer: 1.4840

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-06
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 5000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    | Cer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|
| 0.0873        | 0.72  | 1000 | 0.1086          | 7.7549 | 2.5597 |
| 0.0258        | 1.44  | 2000 | 0.0805          | 4.5475 | 1.7588 |
| 0.0091        | 2.16  | 3000 | 0.0719          | 3.7946 | 1.5664 |
| 0.0086        | 2.88  | 4000 | 0.0704          | 3.5537 | 1.5232 |
| 0.0019        | 3.59  | 5000 | 0.0727          | 3.6440 | 1.4840 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0a0+d0d6b1f
- Datasets 2.7.1
- Tokenizers 0.13.2
