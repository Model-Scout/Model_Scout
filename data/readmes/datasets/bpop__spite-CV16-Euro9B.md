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
    num_bytes: 241596830
    num_examples: 1090061
  download_size: 147278400
  dataset_size: 241596830
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
    num_bytes: 240442143
    num_examples: 1090061
  download_size: 147110108
  dataset_size: 240442143
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
    num_bytes: 245667813
    num_examples: 1090061
  download_size: 149415598
  dataset_size: 245667813
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
    num_bytes: 239926746
    num_examples: 1090061
  download_size: 147508364
  dataset_size: 239926746
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
    num_bytes: 249625817
    num_examples: 1090061
  download_size: 150953813
  dataset_size: 249625817
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
    num_bytes: 238591612
    num_examples: 1090061
  download_size: 145149249
  dataset_size: 238591612
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
    num_bytes: 238164006
    num_examples: 1090061
  download_size: 146753347
  dataset_size: 238164006
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
    num_bytes: 291808807
    num_examples: 1090061
  download_size: 165807495
  dataset_size: 291808807
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
    num_bytes: 225583774
    num_examples: 1090061
  download_size: 144202028
  dataset_size: 225583774
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

Pseudolabeled speech translation data with quality annotations from multiple metrics. This version uses transcripts from [Common Voice 16.1](https://commonvoice.mozilla.org/en) and translations from [EuroLLM-9B-Instruct](https://huggingface.co/utter-project/EuroLLM-9B-Instruct).

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
