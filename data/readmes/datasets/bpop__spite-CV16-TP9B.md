---
language:
- en
- de
- es
- fr
- it
- ko
- nl
- pt
- ru
- zh
license: apache-2.0
task_categories:
- translation
- automatic-speech-recognition
configs:
- config_name: en_de
  data_files:
  - split: train
    path: en_de/train-*
- config_name: en_es
  data_files:
  - split: train
    path: en_es/train-*
- config_name: en_fr
  data_files:
  - split: train
    path: en_fr/train-*
- config_name: en_it
  data_files:
  - split: train
    path: en_it/train-*
- config_name: en_ko
  data_files:
  - split: train
    path: en_ko/train-*
- config_name: en_nl
  data_files:
  - split: train
    path: en_nl/train-*
- config_name: en_pt
  data_files:
  - split: train
    path: en_pt/train-*
- config_name: en_ru
  data_files:
  - split: train
    path: en_ru/train-*
- config_name: en_zh
  data_files:
  - split: train
    path: en_zh/train-*
dataset_info:
- config_name: en_de
  features:
  - name: src
    dtype: string
  - name: mt
    dtype: string
  - name: cometqe_22
    dtype: float64
  - name: xcomet_xl
    dtype: float64
  - name: blaser2_src
    dtype: float64
  - name: audio_length
    dtype: float64
  - name: example_id
    dtype: string
  - name: index
    dtype: int64
  - name: blaser2_mt
    dtype: float64
  splits:
  - name: train
    num_bytes: 242241706
    num_examples: 1090061
  download_size: 147879059
  dataset_size: 242241706
- config_name: en_es
  features:
  - name: src
    dtype: string
  - name: mt
    dtype: string
  - name: cometqe_22
    dtype: float64
  - name: xcomet_xl
    dtype: float64
  - name: blaser2_src
    dtype: float64
  - name: audio_length
    dtype: float64
  - name: example_id
    dtype: string
  - name: index
    dtype: int64
  - name: blaser2_mt
    dtype: float64
  splits:
  - name: train
    num_bytes: 241394834
    num_examples: 1090061
  download_size: 147658485
  dataset_size: 241394834
- config_name: en_fr
  features:
  - name: src
    dtype: string
  - name: mt
    dtype: string
  - name: cometqe_22
    dtype: float64
  - name: xcomet_xl
    dtype: float64
  - name: blaser2_src
    dtype: float64
  - name: audio_length
    dtype: float64
  - name: example_id
    dtype: string
  - name: index
    dtype: int64
  - name: blaser2_mt
    dtype: float64
  splits:
  - name: train
    num_bytes: 246376988
    num_examples: 1090061
  download_size: 150114773
  dataset_size: 246376988
- config_name: en_it
  features:
  - name: src
    dtype: string
  - name: mt
    dtype: string
  - name: cometqe_22
    dtype: float64
  - name: xcomet_xl
    dtype: float64
  - name: blaser2_src
    dtype: float64
  - name: audio_length
    dtype: float64
  - name: example_id
    dtype: string
  - name: index
    dtype: int64
  - name: blaser2_mt
    dtype: float64
  splits:
  - name: train
    num_bytes: 240741077
    num_examples: 1090061
  download_size: 148012842
  dataset_size: 240741077
- config_name: en_ko
  features:
  - name: src
    dtype: string
  - name: mt
    dtype: string
  - name: cometqe_22
    dtype: float64
  - name: xcomet_xl
    dtype: float64
  - name: blaser2_src
    dtype: float64
  - name: audio_length
    dtype: float64
  - name: example_id
    dtype: string
  - name: index
    dtype: int64
  - name: blaser2_mt
    dtype: float64
  splits:
  - name: train
    num_bytes: 251643783
    num_examples: 1090061
  download_size: 151428634
  dataset_size: 251643783
- config_name: en_nl
  features:
  - name: src
    dtype: string
  - name: mt
    dtype: string
  - name: cometqe_22
    dtype: float64
  - name: xcomet_xl
    dtype: float64
  - name: blaser2_src
    dtype: float64
  - name: audio_length
    dtype: float64
  - name: example_id
    dtype: string
  - name: index
    dtype: int64
  - name: blaser2_mt
    dtype: float64
  splits:
  - name: train
    num_bytes: 239544369
    num_examples: 1090061
  download_size: 145787834
  dataset_size: 239544369
- config_name: en_pt
  features:
  - name: src
    dtype: string
  - name: mt
    dtype: string
  - name: cometqe_22
    dtype: float64
  - name: xcomet_xl
    dtype: float64
  - name: blaser2_src
    dtype: float64
  - name: audio_length
    dtype: float64
  - name: example_id
    dtype: string
  - name: index
    dtype: int64
  - name: blaser2_mt
    dtype: float64
  splits:
  - name: train
    num_bytes: 239353736
    num_examples: 1090061
  download_size: 147486964
  dataset_size: 239353736
- config_name: en_ru
  features:
  - name: src
    dtype: string
  - name: mt
    dtype: string
  - name: cometqe_22
    dtype: float64
  - name: xcomet_xl
    dtype: float64
  - name: blaser2_src
    dtype: float64
  - name: audio_length
    dtype: float64
  - name: example_id
    dtype: string
  - name: index
    dtype: int64
  - name: blaser2_mt
    dtype: float64
  splits:
  - name: train
    num_bytes: 295652127
    num_examples: 1090061
  download_size: 167496925
  dataset_size: 295652127
- config_name: en_zh
  features:
  - name: src
    dtype: string
  - name: mt
    dtype: string
  - name: cometqe_22
    dtype: float64
  - name: xcomet_xl
    dtype: float64
  - name: blaser2_src
    dtype: float64
  - name: audio_length
    dtype: float64
  - name: example_id
    dtype: string
  - name: index
    dtype: int64
  - name: blaser2_mt
    dtype: float64
  splits:
  - name: train
    num_bytes: 226769115
    num_examples: 1090061
  download_size: 144717792
  dataset_size: 226769115
---

# Spite Dataset

Pseudolabeled speech translation data with quality annotations from multiple metrics. This version uses transcripts from [Common Voice 16.1](https://commonvoice.mozilla.org/en) and translations from [Tower-Plus-9B](https://huggingface.co/Unbabel/Tower-Plus-9B/).

## Configs
- en_de
- en_es
- en_fr
- en_it
- en_ko
- en_nl
- en_pt
- en_ru
- en_zh

## Usage

```python
from datasets import load_dataset
ds = load_dataset("bpop/spite-CV16-Euro9B", "en_pt")
```
