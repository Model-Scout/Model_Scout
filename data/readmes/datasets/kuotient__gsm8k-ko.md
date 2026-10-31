---
dataset_info:
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: question_en
    dtype: string
  - name: answer_en
    dtype: string
  splits:
  - name: train
    num_bytes: 8792462
    num_examples: 7473
  - name: test
    num_bytes: 1585126
    num_examples: 1319
  download_size: 6575639
  dataset_size: 10377588
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
language:
- ko
pretty_name: g
---
번역 모델 `kuotient/Seagull-13B-translate` 사용.

## How to evaluate
```
git clone https://github.com/kuotient/lm-evaluation-harness.git
cd lm-evaluation-harness
pip install -e .
```

```
lm_eval --model hf \
    --model_args pretrained=yanolja/EEVE-Korean-Instruct-2.8B-v1.0 \
    --tasks gsm8k-ko \
    --device cuda:0 \
    --batch_size auto:4
```
혹은 원본 lm-evaluation-harness에서

데이터셋 내의 `gsm8k-ko.yaml` 파일을 `lm-evaluation-harness/tasks/gsm8k-ko` 내에 생성해 사용.