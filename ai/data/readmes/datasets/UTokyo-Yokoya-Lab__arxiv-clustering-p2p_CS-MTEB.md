---
configs:
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
- config_name: test_zh_en
  features:
  - name: sentences
    dtype: string
  - name: labels
    dtype: string
  splits:
  - name: test
    num_examples: 73272
- config_name: test_ja_en
  features:
  - name: sentences
    dtype: string
  - name: labels
    dtype: string
  splits:
  - name: test
    num_examples: 73272
- config_name: test_de_en
  features:
  - name: sentences
    dtype: string
  - name: labels
    dtype: string
  splits:
  - name: test
    num_examples: 73272
- config_name: test_es_en
  features:
  - name: sentences
    dtype: string
  - name: labels
    dtype: string
  splits:
  - name: test
    num_examples: 73272
- config_name: test_ko_en
  features:
  - name: sentences
    dtype: string
  - name: labels
    dtype: string
  splits:
  - name: test
    num_examples: 73272
- config_name: test_fr_en
  features:
  - name: sentences
    dtype: string
  - name: labels
    dtype: string
  splits:
  - name: test
    num_examples: 73272
- config_name: test_it_en
  features:
  - name: sentences
    dtype: string
  - name: labels
    dtype: string
  splits:
  - name: test
    num_examples: 73272
- config_name: test_pt_en
  features:
  - name: sentences
    dtype: string
  - name: labels
    dtype: string
  splits:
  - name: test
    num_examples: 73272
- config_name: test_nl_en
  features:
  - name: sentences
    dtype: string
  - name: labels
    dtype: string
  splits:
  - name: test
    num_examples: 73272
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
- text-clustering
task_ids: []
tags:
- mteb
- text
- code-switching
- clustering
---

<div align="center" style="padding: 40px 20px; background-color: white; border-radius: 12px; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05); max-width: 600px; margin: 0 auto;">
  <h1 style="font-size: 3.5rem; color: #1a1a1a; margin: 0 0 20px 0; letter-spacing: 2px; font-weight: 700;">ArXiv Clustering P2P CS-MTEB</h1>
  <div style="font-size: 1.5rem; color: #4a4a4a; margin-bottom: 5px; font-weight: 300;">An <a href="https://github.com/embeddings-benchmark/mteb" style="color: #2c5282; font-weight: 600; text-decoration: none;">MTEB</a> dataset</div>
  <div style="font-size: 0.9rem; color: #2c5282; margin-top: 10px;">Massive Text Embedding Benchmark</div>
</div>

Code-switching version of [mteb/arxiv-clustering-p2p](https://huggingface.co/datasets/mteb/arxiv-clustering-p2p), with sentences rewritten in Chinese-English, Japanese-English, German-English, Spanish-English, Korean-English, French-English, Italian-English, Portuguese-English, Dutch-English code-switching styles.

## Dataset Structure

The dataset contains the following configurations:

**Code-switching versions:**
- `test_zh_en`: Chinese-English code-switching sentences
- `test_ja_en`: Japanese-English code-switching sentences
- `test_de_en`: German-English code-switching sentences
- `test_es_en`: Spanish-English code-switching sentences
- `test_ko_en`: Korean-English code-switching sentences
- `test_fr_en`: French-English code-switching sentences
- `test_it_en`: Italian-English code-switching sentences
- `test_pt_en`: Portuguese-English code-switching sentences
- `test_nl_en`: Dutch-English code-switching sentences

## Usage

```python
from datasets import load_dataset

# Load code-switching versions
test_zh = load_dataset("UTokyo-Yokoya-Lab/arxiv-clustering-p2p_CS-MTEB", "test_zh_en")
test_ja = load_dataset("UTokyo-Yokoya-Lab/arxiv-clustering-p2p_CS-MTEB", "test_ja_en")
test_de = load_dataset("UTokyo-Yokoya-Lab/arxiv-clustering-p2p_CS-MTEB", "test_de_en")
test_es = load_dataset("UTokyo-Yokoya-Lab/arxiv-clustering-p2p_CS-MTEB", "test_es_en")
test_ko = load_dataset("UTokyo-Yokoya-Lab/arxiv-clustering-p2p_CS-MTEB", "test_ko_en")
test_fr = load_dataset("UTokyo-Yokoya-Lab/arxiv-clustering-p2p_CS-MTEB", "test_fr_en")
test_it = load_dataset("UTokyo-Yokoya-Lab/arxiv-clustering-p2p_CS-MTEB", "test_it_en")
test_pt = load_dataset("UTokyo-Yokoya-Lab/arxiv-clustering-p2p_CS-MTEB", "test_pt_en")
test_nl = load_dataset("UTokyo-Yokoya-Lab/arxiv-clustering-p2p_CS-MTEB", "test_nl_en")
```

## Attribution
Based on [mteb/arxiv-clustering-p2p](https://huggingface.co/datasets/mteb/arxiv-clustering-p2p).

## Citation
If you use this dataset, please also cite the original:

```bibtex
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
