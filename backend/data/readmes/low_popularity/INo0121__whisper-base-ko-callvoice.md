---
language:
- ko
license: apache-2.0
base_model: openai/whisper-base
tags:
- hf-asr-leaderboard
- generated_from_trainer
datasets:
- INo0121/low_quality_call_voice
model-index:
- name: Whisper Base for Korean Low quaiity Call Voices
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Base for Korean Low quaiity Call Voices

This model is a fine-tuned version of [openai/whisper-base](https://huggingface.co/openai/whisper-base) on the Korean Low Quaiity Call Voices dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4941
- Cer: 30.7538

## Model description

프로젝트 용도로 파인튜닝된 모델입니다.
OpenAI의 Whisper-Base 모델을 바탕으로 '한국어 저음질 음성 통화 데이터'에 대한 정확도를 증가시키고자 파인튜닝을 진행한 모델이며,
사용한 데이터는 AI-HUB의 ‘저음질 전화망 음성인식 데이터’ 중 일부로서 오디오 파일 기준 240,771.06초(파일 1개당 평균 길이는 약 5.296초)
텍스트 데이터 기준 총 1,696,414글자의 크기입니다.

This is a fine-tuned model for project use.
This model was fine-tuned to increase the accuracy of ‘Korean low-quality voice call data’ based on OpenAI’s Whisper-Base model.
The data used is part of AI-HUB’s ‘low-quality telephone network voice recognition data’,
which is 240,771.06 seconds based on audio files(average length per file is about 5.296 seconds).
The total size is 1,696,414 characters based on text data.

## Intended uses & limitations

파인튜닝에 사용된 Base model과 dataset 모두 학습 목적으로 사용하였으며,
따라서 본 모델 역시 학습 목적으로만 사용 가능합니다.

Both the base model and dataset used for fine tuning were used for learning purposes,
so this model can also be used only for learning purposes.

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
- training_steps: 8000

### Training results

| Training Loss | Epoch | Step | Validation Loss | Cer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.6416        | 0.44  | 1000 | 0.6564          | 64.1489 |
| 0.5914        | 0.88  | 2000 | 0.5688          | 37.4957 |
| 0.435         | 1.32  | 3000 | 0.5349          | 32.6734 |
| 0.4056        | 1.76  | 4000 | 0.5124          | 30.9065 |
| 0.3368        | 2.2   | 5000 | 0.5057          | 32.6925 |
| 0.3107        | 2.64  | 6000 | 0.4979          | 32.8315 |
| 0.3016        | 3.08  | 7000 | 0.4947          | 29.3060 |
| 0.2979        | 3.52  | 8000 | 0.4941          | 30.7538 |


### Framework versions

- Transformers 4.34.0.dev0
- Pytorch 2.0.1+cu118
- Datasets 2.14.5
- Tokenizers 0.13.3
