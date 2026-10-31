---
license: other
license_name: aiksd-public-1.1
license_link: https://aikstockdata.com/licenses/aiksd-public-1.1.txt
language:
- en
- ko
pretty_name: Korean Equity Daily Prices and DART Filing Impact
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
configs:
- config_name: daily_prices
  data_files: daily_prices.jsonl
- config_name: stocks
  data_files: stocks.jsonl
- config_name: filing_impact_summary
  data_files: filing_impact_summary.jsonl
- config_name: filing_price_impact
  data_files: filing_price_impact.jsonl
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
    num_examples: 361143
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
    num_examples: 1463
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
    num_examples: 22
- config_name: filing_price_impact
  features:
  - name: rcept_no
    dtype: string
  - name: receipt_date
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
    num_examples: 644
---

> **This repository is frozen.** It is the 2026-08 snapshot of
> [`aikstockdata/korea-equity-daily`](https://huggingface.co/datasets/aikstockdata/korea-equity-daily),
> taken once and never updated. Cite this repository when you need the numbers to
> still be there later.
>
> The rolling dataset is regenerated every trading evening and its `main` is
> overwritten, so figures quoted from it do not survive. Figures here do.
> The live, always-current files are at <https://aikstockdata.com/data/public/>.

# Korean Equity Daily Prices + DART Filing Impact

Daily settled closes for **1,463 Korean listed companies** (KOSPI and KOSDAQ) over the last
250 trading days, plus a table of what stocks did after each type of regulatory filing.

Korean equity data is oddly hard to get. The official sources are free but gated: the
Financial Services Commission open-data portal wants an API key and returns raw payloads with
Korean field names, and DART (the disclosure system) is a separate registration. Commercial
APIs either paywall Korea or cover only large caps. This is the same data, already joined,
as plain CSV.

```python
from datasets import load_dataset

px = load_dataset("aikstockdata/korea-equity-daily-2026-08", "daily_prices", split="train")
print(px[0])
# {'code': '000020', 'name_ko': '동화약품', 'market': 'KOSPI',
#  'date': '20250725', 'close_krw': 6780, 'volume': 34614}
```

## Contents

### `daily_prices` — 361,143 rows

One row per stock per trading day, **2025-07-25 → 2026-08-04** (250 trading days).

| column | type | note |
|---|---|---|
| `code` | string | 6-digit Korean ticker, zero-padded. Keep it a string — `005930` is Samsung Electronics |
| `name_ko` | string | Company name in Korean |
| `market` | string | `KOSPI` (634 names) or `KOSDAQ` (829) |
| `date` | string | `YYYYMMDD`, Korea Standard Time trading date |
| `close_krw` | int | Settled close in won. Not adjusted for splits or dividends |
| `volume` | int | Shares traded. `0` means no trades, which is a fact, not a gap |

Holidays and non-trading days have **no row**. Do not assume date continuity — align on the
dates present, not on a calendar range. Newly listed names have fewer than 250 rows.

**Identifiers are strings, on purpose.** `code`, `date`, `rcept_no` and every date field are
strings. A Korean ticker is six digits *including leading zeros* — `000020` is Dongwha Pharm,
and `20` is nothing at all. Read as integers, they stop joining to anything, including this
project's own per-stock files at `/data/public/s/000020.json`.

This is why the loadable files here are **JSON Lines, not CSV**. CSV carries values without
types, so the reader guesses — and the guess destroys the zero padding. It was wrong on this
dataset until it was caught and fixed. The `.csv` files are still in the repository because
they are a third of the size and convenient over `curl`, but they are **not** what the configs
above load. If you read the CSVs yourself, force the identifier columns to text:

```python
pd.read_csv("daily_prices.csv", dtype={"code": str, "date": str})
```

### `stocks` — 1,463 rows

Master list as of the 2026-08-04 close — the same trading day `daily_prices` ends on:
`code`, `name_ko`, `market`, `close_krw`, `change_pct`, `market_cap_krw`.

### `filing_impact_summary` — 22 rows

The one people come for. Every DART filing in the collection window is joined to that
company's own daily closes and to its own index, giving the **median market-adjusted return**
after each filing type. 644 filings so far.

| Filing type | +1 trading day | +5 trading days |
|---|---|---|
| Supply contract | -0.18% * / 46% / n=142 | -0.27% * / 48% / n=81 |
| Preliminary earnings (consolidated) | -0.14% * / 49% / n=140 | +0.49% * / 51% / n=51 |
| Preliminary earnings (separate) | -1.50% * / 39% / n=74 | +1.32% * / 59% / n=22 |
| Dividend decision | -0.16% * / 49% / n=47 | +2.21% * / 69% / n=32 |
| Largest shareholder change | +1.53% * / 67% / n=27 | n=15 (withheld) |
| Treasury stock trust contract | +2.04% * / 70% / n=20 | n=13 (withheld) |
| Periodic financial report | -0.46% * / 45% / n=20 | n=9 (withheld) |

*median market-adjusted return / share that beat its index / distinct price paths.*
**`*` marks a 95% interval that spans zero — that median is not distinguishable from zero.**
Fifteen more filing types are in the file with samples too small to report.

**Read that asterisk before anything else.** Across all four horizons there are 18 cells
carrying a number and **17 of them are starred**. Exactly one is not: treasury-stock trust
contracts on the baseline day (+2.26%, interval +0.57 to +4.09, beat rate 80% with an interval
of 58–92%, n=20). Everything else in this table is a number you cannot distinguish from zero.
Publishing the intervals was the point; almost none of these survive them.

**Adding six days of data made the table weaker, not stronger.** On 2026-08-05 two cells
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

### `filing_price_impact` — 644 rows

The individual filings behind that table, one row each, so you can recompute the aggregates
instead of taking them on trust — and disagree with them.

| column | note |
|---|---|
| `rcept_no` | DART receipt number. `dart_url` opens the original document |
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

ev = load_dataset("aikstockdata/korea-equity-daily-2026-08", "filing_price_impact", split="train")
seen = {}                       # 같은 issuer-day 는 한 번만 — 집계와 같은 규칙
for r in ev:
    if r["filing_type_en"] == "Dividend decision" and r["h5_excess_pct"] is not None:
        seen.setdefault(r["cluster"], r["h5_excess_pct"])
x = list(seen.values())
print(round(statistics.median(x), 2), len(x))
# 2.21 32  — the same number the summary reports
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
close. DART accepts filings during the session and after it, and the receipt *time* is not in
the public data, so the two cannot be separated. A filing made mid-session is already partly
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
hidden, just never averaged. The **+20 day columns are entirely empty** and left visible: collection
started 2026-07-20, so twenty trading days have not elapsed for anything yet.

**This is a record, not a claim.** A filing and a price move inside the same window does not
mean one caused the other. Earnings, sector rotation and the market itself are all in there.
It is not a signal and it is not investment advice. The `task_categories` tags on this card say
what the data can be *used for* in a search index; they are not a claim that anything here
forecasts anything.

## What is not here

Read this before integrating, so you can stop early if it matters:

- **No real-time or intraday prices.** These are previous-trading-day settled closes from the
  government feed (T+1). If you need live quotes, this is the wrong dataset.
- **No PER, PBR, target prices, analyst ratings, investor-type flows, or sector tags.** Those
  are brokerage-derived; only public-sector data is used here.
- **No adjustment for splits, mergers or dividends.** Closes are as-reported.
- **Korean equities only**, and only the ~1,463 names with a quote on a normal trading day —
  not the entire listed market. Suspended, delisted and just-listed names fall out.
- **The filing sample is young.** Every median above will move.
- Company names are Korean. Column names are English.

## Snapshot vs. live

**`main` is overwritten on every upload — it is not citable.** This repository is regenerated
from the live site each time it is refreshed, so a number you quote from `main` may not exist
here next week. The table above already moved once between two consecutive uploads.

To cite, pin the revision. Every upload is a commit, and commits are permanent:

```python
load_dataset("aikstockdata/korea-equity-daily-2026-08", "filing_impact_summary",
             revision="<commit sha from the repo history>", split="train")
```

Quote that revision together with the `generated_kst` stamp carried inside the JSON. The
pipeline republishes every trading evening; that live version, with no signup, no API key,
no request quota and CORS open, is at:

- Catalog of every file with byte size and freshness: <https://aikstockdata.com/data/public/index.json>
- One stock's year of closes as a single ~7 KB file: `https://aikstockdata.com/data/public/s/005930_history.json`
- Filing impact, in English, with the method written out:
  <https://aikstockdata.com/en/filing-impact>
- The same as JSON, per-filing values keyed by DART receipt number:
  <https://aikstockdata.com/data/public/disclosure_impact.json>
  (aggregates only, smaller: `disclosure_impact_summary.json`)
- OpenAPI 3.1 spec: <https://aikstockdata.com/openapi.json>
- English overview: <https://aikstockdata.com/en>

One caveat worth stating: the CDN's bot filter returns 403 to the default `Python-urllib`
user agent. `requests`, `curl`, `httpx` and browser `fetch` all work; with `urllib`, send any
`User-Agent` header.

## Source, license, citation

Derived from **Financial Supervisory Service DART** (disclosures) and the **Financial Services
Commission** open-data portal (settled quotes), both Korean public-sector data.

**Terms of use (from 2026-09-14): `aiksd-public-1.1`** — Non-commercial use with attribution; commercial redistribution is not permitted. Market prices are also subject to the FSC source licence (KOGL Type 4: attribution, non-commercial, no derivatives). Full text: <https://aikstockdata.com/licenses/aiksd-public-1.1.txt>.

```
Data: aikstockdata.com — source: FSS DART, FSC Korea Open Data Portal
```

## Disclaimer

Information only. Not investment advice, and not a recommendation to buy or sell any security.
Every number is a record of the past. Investment decisions and their consequences are the
reader's own.

---

<details>
<summary>한국어 요약</summary>

한국 상장기업 **1,463종목**의 최근 **250거래일 확정 종가·거래량**(361,143행)과, DART 공시
유형별로 접수일 이후 **시장조정 수익률 중앙값**을 정리한 표입니다.

- `daily_prices` — 종목×거래일 종가·거래량. 휴장일은 행이 없으므로 날짜 연속성을 가정하지
  마세요. 수정주가 아님(액면분할·배당 미조정).
- `stocks` — 2026-08-04 종가 기준 종목 마스터(`daily_prices` 의 마지막 거래일과 같음).
- `filing_impact_summary` — 공시 22유형. 기준점은 접수일 이후 첫 거래일 종가, 구간은
  **거래일** 기준, 소속 시장 지수 등락률을 뺀 값의 **중앙값**. 표본 20건 미만은 수치를
  내지 않습니다. +20거래일 칸은 아직 전부 비어 있습니다(수집 시작 2026-07-20).

**인과가 아니라 기록입니다.** 같은 구간에 공시와 주가 변동이 함께 있었다는 사실일 뿐이며,
투자 권유가 아닙니다.

이 저장소는 **2026-08-05 스냅샷**입니다. 매 거래일 갱신되는 원본은 가입·API 키·요청 제한
없이 <https://aikstockdata.com/data/public/index.json> 에서 받습니다.

출처: 금융감독원 DART · 금융위원회 공공데이터포털.
이용 조건(2026-09-14부터 `aiksd-public-1.1`): 출처를 표기하면 비영리 목적으로 인용·이용할 수 있고, 상업적 재배포는 허용하지 않습니다.

</details>
