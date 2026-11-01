---
language:
- ko
task_categories:
- text-generation
dataset_info:
  features:
  - name: uuid
    dtype: string
  - name: model
    dtype: string
  - name: gen_input_configs
    struct:
    - name: temperature
      dtype: float64
    - name: top_p
      dtype: float64
    - name: input_generator
      dtype: string
    - name: seed
      dtype: 'null'
    - name: pre_query_template
      dtype: string
  - name: instruction
    dtype: string
  - name: response
    dtype: string
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: task_category
    dtype: string
  - name: other_task_category
    sequence: string
  - name: task_category_generator
    dtype: string
  - name: difficulty
    dtype: string
  - name: intent
    dtype: string
  - name: knowledge
    dtype: string
  - name: difficulty_generator
    dtype: string
  - name: input_quality
    dtype: string
  - name: quality_explanation
    dtype: string
  - name: quality_generator
    dtype: string
  - name: llama_guard_2
    dtype: string
  - name: reward_model
    dtype: string
  - name: instruct_reward
    dtype: float64
  - name: min_neighbor_distance
    dtype: float64
  - name: repeat_count
    dtype: int64
  - name: min_similar_uuid
    dtype: string
  - name: instruction_length
    dtype: int64
  - name: response_length
    dtype: int64
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 1375889972
    num_examples: 189802
  download_size: 667135105
  dataset_size: 1375889972
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
tags:
- instruction
- korean
- magpie
size_categories:
- 100K<n<1M
---

Translated [Magpie-Align/Magpie-Qwen-Air-300K-Filtered](https://huggingface.co/datasets/Magpie-Align/Magpie-Qwen-Air-300K-Filtered) using [nayohan/llama3-instrucTrans-enko-8b](https://huggingface.co/nayohan/llama3-instrucTrans-enko-8b).

For this dataset, we only used data that is 5000 characters or less in length and has language of English.

Thanks for @Magpie-Align and @nayohan.

```
@misc{xu2024magpie,
	title={Magpie: Alignment Data Synthesis from Scratch by Prompting Aligned LLMs with Nothing}, 
	author={Zhangchen Xu and Fengqing Jiang and Luyao Niu and Yuntian Deng and Radha Poovendran and Yejin Choi and Bill Yuchen Lin},
	year={2024},
	eprint={2406.08464},
	archivePrefix={arXiv},
	primaryClass={cs.CL}
}