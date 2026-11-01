---
license: cc-by-4.0
language:
  - ko
  - en
tags:
  - finance
  - sentiment-analysis
  - investor-sentiment
  - korean
  - llm-annotations
size_categories:
  - 1M<n<10M
---

# Korean Market Fear & Greed — LLM-Annotated Text Sentiment Dataset

LLM annotations of **1.28 million Korean financial texts** (news headlines and
retail investor community posts) and the resulting **daily fear–greed index** for
the Korean stock market (research period 2021-01 – 2026-08, with a 2019–2020
news-only warm-up segment).

Companion dataset for: *"Measuring fear and greed with large language models:
Evidence from news and retail investor communities in the Korean stock market"*.

## Files

| File | Rows | Description |
|------|------|-------------|
| `news_domestic_annotations.jsonl.gz` | ~195k | Naver Finance main news, 2019–2026. Per-article: `relevant`, `dims` (7 sentiment dimensions, 0=extreme fear…100=extreme greed), `reason`, date/press/URL |
| `community_annotations.jsonl.gz` | ~1.08M | DCinside stock gallery posts, 2021–2026. Per-post: `relevant`, `stance` (bull/bear/neutral), `intensity` (0–100), `type` (position/loss/gain/info/banter), timestamp, post id/URL |
| `news_foreign_annotations.jsonl.gz` | ~8k | Foreign-outlet coverage of Korea (Google News), 2025–2026. Same schema as domestic news. Reference only (zero weight in the index) |
| `daily_index.csv` | ~2.8k | Daily index: official percentile index `pct_ema`, absolute composite `raw_score`, per-source scores, community auxiliaries (`com_vol_z`, `com_disagree`, …), labels. See paper §2 |
| `daily_dims.csv` | — | Long-format per-source per-dimension daily detail |
| `audit/reannotation_audit_2021.jsonl.gz` | 2,000 | Re-annotation audit sample (2021): post ids, original and re-annotated labels; relevance agreement 94.2%, stance 88.3% |

**Original texts are not included** (copyright). Every record carries its source
URL / post id, so texts can be re-fetched. All paper results are reproducible
from the annotations and the daily index alone (scripts included with the paper).

## Annotation pipeline (fully unsupervised)

- Model: DeepSeek (vLLM, OpenAI-compatible), temperature 0, batched JSON outputs
- News: relevance + up to 7 dimension scores (only dimensions the article addresses)
- Community: relevance + stance/intensity/type, with explicit Korean slang/irony
  handling ("가즈아"=bullish, "한강"=bearish, irony resolved to actual sentiment)
- No human labels at any stage

## Index construction (summary)

Daily composite = 0.6 × news (dimension-weighted mean over relevant articles)
+ 0.4 × community bullishness. Official index = rolling 1-year percentile of the
composite, 5-day EMA. Community posting volume z-score (`com_vol_z`) is computed
against a trailing 60-day window. Capitulation signal = `pct_ema < 25 AND
com_vol_z > 2`.

## Caveats

- Community coverage: exhaustive from 2025-01, evenly-spaced 300 posts/day sample
  for 2021–2024
- 2019–2020 rows are a news-only warm-up for the percentile window — do not use
  them as the composite index
- KOSPI/VKOSPI market data are not redistributed (Naver/KRX); see paper scripts

## Citation

```bibtex
@article{korfeargreed2026,
  title  = {Measuring fear and greed with large language models: Evidence from
            news and retail investor communities in the Korean stock market},
  author = {Jun, Tae Joon},
  year   = {2026},
  note   = {Manuscript. Department of Information Medicine, Asan Medical Center,
            University of Ulsan College of Medicine}
}
```

Contact: Tae Joon Jun (taejoon@amc.seoul.kr), Department of Information Medicine,
Asan Medical Center, University of Ulsan College of Medicine, Seoul, Republic of Korea.

## Changelog

**v1.1 (2026-08-12, Revision 1)**
- `daily_index.csv` / `daily_dims.csv` updated: (i) community component dropped on
  days with <10 relevant posts (weight renormalized to news); (ii) community
  volume z-score re-initialized at the 2025-01-01 coverage-regime boundary
  (first 19 days of 2025 have no z); annotation files unchanged.
- Added `prompts/`: exact Korean system prompts used for annotation + English
  translations.

**v1.0 (2026-08-12)** — initial release.

**v1.2 (2026-08-12, Revision 2)**
- Added `audit/reannotation_audit_2021.jsonl.gz`: the 2,000-post re-annotation
  audit sample (balanced 1,000 relevant / 1,000 irrelevant from 2021), with
  post ids, dates, URLs, original and re-annotated labels. Agreement: 94.2%
  (relevance), 88.3% (stance, on the 969 doubly-relevant posts).
