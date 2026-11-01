---
language:
- en
- ko
license: cc-by-nc-4.0
size_categories:
- 1M<n<10M
task_categories:
- text-retrieval
- question-answering
pretty_name: GraFine ACL-OCL and LACD Corpus Graphs
tags:
- graph-rag
- corpus-graph
- legal
- scientific-papers
configs:
- config_name: lacd_corpus
  default: true
  data_files: data/LACD/dataset/corpus.jsonl
- config_name: lacd_queries
  data_files: data/LACD/dataset/queries.jsonl
- config_name: lacd_nodes
  data_files: data/LACD/rag_storage/nodes.jsonl
- config_name: acl_queries
  data_files: data/acl/dataset/queries.jsonl
- config_name: acl_nodes
  data_files: data/acl/rag_storage/nodes.jsonl
---

# GraFine ACL-OCL and LACD Corpus Graphs

**Paper:** [GraFine: Retrieval-Time Refinement for Efficient Graph RAG over Corpus Graphs](https://huggingface.co/papers/2601.18579)  
**Code:** [https://github.com/asmath472/GraFine](https://github.com/asmath472/GraFine)

This repository contains retrieval queries and corpus-graph files used with
GraFine experiments on ACL-OCL and LACD. The graph storage directories are
intentionally limited to `nodes.jsonl` and `edges.jsonl`.

## Repository structure

```text
data/
├── acl/
│   ├── dataset/
│   │   ├── queries.jsonl
│   │   └── query_load.py
│   └── rag_storage/
│       ├── nodes.jsonl
│       └── edges.jsonl
└── LACD/
    ├── dataset/
    │   ├── corpus.jsonl
    │   ├── queries.jsonl
    │   └── qrels/test.tsv
    └── rag_storage/
        ├── nodes.jsonl
        └── edges.jsonl
```

## Loading

Each object-shaped JSONL schema is exposed as an independent Hugging Face dataset config:

```python
import json

import pandas as pd
from datasets import load_dataset
from huggingface_hub import hf_hub_download

repo_id = "OWNER/REPO"
lacd = load_dataset(repo_id, "lacd_corpus")
acl_graph = load_dataset(repo_id, "acl_nodes")

# qrels is kept in its original headerless TSV format.
qrels_path = hf_hub_download(
    repo_id,
    "data/LACD/dataset/qrels/test.tsv",
    repo_type="dataset",
)
qrels = pd.read_csv(
    qrels_path, sep="\t", names=["query_id", "corpus_id", "score"]
)

# Each edge row is a two-element JSON array: [source, target].
edges_path = hf_hub_download(
    repo_id,
    "data/acl/rag_storage/edges.jsonl",
    repo_type="dataset",
)
with open(edges_path, encoding="utf-8") as edges_file:
    source, target = json.loads(next(edges_file))
```

Available configs are `lacd_corpus`, `lacd_queries`, `lacd_nodes`,
`acl_queries`, and `acl_nodes`. The qrels and edge files remain downloadable raw
files. They are not declared as configs because the no-code loader cannot mix
the JSON and CSV/TSV packaged builders or interpret a JSONL row whose top level
is an array.

## Sources and attribution

The ACL portion is derived from
[WINGNUS/ACL-OCL](https://huggingface.co/datasets/WINGNUS/ACL-OCL), which in
turn uses ACL Anthology and Semantic Scholar material. Cite the ACL-OCL corpus
when using this portion:

```bibtex
@inproceedings{rohatgi-etal-2023-acl,
    title = "The {ACL} {OCL} Corpus: Advancing Open Science in Computational Linguistics",
    author = "Rohatgi, Shaurya  and
      Qin, Yanxia  and
      Aw, Benjamin  and
      Unnithan, Niranjana  and
      Kan, Min-Yen",
    editor = "Bouamor, Houda  and
      Pino, Juan  and
      Bali, Kalika",
    booktitle = "Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing",
    month = dec,
    year = "2023",
    address = "Singapore",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.emnlp-main.640/",
    doi = "10.18653/v1/2023.emnlp-main.640",
    pages = "10348--10361",
    abstract = "We present ACL OCL, a scholarly corpus derived from the ACL Anthology to assist Open scientific research in the Computational Linguistics domain. Integrating and enhancing the previous versions of the ACL Anthology, the ACL OCL contributes metadata, PDF files, citation graphs and additional structured full texts with sections, figures, and links to a large knowledge resource (Semantic Scholar). The ACL OCL spans seven decades, containing 73K papers, alongside 210K figures. We spotlight how ACL OCL applies to observe trends in computational linguistics. By detecting paper topics with a supervised neural model, we note that interest in ``Syntax: Tagging, Chunking and Parsing'' is waning and ``Natural Language Generation'' is resurging. Our dataset is available from HuggingFace (\url{https://huggingface.co/datasets/WINGNUS/ACL-OCL})."
}
```

The LACD portion is associated with the following work:

```bibtex
@inproceedings{an-etal-2025-grex,
    title = "{GR}e{X}: A Graph Neural Network-Based Rerank-then-Expand Method for Detecting Conflicts Among Legal Articles in {K}orean Criminal Law",
    author = "An, Seonho  and
      Rhim, Young-Yik  and
      Kim, Min-Soo",
    editor = "Aletras, Nikolaos  and
      Chalkidis, Ilias  and
      Barrett, Leslie  and
      Goanț{\u{a}}, C{\u{a}}t{\u{a}}lina  and
      Preoțiuc-Pietro, Daniel  and
      Spanakis, Gerasimos",
    booktitle = "Proceedings of the Natural Legal Language Processing Workshop 2025",
    month = nov,
    year = "2025",
    address = "Suzhou, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.nllp-1.30/",
    doi = "10.18653/v1/2025.nllp-1.30",
    pages = "408--423",
    ISBN = "979-8-89176-338-8",
    abstract = "As social systems become more complex, legal articles have grown increasingly intricate, making it harder for humans to identify potential conflicts among them, particularly when drafting new laws or applying existing ones. Despite its importance, no method has been proposed to detect such conflicts. We introduce a new legal NLP task, Legal Article Conflict Detection (LACD), which aims to identify conflicting articles within a given body of law. To address this task, we propose GReX, a novel graph neural network-based retrieval method. Experimental results show that GReX significantly outperforms existing methods, achieving improvements of 44.8{\%} in nDCG@50, 32.8{\%} in Recall@50, and 39.8{\%} in Retrieval F1@50. Our codes are in github.com/asmath472/LACD-public."
}
```

Also cite the GraFine paper associated with the processed graph files once
its final citation is available.

## License

This distribution is made available under the
[Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/)
(CC BY-NC 4.0). See [`LICENSE`](LICENSE).

The ACL-OCL dataset card's licensing section states that ACL-OCL is released
under CC BY-NC 4.0.