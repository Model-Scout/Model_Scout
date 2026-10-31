---
language:
- en
license:
- cc-by-4.0
- apache-2.0
- mit
task_categories:
- reinforcement-learning
- text-generation
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train.jsonl
size_categories:
- 1K<n<10K
tags:
- text
- safety
- reinforcement-learning
- verifiable-rewards
- jailbreak
- robustness
- RLVR
- nemo-gym
- nemotron
---

## Dataset Description:
The Nemotron-RL-Jailbreak-Robustness-v1 data is designed to (1) strengthen model robustness against a variety of adversarial jailbreak techniques and (2) at the same time improve adherence to behavioral policies.

This dataset is a collection of hybrid (open-source and synthetically generated) collection of adversarial prompts designed to elicit undesirable behavior from large language models. That's it, just prompts, responses are generated during training (online reinforcement learning). 

The recommended method to use this dataset is to run reward profiling before starting training, with a rollout size K = 4 or 8, and only keep those prompts where the pass@K is not 1.

This dataset is ready for commercial or non-commercial uses.

### The Seed Prompts:
The starting prompts are obtained the [HarmfulTasks](https://huggingface.co/datasets/notadib/harmful-tasks) and `sdg_jailbreaks` subsets of [Nemotron-SFT-Safety-v1](https://huggingface.co/datasets/nvidia/Nemotron-SFT-Safety-v1).

### The Challenging Data Generator: 
Starting with the seed prompts, and using Nemotron 3 Super as a target model, we use the PAIR attack pipeline with Qwen3-30B as the attack model. Some design choices used here are that the attack model maintains multi-turn context. That is, it's trying to evolve its attack knowing what it previously tried, and what the target model's response was. The target model on the other hand sees every attempt with the context flushed, so it has no memory of what the attacker model has tried before or that it is in this multi-turn simulation with another adversarial agent. The attack loop breaks when either the attack succeeds (the target model produces an undersirable response) or the attacker hits max retries.

### Response Policies:
Each prompt is tagged with a response policy, which sheds light on what an approprioate response policy to the user request in the prompt should be, regardless of which jailbreak technique the prompt was wrapped up in.

### Online Reinforcement Learning:
This dataset is intended to be used alongside the [Jailbreak RLVR Environment in NeMo Gym](https://github.com/NVIDIA-NeMo/Gym/tree/main/resources_servers/jailbreak_detection). As part of its RLVR reward design, this environment includes a different subset of response verifiers based on which response policy was tagged against a prompt. 

**Important Note:** The `agent_ref` key inside each data sample handles the set of reward verifiers that are used to judge and assign rewards to each rollout. Therefore, it is very important to use this dataset alongside its corresponding implementation in NeMo Gym.  

## Dataset Owner(s):
NVIDIA Corporation

## Dataset Creation Date:
Created on: 4/15/2026
Last Modified on: 4/15/2026

## License/Terms of Use: 
This dataset is governed by the Creative Commons Attribution 4.0 International License (CC BY 4.0).  
Additional Information: Apache 2.0 License; MIT License.

## Intended Usage:
This dataset is intended to be used alongside the [Jailbreak RLVR Environment in NeMo Gym](https://github.com/NVIDIA-NeMo/Gym/tree/main/resources_servers/jailbreak_detection) by the community as part of their model's online reinforcement learning (RL) recipe to improve model robustness to various types of jailbreak techniques, including:
- DAN (Do Anything Now) prompts
- Educational/research bypass attempts
- Roleplay/persona attacks
- Grandma exploit
- Security training bypass
- Developer mode claims
- Fiction/creative writing bypass
- Completion attacks
- Code generation requests
- Hypothetical/thought experiment bypass
- Encoding attacks

Previous Version: None.

Relationship to Previous Version(s): None.

## Dataset Characterization
**Data Collection Method**  
* Hybrid: Human, Synthetic, Automated

**Labeling Method**
* Hybrid: Human, Synthetic, Automated

## Dataset Format
Modality: Text  
Format: JSONL  
Structure: Text + Metadata

## Dataset Quantification
Note: We source only the prompts from the following underlying datasets.  

Any responses that may already exist in an underlying open-source dataset are discarded and regenerated using the response generation techniques described in the [Dataset Description section](#dataset-description).

Total Samples: 5,611
Total Disk Size: ~8 MB.

---

## Ethical Considerations:
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. Developers should work with their internal developer teams to ensure this dataset meets requirements for the relevant industry and use case and addresses unforeseen product misuse.
Please report quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/)
