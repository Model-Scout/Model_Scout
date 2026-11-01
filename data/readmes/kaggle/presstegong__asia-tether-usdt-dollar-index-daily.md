# Asia Tether (USDT) Dollar Index - Daily

Daily USD value of one USDT in Korea, India, Indonesia, Thailand, Philippines

## What this is

Tether (USDT) is designed to be worth exactly one US dollar. On local exchanges across Asia it trades for local currency, and the price there shows how much local buyers pay for digital dollars and how easily money crosses the border. This dataset records, for each market and each day since 1 January 2025, what one USDT actually cost in US dollars.

A value of 1.000 means exactly one dollar. 1.057 means 5.7% above the peg; 0.968 means 3.2% below. This file is linked to the live source and refreshed from it daily.

## Markets

| Market | Currency | Exchange(s) | Daily candle |
|---|---|---|---|
| South Korea | KRW | Upbit | KST (UTC+9) |
| India | INR | WazirX, CoinDCX (median close) | UTC |
| Indonesia | IDR | Indodax | UTC |
| Thailand | THB | Bitkub | ICT (UTC+7) |
| Philippines | PHP | Coins.ph | UTC |

## Method

`usdt_usd_value = daily close of USDT in local currency / ECB reference rate of that currency per US dollar (same day)`

Reference rates are European Central Bank euro reference rates converted to a US-dollar base via the Frankfurter API. On weekends and holidays the previous business day's rate is used and the row is flagged `fx_carried = true`. The most recent day is provisional; days older than seven days are frozen at the source and not rewritten.

## Columns

| Column | Meaning |
|---|---|
| date | Date of the exchange's daily candle (YYYY-MM-DD) |
| market | KR, IN, ID, TH, PH |
| country | Country name |
| currency | ISO 4217 code |
| usdt_usd_value | USD value of one USDT |
| premium_pct | (usdt_usd_value - 1) x 100 |
| usdt_local_price | USDT close in local currency (median across exchanges where more than one) |
| usd_local_reference_rate | Local currency per USD, ECB reference rate |
| fx_carried | true if the reference rate was carried from the previous business day |
| volume_usdt | Traded volume in USDT, summed across exchanges |
| exchanges | Exchanges used |
| exchange_closes | Close per exchange, local currency |
| provisional | true for the latest, still revisable day |

## Ideas

- Which markets pay the most for digital dollars, and when does the gap between India and Korea open or close?
- How do the premiums react to capital-control news, exchange outages or tax and regulatory dates?
- Weekend versus weekday values: does the carried FX rate bias the mean?
- Does higher turnover compress the gap to $1?

## Limitations

Exchange data can contain errors and thin markets can print outliers; check `volume_usdt` and `exchange_closes` before relying on a single day. Daily candles close at different times in different markets, so same-date values are not simultaneous. The index measures a market price, not the issuer's redemption value.

## Citation

Park, J. (2026). *Asia Tether (USDT) Dollar Index* (Version 1.0.0) [Data set]. Tegong. Zenodo. https://doi.org/10.5281/zenodo.23727401

The Zenodo deposit is a fixed snapshot (1 January 2025 to 27 October 2026). This Kaggle file follows the live series.

## Source and licence

Published by Tegong under CC BY 4.0. Live page, chart and method: https://tegongkorea.com/en/asia-tether-dollar-index · Source file: https://tegongkorea.com/data/asia-tether-dollar-index.csv · JSON: https://tegongkorea.com/data/asia-tether-dollar-index.json

Compiled independently. Not affiliated with, endorsed by or sponsored by Tether Operations Limited. "Tether" and "USDT" are trademarks of their owner. Not investment advice.

출처: Kaggle (presstegong/asia-tether-usdt-dollar-index-daily)
태그: asia, finance, economics, time series analysis, currencies and foreign exchange
라이선스: Attribution 4.0 International (CC BY 4.0)
수정일: 2026-10-30T16:31:08.850Z
