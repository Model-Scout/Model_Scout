---
license: cc-by-nc-nd-4.0
task_categories:
  - table-question-answering
  - image-to-text
  - document-question-answering
language:
  - ar
  - zh
  - en
  - fr
  - de
  - ja
  - ko
  - ru
  - es
size_categories:
  - 1K<n<10K
tags:
  - table-extraction
  - benchmark
  - multilingual
  - document-ai
  - t-lag
  - ocr
configs:
  - config_name: default
    data_files:
      - split: train
        path: data/train-*.parquet
  - config_name: results
    data_files:
      - split: train
        path: results/train-*.parquet
---

# PulseBench-Tab

**A frontier multilingual benchmark for table extraction from document images.**

PulseBench-Tab contains 1,820 human-annotated tables across 9 languages (English 589, Chinese 213, Spanish 176, Russian 170, French 165, Japanese 164, Arabic 146, German 113, Korean 84) and 4 scripts (Latin, CJK, Arabic, Cyrillic), sourced from 380 unique documents including financial filings, government reports, corporate disclosures, and regulatory filings. Each sample is a table image paired with a ground truth HTML table that preserves full structural markup (rowspan, colspan, thead, tbody).

- **Scoring methodology (GitHub):** `https://github.com/Pulse-Software-Corp/PulseBench-Tab`
- **Research paper (arXiv):** `https://benchmark.runpulse.com/research-report`

## Quick Start

```python
from datasets import load_dataset

# Load benchmark data (images + ground truth)
ds = load_dataset("pulse-ai/PulseBench-Tab")

sample = ds["train"][0]
sample["image"]                # PIL Image of the table
sample["ground_truth_html"]    # Ground truth HTML table
sample["language"]             # e.g. "english", "arabic", "japanese"

# Load provider results with T-LAG scores
results = load_dataset("pulse-ai/PulseBench-Tab", "results")

row = results["train"][0]
row["provider"]          # e.g. "pulse_optimized"
row["prediction_html"]   # Provider's extracted HTML
row["tlag_score"]        # T-LAG score (0-1)
```

## Dataset Overview

| Language | Samples | % of Dataset |
|----------|---------|-------------|
| English | 594 | 32.6% |
| Chinese | 213 | 11.7% |
| Spanish | 176 | 9.7% |
| Russian | 170 | 9.3% |
| French | 165 | 9.1% |
| Japanese | 159 | 8.7% |
| Arabic | 146 | 8.0% |
| German | 113 | 6.2% |
| Korean | 84 | 4.6% |

Tables range in complexity from 2 to 1,183 cells, with 48.1% containing merged or spanning cells.

## Scoring: T-LAG

T-LAG (Table Logical Adjacency Graph) is a novel evaluation metric that models tables as 2D directed graphs and evaluates both structural and content fidelity in a single score.

1. **Parse** ground truth and predicted HTML into cell-position grid matrices
2. **Extract directed edges** (RIGHT and BELOW) between adjacent cells, deduplicated for spanning cells
3. **Weigh edges** using a text similarity kernel: Psi(a, b) = (1 - d_Lev(a,b) / max(|a|,|b|))^7
4. **Match** ground truth and predicted edge sets via the Hungarian algorithm (direction-constrained)
5. **Score** as F1 on matched edge weights

Full mathematical specification is available in the research paper.

## Results

We evaluated 9 providers on all 1,820 samples using T-LAG. Providers are scored only on samples where they produced output (exclude-missing mode).

| Rank | Provider | T-LAG Score | Coverage | Perfect | Run |
|------|----------|------------|----------|---------|-----|
| 1 | **Pulse Ultra 2** | **0.9347** | 100.0% | 1053 | 2026-04 |
| 2 | Claude Fable 5.1 | 0.8904 | 99.3% | 616 | 2026-09 |
| 3 | Gemini 3.8 Flash | 0.8857 | 99.9% | 619 | 2026-09 |
| 4 | GPT-6 Astra | 0.8852 | 99.6% | 571 | 2026-09 |
| 5 | GPT-5.6 Sol | 0.8808 | 99.0% | 531 | 2026-09 |
| 6 | Mistral OCR 4.1 | 0.8569 | 97.5% | 553 | 2026-09 |
| 7 | LlamaParse (Agentic) | 0.8396 | 96.4% | 407 | 2026-09 |
| 8 | Extend 2.0 | 0.8244 | 93.1% | 369 | 2026-09 |
| 9 | LlamaParse (Agentic Plus) | 0.8207 | 98.3% | 484 | 2026-09 |
| 10 | Reducto r-1 | 0.8139 | 94.6% | 393 | 2026-09 |
| 11 | Reducto (Agentic) | 0.8133 | 94.8% | 394 | 2026-09 |
| 12 | LlamaParse (Cost Effective) | 0.7789 | 96.0% | 301 | 2026-09 |
| 13 | Datalab | 0.7774 | 91.2% | 316 | 2026-04 |
| 14 | Azure Document Intelligence | 0.7614 | 92.0% | 211 | 2026-04 |
| 15 | Extend (Lite) | 0.7547 | 92.7% | 300 | 2026-09 |
| 16 | Reducto | 0.7115 | 94.8% | 193 | 2026-09 |
| 17 | Snowflake Document AI | 0.7078 | 96.0% | 267 | 2026-04 |
| 18 | Databricks Document AI | 0.6297 | 99.7% | 205 | 2026-04 |

Full results across all 17 evaluated providers -- including per-language breakdowns -- are available in the research paper.

## Schema

### Default config
| Column | Type | Description |
|--------|------|-------------|
| `sample_id` | string | Unique identifier |
| `image` | image | Table image (PNG) |
| `ground_truth_html` | string | Ground truth HTML table |
| `language` | string | One of 9 languages |
| `table_stats` | string | JSON with rows, cols, cells, span_cells, grid_area |

### Results config
| Column | Type | Description |
|--------|------|-------------|
| `sample_id` | string | Links to default config |
| `provider` | string | Provider directory name |
| `display_name` | string | Provider display name |
| `prediction_html` | string | Provider's extracted HTML table |
| `tlag_score` | float | T-LAG score (0-1) |

## License

This dataset is released under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).

## Languages

| Language | Samples | Share |
|---|---|---|
| English | 589 | 32.4% |
| Chinese | 213 | 11.7% |
| Spanish | 176 | 9.7% |
| Russian | 170 | 9.3% |
| French | 165 | 9.1% |
| Japanese | 164 | 9.0% |
| Arabic | 146 | 8.0% |
| German | 113 | 6.2% |
| Korean | 84 | 4.6% |

## Dataset changelog

### v2 (2026-09-10)
- Language labels re-verified against every ground-truth table (script analysis + statistical detection + manual review of every disagreement); 5 labels corrected (japanese_0031, japanese_0078, japanese_0124, japanese_0279, japanese_0298: english → japanese, bilingual tables with Japanese headers).
- 160 sample ids renamed so the id prefix matches the verified language (`legacy_sample_id` keeps the original id; `source_collection` keeps the original collection tag such as `english_sec`, `greek_historical`).
- Ground-truth files now carry `<html lang="xx">` and `legacy-sample-id` / `language` meta tags.
- Results layout unified to `results/<provider>/<language>/<sample_id>.html` for every provider.
- September 2026 reruns added: Reducto, Reducto r-1, Reducto (Agentic), LlamaParse (Cost Effective), LlamaParse (Agentic), LlamaParse (Agentic Plus), Extend 2.0, Extend (Lite), Claude Fable 5.1, Gemini 3.8 Flash, GPT-6 Astra, GPT-5.6 Sol, Mistral OCR 4.1; superseded April rows kept in the scores file as unpublished history.
- Known data-quality flag: `chinese_0282` (legacy arabic_0416) ground truth contains placeholder boxes for some Chinese characters.
