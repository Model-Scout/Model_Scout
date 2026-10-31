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
  - sv
  - nl
  - ko
  - pl
  - id
  - hu
  - da
  - fi
  - nb
  - tr
  - uk
  - cs
  - el
  - vi
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
  - powerpoint
  - presentation
  - presentations
  - pptx
  - slides
  - slide-deck
  - corporate
  - strategy
  - enterprise
  - business-documents
  - digital-forensics
  - forensics
  - e-discovery
  - renewable-energy
  - multilingual
  - llm
  - llm-training
  - pretraining
  - nlp
  - information-extraction
  - visual-document-understanding
size_categories:
  - 1M<n<10M
configs:
  - config_name: default
    data_files:
      - split: train
        path: "data/train-*.parquet"
---

# Sinabis Green Energy – Synthetic Document Dataset (1M PPTX)

More than **1,005,852 business presentations (.pptx)** from the everyday operations of a fictional group of
**Sinabis** companies (Sinabis Green Energy, Sinabis Bank, Sinabis Logistics, Sinabis Electric …) – every
organisation in the data carries the Sinabis name.

Every person, company, address, phone number, financial figure and project in this dataset is **purely fictional**.
Deck contents come from LLM-written blueprints (Gemma 4 26B-A4B) in the target language: an outline per deck, then
fully written slides in blocks of seven (6–45 slides per deck), each with layout, content and speaker notes.
Slides are rendered with `python-pptx` in 17 layouts (title, agenda, section, bullets, two/three columns, KPI tiles,
table, native chart, timeline, process, quote, comparison, team, image + text, FAQ, closing) and deck-level design
variants (16:9/4:3, background, title position, accent, logo position, footer, card style, fonts).

> All figures in this dataset card were **computed directly from the generated files**
> (as of 21 Oct 2026). They are not target estimates.

## At a glance

| Metric | Value |
|---|---|
| Total Presentations | **1,005,852** `.pptx` presentations (102.1 GB uncompressed, 86.2 GB in 26 ZIP archives) |
| Total Slides | **18,410,591** slides (average 18.3 slides per presentation) |
| Aspect Ratio | **16:9 Widescreen** (13.333" x 7.500") for most decks, **4:3** for the rest (about 10 % in a sample of 101,000 decks) |
| Document Themes | **20** distinct business themes |
| Time Span | **2011-04-03** to **2026-06-30** (15.2 years of corporate evolution) |
| Languages | **24** languages (EN 81.2 %, JA 4.9 %, rest across 22 languages) |
| Issuing Organisations | **2,014** fictional companies across **33** countries |
| Partner Organisations | **23,681** corporate partners, suppliers, utilities and clients |
| Visual Brand DNA | Unique primary/secondary colors, header chromes, fonts and high-res vector logos |

## What it is about

**Sinabis Green Energy** (headquartered in Austin, Texas, fictional) develops, constructs,
operates and finances utility-scale renewable energy infrastructure:
- **Solar & Storage**: Rooftop PV, floating solar parks, utility-scale bifacial tracker arrays, and multi-megawatt battery energy storage systems (BESS).
- **Wind & Microgrids**: Onshore and offshore wind farms, smart grid controllers, SCADA power plant automation.
- **Clean Transport & Charging**: Mega-watt EV fleet charging hubs, autonomous campus shuttles, battery swap logistics.
- **Circular Resources**: Industrial water treatment, ocean plastic recovery, and sustainable building engineering.

### Business units and themes represented

The **20 presentation themes** cover the complete operational spectrum of modern industrial enterprises:

| Theme | Count | Share | Description |
|---|---:|---:|---|
| `project_kickoff` | 59,762 | 5.9 % | Project kick-off presentation with milestone plan, work packages, budgets and risk matrix |
| `project_review` | 59,762 | 5.9 % | Construction and project progress report with actual costs, earned value and next steps |
| `sales_pitch` | 59,762 | 5.9 % | Customer presentation with ROI calculation, savings potential and PPA transformation concept |
| `product_catalog` | 59,762 | 5.9 % | Product overview with storage series (C&I, utility), efficiency ratings and warranties |
| `budget_review` | 59,762 | 5.9 % | Financial and budget review with target/actual cost-centre variances and forecast |
| `corporate_presentation` | 59,614 | 5.9 % | Company overview, vision, business areas, global presence and core KPIs |
| `board_deck` | 49,802 | 5.0 % | Board report with strategic goals, segment results, investment plan and governance |
| `partnership_deck` | 49,802 | 5.0 % | Strategic partnership with R&D goals, joint go-to-market and aftersales SLA |
| `hse_briefing` | 49,802 | 5.0 % | Occupational safety briefing with golden rules, mandatory PPE and stop-work authority |
| `system_architecture` | 49,802 | 5.0 % | Technical system architecture for power plant control, BESS and grid integration |
| `supply_chain` | 49,802 | 5.0 % | Global sourcing strategy with OTIF delivery performance, buffer stocks and LkSG supply chain audits |
| `maintenance_briefing` | 49,802 | 5.0 % | O&M service briefing with availability figures, maintenance packages and 5 safety rules |
| `strategy_roadmap` | 49,802 | 5.0 % | Multi-year transformation roadmap with innovation clusters, capex and target states |
| `case_study` | 49,802 | 5.0 % | Customer reference with load profile optimisation, peak shaving and testimonial feedback |
| `esg_report` | 49,802 | 5.0 % | Sustainability report with scope 1/2/3 emissions, occupational safety and biodiversity |
| `townhall_meeting` | 39,842 | 4.0 % | Group-wide quarterly all-hands meeting with business-unit updates, financial highlights and Q&A |
| `compliance_training` | 39,842 | 4.0 % | Code of conduct, anti-corruption, gifts policy and whistleblowing portal |
| `incident_report` | 39,842 | 4.0 % | Incident investigation (RCA) using the 5-why method with corrective actions and fleet lessons learned |
| `employee_onboarding` | 39,842 | 4.0 % | Welcome deck for new employees with culture, tools, buddy and 90-day plan |
| `quality_audit` | 39,842 | 4.0 % | Quality audit report under ISO 9001 with CAPA corrective actions and top ratings |

## Language distribution

The language of each presentation is determined by the issuing organisation's jurisdiction and recorded in the manifests:

| Language | Presentations | **Share** |
|---|---:|---:|
| English (`en`) | 817,061 | **81.2 %** |
| Japanese (`ja`) | 49,306 | **4.9 %** |
| Chinese (`zh`) | 47,393 | **4.7 %** |
| German (`de`) | 16,957 | **1.7 %** |
| Portuguese (`pt`) | 8,430 | **0.8 %** |
| Spanish (`es`) | 8,214 | **0.8 %** |
| Italian (`it`) | 6,268 | **0.6 %** |
| French (`fr`) | 6,013 | **0.6 %** |
| Swedish (`sv`) | 4,937 | **0.5 %** |
| Dutch (`nl`) | 4,370 | **0.4 %** |
| Korean (`ko`) | 4,125 | **0.4 %** |
| Polish (`pl`) | 4,074 | **0.4 %** |
| Indonesian (`id`) | 3,675 | **0.4 %** |
| Hungarian (`hu`) | 3,039 | **0.3 %** |
| Danish (`da`) | 2,742 | **0.3 %** |
| Finnish (`fi`) | 2,617 | **0.3 %** |
| Norwegian (`nb`) | 2,293 | **0.2 %** |
| Turkish (`tr`) | 2,291 | **0.2 %** |
| Ukrainian (`uk`) | 2,283 | **0.2 %** |
| Czech (`cs`) | 2,258 | **0.2 %** |
| Greek (`el`) | 2,142 | **0.2 %** |
| Vietnamese (`vi`) | 2,048 | **0.2 %** |
| Romanian (`ro`) | 2,037 | **0.2 %** |
| Russian (`ru`) | 1,279 | **0.1 %** |

## Design DNA & Visual Hierarchy

Each presentation adheres to strict corporate design standards matching the Sinabis document family:
- **16:9 Widescreen and 4:3 Canvas**: Professional layout with precise millimeter typography and safe margins.
- **Embedded Vector/Raster Logos**: Crisp branding matching the company's industry and country.
- **Executive Header & Footer Chrome**: Category kicker, bold titles, subtitle hierarchy, date, confidentiality level, and slide counter (`Slide X of Y`).
- **Diverse Slide Archetypes**:
  - **Title Slide**: Brand-colored or dark-mode hero banner with corporate metadata.
  - **KPI Dashboard**: Multi-tile metrics with key values, trend badges and takeaway boxes.
  - **Structured Column Cards**: 3-column modular cards with priority badges and bullet streams.
  - **Milestone Timelines**: Horizontal multi-step roadmaps from project kickoff to commissioning.
  - **Styled Tables**: Crisp bordered tables with highlighted headers and sum rows.
  - **Takeaway / Closing Slides**: Executive call-to-action with verified contact details.

## Quick start

The Parquet files under `data/` hold one row per presentation: all manifest fields plus the extracted
text, so the dataset can be browsed in the Dataset Viewer above and loaded directly:

```python
from datasets import load_dataset

ds = load_dataset("sinabis-group/sinabis-1m-synthetic-pptx", split="train")
print(ds[0]["title"], ds[0]["slides"], "slides")
print(ds[0]["text"])     # slide text
print(ds[0]["notes"])    # speaker notes
```

The `text` column holds the slide text, slide by slide, each introduced by `[Slide N]`. The `notes` column holds the speaker notes in the same format; they are often longer than the slides themselves. The original `.pptx` files with layouts, charts and tables are in the ZIP archive.

## Downloads

The dataset is partitioned into 26 ZIP archives (about 3.4 GB each, the last one 1.4 GB), enabling selective downloading and parallel streaming:

| File | Size | Contents |
|---|---:|---|
| `data/train-*.parquet` (11 files) | 6.92 GB | Manifest fields + `text` (slides) + `notes` (speaker notes), one row per presentation (Dataset Viewer, `load_dataset`) |
| `Sinabis_1M_pptx_part_01.zip` | 3.38 GB | `39,497` PPTX files (4.00 GB uncompressed) |
| `Sinabis_1M_pptx_part_02.zip` | 3.38 GB | `39,494` PPTX files (4.01 GB uncompressed) |
| `Sinabis_1M_pptx_part_03.zip` | 3.39 GB | `39,494` PPTX files (4.01 GB uncompressed) |
| `Sinabis_1M_pptx_part_04.zip` | 3.42 GB | `39,994` PPTX files (4.05 GB uncompressed) |
| `Sinabis_1M_pptx_part_05.zip` | 3.38 GB | `39,493` PPTX files (4.00 GB uncompressed) |
| `Sinabis_1M_pptx_part_06.zip` | 3.39 GB | `39,492` PPTX files (4.02 GB uncompressed) |
| `Sinabis_1M_pptx_part_07.zip` | 3.38 GB | `39,498` PPTX files (4.01 GB uncompressed) |
| `Sinabis_1M_pptx_part_08.zip` | 3.41 GB | `39,993` PPTX files (4.04 GB uncompressed) |
| `Sinabis_1M_pptx_part_09.zip` | 3.39 GB | `39,499` PPTX files (4.01 GB uncompressed) |
| `Sinabis_1M_pptx_part_10.zip` | 3.39 GB | `39,487` PPTX files (4.01 GB uncompressed) |
| `Sinabis_1M_pptx_part_11.zip` | 3.39 GB | `39,493` PPTX files (4.01 GB uncompressed) |
| `Sinabis_1M_pptx_part_12.zip` | 3.39 GB | `39,495` PPTX files (4.01 GB uncompressed) |
| `Sinabis_1M_pptx_part_13.zip` | 3.38 GB | `39,492` PPTX files (4.00 GB uncompressed) |
| `Sinabis_1M_pptx_part_14.zip` | 3.39 GB | `39,496` PPTX files (4.02 GB uncompressed) |
| `Sinabis_1M_pptx_part_15.zip` | 3.42 GB | `39,995` PPTX files (4.05 GB uncompressed) |
| `Sinabis_1M_pptx_part_16.zip` | 3.38 GB | `39,491` PPTX files (4.01 GB uncompressed) |
| `Sinabis_1M_pptx_part_17.zip` | 3.38 GB | `39,494` PPTX files (4.01 GB uncompressed) |
| `Sinabis_1M_pptx_part_18.zip` | 3.39 GB | `39,497` PPTX files (4.02 GB uncompressed) |
| `Sinabis_1M_pptx_part_19.zip` | 3.38 GB | `39,493` PPTX files (4.01 GB uncompressed) |
| `Sinabis_1M_pptx_part_20.zip` | 3.38 GB | `39,497` PPTX files (4.00 GB uncompressed) |
| `Sinabis_1M_pptx_part_21.zip` | 3.42 GB | `39,994` PPTX files (4.05 GB uncompressed) |
| `Sinabis_1M_pptx_part_22.zip` | 3.39 GB | `39,491` PPTX files (4.01 GB uncompressed) |
| `Sinabis_1M_pptx_part_23.zip` | 3.41 GB | `39,995` PPTX files (4.04 GB uncompressed) |
| `Sinabis_1M_pptx_part_24.zip` | 3.39 GB | `39,496` PPTX files (4.02 GB uncompressed) |
| `Sinabis_1M_pptx_part_25.zip` | 3.38 GB | `39,496` PPTX files (4.00 GB uncompressed) |
| `Sinabis_1M_pptx_part_26.zip` | 1.37 GB | `15,996` PPTX files (1.62 GB uncompressed) |

`Sinabis_1M_pptx_manifest.zip` holds the JSON Lines manifest records for all 1,005,852
presentations (see "Metadata & Manifest" below).

### Unpacking

All archives share a unified directory structure. Unpacking them into the same directory
merges all files seamlessly. Each part also contains the manifest files of its own presentations, and the
manifest ZIP bundles all of them, so `unzip -o` simply overwrites identical files:

```bash
hf download sinabis-group/sinabis-1m-synthetic-pptx --repo-type dataset --local-dir sinabis-1m-pptx
cd sinabis-1m-pptx
for z in Sinabis_1M_pptx_*.zip; do unzip -qo "$z"; done
```

## Folder structure

In the repository:

```
.
├── README.md
├── data/
│   └── train-*.parquet                 (rows for the Dataset Viewer and load_dataset)
├── Sinabis_1M_pptx_part_01.zip … part_26.zip    → pptx/ (+ manifest/ shards)
└── Sinabis_1M_pptx_manifest.zip                 → manifest/
```

After unpacking all archives into one directory:

```
sinabis-1m-pptx/
├── pptx/
│   ├── board_deck/
│   │   ├── 0042/
│   │   │   ├── 0042100_BRD-2024-0812.pptx
│   │   │   └── ...
│   │   └── ...
│   ├── project_kickoff/
│   ├── esg_report/
│   └── ... (20 themes)
└── manifest/
    ├── pb00000.jsonl
    ├── pb00001.jsonl
    └── ...
```

## Metadata & Manifest

Each ZIP archive contains the PowerPoint presentations in thematic subfolders alongside the JSON Lines manifest files of its documents (`manifest/pb*.jsonl`). A real record (`slide_titles`, the list of all slide titles, omitted for brevity):

```json
{
  "idx": 0,
  "file": "pptx/board_deck/0000/0000000_PRS-2016-84085.pptx",
  "format": "pptx",
  "theme": "board_deck",
  "issuer_id": "painting-0-8",
  "issuer": "Sinabis Painters Bangkok Co., Ltd.",
  "issuer_country": "th",
  "recipient": "",
  "recipient_kind": "internal",
  "lang": "en",
  "date": "2016-01-23",
  "number": "PRS-2016/84085",
  "currency": "THB",
  "title": "Environmental Compliance & Sustainability Roadmap",
  "bytes": 93708,
  "family": "management",
  "blueprint_id": "board_deck_en_00031",
  "length_class": "M",
  "slides": 16,
  "layouts": {
    "title": 1,
    "agenda": 1,
    "section": 3,
    "kpi": 1,
    "two_column": 1,
    "comparison": 1,
    "three_column": 1,
    "chart": 1,
    "process": 1,
    "timeline": 1,
    "table": 1,
    "quote": 1,
    "faq": 1,
    "closing": 1
  },
  "charts": 1,
  "tables": 1,
  "notes_words": 1415,
  "confidentiality": "Confidential",
  "layout_format": "16:9",
  "layout_background": "white",
  "layout_title_position": "top_left",
  "layout_accent": "none",
  "layout_logo_position": "none",
  "layout_footer": "number_only",
  "layout_card_style": "top_border",
  "layout_font": "Tahoma",
  "layout_slide_layouts": "agenda,chart,closing,comparison,faq,kpi,process,quote,section,table,three_column,timeline,title,two_column"
}
```

## How to use this dataset

### Python (`python-pptx`)

```python
from pptx import Presentation

prs = Presentation("0042100_BRD-2024-0812.pptx")
print(f"Total slides: {len(prs.slides)}")

for idx, slide in enumerate(prs.slides, 1):
    for shape in slide.shapes:
        if shape.has_text_frame:
            for p in shape.text_frame.paragraphs:
                if p.text.strip():
                    print(f"Slide {idx}: {p.text}")
```

### Multimodal Vision & OCR Training

The slides feature high-contrast, structured text, tables, and KPI cards, making them ideal for training vision-language models (VLMs) on slide layout analysis, chart-to-text, and visual document reasoning.

## License

This dataset is released under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.
You are free to share and adapt the material for any purpose, including commercial applications,
provided appropriate credit is given:

> Sinabis GmbH (2026). Sinabis Green Energy – Synthetic Document Dataset (1M PPTX).
> https://huggingface.co/datasets/sinabis-group/sinabis-1m-synthetic-pptx

## Citation

```bibtex
@misc{sinabis_green_pptx_dataset_2026,
  author = {{Sinabis GmbH}},
  title  = {Sinabis Green Energy -- Synthetic Document Dataset (1M PPTX)},
  year   = {2026},
  url    = {https://huggingface.co/datasets/sinabis-group/sinabis-1m-synthetic-pptx}
}
```
