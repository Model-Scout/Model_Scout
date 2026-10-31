---
license: other
pretty_name: BTC News and Price Reactions (forward and backward)
language:
  - en
  - zh
  - ja
  - ko
size_categories:
  - 100K<n<1M
task_categories:
  - text-classification
  - time-series-forecasting
tags:
  - cryptocurrency
  - event-study
  - weak-supervision
  - multilingual
  - non-commercial
configs:
  - config_name: licensed_news_price_reaction
    default: true
    data_files:
      - split: analysis
        path: data/licensed_news_price_reaction/*.parquet
  - config_name: news_price_reaction
    data_files:
      - split: analysis
        path: data/news_price_reaction/*.parquet
  - config_name: news_index
    data_files:
      - split: observations
        path: data/news_index/*.parquet
  - config_name: weak_annotations
    data_files:
      - split: annotations
        path: data/weak_annotations/*.parquet
  - config_name: trading_decisions
    data_files:
      - split: observations
        path: data/trading_decisions/*.parquet
  - config_name: market_1m
    data_files:
      - split: market
        path: data/market_1m/*.parquet
  - config_name: funding_rates
    data_files:
      - split: market
        path: data/funding_rates/*.parquet
  - config_name: outcomes
    data_files:
      - split: outcomes
        path: data/outcomes/*.parquet
  - config_name: pre_event_outcomes
    data_files:
      - split: outcomes
        path: data/pre_event_outcomes/*.parquet
  - config_name: market_gap_summary
    data_files:
      - split: quality
        path: data/market_gap_summary/*.parquet
  - config_name: source_registry
    data_files:
      - split: metadata
        path: data/source_registry/*.parquet
  - config_name: source_coverage
    data_files:
      - split: metadata
        path: data/source_coverage/*.parquet
  - config_name: language_coverage
    data_files:
      - split: metadata
        path: data/language_coverage/*.parquet
  - config_name: source_health
    data_files:
      - split: quality
        path: data/source_health/*.parquet
  - config_name: clock_drift_windows
    data_files:
      - split: quality
        path: data/clock_drift_windows/*.parquet
  - config_name: build_provenance
    data_files:
      - split: provenance
        path: data/build_provenance/*.parquet
  - config_name: rights_matrix
    data_files:
      - split: provenance
        path: data/rights_matrix/*.parquet
---


# BTC News and Price Reactions

**120,981 multilingual news events joined to weak semantic
annotations and BTC returns before and after each observation, from 1 minute
to 24 hours.** The release is designed for event studies, classifier
bootstrapping, temporal evaluation, and research on how observed news aligns
with market movement.

> **Start here:** `licensed_news_price_reaction` is the analysis-ready view with
> attributed reusable titles/RSS summaries, weak labels, entry prices, and all
> six forward and backward BTC windows in one row per event.

## Dataset at a glance

| | Coverage |
| --- | --- |
| News observations | **120,981** from 18 publisher feeds |
| Attributed reusable text rows | **12,433** |
| Languages | Korean, Chinese, English, Japanese, and undetermined |
| Observation window | 13 June–19 September 2026 |
| Forward and backward horizons | 1, 5, 15, 60, 240, and 1,440 minutes |
| Market context | Binance BTCUSDT/ETHUSDT one-minute OHLCV and BTCUSDT funding |
| Release | v0.6.4 · immutable snapshot · mixed-source non-commercial terms |

## Quick start

```python
from datasets import load_dataset

ds = load_dataset(
    "dymyt-ry/btc-news-forward-price-reactions",
    "licensed_news_price_reaction",
    split="analysis",
)

sample = ds.select_columns([
    "first_seen_at",
    "title",
    "weak_event_type",
    "backward_return_bps_60m",
    "forward_return_bps_60m",
    "outcome_status_60m",
])
print(sample[0])
```

For maximum event coverage, switch the configuration to
`news_price_reaction`. Publisher text is null by design outside the separately
reviewed reusable subset; URLs, timing, weak annotations, and price windows
remain available.

## Choose the right configuration

| Need | Configuration |
| --- | --- |
| Reusable news text + annotations + wide BTC windows | `licensed_news_price_reaction` |
| All events + annotations + wide BTC windows | `news_price_reaction` |
| Normalized event metadata | `news_index` |
| Full weak-label scores and lineage | `weak_annotations` |
| One-minute BTC/ETH bars | `market_1m` |
| Long-format event × horizon forward targets | `outcomes` |
| Long-format event × horizon backward windows | `pre_event_outcomes` |
| Rights decisions and evidence | `rights_matrix` |

The default configuration is `licensed_news_price_reaction`; each configuration
contains one Parquet file and one semantically named split.

## Backward windows (new in v0.6.4)

`backward_return_bps_<h>m` is the BTC log return over the `h` minutes that end
at `pre_event_anchor_at`, the open of the UTC minute in which the collector
made its decision. That price is known at decision time, so backward columns
are **leak-free features**. Forward columns start one minute later at
`entry_at` and remain **targets**. The long-format table `pre_event_outcomes`
mirrors `outcomes` row for row (719,046 event × horizon rows).

Compare `|forward|` with `|backward|` only after normalizing by the same ratio
at placebo times (for example the same anchors shifted by whole weeks), because
intraday volatility seasonality alone moves the raw ratio away from 1.
`backward_status_<h>m` is `observed`, `before_market_coverage` (the earliest
events, 1,440-minute window only) or `after_market_coverage` (the final
snapshot hours, whose forward status is `pending`). Never treat a
non-observed window as a zero return. Backward windows of later events overlap
forward windows of earlier ones: for machine learning, split chronologically
and purge/embargo at least 1,441 minutes around each boundary.

## Research findings

Two analyses were run on this release. Each fixed one primary hypothesis in
advance; all other results are exploratory. Code and full outputs:
[timing notebook](https://www.kaggle.com/code/dymy1ry/does-crypto-news-lead-btc-forward-backward-test) and
[volatility notebook](https://www.kaggle.com/code/dymy1ry/does-crypto-news-improve-btc-volatility-forecasts).

**1. Does news lead BTC moves?** The test compares BTC's absolute move after
each observation with the equally long move before it, relative to placebo
times with the same weekday and time of day. For Korean, Chinese and Japanese
(CJK) events at 60 minutes, the excess ratio is 0.98 (95% CI 0.963–0.999). The
hypothesis that news leads price is **not supported**. Ratios below 1 at 1–15
minutes come from headlines that report price moves (market commentary ≈0.91)
and from RSS poll batches. Without both, the ratio is 0.99–1.00. Bursts of
unusually dense CJK news show no effect.

**2. Does news flow improve volatility forecasts?** The test adds CJK
news-flow features to a price-only model of next-hour realized volatility. The
pre-registered version passed nominally: 1.2% lower out-of-sample error,
p = 0.019. The gain turned out to be a **weekend proxy**, because news flow and
volatility both drop at weekends. With day-of-week controls or daily rolling
refits, the change is between −0.3% and +0.1% and not significant. Its
features were chosen using the timing analysis of the same period, so its
hypothesis is pre-specified for that notebook rather than independent of the
data.

**Conclusion.** In this sample (13 June–18 September 2026; BTC between about
58k and 82k USD, including a breakout from about 63k to 78k between 18 and
21 August), CJK news flow neither leads
BTC moves nor improves volatility forecasts beyond price history and the
weekly calendar. These are negative research results about one period, not
trading advice.

## What “weak annotation” means

Event type, BTC relevance, and experimental direction were generated from
title/RSS text by a pinned multilingual embedding model plus deterministic
rules. They are useful for filtering, bootstrapping, and review queues, but are
**not human gold labels**. Cosine scores and margins are not calibrated
probabilities. See [ANNOTATION.md](ANNOTATION.md) for model and artifact hashes.

## Modeling rules that matter

- Forward and backward returns describe what BTC did around an observation;
  they do **not** establish that a news item caused a move.
- Keep every `target_*`, `forward_return_*`, and `outcome_status_*` field on the
  target side to prevent look-ahead leakage. Backward columns are features.
- Split chronologically, embargo at least 1,441 minutes, and group
  repeated-title events before evaluation.
- Treat `pending` and non-observed backward windows as unavailable, never as
  zero returns.
- The observed source/language mix is publisher-concentrated, not a balanced
  population sample or a validated CJK classifier benchmark.

## Tables and exact files

| Configuration | Rows | Hub path |
| --- | ---: | --- |
| `licensed_news_price_reaction` | 12,433 | `data/licensed_news_price_reaction/unknown.parquet` |
| `news_price_reaction` | 120,981 | `data/news_price_reaction/unknown.parquet` |
| `news_index` | 120,981 | `data/news_index/unknown.parquet` |
| `weak_annotations` | 120,981 | `data/weak_annotations/unknown.parquet` |
| `trading_decisions` | 119,841 | `data/trading_decisions/unknown.parquet` |
| `market_1m` | 282,240 | `data/market_1m/unknown.parquet` |
| `funding_rates` | 240 | `data/funding_rates/unknown.parquet` |
| `outcomes` | 719,046 | `data/outcomes/unknown.parquet` |
| `pre_event_outcomes` | 719,046 | `data/pre_event_outcomes/unknown.parquet` |
| `market_gap_summary` | 2 | `data/market_gap_summary/unknown.parquet` |
| `source_registry` | 18 | `data/source_registry/unknown.parquet` |
| `source_coverage` | 72 | `data/source_coverage/unknown.parquet` |
| `language_coverage` | 5 | `data/language_coverage/unknown.parquet` |
| `source_health` | 1,782 | `data/source_health/unknown.parquet` |
| `clock_drift_windows` | 29 | `data/clock_drift_windows/unknown.parquet` |
| `build_provenance` | 1 | `data/build_provenance/unknown.parquet` |
| `rights_matrix` | 21 | `data/rights_matrix/unknown.parquet` |

Historical Coin Metrics Community tables from v0.6.2 are intentionally omitted
from this compact news-to-price-reaction edition. Coin Metrics is not Coinbase.

## Rights and reproducibility

This is a mixed-source, **non-commercial research release**. Reusable text is
limited to attributed PANews, U.S. SEC, and Federal Reserve Board rows covered
by the documented source-specific terms; other publishers remain metadata-only.
The Hub `other` license badge is not a blanket grant.

Read [RIGHTS.md](RIGHTS.md) and the machine-readable
[rights matrix](data/rights_matrix/unknown.parquet) before redistribution or
model release. [SOURCES.md](SOURCES.md),
[build provenance](data/build_provenance/unknown.parquet), `manifest.json`, and
`SHA256SUMS` provide exact source and artifact lineage.

## Documentation

- [Data dictionary](DATA_DICTIONARY.md)
- [Weak annotation provenance](ANNOTATION.md)
- [Rights and license review](RIGHTS.md)
- [Sources](SOURCES.md)
- [Publication decision](PUBLICATION.md)
- Machine-readable schemas: `schema.json`, `manifest.json`, and `quality.json`
- Source code, notebooks and release history: [GitHub](https://github.com/Dymyt-ry/btc-news-forward-price-reactions)

## Citation

```bibtex
@dataset{golobokov_2026_btc_news_reactions,
  author       = {Timofej Golobokov},
  title        = {BTC News and Price Reactions},
  year         = {2026},
  version      = {0.6.4},
  publisher    = {Hugging Face},
  url          = {https://huggingface.co/datasets/dymyt-ry/btc-news-forward-price-reactions}
}
```
