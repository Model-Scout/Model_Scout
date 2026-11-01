---
license: unknown
task_categories:
- question-answering
language:
- ko
tags:
- math
- korean
size_categories:
- n<1K
---

# ko-math-500-test

## Dataset Description

This dataset is derived from the original [davidkim205/ko-math-500](https://huggingface.co/datasets/davidkim205/ko-math-500) dataset.

### Changes Made

- **Split modification**: The original 'train' split has been changed to 'test' split
- All data content remains identical to the original dataset

### Original Dataset

- **Source**: [davidkim205/ko-math-500](https://huggingface.co/datasets/davidkim205/ko-math-500)
- **Original Author**: davidkim205
- **Language**: Korean
- **Task**: Math problem solving

### Usage

```python
from datasets import load_dataset

dataset = load_dataset("ENSEONG/ko-math-500-test", split="test")
print(dataset[0])
```

### Citation

Please cite the original dataset if you use this data:

```
Original dataset: davidkim205/ko-math-500
Available at: https://huggingface.co/datasets/davidkim205/ko-math-500
```

### License

Please refer to the original dataset's license at [davidkim205/ko-math-500](https://huggingface.co/datasets/davidkim205/ko-math-500).
