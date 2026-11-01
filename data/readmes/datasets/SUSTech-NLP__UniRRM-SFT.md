---
license: apache-2.0
task_categories:
  - text-generation
language:
  - en
  - fr
  - es
  - it
  - de
  - ru
  - tr
  - pt
  - zh
  - pl
  - ar
  - ko
  - ja
  - id
  - vi
  - multilingual
tags:
  - reward-model
  - sft
  - supervised-fine-tuning
  - reasoning
  - multilingual
  - evaluation
pretty_name: "UniRRM-SFT: Supervised Fine-Tuning Data for Unified Reasoning Reward Model"
size_categories:
  - 10K<n<100K
---

# UniRRM-SFT: Supervised Fine-Tuning Data for Unified Reasoning Reward Models

## Overview

**UniRRM-SFT** is the supervised fine-tuning (SFT) dataset used to train UniRRM, a Unified Reasoning Reward Model. It contains **35,749 instruction-response pairs** distilled from an oracle model, designed to initialize the model with structured reasoning and evaluation capabilities across multiple languages and evaluation paradigms.

This dataset is introduced in the following paper, accepted at **ICML 2026** (the 43rd International Conference on Machine Learning):

> **UniRRM: Unified Reasoning Reward Models Across Languages and Evaluation Paradigms** [[Paper]](https://icml.cc/virtual/2026/poster/61930)

## Dataset Construction

The SFT dataset is constructed from [MixReward](https://huggingface.co/datasets/SUSTech-NLP/MixReward) through knowledge distillation:

1. **Oracle Distillation**: An oracle model (GPT-OSS-120B) generates the full evaluation sequence including deep analysis, adaptive rubric generation, and detailed evaluation for each sample in MixReward.
2. **Quality Filtering**: Only samples whose final judgments are correct are retained, ensuring high-quality training signals.
3. **Structured Output**: Each response follows a structured reasoning chain: `[Analysis → Rubric Generation → Evaluation → Scores → Final Judgment]`.

## Reasoning Workflow

The SFT data trains the model to follow a three-stage reasoning pipeline:

- **Deep Analysis (𝒛)**: Identifies task intent, potential risks, core evaluation objectives, and strict constraints from the input.
- **Adaptive Rubric Generation (𝒓)**: Produces both task-generic criteria (broadly applicable to the domain) and instruction-specific criteria (tailored to the unique requirements of the user query), each on a 1–5 scoring scale.
- **Detailed Evaluation (𝒆)**: Applies the generated rubrics to judge candidate responses, producing per-criterion scores and a final judgment.

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| `sft_prompt` | string | The full instruction prompt including system message, user query, and candidate responses to evaluate |
| `sft_response` | string | The structured evaluation response containing reasoning chain, rubric-based scoring, and final judgment |

## Prompt Format

The prompts use the ChatML format (`<\|im_start\|>system ... <\|im_end\|>`) and include:

- A **system message** defining the model as a multilingual evaluation expert
- The **user query** with candidate responses to evaluate
- Instructions for structured output format

## Usage

```python
from datasets import load_dataset

dataset = load_dataset("SUSTech-NLP/UniRRM-SFT")

# Access a sample
sample = dataset["train"][0]
print(sample["sft_prompt"][:500])
print(sample["sft_response"][:500])
```

## Statistics

- **Total samples**: 35,749
- **Format**: Instruction-response pairs (SFT)
- **Source**: Distilled from MixReward using GPT-OSS-120B
- **Quality**: Only correct-judgment samples retained

## Related Datasets

- [**MixReward**](https://huggingface.co/datasets/SUSTech-NLP/MixReward): The source multilingual preference dataset (64,528 samples, 103 languages, 6 domains)
- [**UniRRM-RL**](https://huggingface.co/datasets/SUSTech-NLP/UniRRM-RL): The reinforcement learning dataset for the second training stage

## Training Pipeline

UniRRM uses a two-stage training pipeline:

1. **Stage 1 - SFT** (this dataset): Initializes the model with structured reasoning capabilities by minimizing the negative log-likelihood loss on distilled oracle outputs.
2. **Stage 2 - RL** ([UniRRM-RL](https://huggingface.co/datasets/SUSTech-NLP/UniRRM-RL)): Further optimizes the model using GRPO with a composite reward comprising format reward, outcome consistency reward, and rubric quality reward.

## Citation

```bibtex
@inproceedings{
lai2026unirrm,
title={Uni{RRM}: Unified Reasoning Reward Models Across Languages and Evaluation Paradigms},
author={Peng Lai and Yichao Du and Junchao Wu and Weibo Gao and Linan Yue and Longyue Wang and Weihua Luo and Derek F. Wong and Guanhua Chen},
booktitle={Forty-third International Conference on Machine Learning},
year={2026},
url={https://openreview.net/forum?id=laiK6TlhL2}
}
```

## License

This dataset is released under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).
