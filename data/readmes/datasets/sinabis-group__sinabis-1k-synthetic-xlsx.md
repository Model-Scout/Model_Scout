---
license: cc-by-4.0
language:
  - en
  - ja
  - zh
  - de
  - pt
  - es
  - it
  - fr
  - nl
  - sv
  - ko
  - pl
  - id
  - hu
  - da
  - nb
  - uk
  - tr
  - cs
  - fi
  - vi
  - el
  - ro
task_categories:
  - text-generation
  - text-classification
  - tabular-classification
  - tabular-regression
  - time-series-forecasting
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
  - xlsx
  - excel
  - spreadsheet
  - spreadsheets
  - tabular
  - financial-records
  - business-documents
  - accounting
  - budgets
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
  - table-understanding
size_categories:
  - 1K<n<10K
configs:
  - config_name: default
    data_files:
      - split: train
        path: "data/train-*.parquet"
---

# Sinabis Green Energy – Synthetic Document Dataset (1k XLSX)

**1,010 business spreadsheets (.xlsx)** from the everyday operations
of a fictional group of **Sinabis** companies (Sinabis Green Energy, Sinabis Bank, Sinabis Post, Sinabis Electric …) –
every organisation in the data carries the Sinabis name.

This is the 1k edition of [sinabis-1m-synthetic-xlsx](https://huggingface.co/datasets/sinabis-group/sinabis-1m-synthetic-xlsx):
the first 1,010 workbooks of the 1M dataset (`idx` 0 to 1,009). File names, folder paths and manifest
records are identical to the 1M dataset, and this edition is the first part of the [10k edition](https://huggingface.co/datasets/sinabis-group/sinabis-10k-synthetic-xlsx) and [100k edition](https://huggingface.co/datasets/sinabis-group/sinabis-100k-synthetic-xlsx),
so all editions can be used side by side.

Every person, company, address, phone number, bank account, tax number, financial amount,
schedule and transaction in this dataset is **purely fictional**. Workbook structures come from LLM-written blueprints
(Gemma 4 26B-A4B) in the target language: sheets with columns, typed generation rules, example rows, formulas, totals,
KPIs, charts and notes. Each workbook expands the rows by these rules to its own length, turns formula columns into
real Excel formulas (with cached results) and is rendered in the issuer's design with `xlsxwriter`
(native Excel tables, conditional formatting, charts, frozen panes, print setup).

> All figures in this dataset card were **computed directly from the files in this edition**
> (as of 23 Oct 2026). They are not target estimates.

## At a glance

| Metric | Value |
|---|---|
| Total Workbooks | **1,010** `.xlsx` spreadsheets (22 MB uncompressed, 21 MB in 1 ZIP archive) |
| Document Themes | **47** distinct business themes (financials, budgets, cashflows, BoQ, KPI dashboards, schedules ...) |
| Real Excel Formulas | **1,009** workbooks (99.9 %) contain real dynamic Excel formulas (`=SUM(...)`, `=AVERAGE(...)`, row calculations) |
| Multi-Sheet Workbooks | **971** multi-sheet workbooks (96.1 %), Ø 2.3 sheets per workbook |
| Native Charts | **979** workbooks (96.9 %) with embedded Excel charts |
| Distinct Structures | **803** LLM blueprints, **835** distinct workbook titles |
| Time span | **2014-01-21** to **2026-06-18** (12.4 years) |
| Languages | **23** languages (EN 82.9 %, JA 5.1 %, rest across 21 languages) |
| Issuing Companies | **798** distinct fictional companies across **33** countries |

## Quick start

The Parquet file under `data/` holds one row per workbook: all manifest fields plus the extracted
text, so the dataset can be browsed in the Dataset Viewer above and loaded directly:

```python
from datasets import load_dataset

ds = load_dataset("sinabis-group/sinabis-1k-synthetic-xlsx", split="train")
print(ds[0]["title"])
print(ds[0]["text"])
```

The `text` column holds every worksheet in order, introduced by `[Sheet: <name>]`, one row per line with cells separated by tabs. Formula cells show their calculated value. The original `.xlsx` files with formulas, charts and formatting are in the ZIP archive.

## Downloads

| File | Size | Contents |
|---|---:|---|
| `data/train-*.parquet` (1 file) | 3 MB | Manifest fields + extracted `text`, one row per workbook (Dataset Viewer, `load_dataset`) |
| `Sinabis_1k_xlsx.zip` | 21 MB | `1,010` XLSX files + manifest (22 MB uncompressed) |

`Sinabis_1k_xlsx_manifest.zip` (0.2 MB) holds only the JSON Lines records for all 1,010 workbooks,
for a quick look at the metadata without downloading the spreadsheets (see "Folder structure" below).

### Unpacking

Both archives share one directory structure. The workbook archive already contains the manifest, so
`unzip -o` simply overwrites identical files:

```bash
# Download and unpack with the Hugging Face CLI
hf download sinabis-group/sinabis-1k-synthetic-xlsx --repo-type dataset --local-dir sinabis-1k-xlsx
cd sinabis-1k-xlsx
for z in Sinabis_1k_xlsx*.zip; do unzip -qo "$z"; done
```

## Folder structure

In the repository:

```
.
├── README.md
├── data/
│   └── train-*.parquet                 (rows for the Dataset Viewer and load_dataset)
├── Sinabis_1k_xlsx.zip             → excel/ + manifest/
└── Sinabis_1k_xlsx_manifest.zip    → manifest/
```

After unpacking:

```
sinabis-1k-xlsx/
├── excel/
│   ├── financial_statement/
│   │   ├── 0000/
│   │   │   ├── 0000xxx_<document-number>.xlsx
│   │   │   └── ...
│   │   └── ... (0000 to 0001)
│   ├── budget_plan/
│   ├── kpi_dashboard/
│   ├── timesheet/
│   └── ... (47 themes)
└── manifest/
    ├── xb00000.jsonl
    ├── ...
    └── xb00002.jsonl
```

Each `xbNNNNN.jsonl` contains 500 records (the last shard 10), one per workbook:
- `idx`: Running document number (same as in the 1M dataset)
- `file`: Relative path to the `.xlsx` file
- `format`: `"xlsx"`
- `theme`: Spreadsheet theme (e.g. `financial_statement`, `budget_plan`, `kpi_dashboard`)
- `issuer_id`: Stable ID of the fictional issuing company
- `issuer`: Fictional issuing company name
- `issuer_country`: Two-letter country code (ISO 3166-1)
- `recipient`: Counterparty or department name
- `recipient_kind`: Counterparty category (e.g. `customer`, `supplier`, `internal`)
- `lang`: Language code (ISO 639-1)
- `date`: Document date (ISO 8601)
- `number`: Reference number
- `currency`: ISO 4217 currency code
- `total`: Main financial or budget total
- `sheets`: Number of worksheets in the workbook
- `bytes`: Exact byte size of the `.xlsx` file
- `title`, `sheet_names`, `headers_preview`: Workbook title, worksheet names and the first table header
- `blueprint_id`, `length_class`: Source blueprint (`<theme>_<lang>_<n>`) and length class (S/M/L/XL)
- `rows`, `columns`, `formulas`, `charts`, `kpis`: Content statistics recorded at generation
- `layout_*`: Native Excel table, conditional formats, coloured sheet tabs

## Spreadsheet Themes

| Theme | Documents | Share | Description |
|---|---:|---:|---|
| `financial_statement` | 49 | 4.9 % | Income statement (P&L) and balance sheet on two worksheets with a column chart |
| `budget_plan` | 48 | 4.8 % | Cost-centre budget plan with target/actual comparison, variances and a bar chart |
| `project_plan` | 42 | 4.2 % | Project schedule with phases, milestones, progress bars and traffic-light status |
| `cashflow_forecast` | 40 | 4.0 % | 12-month liquidity plan with inflows and outflows, closing balances and a line chart |
| `inventory_list` | 39 | 3.9 % | Stock and inventory list with reorder levels, batches and stock values |
| `project_calculation` | 38 | 3.8 % | Project costing and post-calculation with material, labour and subcontractor items |
| `price_list` | 36 | 3.6 % | Item and tiered price list with discount levels, quantity thresholds and contribution margin |
| `bill_of_quantities` | 36 | 3.6 % | Detailed bill of quantities (BoQ) with unit prices and totals |
| `sales_report` | 34 | 3.4 % | Sales report |
| `timesheet` | 33 | 3.3 % | Monthly timesheet with project allocation, break times and overtime balance |
| `open_items` | 29 | 2.9 % | Open items list with due dates, days overdue and ageing structure |
| `cost_center_report` | 27 | 2.7 % | Cost-centre report |
| `invoice_register` | 26 | 2.6 % | Invoice register |
| `fleet_log` | 24 | 2.4 % | Fleet and driver's log with kilometres, fuel consumption and cost per km |
| `training_matrix` | 23 | 2.3 % | Training matrix |
| `risk_register` | 23 | 2.3 % | Risk register |
| `purchase_requisitions` | 23 | 2.3 % | Purchase requisitions |
| `energy_consumption` | 23 | 2.3 % | Energy consumption record |
| `resource_plan` | 22 | 2.2 % | Resource plan |
| `tender_comparison` | 22 | 2.2 % | Tender comparison |
| `kpi_dashboard` | 22 | 2.2 % | Management KPI dashboard with KPI tiles, target achievement and a chart |
| `depreciation_schedule` | 21 | 2.1 % | Depreciation schedule |
| `payroll_summary` | 21 | 2.1 % | Payroll journal and salary list with tax and social security breakdown |
| `asset_register` | 21 | 2.1 % | Asset register |
| `sales_pipeline` | 19 | 1.9 % | Sales pipeline |
| `ticket_log` | 18 | 1.8 % | Ticket log |
| `capex_plan` | 18 | 1.8 % | CAPEX plan |
| `maintenance_log` | 17 | 1.7 % | Maintenance, inspection and servicing register with inspection deadlines and findings |
| `customer_list` | 16 | 1.6 % | Customer list |
| `marketing_campaign_tracker` | 16 | 1.6 % | Marketing campaign tracker |
| `shift_roster` | 14 | 1.4 % | Monthly shift and duty roster for teams (early, late, night and weekend shifts) |
| `supplier_evaluation` | 13 | 1.3 % | Supplier evaluation |
| `expense_report` | 13 | 1.3 % | Travel expense report with meal allowances, mileage rate and receipt list |
| `test_protocol` | 13 | 1.3 % | Test protocol |
| `commission_calculation` | 12 | 1.2 % | Commission calculation |
| `measurement_log` | 12 | 1.2 % | Measurement log |
| `quality_inspection` | 11 | 1.1 % | Quality inspection record |
| `headcount_plan` | 11 | 1.1 % | Headcount plan |
| `event_budget` | 11 | 1.1 % | Event budget |
| `meter_readings` | 11 | 1.1 % | Meter readings |
| `invoice` | 10 | 1.0 % | Commercial invoice as a formatted Excel document with VAT total formulas |
| `production_plan` | 10 | 1.0 % | Production plan |
| `loan_amortization` | 9 | 0.9 % | Loan amortisation schedule |
| `vacation_planner` | 9 | 0.9 % | Vacation planner |
| `delivery_schedule` | 9 | 0.9 % | Delivery schedule |
| `survey_results` | 9 | 0.9 % | Survey results |
| `quote` | 7 | 0.7 % | Commercial quotation as an Excel calculation with discounts and payment terms |

## Language Distribution

| Language | Documents | Share |
|---|---:|---:|
| English (`en`) | 837 | **82.9 %** |
| Japanese (`ja`) | 52 | **5.1 %** |
| Chinese (`zh`) | 50 | **5.0 %** |
| German (`de`) | 10 | **1.0 %** |
| Italian (`it`) | 10 | **1.0 %** |
| Portuguese (`pt`) | 7 | **0.7 %** |
| French (`fr`) | 5 | **0.5 %** |
| Spanish (`es`) | 5 | **0.5 %** |
| Indonesian (`id`) | 5 | **0.5 %** |
| Swedish (`sv`) | 4 | **0.4 %** |
| Danish (`da`) | 3 | **0.3 %** |
| Dutch (`nl`) | 3 | **0.3 %** |
| Korean (`ko`) | 3 | **0.3 %** |
| Hungarian (`hu`) | 3 | **0.3 %** |
| Czech (`cs`) | 2 | **0.2 %** |
| Finnish (`fi`) | 2 | **0.2 %** |
| Turkish (`tr`) | 2 | **0.2 %** |
| Vietnamese (`vi`) | 2 | **0.2 %** |
| Romanian (`ro`) | 1 | **0.1 %** |
| Polish (`pl`) | 1 | **0.1 %** |
| Norwegian (`nb`) | 1 | **0.1 %** |
| Ukrainian (`uk`) | 1 | **0.1 %** |
| Greek (`el`) | 1 | **0.1 %** |

## Visual Design-DNA & Native Excel Features

Every issuing company in the dataset possesses a deterministic visual identity derived
from its unique company ID:
- **Header Banners:** Top-level company header with dedicated logo row (zero text overlap across all viewers).
- **Procedural PNG Logos:** High-resolution company logos embedded into cell A1 at native resolution.
- **Dynamic Excel Formulas:** Column sums (`=SUM(...)`), averages (`=AVERAGE(...)`), row formulas (`=C14*D14`, `=C14-B14`).
- **Interactive Controls:** AutoFilter enabled on tabular datasets, frozen table headers (`freeze_panes`).
- **KPI-Tiles:** Management summary tiles with currency and percentage formatting.
- **Embedded Charts:** Native Excel vector charts (`column`, `bar`, `line`) dynamically linked to table data ranges.
- **Print Optimization:** Formatted page setups (A4 / Letter, Portrait / Landscape, `fit_to_pages(1, 0)`).

## Strict Fictionality Guardrails

- **Domain Names:** All external email and website domains use the RFC 2606 reserved `.example` TLD.
- **Phone Numbers:** All telephone numbers use fictional prefixes (e.g. `555-01xx` in North America).
- **Banking:** Bank names and IBANs are algorithmically generated using synthetic syllables and valid checksum algorithms.
- **Screening:** Every entity is filtered against a 5,000+ entry real-world trademark and organization blocklist.

## License

This dataset is released under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.
You are free to share and adapt the material for any purpose, including commercial applications,
provided appropriate credit is given:

> Sinabis GmbH (2026). Sinabis Green Energy – Synthetic Document Dataset (1k XLSX).
> https://huggingface.co/datasets/sinabis-group/sinabis-1k-synthetic-xlsx

## Citation

```bibtex
@misc{sinabis_green_xlsx_1k_dataset_2026,
  author = {{Sinabis GmbH}},
  title  = {Sinabis Green Energy -- Synthetic Document Dataset (1k XLSX)},
  year   = {2026},
  url    = {https://huggingface.co/datasets/sinabis-group/sinabis-1k-synthetic-xlsx}
}
```
