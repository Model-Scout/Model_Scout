---
dataset_info:
- config_name: default
  features:
  - name: meeting
    dtype: string
  - name: gt_json
    dtype: string
  - name: topic
    dtype: string
  - name: traps
    list: string
  - name: pass2_f1
    dtype: float64
  splits:
  - name: train
    num_bytes: 5291273
    num_examples: 1115
  - name: test
    num_bytes: 1285948
    num_examples: 273
  download_size: 2825445
  dataset_size: 6577221
- config_name: eval_results
  features:
  - name: model
    dtype: string
  - name: n
    dtype: int64
  - name: parse_rate
    dtype: float64
  - name: schema_compliance
    dtype: float64
  - name: semantics_pass_rate
    dtype: float64
  - name: field_f1_mean
    dtype: float64
  - name: struct_f1_mean
    dtype: float64
  - name: text_f1_mean
    dtype: float64
  splits:
  - name: baseline
    num_bytes: 70
    num_examples: 1
  - name: sft
    num_bytes: 79
    num_examples: 1
  - name: grpo
    num_bytes: 84
    num_examples: 1
  download_size: 12127
  dataset_size: 233
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
- config_name: eval_results
  data_files:
  - split: baseline
    path: eval_results/baseline-*
  - split: sft
    path: eval_results/sft-*
  - split: grpo
    path: eval_results/grpo-*
---
