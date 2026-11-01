---
pretty_name: docx-corpus (mirror of superdoc-dev/docx-corpus)
license: odc-by
task_categories:
  - text-classification
language:
  - en
  - ru
  - cs
  - pl
  - es
  - zh
  - lt
  - sk
  - fr
  - pt
  - de
  - it
  - sv
  - nl
  - bg
  - uk
  - tr
  - ja
  - hu
  - ko
  - multilingual
size_categories:
  - 100K<n<1M
source_datasets:
  - superdoc-dev/docx-corpus
tags:
  - docx
  - word-documents
  - document-classification
  - ooxml
  - legal
configs:
  - config_name: default
    default: true
    data_files:
      - split: train
        path: data/train-00000-of-00001.parquet
---

# docx-corpus

The largest classified corpus of Word documents. 736K+ `.docx` files from the public web, classified into
10 document types and 9 topics across 76 languages. This repo is an unmodified duplicate of
[superdoc-dev/docx-corpus](https://huggingface.co/datasets/superdoc-dev/docx-corpus) (duplicated
2026-04-04; same 63.6 MB Parquet file, 736,706 rows), kept here as the input corpus for the
legal-documents / DOCX tooling below.

## Related repos

| Repo | Type | Role |
|---|---|---|
| [superdoc-dev/docx-corpus](https://huggingface.co/datasets/superdoc-dev/docx-corpus) | dataset | **Upstream** — the original release by SuperDoc |
| [arthrod/docx-corpus](https://huggingface.co/datasets/arthrod/docx-corpus) | dataset | **This repo** — mirror |
| [arthrod/neurotic_docx_bench](https://huggingface.co/datasets/arthrod/neurotic_docx_bench) | dataset | DOCX rendering / redline benchmark built on documents from docx-corpus |
| [arthrod/neurotic_docx_bench-fixtures](https://huggingface.co/datasets/arthrod/neurotic_docx_bench-fixtures) | dataset | Source DOCX files and Word reference renders for neurotic_docx_bench |
| [arthrod/sec-ex10-exhibits](https://huggingface.co/datasets/arthrod/sec-ex10-exhibits) | dataset | SEC EX-10 material contracts as Markdown (live-contracts.arthur.law export) |
| [arthrod/sec-ex10-api](https://huggingface.co/spaces/arthrod/sec-ex10-api) | Space | Listener + API that maintains sec-ex10-exhibits |
| [arthrod/contract_parse](https://huggingface.co/datasets/arthrod/contract_parse) | dataset | Clause-hierarchy parser runs over 1,066 SEC EX-10 agreements |
| [arthrod/md-templates](https://huggingface.co/datasets/arthrod/md-templates) | dataset | PT-BR legal petition templates (rough Markdown + LLM templatization) |
| [arthrod/contractscrub-repro](https://huggingface.co/datasets/arthrod/contractscrub-repro) | dataset | ContractScrub-style synthetic contract-review benchmark (unofficial) |
| [arthrod/contractscrub-repro-trackio](https://huggingface.co/spaces/arthrod/contractscrub-repro-trackio) | Space | Trackio dashboard for contractscrub-repro |
| [arthrod/contracts_clauses_config_space](https://huggingface.co/spaces/arthrod/contracts_clauses_config_space) | Space | Streamlit app (domain-specific seed / clause config) |

## Configs & splits

| Config | Split | Rows | Description |
|---|---|---|---|
| `default` | `train` | 736,706 | One row per `.docx` file: classification labels + download URL |

## Dataset Description

This dataset contains metadata for publicly available `.docx` files collected from the web. Each document
has been classified by document type and topic using a two-stage pipeline: LLM labeling (Claude) of a
stratified sample, followed by fine-tuned XLM-RoBERTa classifiers applied at scale. The files themselves are
not in this repo; each row links to the file on the upstream CDN (`docxcorp.us`).

### Schema

| Column | Type | Description |
|--------|------|-------------|
| `id` | string | SHA-256 hash of the file (unique identifier) |
| `filename` | string | Original filename from the source URL |
| `type` | string | Document type (10 classes) |
| `topic` | string | Document topic (9 classes) |
| `language` | string | Detected language (ISO 639-1 code; 76 values incl. `unknown`) |
| `word_count` | int32 | Number of words in the document |
| `confidence` | float32 | Classification confidence (min of type and topic) |
| `url` | string | Direct download URL for the `.docx` file |

### Document Types

legal, forms, reports, policies, educational, correspondence, technical, administrative, creative, reference

Counts in this file: legal 179,823 · forms 165,574 · educational 88,700 · administrative 88,101 ·
policies 60,186 · correspondence 51,341 · reports 41,571 · reference 32,566 · technical 15,682 · creative 13,162.

### Topics

government, education, healthcare, finance, legal_judicial, technology, environment, nonprofit, general

Counts in this file: government 244,915 · education 184,040 · healthcare 64,501 · general 59,949 ·
legal_judicial 55,250 · finance 49,207 · environment 29,887 · nonprofit 26,619 · technology 22,338.

### Languages

Top languages: en 245,256 · ru 58,065 · cs 50,709 · pl 38,546 · es 36,473 · zh 35,032 · lt 34,743 ·
sk 25,873 · fr 25,692 · pt 22,505 · de 17,780 · it 15,523 (76 codes in total; 4,606 rows are `unknown`).

## Examples

```json
[
  {"id": "000014a959f5225c658740fd7915cd50c5728c9cbe06c7d72d79a9708244ec1f", "filename": "document.do",
   "type": "legal", "topic": "legal_judicial", "language": "fr", "word_count": 671, "confidence": 0.9814,
   "url": "https://docxcorp.us/documents/000014a959f5225c658740fd7915cd50c5728c9cbe06c7d72d79a9708244ec1f.docx"},
  {"id": "00003fff80a444ad2f706c74f3c0d9fbef00d7a99ba0c105e7baa0574df63393", "filename": "content",
   "type": "educational", "topic": "education", "language": "es", "word_count": 1846, "confidence": 0.9581,
   "url": "https://docxcorp.us/documents/00003fff80a444ad2f706c74f3c0d9fbef00d7a99ba0c105e7baa0574df63393.docx"},
  {"id": "000041165f84371051941c911c16b94b69ed46cc56a08995afd9dcf93113587f", "filename": "index.php",
   "type": "administrative", "topic": "government", "language": "ru", "word_count": 145, "confidence": 0.7072,
   "url": "https://docxcorp.us/documents/000041165f84371051941c911c16b94b69ed46cc56a08995afd9dcf93113587f.docx"}
]
```

## How it was built

Built upstream by [SuperDoc](https://superdoc.dev) ([superdoc-dev/docx-corpus](https://github.com/superdoc-dev/docx-corpus)):
crawl of public-web `.docx` files, SHA-256 dedup, LLM labeling of a stratified sample, then fine-tuned
XLM-RoBERTa type/topic classifiers over the full set. This mirror was created with the Hub's
"Duplicate from superdoc-dev/docx-corpus" action on 2026-04-04 and has not been modified since (only this
card was extended on 2026-10-10).

## Usage — download files

Each row includes a `url` column pointing to the `.docx` file on the upstream CDN. You can download files directly:

```python
from datasets import load_dataset
import requests

ds = load_dataset("arthrod/docx-corpus", split="train")   # or "superdoc-dev/docx-corpus"

# Filter and download
legal_en = ds.filter(lambda x: x["type"] == "legal" and x["language"] == "en")
for row in legal_en:
    resp = requests.get(row["url"])
    with open(f"corpus/{row['id']}.docx", "wb") as f:
        f.write(resp.content)
```

Or use the upstream manifest API for bulk downloads:

```bash
curl "https://api.docxcorp.us/manifest?type=legal&lang=en" -o manifest.txt
wget -i manifest.txt -P ./corpus/
```

## Limitations

- Labels are model predictions (`confidence` ranges 0.13–0.99); filter on `confidence` for cleaner subsets.
- `filename` is whatever the source URL ended with (`content`, `index.php`, `document.do`, …), not a title.
- Downloads depend on the upstream CDN (`docxcorp.us`); this repo does not host the `.docx` files.
- The mirror is a point-in-time copy; check the upstream repo for newer releases.
- The files are arbitrary public-web documents and may contain personal data; the corpus is metadata only.

## License & attribution

ODC-By, as released by SuperDoc. Attribute the upstream:

- **Website**: [docxcorp.us](https://docxcorp.us)
- **GitHub**: [superdoc-dev/docx-corpus](https://github.com/superdoc-dev/docx-corpus)
- **Built by**: [SuperDoc](https://superdoc.dev)
