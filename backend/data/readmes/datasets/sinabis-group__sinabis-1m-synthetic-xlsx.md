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
  - 1M<n<10M
configs:
  - config_name: default
    data_files:
      - split: train
        path: "data/train-*.parquet"
---

# Sinabis Green Energy – Synthetic Document Dataset (1M XLSX)

More than **1,005,997 business spreadsheets (.xlsx)** from the everyday operations
of a fictional group of **Sinabis** companies (Sinabis Green Energy, Sinabis Bank, Sinabis Post, Sinabis Electric …) –
every organisation in the data carries the Sinabis name.

Every person, company, address, phone number, bank account, tax number, financial amount,
schedule and transaction in this dataset is **purely fictional**. Workbook structures come from LLM-written blueprints
(Gemma 4 26B-A4B) in the target language: sheets with columns, typed generation rules, example rows, formulas, totals,
KPIs, charts and notes. Each workbook expands the rows by these rules to its own length, turns formula columns into
real Excel formulas (with cached results) and is rendered in the issuer's design with `xlsxwriter`
(native Excel tables, conditional formatting, charts, frozen panes, print setup).

> All figures in this dataset card were **computed directly from the generated files**
> (as of 20 Oct 2026). They are not target estimates.

## At a glance

| Metric | Value |
|---|---|
| Total Workbooks | **1,005,997** `.xlsx` spreadsheets (22.0 GB uncompressed, 21.0 GB in 4 ZIP archives) |
| Document Themes | **47** distinct business themes (financials, budgets, cashflows, BoQ, KPI dashboards, schedules ...) |
| Real Excel Formulas | **Over 99 %** of workbooks contain real dynamic Excel formulas (`=SUM(...)`, `=AVERAGE(...)`, row calculations); 99.7 % in a sample of 101,000 workbooks |
| Multi-Sheet Workbooks | **956,058** multi-sheet workbooks (95.0 %) with connected financial sheets |
| Time span | **2011-04-06** to **2026-06-30** (15.2 years of continuous commercial history) |
| Languages | **24** languages (EN 81.1 %, JA 4.9 %, rest across 22 languages) |
| Issuing Companies | **2,014** distinct fictional companies across **33** countries |
| Unique Visual Identities | **201,399** individual company Design-DNA signatures |

## Quick start

The Parquet files under `data/` hold one row per workbook: all manifest fields plus the extracted
text, so the dataset can be browsed in the Dataset Viewer above and loaded directly:

```python
from datasets import load_dataset

ds = load_dataset("sinabis-group/sinabis-1m-synthetic-xlsx", split="train")
print(ds[0]["title"])
print(ds[0]["text"])
```

The `text` column holds every worksheet in order, introduced by `[Sheet: <name>]`, one row per line with cells separated by tabs. Formula cells show their calculated value. The original `.xlsx` files with formulas, charts and formatting are in the ZIP archive.

## Downloads

The dataset is packaged in four ZIP archives (0.1–10.2 GB each) for fast parallel downloads and streaming:

| File | Size | Contents |
|---|---:|---|
| `data/train-*.parquet` (11 files) | 2.56 GB | Manifest fields + extracted `text`, one row per workbook (Dataset Viewer, `load_dataset`) |
| `Sinabis_1M_xlsx_part_01.zip` | 8.61 GB | `413,500` XLSX files (9.05 GB uncompressed) |
| `Sinabis_1M_xlsx_part_02.zip` | 10.22 GB | `490,500` XLSX files (10.74 GB uncompressed) |
| `Sinabis_1M_xlsx_part_03.zip` | 2.00 GB | `95,997` XLSX files (2.10 GB uncompressed) |
| `Sinabis_1M_xlsx_part_04.zip` | 0.13 GB | `6,000` XLSX files (0.13 GB uncompressed) |

`Sinabis_1M_xlsx_manifest.zip` holds the JSON Lines records for all 1,005,997 workbooks
(see "Folder structure" below).

### Unpacking

All archives share a unified directory structure. Unpacking them into the same directory
merges all files seamlessly. Each part also contains the manifest files of its own documents, and the
manifest ZIP bundles all of them, so `unzip -o` simply overwrites identical files:

```bash
# Download and unpack with the Hugging Face CLI
hf download sinabis-group/sinabis-1m-synthetic-xlsx --repo-type dataset --local-dir sinabis-1m-xlsx
cd sinabis-1m-xlsx
for z in Sinabis_1M_xlsx_*.zip; do unzip -qo "$z"; done
```

## Folder structure

In the repository:

```
.
├── README.md
├── data/
│   └── train-*.parquet                 (rows for the Dataset Viewer and load_dataset)
├── Sinabis_1M_xlsx_part_01.zip … part_04.zip    → excel/
└── Sinabis_1M_xlsx_manifest.zip                 → manifest/
```

After unpacking all archives into one directory:

```
sinabis-1m-xlsx/
├── excel/
│   ├── financial_statement/
│   │   ├── 0000/
│   │   │   ├── 0000000_FS-2023-01.xlsx
│   │   │   └── ...
│   │   └── ...
│   ├── budget_plan/
│   ├── kpi_dashboard/
│   ├── timesheet/
│   └── ... (47 themes)
└── manifest/
    ├── xb00000.jsonl
    ├── xb00001.jsonl
    └── ...
```

Each `xbNNNNN.jsonl` manifest contains exact metadata for every spreadsheet:
- `file`: Relative path to the `.xlsx` file
- `format`: `"xlsx"`
- `theme`: Spreadsheet theme (e.g. `financial_statement`, `budget_plan`, `kpi_dashboard`)
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

## Spreadsheet Themes

| Theme | Documents | Share | Description |
|---|---:|---:|---|
| `financial_statement` | 46,284 | 4.6 % | Income statement (P&L) and balance sheet on two worksheets with a column chart |
| `project_calculation` | 46,278 | 4.6 % | Project costing and post-calculation with material, labour and subcontractor items |
| `budget_plan` | 46,260 | 4.6 % | Cost-centre budget plan with target/actual comparison, variances and a bar chart |
| `inventory_list` | 38,595 | 3.8 % | Stock and inventory list with reorder levels, batches and stock values |
| `project_plan` | 38,589 | 3.8 % | Project schedule with phases, milestones, progress bars and traffic-light status |
| `bill_of_quantities` | 38,577 | 3.8 % | Detailed bill of quantities (BoQ) with unit prices and totals |
| `open_items` | 38,558 | 3.8 % | Open items list with due dates, days overdue and ageing structure |
| `cashflow_forecast` | 38,548 | 3.8 % | 12-month liquidity plan with inflows and outflows, closing balances and a line chart |
| `kpi_dashboard` | 30,888 | 3.1 % | Management KPI dashboard with KPI tiles, target achievement and a chart |
| `sales_report` | 30,880 | 3.1 % | Sales report |
| `timesheet` | 30,856 | 3.1 % | Monthly timesheet with project allocation, break times and overtime balance |
| `price_list` | 30,852 | 3.1 % | Item and tiered price list with discount levels, quantity thresholds and contribution margin |
| `maintenance_log` | 23,146 | 2.3 % | Maintenance, inspection and servicing register with inspection deadlines and findings |
| `cost_center_report` | 23,142 | 2.3 % | Cost-centre report |
| `risk_register` | 23,142 | 2.3 % | Risk register |
| `invoice_register` | 23,142 | 2.3 % | Invoice register |
| `test_protocol` | 20,048 | 2.0 % | Test protocol |
| `expense_report` | 18,532 | 1.8 % | Travel expense report with meal allowances, mileage rate and receipt list |
| `asset_register` | 18,524 | 1.8 % | Asset register |
| `depreciation_schedule` | 18,521 | 1.8 % | Depreciation schedule |
| `purchase_requisitions` | 18,521 | 1.8 % | Purchase requisitions |
| `sales_pipeline` | 18,510 | 1.8 % | Sales pipeline |
| `tender_comparison` | 18,509 | 1.8 % | Tender comparison |
| `resource_plan` | 18,508 | 1.8 % | Resource plan |
| `energy_consumption` | 18,508 | 1.8 % | Energy consumption record |
| `customer_list` | 18,507 | 1.8 % | Customer list |
| `fleet_log` | 15,446 | 1.5 % | Fleet and driver's log with kilometres, fuel consumption and cost per km |
| `ticket_log` | 15,440 | 1.5 % | Ticket log |
| `payroll_summary` | 15,435 | 1.5 % | Payroll journal and salary list with tax and social security breakdown |
| `quality_inspection` | 15,432 | 1.5 % | Quality inspection record |
| `capex_plan` | 15,432 | 1.5 % | CAPEX plan |
| `delivery_schedule` | 15,432 | 1.5 % | Delivery schedule |
| `measurement_log` | 15,430 | 1.5 % | Measurement log |
| `production_plan` | 15,423 | 1.5 % | Production plan |
| `supplier_evaluation` | 15,416 | 1.5 % | Supplier evaluation |
| `shift_roster` | 15,413 | 1.5 % | Monthly shift and duty roster for teams (early, late, night and weekend shifts) |
| `vacation_planner` | 12,360 | 1.2 % | Vacation planner |
| `meter_readings` | 12,352 | 1.2 % | Meter readings |
| `training_matrix` | 12,341 | 1.2 % | Training matrix |
| `loan_amortization` | 12,327 | 1.2 % | Loan amortisation schedule |
| `commission_calculation` | 10,807 | 1.1 % | Commission calculation |
| `marketing_campaign_tracker` | 10,801 | 1.1 % | Marketing campaign tracker |
| `headcount_plan` | 10,794 | 1.1 % | Headcount plan |
| `survey_results` | 9,261 | 0.9 % | Survey results |
| `event_budget` | 9,260 | 0.9 % | Event budget |
| `invoice` | 9,248 | 0.9 % | Commercial invoice as a formatted Excel document with VAT total formulas |
| `quote` | 7,722 | 0.8 % | Commercial quotation as an Excel calculation with discounts and payment terms |

## Language Distribution

| Language | Documents | Share |
|---|---:|---:|
| English (`en`) | 815,559 | **81.1 %** |
| Japanese (`ja`) | 49,403 | **4.9 %** |
| Chinese (`zh`) | 47,433 | **4.7 %** |
| German (`de`) | 16,645 | **1.7 %** |
| Portuguese (`pt`) | 8,279 | **0.8 %** |
| Spanish (`es`) | 8,013 | **0.8 %** |
| Italian (`it`) | 6,884 | **0.7 %** |
| French (`fr`) | 5,753 | **0.6 %** |
| Dutch (`nl`) | 5,296 | **0.5 %** |
| Swedish (`sv`) | 4,564 | **0.5 %** |
| Korean (`ko`) | 4,016 | **0.4 %** |
| Polish (`pl`) | 3,833 | **0.4 %** |
| Indonesian (`id`) | 3,766 | **0.4 %** |
| Hungarian (`hu`) | 3,299 | **0.3 %** |
| Danish (`da`) | 3,198 | **0.3 %** |
| Norwegian (`nb`) | 2,504 | **0.2 %** |
| Ukrainian (`uk`) | 2,491 | **0.2 %** |
| Turkish (`tr`) | 2,433 | **0.2 %** |
| Czech (`cs`) | 2,412 | **0.2 %** |
| Finnish (`fi`) | 2,345 | **0.2 %** |
| Vietnamese (`vi`) | 2,284 | **0.2 %** |
| Greek (`el`) | 2,220 | **0.2 %** |
| Romanian (`ro`) | 2,010 | **0.2 %** |
| Russian (`ru`) | 1,357 | **0.1 %** |

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

> Sinabis GmbH (2026). Sinabis Green Energy – Synthetic Document Dataset (1M XLSX).
> https://huggingface.co/datasets/sinabis-group/sinabis-1m-synthetic-xlsx

## Citation

```bibtex
@misc{sinabis_green_xlsx_dataset_2026,
  author = {{Sinabis GmbH}},
  title  = {Sinabis Green Energy -- Synthetic Document Dataset (1M XLSX)},
  year   = {2026},
  url    = {https://huggingface.co/datasets/sinabis-group/sinabis-1m-synthetic-xlsx}
}
```
