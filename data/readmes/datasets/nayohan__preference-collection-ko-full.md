---
dataset_info:
  features:
  - name: orig_criteria
    dtype: string
  - name: orig_feedback_A
    dtype: string
  - name: orig_feedback_B
    dtype: string
  - name: orig_instruction
    dtype: string
  - name: orig_reference_answer
    dtype: string
  - name: orig_response_A
    dtype: string
  - name: orig_response_B
    dtype: string
  - name: output
    dtype: string
  - name: orig_feedback
    dtype: string
  - name: input
    dtype: string
  - name: instruction
    dtype: string
  - name: orig_score_A
    dtype: string
  - name: orig_score_B
    dtype: string
  - name: orig_preference
    dtype: string
  splits:
  - name: train
    num_bytes: 3227593965
    num_examples: 199760
  download_size: 777723605
  dataset_size: 3227593965
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

Translate [prometheus-eval/Preference-Collection](https://huggingface.co/datasets/prometheus-eval/Preference-Collection) using [nayohan/llama3-instrucTrans-enko-8b](https://huggingface.co/nayohan/llama3-instrucTrans-enko-8b).