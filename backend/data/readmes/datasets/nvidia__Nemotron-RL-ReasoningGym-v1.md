---
tags:
- rl-environment
- nemo-gym
language:
- en
license:
- cc-by-4.0
task_categories:
- reinforcement-learning
- text-generation
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train.jsonl
---

## Dataset Description:

The Nemotron-RL-ReasoningGym-v1 dataset is designed to improve reasoning capabilities across a broad range of domains, including algebra, arithmetic, computation, cognition, geometry, graph theory, logic, and many common games. It contains 15,000 samples spanning 104 RL environments generated using [Reasoning Gym](https://github.com/open-thought/reasoning-gym), a library of procedural dataset generators and algorithmically verifiable tasks.

This dataset is ready for commercial use.

## Dataset Owner(s):
NVIDIA Corporation

## Dataset Creation Date:
Created on: 01/09/2026
Last Modified on: 01/09/2026

## License/Terms of Use:
This dataset is governed by the Creative Commons Attribution 4.0 International License (CC BY 4.0)

## Intended Usage:
This dataset is intended for:
1. **Robustness**: Diverse, procedurally generated tasks prevent memorization and ensure models develop genuine reasoning skills.
2. **Generalization**: 104 task types across 12 categories ensure broad coverage of reasoning patterns.
3. **Mathematical reasoning**: Arithmetic, algebra, geometry, and probability tasks strengthen quantitative abilities.
4. **Logical reasoning**: Formal logic, constraint satisfaction, and deductive puzzles build structured reasoning.
5. **Algorithmic thinking**: String manipulation, sorting, graph traversal, and matrix operations develop computational reasoning.
6. **Spatial reasoning**: Games, puzzles, ARC tasks, and geometry problems require spatial awareness and planning.

## Dataset Characterization
**Data Collection Method**
* Synthetic (procedurally generated via Reasoning Gym)

**Labeling Method**
* Automated (verifiable solutions generated programmatically)

## Dataset Format
Modality: Text
Format: JSONL
Structure: Each sample contains a question, a verifiable answer, and task-specific metadata for verification.

## Dataset Quantification

| Subset | Samples |
|--------|---------|
| train | 15,000 |

Total Disk Size: ~50MB

## Ethical Considerations:
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal developer teams to ensure this dataset meets requirements for the relevant industry and use case and addresses unforeseen product misuse.
Please report quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/)