# Korean Won Tether (USDT) Premium - Daily

Daily USDT/KRW premium vs the USD/KRW reference rate on Upbit, 2025-present

## What this is

How far Tether (USDT) trades above or below the official USD/KRW rate on Korean exchanges — the clearest single read on what it costs to move value into or out of the Korean won. One row per day since **2025-01-01**. This dataset is linked to the live source and refreshed from it.

## Columns

| Column | Meaning |
|---|---|
| `date` | Korean calendar date (KST), `YYYY-MM-DD` |
| `usdt_krw` | Upbit KRW-USDT daily close, in won |
| `usd_krw` | USD/KRW reference rate for the same day (European Central Bank reference rate via Frankfurter) |
| `premium_pct` | `(usdt_krw / usd_krw − 1) × 100` |
| `volume_krw` | Upbit KRW-USDT daily turnover, in won |
| `fx_carried` | `true` when no reference rate was published that day (weekend, holiday) and the previous business day's rate was used |

The most recent row is provisional until the Korean trading day closes; the last ~30 days are re-synced at the source, so late revisions are picked up.

## Method

Tether is itself a dollar token, so — unlike the "kimchi premium" on other coins — no global price is involved: the won price is divided directly by the dollar reference rate. Weekend and holiday days carry the last published rate and are flagged, so the mean can be recomputed with those days excluded. Full method and a daily table: https://tegongkorea.com/en/tether-premium

## Ideas

- How does the premium react to capital-control news, exchange outages or regulatory dates (for example the 2026 travel-rule changes)?
- Weekend vs weekday premium — does the carried FX rate bias the mean?
- Turnover vs premium: does high volume compress the gap?

## Citation

Park, J. / Tegong (2026). *Daily Tether (USDT) premium on the South Korean won market.* Zenodo. https://doi.org/10.5281/zenodo.22270442

## Source and licence

Published by Tegong (https://tegongkorea.com/en) under CC BY 4.0. Source file: https://tegongkorea.com/data/usdt-krw-premium.csv · Live API and embeddable chart: https://tegongkorea.com/en/data. Inputs: Upbit public market data; ECB euro foreign exchange reference rates via Frankfurter.

출처: Kaggle (presstegong/korean-won-tether-usdt-premium-daily)
태그: finance, economics, time series analysis, currencies and foreign exchange, korea
라이선스: Attribution 4.0 International (CC BY 4.0)
수정일: 2026-10-31T07:32:33.247Z
