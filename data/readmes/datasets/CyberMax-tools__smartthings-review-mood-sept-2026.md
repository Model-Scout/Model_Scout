---
# LATEST: https://huggingface.co/datasets/CyberMax-tools/smartthings-review-mood-sept-2026/blob/main/latest.json (data date, refresh cadence, fresh API, licence links; also LATEST.md)
# API (fresh data): https://apify.com/cybermax/app-reviews?utm_source=huggingface&utm_medium=free-asset&utm_campaign=file-smartthings-review-mood-sept-2026&utm_content=gripeline
# Licence: cc-by-4.0 (open, unchanged); commercial licence + support: https://cybermaxtools.com/store/dataset-license/?utm_source=huggingface&utm_medium=free-asset&utm_campaign=file-smartthings-review-mood-sept-2026&utm_content=dataset-license
license: cc-by-4.0
pretty_name: 'Gripeline: SmartThings App Review Mood Around the Sept 2026 Fridge Firmware Incident'
language:
- en
- ko
tags:
- app-reviews
- app-store
- google-play
- smart-home
- iot
- firmware
- customer-feedback
- incident-analysis
- tabular
- cybermax
task_categories:
- tabular-classification
size_categories:
- n<1K
configs:
- config_name: default
  data_files:
  - split: train
    path: data/*.parquet
---

# Gripeline: SmartThings app review mood around the Sept 2026 fridge firmware incident

<!-- cybermax-bridge:start -->
> **Get the same review mood for your own app, fresh: $0.10 per 1,000 reviews.** **[Try it on your own list →](https://apify.com/cybermax/app-reviews?utm_source=huggingface&utm_medium=free-asset&utm_campaign=smartthings-review-mood-sept-2026-top&utm_content=gripeline)** · Runs on your own Apify account, pay only per result
> 
> **Need it fresh, filtered or via API?** This free file is a snapshot (app reviews around one September 2026 incident), last updated **2026-09-24**.
> - Using it at work? **[Commercial license + support](https://cybermaxtools.com/store/dataset-license/?utm_source=huggingface&utm_medium=free-asset&utm_campaign=smartthings-review-mood-sept-2026&utm_content=dataset-license)** (from $49/year): invoice, PDF licence certificate, named support, freshness and availability commitments and an SLA; the data stays free and open for everyone.
> - **[Get an email when this dataset updates](https://data.cybermaxtools.com/notify?ds=smartthings-review-mood-sept-2026&s=hf-smartthings-review-mood-sept-2026)**: free, double opt-in, unsubscribe any time.
> - **[CyberMax Store](https://cybermaxtools.com/store/?utm_source=huggingface&utm_medium=dataset&utm_campaign=smartthings-review-mood-sept-2026)**: every CyberMax data product, API plan and weekly brief in one place.
<!-- cybermax-bridge:end -->

<!-- cm:banner -->
![Gripeline: See what users hate about any app](https://cybermax-tools-cybermax.static.hf.space/brand/app-reviews/banner.png)
<!-- /cm:banner -->

On 22 Sep 2026 a refrigerator firmware update pushed through Samsung's SmartThings platform left some smart fridges in Korea without power ([Ars Technica, 23 Sep 2026](https://arstechnica.com/gadgets/2026/09/owners-mourn-spoiled-food-after-firmware-update-bricks-samsung-smart-fridges/); Samsung told Ars the issue was limited to Korea and came from an error during internal testing). Did it show up in the app stores? This dataset has **one row per day, store and country** for the SmartThings app, 8–23 Sep 2026: review count, average rating, share of 1–2 star reviews, and how many reviews mention the fridge, an update/firmware, or going offline/losing connection (keywords matched in Korean and English).

**What the data shows [Verified, from the rows below]:**
- **Korea (Google Play + App Store):** from 8–21 Sep, **0 of 89** reviews mentioned the fridge and about 20% were 1–2 stars. On 22–23 Sep, **3 of 9** reviews mentioned the fridge and **7 of 9** were 1–2 stars.
- **US:** no change (Google Play 26% negative before, 28% after; no fridge mentions on 22–23 Sep). This matches Samsung's statement that the problem was limited to Korea.
- The volume is small: most owners took the problem to Samsung's forum and service centres, not the app stores. A review-mood signal can still flag an incident within a day. That's what a daily Gripeline monitor run is for.

Aggregates only: no review text, titles or reviewer names are included.

<!-- cm:gallery -->
![Gripeline: product image 1](https://cybermax-tools-cybermax.static.hf.space/brand/app-reviews/image-1-output.png)
![Gripeline: product image 2](https://cybermax-tools-cybermax.static.hf.space/brand/app-reviews/image-2-inside.png)
![Gripeline: product image 3](https://cybermax-tools-cybermax.static.hf.space/brand/app-reviews/image-3-savings.png)
<!-- /cm:gallery -->

## Use it

```python
from datasets import load_dataset
df = load_dataset("CyberMax-tools/smartthings-review-mood-sept-2026", split="train").to_pandas()
print(df[df.country == "KR"].sort_values("date")[["date", "store", "reviews", "negative_share", "mentions_fridge"]])
```

## Columns

| column | meaning |
|---|---|
| `date` | review date (UTC) |
| `store`, `country` | `google_play` / `app_store`; `KR` (Korean) or `US` (English) |
| `reviews`, `avg_rating`, `negative_share` | reviews that day, their average stars, share at 1–2 stars |
| `mentions_fridge`, `mentions_fridge_negative` | reviews mentioning fridge/freezer (냉장고, 냉동, fridge, refrigerator, freezer), and how many of those were 1–2 stars |
| `mentions_update` | reviews mentioning an update or firmware (업데이트, 펌웨어, update, firmware) |
| `mentions_offline_or_connection` | reviews mentioning going offline or connection trouble |

## Get fresh data

- **Watch any app's reviews daily, both stores, with a complaint summary agents can read:** [Gripeline on the Apify Store](https://apify.com/cybermax/app-reviews) (monitor mode returns only new reviews).
- **Complaint stats for 30 popular apps:** [app-complaint-stats dataset](https://huggingface.co/datasets/CyberMax-tools/app-complaint-stats) · [free Gripeline Space](https://huggingface.co/spaces/CyberMax-tools/app-complaints).

## How it was made

Collected 24 Sep 2026 with Gripeline's store clients (newest Google Play reviews for `com.samsung.android.oneconnect`, KR/ko and US/en; newest App Store reviews for id 1222822904, KR and US), keeping reviews dated 8–23 Sep. Builder: `build.mjs` in the CyberMax factory. Keyword matching is simple and literal, so treat the mention counts as a rough signal. Not affiliated with Samsung, Apple or Google; SmartThings is a trademark of its owner. By CyberMax.

<!-- cybermax-xlinks:start -->
## More free from CyberMax

- [All free CyberMax demos & datasets](https://huggingface.co/spaces/CyberMax-tools/cybermax)
- [Gripeline: App Store & Google Play Complaint Stats](https://huggingface.co/datasets/CyberMax-tools/app-complaint-stats)
- [Gripeline: What App Users Complain About](https://huggingface.co/spaces/CyberMax-tools/app-complaints)
<!-- cybermax-xlinks:end -->

<!-- cybermax-notebook:start -->
## Quickstart notebook

Load this dataset with pandas and see real outputs in the [quickstart notebook](https://huggingface.co/datasets/CyberMax-tools/smartthings-review-mood-sept-2026/blob/main/notebooks/quickstart.ipynb). Need it refreshed for your own list? [App Store Reviews & Google Play Reviews Scraper — Gripeline](https://apify.com/cybermax/app-reviews).
<!-- cybermax-notebook:end -->
