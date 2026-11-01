---
dataset_info:
  features:
  - name: messages
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 4024694246
    num_examples: 1043917
  - name: test
    num_bytes: 211451508
    num_examples: 54948
  download_size: 2110004410
  dataset_size: 4236145754
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
---

# smoltalk-flat

A lazy flattened version of the excellent [HuggingFaceTB/smoltalk](https://huggingface.co/datasets/HuggingFaceTB/smoltalk) dataset so the "all" split becomes "default" split (due to compatibility issues with most fine-tuning frameworks).

For [MaziyarPanahi](https://huggingface.co/MaziyarPanahi)!