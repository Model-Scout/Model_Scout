---
license: mit
task_categories:
  - text-generation
  - question-answering
language:
  - en
tags:
  - claude
  - distillation
  - reasoning
  - instruction-tuning
  - sft
size_categories:
  - 100K<n<1M
---

# Claude-Distills

A curated collection of open-source Claude distillation datasets, unified and deduplicated.

> **Note**: This repo only provides unified formatting, deduplication, and documentation. **All credits go to the original data creators. I did NOT create any of the original data.**

## Data Sources

| Source | Samples | Description |
|--------|--------:|-------------|
| [claude-sonnet-4.6-120000x](https://huggingface.co/datasets/Roman1111111/claude-sonnet-4.6-120000x) | 119,446 | Claude Sonnet 4.6 general, code, math, psychology data |
| [claude-opus-4.6-10000x](https://huggingface.co/datasets/Roman1111111/claude-opus-4.6-10000x) | 9,633 | Claude Opus 4.6 multi-task data |
| [claude-opus-4.6-high-reasoning-700x](https://huggingface.co/datasets/dalisoft/claude-opus-4.6-high-reasoning-700x) | 758 | High-quality reasoning data |
| [Claude-Opus-4.6-Reasoning-887x](https://huggingface.co/datasets/TeichAI/Claude-Opus-4.6-Reasoning-887x) | 887 | Reasoning task data |
| [Claude-Opus-4.6-Reasoning-500x](https://huggingface.co/datasets/Hastagaras/Claude-Sonnet-X-Opus-4.6-Reasoning-small-500) | 500 | Reasoning task data |
| [Claude-Sonnet-X-Opus-4.6-Reasoning-small-500](https://huggingface.co/datasets/Hastagaras/Claude-Sonnet-X-Opus-4.6-Reasoning-small-500) | 524 | Sonnet & Opus mixed data |
| [claude-4.5-opus-high-reasoning-250x](https://huggingface.co/datasets/TeichAI/claude-4.5-opus-high-reasoning-250x) | 250 | Claude 4.5 Opus reasoning data |
| [claude-opus-4.6-4.7-reasoning-8.7k](https://huggingface.co/datasets/angrygiraffe/claude-opus-4.6-4.7-reasoning-8.7k) | 8,706 | Claude Opus 4.6/4.7 multi-category reasoning data |
| **Total (after dedup)** | **140,504** | |

## What This Repo Does

1. **Unified formatting**: Converted all data sources to a consistent `messages` format with `source` field
2. **Deduplication**: Removed 3,098 duplicate samples by user prompt content
3. **Documentation**: Added data statistics, source attribution, and usage instructions

## Data Format

```json
{
  "messages": [
    {"role": "system", "content": "You are a helpful AI assistant."},
    {"role": "user", "content": "Question content"},
    {"role": "assistant", "content": "thinking process and answer"}
  ],
  "source": "claude-sonnet-4.6-120000x"
}
```

### Thinking Process Format

Assistant responses include thinking process using special tokens to mark the thinking section, followed by the final answer.

## Statistics

| Metric | Value |
|--------|-------|
| Total samples | 140,504 |
| From Sonnet 4.6 | 119,446 (85.0%) |
| From Opus datasets | 12,354 (8.8%) |
| From Opus 4.6/4.7 Reasoning | 8,704 (6.2%) |
| Duplicates removed | 3,100 |

## Usage

```python
from datasets import load_dataset

dataset = load_dataset("Kassadin88/Claude-Distillation-Dataset")
```

## License

This dataset is for research and educational purposes only. **Please follow the terms of use of the original data sources.**

## Citation

If you use this dataset, please cite:

```bibtex
@misc{claude-distills,
  title={Claude-Distills: A Curated Collection of Open-Source Claude Distillation Datasets},
  author={Kassadin88},
  year={2026},
  publisher={HuggingFace},
  url={https://huggingface.co/datasets/Kassadin88/Claude-Distillation-Dataset}
}
```

And the original sources:

```bibtex
@misc{claude-sonnet-4.6-120000x,
  title={claude-sonnet-4.6-120000x},
  author={Roman1111111},
  year={2026},
  publisher={HuggingFace},
  url={https://huggingface.co/datasets/Roman1111111/claude-sonnet-4.6-120000x}
}

@misc{claude-opus-4.6-10000x,
  title={claude-opus-4.6-10000x},
  author={Roman1111111},
  year={2026},
  publisher={HuggingFace},
  url={https://huggingface.co/datasets/Roman1111111/claude-opus-4.6-10000x}
}

@misc{claude-opus-4.6-high-reasoning-700x,
  title={claude-opus-4.6-high-reasoning-700x},
  author={dalisoft},
  year={2026},
  publisher={HuggingFace},
  url={https://huggingface.co/datasets/dalisoft/claude-opus-4.6-high-reasoning-700x}
}

@misc{claude-opus-4.6-reasoning-887x,
  title={Claude-Opus-4.6-Reasoning-887x},
  author={TeichAI},
  year={2026},
  publisher={HuggingFace},
  url={https://huggingface.co/datasets/TeichAI/Claude-Opus-4.6-Reasoning-887x}
}

@misc{claude-sonnet-x-opus-4.6-reasoning-small-500,
  title={Claude-Sonnet-X-Opus-4.6-Reasoning-small-500},
  author={Hastagaras},
  year={2026},
  publisher={HuggingFace},
  url={https://huggingface.co/datasets/Hastagaras/Claude-Sonnet-X-Opus-4.6-Reasoning-small-500}
}

@misc{claude-4.5-opus-high-reasoning-250x,
  title={claude-4.5-opus-high-reasoning-250x},
  author={TeichAI},
  year={2026},
  publisher={HuggingFace},
  url={https://huggingface.co/datasets/TeichAI/claude-4.5-opus-high-reasoning-250x}
}

@misc{claude-opus-4.6-4.7-reasoning-8.7k,
  title={claude-opus-4.6-4.7-reasoning-8.7k},
  author={angrygiraffe},
  year={2026},
  publisher={HuggingFace},
  url={https://huggingface.co/datasets/angrygiraffe/claude-opus-4.6-4.7-reasoning-8.7k}
}
```

## Acknowledgments

Thanks to all original data creators and providers. This is just a curated collection of their work.
