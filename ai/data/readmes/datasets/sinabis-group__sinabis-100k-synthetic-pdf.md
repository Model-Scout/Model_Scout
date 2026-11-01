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
  - 100K<n<1M
configs:
  - config_name: default
    data_files:
      - split: train
        path: "data/train-*.parquet"
---

# Sinabis Green Energy – Synthetic Document Dataset (100k PDFs)

**101,000 business documents (PDF)** from the everyday operations
of a fictional renewable-energy group (**Sinabis Green Energy**) and its worldwide
ecosystem of customers, suppliers, subcontractors, utilities, authorities, insurers,
banks, hotels and service providers.

This is the 100k edition of [sinabis-1m-synthetic-pdf](https://huggingface.co/datasets/sinabis-group/sinabis-1m-synthetic-pdf):
the first 101,000 documents of the 1M dataset (`idx` 0 to 100,999). File names, folder paths and manifest
records are identical to the 1M dataset, so both editions can be used side by side.

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
| Total Documents | **101,000** PDFs (7.21 GB uncompressed, 6.59 GB in 1 ZIP archive) |
| Document Types | **20** distinct business themes (invoices, receipts, payslips, bank statements, certificates ...) |
| Vector vs. Scanned | **64,987** clean vector PDFs (64.3 %) · **36,013** scanned/photocopied (35.7 %) with stamps, handwritten notes, skew and sensor noise |
| Time span | **2014-03-23** to **2026-06-30** (12.3 years of continuous commercial history) |
| Languages | **24** languages (EN 83.0 %, ZH 4.3 %, rest across 22 languages) |
| Issuing Companies | **1,777** distinct fictional companies across **33** countries |

## Quick start

The Parquet file under `data/` holds one row per document: all manifest fields plus the extracted
text, so the dataset can be browsed in the Dataset Viewer above and loaded directly:

```python
from datasets import load_dataset

ds = load_dataset("sinabis-group/sinabis-100k-synthetic-pdf", split="train")
print(ds[0]["theme"], ds[0]["number"], ds[0]["total"], ds[0]["currency"])
print(ds[0]["text"])

vector = ds.filter(lambda r: not r["scanned"])   # documents with a text layer
```

The `text` column holds the text layer of the PDF, page by page; `pages` is the page count. The scanned/photocopied documents (`scanned == True`) are images without a text layer, so their `text` is empty: they are meant for OCR and vision models. The original PDFs are in the ZIP archive.

## Downloads

| File | Size | Contents |
|---|---:|---|
| `data/train-*.parquet` (1 file) | 46 MB | Manifest fields + extracted `text`, one row per document (Dataset Viewer, `load_dataset`) |
| `Sinabis_100k_pdfs.zip` | 6.59 GB | `101,000` PDFs + manifest (7.21 GB uncompressed) |
| `Sinabis_100k_pdfs_manifest.zip` | 7.5 MB | Dataset index only: 101,000 JSONL records with file paths, metadata and sums |

### Unpacking

Both archives share one directory structure. The PDF archive already contains the manifest, so
`unzip -o` simply overwrites identical files:

```bash
# Download and unpack with the Hugging Face CLI
hf download sinabis-group/sinabis-100k-synthetic-pdf --repo-type dataset --local-dir sinabis-100k-pdf
cd sinabis-100k-pdf
for z in Sinabis_100k_pdfs*.zip; do unzip -qo "$z"; done
```

## Folder structure

In the repository:

```
.
├── README.md
├── data/
│   └── train-*.parquet                 (rows for the Dataset Viewer and load_dataset)
├── Sinabis_100k_pdfs.zip             → pdf/ + manifest/
└── Sinabis_100k_pdfs_manifest.zip    → manifest/
```

After unpacking:

```
sinabis-100k-pdf/
├── README.md
├── pdf/
│   ├── invoice/
│   │   ├── 0000/
│   │   │   ├── 0000xxx_<document-number>.pdf
│   │   │   └── ...
│   │   └── ... (0000 to 0100)
│   ├── payslip/
│   ├── utility_bill/
│   └── ... (20 themes)
└── manifest/
    ├── b00000.jsonl
    ├── ...
    └── b00201.jsonl
```

Each `bNNNNN.jsonl` contains 500 records, one per document:
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
| `invoice` | 28,389 | 28.1 % | Trade and service invoices with tax and early-payment discount calculations |
| `receipt` | 9,009 | 8.9 % | Receipts and till slips for cash and card payments |
| `quote` | 5,948 | 5.9 % | Commercial quotations with validity periods and payment terms |
| `payslip` | 5,020 | 5.0 % | Monthly payslips with deductions, taxes and social security contributions |
| `delivery_note` | 4,997 | 4.9 % | Delivery notes with package details and handover receipt |
| `order_confirmation` | 4,191 | 4.1 % | Order confirmations with delivery dates |
| `bank_statement` | 4,030 | 4.0 % | Bank statements with transaction descriptions and running balances |
| `utility_bill` | 4,017 | 4.0 % | Energy and utility bills with consumption history |
| `dunning` | 3,988 | 3.9 % | Multi-level payment reminders with dunning fees and deadlines |
| `certificate` | 3,966 | 3.9 % | Participation, training and calibration certificates with seal |
| `maintenance_report` | 3,113 | 3.1 % | Technical maintenance and inspection reports with test points |
| `freight_bill` | 3,084 | 3.1 % | Freight and forwarding documents (CMR/AWB) with dangerous-goods notes |
| `expense_report` | 3,078 | 3.0 % | Travel expense reports with meal allowances and receipts |
| `authority_notice` | 3,027 | 3.0 % | Authority notices and fee decisions with appeal instructions |
| `timesheet` | 3,006 | 3.0 % | Monthly timesheets with project and daywork hours |
| `workshop_invoice` | 3,006 | 3.0 % | Workshop invoices with labour units (AW) and spare parts |
| `hotel_invoice` | 2,994 | 3.0 % | Hotel invoices with tourist tax, lodging and catering |
| `packing_list` | 2,102 | 2.1 % | Detailed packing lists with weight and dimension details |
| `credit_note` | 2,065 | 2.0 % | Credit notes referencing the original invoice |
| `insurance_policy` | 1,970 | 2.0 % | Insurance policies with coverage amounts and clauses |

## Language Distribution

| Language | Documents | Share |
|---|---:|---:|
| English (`en`) | 83,825 | **83.0 %** |
| Chinese (`zh`) | 4,307 | **4.3 %** |
| Japanese (`ja`) | 4,149 | **4.1 %** |
| German (`de`) | 1,697 | **1.7 %** |
| Spanish (`es`) | 858 | **0.8 %** |
| Italian (`it`) | 694 | **0.7 %** |
| Portuguese (`pt`) | 679 | **0.7 %** |
| French (`fr`) | 514 | **0.5 %** |
| Polish (`pl`) | 502 | **0.5 %** |
| Swedish (`sv`) | 482 | **0.5 %** |
| Dutch (`nl`) | 402 | **0.4 %** |
| Hungarian (`hu`) | 338 | **0.3 %** |
| Korean (`ko`) | 335 | **0.3 %** |
| Norwegian (`nb`) | 300 | **0.3 %** |
| Vietnamese (`vi`) | 268 | **0.3 %** |
| Danish (`da`) | 254 | **0.3 %** |
| Greek (`el`) | 235 | **0.2 %** |
| Indonesian (`id`) | 208 | **0.2 %** |
| Turkish (`tr`) | 193 | **0.2 %** |
| Finnish (`fi`) | 182 | **0.2 %** |
| Czech (`cs`) | 171 | **0.2 %** |
| Ukrainian (`uk`) | 158 | **0.2 %** |
| Romanian (`ro`) | 151 | **0.1 %** |
| Russian (`ru`) | 98 | **0.1 %** |

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

> Sinabis GmbH (2026). Sinabis Green Energy – Synthetic Document Dataset (100k PDFs).
> https://huggingface.co/datasets/sinabis-group/sinabis-100k-synthetic-pdf

## Citation

```bibtex
@misc{sinabis_green_pdf_100k_dataset_2026,
  author = {{Sinabis GmbH}},
  title  = {Sinabis Green Energy -- Synthetic Document Dataset (100k PDFs)},
  year   = {2026},
  url    = {https://huggingface.co/datasets/sinabis-group/sinabis-100k-synthetic-pdf}
}
```
