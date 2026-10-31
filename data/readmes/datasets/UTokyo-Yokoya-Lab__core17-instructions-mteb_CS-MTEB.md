---
configs:
- config_name: corpus
  data_files:
  - path: corpus/corpus-*
    split: corpus
- config_name: default
  data_files:
  - path: data/default-*
    split: test
- config_name: qrel_diff
  data_files:
  - path: qrel_diff/qrel_diff-*
    split: qrel_diff
- config_name: top_ranked
  data_files:
  - path: top_ranked/top_ranked-*
    split: top_ranked
- config_name: queries_zh_en
  data_files:
  - path: queries_zh_en/queries-*
    split: queries
- config_name: instructions_zh_en
  data_files:
  - path: instructions_zh_en/instruction-*
    split: instruction
- config_name: queries_ja_en
  data_files:
  - path: queries_ja_en/queries-*
    split: queries
- config_name: instructions_ja_en
  data_files:
  - path: instructions_ja_en/instruction-*
    split: instruction
- config_name: queries_de_en
  data_files:
  - path: queries_de_en/queries-*
    split: queries
- config_name: instructions_de_en
  data_files:
  - path: instructions_de_en/instruction-*
    split: instruction
- config_name: queries_es_en
  data_files:
  - path: queries_es_en/queries-*
    split: queries
- config_name: instructions_es_en
  data_files:
  - path: instructions_es_en/instruction-*
    split: instruction
- config_name: queries_ko_en
  data_files:
  - path: queries_ko_en/queries-*
    split: queries
- config_name: instructions_ko_en
  data_files:
  - path: instructions_ko_en/instruction-*
    split: instruction
- config_name: queries_fr_en
  data_files:
  - path: queries_fr_en/queries-*
    split: queries
- config_name: instructions_fr_en
  data_files:
  - path: instructions_fr_en/instruction-*
    split: instruction
- config_name: queries_it_en
  data_files:
  - path: queries_it_en/queries-*
    split: queries
- config_name: instructions_it_en
  data_files:
  - path: instructions_it_en/instruction-*
    split: instruction
- config_name: queries_pt_en
  data_files:
  - path: queries_pt_en/queries-*
    split: queries
- config_name: instructions_pt_en
  data_files:
  - path: instructions_pt_en/instruction-*
    split: instruction
- config_name: queries_nl_en
  data_files:
  - path: queries_nl_en/queries-*
    split: queries
- config_name: instructions_nl_en
  data_files:
  - path: instructions_nl_en/instruction-*
    split: instruction
dataset_info:
- config_name: corpus
  features:
  - name: _id
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: corpus
    num_examples: 19899
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
    num_examples: 9480
- config_name: qrel_diff
  features:
  - name: query-id
    dtype: string
  - name: corpus-ids
    list: string
  splits:
  - name: qrel_diff
    num_examples: 20
- config_name: top_ranked
  features:
  - name: query-id
    dtype: string
  - name: corpus-ids
    list: string
  splits:
  - name: top_ranked
    num_examples: 40
- config_name: queries_zh_en
  features:
  - name: _id
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: queries
    num_examples: 40
- config_name: instructions_zh_en
  features:
  - name: query-id
    dtype: string
  - name: instruction
    dtype: string
  splits:
  - name: instruction
    num_examples: 40
- config_name: queries_ja_en
  features:
  - name: _id
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: queries
    num_examples: 40
- config_name: instructions_ja_en
  features:
  - name: query-id
    dtype: string
  - name: instruction
    dtype: string
  splits:
  - name: instruction
    num_examples: 40
- config_name: queries_de_en
  features:
  - name: _id
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: queries
    num_examples: 40
- config_name: instructions_de_en
  features:
  - name: query-id
    dtype: string
  - name: instruction
    dtype: string
  splits:
  - name: instruction
    num_examples: 40
- config_name: queries_es_en
  features:
  - name: _id
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: queries
    num_examples: 40
- config_name: instructions_es_en
  features:
  - name: query-id
    dtype: string
  - name: instruction
    dtype: string
  splits:
  - name: instruction
    num_examples: 40
- config_name: queries_ko_en
  features:
  - name: _id
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: queries
    num_examples: 40
- config_name: instructions_ko_en
  features:
  - name: query-id
    dtype: string
  - name: instruction
    dtype: string
  splits:
  - name: instruction
    num_examples: 40
- config_name: queries_fr_en
  features:
  - name: _id
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: queries
    num_examples: 40
- config_name: instructions_fr_en
  features:
  - name: query-id
    dtype: string
  - name: instruction
    dtype: string
  splits:
  - name: instruction
    num_examples: 40
- config_name: queries_it_en
  features:
  - name: _id
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: queries
    num_examples: 40
- config_name: instructions_it_en
  features:
  - name: query-id
    dtype: string
  - name: instruction
    dtype: string
  splits:
  - name: instruction
    num_examples: 40
- config_name: queries_pt_en
  features:
  - name: _id
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: queries
    num_examples: 40
- config_name: instructions_pt_en
  features:
  - name: query-id
    dtype: string
  - name: instruction
    dtype: string
  splits:
  - name: instruction
    num_examples: 40
- config_name: queries_nl_en
  features:
  - name: _id
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: queries
    num_examples: 40
- config_name: instructions_nl_en
  features:
  - name: query-id
    dtype: string
  - name: instruction
    dtype: string
  splits:
  - name: instruction
    num_examples: 40
license: mit
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
tags:
- text-retrieval
- instruction-retrieval
- code-switching
task_categories:
- text-retrieval
task_ids:
- document-retrieval
---

<div align="center" style="padding: 40px 20px; background-color: white; border-radius: 12px; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05); max-width: 600px; margin: 0 auto;">
  <h1 style="font-size: 3.5rem; color: #1a1a1a; margin: 0 0 20px 0; letter-spacing: 2px; font-weight: 700;">Core17 Instructions CS-MTEB</h1>
  <div style="font-size: 1.5rem; color: #4a4a4a; margin-bottom: 5px; font-weight: 300;">An <a href="https://github.com/embeddings-benchmark/mteb" style="color: #2c5282; font-weight: 600; text-decoration: none;">MTEB</a> dataset</div>
  <div style="font-size: 0.9rem; color: #2c5282; margin-top: 10px;">Massive Text Embedding Benchmark</div>
</div>

Code-switching version of [jhu-clsp/core17-instructions-mteb](https://huggingface.co/datasets/jhu-clsp/core17-instructions-mteb), with queries and instructions rewritten in Chinese-English, Japanese-English, German-English, Spanish-English, Korean-English, French-English, Italian-English, Portuguese-English, Dutch-English code-switching styles.

## Dataset Structure

The dataset contains the following configurations:

**From original dataset (unchanged):**
- `corpus`: Original corpus documents
- `default`: Original relevance judgments
- `qrel_diff`: Changes in relevance judgments
- `top_ranked`: Top ranked documents for each query

**Code-switching queries and instructions:**
- `queries_zh_en` / `instructions_zh_en`: Chinese-English
- `queries_ja_en` / `instructions_ja_en`: Japanese-English
- `queries_de_en` / `instructions_de_en`: German-English
- `queries_es_en` / `instructions_es_en`: Spanish-English
- `queries_ko_en` / `instructions_ko_en`: Korean-English
- `queries_fr_en` / `instructions_fr_en`: French-English
- `queries_it_en` / `instructions_it_en`: Italian-English
- `queries_pt_en` / `instructions_pt_en`: Portuguese-English
- `queries_nl_en` / `instructions_nl_en`: Dutch-English

## Usage

```python
from datasets import load_dataset

# Load code-switching queries and instructions
queries_zh = load_dataset("UTokyo-Yokoya-Lab/core17-instructions-mteb_CS-MTEB", "queries_zh_en")
instructions_zh = load_dataset("UTokyo-Yokoya-Lab/core17-instructions-mteb_CS-MTEB", "instructions_zh_en")
queries_ja = load_dataset("UTokyo-Yokoya-Lab/core17-instructions-mteb_CS-MTEB", "queries_ja_en")
instructions_ja = load_dataset("UTokyo-Yokoya-Lab/core17-instructions-mteb_CS-MTEB", "instructions_ja_en")
queries_de = load_dataset("UTokyo-Yokoya-Lab/core17-instructions-mteb_CS-MTEB", "queries_de_en")
instructions_de = load_dataset("UTokyo-Yokoya-Lab/core17-instructions-mteb_CS-MTEB", "instructions_de_en")
queries_es = load_dataset("UTokyo-Yokoya-Lab/core17-instructions-mteb_CS-MTEB", "queries_es_en")
instructions_es = load_dataset("UTokyo-Yokoya-Lab/core17-instructions-mteb_CS-MTEB", "instructions_es_en")
queries_ko = load_dataset("UTokyo-Yokoya-Lab/core17-instructions-mteb_CS-MTEB", "queries_ko_en")
instructions_ko = load_dataset("UTokyo-Yokoya-Lab/core17-instructions-mteb_CS-MTEB", "instructions_ko_en")
queries_fr = load_dataset("UTokyo-Yokoya-Lab/core17-instructions-mteb_CS-MTEB", "queries_fr_en")
instructions_fr = load_dataset("UTokyo-Yokoya-Lab/core17-instructions-mteb_CS-MTEB", "instructions_fr_en")
queries_it = load_dataset("UTokyo-Yokoya-Lab/core17-instructions-mteb_CS-MTEB", "queries_it_en")
instructions_it = load_dataset("UTokyo-Yokoya-Lab/core17-instructions-mteb_CS-MTEB", "instructions_it_en")
queries_pt = load_dataset("UTokyo-Yokoya-Lab/core17-instructions-mteb_CS-MTEB", "queries_pt_en")
instructions_pt = load_dataset("UTokyo-Yokoya-Lab/core17-instructions-mteb_CS-MTEB", "instructions_pt_en")
queries_nl = load_dataset("UTokyo-Yokoya-Lab/core17-instructions-mteb_CS-MTEB", "queries_nl_en")
instructions_nl = load_dataset("UTokyo-Yokoya-Lab/core17-instructions-mteb_CS-MTEB", "instructions_nl_en")

# Load original configs
corpus = load_dataset("UTokyo-Yokoya-Lab/core17-instructions-mteb_CS-MTEB", "corpus")
qrels = load_dataset("UTokyo-Yokoya-Lab/core17-instructions-mteb_CS-MTEB", "default")
```

## Attribution
Based on [jhu-clsp/core17-instructions-mteb](https://huggingface.co/datasets/jhu-clsp/core17-instructions-mteb) (MIT License).

## Citation
If you use this dataset, please also cite the original:

```bibtex
@misc{weller2024followir,
  archiveprefix = {arXiv},
  author = {Orion Weller and Benjamin Chang and Sean MacAvaney and Kyle Lo and Arman Cohan and Benjamin Van Durme and Dawn Lawrie and Luca Soldaini},
  eprint = {2403.15246},
  primaryclass = {cs.IR},
  title = {FollowIR: Evaluating and Teaching Information Retrieval Models to Follow Instructions},
  year = {2024},
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
