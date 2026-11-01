---
language:
- ko
license: cc-by-nc-4.0
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
    num_bytes: 54370706875
    num_examples: 1313581
  download_size: 17963163604
  dataset_size: 54370706875
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

![geulgyeol logo](https://huggingface.co/datasets/geulgyeol/metadata/resolve/main/geulgyeol_w256.png)

PREVIEW
