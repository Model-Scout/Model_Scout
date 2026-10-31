---
dataset_info:
- config_name: raw
  features:
  - name: text
    dtype: string
  - name: score
    dtype: float64
  splits:
  - name: train
    num_bytes: 641750068
    num_examples: 312352
  download_size: 373614461
  dataset_size: 641750068
- config_name: scored_over_2
  features:
  - name: text
    dtype: string
  - name: score
    dtype: float64
  splits:
  - name: train
    num_bytes: 467388707.99327683
    num_examples: 227487
  download_size: 285736778
  dataset_size: 467388707.99327683
- config_name: scored_over_3
  features:
  - name: text
    dtype: string
  - name: score
    dtype: float64
  splits:
  - name: train
    num_bytes: 133878048.42276663
    num_examples: 65161
  download_size: 104199742
  dataset_size: 133878048.42276663
configs:
- config_name: raw
  data_files:
  - split: train
    path: raw/train-*
- config_name: scored_over_2
  data_files:
  - split: train
    path: scored_over_2/train-*
- config_name: scored_over_3
  data_files:
  - split: train
    path: scored_over_3/train-*
  default: true
license: cc-by-sa-4.0
task_categories:
- text-generation
language:
- ko
size_categories:
- 10K<n<100K
- 100K<n<1M
---

## 🇰🇷📚 korean-wikipedia-edu

[devngho/korean_wikipedia](https://huggingface.co/datasets/devngho/korean_wikipedia)의 20240701-filtered subset을 [devngho/ko_edu_classifier_v2_nlpai-lab_KoE5](https://huggingface.co/devngho/ko_edu_classifier_v2_nlpai-lab_KoE5) 모델로 평가한 데이터셋

### 불러오기

```py
from datasets import load_dataset

ds = load_dataset("devngho/korean-wikipedia-edu", name="scored_over_3", split="train")
```

### 성능

예정

### 컴퓨팅

Google Cloud TPU, transformers, [JAX](https://github.com/jax-ml/jax), [tpuswarm](https://github.com/devngho/tpuswarm)

#### 하드웨어

TPU v4-8 x 4 instances, 약 10분 소요

이 연구는 Google의 TPU Research Cloud [(TRC)](https://sites.research.google/trc/about/)의 Cloud TPU 제공으로 수행되었습니다. ⚡

### 라이선스

한국어 위키백과의 [CC BY-SA 4.0 DEED](https://creativecommons.org/licenses/by-sa/4.0/deed.ko) 라이선스에 따라 이 데이터셋에는 [CC BY-SA 4.0 DEED](https://creativecommons.org/licenses/by-sa/4.0/deed.ko) 라이선스가 적용됩니다.