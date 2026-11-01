---
language:
  - ko
pretty_name: "KRX Investment Warning Prediction Dataset (OHLCV + Technical Indicators + Korean News)"
tags:
  - finance
  - krx
  - korea
  - time-series
  - ohlcv
  - technical-indicators
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

# KRX Investment Warning Prediction Dataset (OHLCV + Technical Indicators + Korean News)

## Dataset Summary

This dataset is a test dataset for predicting **Investment Warning (투자주의종목)** designations in the Korean stock market (KRX).
It contains **raw daily OHLCV** price data, **13 technical indicators**, and **Korean news text** (title + body), designed for **multimodal anomaly detection / binary classification**.

**Important:** No normalization/scaling is applied. All values are raw.

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
- **`time_series`**: Price time-series information (OHLCV + Technical Indicators)
- **`texts`**: Korean news text mapped to the corresponding stock (title + body)

### Example (Conceptual)

- `labels`: `0` or `1`
- `time_series`: `[[open, high, low, close, volume, rsi, macd, macd_signal, macd_hist, bb_upper, bb_middle, bb_lower, bb_width, sma_5, sma_20, ema_9, atr, obv], ...]`
- `texts`: `["article1 ...", "article2 ..."]`

## Feature Details

### Price & Indicators — `time_series`

Each sample has shape `[10, 18]` with the following 18 features:

| Index | Feature | Description |
|-------|---------|-------------|
| 0 | `open` | Opening price (KRW) |
| 1 | `high` | High price (KRW) |
| 2 | `low` | Low price (KRW) |
| 3 | `close` | Closing price (KRW) |
| 4 | `volume` | Trading volume (shares) |
| 5 | `rsi` | Relative Strength Index (14-period) |
| 6 | `macd` | MACD line (12, 26) |
| 7 | `macd_signal` | MACD signal line (9-period) |
| 8 | `macd_hist` | MACD histogram |
| 9 | `bb_upper` | Bollinger Band upper (20, 2std) |
| 10 | `bb_middle` | Bollinger Band middle (20-SMA) |
| 11 | `bb_lower` | Bollinger Band lower (20, 2std) |
| 12 | `bb_width` | Bollinger Band width (normalized) |
| 13 | `sma_5` | Simple Moving Average (5-period) |
| 14 | `sma_20` | Simple Moving Average (20-period) |
| 15 | `ema_9` | Exponential Moving Average (9-period) |
| 16 | `atr` | Average True Range (14-period) |
| 17 | `obv` | On-Balance Volume |

- **No normalization/scaling** is applied. All values are raw.
- **Currency unit:** KRW
- **Volume:** number of shares (not value)
- Technical indicators are computed with a lookback of 35 days to ensure stable values.

### News — `texts`

- News is mapped to tickers via an **exact ticker-code mapping**.
- **Deduplication** has been applied.
- Each news item includes **title + body** (concatenated as a single string).

## Dataset Statistics

- **Total Samples**: 10,605
- **Label Distribution**: {0: 10570, 1: 35}
- **Sequence Length**: 10
- **Features per timestep**: 18
- **Undersampling**: Majority class reduced to 10%

## Recommended Metrics

Because investment warning events are likely to be rare (class imbalance), the following metrics are recommended:

- ROC-AUC, PR-AUC
- F1 (positive class), precision/recall
- Precision/recall at Top-k (useful for practical detection scenarios)
- (Optional) probability calibration

## Usage

```python
from datasets import load_dataset

dataset = load_dataset("k-datasoft/Multimodal-test-dataset-technicalindicators")
```

## License

MIT License
