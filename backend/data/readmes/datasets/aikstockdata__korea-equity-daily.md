---
license: other
license_name: aiksd-public-1.1
license_link: https://aikstockdata.com/licenses/aiksd-public-1.1.txt
language:
- en
- ko
pretty_name: 한국주식데이터 — Korean Equity Daily Prices and DART Filing Impact
size_categories:
- 100K<n<1M
task_categories:
# 이 태그는 "이 데이터로 그런 작업을 할 수 있다"는 검색용 표시이지, 우리가 예측을
# 한다는 뜻이 아니다. 본문의 "record, not a claim" 과 충돌한다는 리뷰 지적(2026-08-06)에
# 대해, 태그는 유지하고 카드 본문에서 그 차이를 한 줄로 밝히는 쪽을 택했다.
- time-series-forecasting
- tabular-regression
tags:
- finance
- stocks
- korea
- kospi
- kosdaq
- equities
- event-study
- dart
- ohlcv
- konex
- south-korea
- stock-market
- financial-data
configs:
- config_name: daily_prices
  data_files: daily_prices.parquet
- config_name: stocks
  data_files: stocks.parquet
- config_name: filing_impact_summary
  data_files: filing_impact_summary.parquet
- config_name: filing_price_impact
  data_files: filing_price_impact.parquet
dataset_info:
- config_name: daily_prices
  features:
  - name: code
    dtype: string
  - name: name_ko
    dtype: string
  - name: market
    dtype: string
  - name: date
    dtype: string
  - name: close_krw
    dtype: int64
  - name: volume
    dtype: int64
  splits:
  - name: train
    num_examples: 880740
- config_name: stocks
  features:
  - name: code
    dtype: string
  - name: name_ko
    dtype: string
  - name: market
    dtype: string
  - name: close_krw
    dtype: int64
  - name: change_pct
    dtype: float64
  - name: market_cap_krw
    dtype: int64
  splits:
  - name: train
    num_examples: 2787
- config_name: filing_impact_summary
  features:
  - name: filing_type_ko
    dtype: string
  - name: filing_type_en
    dtype: string
  - name: n_max
    dtype: int64
  - name: withheld_reason
    dtype: string
  - name: h0_n
    dtype: int64
  - name: h0_n_filings
    dtype: int64
  - name: h0_enough
    dtype: bool
  - name: h0_median_excess_pct
    dtype: float64
  - name: h0_median_ci95_lo
    dtype: float64
  - name: h0_median_ci95_hi
    dtype: float64
  - name: h0_ci_includes_zero
    dtype: bool
  - name: h0_up_ratio_pct
    dtype: float64
  - name: h0_up_ratio_ci95_lo
    dtype: float64
  - name: h0_up_ratio_ci95_hi
    dtype: float64
  - name: h0_up_ratio_ci_includes_50
    dtype: bool
  - name: h0_base_date_from
    dtype: string
  - name: h0_base_date_to
    dtype: string
  - name: h1_n
    dtype: int64
  - name: h1_n_filings
    dtype: int64
  - name: h1_enough
    dtype: bool
  - name: h1_median_excess_pct
    dtype: float64
  - name: h1_median_ci95_lo
    dtype: float64
  - name: h1_median_ci95_hi
    dtype: float64
  - name: h1_ci_includes_zero
    dtype: bool
  - name: h1_up_ratio_pct
    dtype: float64
  - name: h1_up_ratio_ci95_lo
    dtype: float64
  - name: h1_up_ratio_ci95_hi
    dtype: float64
  - name: h1_up_ratio_ci_includes_50
    dtype: bool
  - name: h1_base_date_from
    dtype: string
  - name: h1_base_date_to
    dtype: string
  - name: h5_n
    dtype: int64
  - name: h5_n_filings
    dtype: int64
  - name: h5_enough
    dtype: bool
  - name: h5_median_excess_pct
    dtype: float64
  - name: h5_median_ci95_lo
    dtype: float64
  - name: h5_median_ci95_hi
    dtype: float64
  - name: h5_ci_includes_zero
    dtype: bool
  - name: h5_up_ratio_pct
    dtype: float64
  - name: h5_up_ratio_ci95_lo
    dtype: float64
  - name: h5_up_ratio_ci95_hi
    dtype: float64
  - name: h5_up_ratio_ci_includes_50
    dtype: bool
  - name: h5_base_date_from
    dtype: string
  - name: h5_base_date_to
    dtype: string
  - name: h20_n
    dtype: int64
  - name: h20_n_filings
    dtype: int64
  - name: h20_enough
    dtype: bool
  - name: h20_median_excess_pct
    dtype: float64
  - name: h20_median_ci95_lo
    dtype: float64
  - name: h20_median_ci95_hi
    dtype: float64
  - name: h20_ci_includes_zero
    dtype: bool
  - name: h20_up_ratio_pct
    dtype: float64
  - name: h20_up_ratio_ci95_lo
    dtype: float64
  - name: h20_up_ratio_ci95_hi
    dtype: float64
  - name: h20_up_ratio_ci_includes_50
    dtype: bool
  - name: h20_base_date_from
    dtype: string
  - name: h20_base_date_to
    dtype: string
  splits:
  - name: train
    num_examples: 29
- config_name: filing_price_impact
  features:
  - name: rcept_no
    dtype: string
  - name: receipt_date
    dtype: string
  - name: receipt_time
    dtype: string
  - name: receipt_session
    dtype: string
  - name: code
    dtype: string
  - name: name_ko
    dtype: string
  - name: market
    dtype: string
  - name: filing_type_ko
    dtype: string
  - name: filing_type_en
    dtype: string
  - name: kind
    dtype: string
  - name: cluster
    dtype: string
  - name: price_break
    dtype: bool
  - name: base_date
    dtype: string
  - name: base_close_krw
    dtype: float64
  - name: h0_date
    dtype: string
  - name: h0_return_pct
    dtype: float64
  - name: h0_market_return_pct
    dtype: float64
  - name: h0_excess_pct
    dtype: float64
  - name: h1_date
    dtype: string
  - name: h1_return_pct
    dtype: float64
  - name: h1_market_return_pct
    dtype: float64
  - name: h1_excess_pct
    dtype: float64
  - name: h5_date
    dtype: string
  - name: h5_return_pct
    dtype: float64
  - name: h5_market_return_pct
    dtype: float64
  - name: h5_excess_pct
    dtype: float64
  - name: h20_date
    dtype: string
  - name: h20_return_pct
    dtype: float64
  - name: h20_market_return_pct
    dtype: float64
  - name: h20_excess_pct
    dtype: float64
  - name: dart_url
    dtype: string
  splits:
  - name: train
    num_examples: 2803
---

# Korean Equity Daily Prices + DART Filing Impact (한국주식데이터)

Daily settled closes for **2,787 Korean listed companies** (KOSPI, KOSDAQ and KONEX) across
321 trading days (2025-05-28 → 2026-09-17), plus a table of what stocks did after each type of
regulatory filing. The per-stock history is no longer cut at 250 days: since the 2026-09-14 publish
the live files gain one row every trading day, and this repository is a dated snapshot of them.

Korean equity data is oddly hard to get. The official sources are free but gated: the
Financial Services Commission open-data portal wants an API key and returns raw payloads with
Korean field names, and DART (the disclosure system) is a separate registration. This is the
same data, already joined, as plain CSV — no key and no registration.

```python
from datasets import load_dataset

px = load_dataset("aikstockdata/korea-equity-daily", "daily_prices", split="train")
print(px[0])
# {'code': '000020', 'name_ko': '동화약품', 'market': 'KOSPI',
#  'date': '20250528', 'close_krw': 6430, 'volume': 31856}
```

## A worked example

`receipt_time_matters.ipynb` in this repository reproduces one finding end to end from the
public URLs alone: **in our ledger of the filing types we track, more than half were received after the market closed**,
so reading the same-day close as a reaction to them produces an artefact. The notebook is the
reason the `filing_price_impact` table carries a receipt timestamp and a session marker at all.

```python
from datasets import load_dataset
ev = load_dataset("aikstockdata/korea-equity-daily", "filing_price_impact", split="train")
# every row carries the receipt time (HH:MM) and the session it landed in
```

## Contents

### `daily_prices` — 880,740 rows

One row per stock per trading day, **2025-05-28 → 2026-09-17** (321 trading days). This table is a fixed snapshot; the live per-stock files it came from keep growing (no rolling 250-day cut).

| column | type | note |
|---|---|---|
| `code` | string | 6-digit Korean ticker, zero-padded. Keep it a string — `005930` is Samsung Electronics |
| `name_ko` | string | Company name in Korean |
| `market` | string | `KOSPI` (915 names) or `KOSDAQ` (1,766 names) or `KONEX` (106 names) |
| `date` | string | `YYYYMMDD`, Korea Standard Time trading date |
| `close_krw` | int | Settled close in won. Not adjusted for splits or dividends |
| `volume` | int | Shares traded. `0` means no trades, which is a fact, not a gap |

Holidays and non-trading days have **no row**. Do not assume date continuity — align on the
dates present, not on a calendar range. Names listed after the first date have fewer rows — use each
stock's own first date, not the table's.

**Identifiers are strings, on purpose.** `code`, `date`, `rcept_no` and every date field are
strings. A Korean ticker is six digits *including leading zeros* — `000020` is Dongwha Pharm,
and `20` is nothing at all. Read as integers, they stop joining to anything, including this
project's own per-stock files at `/data/public/s/000020.json`.

This is why the loadable files here are **Parquet, not CSV**. CSV carries values without
types, so the reader guesses — and the guess destroys the zero padding. It was wrong on this
dataset until it was caught and fixed. Parquet keeps the type with the column, so there is
nothing left to guess.

The configs pointed at JSON Lines until 2026-09-09. JSONL is self-typed too and it was correct,
but `daily_prices.jsonl` had grown to 86 MB and the Hub's auto-conversion job kept being killed
on it — `Job has been terminated due to a temporary spike in resource usage`. The visible cost
was that this repository was publicly tagged `size_categories:1K<n<10K` while `daily_prices`
alone holds 880,740 rows: the Hub had measured only the three small tables. The same
table is 3.5 MB as Parquet, which the Hub reads without converting anything.

The `.csv` and `.jsonl` files are still in the repository — they are convenient over `curl` —
but they are **not** what the configs above load. If you read the CSVs yourself, force the
identifier columns to text:

```python
pd.read_csv("daily_prices.csv", dtype={"code": str, "date": str})
```

### `stocks` — 2,787 rows

Master list as of the 2026-09-17 close — the same trading day `daily_prices` ends on:
`code`, `name_ko`, `market`, `close_krw`, `change_pct`, `market_cap_krw`.

### `filing_impact_summary` — 29 rows

The one people come for. Every filing of the types we track in the collection window is joined to that
company's own daily closes and to its own index, giving the **median market-adjusted return**
after each filing type. 2,803 filings so far.

| Filing type | +1 trading day | +5 trading days |
|---|---|---|
| Periodic financial report | -0.41% / 44% / n=1450 | -0.37% * / 48% / n=1444 |
| Supply contract | +0.02% * / 51% / n=256 | +0.74% * / 54% / n=220 |
| Preliminary earnings (consolidated) | -0.08% * / 49% / n=252 | +0.43% * / 53% / n=252 |
| Preliminary earnings (separate) | -1.31% / 38% / n=202 | -3.37% / 36% / n=202 |
| Dividend decision | -0.55% * / 46% / n=116 | -1.12% * / 43% / n=112 |
| Treasury stock trust contract | +2.31% / 67% / n=54 | +3.63% / 71% / n=52 |
| Treasury stock trust termination | -0.03% * / 50% / n=44 | -0.59% * / 43% / n=42 |
| Convertible bond issuance | -0.28% * / 46% / n=44 | +0.39% * / 53% / n=38 |
| Largest shareholder change | -0.49% * / 45% / n=42 | -1.74% * / 34% / n=35 |
| Preliminary earnings | +0.12% * / 51% / n=39 | -1.29% * / 46% / n=37 |
| Treasury stock disposal | -0.55% * / 43% / n=37 | -0.66% * / 46% / n=35 |
| Treasury stock acquisition | +4.51% * / 69% / n=32 | +4.35% * / 69% / n=32 |
| New facility investment | -1.68% * / 39% / n=28 | -2.13% * / 36% / n=25 |
| Merger | +2.33% * / 67% / n=24 | +3.70% * / 70% / n=23 |
| Subsidiary paid-in capital increase | +0.27% * / 50% / n=20 | n=18 (withheld) |

*median market-adjusted return / share that beat its index / distinct price paths.*
**`*` marks a 95% interval that spans zero — that median is not distinguishable from zero.**
Fourteen more filing types are in the file with samples too small to report.

**Read that asterisk before anything else.** Across all four horizons there are 56 cells
carrying a number and **41 of them are starred**. Fifteen are not: periodic financial report at the baseline day (-0.55%, interval -0.67 to -0.38, beat rate 40%, n=1449); periodic financial report at +1 day (-0.41%, interval -0.64 to -0.26, beat rate 44%, n=1450); periodic financial report at +20 days (+1.38%, interval +0.68 to +1.91, beat rate 55%, n=1411); supply contract at +20 days (-2.83%, interval -6.00 to -0.32, beat rate 38%, n=118); preliminary earnings (consolidated) at +20 days (-2.89%, interval -4.92 to -1.39, beat rate 39%, n=251); preliminary earnings (separate) at +1 day (-1.31%, interval -2.05 to -0.35, beat rate 38%, n=202); preliminary earnings (separate) at +5 days (-3.37%, interval -4.98 to -1.74, beat rate 36%, n=202); preliminary earnings (separate) at +20 days (-3.13%, interval -4.74 to -1.26, beat rate 38%, n=202); dividend decision at +20 days (-3.61%, interval -7.94 to -0.53, beat rate 37%, n=107); treasury stock trust contract at the baseline day (+4.22%, interval +2.12 to +5.09, beat rate 80%, n=54); treasury stock trust contract at +1 day (+2.31%, interval +0.16 to +3.43, beat rate 67%, n=54); treasury stock trust contract at +5 days (+3.63%, interval +0.84 to +8.19, beat rate 71%, n=52); convertible bond issuance at +20 days (-6.99%, interval -11.42 to -2.09, beat rate 15%, n=20); preliminary earnings at +20 days (-7.33%, interval -11.24 to -2.03, beat rate 26%, n=23); treasury stock acquisition at the baseline day (+2.87%, interval +0.25 to +6.67, beat rate 72%, n=32).
Everything else in this table is a number you cannot distinguish from zero.
Publishing the intervals was the point; almost none of these survive them.

**Earlier (2026-08-06): adding six days of data made the table weaker, not stronger.** On 2026-08-05 two cells
cleared zero; on 2026-08-06, with 644 filings instead of 598, only one does. Dividend decisions
at +5 days fell from +3.52% (interval +0.23 to +8.93) to +2.21% with an interval that now spans
zero. Periodic financial reports came back into the table at +1 day by crossing the n=20
threshold — at -0.46%, starred. This is what a small sample looks like from the inside, and it
is the reason the intervals are printed rather than the medians alone. The numbers here are
regenerated from the live site on every upload; expect them to move again.

**An earlier revision fixed a double-count.** Until 2026-08-05 each DART receipt number counted
as one observation. When one company files three documents on the same day the baseline and the
entire price path are identical across them, so a single company-day was counted three times.
Aggregation is now keyed on issuer × baseline date × filing type. Both counts are published:
`n` is distinct price paths, `n_filings` is receipts.

### `filing_price_impact` — 2,803 rows

The individual filings behind that table, one row each, so you can recompute the aggregates
instead of taking them on trust — and disagree with them.

| column | note |
|---|---|
| `rcept_no` | DART receipt number. `dart_url` opens the original document |
| `receipt_date`, `receipt_time`, `receipt_session` | when DART received it — date, HH:MM (KST), and `pre_open` / `intraday` / `after_close` / `unknown`. OpenDART's API has the date only; the time comes from DART's recent-filings page, so it is empty where we could not collect it |
| `code`, `name_ko`, `market` | the filing company |
| `filing_type_ko`, `filing_type_en`, `kind` | type, matching the summary table exactly |
| `cluster` | issuer + baseline date. Rows sharing one are the same price path — dedupe on this before aggregating, or you will double-count |
| `price_break` | true where an ex-rights date or share consolidation resets the quoted price |
| `base_date`, `base_close_krw` | the baseline: first trading-day close on or after receipt |
| `h0_*` | the **baseline day itself** — previous close into the baseline close |
| `h1_*`, `h5_*`, `h20_*` | horizon date, raw return, index return, and the difference |

```python
import statistics
from datasets import load_dataset

ev = load_dataset("aikstockdata/korea-equity-daily", "filing_price_impact", split="train")
seen = {}                       # 같은 issuer-day 는 한 번만 — 집계와 같은 규칙
for r in ev:
    if r["filing_type_en"] == "Dividend decision" and r["h5_excess_pct"] is not None:
        seen.setdefault(r["cluster"], r["h5_excess_pct"])
x = list(seen.values())
print(round(statistics.median(x), 2), len(x))
# -1.12 112  — the same number the summary reports
```

Every published median reproduces exactly from these rows; that is checked before each upload.

**Method.** Baseline is the first trading-day close on or after the filing receipt date.
Returns are measured at +1, +5 and +20 **trading** days — five rows forward in that stock's own
series, not a calendar offset, because Korean market closures are irregular. From each return
the stock's own index (KOSPI or KOSDAQ) over the identical window is subtracted. The statistic
is the **median**, not the mean. Amended filings are dropped because they duplicate the
original.

**Every published median ships with a 95% interval.** `*_median_ci95_lo/hi` come from order
statistics, `*_up_ratio_ci95_lo/hi` from a Wilson score interval — both closed-form and
deterministic, so they are identical on every rebuild. `*_ci_includes_zero` is set when the
interval spans zero, which means that median is not distinguishable from zero. A bold number
without its interval is the dishonest option; 70% at n=20 has a Wilson interval of 48–86%.

**The `h0` columns are the baseline day itself**, measured from the previous trading day's
close. DART accepts filings during the session and after it. OpenDART's public API gives only the
receipt *date*; this table adds `receipt_time` and `receipt_session`, collected from DART's
recent-filings page. `h0` mixes sessions — for a filing received after the close the whole
baseline-day move precedes it, so filter on `receipt_session` before reading `h0` as a reaction.
A filing made mid-session is already partly
reflected in that day's close, and that part disappears into the baseline. `h0` exists to make
the missing piece visible, not to remove it.

**Each horizon covers a different set of filings** — `*_base_date_from/to` say which. A longer
horizon excludes recent filings that have not had time to elapse, so its sample clusters
earlier. Reading two horizons side by side as "what happened N days later" is wrong when those
windows differ.

When one company files several documents on the same day, they share a baseline and therefore
an identical price path. Those count **once** per filing type; `n_filings` records how many
receipts sat behind that count.

**Fewer than 20 observations gets no number at all** — a median over eight cases turns
coincidence into a statistic. That is why the `_enough` column exists and why most of this
table is withheld.

**Four types are withheld no matter how large the sample gets**: paid-in capital increase,
bonus issue, paid-in and bonus issue, and reverse stock split. An ex-rights date or a share
consolidation resets the quoted price mechanically, and these closes are not adjusted for
corporate actions, so a window containing that date measures the break rather than a market
reaction. Their individual rows stay in `filing_price_impact`, flagged `price_break` — not
hidden, just never averaged. The **+20 day columns now carry numbers for 12 filing types** (Convertible bond issuance, Dividend decision, Largest shareholder change, Periodic financial report, Preliminary earnings, Preliminary earnings (consolidated), Preliminary earnings (separate), Supply contract, Treasury stock acquisition, Treasury stock disposal, Treasury stock trust contract, Treasury stock trust termination); the rest still have too few distinct price paths and stay empty.

**This is a record, not a claim.** A filing and a price move inside the same window does not
mean one caused the other. Earnings, sector rotation and the market itself are all in there.
It is not a signal and it is not investment advice. The `task_categories` tags on this card say
what the data can be *used for* in a search index; they are not a claim that anything here
forecasts anything.

## What is not here

Read this before integrating, so you can stop early if it matters:

- **No real-time or intraday prices.** These are previous-trading-day settled closes from the
  government feed (T+1). If you need live quotes, this is the wrong dataset.
- **No PER/PBR columns in this dataset, and no target prices, analyst ratings, investor-type flows
  or sector tags.** Consensus-type fields are brokerage-derived and are not redistributed. Trailing
  PER (TTM) and PBR computed from public filings only are published on the site per stock
  (`/data/public/s/{code}.json` → `valuation`, `null` with a reason where not computable) — not mirrored here.
- **No adjustment for splits, mergers or dividends.** Closes are as-reported.
- **Korean equities only** — every KOSPI, KOSDAQ and KONEX stock in the government price feed that had a
  quote that day (~2,787 names). No ETFs or ETNs. Suspended and just-listed names without a
  quote that day fall out.
- **The filing sample is young.** Every median above will move.
- Company names are Korean. Column names are English.

## Snapshot vs. live

**`main` is overwritten on every upload — it is not citable.** This repository is regenerated
from the live site each time it is refreshed, so a number you quote from `main` may not exist
here next week. The table above already moved once between two consecutive uploads.

To cite, pin the revision. Every upload is a commit, and commits are permanent:

```python
load_dataset("aikstockdata/korea-equity-daily", "filing_impact_summary",
             revision="<commit sha from the repo history>", split="train")
```

Quote that revision together with the `generated_kst` stamp carried inside the JSON.

Two other ways to get a number that stays put:

- **A frozen monthly repository.** A month's snapshot is uploaded once as
  `aikstockdata/korea-equity-daily-YYYY-MM` and never updated. Cite it by name; no revision
  hash needed. Not every month has one, and the current month never does until it ends —
  which ones exist is listed at <https://huggingface.co/aikstockdata>. Guessing this
  month's name will 404.
- **A dated file on the site.** Every publish leaves an immutable copy at
  `https://aikstockdata.com/data/public/snapshots/disclosure_impact_YYYY-MM-DD.json`, listed in
  `snapshots/index.json`. Aggregates only, no per-filing rows, but it is the same table.

The pipeline republishes every trading evening; that live version, with no signup, no API key,
no request quota and CORS open, is at:

- Catalog of every file with byte size and freshness: <https://aikstockdata.com/data/public/index.json>
- One stock's full stored history of closes, in one file that gains a row every trading day (its `count` and `retention` say how much and why): `https://aikstockdata.com/data/public/s/005930_history.json`
- Filing impact, in English, with the method written out:
  <https://aikstockdata.com/en/filing-impact>
- Remote MCP server for Claude / ChatGPT (no auth): `https://mcp.aikstockdata.com/mcp` — setup: <https://aikstockdata.com/en/mcp>
- Code, examples and the MCP registry manifest: <https://github.com/na77tech-creator/aikstockdata>
- The same as JSON, per-filing values keyed by DART receipt number:
  <https://aikstockdata.com/data/public/disclosure_impact.json>
  (aggregates only, smaller: `disclosure_impact_summary.json`)
- OpenAPI 3.1 spec: <https://aikstockdata.com/openapi.json>
- English overview: <https://aikstockdata.com/en>

A caveat we used to have, now gone: from 2026-08-11 to 2026-09-16 the CDN bot filter returned
403 to the default `Python-urllib` user agent. That filter is off since 2026-09-16 — every agent
we tested returns 200 (6 agents x 4 paths), including a bare `pd.read_csv(url)` and
`urllib.request.urlopen(url)`. If you ever do get a 403, send any `User-Agent` header.

## Source, license, citation

Derived from **Financial Supervisory Service DART** (disclosures) and the **Financial Services
Commission** open-data portal (settled quotes), both Korean public-sector data.

**License: `aiksd-public-1.1`** — <https://aikstockdata.com/licenses/aiksd-public-1.1.txt>

Data published here (/data/public/*) may be quoted and used for non-commercial purposes with attribution. Commercial redistribution is not permitted in any form. Market prices come from the Financial Services Commission's public data portal and are also subject to that source's licence (KOGL Type 4: attribution, non-commercial, no derivatives) and notices; disclosure content follows FSS DART's terms. Real-time quotes are never redistributed here.

In short: Non-commercial use with attribution; commercial redistribution is not permitted. The Korean canonical text at the end of this card
prevails where the two differ.

```
Data: aikstockdata.com — source: FSS DART, FSC Korea Open Data Portal
```

**DOI** — a related frozen snapshot (quote basis date 2026-09-02; quotes, disclosures and rankings as CSV/JSON) is archived on Zenodo under this concept DOI:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22502446.svg)](https://doi.org/10.5281/zenodo.22502446)

```bibtex
@dataset{aikstockdata_korea_equity_daily,
  title  = {Korea Stock Market Daily Dataset: Settled Closes, DART Filings with
            Receipt Time, and Quarterly Earnings (KOSPI, KOSDAQ, KONEX)},
  author = {aikstockdata},
  doi    = {10.5281/zenodo.22502446},
  url    = {https://aikstockdata.com},
  note   = {Concept DOI — resolves to the latest version}
}
```

Cite the DOI when you need a stable academic reference; cite a pinned Hugging Face revision
(above) when you need the exact bytes you read.

The DOI is a citation identifier; the terms of use are `aiksd-public-1.1` above.

## Disclaimer

Information only. Not investment advice, and not a recommendation to buy or sell any security.
Every number is a record of the past. Investment decisions and their consequences are the
reader's own.

---

<details>
<summary>한국어 요약</summary>

한국 상장기업 **2,787종목**의 **321거래일(2025-05-28 → 2026-09-17) 확정 종가·거래량**(880,740행)과, DART 공시
유형별로 접수일 이후 **시장조정 수익률 중앙값**을 정리한 표입니다.

- `daily_prices` — 종목×거래일 종가·거래량. 휴장일은 행이 없으므로 날짜 연속성을 가정하지
  마세요. 수정주가 아님(액면분할·배당 미조정).
- 원본 시계열(`s/{종목코드}_history.json`)은 2026-09-14 발행부터 250거래일에서 자르지 않고 매 거래일 한 행씩 쌓습니다. 이 저장소는 그 날짜 스냅샷입니다.
- `stocks` — 2026-09-17 종가 기준 종목 마스터(`daily_prices` 의 마지막 거래일과 같음).
- `filing_impact_summary` — 공시 29유형. 기준점은 접수일 이후 첫 거래일 종가, 구간은
  **거래일** 기준, 소속 시장 지수 등락률을 뺀 값의 **중앙값**. 표본 20건 미만은 수치를
  내지 않습니다. +20거래일 칸은 현재 12개 유형에 수치가 있습니다(나머지는 표본이 모자라 비어 있습니다).

**인과가 아니라 기록입니다.** 같은 구간에 공시와 주가 변동이 함께 있었다는 사실일 뿐이며,
투자 권유가 아닙니다.

이 저장소는 **2026-09-17 스냅샷**입니다. 매 거래일 갱신되는 원본은 가입·API 키 없이(요청
쿼터도 없습니다) <https://aikstockdata.com/data/public/index.json> 에서 받습니다.

### 라이선스·인용·면책 (정본)

아래 문단은 사이트의 단일 출처(`legal_text.py`)에서 그대로 옮긴 것입니다.
**요약하거나 다시 쓰지 않습니다** — 문구가 갈라져 실시간 재배포 단서가 통째로 빠진
사고가 실제로 있었고(2026-08, 15:00 장중 발행분), 그 뒤로 문구는 한 곳에서만 씁니다.
`test_mirror_license.py` 가 이 절과 원본을 매번 대조합니다. 위 영문 절은 이 정본의
요약이며, 조건이 갈리면 **아래가 우선합니다.**

**출처**

금융감독원 전자공시시스템(DART) · 금융위원회 공공데이터포털

Financial Supervisory Service DART (filings) · Financial Services Commission public data portal (prices)

**라이선스**

출처 표기 · 비영리 인용·이용 · 상업적 재배포 불허(시세는 공공누리 제4유형도 따름)

본 사이트가 공개하는 데이터(/data/public/*)는 출처를 표기하면 비영리 목적으로 인용·이용할 수 있습니다. 상업적(영리) 목적의 재배포는 어떤 경우에도 허용하지 않습니다. 시세(종가·거래량·시가총액 등)는 금융위원회 공공데이터포털이 원천이며 원천의 이용허락범위(공공누리 제4유형: 출처표시·상업적 이용금지·변경금지)와 제공기관 안내도 함께 따라야 하고, 공시 내용은 금융감독원 전자공시시스템(DART)의 이용 조건을 따릅니다. 다만 증권사 실시간 시세 등 원천의 실시간 정보를 그대로 재배포하는 것은 허용되지 않습니다.

출처를 표기하면 비영리 목적으로 인용·이용할 수 있고, 상업적 재배포는 허용하지 않습니다.

**라이선스 정본 (2026-08-22 신설 · 1.1 개정)**

위 조건에는 식별자와 버전이 붙습니다 — `aiksd-public-1.1` (version 1.1).
적용 범위는 `/data/public/**` 이며, 정본은 아래 주소입니다.

https://aikstockdata.com/licenses/aiksd-public-1.1.txt

변경 이유: 원천(금융위원회 공공데이터 주식시세정보·지수시세정보)의 이용허락범위가 2026-09-09 부터 공공누리 제4유형으로 바뀌었습니다. 이전 버전 aiksd-public-1.0 은 기록으로 남기며, 이 버전의 시행일부터 이 사이트의 이용 조건은 이 파일을 따릅니다.

정본 파일은 수정되지 않습니다. 조건이 바뀌면 새 버전 파일이 생기며, 전 버전 목록은
<https://aikstockdata.com/licenses/index.json> 에 있습니다.
공개 JSON 은 저마다 `license.id`·`license.version`·`license.scope`·`license.url`·
`license.full_text` 를 실어 같은 값을 기계가 읽을 수 있게 합니다.

**인용 예시**

자료: 한국주식데이터(aikstockdata.com) — 원천: 금융감독원 DART · 금융위원회 공공데이터포털

Source: aikstockdata (aikstockdata.com) — original data: FSS DART, FSC open data portal, Republic of Korea

**면책**

정보 제공 목적이며 투자 권유가 아닙니다. 데이터는 갱신 시점 기준 스냅샷(매 거래일 저녁 6시 30분 전후 갱신)이며, 투자 판단과 책임은 이용자 본인에게 있습니다.

</details>
