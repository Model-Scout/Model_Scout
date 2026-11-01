---
pretty_name: Multilingual LIMA Dataset
language:
- en
- zh
- it
- bn
- ko
- th
- vi
- ar
- jv
- sw
dataset_info:
- config_name: ar
  features:
  - name: prompt
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 4408353
    num_examples: 1000
  download_size: 2147971
  dataset_size: 4408353
- config_name: bn
  features:
  - name: prompt
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 7247101
    num_examples: 1000
  download_size: 2577068
  dataset_size: 7247101
- config_name: en
  features:
  - name: prompt
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 2803583
    num_examples: 1000
  download_size: 1617276
  dataset_size: 2803583
- config_name: it
  features:
  - name: prompt
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 3385909
    num_examples: 1000
  download_size: 1933569
  dataset_size: 3385909
- config_name: jv
  features:
  - name: prompt
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 3076706
    num_examples: 1000
  download_size: 1599621
  dataset_size: 3076706
- config_name: ko
  features:
  - name: prompt
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 3500907
    num_examples: 1000
  download_size: 1851853
  dataset_size: 3500907
- config_name: sw
  features:
  - name: prompt
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 3022825
    num_examples: 1000
  download_size: 1663723
  dataset_size: 3022825
- config_name: th
  features:
  - name: prompt
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 7059240
    num_examples: 1000
  download_size: 2615476
  dataset_size: 7059240
- config_name: vi
  features:
  - name: prompt
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 4119447
    num_examples: 1000
  download_size: 1986977
  dataset_size: 4119447
- config_name: zh
  features:
  - name: prompt
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 2801647
    num_examples: 1000
  download_size: 1733683
  dataset_size: 2801647
configs:
- config_name: ar
  data_files:
  - split: train
    path: ar/train-*
- config_name: bn
  data_files:
  - split: train
    path: bn/train-*
- config_name: en
  data_files:
  - split: train
    path: en/train-*
- config_name: it
  data_files:
  - split: train
    path: it/train-*
- config_name: jv
  data_files:
  - split: train
    path: jv/train-*
- config_name: ko
  data_files:
  - split: train
    path: ko/train-*
- config_name: sw
  data_files:
  - split: train
    path: sw/train-*
- config_name: th
  data_files:
  - split: train
    path: th/train-*
- config_name: vi
  data_files:
  - split: train
    path: vi/train-*
- config_name: zh
  data_files:
  - split: train
    path: zh/train-*
---

# Multilingual LIMA Dataset

Each language is stored as a separate Hugging Face **config**, translated by `google/gemini-2.0-flash-001`.

## Usage

```python
from datasets import load_dataset

ds_en = load_dataset("longhp1618/multilingual-lima", "en")
ds_zh = load_dataset("longhp1618/multilingual-lima", "zh")
```