---
language:
  - ko
pretty_name: "KRX Investment Warning Prediction Dataset (OHLCV + Korean News)"
tags:
  - finance
  - krx
  - korea
  - time-series
  - ohlcv
  - news
  - multimodal
  - anomaly-detection
  - binary-classification
task_categories:
  - text-classification
  - time-series-forecasting
task_ids:
  - binary-classification
license: mit
---

# KRX Investment Warning Prediction Dataset (OHLCV + Korean News)

## Dataset Summary

This dataset is a test dataset for predicting **Investment Warning (투자주의종목)** designations in the Korean stock market (KRX).  
It contains **raw daily OHLCV** price data and **Korean news text** (title + body), designed for **multimodal anomaly detection / binary classification**.

**Important:** No technical indicators are included, and no normalization/scaling is applied.

- **Date range:** 2025-07-01 ~ 2025-09-30
- **Prediction horizon:** whether a stock will be designated as an investment warning **within the next 1 trading day**

## Task

Binary classification:

- **Label 0:** Normal trading (no investment warning designation within the next 1 trading day)
- **Label 1:** Investment warning designation (within the next 1 trading day)

### Label Alignment

For each `(ticker, date=t)`, set `label=1` if the stock is designated as an investment warning on `t+1` (the next trading day).

## Data Sources

| Source | Description |
|------|-------------|
| **Stock Prices** | Daily OHLCV data for KRX listed stocks |
| **Investment Warning** | KRX investment warning designation history (labels) |
| **News** | Korean news articles per stock (title + body) |

## Dataset Format

This dataset is structured to be used directly with Hugging Face `datasets`, and consists of **three columns**:

- **`labels`**: Binary label (`0` or `1`)
- **`time_series`**: Price time-series information (OHLCV)
- **`texts`**: Korean news text mapped to the corresponding stock (title + body)

> The exact internal structure of `time_series` and `texts` (e.g., list/dict formats, sequence length, date ordering) follows the dataset schema.  
> In general, `time_series` is provided as a fixed-length historical window, and `texts` contains news from the same date (or window period), either concatenated or stored as a list.

### Example (Conceptual)

- `labels`: `0` or `1`
- `time_series`: `[[open, high, low, close, volume], ...]`
- `texts`: `["article1 ...", "article2 ..."]`

## Feature Details

### Price (OHLCV) — `time_series`

- OHLCV is provided as **raw daily bars**.
- **No technical indicators** (e.g., RSI, MACD) are included.
- **No normalization/scaling** is applied.
- **Currency unit:** KRW
- **Volume:** number of shares (not value)

### News — `texts`

- News is mapped to tickers via an **exact ticker-code mapping**.
- **Deduplication** has been applied.
- Each news item includes **title + body** (stored as a single string or list depending on schema).

## Recommended Metrics

Because investment warning events are likely to be rare (class imbalance), the following metrics are recommended:

- ROC-AUC, PR-AUC
- F1 (positive class), precision/recall
- Precision/recall at Top-k (useful for practical detection scenarios)
- (Optional) probability calibration
