---
dataset_info:
  features:
  - name: id
    dtype: int64
  - name: text
    dtype: string
  - name: Instruction
    dtype: string
  - name: Reasoning
    dtype: string
  - name: Reasoning Answer
    dtype: string
  - name: Final Answer
    dtype: string
  - name: __index_level_0__
    dtype: int64
  splits:
  - name: train
    num_bytes: 3119512656
    num_examples: 730695
  download_size: 694203563
  dataset_size: 3119512656
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: cc-by-sa-3.0
---

# kowikitext-qa-ref-detail-preview

Korean Wikipedia texts into QA-like with reasoning process dataset.

This release is preview released.

License follows original Wikipedia(CC-BY-SA-3.0)