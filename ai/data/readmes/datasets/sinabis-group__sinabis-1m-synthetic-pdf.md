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
  - 1M<n<10M
configs:
  - config_name: default
    data_files:
      - split: train
        path: "data/train-*.parquet"
---

# Sinabis Green Energy – Synthetic Document Dataset (1M PDFs)

More than **1,006,000 business documents (PDF)** from the everyday operations
of a fictional renewable-energy group (**Sinabis Green Energy**) and its worldwide
ecosystem of customers, suppliers, subcontractors, utilities, authorities, insurers,
banks, hotels and service providers.

Every person, company, address, phone number, bank account, tax number, invoice and
transaction in this dataset is **purely fictional**. The underlying world and business
taxonomy were created with LLM assistance, while all documents, calculations,
serial numbers, dates and visual company designs were rendered deterministically
using ReportLab and custom vector engines.

> All figures in this dataset card were **computed directly from the generated files**
> (as of 16 Oct 2026). They are not target estimates.

## At a glance

| Metric | Value |
|---|---|
| Total Documents | **1,006,000** PDFs (71.8 GB uncompressed, 65.9 GB in 7 ZIP archives) |
| Document Types | **20** distinct business themes (invoices, receipts, payslips, bank statements, certificates ...) |
| Vector vs. Scanned | **645,457** clean vector PDFs (64.2 %) · **360,543** scanned/photocopied (35.8 %) with stamps, handwritten notes, skew and sensor noise |
| Time span | **2014-03-14** to **2026-06-30** (12.3 years of continuous commercial history) |
| Languages | **24** languages (EN 83.1 %, ZH 4.2 %, rest across 22 languages) |
| Issuing Companies | **1,777** distinct fictional companies across **33** countries |
| Unique Visual Identities | **178,099** individual company Design-DNA signatures |

## Quick start

The Parquet files under `data/` hold one row per document: all manifest fields plus the extracted
text, so the dataset can be browsed in the Dataset Viewer above and loaded directly:

```python
from datasets import load_dataset

ds = load_dataset("sinabis-group/sinabis-1m-synthetic-pdf", split="train")
print(ds[0]["theme"], ds[0]["number"], ds[0]["total"], ds[0]["currency"])
print(ds[0]["text"])

vector = ds.filter(lambda r: not r["scanned"])   # documents with a text layer
```

The `text` column holds the text layer of the PDF, page by page; `pages` is the page count. The scanned/photocopied documents (`scanned == True`) are images without a text layer, so their `text` is empty: they are meant for OCR and vision models. The original PDFs are in the ZIP archives.

## Downloads

The dataset is packaged in rolling ~10 GB ZIP archives for fast parallel downloads and streaming:

| File | Size | Contents |
|---|---:|---|
| `data/train-*.parquet` (11 files) | 458 MB | Manifest fields + extracted `text`, one row per document (Dataset Viewer, `load_dataset`) |
| `Sinabis_1M_pdfs_part_01.zip` | 9.86 GB | `150,500` PDFs (10.74 GB uncompressed) |
| `Sinabis_1M_pdfs_part_02.zip` | 9.88 GB | `151,000` PDFs (10.76 GB uncompressed) |
| `Sinabis_1M_pdfs_part_03.zip` | 9.89 GB | `151,000` PDFs (10.77 GB uncompressed) |
| `Sinabis_1M_pdfs_part_04.zip` | 9.87 GB | `151,500` PDFs (10.74 GB uncompressed) |
| `Sinabis_1M_pdfs_part_05.zip` | 9.89 GB | `150,500` PDFs (10.77 GB uncompressed) |
| `Sinabis_1M_pdfs_part_06.zip` | 9.88 GB | `150,500` PDFs (10.76 GB uncompressed) |
| `Sinabis_1M_pdfs_part_07.zip` | 6.65 GB | `101,000` PDFs (7.24 GB uncompressed) |
| `Sinabis_1M_pdfs_manifest.zip` | 74.3 MB | Complete dataset index: 1,006,000 JSONL records with file paths, metadata and sums |

### Unpacking

All archives share a unified directory structure. Unpacking them into the same directory
merges all files seamlessly:

```bash
# Download and unpack with the Hugging Face CLI
hf download sinabis-group/sinabis-1m-synthetic-pdf --repo-type dataset --local-dir sinabis-1m-pdf
cd sinabis-1m-pdf
for z in Sinabis_1M_pdfs_*.zip; do unzip -q "$z"; done
```

## Folder structure

In the repository:

```
.
├── README.md
├── data/
│   └── train-*.parquet                 (rows for the Dataset Viewer and load_dataset)
├── Sinabis_1M_pdfs_part_01.zip … part_07.zip    → pdf/ (+ manifest/ shards)
└── Sinabis_1M_pdfs_manifest.zip                 → manifest/
```

After unpacking:

```
sinabis-1m-pdf/
├── README.md
├── pdf/
│   ├── invoice/
│   │   ├── 0000/
│   │   │   ├── 0000000_INV-40192.pdf
│   │   │   └── ...
│   │   └── ...
│   ├── payslip/
│   ├── utility_bill/
│   └── ... (20 themes)
└── manifest/
    ├── b00000.jsonl
    ├── b00001.jsonl
    └── ...
```

Each `bNNNNN.jsonl` manifest contains exact metadata for every document:
- `file`: Relative path to the PDF
- `theme`: Document theme (e.g. `invoice`, `payslip`)
- `issuer`: Fictional issuing company name
- `issuer_country`: Two-letter country code (ISO 3166-1)
- `recipient`: Recipient name
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
| `invoice` | 281,680 | 28.0 % | Trade and service invoices with tax and early-payment discount calculations |
| `receipt` | 90,540 | 9.0 % | Receipts and till slips for cash and card payments |
| `quote` | 60,360 | 6.0 % | Commercial quotations with validity periods and payment terms |
| `payslip` | 50,300 | 5.0 % | Monthly payslips with deductions, taxes and social security contributions |
| `delivery_note` | 50,300 | 5.0 % | Delivery notes with package details and handover receipt |
| `bank_statement` | 40,240 | 4.0 % | Bank statements with transaction descriptions and running balances |
| `utility_bill` | 40,240 | 4.0 % | Energy and utility bills with consumption history |
| `certificate` | 40,240 | 4.0 % | Participation, training and calibration certificates with seal |
| `dunning` | 40,240 | 4.0 % | Multi-level payment reminders with dunning fees and deadlines |
| `order_confirmation` | 40,240 | 4.0 % | Order confirmations with delivery dates |
| `timesheet` | 30,180 | 3.0 % | Monthly timesheets with project and daywork hours |
| `freight_bill` | 30,180 | 3.0 % | Freight and forwarding documents (CMR/AWB) with dangerous-goods notes |
| `hotel_invoice` | 30,180 | 3.0 % | Hotel invoices with tourist tax, lodging and catering |
| `authority_notice` | 30,180 | 3.0 % | Authority notices and fee decisions with appeal instructions |
| `maintenance_report` | 30,180 | 3.0 % | Technical maintenance and inspection reports with test points |
| `workshop_invoice` | 30,180 | 3.0 % | Workshop invoices with labour units (AW) and spare parts |
| `expense_report` | 30,180 | 3.0 % | Travel expense reports with meal allowances and receipts |
| `insurance_policy` | 20,120 | 2.0 % | Insurance policies with coverage amounts and clauses |
| `packing_list` | 20,120 | 2.0 % | Detailed packing lists with weight and dimension details |
| `credit_note` | 20,120 | 2.0 % | Credit notes referencing the original invoice |

## Language Distribution

| Language | Documents | Share |
|---|---:|---:|
| English (`en`) | 836,257 | **83.1 %** |
| Chinese (`zh`) | 42,399 | **4.2 %** |
| Japanese (`ja`) | 40,678 | **4.0 %** |
| German (`de`) | 16,166 | **1.6 %** |
| Spanish (`es`) | 8,659 | **0.9 %** |
| Italian (`it`) | 6,710 | **0.7 %** |
| Portuguese (`pt`) | 6,616 | **0.7 %** |
| French (`fr`) | 4,945 | **0.5 %** |
| Swedish (`sv`) | 4,882 | **0.5 %** |
| Polish (`pl`) | 4,808 | **0.5 %** |
| Dutch (`nl`) | 4,069 | **0.4 %** |
| Korean (`ko`) | 3,684 | **0.4 %** |
| Hungarian (`hu`) | 3,417 | **0.3 %** |
| Norwegian (`nb`) | 3,043 | **0.3 %** |
| Danish (`da`) | 2,713 | **0.3 %** |
| Vietnamese (`vi`) | 2,575 | **0.3 %** |
| Greek (`el`) | 2,351 | **0.2 %** |
| Indonesian (`id`) | 2,278 | **0.2 %** |
| Turkish (`tr`) | 2,005 | **0.2 %** |
| Finnish (`fi`) | 1,840 | **0.2 %** |
| Czech (`cs`) | 1,733 | **0.2 %** |
| Ukrainian (`uk`) | 1,609 | **0.2 %** |
| Romanian (`ro`) | 1,541 | **0.2 %** |
| Russian (`ru`) | 1,022 | **0.1 %** |

## Visual Design-DNA

Every issuing company in the dataset possesses a deterministic visual identity derived
from its unique company ID:
- **Header Archetypes:** Full-bleed color band, clean letterhead, modern sidebar, minimalist, split-block.
- **Procedural Logos:** 20 vector geometric symbols, typography and layouts generated with exact brand rules.
- **Color Palettes:** Harmonized primary, secondary, accent and neutral tones with WCAG-compliant contrast.
- **Typography:** Tailored font pairings for the scripts used by the 24 languages (Latin, CJK, Cyrillic and Greek).
- **Physical Scan Artifacts:** About a third (35.8 %) of the documents undergo a high-resolution copier/scanner simulation
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

> Sinabis GmbH (2026). Sinabis Green Energy – Synthetic Document Dataset (1M PDFs).
> https://huggingface.co/datasets/sinabis-group/sinabis-1m-synthetic-pdf

## Citation

```bibtex
@misc{sinabis_green_pdf_dataset_2026,
  author = {{Sinabis GmbH}},
  title  = {Sinabis Green Energy -- Synthetic Document Dataset (1M PDFs)},
  year   = {2026},
  url    = {https://huggingface.co/datasets/sinabis-group/sinabis-1m-synthetic-pdf}
}
```
