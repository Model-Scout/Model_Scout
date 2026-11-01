---
language:
- af
- ar
- az
- bg
- bn
- de
- el
- en
- es
- et
- eu
- fa
- fi
- fr
- gu
- he
- hi
- ht
- hu
- id
- it
- ja
- jv
- ka
- kk
- ko
- lt
- ml
- mr
- ms
- my
- nl
- pa
- pl
- pt
- qu
- ro
- ru
- sw
- ta
- te
- th
- tl
- tr
- uk
- ur
- vi
- wo
- yo
- zh
license: apache-2.0
pretty_name: Mewsli-X
task_categories:
- text-retrieval
task_ids:
- entity-linking-retrieval
configs:
- config_name: wikipedia_pairs
  data_files:
  - split: train
    path: wikipedia_pairs/train.jsonl.tar.gz
  - split: validation
    path: wikipedia_pairs/dev.jsonl.tar.gz
- config_name: ar
  data_files:
  - split: validation
    path: wikinews_mentions/ar/dev.jsonl
  - split: test
    path: wikinews_mentions/ar/test.jsonl
- config_name: de
  data_files:
  - split: validation
    path: wikinews_mentions/de/dev.jsonl
  - split: test
    path: wikinews_mentions/de/test.jsonl
- config_name: en
  data_files:
  - split: validation
    path: wikinews_mentions/en/dev.jsonl
  - split: test
    path: wikinews_mentions/en/test.jsonl
- config_name: es
  data_files:
  - split: validation
    path: wikinews_mentions/es/dev.jsonl
  - split: test
    path: wikinews_mentions/es/test.jsonl
- config_name: fa
  data_files:
  - split: validation
    path: wikinews_mentions/fa/dev.jsonl
  - split: test
    path: wikinews_mentions/fa/test.jsonl
- config_name: ja
  data_files:
  - split: validation
    path: wikinews_mentions/ja/dev.jsonl
  - split: test
    path: wikinews_mentions/ja/test.jsonl
- config_name: pl
  data_files:
  - split: validation
    path: wikinews_mentions/pl/dev.jsonl
  - split: test
    path: wikinews_mentions/pl/test.jsonl
- config_name: ro
  data_files:
  - split: validation
    path: wikinews_mentions/ro/dev.jsonl
  - split: test
    path: wikinews_mentions/ro/test.jsonl
- config_name: ta
  data_files:
  - split: validation
    path: wikinews_mentions/ta/dev.jsonl
  - split: test
    path: wikinews_mentions/ta/test.jsonl
- config_name: tr
  data_files:
  - split: validation
    path: wikinews_mentions/tr/dev.jsonl
  - split: test
    path: wikinews_mentions/tr/test.jsonl
- config_name: uk
  data_files:
  - split: validation
    path: wikinews_mentions/uk/dev.jsonl
  - split: test
    path: wikinews_mentions/uk/test.jsonl
- config_name: candidate_entities
  data_files:
  - split: test
    path: candidate_entities.jsonl.tar.gz
size_categories:
- 100K<n<1M
---

I generated the dataset following [mewsli-x.md#getting-started](https://github.com/google-research/google-research/blob/master/dense_representations_for_entity_retrieval/mel/mewsli-x.md#getting-started)
and converted into different parts (see [`process.py`](process.py)):
 - ar/de/en/es/fa/ja/pl/ro/ta/tr/uk wikinews_mentions dev and test (from `wikinews_mentions-dev/test.jsonl`)
 - candidate entities of 50 languages (from `candidate_set_entities.jsonl`)
 - English wikipedia_pairs to fine-tune models (from `wikipedia_pairs-dev/train.jsonl`)

Raw data files are in [`raw.tar.gz`](raw.tar.gz), which contains:
```
[...] 535M Feb 24 22:06 candidate_set_entities.jsonl
[...] 9.8M Feb 24 22:06 wikinews_mentions-dev.jsonl
[...]  35M Feb 24 22:06 wikinews_mentions-test.jsonl
[...]  24M Feb 24 22:06 wikipedia_pairs-dev.jsonl
[...] 283M Feb 24 22:06 wikipedia_pairs-train.jsonl
```

**Below is from the original [readme](https://github.com/google-research/google-research/blob/master/dense_representations_for_entity_retrieval/mel/mewsli-x.md)**

# Mewsli-X

Mewsli-X is a multilingual dataset of entity mentions appearing in
[WikiNews](https://www.wikinews.org/) and
[Wikipedia](https://www.wikipedia.org/) articles, that have been automatically
linked to [WikiData](https://www.wikidata.org/) entries.

The primary use case is to evaluate transfer-learning in the zero-shot
cross-lingual setting of the
[XTREME-R benchmark suite](https://sites.research.google/xtremer):

1.  Fine-tune a pretrained model on English Wikipedia examples;
2.  Evaluate on WikiNews in other languages &mdash; **given an *entity mention*
    in a WikiNews article, retrieve the correct *entity* from the predefined
    candidate set by means of its textual description.**

Mewsli-X constitutes a *doubly zero-shot* task by construction: at test time, a
model has to contend with different languages and a different set of entities
from those observed during fine-tuning.

👉 For data examples and other editions of Mewsli, see [README.md](https://github.com/google-research/google-research/blob/master/dense_representations_for_entity_retrieval/mel/README.md).

👉 Consider submitting to the
**[XTREME-R leaderboard](https://sites.research.google/xtremer)**. The XTREME-R
[repository](https://github.com/google-research/xtreme) includes code for
getting started with training and evaluating a baseline model in PyTorch.

👉 Please cite this paper if you use the data/code in your work: *[XTREME-R:
Towards More Challenging and Nuanced Multilingual Evaluation (Ruder et al.,
2021)](https://aclanthology.org/2021.emnlp-main.802.pdf)*.

> _**NOTE:** New evaluation results on Mewsli-X are **not** directly comparable to those reported in the paper because the dataset required further updates, as detailed [below](#updated-dataset). This does not affect the overall findings of the paper._

```
@inproceedings{ruder-etal-2021-xtreme,
    title = "{XTREME}-{R}: Towards More Challenging and Nuanced Multilingual Evaluation",
    author = "Ruder, Sebastian  and
      Constant, Noah  and
      Botha, Jan  and
      Siddhant, Aditya  and
      Firat, Orhan  and
      Fu, Jinlan  and
      Liu, Pengfei  and
      Hu, Junjie  and
      Garrette, Dan  and
      Neubig, Graham  and
      Johnson, Melvin",
    booktitle = "Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing",
    month = nov,
    year = "2021",
    address = "Online and Punta Cana, Dominican Republic",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.emnlp-main.802",
    doi = "10.18653/v1/2021.emnlp-main.802",
    pages = "10215--10245",
}
```