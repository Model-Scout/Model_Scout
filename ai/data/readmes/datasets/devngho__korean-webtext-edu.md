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
    num_bytes: 8528708812
    num_examples: 1284879
  download_size: 4462835969
  dataset_size: 8528708812
- config_name: scored_over_2
  features:
  - name: text
    dtype: string
  - name: score
    dtype: float64
  splits:
  - name: train
    num_bytes: 3729474351.820441
    num_examples: 561858
  download_size: 2075034458
  dataset_size: 3729474351.820441
- config_name: scored_over_3
  features:
  - name: text
    dtype: string
  - name: score
    dtype: float64
  splits:
  - name: train
    num_bytes: 854185819.9729562
    num_examples: 128686
  download_size: 494289966
  dataset_size: 854185819.9729562
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
- HAERAE-HUB/KOREAN-WEBTEXT
task_categories:
- text-generation
language:
- ko
size_categories:
- 100K<n<1M
---

## 🇰🇷🌐📚 korean-webtext-edu

[HAERAE-HUB/KOREAN-WEBTEXT](https://huggingface.co/datasets/HAERAE-HUB/KOREAN-WEBTEXT)를 [devngho/ko_edu_classifier_v2_nlpai-lab_KoE5](https://huggingface.co/devngho/ko_edu_classifier_v2_nlpai-lab_KoE5) 모델로 평가한 데이터셋

### 불러오기

```py
from datasets import load_dataset

ds = load_dataset("devngho/korean-webtext-edu", name="scored_over_3", split="train")
```

### 성능

예정

### 컴퓨팅

Google Cloud TPU, transformers, [JAX](https://github.com/jax-ml/jax), [tpuswarm](https://github.com/devngho/tpuswarm)

#### 하드웨어

TPU v4-8 x 4 instances, 약 35분 소요

이 연구는 Google의 TPU Research Cloud [(TRC)](https://sites.research.google/trc/about/)의 Cloud TPU 제공으로 수행되었습니다. ⚡

### 라이선스

원본 데이터셋(HAERAE-HUB/KOREAN-WEBTEXT)은 라이선스가 기재되어 있지 않습니다. 이 데이터셋은 [MIT 라이선스](https://huggingface.co/datasets/choosealicense/licenses/blob/main/markdown/mit.md)로 배포되지만, 원본 데이터셋의 사용 가능 여부를 직접 확인하시고 사용하시기를 권합니다.