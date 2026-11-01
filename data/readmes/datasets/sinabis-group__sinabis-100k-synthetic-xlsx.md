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
  - 100K<n<1M
configs:
  - config_name: default
    data_files:
      - split: train
        path: "data/train-*.parquet"
---

# Sinabis Green Energy – Synthetic Document Dataset (100k XLSX)

**101,000 business spreadsheets (.xlsx)** from the everyday operations
of a fictional group of **Sinabis** companies (Sinabis Green Energy, Sinabis Bank, Sinabis Post, Sinabis Electric …) –
every organisation in the data carries the Sinabis name.

This is the 100k edition of [sinabis-1m-synthetic-xlsx](https://huggingface.co/datasets/sinabis-group/sinabis-1m-synthetic-xlsx):
the first 101,000 workbooks of the 1M dataset (`idx` 0 to 100,999). File names, folder paths and manifest
records are identical to the 1M dataset, so both editions can be used side by side.

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
| Total Workbooks | **101,000** `.xlsx` spreadsheets (2.21 GB uncompressed, 2.09 GB in 1 ZIP archive) |
| Document Themes | **47** distinct business themes (financials, budgets, cashflows, BoQ, KPI dashboards, schedules ...) |
| Real Excel Formulas | **100,745** workbooks (99.7 %) contain real dynamic Excel formulas (`=SUM(...)`, `=AVERAGE(...)`, row calculations) |
| Multi-Sheet Workbooks | **96,094** multi-sheet workbooks (95.1 %), Ø 2.3 sheets per workbook |
| Native Charts | **97,705** workbooks (96.7 %) with embedded Excel charts |
| Distinct Structures | **4,004** LLM blueprints, **19,215** distinct workbook titles |
| Time span | **2011-05-29** to **2026-06-30** (15.1 years) |
| Languages | **24** languages (EN 81.2 %, JA 4.9 %, rest across 22 languages) |
| Issuing Companies | **2,014** distinct fictional companies across **33** countries |

## Quick start

The Parquet file under `data/` holds one row per workbook: all manifest fields plus the extracted
text, so the dataset can be browsed in the Dataset Viewer above and loaded directly:

```python
from datasets import load_dataset

ds = load_dataset("sinabis-group/sinabis-100k-synthetic-xlsx", split="train")
print(ds[0]["title"])
print(ds[0]["text"])
```

The `text` column holds every worksheet in order, introduced by `[Sheet: <name>]`, one row per line with cells separated by tabs. Formula cells show their calculated value. The original `.xlsx` files with formulas, charts and formatting are in the ZIP archive.

## Downloads

| File | Size | Contents |
|---|---:|---|
| `data/train-*.parquet` (1 file) | 257 MB | Manifest fields + extracted `text`, one row per workbook (Dataset Viewer, `load_dataset`) |
| `Sinabis_100k_xlsx.zip` | 2.09 GB | `101,000` XLSX files + manifest (2.21 GB uncompressed) |

`Sinabis_100k_xlsx_manifest.zip` (17.3 MB) holds only the JSON Lines records for all 101,000 workbooks,
for a quick look at the metadata without downloading the spreadsheets (see "Folder structure" below).

### Unpacking

Both archives share one directory structure. The workbook archive already contains the manifest, so
`unzip -o` simply overwrites identical files:

```bash
# Download and unpack with the Hugging Face CLI
hf download sinabis-group/sinabis-100k-synthetic-xlsx --repo-type dataset --local-dir sinabis-100k-xlsx
cd sinabis-100k-xlsx
for z in Sinabis_100k_xlsx*.zip; do unzip -qo "$z"; done
```

## Folder structure

In the repository:

```
.
├── README.md
├── data/
│   └── train-*.parquet                 (rows for the Dataset Viewer and load_dataset)
├── Sinabis_100k_xlsx.zip             → excel/ + manifest/
└── Sinabis_100k_xlsx_manifest.zip    → manifest/
```

After unpacking:

```
sinabis-100k-xlsx/
├── excel/
│   ├── financial_statement/
│   │   ├── 0000/
│   │   │   ├── 0000xxx_<document-number>.xlsx
│   │   │   └── ...
│   │   └── ... (0000 to 0100)
│   ├── budget_plan/
│   ├── kpi_dashboard/
│   ├── timesheet/
│   └── ... (47 themes)
└── manifest/
    ├── xb00000.jsonl
    ├── ...
    └── xb00201.jsonl
```

Each `xbNNNNN.jsonl` contains 500 records, one per workbook:
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
| `budget_plan` | 4,665 | 4.6 % | Cost-centre budget plan with target/actual comparison, variances and a bar chart |
| `financial_statement` | 4,618 | 4.6 % | Income statement (P&L) and balance sheet on two worksheets with a column chart |
| `project_calculation` | 4,554 | 4.5 % | Project costing and post-calculation with material, labour and subcontractor items |
| `inventory_list` | 3,959 | 3.9 % | Stock and inventory list with reorder levels, batches and stock values |
| `open_items` | 3,904 | 3.9 % | Open items list with due dates, days overdue and ageing structure |
| `cashflow_forecast` | 3,880 | 3.8 % | 12-month liquidity plan with inflows and outflows, closing balances and a line chart |
| `bill_of_quantities` | 3,853 | 3.8 % | Detailed bill of quantities (BoQ) with unit prices and totals |
| `project_plan` | 3,815 | 3.8 % | Project schedule with phases, milestones, progress bars and traffic-light status |
| `timesheet` | 3,226 | 3.2 % | Monthly timesheet with project allocation, break times and overtime balance |
| `price_list` | 3,062 | 3.0 % | Item and tiered price list with discount levels, quantity thresholds and contribution margin |
| `sales_report` | 3,040 | 3.0 % | Sales report |
| `kpi_dashboard` | 3,031 | 3.0 % | Management KPI dashboard with KPI tiles, target achievement and a chart |
| `invoice_register` | 2,371 | 2.3 % | Invoice register |
| `maintenance_log` | 2,349 | 2.3 % | Maintenance, inspection and servicing register with inspection deadlines and findings |
| `risk_register` | 2,323 | 2.3 % | Risk register |
| `cost_center_report` | 2,286 | 2.3 % | Cost-centre report |
| `test_protocol` | 2,032 | 2.0 % | Test protocol |
| `purchase_requisitions` | 1,927 | 1.9 % | Purchase requisitions |
| `resource_plan` | 1,904 | 1.9 % | Resource plan |
| `customer_list` | 1,885 | 1.9 % | Customer list |
| `asset_register` | 1,880 | 1.9 % | Asset register |
| `tender_comparison` | 1,874 | 1.9 % | Tender comparison |
| `expense_report` | 1,872 | 1.9 % | Travel expense report with meal allowances, mileage rate and receipt list |
| `energy_consumption` | 1,848 | 1.8 % | Energy consumption record |
| `depreciation_schedule` | 1,827 | 1.8 % | Depreciation schedule |
| `sales_pipeline` | 1,803 | 1.8 % | Sales pipeline |
| `payroll_summary` | 1,580 | 1.6 % | Payroll journal and salary list with tax and social security breakdown |
| `shift_roster` | 1,554 | 1.5 % | Monthly shift and duty roster for teams (early, late, night and weekend shifts) |
| `quality_inspection` | 1,544 | 1.5 % | Quality inspection record |
| `capex_plan` | 1,544 | 1.5 % | CAPEX plan |
| `ticket_log` | 1,538 | 1.5 % | Ticket log |
| `supplier_evaluation` | 1,515 | 1.5 % | Supplier evaluation |
| `fleet_log` | 1,507 | 1.5 % | Fleet and driver's log with kilometres, fuel consumption and cost per km |
| `delivery_schedule` | 1,505 | 1.5 % | Delivery schedule |
| `production_plan` | 1,491 | 1.5 % | Production plan |
| `measurement_log` | 1,484 | 1.5 % | Measurement log |
| `meter_readings` | 1,263 | 1.3 % | Meter readings |
| `training_matrix` | 1,243 | 1.2 % | Training matrix |
| `vacation_planner` | 1,243 | 1.2 % | Vacation planner |
| `loan_amortization` | 1,230 | 1.2 % | Loan amortisation schedule |
| `marketing_campaign_tracker` | 1,143 | 1.1 % | Marketing campaign tracker |
| `headcount_plan` | 1,107 | 1.1 % | Headcount plan |
| `commission_calculation` | 1,065 | 1.1 % | Commission calculation |
| `event_budget` | 982 | 1.0 % | Event budget |
| `invoice` | 955 | 0.9 % | Commercial invoice as a formatted Excel document with VAT total formulas |
| `survey_results` | 933 | 0.9 % | Survey results |
| `quote` | 786 | 0.8 % | Commercial quotation as an Excel calculation with discounts and payment terms |

## Language Distribution

| Language | Documents | Share |
|---|---:|---:|
| English (`en`) | 82,032 | **81.2 %** |
| Japanese (`ja`) | 4,947 | **4.9 %** |
| Chinese (`zh`) | 4,786 | **4.7 %** |
| German (`de`) | 1,594 | **1.6 %** |
| Portuguese (`pt`) | 826 | **0.8 %** |
| Spanish (`es`) | 758 | **0.8 %** |
| Italian (`it`) | 674 | **0.7 %** |
| Dutch (`nl`) | 557 | **0.6 %** |
| French (`fr`) | 552 | **0.5 %** |
| Swedish (`sv`) | 452 | **0.4 %** |
| Indonesian (`id`) | 396 | **0.4 %** |
| Polish (`pl`) | 388 | **0.4 %** |
| Korean (`ko`) | 369 | **0.4 %** |
| Danish (`da`) | 331 | **0.3 %** |
| Hungarian (`hu`) | 326 | **0.3 %** |
| Norwegian (`nb`) | 268 | **0.3 %** |
| Finnish (`fi`) | 247 | **0.2 %** |
| Turkish (`tr`) | 246 | **0.2 %** |
| Ukrainian (`uk`) | 243 | **0.2 %** |
| Czech (`cs`) | 231 | **0.2 %** |
| Greek (`el`) | 229 | **0.2 %** |
| Vietnamese (`vi`) | 211 | **0.2 %** |
| Romanian (`ro`) | 198 | **0.2 %** |
| Russian (`ru`) | 139 | **0.1 %** |

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

> Sinabis GmbH (2026). Sinabis Green Energy – Synthetic Document Dataset (100k XLSX).
> https://huggingface.co/datasets/sinabis-group/sinabis-100k-synthetic-xlsx

## Citation

```bibtex
@misc{sinabis_green_xlsx_100k_dataset_2026,
  author = {{Sinabis GmbH}},
  title  = {Sinabis Green Energy -- Synthetic Document Dataset (100k XLSX)},
  year   = {2026},
  url    = {https://huggingface.co/datasets/sinabis-group/sinabis-100k-synthetic-xlsx}
}
```
