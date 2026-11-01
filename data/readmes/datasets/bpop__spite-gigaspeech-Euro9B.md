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
    num_bytes: 1912480336
    num_examples: 8282988
  download_size: 1265286546
  dataset_size: 1912480336
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
    num_bytes: 1875580355
    num_examples: 8282988
  download_size: 1254245676
  dataset_size: 1875580355
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
    num_bytes: 1929321630
    num_examples: 8282988
  download_size: 1278694957
  dataset_size: 1929321630
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
    num_bytes: 1868438454
    num_examples: 8282988
  download_size: 1254176187
  dataset_size: 1868438454
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
    num_bytes: 1988081635
    num_examples: 8282988
  download_size: 1287788948
  dataset_size: 1988081635
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
    num_bytes: 1865531337
    num_examples: 8282988
  download_size: 1241242870
  dataset_size: 1865531337
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
    num_bytes: 1868525017
    num_examples: 8282988
  download_size: 1248582221
  dataset_size: 1868525017
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
    num_bytes: 2308034493
    num_examples: 8282988
  download_size: 1402135781
  dataset_size: 2308034493
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
    num_bytes: 1775163602
    num_examples: 8282988
  download_size: 1220573747
  dataset_size: 1775163602
---

# Spite Dataset

Pseudolabeled speech translation data with quality annotations from multiple metrics. This version uses transcripts from [GigaSpeech](https://huggingface.co/datasets/speechcolab/gigaspeech) and translations from [EuroLLM-9B-Instruct](https://huggingface.co/utter-project/EuroLLM-9B-Instruct).

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
