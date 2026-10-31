---
license: other
license_name: mixed-see-card
language: [en, ru, zh, ko, ja, fr]
pretty_name: "1F50D: tech and trade press, 2020-2026"
size_categories: [1M<n<10M]
task_categories: [text-retrieval, text-classification]
extra_gated_prompt: >-
  Article text belongs to its publishers. It is shared for research and analysis.
  By requesting access you agree not to republish the text.
extra_gated_button_content: Agree and access
configs:
  - config_name: all
    default: true
    data_files:
      - "articles/dated/*/*.parquet"
      - "articles/undated/*.parquet"
  - config_name: window
    data_files:
      - "articles/dated/2023-0[7-9]/*.parquet"
      - "articles/dated/2023-1[0-2]/*.parquet"
      - "articles/dated/2024-*/*.parquet"
      - "articles/dated/2025-*/*.parquet"
      - "articles/dated/2026-*/*.parquet"
  - config_name: dated
    data_files: "articles/dated/*/*.parquet"
  - config_name: undated
    data_files: "articles/undated/*.parquet"
  - config_name: outliers
    data_files: "articles/outliers/*.parquet"
---

# 1F50D: tech and trade press, 2020-2026

A dated, deduplicated corpus of technology news, trade press and vendor publications: 6,489,215
articles from 1,383 hosts, full extracted text (6,674,439 rows with the outliers).

| Config | Rows | What it is |
|---|---|---|
| `all` (default) | 6,489,215 | `dated` and `undated` |
| `window` | 4,135,904 | published 2023-07 to 2026-09, the three-year window the corpus was built for |
| `dated` | 4,502,047 | every article with a publication date, 2020-01 to 2026-09 |
| `undated` | 1,987,168 | pages with no evidenced publication date |
| `outliers` | 185,224 | pages whose dates are not trustworthy as publication dates, kept apart (see below) |

## Load it

```python
from datasets import load_dataset

ds = load_dataset("IDONTCARELETMEIN/tech-trade-press", "window", split="train", streaming=True)
for row in ds.filter(lambda r: r["host"] == "tomshardware.com").take(5):
    print(row["published"], row["title"])
```

DuckDB reads only the columns and row groups it needs:

```sql
INSTALL httpfs; LOAD httpfs;
CREATE SECRET hf (TYPE huggingface, PROVIDER credential_chain);  -- picks up your hf auth login token
SELECT date_trunc('month', published) AS month,
       count(*) FILTER (WHERE text ILIKE '%solid-state batter%') AS n,
       count(*) AS total
FROM 'hf://datasets/IDONTCARELETMEIN/tech-trade-press/articles/dated/*/*.parquet'
WHERE lang = 'en' AND published >= DATE '2023-07-01'
  AND host_first <= '2023-10'   -- only hosts covered across the whole window
GROUP BY 1 ORDER BY 1;
```

One month to disk:

```bash
hf download IDONTCARELETMEIN/tech-trade-press --repo-type dataset \
  --include "articles/dated/2025-03/*" --local-dir ./f50d
```

Polars, lazily:

```python
import polars as pl
lf = pl.scan_parquet("hf://datasets/IDONTCARELETMEIN/tech-trade-press/articles/dated/*/*.parquet")
lf.filter(pl.col("topics").list.contains("ai")).group_by("host").len().sort("len", descending=True).head(20).collect()
```

## What is in it

Counts below are for `all` (`dated` and `undated`); `outliers` is not included.

Rows by publication year:

| Year | Rows |
|---|---|
| 2020 | 77,640 |
| 2021 | 90,920 |
| 2022 | 131,956 |
| 2023 | 334,647 |
| 2024 | 959,188 |
| 2025 | 1,088,480 |
| 2026 | 1,819,216 |
| undated | 1,987,168 |

Languages:

| Language | Rows | Share |
|---|---|---|
| en | 4,746,830 | 73.1% |
| ru | 744,198 | 11.5% |
| zh | 318,722 | 4.9% |
| ko | 248,366 | 3.8% |
| ja | 164,717 | 2.5% |
| fr | 136,057 | 2.1% |
| other | 130,325 | 2.0% |

Where the date came from:

| date_source | Rows | Share |
|---|---|---|
| meta | 2,637,532 | 40.6% |
| (undated) | 1,987,168 | 30.6% |
| jsonld | 1,546,981 | 23.8% |
| url | 204,206 | 3.1% |
| time | 103,728 | 1.6% |

Source format:

| format | Rows | Share |
|---|---|---|
| html | 6,479,423 | 99.8% |

Topics (a row can carry several):

| Topic | Rows | Share |
|---|---|---|
| technology | 2,176,556 | 33.5% |
| investment | 1,499,852 | 23.1% |
| domain | 1,345,391 | 20.7% |
| money | 1,068,662 | 16.5% |
| ai | 989,733 | 15.3% |
| innovation | 613,439 | 9.5% |

`relevant` is true on 2,974,469 rows (45.8%). Text length: median 3,113 characters, 90th percentile 11,370.

## Layout

```
articles/dated/<YYYY-MM>/NNNN.parquet   by publication month, 2020-01 to 2026-09
articles/undated/NNNN.parquet           no evidenced publication date
articles/outliers/NNNN.parquet          dates kept, but not trustworthy; see date_flag
```

Files hold up to 100,000 rows in row groups of 5,000, zstd-compressed.

## Columns

| Column | Meaning |
|---|---|
| `id` | Row id |
| `url`, `host` | Source page and its host |
| `lang` | Language of the text, py3langid on the first 2,000 characters; rare labels are often misdetections |
| `published` | Publication date, or null in `undated`; in `outliers`, the date the page gave |
| `date_source` | Where the date came from (see the table above); empty when undated |
| `format` | Source format: `html`, `pdf`, `aem`, `xml` |
| `fetched_at` | When the page was fetched (UTC) |
| `title`, `text` | Extracted title and main text |
| `chars`, `words` | Length of `text` |
| `text_sha1` | SHA-1 of `text`; the corpus is deduplicated on it and on `url` |
| `relevant` | Heuristic flag: the page touches technology, investment or innovation vocabulary |
| `topics` | Heuristic topic labels, e.g. `ai`, `technology`, `investment`, `money` |
| `tags` | Reserved; empty in this release |
| `money` | Candidate sentences with amounts, funding rounds, revenue or deal terms: `kinds`, `amount`, `sentence` |
| `deliverables` | Candidate sentences naming launches, releases, deployments, contracts: `trigger`, `sentence` |
| `date_flag` | Null, or in `outliers` why the date is not trusted: `bunched_host`, `stamped_day` |
| `host_first` | First month (`YYYY-MM`) with a trusted dated row from this row's host; `2020-01` means at or before it. Null when the host has none |

One row, with `text` cut short:

```json
{
  "id": 2811374,
  "url": "https://europeanspaceflight.com/uk-based-hyperspectral-data-analytics-startup-messium-raises-3-3m/",
  "host": "europeanspaceflight.com",
  "lang": "en",
  "published": "2025-09-15",
  "date_source": "meta",
  "format": "html",
  "fetched_at": "2026-09-26 21:25:00+00:00",
  "title": "UK-Based Hyperspectral Data Analytics Startup Messium Raises £3.3M",
  "text": "UK-based startup Messium has raised £3.3 million in seed funding to accelerate the rollout of its agricultural analytics platform, which uses AI to analyse hyperspectral satellite data to track nitrogen levels in crops. The analysis can then be used by farmers to more efficiently fertilise crops, mi...",
  "chars": 2605,
  "words": 400,
  "text_sha1": "53532d7b7781af40a27b3b7b188f12acc9507cfc",
  "relevant": true,
  "topics": [
    "ai",
    "domain",
    "innovation",
    "investment",
    "money",
    "technology"
  ],
  "tags": [],
  "money": [
    {
      "kinds": [
        "amount",
        "round",
        "funding"
      ],
      "amount": "£3.3 million",
      "sentence": "UK-based startup Messium has raised £3.3 million in seed funding to accelerate the rollout of its agricultural analytics platform, which uses AI to analyse hyperspectral satellite data to track nitrogen levels in crops."
    }
  ],
  "deliverables": [
    {
      "trigger": "rollout",
      "sentence": "UK-based startup Messium has raised £3.3 million in seed funding to accelerate the rollout of its agricultural analytics platform, which uses AI to analyse hyperspectral satellite data to track nitrogen levels in crops."
    }
  ],
  "date_flag": null,
  "host_first": "2022-02"
}
```

## How it was built

- **Hosts.** The seed was 206 curated hosts across six domains (fintech, energy, medtech,
  logistics, industry, IT). Discovery passes
  added sources in sixteen further fields (space, medicine, infrastructure, chemistry, avionics
  and others) and Chinese-language trade press, each host checked by fetching it.
- **URLs.** Every host's sitemaps were read (its listing pages, for hosts without one), and everything inside the three-year window was
  crawled until the host refused. Pages outside the window were kept when the crawl reached
  them.
- **Text.** The main text of each page, without navigation, ads or boilerplate. PDF, XML and
  AEM JSON bodies are converted to HTML first and extracted the same way.
- **Dates.** From the page itself: meta tags, JSON-LD, the URL, `<time>` elements, or the
  document's own metadata. `date_source` names which. A page with no date evidence is undated.
- **Pruning.** Every page was stored from a successful response. A response other than a 200,
  a challenge page, a redirect to a homepage, an empty or near-empty extraction, a JSON or
  non-HTML page with no convertible body, and gibberish were all dropped.
- **Deduplication.** Exact duplicates by `text_sha1`, keeping the first; each `url` appears
  once.
- **Tags.** `money` and `deliverables` are regex candidates; `relevant` and `topics` are
  keyword rules. None of them was reviewed by hand.
- **Cutoff.** Pages with a publication date before 2020-01-01 were dropped. Undated pages are
  kept, in `undated`.
- **Outliers.** Rows whose dates cannot be trusted as publication dates are moved to
  `outliers` with their date kept and a `date_flag`:
  - `bunched_host`: every dated row of a host with at least half of its dated rows inside
    three consecutive days, or, for a host with under 20 dated rows, 90% on one day. These
    are archives stamped with one date, and hosts whose rows all fall in the last days
    before the crawl ended.
  - `stamped_day`: a host's day with at least 200 rows, at least 20 times that host's
    median day and at least 5 times the average of the 7 days either side of it, unless
    the page URL carries that date. A busy stretch of real news days is not isolated and
    stays dated. These are archive pages stamped with
    a record-update date (project reports, publication lists, case pages).

  In this release: `bunched_host` 81,620 rows from 401 hosts; `stamped_day` 103,604 rows from 30 hosts.

## Uses

Built to detect emerging technologies and trends early, by tracking a term's monthly share of
coverage and how it changes. It also serves retrieval and search over tech press, and training
and evaluating classifiers on the heuristic tags.

## Known limits

- Coverage is a curated host list, not the open web, and monthly volume is uneven. From 2023-07 to 2026-09 the median month has 88,120 articles, the middle half 72,748 to 103,571. 2023-10 to 2025-12 runs at 56k to 104k a month. 2023-07 to 2023-09 are thin (11k to 42k): they sit at the start of the three-year crawl window. 2026 rises from 118k in 2026-01 to 242k in 2026-09, so its 9 months hold 44% of the window. Hosts per month: 456 in 2023-10, 529 in 2026-09.
  The ramp is more pages per host in recent months, not new sources: sites list recent
  pages in their sitemaps far more fully than old ones. Compare a term's share of each
  month's total, not raw counts.
- Hosts join the corpus over time. 67 hosts have their first dated row in 2026 and hold 21% of 2026's rows. 600 hosts have `host_first` at or before 2023-10; they hold 71% of the window. A host that appears in a given month makes
  the terms it covers look as if they start rising then. For trends, keep to hosts present
  across the window with `host_first`, for example `host_first <= '2023-10'`.
- Dates before 2023-07 come from the archives of hosts crawled for the window. They are a
  baseline, not a balanced sample of those years.
- 31% of the rows have no publication date. They are full articles, useful for
  search and retrieval, not for time series.
- Some pages are not articles (listings, tag pages, product pages). `words` and `relevant`
  help filter them.
- On some hosts the same block repeats on every page: a cookie or privacy notice, a
  disclaimer, a subscription pitch or a sidebar, at the start or end of `text`. On 235 hosts
  at least a fifth of the rows share the same opening or closing text, about 1.6 million rows
  in all. A sidebar holds what the site showed when it was fetched, so a term that appears
  only there shows up on every page of that host, whatever its date. Before counting, strip
  the text that most of a host's rows share at the start or end of `text`.
- A few paywalled hosts yield only a lead.
- `relevant`, `topics`, `money` and `deliverables` are heuristic, not labels.

## Rights

- **Article text belongs to its publishers**: `title`, `text`, and the `sentence` fields of
  `money` and `deliverables`.
- **The dataset's own fields** (`url`, `host`, `lang`, `published`, `date_source`, `format`,
  `fetched_at`, `chars`, `words`, `text_sha1`, `relevant`, `topics`, `money.kinds`,
  `money.amount`, `deliverables.trigger`, `date_flag`, `host_first`) are released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
- **Every page was stored from a successful response.** No block, challenge or error page is
  in the set.
