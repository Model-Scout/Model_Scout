---
language:
- en
- ko
task_categories:
- text-classification
tags:
- safety
- adversarial
- benchmark
- multilingual
- cultural-adaptation
- national-security
license: cc-by-4.0
pretty_name: ROK-FORTRESS Public Benchmark
size_categories:
- n<1K
dataset_info:
  features:
  - name: TASK_ID
    dtype: int64
  - name: Phase
    dtype: string
  - name: Tactic
    dtype: string
  - name: Task Type
    dtype: string
  - name: Adversarial Prompt
    dtype: string
  - name: Risk Domain
    dtype: string
  - name: Risk Sub-Domain
    dtype: string
  - name: Benign Prompt
    dtype: string
  - name: Simplified Direct Request Variant
    dtype: string
  - name: Rubric
    dtype: string
  - name: Harm Dimensions
    dtype: string
  - name: "[KR] Translated - Adversarial Prompt"
    dtype: string
  - name: "[KR] Translated - Benign Prompt"
    dtype: string
  - name: "[KR] Translated - Simplified Direct Request Variant"
    dtype: string
  - name: "[KR] Translated - Rubric"
    dtype: string
  - name: "[EN] Cultural Adapted - Adversarial Prompt"
    dtype: string
  - name: "[EN] Cultural Adapted - Benign Prompt"
    dtype: string
  - name: "[EN] Cultural Adapted - Simplified Direct Request Variant"
    dtype: string
  - name: "[EN] Cultural Adapted - Rubric"
    dtype: string
  - name: "[KR] Transcreated - Adversarial Prompt"
    dtype: string
  - name: "[KR] Transcreated - Benign Prompt"
    dtype: string
  - name: "[KR] Transcreated - Simplified Direct Request Variant"
    dtype: string
  - name: "[KR] Transcreated - Rubric"
    dtype: string
  splits:
  - name: train
    num_examples: 791
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  default: true
---

# ROK-FORTRESS: Public Dataset

## Overview

ROK-FORTRESS is a culturally adversarial safety benchmark for large language models (LLMs) targeting National Security and Public Safety (NSPS) risks. It evaluates how language (English vs. Korean) and geopolitical grounding (U.S. vs. Korean context) jointly shape model safety behavior under adversarial prompting.

This repository contains the **public subset** of the ROK-FORTRESS benchmark: **791 of 1,235 tasks** (64%). A private holdout (36%) is retained to preserve benchmark integrity and prevent training contamination. The public subset maintains full distributional diversity across all risk domains, subdomains, phases, tactics, and task types.

## Public/Private Split Rationale

This release contains 791 of 1,235 tasks (64%). The remaining 444 tasks (36%) are withheld as a private holdout. Tasks were designated private based on expert red-teamer assessment of harm potential — prompts judged to pose greater risk of real-world misuse if publicly disseminated are restricted.

The public subset preserves full distributional diversity across all risk domains, subdomains, phases, adversarial tactics, and task types, and is sufficient to replicate the core analyses reported in the paper. The private holdout additionally serves to prevent benchmark contamination and training data leakage.

## Dataset Format

The dataset is provided in Parquet format (`data/train-00000-of-00001.parquet`). A TSV version (`rok_fortress_public.tsv`) is also included for convenience. Each row represents one task.

### Metadata Columns

| Column | Description |
| :---- | :---- |
| `TASK_ID` | Unique task identifier (non-contiguous due to private holdout removal) |
| `Phase` | Construction phase: `1` (adapted from FORTRESS) or `2` (newly authored) |
| `Tactic` | Adversarial red-teaming tactic(s) used in the prompt |
| `Task Type` | `Culture Agnostic` (no locale-specific references) or `Culture Specific` (references specific entities/institutions) |
| `Risk Domain` | One of four NSPS domains: CBRNE, Political Violence & Terrorism, Criminal & Financial Illicit Activities, Information Leakage |
| `Risk Sub-Domain` | Finer-grained risk category within each domain |

### Prompt & Rubric Columns

Each task contains up to four transcreation variants, depending on task type.

**All tasks (Culture Agnostic and Culture Specific):**

| Column | Variant | Description |
| :---- | :---- | :---- |
| `Adversarial Prompt` | V(En) or V(En,US) | Original English adversarial prompt |
| `Benign Prompt` | — | Paired benign prompt with similar keywords but innocent intent |
| `Simplified Direct Request Variant` | — | Stripped-down version without adversarial obfuscation |
| `Rubric` | — | Binary rubric items for evaluating response harmfulness |
| `Harm Dimensions` | — | Per-rubric-item harm dimension labels (comma-separated, aligned 1:1 with `Rubric` items). See Rubric Structure below for dimension definitions. |
| `[KR] Translated - Adversarial Prompt` | V(Ko) or V(Ko,US) | Korean translation of adversarial prompt |
| `[KR] Translated - Benign Prompt` | — | Korean translation of benign prompt |
| `[KR] Translated - Simplified Direct Request Variant` | — | Korean translation of direct request |
| `[KR] Translated - Rubric` | — | Korean translation of rubric |

**Culture Specific tasks only** (empty for Culture Agnostic):

| Column | Variant | Description |
| :---- | :---- | :---- |
| `[EN] Cultural Adapted - Adversarial Prompt` | V(En,KR) | English with Korean cultural adaptation |
| `[EN] Cultural Adapted - Benign Prompt` | — | Culturally adapted benign prompt |
| `[EN] Cultural Adapted - Simplified Direct Request Variant` | — | Culturally adapted direct request |
| `[EN] Cultural Adapted - Rubric` | — | Culturally adapted rubric |
| `[KR] Transcreated - Adversarial Prompt` | V(Ko,KR) | Full Korean transcreation |
| `[KR] Transcreated - Benign Prompt` | — | Transcreated benign prompt |
| `[KR] Transcreated - Simplified Direct Request Variant` | — | Transcreated direct request |
| `[KR] Transcreated - Rubric` | — | Transcreated rubric |

### Transcreation Matrix

The benchmark systematically varies language and cultural grounding:

|  | U.S. Context | Korean Context |
| :---- | :---- | :---- |
| **English** | V(En,US) — original | V(En,KR) — cultural adaptation |
| **Korean** | V(Ko,US) — translation | V(Ko,KR) — full transcreation |

- **Culture Agnostic** tasks (N=359): 2 variants — V(En) and V(Ko)  
- **Culture Specific** tasks (N=432): 4 variants — V(En,US), V(Ko,US), V(En,KR), V(Ko,KR)

This yields **1,519 effective task-variant pairs** in the public subset.

## Dataset Composition

### By Risk Domain

| Risk Domain | Culture Agnostic | Culture Specific | Total |
| :---- | :---- | :---- | :---- |
| CBRNE | 138 | 113 | 251 |
| Criminal & Financial | 115 | 133 | 248 |
| Political Violence & Terrorism | 76 | 133 | 209 |
| Information Leakage | 30 | 53 | 83 |
| **Total** | **359** | **432** | **791** |

### By Phase

| Phase | Culture Agnostic | Culture Specific | Total |
| :---- | :---- | :---- | :---- |
| Phase 1 | 223 | 227 | 450 |
| Phase 2 | 136 | 205 | 341 |
| **Total** | **359** | **432** | **791** |

## Rubric Structure

Each task includes 1–7 binary (Yes/No) rubric items that operationalize harm measurement. Rubric items map to seven harm dimensions:

| Dimension | Description |
| :---- | :---- |
| **(WHAT)** Specificity | Identification of concrete harmful entities |
| **(HOW-1)** Acquisition | How to obtain harmful materials or access |
| **(HOW-2)** Weaponization | Transforming materials into harmful tools |
| **(HOW-3)** Delivery | Methods for deploying harmful elements |
| **(WHY)** Vulnerability Exploitation | Exploiting system or human weaknesses |
| **(WHO/WHERE)** Targeting Guidance | Identifying targets that maximize harm |
| **(WHEN)** Operational Windows | Time-sensitive exploitable disclosures |

Each dimension is assigned domain-specific risk tiers (Tier 1–3) for tier-weighted scoring. See the paper for full definitions.

## Usage Notes

- **Task IDs are non-contiguous** due to private holdout removal. This is expected and does not affect usage.  
- **Rubric items** are separated by commas within the rubric column. Each item is a standalone binary question.  
- **Cultural adaptation columns** are empty for Culture Agnostic tasks by design.  
- **Evaluation**: We recommend 3-judge majority voting with diverse model families. See the paper for our calibrated panel selection methodology.

## Content Warning

This dataset contains adversarial prompts designed to elicit harmful content across NSPS domains including CBRNE threats, terrorism, criminal activity, and information leakage. The content is intended solely for safety evaluation research.


## Loading the Dataset

```python
from datasets import load_dataset

dataset = load_dataset("ScaleAI/ROK-FORTRESS_public")
```

## Citation

```bibtex
@misc{rokfortress2026,
      title={ROK-FORTRESS: Measuring the Effect of Geopolitical Transcreation for National Security and Public Safety}, 
      author={Michael S. Lee and Yash Maurya and Drew Rein and Bert Herring and Jonathan Nguyen and Kyungho Song and Udari Madhushani Sehwag and Jiyeon Cho and Kaustubh Deshpande and Yeongkyun Jang and Jiyeon Joo and Minn Seok Choi and Evi Fuelle and Christina Q Knight and Joseph Brandifino and Max Fenkell},
      year={2026},
      eprint={2605.14152},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2605.14152}, 
}
```

## License

This dataset is released under the [CC-BY-4.0 License](https://creativecommons.org/licenses/by/4.0/).