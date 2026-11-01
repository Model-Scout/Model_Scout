---
license: apache-2.0
task_categories:
- text-generation
language:
- ko
tags:
- korean
- education
- fineweb
- text
size_categories:
- 10M<n<100M
---

# Korean FineWeb Edu Demo

A sampled subset of the Korean-translated FineWeb educational dataset for demonstration and development purposes.

## Dataset Description

This dataset is a ~30GB sample from the larger [eliceai/korean-translated-fineweb-edu-dedup](https://huggingface.co/datasets/eliceai/korean-translated-fineweb-edu-dedup) dataset (600GB total). It contains Korean-translated educational content from the FineWeb dataset.

### Dataset Summary

- **Source**: Sampled from `eliceai/korean-translated-fineweb-edu-dedup`
- **Size**: ~30GB
- **Language**: Korean
- **Content**: Educational text content
- **Format**: Parquet files

### Dataset Structure

The dataset contains a single `train` split with the following features:

- `text`: Korean text content (string)

### Usage

```python
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("eliceai/korean-fineweb-edu-demo", split="train")

# Access examples
for example in dataset:
    print(example["text"])
```

### Sampling Method

This dataset was created using streaming mode to sample approximately 30GB from the source dataset without downloading the entire 600GB dataset. The sampling preserves the original order and structure of the source data.

### Source Dataset

- **Original Dataset**: [eliceai/korean-translated-fineweb-edu-dedup](https://huggingface.co/datasets/eliceai/korean-translated-fineweb-edu-dedup)
- **Original Size**: ~600GB
- **Sampling Ratio**: ~5% of original dataset

### License

This dataset follows the same license as the source dataset (Apache 2.0).

### Citation

If you use this dataset, please cite the original source:

```bibtex
@dataset{korean_fineweb_edu_demo,
  title={Korean FineWeb Edu Demo},
  author={Elice AI},
  year={2024},
  url={https://huggingface.co/datasets/eliceai/korean-fineweb-edu-demo}
}
```
