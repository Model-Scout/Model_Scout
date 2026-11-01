---
configs:
- config_name: default
  data_files:
  - split: train
    path: train.jsonl.gz
  - split: validation
    path: validation.jsonl.gz
  - split: test
    path: test.jsonl.gz
- config_name: test_zh_en
  data_files:
  - split: test
    path: test_zh_en.jsonl
- config_name: test_ja_en
  data_files:
  - split: test
    path: test_ja_en.jsonl
- config_name: test_de_en
  data_files:
  - split: test
    path: test_de_en.jsonl
- config_name: test_es_en
  data_files:
  - split: test
    path: test_es_en.jsonl
- config_name: test_ko_en
  data_files:
  - split: test
    path: test_ko_en.jsonl
- config_name: test_fr_en
  data_files:
  - split: test
    path: test_fr_en.jsonl
- config_name: test_it_en
  data_files:
  - split: test
    path: test_it_en.jsonl
- config_name: test_pt_en
  data_files:
  - split: test
    path: test_pt_en.jsonl
- config_name: test_nl_en
  data_files:
  - split: test
    path: test_nl_en.jsonl
dataset_info:
- config_name: default
  features:
  - name: split
    dtype: string
  - name: genre
    dtype: string
  - name: dataset
    dtype: string
  - name: year
    dtype: string
  - name: sid
    dtype: string
  - name: score
    dtype: float64
  - name: sentence1
    dtype: string
  - name: sentence2
    dtype: string
  splits:
  - name: train
    num_examples: 5749
  - name: validation
    num_examples: 1500
  - name: test
    num_examples: 1379
- config_name: test_zh_en
  features:
  - name: split
    dtype: string
  - name: genre
    dtype: string
  - name: dataset
    dtype: string
  - name: year
    dtype: string
  - name: sid
    dtype: string
  - name: score
    dtype: float64
  - name: sentence1
    dtype: string
  - name: sentence2
    dtype: string
  splits:
  - name: test
    num_examples: 1379
- config_name: test_ja_en
  features:
  - name: split
    dtype: string
  - name: genre
    dtype: string
  - name: dataset
    dtype: string
  - name: year
    dtype: string
  - name: sid
    dtype: string
  - name: score
    dtype: float64
  - name: sentence1
    dtype: string
  - name: sentence2
    dtype: string
  splits:
  - name: test
    num_examples: 1379
- config_name: test_de_en
  features:
  - name: split
    dtype: string
  - name: genre
    dtype: string
  - name: dataset
    dtype: string
  - name: year
    dtype: string
  - name: sid
    dtype: string
  - name: score
    dtype: float64
  - name: sentence1
    dtype: string
  - name: sentence2
    dtype: string
  splits:
  - name: test
    num_examples: 1379
- config_name: test_es_en
  features:
  - name: split
    dtype: string
  - name: genre
    dtype: string
  - name: dataset
    dtype: string
  - name: year
    dtype: string
  - name: sid
    dtype: string
  - name: score
    dtype: float64
  - name: sentence1
    dtype: string
  - name: sentence2
    dtype: string
  splits:
  - name: test
    num_examples: 1379
- config_name: test_ko_en
  features:
  - name: split
    dtype: string
  - name: genre
    dtype: string
  - name: dataset
    dtype: string
  - name: year
    dtype: string
  - name: sid
    dtype: string
  - name: score
    dtype: float64
  - name: sentence1
    dtype: string
  - name: sentence2
    dtype: string
  splits:
  - name: test
    num_examples: 1379
- config_name: test_fr_en
  features:
  - name: split
    dtype: string
  - name: genre
    dtype: string
  - name: dataset
    dtype: string
  - name: year
    dtype: string
  - name: sid
    dtype: string
  - name: score
    dtype: float64
  - name: sentence1
    dtype: string
  - name: sentence2
    dtype: string
  splits:
  - name: test
    num_examples: 1379
- config_name: test_it_en
  features:
  - name: split
    dtype: string
  - name: genre
    dtype: string
  - name: dataset
    dtype: string
  - name: year
    dtype: string
  - name: sid
    dtype: string
  - name: score
    dtype: float64
  - name: sentence1
    dtype: string
  - name: sentence2
    dtype: string
  splits:
  - name: test
    num_examples: 1379
- config_name: test_pt_en
  features:
  - name: split
    dtype: string
  - name: genre
    dtype: string
  - name: dataset
    dtype: string
  - name: year
    dtype: string
  - name: sid
    dtype: string
  - name: score
    dtype: float64
  - name: sentence1
    dtype: string
  - name: sentence2
    dtype: string
  splits:
  - name: test
    num_examples: 1379
- config_name: test_nl_en
  features:
  - name: split
    dtype: string
  - name: genre
    dtype: string
  - name: dataset
    dtype: string
  - name: year
    dtype: string
  - name: sid
    dtype: string
  - name: score
    dtype: float64
  - name: sentence1
    dtype: string
  - name: sentence2
    dtype: string
  splits:
  - name: test
    num_examples: 1379
language:
- en
- zh
- ja
- de
- es
- ko
- fr
- it
- pt
- nl
multilinguality: multilingual
task_categories:
- sentence-similarity
task_ids: []
tags:
- mteb
- text
- code-switching
- sts
---

<div align="center" style="padding: 40px 20px; background-color: white; border-radius: 12px; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05); max-width: 600px; margin: 0 auto;">
  <h1 style="font-size: 3.5rem; color: #1a1a1a; margin: 0 0 20px 0; letter-spacing: 2px; font-weight: 700;">STSBenchmark CS-MTEB</h1>
  <div style="font-size: 1.5rem; color: #4a4a4a; margin-bottom: 5px; font-weight: 300;">An <a href="https://github.com/embeddings-benchmark/mteb" style="color: #2c5282; font-weight: 600; text-decoration: none;">MTEB</a> dataset</div>
  <div style="font-size: 0.9rem; color: #2c5282; margin-top: 10px;">Massive Text Embedding Benchmark</div>
</div>

Code-switching version of [mteb/stsbenchmark-sts](https://huggingface.co/datasets/mteb/stsbenchmark-sts), with test set sentence pairs rewritten in Chinese-English, Japanese-English, German-English, Spanish-English, Korean-English, French-English, Italian-English, Portuguese-English, Dutch-English code-switching styles.

## Dataset Structure

The dataset contains the following configurations:

**From original dataset (unchanged):**
- `default`: Original train, validation, and test splits

**Code-switching test sets:**
- `test_zh_en`: Chinese-English code-switching test set
- `test_ja_en`: Japanese-English code-switching test set
- `test_de_en`: German-English code-switching test set
- `test_es_en`: Spanish-English code-switching test set
- `test_ko_en`: Korean-English code-switching test set
- `test_fr_en`: French-English code-switching test set
- `test_it_en`: Italian-English code-switching test set
- `test_pt_en`: Portuguese-English code-switching test set
- `test_nl_en`: Dutch-English code-switching test set

## Usage

```python
from datasets import load_dataset

# Load code-switching test sets
test_zh = load_dataset("UTokyo-Yokoya-Lab/stsbenchmark-sts_CS-MTEB", "test_zh_en")
test_ja = load_dataset("UTokyo-Yokoya-Lab/stsbenchmark-sts_CS-MTEB", "test_ja_en")
test_de = load_dataset("UTokyo-Yokoya-Lab/stsbenchmark-sts_CS-MTEB", "test_de_en")
test_es = load_dataset("UTokyo-Yokoya-Lab/stsbenchmark-sts_CS-MTEB", "test_es_en")
test_ko = load_dataset("UTokyo-Yokoya-Lab/stsbenchmark-sts_CS-MTEB", "test_ko_en")
test_fr = load_dataset("UTokyo-Yokoya-Lab/stsbenchmark-sts_CS-MTEB", "test_fr_en")
test_it = load_dataset("UTokyo-Yokoya-Lab/stsbenchmark-sts_CS-MTEB", "test_it_en")
test_pt = load_dataset("UTokyo-Yokoya-Lab/stsbenchmark-sts_CS-MTEB", "test_pt_en")
test_nl = load_dataset("UTokyo-Yokoya-Lab/stsbenchmark-sts_CS-MTEB", "test_nl_en")

# Load original data
original = load_dataset("UTokyo-Yokoya-Lab/stsbenchmark-sts_CS-MTEB", "default")
```

## Attribution
Based on [mteb/stsbenchmark-sts](https://huggingface.co/datasets/mteb/stsbenchmark-sts).

## Citation
If you use this dataset, please also cite the original:

```bibtex
@inproceedings{cer2017semeval,
  author = {Daniel Cer and Mona Diab and Eneko Agirre and I\~{n}igo Lopez-Gazpio and Lucia Specia},
  booktitle = {Proceedings of the 11th International Workshop on Semantic Evaluation (SemEval-2017)},
  doi = {10.18653/v1/S17-2001},
  pages = {1--14},
  title = {SemEval-2017 Task 1: Semantic Textual Similarity Multilingual and Crosslingual Focused Evaluation},
  year = {2017},
}

@article{enevoldsen2025mmtebmassivemultilingualtext,
  title={MMTEB: Massive Multilingual Text Embedding Benchmark},
  author={Kenneth Enevoldsen and Isaac Chung and Imene Kerboua and others},
  journal={arXiv preprint arXiv:2502.13595},
  year={2025},
  url={https://arxiv.org/abs/2502.13595},
  doi={10.48550/arXiv.2502.13595},
}

@article{muennighoff2022mteb,
  author = {Muennighoff, Niklas and Tazi, Nouamane and Magne, Lo\"{\i}c and Reimers, Nils},
  title = {MTEB: Massive Text Embedding Benchmark},
  journal={arXiv preprint arXiv:2210.07316},
  year = {2022},
  url = {https://arxiv.org/abs/2210.07316},
  doi = {10.48550/ARXIV.2210.07316},
}
```
