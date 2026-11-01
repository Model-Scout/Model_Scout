---
language:
- ko
---
This dataset is a filtered dataset of the [mncai/kin_med_2M](https://huggingface.co/datasets/mncai/kin_med_2M/) dataset.

---
dataset_info:
  features:
  - name: instruction
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 1148794959.3408744
    num_examples: 791469
  download_size: 758333953
  dataset_size: 1148794959.3408744
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
