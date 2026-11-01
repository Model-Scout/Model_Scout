---
license: cc-by-4.0
language:
- ko
task_categories:
- image-to-text
tags:
- ocr
- benchmark
- korean
- pdf
- table
- header-footer
pretty_name: KDoc-OCRBench-V2
size_categories:
- 10K<n<100K
---

# KDoc-OCRBench-V2

A Korean document OCR benchmark, built in the style of [olmOCR-Bench](https://huggingface.co/datasets/allenai/olmOCR-bench). 849 single-page PDFs from Korean public-sector documents with **56,197 manually-reviewed unit tests** across three categories.

## Quick summary

849 single-page PDFs. Every PDF has at least one verified test in some category (no PDF is empty).

| Category | Tests | Type | PDFs covered |
|---|---:|---|---:|
| `text_present` | 6,290 | sentence-level presence | 780 / 849 |
| `tables` | 49,115 | table cell + adjacency | 760 / 849 |
| `header_footer_tests` | **792** | header/footer absence | 632 / 849 |
| **Total** | **56,197** | | **849 / 849** (union) |

All tests are `verified` after human review (`rejected` units are excluded).

## Document categories

Each PDF is labelled with one of four broad categories (classified by GPT-5.5 from filename + paddle-vl markdown excerpt). Per-PDF labels are in `categories.jsonl` (`{pdf, category, raw}`).

| Category | Count | % |
|---|---:|---:|
| Statistics | 283 | 33.3 |
| Reports    | 238 | 28.0 |
| Manuals    | 216 | 25.4 |
| Notices    | 112 | 13.2 |

- **Statistics** — numerical data, yearbooks, indicators, time-series tables
- **Reports** — research / survey / analysis / evaluation reports
- **Manuals** — guidelines, manuals, standards, exam criteria, operating procedures
- **Notices** — public announcements, recruitment, press releases, financial disclosures

## Layout

```
.
├── pdfs/                          # 849 single-page Korean public-sector PDFs (flat layout, basename only)
│   └── <basename>.pdf
├── text_present.jsonl             # 6,290 PRESENT-type tests
├── tables.jsonl                   # 49,115 TABLE-type tests
├── header_footer_tests.jsonl      # 792 ABSENT-type tests (headers + footers)
└── licenses.csv                   # per-PDF license info (filename / license / source_url / attribution)
```

## Test types

This benchmark follows the olmOCR-Bench conventions and uses three of its test types:

### `text_present`
Each unit asserts that a short text fragment appears anywhere in the OCR output of the given page. Matching uses [`rapidfuzz.fuzz.partial_ratio`](https://rapidfuzz.github.io/RapidFuzz/Usage/fuzz.html#partial-ratio) with a per-test `max_diffs` tolerance.

```json
{"pdf": "<file>.pdf", "page": 1, "id": "...", "type": "present",
 "text": "...sentence...", "case_sensitive": true,
 "first_n": null, "last_n": null,
 "max_diffs": 0, "checked": "verified"}
```

### `tables`
Each unit asserts that a cell with the given text exists somewhere in any table parsed from the OCR output, and that some neighboring cells match expected values. Cell matching uses `rapidfuzz.fuzz.ratio` (full-string) with `max_diffs` tolerance, floored at 50% similarity. Any subset of `up / down / left / right / top_heading / left_heading` may be specified; only non-empty relationships are checked.

```json
{"pdf": "<file>.pdf", "page": 1, "id": "...", "type": "table",
 "cell": "1,659,061",
 "up": "가입자 Insured", "down": "가입자 Insured",
 "left": "(세대수) (Households)", "right": "1,144,395",
 "top_heading": "1990", "left_heading": "(세대수) (Households)",
 "max_diffs": 0, "checked": "verified"}
```

### `header_footer_tests` (ABSENT)
Each unit asserts that a header/footer text string **must NOT appear** in the OCR output's edge region. This evaluates whether the OCR system properly removes page-level chrome (page numbers, running heads, footers) rather than including them in the body.

- **Header tests** use `first_n=300` — checked only in the first 300 characters of OCR output.
- **Footer tests** use `last_n=300` — checked only in the last 300 characters.

If the text appears within the search window with fuzzy similarity ≥ `threshold`, the OCR system fails (header/footer leaked into output). If not found, the OCR system passes (chrome correctly removed).

```json
{"pdf": "<file>.pdf", "page": 1, "id": "..._pg1_header_00", "type": "absent",
 "text": "경상북도 포항시", "case_sensitive": true,
 "first_n": 300, "last_n": null,
 "max_diffs": 1, "checked": "verified"}

{"pdf": "<file>.pdf", "page": 1, "id": "..._pg1_footer_00", "type": "absent",
 "text": "19 / 53", "case_sensitive": true,
 "first_n": null, "last_n": 300,
 "max_diffs": 0, "checked": "verified"}
```

Note: for ABSENT, higher `max_diffs` makes the test **stricter** (catches OCR output variants like `"19/53"` vs `"19 / 53"`).

## Usage

The dataset is plug-compatible with the official `olmocr` bench tooling.

```bash
# 1) Install olmocr (or use this repo's bench package)
git clone https://github.com/allenai/olmocr.git
cd olmocr
pip install -e .[bench]

# 2) Download this dataset
huggingface-cli download --repo-type dataset ONTHEIT/KDoc-OCRBench-V2 \
    --local-dir ./KDoc-OCRBench-V2

# 3) Run an OCR system to produce candidate outputs
python -m olmocr.bench.convert chatgpt --dir ./KDoc-OCRBench-V2 --parallel 20
# (other supported methods: gemini, mistral, marker, mineru, olmocr_pipeline, etc.)

# 4) Score
python -m olmocr.bench.benchmark --dir ./KDoc-OCRBench-V2 \
    --bootstrap_samples 1000 --confidence_level 0.95 \
    --test_report results.html \
    --output_failed failed_tests.jsonl
```

Each candidate's outputs land in `./KDoc-OCRBench-V2/<method>/<basename>_pg1_repeat1.md`, and `benchmark.py` scores per category.

## Construction pipeline

1. **Source PDFs** — 849 single-page documents from Korean public-sector portals, spanning 323 distinct issuing institutions across multiple ministries, public corporations, and local governments. Document types include statistical yearbooks, regulations, manuals, posters, and bulletins.
2. **Silver labels** — Per-page silver text generated by **GPT-5.5** using the [`build_openai_silver_data_prompt_v3_simple`](https://github.com/allenai/olmocr/blob/main/olmocr/prompts/prompts.py) prompt: HTML tables, LaTeX equations, headers/footers stripped. Each page returns the full olmOCR `PageResponse` schema (language, rotation, table/diagram flags, natural text).
3. **Auto unit generation** —
   - `text_present` / `tables`: derived from the silver text by sentence-splitting prose and per-cell table enumeration with grid neighbors.
   - `header_footer_tests`: separately extracted via an additional GPT-5.5 call per page using a structured-output schema `{headers: [str], footers: [str]}`. Each detected string becomes one ABSENT test with `first_n` (header) or `last_n` (footer) scoping.
4. **Manual review** — 117K + 1.1K auto-generated units distributed across reviewers via per-port buckets using the olmOCR `review_app`. Reviewers approve / reject / edit each unit, with the option to adjust `max_diffs` for legitimate OCR variation.
5. **Per-page cap** — A cap of 200 tests per page was applied mid-review on `tables` to balance reviewer workload: all `text_present` preserved, all already-reviewed units preserved, and any excess null `table` units randomly sub-sampled. No reviewed work was lost.
6. **Final filter** — Only `verified` units are kept. `rejected` and `null` are excluded. PDFs with all tests rejected are dropped.

For details on the matching engine and `max_diffs` semantics, see the upstream [olmocr/bench/tests.py](https://github.com/allenai/olmocr/blob/main/olmocr/bench/tests.py).

## Benchmark results

Per-category pass rate (%) on the full 849-PDF / 56,197-test benchmark. Overall = mean of the four per-JSONL pass rates.

| Model           | Baseline | Header/Footer | Long Text | Table | Overall |
|-----------------|---------:|--------------:|----------:|------:|--------:|
| **BizOnAI-OCR** |     98.6 |          94.7 |  **77.9** | **58.1** | **82.3** |
| PaddleOCR-VL    |    100.0 |          95.6 |      66.2 |  48.9 |    77.7 |
| DeepSeek OCR    |     99.9 |          95.8 |      64.5 |  46.6 |    76.7 |
| olmOCR v0.2.0   |     99.9 |          95.2 |      65.0 |  44.9 |    76.3 |
| GLM OCR         |     99.2 |      **97.4** |      20.0 |  30.0 |    61.7 |

Column mapping: **Baseline** = auto-generated baseline tests, **Header/Footer** = `header_footer_tests.jsonl` (ABSENT), **Long Text** = `text_present.jsonl` (PRESENT), **Table** = `tables.jsonl`.

## Notes & limitations

- **Single-page only**: one source PDF (53-page training-criteria document) was excluded because it was not page-split like the other documents, to keep the benchmark uniformly single-page.
- **Test asymmetry**: `text_present` uses substring matching (lenient); `tables` uses full-cell matching with a 0.5 similarity floor; `header_footer_tests` uses substring matching scoped to edge regions (first/last 300 chars). Reviewers may have adjusted `max_diffs` on individual cells/headers to allow OCR-typical variations.
- **`text_present` density** is intentionally sparse — only a few distinctive sentences per page are kept.
- **`header_footer_tests` coverage**: 632 of the 849 PDFs have at least one verified header/footer unit. The remaining 217 PDFs either have no visible page chrome or all GPT-detected candidates were rejected as false positives.
- **Reading order, math, and footnote test types are not included** in this release. They can be added in a follow-up by extending the mining pipeline.
- **PDF source rights**: all 849 source PDFs are Korean public-sector publications under one of two open terms — 677 PDFs with no usage restrictions, and 172 PDFs under [KOGL Type 1](https://www.kogl.or.kr/info/license.do) (attribution-only). See `licenses.csv` for per-file license, source URL on [data.go.kr](https://www.data.go.kr/), and attribution requirement.

## License

This dataset has **two distinct rights layers** — please treat them separately.

- **Annotations** (the jsonl test units) — © ONTHEIT, released under **CC BY 4.0**. The `cc-by-4.0` tag on this dataset refers to this layer. Attribute ONTHEIT when you use the tests.
- **Source PDFs** — redistributed under each publisher's **original Korean public-data terms**; they are **NOT relicensed** by ONTHEIT. Two terms apply:
  - **677 PDFs (79.7%)** — `이용허락범위 제한없음` (no usage restrictions, public-domain-like): **no attribution required**.
  - **172 PDFs (20.3%)** — [KOGL Type 1](https://www.kogl.or.kr/info/license.do) (`공공저작물 출처표시` / 공공누리 제1유형): commercial use and modification allowed, but **attribution required**. When you reuse these files, include the publisher attribution string provided per-file in `licenses.csv`.

Per-file license, source URL on [data.go.kr](https://www.data.go.kr/) (or the publishing institution), and the ready-to-use attribution string are listed in `licenses.csv` (`filename, license, source_url, attribution`).

## Citation

Citation TBD.

## Contact

[ONTHEIT](http://www.ontheit.com/) — bizonai@ontheit.com
