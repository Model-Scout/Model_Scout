---
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
    num_bytes: 11169954042.658998
    num_examples: 102263
  download_size: 10204609448
  dataset_size: 11169954042.658998
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: apache-2.0
task_categories:
- automatic-speech-recognition
language:
- ko
size_categories:
- 100K<n<1M
---
# Zeroth-STT-Korean Dataset

## Description
This is a shuffled version of the Zeroth-STT-Ko dataset.

## Citation

Zeroth-Korean Dataset, created by [Lucas Jo(@Atlas Guide Inc.) and Wonkyum Lee(@Gridspace Inc.)], 2023.
Available at https://github.com/goodatlas/zeroth under CC-BY-4.0 license.

Junhoee/STT_Korean_Dataset_80000 Dataset, created by [Junhoee], 2024.
Available at https://huggingface.co/datasets/Junhoee/STT_Korean_Dataset_80000

