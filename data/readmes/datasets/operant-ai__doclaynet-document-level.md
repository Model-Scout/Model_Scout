---
license: other
license_name: cdla-permissive-1.0
license_link: https://cdla.io/permissive-1-0/
pretty_name: DocLayNet Document-Level Reconstruction
language:
  - en
  - de
  - ru
  - zh
  - ja
  - ko
tags:
  - document-ai
  - document-layout-analysis
  - doclaynet
  - parquet
configs:
  - config_name: default
    data_files:
      - split: train
        path: train.parquet
      - split: validation
        path: val.parquet
      - split: test
        path: test.parquet
  - config_name: expanded
    data_files:
      - split: train
        path: expanded/train.parquet
      - split: validation
        path: expanded/validation.parquet
      - split: test
        path: expanded/test.parquet
---

# DocLayNet Document-Level Reconstruction and 8K Expansion

This dataset is a normalized, one-row-per-document view over the page-level
[DocLayNet v1.1](https://huggingface.co/datasets/docling-project/DocLayNet-v1.1)
dataset. Pages are grouped using DocLayNet's source metadata and ordered by their original
page number.

## Dataset summary

- 2,944 logical documents
- 80,863 observed pages
- 896 complete document groups
- 2,048 partial document groups
- Train: 2,355 documents / 60,810 pages
- Validation: 294 documents / 7,964 pages
- Test: 295 documents / 12,089 pages

## Curated, materialized expansion

The `expanded` config contains 7,086 curated logical documents with a deterministic,
family-safe split:

- Train: 6,381 documents
- Validation: 353 documents
- Test: 352 documents

It combines reconstructed DocLayNet documents with clinical protocols, historical
newspapers, charity reports, court decisions, synthetic financial and PII documents,
receipts, insurance documents, and NIST tax submissions.

Every retained `expanded` row has its complete extracted text embedded in the `text`
column and uses `content_mode="embedded_text"`. Loading or evaluating this config does
not require downloading source PDFs, ZIP archives, or upstream DocLayNet parquet rows.
Canonical source URLs, record IDs, license metadata, capture type, synthetic status,
family IDs, `page_references_json`, and `metadata_json` remain available for provenance.
Large source binaries and page images are not mirrored.

Load the expansion explicitly:

```python
from datasets import load_dataset

documents = load_dataset(
    "operant-ai/doclaynet-document-level",
    "expanded",
)
```

The row-level `split` field retains the upstream split for provenance; it does not denote
the output parquet file.

The document key is:

```text
(split, original_filename, doc_category, collection)
```

This repository intentionally does not duplicate DocLayNet's approximately 30 GB of page
images and annotations. Every entry in the nested `pages` field contains `source_file` and
`source_row`, which identify the original page row in
`docling-project/DocLayNet-v1.1`.

## Schema

Each row contains:

- `document_id`: stable SHA-256-derived identifier;
- `split`, `original_filename`, `doc_category`, and `collection`;
- `num_pages_in_original` and `num_pages_present`;
- `coverage_ratio` and `is_complete`;
- ordered `pages_present` and `missing_pages`;
- `pages`: ordered page metadata containing page number, page hash, image ID, dimensions,
  source parquet path, and zero-based source row.

## Load

```python
from datasets import load_dataset

documents = load_dataset("operant-ai/doclaynet-document-level")
document = documents["train"][0]
print(document["original_filename"], document["pages_present"])
```

To dereference an original page:

```python
import pyarrow.parquet as pq
from huggingface_hub import hf_hub_download

page = document["pages"][0]
source_path = hf_hub_download(
    repo_id="docling-project/DocLayNet-v1.1",
    repo_type="dataset",
    filename=page["source_file"],
)
source_page = pq.read_table(source_path).slice(page["source_row"], 1)
```

## Document categories

The six `doc_category` values are copied from DocLayNet metadata rather than inferred:

- `scientific_articles`
- `laws_and_regulations`
- `patents`
- `financial_reports`
- `government_tenders`
- `manuals`

The expanded config uses `document_category` as its classification label. Its 14-label
distribution is:

- `medical_and_clinical`: 1,180
- `nonprofit_and_public_admin`: 496
- `scientific_articles`: 978
- `news_and_periodicals`: 600
- `laws_and_regulations`: 1,044
- `contracts_and_agreements`: 74
- `patents`: 498
- `financial_reports`: 647
- `synthetic_sensitive`: 20
- `insurance`: 336
- `invoices_and_receipts`: 430
- `forms_and_applications`: 347
- `government_tenders`: 269
- `manuals`: 167

## Length statistics

`length_histograms.json` contains corpus-level page and text-token length distributions.
Token counts use `google/gemma-4-E4B-it` over text reconstructed from `pdf_cells`, with
pages joined in `page_no` order. BOS/EOS tokens and chat templates are excluded.

## Limitations

- This is a logical reconstruction, not a set of rebuilt source PDFs.
- 69.6% of document groups are partial because DocLayNet does not contain every original
  page for those documents.
- The default config's page pointers require the upstream DocLayNet v1.1 dataset; the
  expanded config embeds its text and does not.
- Categories and collections are inherited source metadata and may be broader than their
  names suggest.
- Extracted text can contain reading-order, OCR, formula, and multilingual character noise.
- Source licenses differ. Review `source_license`, `redistribution_allowed`, and the
  upstream terms before redistributing source binaries.

## License and attribution

The source dataset is released under
[CDLA-Permissive-1.0](https://cdla.io/permissive-1-0/). Users should review and comply
with the upstream [DocLayNet dataset card](https://huggingface.co/datasets/docling-project/DocLayNet-v1.1).

The expanded config also includes CC0, CC BY 4.0, Apache 2.0, Open Government
Licence 3.0, NIST public-reference-data, and public-domain sources. Per-record provenance
is authoritative for the applicable terms.
