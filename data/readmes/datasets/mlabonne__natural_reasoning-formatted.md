---
license: cc-by-nc-4.0
task_categories:
- text-generation
language:
- en
pretty_name: Natural Reasoning
size_categories:
- 1M<n<10M
dataset_info:
  features:
  - name: messages
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  splits:
  - name: train
    num_bytes: 3905006186
    num_examples: 1145824
  download_size: 1744787002
  dataset_size: 3905006186
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

# Natural reasoning

This is a reformatted version of [facebook/natural_reasoning](https://huggingface.co/datasets/facebook/natural_reasoning) to match the HF/OAI format.