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
  - 1K<n<10K
configs:
  - config_name: default
    data_files:
      - split: train
        path: "data/train-*.parquet"
---

# Sinabis Green Energy – Synthetic Document Dataset (1k PPTX)

**1,010 business presentations (.pptx)** from the everyday operations of a fictional group of
**Sinabis** companies (Sinabis Green Energy, Sinabis Bank, Sinabis Logistics, Sinabis Electric …) – every
organisation in the data carries the Sinabis name.

This is the 1k edition of [sinabis-1m-synthetic-pptx](https://huggingface.co/datasets/sinabis-group/sinabis-1m-synthetic-pptx):
the first 1,010 presentations of the 1M dataset (`idx` 0 to 1,009). File names, folder paths and manifest
records are identical to the 1M dataset, and this edition is the first part of the [10k edition](https://huggingface.co/datasets/sinabis-group/sinabis-10k-synthetic-pptx) and [100k edition](https://huggingface.co/datasets/sinabis-group/sinabis-100k-synthetic-pptx),
so all editions can be used side by side.

Every person, company, address, phone number, financial figure and project in this dataset is **purely fictional**.
Deck contents come from LLM-written blueprints (Gemma 4 26B-A4B) in the target language: an outline per deck, then
fully written slides in blocks of seven (6–45 slides per deck), each with layout, content and speaker notes.
Slides are rendered with `python-pptx` in 17 layouts (title, agenda, section, bullets, two/three columns, KPI tiles,
table, native chart, timeline, process, quote, comparison, team, image + text, FAQ, closing) and deck-level design
variants (16:9/4:3, background, title position, accent, logo position, footer, card style, fonts).

> All figures in this dataset card were **computed directly from the files in this edition**
> (as of 23 Oct 2026). They are not target estimates.

## At a glance

| Metric | Value |
|---|---|
| Total Presentations | **1,010** `.pptx` presentations (102 MB uncompressed, 85 MB in 1 ZIP archive) |
| Total Slides | **18,404** slides (average 18.2 slides per presentation, 6–45) |
| Aspect Ratio | **16:9** widescreen for 907 decks (89.8 %), **4:3** for 103 decks (10.2 %) |
| Native Charts & Tables | **804** decks (79.6 %) with native charts, **872** (86.3 %) with tables |
| Speaker Notes | Ø **1,361** words of speaker notes per presentation |
| Document Themes | **20** distinct business themes in 5 families |
| Time Span | **2014-11-10** to **2026-06-30** (11.6 years of corporate evolution) |
| Languages | **24** languages (EN 80.4 %, ZH 5.4 %, rest across 22 languages) |
| Issuing Organisations | **753** fictional companies across **33** countries |
| Partner Organisations | **117** distinct named recipients (partners, suppliers, clients); 77.0 % of decks are internal |

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
| `sales_pitch` | 75 | 7.4 % | Customer presentation with ROI calculation, savings potential and PPA transformation concept |
| `project_kickoff` | 68 | 6.7 % | Project kick-off presentation with milestone plan, work packages, budgets and risk matrix |
| `corporate_presentation` | 66 | 6.5 % | Company overview, vision, business areas, global presence and core KPIs |
| `project_review` | 65 | 6.4 % | Construction and project progress report with actual costs, earned value and next steps |
| `case_study` | 60 | 5.9 % | Customer reference with load profile optimisation, peak shaving and testimonial feedback |
| `system_architecture` | 55 | 5.4 % | Technical system architecture for power plant control, BESS and grid integration |
| `strategy_roadmap` | 55 | 5.4 % | Multi-year transformation roadmap with innovation clusters, capex and target states |
| `product_catalog` | 55 | 5.4 % | Product overview with storage series (C&I, utility), efficiency ratings and warranties |
| `budget_review` | 55 | 5.4 % | Financial and budget review with target/actual cost-centre variances and forecast |
| `maintenance_briefing` | 51 | 5.0 % | O&M service briefing with availability figures, maintenance packages and 5 safety rules |
| `hse_briefing` | 48 | 4.8 % | Occupational safety briefing with golden rules, mandatory PPE and stop-work authority |
| `quality_audit` | 47 | 4.7 % | Quality audit report under ISO 9001 with CAPA corrective actions and top ratings |
| `supply_chain` | 43 | 4.3 % | Global sourcing strategy with OTIF delivery performance, buffer stocks and LkSG supply chain audits |
| `board_deck` | 42 | 4.2 % | Board report with strategic goals, segment results, investment plan and governance |
| `compliance_training` | 42 | 4.2 % | Code of conduct, anti-corruption, gifts policy and whistleblowing portal |
| `partnership_deck` | 42 | 4.2 % | Strategic partnership with R&D goals, joint go-to-market and aftersales SLA |
| `incident_report` | 39 | 3.9 % | Incident investigation (RCA) using the 5-why method with corrective actions and fleet lessons learned |
| `esg_report` | 39 | 3.9 % | Sustainability report with scope 1/2/3 emissions, occupational safety and biodiversity |
| `employee_onboarding` | 34 | 3.4 % | Welcome deck for new employees with culture, tools, buddy and 90-day plan |
| `townhall_meeting` | 29 | 2.9 % | Group-wide quarterly all-hands meeting with business-unit updates, financial highlights and Q&A |

## Language distribution

The language of each presentation is determined by the issuing organisation's jurisdiction and recorded in the manifests:

| Language | Presentations | **Share** |
|---|---:|---:|
| English (`en`) | 812 | **80.4 %** |
| Chinese (`zh`) | 55 | **5.4 %** |
| Japanese (`ja`) | 50 | **5.0 %** |
| German (`de`) | 18 | **1.8 %** |
| Finnish (`fi`) | 9 | **0.9 %** |
| Portuguese (`pt`) | 7 | **0.7 %** |
| Polish (`pl`) | 7 | **0.7 %** |
| Indonesian (`id`) | 6 | **0.6 %** |
| Dutch (`nl`) | 6 | **0.6 %** |
| Swedish (`sv`) | 6 | **0.6 %** |
| Korean (`ko`) | 5 | **0.5 %** |
| Italian (`it`) | 4 | **0.4 %** |
| Spanish (`es`) | 4 | **0.4 %** |
| Ukrainian (`uk`) | 3 | **0.3 %** |
| French (`fr`) | 3 | **0.3 %** |
| Vietnamese (`vi`) | 3 | **0.3 %** |
| Danish (`da`) | 3 | **0.3 %** |
| Hungarian (`hu`) | 2 | **0.2 %** |
| Romanian (`ro`) | 2 | **0.2 %** |
| Russian (`ru`) | 1 | **0.1 %** |
| Czech (`cs`) | 1 | **0.1 %** |
| Turkish (`tr`) | 1 | **0.1 %** |
| Norwegian (`nb`) | 1 | **0.1 %** |
| Greek (`el`) | 1 | **0.1 %** |

## Design DNA & Visual Hierarchy

Each presentation adheres to strict corporate design standards matching the Sinabis document family:
- **16:9 Widescreen and 4:3 Canvas**: 89.8 % widescreen, 10.2 % classic 4:3; professional layout with precise millimeter typography and safe margins.
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

The Parquet file under `data/` holds one row per presentation: all manifest fields plus the extracted
text, so the dataset can be browsed in the Dataset Viewer above and loaded directly:

```python
from datasets import load_dataset

ds = load_dataset("sinabis-group/sinabis-1k-synthetic-pptx", split="train")
print(ds[0]["title"], ds[0]["slides"], "slides")
print(ds[0]["text"])     # slide text
print(ds[0]["notes"])    # speaker notes
```

The `text` column holds the slide text, slide by slide, each introduced by `[Slide N]`. The `notes` column holds the speaker notes in the same format; they are often longer than the slides themselves. The original `.pptx` files with layouts, charts and tables are in the ZIP archive.

## Downloads

| File | Size | Contents |
|---|---:|---|
| `data/train-*.parquet` (1 file) | 7 MB | Manifest fields + `text` (slides) + `notes` (speaker notes), one row per presentation (Dataset Viewer, `load_dataset`) |
| `Sinabis_1k_pptx.zip` | 85 MB | `1,010` PPTX files + manifest (102 MB uncompressed) |

`Sinabis_1k_pptx_manifest.zip` (0.3 MB) holds only the JSON Lines manifest records for all 1,010
presentations, for a quick look at the metadata without downloading the decks (see "Metadata & Manifest" below).

### Unpacking

Both archives share one directory structure. The presentation archive already contains the manifest, so
`unzip -o` simply overwrites identical files:

```bash
hf download sinabis-group/sinabis-1k-synthetic-pptx --repo-type dataset --local-dir sinabis-1k-pptx
cd sinabis-1k-pptx
for z in Sinabis_1k_pptx*.zip; do unzip -qo "$z"; done
```

## Folder structure

In the repository:

```
.
├── README.md
├── data/
│   └── train-*.parquet                 (rows for the Dataset Viewer and load_dataset)
├── Sinabis_1k_pptx.zip             → pptx/ + manifest/
└── Sinabis_1k_pptx_manifest.zip    → manifest/
```

After unpacking:

```
sinabis-1k-pptx/
├── pptx/
│   ├── board_deck/
│   │   ├── 0000/
│   │   │   ├── 0000000_PRS-2016-84085.pptx
│   │   │   └── ...
│   │   └── ... (0000 to 0001)
│   ├── project_kickoff/
│   ├── esg_report/
│   └── ... (20 themes)
└── manifest/
    ├── pb00000.jsonl
    ├── ...
    └── pb00002.jsonl
```

## Metadata & Manifest

Each `pbNNNNN.jsonl` contains 500 records (the last shard 10), one per presentation. A real record from this dataset
(`slide_titles`, the list of all slide titles, omitted for brevity):

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

Besides the identifying fields (`idx`, `file`, `theme`, `issuer_id`, `issuer`, `issuer_country`, `recipient`,
`recipient_kind`, `lang`, `date`, `number`, `currency`, `title`), each record carries:
- `family`, `blueprint_id`, `length_class`: Theme family, source blueprint (`<theme>_<lang>_<n>`) and length class (S/M/L/XL)
- `slides`, `layouts`: Slide count and number of slides per slide layout
- `charts`, `tables`, `notes_words`: Native charts, tables and words of speaker notes
- `confidentiality`: Confidentiality label printed on the slides
- `layout_*`: Deck-level design decisions (format, background, title position, accent, logo position, footer, card style, font, slide layouts used)
- `slide_titles`: Titles of all slides in order
- `bytes`: Exact byte size of the `.pptx` file

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

> Sinabis GmbH (2026). Sinabis Green Energy – Synthetic Document Dataset (1k PPTX).
> https://huggingface.co/datasets/sinabis-group/sinabis-1k-synthetic-pptx

## Citation

```bibtex
@misc{sinabis_green_pptx_1k_dataset_2026,
  author = {{Sinabis GmbH}},
  title  = {Sinabis Green Energy -- Synthetic Document Dataset (1k PPTX)},
  year   = {2026},
  url    = {https://huggingface.co/datasets/sinabis-group/sinabis-1k-synthetic-pptx}
}
```
