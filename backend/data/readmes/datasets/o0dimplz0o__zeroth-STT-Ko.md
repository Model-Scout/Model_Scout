---
license: apache-2.0
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
dataset_info:
  features:
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 11169873357.152
    num_examples: 102263
  download_size: 10186919269
  dataset_size: 11169873357.152
task_categories:
- automatic-speech-recognition
language:
- ko
size_categories:
- 100K<n<1M
pretty_name: zeroth-STT-Ko
---
# Zeroth-STT-Ko Dataset

## Description
This dataset combines the following publicly available Korean language datasets:

Junhoee/STT_Korean_Dataset_80000
and
Zeroth-Korean Dataset (from Project: Zeroth, by GoodAtlas and Gridspace)

This provides over 102K rows of data (sentences) in total.

## Citation

Zeroth-Korean Dataset, created by [Lucas Jo(@Atlas Guide Inc.) and Wonkyum Lee(@Gridspace Inc.)], 2023.
Available at https://github.com/goodatlas/zeroth under CC-BY-4.0 license.

Junhoee/STT_Korean_Dataset_80000 Dataset, created by [Junhoee], 2024.
Available at https://huggingface.co/datasets/Junhoee/STT_Korean_Dataset_80000