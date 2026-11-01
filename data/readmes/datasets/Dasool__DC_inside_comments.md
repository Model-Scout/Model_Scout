---
dataset_info:
  features:
  - name: comments
    dtype: string
  splits:
  - name: train
    num_bytes: 11577591
    num_examples: 111546
  download_size: 7972902
  dataset_size: 11577591
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: apache-2.0
task_categories:
- text-generation
language:
- ko
size_categories:
- 100K<n<1M
---

# DC_inside_comments

This dataset contains 110,000 raw comments collected from [DC Inside](https://www.dcinside.com/). It is intended for unsupervised learning or pretraining purposes.

## Dataset Summary

- **Data Type**: Unlabeled raw comments
- **Number of Examples**: 110,000
- **Source**: DC Inside

## Related Dataset

For labeled data and multi-task annotated examples, please refer to the [KoMultiText](https://huggingface.co/datasets/Dasool/KoMultiText) dataset.

## How to Load the Dataset
```python
from datasets import load_dataset

# Load the unlabeled dataset
dataset = load_dataset("Dasool/DC_inside_comments")
print(dataset)
```

## Citation

```bibtex
@misc{choi2023largescale,
      title={Large-Scale Korean Text Dataset for Classifying Biased Speech in Real-World Online Services}, 
      author={Dasol Choi and Jooyoung Song and Eunsun Lee and Jinwoo Seo and Heejune Park and Dongbin Na},
      year={2023},
      eprint={2310.04313},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

## Contact
* dasolchoi@yonsei.ac.kr