---
dataset_info:
- config_name: corpus
  features:
  - name: corpus-id
    dtype: int64
  - name: image
    dtype: image
  - name: doc-id
    dtype: string
  splits:
  - name: test
    num_bytes: 2847152161
    num_examples: 5873
  download_size: 2525192800
  dataset_size: 2847152161
- config_name: qrels
  features:
  - name: query-id
    dtype: int64
  - name: corpus-id
    dtype: int64
  - name: is-answerable
    dtype: string
  - name: answer
    dtype: string
  - name: score
    dtype: int64
  splits:
  - name: test
    num_bytes: 150816
    num_examples: 3142
  download_size: 27588
  dataset_size: 150816
- config_name: queries
  features:
  - name: query-id
    dtype: int64
  - name: query
    dtype: string
  - name: language
    dtype: string
  - name: gpt-4o-reasoning
    dtype: string
  - name: answer
    dtype: string
  splits:
  - name: test
    num_bytes: 403924
    num_examples: 1000
  download_size: 257024
  dataset_size: 403924
configs:
- config_name: corpus
  data_files:
  - split: test
    path: corpus/test-*
- config_name: qrels
  data_files:
  - split: test
    path: qrels/test-*
- config_name: queries
  data_files:
  - split: test
    path: queries/test-*
language:
- en
- bn
- de
- es
- fr
- hi
- it
- kn
- mr
- ml
- or
- pa
- te
- ta
- sa
- gu
- th
- zh
- ja
- ko
---

# NayanaIR-CrossBench

![M3DR Overview](https://cdn-uploads.huggingface.co/production/uploads/6442d975ad54813badc1ddf7/-fYMikXhSuqRqm-UIdulK.png)

[![Paper](https://img.shields.io/badge/arXiv-2512.03514-b31b1b.svg)](https://arxiv.org/abs/2512.03514)
[![GitHub](https://img.shields.io/badge/GitHub-CognitiveLab-181717?logo=github)](https://github.com/adithya-s-k/colpali)
[![Website](https://img.shields.io/badge/Website-CognitiveLab-blue)](https://www.cognitivelab.in)

**NayanaIR-CrossBench** is a comprehensive multilingual multimodal document retrieval benchmark designed to evaluate **cross-lingual** visual search capabilities. It is part of the **M3DR (Multilingual Multimodal Document Retrieval)** framework.

This dataset challenges models to retrieve documents in *any* language given queries in *any* language, evaluating the ability to map diverse scripts and languages into a unified semantic space.

## Dataset Details

- **Curator:** [CognitiveLab](https://huggingface.co/Cognitive-Lab)
- **Languages:** 20 typologically diverse languages (Latin, Devanagari, Dravidian, CJK, Arabic, etc.)
- **Format:** BEIR-compatible (Images + Queries + Qrels)
- **Paper:** [M3DR: Towards Universal Multilingual Multimodal Document Retrieval](https://arxiv.org/abs/2512.03514)

### Languages Covered
| Family | Languages |
|--------|-----------|
| **Latin** | English, Spanish, French, German, Italian |
| **Devanagari** | Hindi, Marathi, Sanskrit |
| **Dravidian** | Kannada, Telugu, Tamil, Malayalam |
| **CJK** | Chinese, Japanese, Korean |
| **Others** | Bengali, Gujarati, Odia, Punjabi, Thai |

## Statistics

The Cross-Lingual benchmark consists of a parallel corpus where semantically equivalent documents exist across languages.

- **Documents:** 5,870 parallel document images (spanning 20 languages).
- **Queries:** 1,000 queries distributed uniformly (~50 per language).
- **Task:** Retrieve the correct visual document regardless of the query language or document language.
- **Relevance:** Binary relevance (Score 2: Exact match / Score 0: Non-relevant).

## Dataset Construction

This dataset was generated using the **M3DR synthetic pipeline**:
1.  **Source:** 50k diverse English document images (scientific papers, reports, forms) from datasets like SafeDocs.
2.  **Layout-Aware Translation:** Using DocLayout-YOLO and NLLB-200 to translate text while preserving visual layout.
3.  **Rendering:** High-resolution rendering using various fonts for multiple script coverage.
4.  **Query Synthesis:** Generated using Llama 3.1 90B Vision and Llama 4 Scout, covering factual questions, cross-paragraph reasoning, and keyword search.

## Usage

This dataset follows the standard BEIR format. You can use it with the `colpali_engine` or standard retrieval evaluation scripts.

```python
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("Cognitive-Lab/NayanaIR-CrossBench", 'corpus', split="test")

# Example structure
print(dataset[0])
# {
#   "corpus-id": int,
#   "image": <PIL.Image>,
#   "doc-id": str,
#   ...
# }
```

## Evaluation Metrics

As per the M3DR paper, the recommended metrics for this benchmark are:
- **NDCG@5** (Primary)
- Recall@10
- MAP@10
- MRR@10

## Citation

If you use this dataset, please cite the following paper:

```bibtex
@misc{kolavi2025m3druniversalmultilingualmultimodal,
  title={M3DR: Towards Universal Multilingual Multimodal Document Retrieval}, 
  author={Adithya S Kolavi and Vyoman Jain},
  year={2025},
  eprint={2512.03514},
  archivePrefix={arXiv},
  primaryClass={cs.IR},
  url={https://arxiv.org/abs/2512.03514}
}
```

## Acknowledgments

Dataset curation and synthesis were supported by the **Meta LLaMA Impact Grant** through the Nayana initiative. We appreciate Meta for continued support of our research efforts at CognitiveLab.