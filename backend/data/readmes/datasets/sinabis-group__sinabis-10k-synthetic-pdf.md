---
license: cc-by-4.0
language:
  - en
  - zh
  - ja
  - de
  - es
  - it
  - pt
  - fr
  - sv
  - pl
  - nl
  - ko
  - hu
  - nb
  - da
  - vi
  - el
  - id
  - tr
  - fi
  - cs
  - uk
  - ro
  - ru
task_categories:
  - text-generation
  - text-classification
  - summarization
  - token-classification
  - feature-extraction
language_creators:
  - machine-generated
multilinguality:
  - multilingual
source_datasets:
  - original
tags:
  - synthetic
  - synthetic-data
  - pdf
  - documents
  - business-documents
  - invoice
  - financial-records
  - digital-forensics
  - forensics
  - e-discovery
  - renewable-energy
  - enterprise
  - business
  - multilingual
  - llm
  - llm-training
  - pretraining
  - nlp
  - information-extraction
  - ocr
  - document-understanding
  - multimodal
size_categories:
  - 10K<n<100K
configs:
  - config_name: default
    data_files:
      - split: train
        path: "data/train-*.parquet"
---

# Sinabis Green Energy – Synthetic Document Dataset (10k PDFs)

**10,100 business documents (PDF)** from the everyday operations
of a fictional renewable-energy group (**Sinabis Green Energy**) and its worldwide
ecosystem of customers, suppliers, subcontractors, utilities, authorities, insurers,
banks, hotels and service providers.

This is the 10k edition of [sinabis-1m-synthetic-pdf](https://huggingface.co/datasets/sinabis-group/sinabis-1m-synthetic-pdf):
the first 10,100 documents of the 1M dataset (`idx` 0 to 10,099). File names, folder paths and manifest
records are identical to the 1M dataset, and this edition is the first part of the [100k edition](https://huggingface.co/datasets/sinabis-group/sinabis-100k-synthetic-pdf),
so all editions can be used side by side.

Every person, company, address, phone number, bank account, tax number, invoice and
transaction in this dataset is **purely fictional**. The underlying world and business
taxonomy were created with LLM assistance, while all documents, calculations,
serial numbers, dates and visual company designs were rendered deterministically
using ReportLab and custom vector engines.

> All figures in this dataset card were **computed directly from the files in this edition**
> (as of 23 Oct 2026). They are not target estimates.

## At a glance

| Metric | Value |
|---|---|
| Total Documents | **10,100** PDFs (717 MB uncompressed, 655 MB in 1 ZIP archive) |
| Document Types | **20** distinct business themes (invoices, receipts, payslips, bank statements, certificates ...) |
| Vector vs. Scanned | **6,498** clean vector PDFs (64.3 %) · **3,602** scanned/photocopied (35.7 %) with stamps, handwritten notes, skew and sensor noise |
| Time span | **2014-08-28** to **2026-06-30** (11.8 years of continuous commercial history) |
| Languages | **24** languages (EN 82.4 %, ZH 4.7 %, rest across 22 languages) |
| Issuing Companies | **1,746** distinct fictional companies across **33** countries |

## Quick start

The Parquet file under `data/` holds one row per document: all manifest fields plus the extracted
text, so the dataset can be browsed in the Dataset Viewer above and loaded directly:

```python
from datasets import load_dataset

ds = load_dataset("sinabis-group/sinabis-10k-synthetic-pdf", split="train")
print(ds[0]["theme"], ds[0]["number"], ds[0]["total"], ds[0]["currency"])
print(ds[0]["text"])

vector = ds.filter(lambda r: not r["scanned"])   # documents with a text layer
```

The `text` column holds the text layer of the PDF, page by page; `pages` is the page count. The scanned/photocopied documents (`scanned == True`) are images without a text layer, so their `text` is empty: they are meant for OCR and vision models. The original PDFs are in the ZIP archive.

## Downloads

| File | Size | Contents |
|---|---:|---|
| `data/train-*.parquet` (1 file) | 5 MB | Manifest fields + extracted `text`, one row per document (Dataset Viewer, `load_dataset`) |
| `Sinabis_10k_pdfs.zip` | 655 MB | `10,100` PDFs + manifest (717 MB uncompressed) |
| `Sinabis_10k_pdfs_manifest.zip` | 0.8 MB | Dataset index only: 10,100 JSONL records with file paths, metadata and sums |

### Unpacking

Both archives share one directory structure. The PDF archive already contains the manifest, so
`unzip -o` simply overwrites identical files:

```bash
# Download and unpack with the Hugging Face CLI
hf download sinabis-group/sinabis-10k-synthetic-pdf --repo-type dataset --local-dir sinabis-10k-pdf
cd sinabis-10k-pdf
for z in Sinabis_10k_pdfs*.zip; do unzip -qo "$z"; done
```

## Folder structure

In the repository:

```
.
├── README.md
├── data/
│   └── train-*.parquet                 (rows for the Dataset Viewer and load_dataset)
├── Sinabis_10k_pdfs.zip             → pdf/ + manifest/
└── Sinabis_10k_pdfs_manifest.zip    → manifest/
```

After unpacking:

```
sinabis-10k-pdf/
├── README.md
├── pdf/
│   ├── invoice/
│   │   ├── 0000/
│   │   │   ├── 0000xxx_<document-number>.pdf
│   │   │   └── ...
│   │   └── ... (0000 to 0010)
│   ├── payslip/
│   ├── utility_bill/
│   └── ... (20 themes)
└── manifest/
    ├── b00000.jsonl
    ├── ...
    └── b00020.jsonl
```

Each `bNNNNN.jsonl` contains 500 records (the last shard 100), one per document:
- `idx`: Running document number (same as in the 1M dataset)
- `file`: Relative path to the PDF
- `theme`: Document theme (e.g. `invoice`, `payslip`)
- `issuer_id`: Stable ID of the fictional issuing company
- `issuer`: Fictional issuing company name
- `issuer_country`: Two-letter country code (ISO 3166-1)
- `recipient`: Recipient name
- `recipient_kind`: Recipient category (`private`, `business`, `sinabis`)
- `lang`: Language code (ISO 639-1)
- `date`: Document issue date (ISO 8601)
- `number`: Serial document number
- `currency`: ISO 4217 currency code
- `total`: Document net/gross total (recalculable from line items)
- `scanned`: Boolean flag indicating whether physical scanner simulation was applied
- `bytes`: Exact byte size

## Document Themes

| Theme | Documents | Share | Description |
|---|---:|---:|---|
| `invoice` | 2,837 | 28.1 % | Trade and service invoices with tax and early-payment discount calculations |
| `receipt` | 907 | 9.0 % | Receipts and till slips for cash and card payments |
| `quote` | 601 | 6.0 % | Commercial quotations with validity periods and payment terms |
| `payslip` | 529 | 5.2 % | Monthly payslips with deductions, taxes and social security contributions |
| `delivery_note` | 512 | 5.1 % | Delivery notes with package details and handover receipt |
| `dunning` | 413 | 4.1 % | Multi-level payment reminders with dunning fees and deadlines |
| `utility_bill` | 398 | 3.9 % | Energy and utility bills with consumption history |
| `bank_statement` | 396 | 3.9 % | Bank statements with transaction descriptions and running balances |
| `order_confirmation` | 382 | 3.8 % | Order confirmations with delivery dates |
| `certificate` | 374 | 3.7 % | Participation, training and calibration certificates with seal |
| `freight_bill` | 318 | 3.1 % | Freight and forwarding documents (CMR/AWB) with dangerous-goods notes |
| `maintenance_report` | 317 | 3.1 % | Technical maintenance and inspection reports with test points |
| `expense_report` | 312 | 3.1 % | Travel expense reports with meal allowances and receipts |
| `timesheet` | 305 | 3.0 % | Monthly timesheets with project and daywork hours |
| `authority_notice` | 302 | 3.0 % | Authority notices and fee decisions with appeal instructions |
| `hotel_invoice` | 297 | 2.9 % | Hotel invoices with tourist tax, lodging and catering |
| `workshop_invoice` | 268 | 2.7 % | Workshop invoices with labour units (AW) and spare parts |
| `credit_note` | 234 | 2.3 % | Credit notes referencing the original invoice |
| `packing_list` | 217 | 2.1 % | Detailed packing lists with weight and dimension details |
| `insurance_policy` | 181 | 1.8 % | Insurance policies with coverage amounts and clauses |

## Language Distribution

| Language | Documents | Share |
|---|---:|---:|
| English (`en`) | 8,322 | **82.4 %** |
| Chinese (`zh`) | 478 | **4.7 %** |
| Japanese (`ja`) | 432 | **4.3 %** |
| German (`de`) | 158 | **1.6 %** |
| Spanish (`es`) | 86 | **0.9 %** |
| Italian (`it`) | 83 | **0.8 %** |
| Polish (`pl`) | 60 | **0.6 %** |
| Swedish (`sv`) | 51 | **0.5 %** |
| French (`fr`) | 47 | **0.5 %** |
| Portuguese (`pt`) | 45 | **0.4 %** |
| Dutch (`nl`) | 41 | **0.4 %** |
| Danish (`da`) | 36 | **0.4 %** |
| Korean (`ko`) | 36 | **0.4 %** |
| Norwegian (`nb`) | 35 | **0.3 %** |
| Hungarian (`hu`) | 31 | **0.3 %** |
| Greek (`el`) | 29 | **0.3 %** |
| Vietnamese (`vi`) | 24 | **0.2 %** |
| Indonesian (`id`) | 22 | **0.2 %** |
| Turkish (`tr`) | 18 | **0.2 %** |
| Romanian (`ro`) | 16 | **0.2 %** |
| Finnish (`fi`) | 15 | **0.1 %** |
| Czech (`cs`) | 14 | **0.1 %** |
| Ukrainian (`uk`) | 11 | **0.1 %** |
| Russian (`ru`) | 10 | **0.1 %** |

## Visual Design-DNA

Every issuing company in the dataset possesses a deterministic visual identity derived
from its unique company ID:
- **Header Archetypes:** Full-bleed color band, clean letterhead, modern sidebar, minimalist, split-block.
- **Procedural Logos:** 20 vector geometric symbols, typography and layouts generated with exact brand rules.
- **Color Palettes:** Harmonized primary, secondary, accent and neutral tones with WCAG-compliant contrast.
- **Typography:** Tailored font pairings for the scripts used by the 24 languages (Latin, CJK, Cyrillic and Greek).
- **Physical Scan Artifacts:** About a third (35.7 %) of the documents undergo a high-resolution copier/scanner simulation
  featuring ink stamps, ballpoint pen annotations, checkmarks, paper fiber textures, tilt, and optical noise.

## Strict Fictionality Guardrails

- **Domain Names:** All external email and website domains use the RFC 2606 reserved `.example` TLD.
- **Phone Numbers:** All telephone numbers use fictional prefixes (e.g. `555-01xx` in North America).
- **Banking:** Bank names and IBANs are algorithmically generated using synthetic syllables and valid checksum algorithms.
- **Screening:** Every entity is filtered against a 5,000+ entry real-world trademark and organization blocklist (`guard.json`).

## License

This dataset is released under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.
You are free to share and adapt the material for any purpose, including commercial applications,
provided appropriate credit is given:

> Sinabis GmbH (2026). Sinabis Green Energy – Synthetic Document Dataset (10k PDFs).
> https://huggingface.co/datasets/sinabis-group/sinabis-10k-synthetic-pdf

## Citation

```bibtex
@misc{sinabis_green_pdf_10k_dataset_2026,
  author = {{Sinabis GmbH}},
  title  = {Sinabis Green Energy -- Synthetic Document Dataset (10k PDFs)},
  year   = {2026},
  url    = {https://huggingface.co/datasets/sinabis-group/sinabis-10k-synthetic-pdf}
}
```
