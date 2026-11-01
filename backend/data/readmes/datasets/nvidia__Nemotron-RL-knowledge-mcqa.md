---
dataset_info:
  features:
  - name: responses_create_params
    struct:
    - name: input
      list:
      - name: content
        dtype: string
      - name: role
        dtype: string
  - name: expected_answer
    dtype: string
  - name: uuid
    dtype: string
  - name: options
    list:
    - name: A
      dtype: string
    - name: B
      dtype: string
    - name: C
      dtype: string
    - name: D
      dtype: string
    - name: E
      dtype: string
    - name: F
      dtype: string
    - name: G
      dtype: string
    - name: H
      dtype: string
    - name: I
      dtype: string
    - name: J
      dtype: string
    - name: K
      dtype: string
    - name: L
      dtype: string
    - name: M
      dtype: string
    - name: 'N'
      dtype: string
    - name: O
      dtype: string
    - name: P
      dtype: string
    - name: Q
      dtype: string
    - name: R
      dtype: string
    - name: S
      dtype: string
    - name: T
      dtype: string
    - name: U
      dtype: string
    - name: V
      dtype: string
    - name: W
      dtype: string
    - name: X
      dtype: string
    - name: 'Y'
      dtype: string
    - name: Z
      dtype: string
  - name: reward_profiles
    list:
    - name: model_hf_path
      dtype: string
    - name: num_generations
      dtype: int64
    - name: pass_rate
      dtype: float64
  - name: template_metadata
    struct:
    - name: format_type
      dtype: string
    - name: output_regex
      dtype: string
    - name: prompt_type
      dtype: string
    - name: template_id
      dtype: string
    - name: template_prompt
      dtype: string
    - name: weight
      dtype: float64
  splits:
  - name: train
    num_bytes: 1809438313
    num_examples: 617020
  - name: validation
    num_bytes: 200924087
    num_examples: 68553
  download_size: 757218926
  dataset_size: 2010362400
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
tags:
- nemo-gym
license: cc-by-4.0
---



## Dataset Description:

The Nemotron-RL-knowledge-mcqa is a multi-domain synthetic multiple-choice question-answering (MCQA) dataset containing knowledge based questions. It combines and refines subsets of the [OpenScienceReasoning-2] (https://huggingface.co/datasets/nvidia/OpenScienceReasoning-2) dataset and other unstructured sources such as books and articles.The dataset was created using [Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B), [Qwen3-235B-A22B-Instruct-2507] (https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507), and [DeepSeek-R1-0528](​​https://huggingface.co/deepseek-ai/DeepSeek-R1-0528).  Each sample consists of a question with multiple answer options and one correct answer. The dataset spans a broad range of domains, including physics, biology, chemistry, mathematics, computer science, engineering, humanities, law, and others.

This dataset is released as part of NVIDIA [NeMo Gym](https://github.com/NVIDIA-NeMo/Gym), a framework for building reinforcement learning environments to train large language models. NeMo Gym contains a growing collection of training environments and datasets to enable Reinforcement Learning from Verifiable Reward (RLVR).

NeMo Gym is an open-source library within the [NVIDIA NeMo framework](https://github.com/NVIDIA-NeMo/), NVIDIA's GPU accelerated, end-to-end training framework for large language models (LLMs), multi-modal models and speech models.

This dataset is part of the [Nemo Gym Collection](https://huggingface.co/collections/nvidia/nemo-gym).

This dataset is ready for commercial use.

## Dataset Owner(s):
NVIDIA Corporation

## Dataset Creation Date:
October 20, 2025

## License/Terms of Use: 
CC BY 4.0 

## Intended Usage:
To be used with [NeMo Gym](https://github.com/NVIDIA-NeMo/Gym) for post-training LLMs. 

## Dataset Characterization
Data Collection Method<br>
* [Synthetic] <br>

Labeling Method<br>
* [Synthetic] <br>

## Dataset Format
Text Only, Compatible with [NeMo Gym](https://github.com/NVIDIA-NeMo/Gym)

## Dataset Quantification
Number of records: 685,573  tuples of (question, answer)
Features per record: 6
Total Data Storage:  757 MB


## Reference(s):
[NeMo Gym](https://github.com/NVIDIA-NeMo/Gym) 

## Ethical Considerations:
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.   
Please report model quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).