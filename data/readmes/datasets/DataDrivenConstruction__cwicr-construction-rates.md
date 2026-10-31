---
license: apache-2.0
language:
  - ar
  - bg
  - cs
  - de
  - en
  - es
  - fr
  - hi
  - hr
  - id
  - it
  - ja
  - ko
  - nl
  - pl
  - pt
  - ro
  - ru
  - sv
  - th
  - tr
  - vi
  - zh
tags:
  - construction
  - cost-estimation
  - quantity-surveying
  - BIM
  - construction-rates
  - bill-of-quantities
  - tabular
  - parquet
  - multilingual
size_categories:
  - 1M<n<10M
pretty_name: CWICR — Construction Works, Items, Costs & Resources (30 Countries)
configs:
  - config_name: default
    data_files:
      - split: en
        path: EN/*.parquet
      - split: us
        path: US/*.parquet
      - split: uk
        path: UK/*.parquet
      - split: au
        path: AU/*.parquet
      - split: nz
        path: NZ/*.parquet
      - split: ng
        path: NG/*.parquet
      - split: za
        path: ZA/*.parquet
      - split: de
        path: DE/*.parquet
      - split: fr
        path: FR/*.parquet
      - split: es
        path: ES/*.parquet
      - split: mx
        path: MX/*.parquet
      - split: pt
        path: PT/*.parquet
      - split: it
        path: IT/*.parquet
      - split: nl
        path: NL/*.parquet
      - split: ru
        path: RU/*.parquet
      - split: pl
        path: PL/*.parquet
      - split: cs
        path: CS/*.parquet
      - split: hr
        path: HR/*.parquet
      - split: bg
        path: BG/*.parquet
      - split: ro
        path: RO/*.parquet
      - split: sv
        path: SV/*.parquet
      - split: tr
        path: TR/*.parquet
      - split: ar
        path: AR/*.parquet
      - split: hi
        path: HI/*.parquet
      - split: zh
        path: ZH/*.parquet
      - split: ja
        path: JA/*.parquet
      - split: ko
        path: KO/*.parquet
      - split: th
        path: TH/*.parquet
      - split: vi
        path: VI/*.parquet
      - split: id
        path: ID/*.parquet
---

# CWICR — Construction Works, Items, Costs & Resources

![OpenConstructionERP — the platform that consumes CWICR](./assets/hero-overview.jpg)

**A multilingual, machine-readable database of national construction rate books for 30 countries / language locales.** Each rate is fully decomposed into its work composition and resource breakdown (labour, machinery, materials), with unit prices, hierarchical classification, and physical parameters preserved in the source language.

This dataset is the **tabular source-of-truth** behind the [`cwicr-vector-db-bgem3-v3`](https://huggingface.co/datasets/DataDrivenConstruction/cwicr-vector-db-bgem3-v3) Qdrant snapshots. Use this repository when you need raw numeric data (prices, quantities, time norms); use the vector DB repository when you need semantic search over rate descriptions.

> 💡 **Looking for a complete estimation platform?** CWICR powers the cost database inside [**OpenConstructionERP**](https://github.com/datadrivenconstruction/OpenConstructionERP) — an open-source modular ERP for construction (BOQ editor, BIM/CAD import, AI takeoff, GAEB XML, AGPL-3.0). The ERP consumes the parquets here and the Qdrant snapshots in the companion repo to provide localised cost estimation in 30 markets out of the box.

## How CWICR is used inside OpenConstructionERP

![BOQ Editor, Resource Catalog, Cost Database, Smart Item Search](./assets/feature-databases.jpg)

The parquets in this repository are loaded into the ERP as four cooperating surfaces:

- **BOQ Editor** — pick rates from the localised database and assemble Bills of Quantities in the project's currency.
- **Resource Catalog** — drill into the per-rate decomposition (labour roles, machinery classes, material families) preserved verbatim in the parquet.
- **Cost Database** — browse the full catalogue with national filters; the underlying schema matches the parquet 1-to-1.
- **Smart Item Search** — backed by the companion Qdrant snapshots (BGE-M3 hybrid dense + sparse) for typo-tolerant multilingual lookup.

## Contents per country

Each language directory (`AR/`, `BG/`, `CS/`, `DE/`, `EN/`, `ES/`, `FR/`, `HI/`, `HR/`, `ID/`, `IT/`, `JA/`, `KO/`, `MX/`, `NG/`, `NL/`, `NZ/`, `PL/`, `PT/`, `RO/`, `RU/`, `SV/`, `TH/`, `TR/`, `UK/`, `US/`, `VI/`, `ZA/`, `ZH/`) contains **5 files**, all uploaded for all 30 locales:

| File | Description |
|---|---|
| `<LANG>_<CITY>_workitems_costs_resources_DDC_CWICR.parquet` | Primary table — one row per (rate × resource). ~900K rows per country, 84 columns. |
| `DDC_CWICR_<LANG>_<CITY>_Catalog.csv` | Compact catalogue — one row per unique `rate_code` with title, unit, collection, hierarchy. ~55K rows per country. |
| `DDC_CWICR_<LANG>_<CITY>_Catalog.xlsx` | Same catalogue, Excel-formatted (auto-widths, frozen headers, ~800 KB). |
| `README.md` | Per-country quick reference in the source language (locale, collections, schema notes). |
| `README_DDC_CWICR_TABULAR_<LANG>_<CITY>.txt` | Plain-text full documentation in the source language — covers schema, classification hierarchy, units, currency, source publication and license notes for that country's rate book. |

**File totals on this repository**: 30 parquets + 30 CSV catalogues + 30 XLSX catalogues + 30 per-country README.md + 30 localised TXT readmes = 150 country files (plus the top-level README and assets).

Excel exports of the full table (`*_FORMATTED.xlsx`, `*_SIMPLE.xlsx`) and the localised PDF documentation are reproducible from the parquet + TXT readme and are kept in the source GitHub repository as Git LFS objects.

## Schema (parquet — 84 columns)

The parquet preserves the full rate decomposition. A rate (e.g. *"Excavator 15 m³, soil class 2"*) is unfolded into multiple rows, one per resource it consumes (the excavator itself, fuel, operator labour, transport, etc.). Each row carries both rate-level fields (replicated across the rate's rows) and resource-level fields (unique per row).

Column groups:

- **Identification**: `rate_code`, `rate_original_name`, `rate_final_name`, `rate_unit`, `is_abstract` (parent aggregator vs. specific variant)
- **Hierarchy**: `category_type`, `department_code`, `department_name`, `section_name`, `subsection_name`, `collection_name`
- **Physical params**: `mass_name`, `mass_value`, `mass_unit` (preserves original semantics: "масса 1 шт.", "Gewicht", etc.)
- **Costs**: `rate_total_cost`, `rate_labour_cost`, `rate_materials_cost`, `rate_machinery_cost`, `rate_overhead`, `rate_profit`, `currency`
- **Work composition**: `work_composition_text` — full natural-language description of the work performed
- **Resources** (one row each): `resource_code`, `resource_name`, `resource_type`, `resource_quantity`, `resource_unit`, `resource_unit_cost`, `resource_total_cost`
- **Machinery taxonomy**: `machine_class1_name` … `machine_class3_name` — classification of machinery resources
- **Provenance**: `source_book`, `source_year`, `source_publisher`, `source_url`

All text fields are in the **source language of the rate book** (Russian, German, Chinese, Hindi, etc.). Unit symbols and numeric values are kept verbatim from the original publication.

## Quick start (Python)

```python
from datasets import load_dataset

# Load all rates for one country (parquet → in-memory Arrow table)
ds = load_dataset("DataDrivenConstruction/cwicr-construction-rates", split="de")
print(ds.column_names)
print(ds[0])

# Or load lazily with polars (recommended for >100K rows)
import polars as pl
df = pl.scan_parquet(
    "hf://datasets/DataDrivenConstruction/cwicr-construction-rates/DE/DE_BERLIN_workitems_costs_resources_DDC_CWICR.parquet"
).filter(pl.col("collection_name").str.contains("Erdarbeiten")).collect()
```

## Quick start (CLI)

```bash
# Download one country
huggingface-cli download DataDrivenConstruction/cwicr-construction-rates \
  --include "DE/*" --repo-type dataset --local-dir ./cwicr_de

# Convert to CSV for quick inspection
python -c "import polars as pl; pl.read_parquet('cwicr_de/DE/DE_BERLIN_workitems_costs_resources_DDC_CWICR.parquet').write_csv('de.csv')"
```

## Coverage

**30 locale-specific rate books** spanning **23 languages**:

| Region | Locales |
|---|---|
| Russian-speaking | RU (St. Petersburg / federal) |
| English-speaking | EN (Toronto), UK (London / GBP), US (USA / USD), AU (Sydney), NZ (Auckland), NG (Lagos), ZA (Johannesburg) |
| Spanish/Portuguese | ES (Barcelona), MX (Mexico City), PT (São Paulo) |
| Central/Eastern Europe | DE (Berlin), FR (Paris), IT (Rome), NL (Amsterdam), PL (Warsaw), CS (Prague), HR (Zagreb), BG (Sofia), RO (Bucharest), SV (Stockholm), TR (Istanbul) |
| Middle East / South Asia | AR (Dubai), HI (Mumbai) |
| East / Southeast Asia | ZH (Shanghai), JA (Tokyo), KO (Seoul), TH (Bangkok), VI (Hanoi), ID (Jakarta) |

Each rate book uses its **native classification system** (Russian СНиП codes, German DIN structures, US MasterFormat-style hierarchies, Chinese GB classifiers, etc.). The schema is unified across countries but the *values* in `collection_name` / `department_code` / etc. are in the source language and follow each country's own taxonomy.

## Use cases

- **Cost estimation**: BIM quantity takeoff → match elements to rates → compute project cost in local currency
- **Cross-country price benchmarking**: compare the unit cost of equivalent works (e.g. concrete pouring) across markets
- **Construction-specific LLM fine-tuning**: rich multilingual corpus of technical construction language with structured grounding
- **Resource normalization research**: align machinery / material / labour ontologies across national catalogues
- **Quantity surveying education**: realistic worked examples in 23 languages

## Related artifacts

- **Vector DB snapshots** (Qdrant, hybrid BGE-M3 dense + sparse + resources, ready to restore):  
  → [`DataDrivenConstruction/cwicr-vector-db-bgem3-v3`](https://huggingface.co/datasets/DataDrivenConstruction/cwicr-vector-db-bgem3-v3)
- **OpenConstructionERP** — production ERP that consumes this dataset (BOQ editor, BIM/CAD import, AI takeoff, GAEB):  
  → [`github.com/datadrivenconstruction/OpenConstructionERP`](https://github.com/datadrivenconstruction/OpenConstructionERP)
- **Source code / pipelines** (encoders, classifiers, search demos, BIM matchers):  
  → [`github.com/datadrivenconstruction/OpenConstructionEstimate-DDC-CWICR`](https://github.com/datadrivenconstruction/OpenConstructionEstimate-DDC-CWICR)

## Exploring the data

Below are a few summary visualisations produced directly from the parquet files (chart code lives in the [source repository](https://github.com/datadrivenconstruction/OpenConstructionEstimate-DDC-CWICR) under `0_Workflow and Pipelines CWICR/python/08-data-analysis/`).

### Cost distribution by department

Boxplots of total cost per rate position, grouped by department. Heat-supply and rolling-equipment works dominate at the top end; electrical-installation rates are tightly clustered in the low-cost band.

![Cost distribution by department](./assets/cost_distribution_by_department.png)

### Material vs labour cost

Scatter of (material cost, labour cost) per rate, coloured by department. Three regimes are visible: labour-heavy structural works (left vertical band), material-heavy mechanical installations (top-right cluster) and balanced general-purpose rates (diagonal).

![Material vs labour cost](./assets/labor_vs_material_ratio.png)

### Resource utilisation

Distribution of how often each resource type (labour roles, machinery classes, material families) is consumed across all rates.

![Resource utilisation](./assets/resource_utilization.png)

### Beyond the database — AI takeoff in OpenConstructionERP

![AI takeoff from PDF drawings](./assets/feature-takeoff-ai.jpg)

CWICR rates become live cost data once they are matched against quantities. In OpenConstructionERP that matching is automated: drawings (PDF / DWG / RVT / IFC) are converted to a canonical element list, CV/OCR detects symbols and dimensions, and the resulting quantities are paired with the closest CWICR rates via the companion Qdrant snapshots.

## Data sources

CWICR aggregates publicly available national rate catalogues:

- **RU**: Federal Unified Rates (ФЕР / ТЕР), Ministry of Construction RF, regional indices.
- **EU**: National building cost compendia for each member state.
- **US/CA**: RSMeans-style cost data, MasterFormat-aligned.
- **CN/JP/KR/TH/VN/ID**: Government-published quota / norm catalogues.
- **Other**: Country-specific official sources cited in each rate's `source_book` field.

The CWICR pipeline normalises these into a single schema; the **rate codes, prices, and work compositions are preserved verbatim** from the originals. License applicability of underlying codes follows each catalogue's terms; this redistribution is for research and reference. Where redistribution is restricted, only derived metrics or anonymised samples are included.

## Reproducibility

The CWICR pipeline (parsers, normalisers, classifiers) is open-source. Each parquet here is built by:

1. Source-specific parser → standard `workitems_costs_resources` raw frame
2. `v3_classifier.enrich_v3` → 29 indexed payload fields (collections, departments, physical params)
3. `ost_ifc_mapping.base_code` → cross-language rate-code normalisation (lang/unit suffixes + inline tags)

See the source repository for full pipeline scripts.

## Support the project ⭐

If this dataset is useful to you — or if you'd like to see more open construction databases like it — the most helpful thing you can do is **leave a star on the [OpenConstructionERP repository](https://github.com/datadrivenconstruction/OpenConstructionERP)**. Stars are how we gauge demand and prioritise the next country / language / source to publish. No account needed beyond GitHub, no signup, no money — just a one-click thank-you that directly steers what gets built next.

## License

Released under **Apache-2.0** for the dataset structure, normalisation pipeline, and derived metadata. Underlying rate codes and prices are sourced from publicly available national catalogues — each catalogue's terms of use apply to commercial redistribution of raw numeric values.

## Citation

```bibtex
@dataset{cwicr_rates_2026,
  author    = {Boiko, Artem and DataDrivenConstruction},
  title     = {CWICR — Construction Works, Items, Costs \& Resources (30 Countries)},
  year      = {2026},
  publisher = {Hugging Face},
  url       = {https://huggingface.co/datasets/DataDrivenConstruction/cwicr-construction-rates}
}
```

## Contact

- Source code & issue tracker: <https://github.com/datadrivenconstruction/OpenConstructionEstimate-DDC-CWICR>
- Author: Artem Boiko (DataDrivenConstruction)
- Email: boikoartem@gmail.com
