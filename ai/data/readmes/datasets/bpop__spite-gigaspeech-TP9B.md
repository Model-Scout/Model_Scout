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
    num_bytes: 1923112720
    num_examples: 8282988
  download_size: 1271538322
  dataset_size: 1923112720
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
    num_bytes: 1888557877
    num_examples: 8282988
  download_size: 1261031393
  dataset_size: 1888557877
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
    num_bytes: 1936989910
    num_examples: 8282988
  download_size: 1284609546
  dataset_size: 1936989910
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
    num_bytes: 1882464034
    num_examples: 8282988
  download_size: 1262889264
  dataset_size: 1882464034
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
    num_bytes: 1994335847
    num_examples: 8282988
  download_size: 1293242121
  dataset_size: 1994335847
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
    num_bytes: 1877956825
    num_examples: 8282988
  download_size: 1249335271
  dataset_size: 1877956825
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
    num_bytes: 1878535357
    num_examples: 8282988
  download_size: 1256310117
  dataset_size: 1878535357
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
    num_bytes: 2338604523
    num_examples: 8282988
  download_size: 1418570245
  dataset_size: 2338604523
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
    num_bytes: 1791747571
    num_examples: 8282988
  download_size: 1234948784
  dataset_size: 1791747571
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
---

# Spite Dataset

Pseudolabeled speech translation data with quality annotations from multiple metrics. This version uses transcripts from [GigaSpeech](https://huggingface.co/datasets/speechcolab/gigaspeech) and translations from [Tower-Plus-9B](https://huggingface.co/Unbabel/Tower-Plus-9B).

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
