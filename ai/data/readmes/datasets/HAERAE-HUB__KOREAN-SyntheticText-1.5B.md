---
dataset_info:
  features:
  - name: text
    dtype: string
  - name: __index_level_0__
    dtype: int64
  splits:
  - name: train
    num_bytes: 6024153349
    num_examples: 1552370
  download_size: 2971513787
  dataset_size: 6024153349
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

# KOREAN-SyntheticText

**KOREAN-SyntheticText** is a successor of the **KOREAN-WEBTEXT** project in our mission to create high-quality Korean corpora. The dataset consists of 1.4B tokens generated over 600 H100 hours following the [Cosmopedia](https://huggingface.co/blog/cosmopedia) project.

The dataset has been generated using a 100B + open-source LLM fine-tuned on text generation. No filtering has been done yet.