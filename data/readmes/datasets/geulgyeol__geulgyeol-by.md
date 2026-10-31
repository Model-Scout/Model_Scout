---
language:
- ko
license: cc-by-4.0
task_categories:
- text-generation
dataset_info:
  features:
  - name: url
    dtype: large_string
  - name: title
    dtype: large_string
  - name: author
    dtype: large_string
  - name: text
    dtype: large_string
  - name: markdown
    dtype: large_string
  - name: markdown_text
    dtype: large_string
  - name: raw
    dtype: large_string
  - name: accessed_at
    dtype: int64
  - name: written_at
    dtype: int64
  - name: ccl
    dtype: large_string
  splits:
  - name: train
    num_bytes: 7831979554
    num_examples: 204395
  download_size: 2472625394
  dataset_size: 7831979554
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

![geulgyeol logo](https://huggingface.co/datasets/geulgyeol/metadata/resolve/main/geulgyeol_w256.png)

PREVIEW