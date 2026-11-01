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
    num_bytes: 18413993666
    num_examples: 4414956
  download_size: 6813327957
  dataset_size: 18413993666
- config_name: scored_over_2
  features:
  - name: text
    dtype: string
  - name: score
    dtype: float64
  splits:
  - name: train
    num_bytes: 16556122056.735634
    num_examples: 3969511
  download_size: 6199789090
  dataset_size: 16556122056.735634
- config_name: scored_over_3
  features:
  - name: text
    dtype: string
  - name: score
    dtype: float64
  splits:
  - name: train
    num_bytes: 7237438964.033805
    num_examples: 1735255
  download_size: 2832546560
  dataset_size: 7237438964.033805
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
license: mit
source_datasets:
- maywell/korean_textbooks
task_categories:
- text-generation
language:
- ko
size_categories:
- 1M<n<10M
---

## 🇰🇷📚 korean-textbooks-edu

[maywell/korean_textbooks](https://huggingface.co/datasets/maywell/korean_textbooks)의 모든 subset을 [devngho/ko_edu_classifier_v2_nlpai-lab_KoE5](https://huggingface.co/devngho/ko_edu_classifier_v2_nlpai-lab_KoE5) 모델로 평가한 데이터셋

### 불러오기

```py
from datasets import load_dataset

ds = load_dataset("devngho/korean-textbooks-edu", name="scored_over_3", split="train")
```

### 성능

예정

### 컴퓨팅

Google Cloud TPU, transformers, [JAX](https://github.com/jax-ml/jax), [tpuswarm](https://github.com/devngho/tpuswarm)

#### 하드웨어

TPU v4-8 x 4 instances, 약 2시간 소요

이 연구는 Google의 TPU Research Cloud [(TRC)](https://sites.research.google/trc/about/)의 Cloud TPU 제공으로 수행되었습니다. ⚡

### 라이선스

원본 데이터셋(maywell/korean_textbooks)은 [Apache 2.0](https://huggingface.co/datasets/choosealicense/licenses/blob/main/markdown/apache-2.0.md) 라이선스를 따릅니다. 이 데이터셋은 [MIT 라이선스](https://huggingface.co/datasets/choosealicense/licenses/blob/main/markdown/mit.md)로 배포됩니다.