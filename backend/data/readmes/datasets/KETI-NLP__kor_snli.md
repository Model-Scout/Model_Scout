---
language:
- ko
license: cc-by-4.0
size_categories:
- 100K<n<1M
task_categories:
- text-classification
task_ids:
- natural-language-inference
- multi-input-text-classification
dataset_info:
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: label
    dtype:
      class_label:
        names:
          '0': entailment
          '1': neutral
          '2': contradiction
  - name: data_index_by_user
    dtype: int32
  splits:
  - name: train
    num_bytes: 85943643
    num_examples: 550152
  - name: validation
    num_bytes: 1631544
    num_examples: 10000
  - name: test
    num_bytes: 1638084
    num_examples: 10000
  download_size: 27268480
  dataset_size: 89213271
---

# Dataset Card for QASC

## Licensing Information

The data is distributed under the [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) license.

## Source Data Citation INformation

```
@inproceedings{snli:emnlp2015,
	Author = {Bowman, Samuel R. and Angeli, Gabor and Potts, Christopher, and Manning, Christopher D.},
	Booktitle = {Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
	Publisher = {Association for Computational Linguistics},
	Title = {A large annotated corpus for learning natural language inference},
	Year = {2015}
}
```