---
license: cc-by-4.0
language:
  - zh
  - ja
  - ko
  - vi
task_categories:
  - question-answering
  - text-classification
size_categories:
  - 100K<n<1M
dataset_info:
  features:
    - name: id
      dtype: string
    - name: prompt
      dtype: string
    - name: linguistic_data
      dtype: string
    - name: expected_explanation
      dtype: string
    - name: linguistic_phenomena
      dtype: string
    - name: category
      dtype: string
    - name: language
      dtype: string
    - name: task_type
      dtype: string
  splits:
    - name: train
      num_bytes: 1500000
      num_examples: 297
  download_size: 500000
  dataset_size: 1500000
---

# Sino-Xenic Reasoning Gap Dataset

A comprehensive evaluation dataset for testing Large Language Models' understanding of Sino-Xenic linguistic phenomena across Chinese, Japanese, Korean, and Vietnamese.

## Dataset Overview

- **Total Samples**: 297
- **Languages**: Chinese, Japanese, Korean, Vietnamese
- **Categories**: 11
- **Task Types**: Surface-level and Deep Structural

## Categories

1. **Chinese Idioms** (27 samples) - Understanding Chinese idioms and their cultural meanings
2. **Chinese Characters** (27 samples) - Recognizing and understanding Chinese characters
3. **Chinese Segmentation** (27 samples) - Morphological segmentation of Chinese words
4. **Japanese Kanji** (27 samples) - Understanding Japanese kanji characters
5. **Japanese Compounds** (27 samples) - Analyzing Japanese compound words
6. **Korean Sino Words** (27 samples) - Sino-Korean vocabulary and etymology
7. **Korean Etymology** (27 samples) - Etymology of Korean words
8. **Vietnamese Sino Words** (27 samples) - Sino-Vietnamese vocabulary
9. **Vietnamese Etymology** (27 samples) - Etymology of Vietnamese words
10. **Multilingual Semantics** (27 samples) - Cross-lingual semantic comparison
11. **Cross-Lingual Cognates** (27 samples) - Identifying cognates across languages

## Data Format

Each sample contains:
- `id`: Unique identifier
- `prompt`: The question or task
- `linguistic_data`: The linguistic element being analyzed
- `expected_explanation`: The expected reasoning and answer
- `linguistic_phenomena`: Tags indicating the type of linguistic phenomenon (pipe-separated)
- `category`: The category this sample belongs to
- `language`: The primary language(s) involved
- `task_type`: Either "surface-level" or "deep_structural"

## Usage

### Load with Hugging Face Datasets

```python
from datasets import load_dataset

dataset = load_dataset('nguyenthanhasia/sino-xenic-reasoning-gap-dataset')
print(dataset)
```

### Load from CSV

```python
import pandas as pd

df = pd.read_csv('data.csv')
print(df.head())
```

## Dataset Statistics

- **Total Samples**: 297
- **Average Prompt Length**: ~100 characters
- **Average Explanation Length**: ~300 characters
- **Languages Covered**: 4 (Chinese, Japanese, Korean, Vietnamese)

## Quality Assurance

This dataset has been thoroughly validated for:
- ✓ Complete metadata
- ✓ Proper sample structure
- ✓ Balanced distribution across categories
- ✓ UTF-8 encoding compliance
- ✓ Unique sample IDs
- ✓ Non-empty required fields

**Quality Check Result**: 0 Errors, 0 Critical Warnings

## Citation

If you use this dataset, please cite the original paper:
```
@article{sino-xenic-reasoning-gap,
  title={The Sino-Xenic Reasoning Gap in LLMs},
  year={2025}
}
```

## License

This dataset is licensed under the Creative Commons Attribution 4.0 International License (CC-BY-4.0).
