# BTC News and Price Reactions

120K multilingual news events, weak labels, BTC moves before and after

## What did BTC do before and after a news event was observed?

This research dataset connects **120,981 timestamped events from 18 publisher
feeds** with weak semantic labels and BTC price moves over six windows
**before and after** each observation. It is designed for reproducible event
studies, classifier bootstrapping, multilingual coverage analysis, and
market-reaction research.

**Coverage:** 13 June–19 September 2026 · **Languages:** Korean, Chinese,
English, Japanese, and undetermined · **Windows:** 1, 5, 15, 60, 240, and
1,440 minutes

> **Start here:**
> `START_HERE__licensed_news_price_reaction.parquet` contains the cleanest
> analysis-ready view: attributed reusable titles and RSS summaries, weak
> labels, entry prices, and all six forward and backward BTC windows in one
> row per event.

## Choose the right table

| If you need… | Open this file | Rows |
| --- | --- | ---: |
| Reusable news text + labels + BTC windows | `START_HERE__licensed_news_price_reaction.parquet` | 12,433 |
| Maximum event coverage; restricted text omitted | `START_HERE__all_news_price_reaction.parquet` | 120,981 |
| One-minute BTCUSDT and ETHUSDT OHLCV bars | `data__market_1m__unknown.parquet` | 282,240 |
| Long-format event × horizon forward targets | `data__outcomes__unknown.parquet` | 719,046 |
| Long-format event × horizon backward windows | `data__pre_event_outcomes__unknown.parquet` | 719,046 |
| Source rights and publication scope | `data__rights_matrix__unknown.parquet` | 21 |

The remaining tables expose normalized annotations, decision-time lineage,
funding rates, language/source coverage, collection health, clock-drift windows,
and build provenance.

## Quick start

```python
import pandas as pd

path = "/kaggle/input/btc-multilingual-news-market-events/START_HERE__licensed_news_price_reaction.parquet"
df = pd.read_parquet(path)

features = df[["title", "summary", "weak_event_type", "backward_return_bps_60m"]]
targets = df[["forward_return_bps_60m", "outcome_status_60m"]]
```

Runnable notebooks: the
[quickstart](https://www.kaggle.com/code/dymy1ry/quickstart-btc-news-and-price-reactions),
the [timing test](https://www.kaggle.com/code/dymy1ry/does-crypto-news-lead-btc-forward-backward-test), and the
[volatility forecast test](https://www.kaggle.com/code/dymy1ry/does-crypto-news-improve-btc-volatility-forecasts).

## Backward windows (new in v0.6.4)

`backward_return_bps_

출처: Kaggle (dymy1ry/btc-multilingual-news-market-events)
태그: finance, nlp, time series analysis, text classification, multilingual
라이선스: Other (specified in description)
수정일: 2026-09-22T20:25:39.307Z
