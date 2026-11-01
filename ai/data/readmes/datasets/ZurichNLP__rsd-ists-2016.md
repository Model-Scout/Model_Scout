---
license: cc-by-sa-4.0
language_creators:
  - machine-generated
dataset_info:
  features:
  - name: tokens_a
    sequence: string
  - name: tokens_b
    sequence: string
  - name: labels_a
    sequence: float64
  - name: labels_b
    sequence: float64
  - name: lang_a
    dtype: string
  - name: lang_b
    dtype: string
  - name: subset
    dtype: string
  - name: id
    dtype: string
  - name: alignments
    dtype: string
  splits:
  - name: train_en
    num_bytes: 1640900
    num_examples: 1506
  - name: train_de
    num_bytes: 1101404
    num_examples: 3012
  - name: train_es
    num_bytes: 1154765
    num_examples: 3012
  - name: train_fr
    num_bytes: 1206414
    num_examples: 3012
  - name: train_ja
    num_bytes: 838252
    num_examples: 3012
  - name: train_ko
    num_bytes: 829328
    num_examples: 3012
  - name: train_zh
    num_bytes: 796140
    num_examples: 3012
  - name: train_it
    num_bytes: 1111516
    num_examples: 3012
  - name: test_en
    num_bytes: 833900
    num_examples: 750
  - name: test_de
    num_bytes: 558624
    num_examples: 1500
  - name: test_es
    num_bytes: 580224
    num_examples: 1500
  - name: test_fr
    num_bytes: 610017
    num_examples: 1500
  - name: test_ja
    num_bytes: 425912
    num_examples: 1500
  - name: test_ko
    num_bytes: 424407
    num_examples: 1500
  - name: test_zh
    num_bytes: 403680
    num_examples: 1500
  - name: test_it
    num_bytes: 561989
    num_examples: 1500
  download_size: 2569205
  dataset_size: 11403967
task_categories:
- token-classification
language:
- en
- de
- es
- fr
- ja
- ko
- zh
- it
size_categories:
- 1K<n<10K
---

Training and test data for the task of Recognizing Semantic Differences (RSD).

[See the paper](https://arxiv.org/abs/2305.13303) for details on how the dataset was created, and see our code at https://github.com/ZurichNLP/recognizing-semantic-differences for an example of how to use the data for evaluation.

The data are derived from the [SemEval-2016 Task 2 for Interpretable Semantic Textual Similarity](https://alt.qcri.org/semeval2016/task2/) organized by [Agirre et al. (2016)](http://dx.doi.org/10.18653/v1/S16-1082).
The original URLs of the data are:
* Train: http://alt.qcri.org/semeval2016/task2/data/uploads/train_2015_10_22.utf-8.tar.gz
* Test: http://alt.qcri.org/semeval2016/task2/data/uploads/test_goldstandard.tar.gz

The translations into non-English languages have been created using machine translation (DeepL).

## Citation
```bibtex
@inproceedings{vamvas-sennrich-2023-rsd,
      title={Towards Unsupervised Recognition of Token-level Semantic Differences in Related Documents},
      author={Jannis Vamvas and Rico Sennrich},
      month = dec,
      year = "2023",
      booktitle = "Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing",
      address = "Singapore",
      publisher = "Association for Computational Linguistics",
}
```
