# Korean Equity Daily Prices + DART Filing Impact

2026-09-18 snapshot: KOSPI/KOSDAQ/KONEX closes, DART filings with receipt times

Daily settled closes for 2,787 Korean listed companies (KOSPI, KOSDAQ and KONEX) over the 321 trading days to 2026-09-17, plus a table of what those stocks did after each type of regulatory filing.

**This snapshot is fixed; the live files are not.** The four CSVs here are a dated extract of the 2026-09-18 publish (prices through 2026-09-17). The per-stock history files they were built from are not cut at a fixed length — each trading day adds a row and nothing is dropped, so the live span keeps growing. In this extract Samsung Electronics (005930) has 321 rows, 2025-05-28 to 2026-09-17.

To read the live version instead of this snapshot:

- https://aikstockdata.com/data/public/s/005930_history.json — one stock, every row it has (count, period, max_days (null) and retention say how much)
- https://aikstockdata.com/data/public/index.json — what exists, and as of when

Korean equity data is oddly hard to get. The official sources are free but gated: the Financial Services Commission open-data portal wants an API key and returns raw payloads with Korean field names, and DART (the disclosure system) is a separate registration. Commercial APIs either paywall Korea or cover only large caps. This is the same data, already joined.

## Files

| file | rows | what |
|---|---|---|
| daily_prices.csv | 880,740 | one row per stock per trading day, 2025-05-28 to 2026-09-17 |
| stocks.csv | 2,787 | master list as of the 2026-09-17 close (KOSPI 915, KOSDAQ 1,766, KONEX 106) |
| filing_impact_summary.csv | 29 | median market-adjusted return after each filing type |
| filing_price_impact.csv | 2,803 | the individual filings behind that table, one row each |

Both filing files carry a `receipt_time` (HH:MM) and a session column. No public Korean source publishes the minute a filing arrived - see below for why that decides whether the number in the next column means anything.

## Read the asterisk before anything else

Across all four horizons the summary table has 56 cells carrying a number, and 41 of them have a 95% interval that spans zero. Fifteen clear it, and eight of those fifteen sit at +20 trading days, where the window is long enough for plenty of other things to happen. Publishing the intervals was the point; most of these do not survive them.

These numbers move. In the 2026-08-04 extract, dividend decisions at +5 trading days read +2.21% on 32 distinct price paths. Here the same cell reads -1.12% on 112, with an interval spanning zero in both. More data made the earlier result disappear, which is what a small sample looks like from the inside.

## The identification problem, stated plainly

The public DART API gives a receipt date, not a time. Neither does the individual filing viewer, nor the search screen. We scrape the minute from the one page that still carries it and ship it as `receipt_time`, with session derived from the Korean regular session (09:00-15:30):

| session | filings | what the baseline-day return contains |
|---|---|---|
| pre_open | 63 | the whole day comes after the filing - the only identified case |
| intraday | 1,244 | part of the day precedes the filing |
| after_close | 1,477 | the entire day precedes the filing - not a reaction at all |
| unknown | 19 | no minute recovered |

So the "baseline day" column is 2.2% identified. It is a diagnostic column showing the window that disappears into the baseline, not an estimate of a reaction. filing_impact_summary.csv carries the same breakdown per filing type (filings_pre_open, h0_identified_pct, ...) so you can see which rows are worth reading at all.

Splitting the baseline-day figure by session is the fastest way to see the problem:

    ev.groupby("receipt_session").h0_excess_pct.median()
    # pre_open    +0.02 (n=63)
    # intraday    +0.09 (n=1,243)
    # after_close -0.45 (n=1,474)

## Aggregation

Baseline is the first trading-day close on or after the receipt date. Returns are measured at +1, +5 and +20 trading days, minus the stock's own index (KOSPI or KOSDAQ) over the same window. Aggregation is keyed on issuer x baseline date x filing type - one company filing three documents in a day shares one price path, so it counts once. Both counts ship: `n` is distinct price paths, `n_filings` is receipt numbers. Under 20 observations, no number is published. The +20-day column is now published for the 12 filing types with enough distinct price paths; collection started 2026-07-20.

Four filing types are withheld permanently, not for sample size: paid-in capital increase, bonus issue, paid-in and bonus issue, reverse stock split. An ex-rights date or a share consolidation resets the quoted price mechanically and these closes are not adjusted for corporate actions, so a window containing that date measures the break rather than any market reaction.

## Zero-padded tickers - this WILL bite you

A Korean ticker is six digits including leading zeros. `000020` is Dongwha Pharm; `20` is nothing at all. Kaggle's preview and most CSV readers will silently turn it into an integer.

    import pandas as pd
    px = pd.read_csv("daily_prices.csv", dtype={"code": str, "date": str})

Same for `rcept_no`, `receipt_date`, `receipt_time`, `base_date` and every `h*_date` column in the filing files (`receipt_time` is a "HH:MM" string - comparing it as text sorts correctly). If you skip this, joins to any other Korean dataset - including this project's own per-stock JSON at /data/public/s/000020.json - will fail silently.

## Reproduce the aggregates, or disagree with them

filing_price_impact.csv exists so you can recompute the summary instead of trusting it. Dedupe on `cluster` (issuer + baseline date) first, or you will double-count exactly the way an earlier version of this dataset did.

    import pandas as pd, statistics
    ev = pd.read_csv("filing_price_impact.csv",
                     dtype={"code": str, "cluster": str, "rcept_no": str, "receipt_time": str})
    d = ev[ev.filing_type_en.eq("Dividend decision") & ev.h5_excess_pct.notna()]
    d = d.drop_duplicates("cluster")
    print(round(statistics.median(d.h5_excess_pct), 2), len(d))
    # -1.12 112 - the same number the summary reports

## This is a record, not a claim

A filing and a price move inside the same window does not mean one caused the other. Earnings, sector rotation and the market itself are all in there. Not investment advice, and not a recommendation to buy or sell any security.

## Live version, and how to cite

This upload is a snapshot. The pipeline republishes every trading evening - no signup, no API key, no request quota, CORS open:

- Catalog: https://aikstockdata.com/data/public/index.json
- Filing impact with the method written out: https://aikstockdata.com/en/filing-impact
- Immutable dated copies for citation: https://aikstockdata.com/data/public/snapshots/index.json
- Receipt times (not in any public API): https://aikstockdata.com/data/public/dart_receipt_times.json
- Today's filings with receipt times, published intraday at 15:00 KST: https://aikstockdata.com/data/public/disclosures_intraday.json
- Hugging Face, same data as JSON Lines: https://huggingface.co/datasets/aikstockdata/korea-equity-daily
- Frozen monthly snapshot: https://huggingface.co/datasets/aikstockdata/korea-equity-daily-2026-08

Source: Financial Services Commission open-data portal (prices) and DART, the Financial Supervisory Service filing system.

License: aiksd-public-1.1 (https://aikstockdata.com/licenses/aiksd-public-1.1.txt). Non-commercial use with attribution. Commercial redistribution is not permitted in any form. Market prices originate from the Financial Services Commission (Korea) public data portal and are also subject to that source's licence (KOGL Type 4: attribution, non-commercial, no derivatives).

출처: Kaggle (aikstokdata/korean-equity-daily-prices-dart-filing-impact)
태그: finance, korea, korean
라이선스: Other (specified in description)
수정일: 2026-09-21T02:20:54.770Z
