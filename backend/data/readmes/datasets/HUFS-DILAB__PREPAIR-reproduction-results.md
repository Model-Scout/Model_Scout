---
license: mit
task_categories:
- text-generation
language:
- en
- ko
pretty_name: PREPAIR Reproduction Results
viewer: true
dataset_info:
  config_name: LLMBar
  features:
  - name: original_question
    dtype: string
  - name: output_a
    dtype: string
  - name: output_b
    dtype: string
  - name: label
    dtype: int64
  - name: pointwise_pred
    dtype: int64
  - name: pointwise_correct
    dtype: bool
  - name: pairwise_raw
    dtype: string
  - name: pairwise_pred
    dtype: int64
  - name: pairwise_correct
    dtype: bool
  - name: w_CoT_raw
    dtype: string
  - name: w_CoT_pred
    dtype: int64
  - name: w_CoT_correct
    dtype: bool
  - name: w_PREPAIR_star_explanation
    dtype: string
  - name: w_PREPAIR_star_raw
    dtype: string
  - name: w_PREPAIR_star_pred
    dtype: int64
  - name: w_PREPAIR_star_correct
    dtype: bool
  - name: w_PREPAIR_explanation
    dtype: string
  - name: w_PREPAIR_raw
    dtype: string
  - name: w_PREPAIR_pred
    dtype: int64
  - name: w_PREPAIR_correct
    dtype: bool
  splits:
  - name: train
    num_bytes: 1778954
    num_examples: 319
  download_size: 785830
  dataset_size: 1778954
configs:
- config_name: LLMBar
  data_files:
  - split: train
    path: LLMBar/train-*
---

# PREPAIR Reproduction Results

This dataset contains the reproduction results of the PREPAIR method.
- **Source Project**: PREPAIR
- **Target File**: `results_LLMBar_all_methods.csv`