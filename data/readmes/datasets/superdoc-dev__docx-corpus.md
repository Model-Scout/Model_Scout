---
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
size_categories:
  - 100K<n<1M
tags:
  - docx
  - word-documents
  - document-classification
  - ooxml
pretty_name: docx-corpus
---

# docx-corpus

The largest classified corpus of Word documents. 736K+ `.docx` files from the public web, classified into 10 document types and 9 topics across 76 languages.

## Dataset Description

This dataset contains metadata for publicly available `.docx` files collected from the web. Each document has been classified by document type and topic using a two-stage pipeline: LLM labeling (Claude) of a stratified sample, followed by fine-tuned XLM-RoBERTa classifiers applied at scale.

### Schema

| Column | Type | Description |
|--------|------|-------------|
| `id` | string | SHA-256 hash of the file (unique identifier) |
| `filename` | string | Original filename from the source URL |
| `type` | string | Document type (10 classes) |
| `topic` | string | Document topic (9 classes) |
| `language` | string | Detected language (ISO 639-1 code) |
| `word_count` | int | Number of words in the document |
| `confidence` | float | Classification confidence (min of type and topic) |
| `url` | string | Direct download URL for the `.docx` file |

### Document Types

legal, forms, reports, policies, educational, correspondence, technical, administrative, creative, reference

### Topics

government, education, healthcare, finance, legal_judicial, technology, environment, nonprofit, general

## Download Files

Each row includes a `url` column pointing to the `.docx` file on our CDN. You can download files directly:

```python
from datasets import load_dataset
import requests

ds = load_dataset("superdoc-dev/docx-corpus", split="train")

# Filter and download
legal_en = ds.filter(lambda x: x["type"] == "legal" and x["language"] == "en")
for row in legal_en:
    resp = requests.get(row["url"])
    with open(f"corpus/{row['id']}.docx", "wb") as f:
        f.write(resp.content)
```

Or use the manifest API for bulk downloads:

```bash
curl "https://api.docxcorp.us/manifest?type=legal&lang=en" -o manifest.txt
wget -i manifest.txt -P ./corpus/
```

## Links

- **Website**: [docxcorp.us](https://docxcorp.us)
- **GitHub**: [superdoc-dev/docx-corpus](https://github.com/superdoc-dev/docx-corpus)
- **Built by**: [🦋 SuperDoc](https://superdoc.dev)
