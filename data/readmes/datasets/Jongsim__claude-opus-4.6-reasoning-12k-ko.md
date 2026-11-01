---
language:
- ko
license: other
tags:
- reasoning
- chain-of-thought
- distillation
- claude-opus
- math
- logic
- korean
- translation
size_categories:
- 10K<n<100K
task_categories:
- text-generation
pretty_name: Claude Opus 4.6 Reasoning 12K (Korean)
dataset_info:
  features:
    - name: id
      dtype: string
    - name: source
      dtype: string
    - name: messages
      dtype: string
    - name: domain
      dtype: string
    - name: difficulty
      dtype: string
    - name: teacher_model
      dtype: string
    - name: language
      dtype: string
  splits:
    - name: train
      num_examples: 12842
---

# Claude Opus 4.6 Reasoning 12K (Korean) — v1

Korean translation of the [Jongsim/claude-opus-4.6-reasoning-12k](https://huggingface.co/datasets/Jongsim/claude-opus-4.6-reasoning-12k) dataset.

**12,842** reasoning samples with full chain-of-thought traces, translated to Korean.
Both the questions and reasoning steps are translated, making it suitable for training Korean-language reasoning models.

## Dataset Description

This dataset provides Korean translations of Claude Opus 4.6 reasoning samples covering math, logic, science, and code domains.
It is intended for fine-tuning Korean LLMs with step-by-step reasoning capabilities.

## Data Sources

| Source | Count |
|--------|-------|
| [Roman1111111/claude-opus-4.6-10000x](https://huggingface.co/datasets/Roman1111111/claude-opus-4.6-10000x) | 9,633 |
| [nohurry/Opus-4.6-Reasoning-3000x-filtered](https://huggingface.co/datasets/nohurry/Opus-4.6-Reasoning-3000x-filtered) | 2,326 |
| [Jackrong/Qwen3.5-reasoning-700x](https://huggingface.co/datasets/Jackrong/Qwen3.5-reasoning-700x) | 633 |
| [TeichAI/claude-4.5-opus-high-reasoning-250x](https://huggingface.co/datasets/TeichAI/claude-4.5-opus-high-reasoning-250x) | 250 |
| **Total** | **12,842** |

## Dataset Structure

### Fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique sample identifier |
| `source` | string | Original dataset source |
| `messages` | string | JSON array of conversation messages (translated to Korean) |
| `domain` | string | Problem domain |
| `difficulty` | string | Problem difficulty level |
| `teacher_model` | string | Model used to generate the original reasoning |
| `language` | string | Language code (`ko`) |

### Message Format

```json
[
  {"role": "user", "content": "문제 내용 (한국어)"},
  {"role": "assistant", "content": "최종 답변 (한국어)", "reasoning": "단계별 추론 과정 (한국어)"}
]
```

### Domain Distribution

| Domain | Count |
|--------|-------|
| simple logic and math | 7,473 |
| math | 4,447 |
| code | 366 |
| science | 166 |
| instruction_following | 140 |

### Difficulty Distribution

| Difficulty | Count |
|------------|-------|
| medium | 11,827 |
| hard | 61 |
| phd | 71 |

## Versioning

| Version | Description |
|---------|-------------|
| v1 | Initial Korean translation release (12,842 samples) |

## Usage

```python
from datasets import load_dataset
import json

ds = load_dataset("Jongsim/claude-opus-4.6-reasoning-12k-ko")

# Parse messages
sample = ds["train"][0]
messages = json.loads(sample["messages"])
print(messages[0]["content"])  # 문제 (한국어)
print(messages[1]["reasoning"])  # 추론 과정 (한국어)
print(messages[1]["content"])   # 최종 답변 (한국어)
```

## Related Datasets

- 🇺🇸 English original: [Jongsim/claude-opus-4.6-reasoning-12k](https://huggingface.co/datasets/Jongsim/claude-opus-4.6-reasoning-12k)
