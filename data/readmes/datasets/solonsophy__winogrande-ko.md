---
language:
- ko
license: cc-by-4.0
task_categories:
- text-classification
- multiple-choice
size_categories:
- 10K<n<100K
source_datasets:
- allenai/winogrande
---

# Winogrande-Ko (Korean Translation)

## Dataset Summary

This dataset is a Korean translation of the [Winogrande](https://huggingface.co/datasets/allenai/winogrande) dataset by Allen Institute for AI. Winogrande is a commonsense reasoning benchmark consisting of 44k fill-in-the-blank problems.

I provide Korean translations for the "XL" split (43,432 records total).

## Data Splits

| Split      | Records | Description |
|------------|---------|-------------|
| **Train**      | 40,398  | Main training data (verified clean) |
| **Validation** | 1,267   | Validation set (verified clean) |
| **Test**       | 1,767   | Test set (labels hidden/empty) |

## Supported Tasks

- Commonsense Reasoning
- Text Classification (Binary Choice)

## Data Structure

Each record contains the original English fields and their Korean translations:

- `id`: Original record ID
- `sentence`: Original English sentence with a blank `_`
- `option1`: English Option 1
- `option2`: English Option 2
- `answer`: Correct answer "1" or "2" (Empty string `""` in Test set)
- `sentence_ko`: Korean translated sentence with `_`
- `option1_ko`: Korean Option 1
- `option2_ko`: Korean Option 2

## Citation

If you use this dataset, please cite the original Winogrande paper:

```bibtex
@article{sakaguchi2019winogrande,
  title={WinoGrande: An Adversarial Winograd Schema Challenge at Scale},
  author={Sakaguchi, Keisuke and Bras, Ronan Le and Bhagavatula, Chandra and Choi, Yejin},
  journal={arXiv preprint arXiv:1907.10641},
  year={2019}
}
```

## License

The **dataset** is distributed under the [CC-BY (Creative Commons Attribution)](https://creativecommons.org/licenses/by/4.0/) license.

## Acknowledgments

This model was trained with computing resources provided by [DDOK.AI](https://huggingface.co/DDOKAI).
