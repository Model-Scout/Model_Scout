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
  - ru
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
  - 10K<n<100K
configs:
  - config_name: default
    data_files:
      - split: train
        path: "data/train-*.parquet"
---

# Sinabis Green Energy – Synthetic Document Dataset (10k XLSX)

**10,100 business spreadsheets (.xlsx)** from the everyday operations
of a fictional group of **Sinabis** companies (Sinabis Green Energy, Sinabis Bank, Sinabis Post, Sinabis Electric …) –
every organisation in the data carries the Sinabis name.

This is the 10k edition of [sinabis-1m-synthetic-xlsx](https://huggingface.co/datasets/sinabis-group/sinabis-1m-synthetic-xlsx):
the first 10,100 workbooks of the 1M dataset (`idx` 0 to 10,099). File names, folder paths and manifest
records are identical to the 1M dataset, and this edition is the first part of the [100k edition](https://huggingface.co/datasets/sinabis-group/sinabis-100k-synthetic-xlsx),
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
| Total Workbooks | **10,100** `.xlsx` spreadsheets (221 MB uncompressed, 209 MB in 1 ZIP archive) |
| Document Themes | **47** distinct business themes (financials, budgets, cashflows, BoQ, KPI dashboards, schedules ...) |
| Real Excel Formulas | **10,076** workbooks (99.8 %) contain real dynamic Excel formulas (`=SUM(...)`, `=AVERAGE(...)`, row calculations) |
| Multi-Sheet Workbooks | **9,591** multi-sheet workbooks (95.0 %), Ø 2.3 sheets per workbook |
| Native Charts | **9,772** workbooks (96.8 %) with embedded Excel charts |
| Distinct Structures | **2,777** LLM blueprints, **3,991** distinct workbook titles |
| Time span | **2012-03-15** to **2026-06-30** (14.3 years) |
| Languages | **24** languages (EN 80.9 %, JA 5.5 %, rest across 22 languages) |
| Issuing Companies | **1,981** distinct fictional companies across **33** countries |

## Quick start

The Parquet file under `data/` holds one row per workbook: all manifest fields plus the extracted
text, so the dataset can be browsed in the Dataset Viewer above and loaded directly:

```python
from datasets import load_dataset

ds = load_dataset("sinabis-group/sinabis-10k-synthetic-xlsx", split="train")
print(ds[0]["title"])
print(ds[0]["text"])
```

The `text` column holds every worksheet in order, introduced by `[Sheet: <name>]`, one row per line with cells separated by tabs. Formula cells show their calculated value. The original `.xlsx` files with formulas, charts and formatting are in the ZIP archive.

## Downloads

| File | Size | Contents |
|---|---:|---|
| `data/train-*.parquet` (1 file) | 26 MB | Manifest fields + extracted `text`, one row per workbook (Dataset Viewer, `load_dataset`) |
| `Sinabis_10k_xlsx.zip` | 209 MB | `10,100` XLSX files + manifest (221 MB uncompressed) |

`Sinabis_10k_xlsx_manifest.zip` (1.7 MB) holds only the JSON Lines records for all 10,100 workbooks,
for a quick look at the metadata without downloading the spreadsheets (see "Folder structure" below).

### Unpacking

Both archives share one directory structure. The workbook archive already contains the manifest, so
`unzip -o` simply overwrites identical files:

```bash
# Download and unpack with the Hugging Face CLI
hf download sinabis-group/sinabis-10k-synthetic-xlsx --repo-type dataset --local-dir sinabis-10k-xlsx
cd sinabis-10k-xlsx
for z in Sinabis_10k_xlsx*.zip; do unzip -qo "$z"; done
```

## Folder structure

In the repository:

```
.
├── README.md
├── data/
│   └── train-*.parquet                 (rows for the Dataset Viewer and load_dataset)
├── Sinabis_10k_xlsx.zip             → excel/ + manifest/
└── Sinabis_10k_xlsx_manifest.zip    → manifest/
```

After unpacking:

```
sinabis-10k-xlsx/
├── excel/
│   ├── financial_statement/
│   │   ├── 0000/
│   │   │   ├── 0000xxx_<document-number>.xlsx
│   │   │   └── ...
│   │   └── ... (0000 to 0010)
│   ├── budget_plan/
│   ├── kpi_dashboard/
│   ├── timesheet/
│   └── ... (47 themes)
└── manifest/
    ├── xb00000.jsonl
    ├── ...
    └── xb00020.jsonl
```

Each `xbNNNNN.jsonl` contains 500 records (the last shard 100), one per workbook:
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
| `budget_plan` | 463 | 4.6 % | Cost-centre budget plan with target/actual comparison, variances and a bar chart |
| `financial_statement` | 462 | 4.6 % | Income statement (P&L) and balance sheet on two worksheets with a column chart |
| `project_calculation` | 440 | 4.4 % | Project costing and post-calculation with material, labour and subcontractor items |
| `cashflow_forecast` | 408 | 4.0 % | 12-month liquidity plan with inflows and outflows, closing balances and a line chart |
| `inventory_list` | 389 | 3.9 % | Stock and inventory list with reorder levels, batches and stock values |
| `open_items` | 388 | 3.8 % | Open items list with due dates, days overdue and ageing structure |
| `bill_of_quantities` | 385 | 3.8 % | Detailed bill of quantities (BoQ) with unit prices and totals |
| `project_plan` | 354 | 3.5 % | Project schedule with phases, milestones, progress bars and traffic-light status |
| `timesheet` | 323 | 3.2 % | Monthly timesheet with project allocation, break times and overtime balance |
| `kpi_dashboard` | 301 | 3.0 % | Management KPI dashboard with KPI tiles, target achievement and a chart |
| `sales_report` | 299 | 3.0 % | Sales report |
| `price_list` | 296 | 2.9 % | Item and tiered price list with discount levels, quantity thresholds and contribution margin |
| `maintenance_log` | 227 | 2.2 % | Maintenance, inspection and servicing register with inspection deadlines and findings |
| `risk_register` | 223 | 2.2 % | Risk register |
| `invoice_register` | 223 | 2.2 % | Invoice register |
| `cost_center_report` | 216 | 2.1 % | Cost-centre report |
| `resource_plan` | 215 | 2.1 % | Resource plan |
| `purchase_requisitions` | 209 | 2.1 % | Purchase requisitions |
| `customer_list` | 196 | 1.9 % | Customer list |
| `tender_comparison` | 192 | 1.9 % | Tender comparison |
| `test_protocol` | 192 | 1.9 % | Test protocol |
| `asset_register` | 188 | 1.9 % | Asset register |
| `depreciation_schedule` | 187 | 1.9 % | Depreciation schedule |
| `energy_consumption` | 185 | 1.8 % | Energy consumption record |
| `expense_report` | 181 | 1.8 % | Travel expense report with meal allowances, mileage rate and receipt list |
| `capex_plan` | 168 | 1.7 % | CAPEX plan |
| `ticket_log` | 165 | 1.6 % | Ticket log |
| `sales_pipeline` | 165 | 1.6 % | Sales pipeline |
| `shift_roster` | 155 | 1.5 % | Monthly shift and duty roster for teams (early, late, night and weekend shifts) |
| `fleet_log` | 153 | 1.5 % | Fleet and driver's log with kilometres, fuel consumption and cost per km |
| `delivery_schedule` | 153 | 1.5 % | Delivery schedule |
| `supplier_evaluation` | 152 | 1.5 % | Supplier evaluation |
| `payroll_summary` | 145 | 1.4 % | Payroll journal and salary list with tax and social security breakdown |
| `measurement_log` | 144 | 1.4 % | Measurement log |
| `quality_inspection` | 143 | 1.4 % | Quality inspection record |
| `vacation_planner` | 139 | 1.4 % | Vacation planner |
| `production_plan` | 136 | 1.3 % | Production plan |
| `meter_readings` | 136 | 1.3 % | Meter readings |
| `loan_amortization` | 127 | 1.3 % | Loan amortisation schedule |
| `training_matrix` | 125 | 1.2 % | Training matrix |
| `commission_calculation` | 124 | 1.2 % | Commission calculation |
| `headcount_plan` | 115 | 1.1 % | Headcount plan |
| `marketing_campaign_tracker` | 111 | 1.1 % | Marketing campaign tracker |
| `invoice` | 110 | 1.1 % | Commercial invoice as a formatted Excel document with VAT total formulas |
| `survey_results` | 102 | 1.0 % | Survey results |
| `event_budget` | 101 | 1.0 % | Event budget |
| `quote` | 89 | 0.9 % | Commercial quotation as an Excel calculation with discounts and payment terms |

## Language Distribution

| Language | Documents | Share |
|---|---:|---:|
| English (`en`) | 8,172 | **80.9 %** |
| Japanese (`ja`) | 553 | **5.5 %** |
| Chinese (`zh`) | 473 | **4.7 %** |
| German (`de`) | 139 | **1.4 %** |
| Portuguese (`pt`) | 75 | **0.7 %** |
| Spanish (`es`) | 68 | **0.7 %** |
| Italian (`it`) | 64 | **0.6 %** |
| Dutch (`nl`) | 52 | **0.5 %** |
| French (`fr`) | 51 | **0.5 %** |
| Swedish (`sv`) | 48 | **0.5 %** |
| Hungarian (`hu`) | 47 | **0.5 %** |
| Indonesian (`id`) | 43 | **0.4 %** |
| Polish (`pl`) | 42 | **0.4 %** |
| Korean (`ko`) | 39 | **0.4 %** |
| Danish (`da`) | 33 | **0.3 %** |
| Norwegian (`nb`) | 32 | **0.3 %** |
| Vietnamese (`vi`) | 28 | **0.3 %** |
| Finnish (`fi`) | 25 | **0.2 %** |
| Turkish (`tr`) | 23 | **0.2 %** |
| Greek (`el`) | 23 | **0.2 %** |
| Czech (`cs`) | 21 | **0.2 %** |
| Romanian (`ro`) | 18 | **0.2 %** |
| Ukrainian (`uk`) | 18 | **0.2 %** |
| Russian (`ru`) | 13 | **0.1 %** |

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

> Sinabis GmbH (2026). Sinabis Green Energy – Synthetic Document Dataset (10k XLSX).
> https://huggingface.co/datasets/sinabis-group/sinabis-10k-synthetic-xlsx

## Citation

```bibtex
@misc{sinabis_green_xlsx_10k_dataset_2026,
  author = {{Sinabis GmbH}},
  title  = {Sinabis Green Energy -- Synthetic Document Dataset (10k XLSX)},
  year   = {2026},
  url    = {https://huggingface.co/datasets/sinabis-group/sinabis-10k-synthetic-xlsx}
}
```
