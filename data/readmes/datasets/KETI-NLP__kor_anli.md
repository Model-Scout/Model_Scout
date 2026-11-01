---
language:
- ko
license: 
- cc-by-nc-4.0
size_categories:
- 100K<n<1M
task_categories:
- text-classification
task_ids:
- natural-language-inference
- multi-input-text-classification
paperswithcode_id: anli
pretty_name: Adversarial NLI
dataset_info:
  features:
  - name: data_index_by_user
    dtype: int32
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
  - name: reason
    dtype: string
  splits:
  - name: train_r1
    num_bytes: 8505556
    num_examples: 16946
  - name: train_r2
    num_bytes: 22521662
    num_examples: 45460
  - name: train_r3
    num_bytes: 48605206
    num_examples: 100459
  - name: dev_r1
    num_bytes: 628891
    num_examples: 1000
  - name: dev_r2
    num_bytes: 613763
    num_examples: 1000
  - name: dev_r3
    num_bytes: 740840
    num_examples: 1200
  - name: test_r1
    num_bytes: 626555
    num_examples: 1000
  - name: test_r2
    num_bytes: 633241
    num_examples: 1000
  - name: test_r3
    num_bytes: 736887
    num_examples: 1200
  download_size: 23386318
  dataset_size: 83612601
---

# Dataset Card for anli

## Licensing Information

[cc-4 Attribution-NonCommercial](https://github.com/facebookresearch/anli/blob/main/LICENSE)

## Source Data Citation INformation

```
@InProceedings{nie2019adversarial,
    title={Adversarial NLI: A New Benchmark for Natural Language Understanding},
    author={Nie, Yixin
                and Williams, Adina
                and Dinan, Emily
                and Bansal, Mohit
                and Weston, Jason
                and Kiela, Douwe},
    booktitle = "Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics",
    year = "2020",
    publisher = "Association for Computational Linguistics",
}