---
pretty_name: Nemotron-RL-CFBench-v1
license: cc-by-4.0
language:
- en
- ar
- hi
- zh
- ja
- ko
task_categories:
- reinforcement-learning
- text-generation
tags:
- instruction-following
- constraint-following
- rlvr
- nemo-gym
- text
- manually-collected
- synthetic
- Nemotron_3_Ultra
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train.jsonl
size_categories:
- 1K<n<10K
---
**Nemotron-RL-CFBench-v1**

- License: cc-by-4.0
- Language: en, ar, hi, zh, ja, ko
- Task Categories: reinforcement-learning, text-generation
- Tags: instruction-following, constraint-following, rlvr, nemo-gym
- Configs: default train split at data/train.jsonl
- Domain: instruction following, constraint following
- Modality: text
- Capability Breakdown: Constraint following [100%]
- Source: Hybrid: Manually Collected, Synthetic
- Size Bin: <10K
- Associated Model Release: Nemotron Ultra

## Dataset Description:
Nemotron-RL-CFBench-v1 is an RL dataset for instruction-following problems where the focus is on whether an LLM can satisfy explicit constraints. The dataset is manually collected and synthetically augmented, and formatted for the VerifIF Gym environment.

The seed data comes from manually collected instruction-following sources. NVIDIA-Nemotron-3-Nano-30B-A3B-BF16 and Qwen/Qwen3-235B-A22B-Thinking-2507 are used as SDG models, and GPT-5 is used for filtering.

The dataset uses the VerifIF Gym schema with `agent_ref`, `id`, `instructions`, `llm_judge`, and `responses_create_params`. Each record contains one system message and at least one user message in `responses_create_params.input`; many records also include prior assistant messages. The file also contains structured instruction metadata and judge checks that describe the constraints to verify.

This dataset is ready for commercial or non-commercial uses.

## Dataset Owner(s):
NVIDIA Corporation

## Dataset Creation Date:
Created on: 04/28/2026
Last Modified on: 05/21/2026

## Version:
Nemotron-RL-CFBench-v1 <br>

Previous Version(s): N/A

## License/Terms of Use:
This dataset is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

## Intended Usage:
This dataset is intended for:

* Reinforcement learning of LLMs on complex constraint-following prompts.
* Reinforcement learning with verifiable rewards (RLVR) experiments where rewards measure satisfaction of granular instruction criteria.
* Training and evaluating robustness to multiple simultaneous user constraints.
* Studying model behavior on prompts with formatting, keyword, scenario, and other constraint types.
* Building NeMo Gym-compatible constraint-following environments.

## Dataset Characterization

### Dataset Composition and Generation

#### Problem Sources
The dataset is manually collected and synthetically augmented. Tasks are instruction-following problems focused on constraint satisfaction.

#### Curation and Filtering
RL problems are curated and filtered with GPT-5.

#### Dataset Fields
The Ultra-format JSONL file contains the following top-level fields:

* `agent_ref`: Agent metadata for the VerifIF Gym environment. Records use `responses_api_agents/verifif_simple_agent`.
* `id`: Numeric example identifier.
* `instructions`: Structured instruction metadata. Items include fields such as `uid`, `source`, `instruction_id`, `is_misalignment_check`, and task-specific constraint parameters such as keywords.
* `llm_judge`: Judge checks. Items include `uid`, `source`, `content`, and `is_misalignment_check`.
* `responses_create_params`: Responses API-style input payload containing system/user messages with optional assistant history.

**Data Collection Method**<br>
* Hybrid: Manually Collected, Synthetic <br>

**Labeling Method**<br>
* Hybrid: Manually-Labelled, Automated. GPT-5 is used for filtering. <br>

## Dataset Format
Language: English (en), Arabic (ar), Hindi (hi), Chinese (zh), Japanese (ja), Korean (ko)
Modality: Text
Format: JSONL
Structure: VerifIF Gym records with agent metadata, Responses API-style system/user messages with optional assistant history, structured instruction metadata, and LLM-judge checks.

## Dataset Quantification
| Subset | Samples | File Size | Notes |
|--------|---------|-----------|-------|
| train | 1,121 | 25MB | Input length ranges from 2 to 20 messages; instruction checks range from 3 to 16 per record; LLM-judge checks range from 1 to 7 per record |

## Reference(s):
N/A

## Ethical Considerations:
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. Developers should work with their internal developer teams to ensure this dataset meets requirements for the relevant industry and use case and addresses unforeseen product misuse.
Please report quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).