---
language:
- ko
task_categories:
- text-generation
dataset_info:
  features:
  - name: instruction
    dtype: string
  - name: reasoning
    dtype: string
  - name: output
    dtype: string
  - name: reasoning_chains
    list:
    - name: step
      dtype: int64
    - name: thought
      dtype: string
  splits:
  - name: train
    num_bytes: 126390632
    num_examples: 29857
  download_size: 60009967
  dataset_size: 126390632
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
tags:
- instruction
- korean
- reasoning
license: apache-2.0
---

[SkunkworksAI/reasoning-0.01](https://huggingface.co/datasets/SkunkworksAI/reasoning-0.01) 데이터셋을 [nayohan/llama3-instrucTrans-enko-8b](https://huggingface.co/nayohan/llama3-instrucTrans-enko-8b) 모델을 사용해 번역했습니다.

Thanks for [SkunkworksAI](https://huggingface.co/SkunkworksAI) and [nayohan](https://huggingface.co/nayohan).

---
# 원본

# reasoning-0.01 subset

synthetic dataset of reasoning chains for a wide variety of tasks.
we leverage data like this across multiple reasoning experiments/projects.
stay tuned for reasoning models and more data.


Thanks to Hive Digital Technologies (https://x.com/HIVEDigitalTech) for their compute support in this project and beyond.