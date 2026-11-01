---
license: cc-by-4.0
task_categories:
- text-generation
language:
- ko
tags:
- dialogue
- translation
- korean
- conversational
size_categories:
- n<1K
---

# SODA-KR (Simplified)

Korean translation of the SODA dataset (simplified version with 40722 samples).

## Dataset Description

This is a Korean-translated version of the [allenai/soda](https://huggingface.co/datasets/allenai/soda) dataset.
Each sample contains speakers, narrative context, and dialogue translated to Korean.

## Source Dataset

- **Original Dataset**: [allenai/soda](https://huggingface.co/datasets/allenai/soda)
- **Original License**: CC-BY-4.0
- **Citation**: Please cite the original SODA paper

## Translation Details

- **Translation Model**: moonshotai/kimi-k2-0905
- **Translation Date**: 2025-10-06
- **Translated by**: CaveduckAI
- **Number of Samples**: 40722

## Dataset Structure

```python
{
    "index": int,           # Original dataset index
    "speakers": list[str],  # List of speaker names (max 2)
    "narrative": str,       # Narrative context in Korean
    "dialogue": list[str]   # Dialogue lines in Korean (first line only)
}
```

## License

CC-BY-4.0 (same as original dataset)

## Attribution

This dataset is a derivative work of SODA by Allen Institute for AI, used under CC-BY-4.0.
