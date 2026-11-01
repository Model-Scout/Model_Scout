---
license: cc-by-nc-4.0
language:
- ko
tags:
- roleplay
- character
- sft
- korean
- conversation
size_categories:
- 1K<n<10K
task_categories:
- conversational
- text-generation
---

# Korean Character Roleplay SFT Dataset

Character-based Korean roleplay conversation dataset for fine-tuning language models.

## Dataset Description

This dataset contains high-quality Korean roleplay conversations between users and AI characters. Each conversation follows a specific character's personality, speech patterns, and voice profile.

### Dataset Statistics

| Split | Samples |
|-------|---------|
| Train | 965 |
| Test | 108 |
| **Total** | **1,073** |

### Quality Metrics

- **Overall Grade**: A (0.801)
- **Average Response Length**: 99.8 characters
- **Vocabulary Size**: 7,529 unique tokens
- **TTR (Type-Token Ratio)**: 0.270
- **Characters**: 41 unique characters
- **A-Grade Characters**: 35 (85.4%)

## Dataset Structure

Each sample follows the OpenAI conversation format:

```json
{
  "id": "unique_sample_id",
  "messages": [
    {"role": "user", "content": "User message"},
    {"role": "assistant", "content": "Character response"}
  ],
  "metadata": {
    "character": "character_name",
    "scenario": "scenario_type",
    "boosted": true
  }
}
```

### Fields

| Field | Description |
|-------|-------------|
| `id` | Unique identifier for the sample |
| `messages` | Conversation in OpenAI format |
| `metadata.character` | Character name |
| `metadata.scenario` | Conversation scenario type (optional) |
| `metadata.boosted` | Whether quality-boosted (optional) |

## Usage

```python
from datasets import load_dataset

dataset = load_dataset("your-username/korean-character-roleplay-sft")

# Access train split
train_data = dataset["train"]

# Example usage
for sample in train_data:
    print(f"Character: {sample['metadata']['character']}")
    print(f"User: {sample['messages'][0]['content']}")
    print(f"Assistant: {sample['messages'][1]['content']}")
    break
```

## Characters

Top 10 characters by sample count:

| Character | Samples | Avg Response Length |
|-----------|---------|---------------------|
| 1 | 982 | 108 chars |
| 2 | 965 | 112 chars |
| 3 | 893 | 77 chars |
| 4 | 872 | 130 chars |
| 5 | 815 | 86 chars |

## License

This dataset is released under **CC BY-NC 4.0** (Creative Commons Attribution-NonCommercial 4.0 International).

- You may share and adapt the material
- You must give appropriate credit
- You may not use for commercial purposes

## Citation

```bibtex
@dataset{korean_character_roleplay_sft_2026,
  title={Korean Character Roleplay SFT Dataset},
  year={2026},
  publisher={HuggingFace}
}
```

## Acknowledgments

Generated using the Kaidol LLM Dataset Pipeline with quality filtering and voice profile matching.
