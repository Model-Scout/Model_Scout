---
language:
- ko
license:
- cc-by-sa-3.0
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- question-answering
task_ids:
- extractive-qa
paperswithcode_id: wikihop
pretty_name: WikiHop
dataset_info:
  features:
  - name: data_index_by_user
    dtype: int32
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: candidates
    sequence: string
  - name: supports
    sequence: string
  - name: annotations
    sequence:
      sequence: string
  splits:
  - name: train
    num_bytes: 351647702
    num_examples: 43738
  - name: validation
    num_bytes: 44492664
    num_examples: 5129
  download_size: 221782303
  dataset_size: 396140366
---

# Dataset Card for wiki_hop

## Licensing Information

The data is distributed under the [CC BY SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en) license.

## Source Data Citation Information

```
@article{DBLP:journals/corr/abs-1710-06481,
  author       = {Johannes Welbl and
                  Pontus Stenetorp and
                  Sebastian Riedel},
  title        = {Constructing Datasets for Multi-hop Reading Comprehension Across Documents},
  journal      = {CoRR},
  volume       = {abs/1710.06481},
  year         = {2017},
  url          = {http://arxiv.org/abs/1710.06481},
  eprinttype    = {arXiv},
  eprint       = {1710.06481},
  timestamp    = {Mon, 13 Aug 2018 16:46:34 +0200},
  biburl       = {https://dblp.org/rec/journals/corr/abs-1710-06481.bib},
  bibsource    = {dblp computer science bibliography, https://dblp.org}
}
```