# SmartThings App Reviews: Sept 2026 Fridge Incident

Daily app review mood, ratings and fridge mentions, Korea vs US, 8-23 Sep

> **Get the same review mood for your own app, fresh: $0.10 per 1,000 reviews.** **[Try it on your own list →](https://apify.com/cybermax/app-reviews?utm_source=kaggle&utm_medium=free-asset&utm_campaign=smartthings-review-mood-sept-2026-top&utm_content=gripeline)** · Runs on your own Apify account, pay only per result
> 
> **Need it fresh, filtered or via API?** This free file is a snapshot (app reviews around one September 2026 incident), last updated **2026-09-24**.
> - Using it at work? **[CyberMax Dataset Commercial License: Small (up to 10 people)](https://buy.stripe.com/5kQ9AT4A40oVfF7dlNbV61L?utm_source=kaggle&utm_medium=free-asset&utm_campaign=smartthings-review-mood-sept-2026&utm_content=st-dataset-license-small&client_reference_id=data_hf-smartthings-review-mood-sept-2026)** ($49/year, direct checkout; bigger teams: [Business and Enterprise](https://cybermaxtools.com/store/dataset-license/)): Commercial licence and support for one company or organisation with up to 10 people, for one year; first support reply within 2 business days.
> - **[Get an email when this dataset updates](https://data.cybermaxtools.com/notify?ds=smartthings-review-mood-sept-2026&s=kaggle-smartthings-review-mood-sept-2026)**: free, double opt-in, unsubscribe any time.
> - **[CyberMax Store](https://cybermaxtools.com/store/?utm_source=kaggle&utm_medium=dataset&utm_campaign=smartthings-review-mood-sept-2026)**: every CyberMax data product, API plan and weekly brief in one place.

## Overview

On 22 Sep 2026 a refrigerator firmware update pushed through Samsung's SmartThings platform left some smart fridges in Korea without power. This dataset tracks the SmartThings app's Google Play and App Store reviews day by day from 8 to 23 Sep 2026, in Korea and the US: review counts, average rating, share of 1-2 star reviews and how many reviews mention the fridge, an update or firmware, or connection trouble. It is a compact, ready-to-plot case study for incident analysis, customer-feedback monitoring and app review sentiment.

**Published by CyberMax.** Canonical copy: [CyberMax-tools/smartthings-review-mood-sept-2026 on Hugging Face](https://huggingface.co/datasets/CyberMax-tools/smartthings-review-mood-sept-2026). This Kaggle copy gets a new version automatically whenever the source data is refreshed.

## What's inside

- 63 rows: one per day, store and country for the SmartThings app, 8-23 Sep 2026
- Google Play and Apple App Store, Korea (Korean reviews) and US (English reviews)
- Review count, average star rating and share of 1-2 star reviews per day
- Keyword mention counts for fridge/freezer, update/firmware and offline/connection, matched in Korean and English
- Aggregates only: no review text, titles or reviewer names
- Same rows in JSONL and Parquet

| File | Rows | Size | What it holds |
|---|---|---|---|
| `daily-2026-09-24.jsonl` |  | 0.0 MB | JSON Lines: one row per review date, store and country for the SmartThings app (collected 2026-09-24). Holds the same rows as the Parquet copy. |
| `daily-2026-09-24.parquet` | 63 | 0.0 MB | Parquet copy with typed columns: 63 rows, one per review date, store and country. Same rows as the JSONL copy. |

## Column dictionary

**`daily-2026-09-24.jsonl` / `daily-2026-09-24.parquet`**

| Column | Type | Description |
|---|---|---|
| `date` | str | Review date (UTC, YYYY-MM-DD) |
| `store` | str | App store: google_play or app_store |
| `country` | str | Store country: KR (Korean-language reviews) or US (English-language reviews) |
| `app` | str | App name (always SmartThings) |
| `reviews` | int | Number of reviews posted that day in that store and country |
| `avg_rating` | float | Average star rating of those reviews (1-5, two decimals) |
| `negative_share` | float | Share of those reviews rated 1 or 2 stars (0-1, three decimals) |
| `mentions_fridge` | int | Reviews mentioning a fridge or freezer (냉장고, 냉동, fridge, refrigerator, freezer) in title or text |
| `mentions_fridge_negative` | int | Of the fridge-mentioning reviews, how many were rated 1 or 2 stars |
| `mentions_update` | int | Reviews mentioning an update or firmware (업데이트, 펌웨어, update, firmware) |
| `mentions_offline_or_connection` | int | Reviews mentioning going offline or connection trouble (오프라인, 연결, offline, disconnect, connect) |

## Source and provenance

- [Google Play reviews for the SmartThings app (com.samsung.android.oneconnect)](https://play.google.com/store/apps/details?id=com.samsung.android.oneconnect)
- [Apple App Store reviews for the SmartThings app (id 1222822904)](https://apps.apple.com/us/app/id1222822904)

Collected by CyberMax on 24 Sep 2026 with its Gripeline app-review clients: the newest public reviews from both stores were fetched, reviews dated 8-23 Sep were kept and aggregated per day. Only daily counts and averages are published, never review text or names. Released under CC BY 4.0; not affiliated with Samsung, Apple or Google.

## Methodology

1. Fetch the newest Google Play reviews for com.samsung.android.oneconnect (KR in Korean, US in English) and the newest App Store reviews for the same app (KR and US)
2. Keep reviews dated from 8 Sep 2026 onward
3. Group by review date, store and country; count reviews, average the star ratings and compute the share rated 1-2 stars
4. Match each review's title and text against simple Korean and English keyword lists (fridge/freezer, update/firmware, offline/connection) and count matches
5. Write one row per day, store and country in JSONL and Parquet

## Update frequency

**Never.** A one-off snapshot of reviews around the September 2026 incident, collected on 24 Sep 2026; it is not refreshed.

## Licence

`cc-by-4.0`. Please credit the original sources listed above.

## Example uses

- Plot negative-review share before and after 22 Sep to see how fast an incident shows up in app stores
- Compare Korea and US review mood to test whether the problem was regional
- Prototype an incident-detection alert on daily app review signals
- Teach event-study and before/after analysis with a small, clean time series
- Contrast Google Play and App Store review volume and ratings for the same app

## Good to know

- Small volumes: only a handful of reviews per day, so one review moves the percentages a lot
- Keyword matching is simple and literal (e.g. 'connect' also matches unrelated uses), so mention counts are a rough signal
- Only the newest reviews each store returned were collected, and days with no reviews have no row

## Load it in a Kaggle notebook

```python
import pandas as pd
df = pd.read_json('/kaggle/input/smartthings-review-mood-sept-2026/daily-2026-09-24.jsonl', lines=True)
df.head()
```

## Need it fresh or via API?

This file is a free snapshot. For always-fresh data, filters, alerts or an API, use the CyberMax tools linked at the top of this page, or browse every data product in the [CyberMax Store](https://cybermaxtools.com/store/?utm_source=kaggle&utm_medium=dataset&utm_campaign=smartthings-review-mood-sept-2026).

More free datasets and tools from CyberMax: https://cybermax-tools-cybermax.static.hf.space/

출처: Kaggle (cybermaxtools/smartthings-review-mood-sept-2026)
태그: business, internet, mobile and wireless, exploratory data analysis, time series analysis, tabular
라이선스: Attribution 4.0 International (CC BY 4.0)
수정일: 2026-10-09T04:12:55.967Z
