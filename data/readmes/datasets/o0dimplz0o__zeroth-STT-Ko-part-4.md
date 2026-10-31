---
language:
- ko
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
    num_bytes: 1113459385.076
    num_examples: 10226
  download_size: 1016618966
  dataset_size: 1113459385.076
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
# Zeroth-STT-Korean Dataset

## Description
This is a one of ten equally divided parts of the Zeroth-STT-Korean dataset. Ten equal shards of the original dataset were created and uploaded as individual repos for fine-tuning/training needs.

## Citation

Zeroth-Korean Dataset, created by [Lucas Jo(@Atlas Guide Inc.) and Wonkyum Lee(@Gridspace Inc.)], 2023.
Available at https://github.com/goodatlas/zeroth under CC-BY-4.0 license.

Junhoee/STT_Korean_Dataset_80000 Dataset, created by [Junhoee], 2024.
Available at https://huggingface.co/datasets/Junhoee/STT_Korean_Dataset_80000