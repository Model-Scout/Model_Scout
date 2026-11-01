---
language:
- ko
task_categories:
- text-generation
dataset_info:
  features:
  - name: uuid
    dtype: string
  - name: instruction
    dtype: string
  - name: gen_input_configs
    struct:
    - name: temperature
      dtype: float64
    - name: top_p
      dtype: float64
  - name: response_8b_instruct
    dtype: string
  - name: response_8b_instruct_reward
    dtype: float64
  - name: response_8b_instruct_generator
    dtype: string
  - name: response_8b_base
    dtype: string
  - name: response_8b_base_reward
    dtype: float64
  - name: response_8b_base_generator
    dtype: string
  - name: response_70b_instruct
    dtype: string
  - name: response_70b_instruct_reward
    dtype: float64
  - name: response_70b_instruct_generator
    dtype: string
  - name: response_405b_instruct
    dtype: string
  - name: response_405b_instruct_reward
    dtype: float64
  - name: response_405b_instruct_generator
    dtype: string
  - name: reward_model
    dtype: string
  - name: intent
    dtype: string
  - name: knowledge
    dtype: string
  - name: difficulty
    dtype: string
  - name: input_quality
    dtype: string
  - name: quality_explanation
    dtype: string
  - name: task_category
    dtype: string
  - name: llama_guard_2
    dtype: string
  - name: input_length
    dtype: int64
  - name: output_length
    dtype: int64
  - name: chosen
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: rejected
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: all_rm_scores
    sequence: float64
  splits:
  - name: train
    num_bytes: 1415464108
    num_examples: 80884
  download_size: 694975271
  dataset_size: 1415464108
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
tags:
- instruction
- korean
- magpie
---

[Magpie-Align/Magpie-DPO-100K-SML](https://huggingface.co/datasets/Magpie-Align/Magpie-DPO-100K-SML) 데이터셋을 [nayohan/llama3-instrucTrans-enko-8b](https://huggingface.co/nayohan/llama3-instrucTrans-enko-8b) 모델을 사용해 번역했습니다.

Thanks for [Magpie-Align](https://huggingface.co/Magpie-Align) and [nayohan](https://huggingface.co/nayohan).

---

This dataset is still under internal assessment. Please use it with caution!

To create this dataset, we first generate responses from the base model using URIAL as rejected. Then, we generate responses from 8B, 70B, and 405B models, and take the instruction-response pair with the highest reward as chosen.

### Other Magpie DPO Datasets
We observed that the following DPO datasets may have better performance after we burned a lot of GPU hours :)

|Model Name | Dataset | Type | Description |
|-------------|:-------|:-------|:-------|
| [Llama 3 8B Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) | [Magpie-Air-DPO-100K](https://huggingface.co/datasets/Magpie-Align/Magpie-Air-DPO-100K-v0.1) | DPO | DPO dataset via Best-of-N sampling and rewards.
| [Llama 3 70B Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-70B-Instruct) | [Magpie-Pro-DPO-100K](https://huggingface.co/datasets/Magpie-Align/Magpie-Pro-DPO-100K-v0.1) | DPO | DPO dataset via Best-of-N sampling and rewards.
| [Llama 3.1 70B Instruct](https://huggingface.co/meta-llama/Meta-Llama-3.1-70B-Instruct) | [Magpie-Llama-3.1-Pro-DPO-100K](https://huggingface.co/datasets/Magpie-Align/Magpie-Llama-3.1-Pro-DPO-100K-v0.1) | DPO | DPO dataset via Best-of-N sampling and rewards.