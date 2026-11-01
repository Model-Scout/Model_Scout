---
configs:
- config_name: corpus
  data_files:
  - path: corpus/test-*
    split: test
- config_name: default
  data_files:
  - path: data/test-*
    split: test
- config_name: queries_zh_en
  data_files:
  - path: queries_zh_en/test-*
    split: test
- config_name: queries_ja_en
  data_files:
  - path: queries_ja_en/test-*
    split: test
- config_name: queries_de_en
  data_files:
  - path: queries_de_en/test-*
    split: test
- config_name: queries_es_en
  data_files:
  - path: queries_es_en/test-*
    split: test
- config_name: queries_ko_en
  data_files:
  - path: queries_ko_en/test-*
    split: test
- config_name: queries_fr_en
  data_files:
  - path: queries_fr_en/test-*
    split: test
- config_name: queries_it_en
  data_files:
  - path: queries_it_en/test-*
    split: test
- config_name: queries_pt_en
  data_files:
  - path: queries_pt_en/test-*
    split: test
- config_name: queries_nl_en
  data_files:
  - path: queries_nl_en/test-*
    split: test
dataset_info:
- config_name: corpus
  features:
  - name: _id
    dtype: string
  - name: text
    dtype: string
  - name: title
    dtype: string
  splits:
  - name: test
    num_examples: 47416
- config_name: default
  features:
  - name: query-id
    dtype: string
  - name: corpus-id
    dtype: string
  - name: score
    dtype: float64
  splits:
  - name: test
    num_examples: 3048
- config_name: queries_zh_en
  features:
  - name: _id
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_examples: 1000
- config_name: queries_ja_en
  features:
  - name: _id
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_examples: 1000
- config_name: queries_de_en
  features:
  - name: _id
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_examples: 1000
- config_name: queries_es_en
  features:
  - name: _id
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_examples: 1000
- config_name: queries_ko_en
  features:
  - name: _id
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_examples: 1000
- config_name: queries_fr_en
  features:
  - name: _id
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_examples: 1000
- config_name: queries_it_en
  features:
  - name: _id
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_examples: 1000
- config_name: queries_pt_en
  features:
  - name: _id
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_examples: 1000
- config_name: queries_nl_en
  features:
  - name: _id
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_examples: 1000
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
- text-retrieval
task_ids: []
tags:
- mteb
- text
- code-switching
---

<div align="center" style="padding: 40px 20px; background-color: white; border-radius: 12px; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05); max-width: 600px; margin: 0 auto;">
  <h1 style="font-size: 3.5rem; color: #1a1a1a; margin: 0 0 20px 0; letter-spacing: 2px; font-weight: 700;">ClimateFEVER CS-MTEB</h1>
  <div style="font-size: 1.5rem; color: #4a4a4a; margin-bottom: 5px; font-weight: 300;">An <a href="https://github.com/embeddings-benchmark/mteb" style="color: #2c5282; font-weight: 600; text-decoration: none;">MTEB</a> dataset</div>
  <div style="font-size: 0.9rem; color: #2c5282; margin-top: 10px;">Massive Text Embedding Benchmark</div>
</div>

Code-switching version of [mteb/ClimateFEVER_test_top_250_only_w_correct-v2](https://huggingface.co/datasets/mteb/ClimateFEVER_test_top_250_only_w_correct-v2), with queries rewritten in Chinese-English, Japanese-English, German-English, Spanish-English, Korean-English, French-English, Italian-English, Portuguese-English, Dutch-English code-switching styles.

## Dataset Structure

The dataset contains the following configurations:

**From original dataset (unchanged):**
- `corpus`: Original corpus documents
- `default`: Original relevance judgments (qrels)

**Code-switching queries:**
- `queries_zh_en`: Chinese-English code-switching queries
- `queries_ja_en`: Japanese-English code-switching queries
- `queries_de_en`: German-English code-switching queries
- `queries_es_en`: Spanish-English code-switching queries
- `queries_ko_en`: Korean-English code-switching queries
- `queries_fr_en`: French-English code-switching queries
- `queries_it_en`: Italian-English code-switching queries
- `queries_pt_en`: Portuguese-English code-switching queries
- `queries_nl_en`: Dutch-English code-switching queries

## Usage

```python
from datasets import load_dataset

# Load code-switching queries
queries_zh = load_dataset("UTokyo-Yokoya-Lab/ClimateFEVER_hardnegatives_CS-MTEB", "queries_zh_en")
queries_ja = load_dataset("UTokyo-Yokoya-Lab/ClimateFEVER_hardnegatives_CS-MTEB", "queries_ja_en")
queries_de = load_dataset("UTokyo-Yokoya-Lab/ClimateFEVER_hardnegatives_CS-MTEB", "queries_de_en")
queries_es = load_dataset("UTokyo-Yokoya-Lab/ClimateFEVER_hardnegatives_CS-MTEB", "queries_es_en")
queries_ko = load_dataset("UTokyo-Yokoya-Lab/ClimateFEVER_hardnegatives_CS-MTEB", "queries_ko_en")
queries_fr = load_dataset("UTokyo-Yokoya-Lab/ClimateFEVER_hardnegatives_CS-MTEB", "queries_fr_en")
queries_it = load_dataset("UTokyo-Yokoya-Lab/ClimateFEVER_hardnegatives_CS-MTEB", "queries_it_en")
queries_pt = load_dataset("UTokyo-Yokoya-Lab/ClimateFEVER_hardnegatives_CS-MTEB", "queries_pt_en")
queries_nl = load_dataset("UTokyo-Yokoya-Lab/ClimateFEVER_hardnegatives_CS-MTEB", "queries_nl_en")

# Load original configs
corpus = load_dataset("UTokyo-Yokoya-Lab/ClimateFEVER_hardnegatives_CS-MTEB", "corpus")
qrels = load_dataset("UTokyo-Yokoya-Lab/ClimateFEVER_hardnegatives_CS-MTEB", "default")
```

## Attribution
Based on [mteb/ClimateFEVER_test_top_250_only_w_correct-v2](https://huggingface.co/datasets/mteb/ClimateFEVER_test_top_250_only_w_correct-v2).

## Citation
If you use this dataset, please also cite the original:

```bibtex
@misc{diggelmann2020climatefever,
  archiveprefix = {arXiv},
  author = {Thomas Diggelmann and Jordan Boyd-Graber and Jannis Bulian and Massimiliano Ciaramita and Markus Leippold},
  eprint = {2012.00614},
  primaryclass = {cs.CL},
  title = {CLIMATE-FEVER: A Dataset for Verification of Real-World Climate Claims},
  year = {2020},
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
