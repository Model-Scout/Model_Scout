---
language:
- ko
license: apache-2.0
task_categories:
- text-generation
- question-answering
pretty_name: KITE (Korean Instruction-following Task Evaluation)
size_categories:
- n<1K
tags:
- instruction-following
- korean
- evaluation
- benchmark
- llm
configs:
- config_name: culturally_aware_all
  data_files:
  - split: test
    path: culturally_aware_all/test-*
- config_name: culturally_aware_acrostic
  data_files:
  - split: test
    path: culturally_aware_acrostic/test-*
- config_name: culturally_aware_honorifics
  data_files:
  - split: test
    path: culturally_aware_honorifics/test-*
- config_name: culturally_aware_numbers
  data_files:
  - split: test
    path: culturally_aware_numbers/test-*
- config_name: culturally_aware_postposition
  data_files:
  - split: test
    path: culturally_aware_postposition/test-*
- config_name: translated_and_filtered
  data_files:
  - split: test
    path: translated_and_filtered/test-*
---

# KITE: Korean Instruction-following Task Evaluation

[![arXiv](https://img.shields.io/badge/arXiv-2510.15558-b31b1b.svg)](https://arxiv.org/abs/2510.15558)
[![GitHub](https://img.shields.io/badge/GitHub-KITE-blue?logo=github)](https://github.com/junkim100/KITE)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

## Dataset Description

**KITE (Korean Instruction-following Task Evaluation)** is the first comprehensive benchmark specifically designed to evaluate the Korean instruction-following capabilities of Large Language Models (LLMs). Unlike existing Korean benchmarks that focus mainly on factual knowledge or multiple-choice testing, KITE directly targets diverse, open-ended instruction-following tasks.

### Dataset Summary

KITE consists of two main components:

1. **KITE General (427 instructions)**: Universally applicable tasks translated and filtered from Google's IFEval dataset
2. **KITE Korean (100 instructions)**: Korean-specific linguistic tasks created from scratch

All instructions are verifiable through rule-based evaluation, ensuring objective and measurable outcomes.

### Supported Tasks

- **Instruction Following Evaluation**: Assess LLMs' ability to follow explicit instructions in Korean
- **Korean Linguistic Phenomena**: Evaluate understanding of Korean-specific features (honorifics, number systems, etc.)
- **Cultural Awareness**: Test models on culturally-embedded Korean tasks

### Languages

- Korean (ko)

## Dataset Structure

### Data Instances

Each instance contains:

```json
{
  "instruction": "이행시는 주어진 두 글자 단어의 각 글자로 시작하는 일관성 있는 짧막한 이야기를 의미합니다. '자유'로 이행시를 지으세요...",
  "instruction_id_list": ["Korean:acrostic_poem", "keywords:frequency"],
  "kwargs": [
    {"target_word": "자유"},
    {"relation": "최소", "keyword": "평화", "frequency": 1}
  ],
  "key": null,
  "source_kwargs": null,
  "source_prompt": null
}
```

### Data Fields

- `instruction` (string): The Korean instruction text
- `instruction_id_list` (list of strings): List of instruction types/categories for verification
- `kwargs` (list of dicts): Parameters needed for rule-based verification
- `key` (int, optional): Original IFEval key (only for translated_and_filtered subset)
- `source_kwargs` (list, optional): Original English kwargs (only for translated_and_filtered subset)
- `source_prompt` (string, optional): Original English instruction (only for translated_and_filtered subset)

### Data Splits

All subsets use the **test** split only (no train/validation splits).

| Subset | Split | Examples | Description |
|--------|-------|----------|-------------|
| `culturally_aware_all` | test | 100 | All Korean-specific instructions combined |
| `culturally_aware_acrostic` | test | 25 | Acrostic poem (삼행시) instructions |
| `culturally_aware_honorifics` | test | 25 | Honorifics (존댓말/반말) instructions |
| `culturally_aware_numbers` | test | 25 | Native/Sino Korean number system instructions |
| `culturally_aware_postposition` | test | 25 | Post-position drop (조사 생략) instructions |
| `translated_and_filtered` | test | 427 | KITE General - translated from IFEval |

## Dataset Creation

### KITE General (translated_and_filtered)

1. **Automated Translation**: GPT-4o translated the original IFEval dataset
2. **Manual Verification**: Native Korean speakers reviewed all translations
3. **Contextual Filtering**: Removed English-centric instructions (e.g., capitalization rules)
4. **Expert Review**: Five native Korean speakers with NLP knowledge validated the dataset

Out of 541 original IFEval instructions, 114 were filtered as culturally/linguistically irrelevant, resulting in 427 high-quality Korean instructions.

### KITE Korean (culturally_aware_*)

Created from scratch to evaluate Korean-specific linguistic phenomena:

- **Acrostic Poem (삼행시)**: Generate poetry where each line starts with a specific letter
- **Post-position Drop (조사 생략)**: Form sentences without Korean grammatical markers
- **Honorifics (존댓말/반말)**: Switch between honorific and informal speech
- **Native/Sino Korean Numbers (순한국어/한자어 숫자)**: Convert between number systems

Each category contains 25 carefully crafted instructions.

### Curation Rationale

Korean presents unique challenges for LLMs:
- **Agglutinative Structure**: Complex word formation through affixes
- **Honorific System**: Multiple levels of formality
- **Dual Number Systems**: Native Korean and Sino-Korean numbers
- **Post-positions**: Grammatical markers that change based on context

KITE addresses these challenges by providing targeted evaluation tasks.

## Usage

### Loading the Dataset

```python
from datasets import load_dataset

# Load all subsets
dataset = load_dataset("junkim100/KITE")

# Load specific subset
kite_korean = load_dataset("junkim100/KITE", "culturally_aware_all")
kite_general = load_dataset("junkim100/KITE", "translated_and_filtered")

# Load specific category
acrostic = load_dataset("junkim100/KITE", "culturally_aware_acrostic")

# Access test split
test_data = kite_korean["test"]
print(f"Number of examples: {len(test_data)}")
print(f"First example: {test_data[0]}")
```

### Evaluation

For evaluation code and detailed instructions, see the [GitHub repository](https://github.com/junkim100/KITE).

```bash
# Clone the repository
git clone https://github.com/junkim100/KITE.git
cd KITE

# Install dependencies
conda env create -f kite.yml
conda activate kite

# Run evaluation
bash run.sh
```

## Benchmark Results

Performance of various LLMs on KITE (Strict Accuracy %):

| Model | KITE General | KITE Korean | Acrostic | Honorifics | Numbers | Postposition |
|-------|--------------|-------------|----------|------------|---------|--------------|
| GPT-4o | **71.4** | **64.0** | **72.0** | **68.0** | **60.0** | **56.0** |
| GPT-3.5-turbo | 50.8 | 38.0 | 44.0 | 40.0 | 32.0 | 36.0 |
| SOLAR-10.7B | 45.2 | 28.0 | 24.0 | 32.0 | 28.0 | 28.0 |
| EEVE-10.8B | 42.6 | 26.0 | 20.0 | 28.0 | 24.0 | 32.0 |

*Note: Results may vary based on evaluation settings and model versions.*

## Citation

If you use KITE in your research, please cite:

```bibtex
@misc{kim2025kitebenchmarkevaluatingkorean,
      title={KITE: A Benchmark for Evaluating Korean Instruction-Following Abilities in Large Language Models}, 
      author={Dongjun Kim and Chanhee Park and Chanjun Park and Heuiseok Lim},
      year={2025},
      eprint={2510.15558},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2510.15558}, 
}
```

## License

This dataset is licensed under the Apache License 2.0. See [LICENSE](https://github.com/junkim100/KITE/blob/master/LICENSE) for details.

## Acknowledgments

KITE is inspired by Google's IFEval benchmark. We thank the original authors for their foundational work on instruction-following evaluation.

