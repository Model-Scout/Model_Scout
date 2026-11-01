---
license: mit
task_categories:
  - tabular-regression
  - time-series-forecasting
  - text-classification
language:
  - en
  - zh
  - es
  - ar
  - hi
  - bn
  - pt
  - ru
  - ja
  - de
  - fr
  - ko
  - tr
  - vi
  - it
tags:
  - ens
  - ethereum
  - web3
  - blockchain
  - domain-names
  - cryptocurrency
  - governance
  - price-prediction
  - trademarks
  - clubs
  - wordlists
  - dictionaries
  - geonames
pretty_name: ENS Appraiser — Multi-source Training Data
size_categories:
  - 100M<n<1B
configs:
  - config_name: discourse_topics
    data_files:
      - split: all
        path: "discourse/*/all_topics.parquet"
      - split: ens
        path: "discourse/*/ens/topics.parquet"
      - split: ethresearch
        path: "discourse/*/ethresearch/topics.parquet"
      - split: optimism
        path: "discourse/*/optimism/topics.parquet"
      - split: arbitrum
        path: "discourse/*/arbitrum/topics.parquet"
      - split: uniswap
        path: "discourse/*/uniswap/topics.parquet"
      - split: aave
        path: "discourse/*/aave/topics.parquet"
      - split: makerdao
        path: "discourse/*/makerdao/topics.parquet"
      - split: compound
        path: "discourse/*/compound/topics.parquet"
      - split: safe
        path: "discourse/*/safe/topics.parquet"
      - split: openzeppelin
        path: "discourse/*/openzeppelin/topics.parquet"
      - split: polkadot
        path: "discourse/*/polkadot/topics.parquet"
      - split: ipfs
        path: "discourse/*/ipfs/topics.parquet"
  - config_name: discourse_posts
    data_files:
      - split: all
        path: "discourse/*/all_posts.parquet"
      - split: ens
        path: "discourse/*/ens/posts.parquet"
      - split: ethresearch
        path: "discourse/*/ethresearch/posts.parquet"
      - split: optimism
        path: "discourse/*/optimism/posts.parquet"
      - split: arbitrum
        path: "discourse/*/arbitrum/posts.parquet"
      - split: uniswap
        path: "discourse/*/uniswap/posts.parquet"
      - split: aave
        path: "discourse/*/aave/posts.parquet"
      - split: makerdao
        path: "discourse/*/makerdao/posts.parquet"
      - split: compound
        path: "discourse/*/compound/posts.parquet"
      - split: safe
        path: "discourse/*/safe/posts.parquet"
      - split: openzeppelin
        path: "discourse/*/openzeppelin/posts.parquet"
      - split: polkadot
        path: "discourse/*/polkadot/posts.parquet"
      - split: ipfs
        path: "discourse/*/ipfs/posts.parquet"
  - config_name: discourse_categories
    data_files:
      - split: all
        path: "discourse/*/all_categories.parquet"
  - config_name: coingecko_ohlc_hourly
    data_files:
      - split: all
        path: "coingecko/*/all_ohlc_hourly.parquet"
      - split: eth
        path: "coingecko/*/eth/ohlc_hourly.parquet"
      - split: ens
        path: "coingecko/*/ens/ohlc_hourly.parquet"
      - split: weth
        path: "coingecko/*/weth/ohlc_hourly.parquet"
      - split: usdc
        path: "coingecko/*/usdc/ohlc_hourly.parquet"
      - split: btc
        path: "coingecko/*/btc/ohlc_hourly.parquet"
  - config_name: market_regime
    data_files:
      - split: fear_greed
        path: "market_regime/*/fear_greed_partial.parquet"
      - split: eth_tvl
        path: "market_regime/*/ethereum_tvl_partial.parquet"
      - split: stables_eth
        path: "market_regime/*/stablecoins_ethereum_partial.parquet"
      - split: stables_all
        path: "market_regime/*/stablecoins_all_partial.parquet"
  - config_name: trademarks
    data_files:
      - split: uspto_case_files
        path: "trademarks/*/uspto_case_files_partial.parquet"
      - split: uspto_intl_classes
        path: "trademarks/*/uspto_intl_classes_partial.parquet"
      - split: uspto_statements
        path: "trademarks/*/uspto_statements_partial.parquet"
      - split: uspto_events
        path: "trademarks/*/uspto_events_partial.parquet"
  - config_name: clubs
    data_files:
      - split: grails
        path: "clubs/*/grails_clubs_partial.parquet"
  - config_name: wordlists
    data_files:
      - split: wikipedia_titles
        path: "wordlists/*/wikipedia_titles_partial.parquet"
      - split: geonames_cities
        path: "wordlists/*/geonames_cities_partial.parquet"
      - split: us_firstnames
        path: "wordlists/*/us_census_firstnames_partial.parquet"
      - split: us_surnames
        path: "wordlists/*/us_census_surnames_partial.parquet"
      - split: iso3166_countries
        path: "wordlists/*/iso3166_countries_partial.parquet"
      - split: stock_tickers
        path: "wordlists/*/stock_tickers_partial.parquet"
      - split: sec_edgar_companies
        path: "wordlists/*/sec_edgar_companies_partial.parquet"
      - split: wiktionary_en
        path: "wordlists/*/wiktionary_en_partial.parquet"
      - split: wiktionary_zh
        path: "wordlists/*/wiktionary_zh_partial.parquet"
      - split: wiktionary_es
        path: "wordlists/*/wiktionary_es_partial.parquet"
      - split: wiktionary_ar
        path: "wordlists/*/wiktionary_ar_partial.parquet"
      - split: wiktionary_hi
        path: "wordlists/*/wiktionary_hi_partial.parquet"
      - split: wiktionary_bn
        path: "wordlists/*/wiktionary_bn_partial.parquet"
      - split: wiktionary_pt
        path: "wordlists/*/wiktionary_pt_partial.parquet"
      - split: wiktionary_ru
        path: "wordlists/*/wiktionary_ru_partial.parquet"
      - split: wiktionary_ja
        path: "wordlists/*/wiktionary_ja_partial.parquet"
      - split: wiktionary_de
        path: "wordlists/*/wiktionary_de_partial.parquet"
      - split: wiktionary_fr
        path: "wordlists/*/wiktionary_fr_partial.parquet"
      - split: wiktionary_ko
        path: "wordlists/*/wiktionary_ko_partial.parquet"
      - split: wiktionary_tr
        path: "wordlists/*/wiktionary_tr_partial.parquet"
      - split: wiktionary_vi
        path: "wordlists/*/wiktionary_vi_partial.parquet"
      - split: wiktionary_it
        path: "wordlists/*/wiktionary_it_partial.parquet"
  - config_name: onchain
    data_files:
      - split: registrations
        path: "onchain/*/ens_registrations_partial.parquet"
      - split: renewals
        path: "onchain/*/ens_renewals_partial.parquet"
      - split: transfers
        path: "onchain/*/ens_transfers_partial.parquet"
      - split: sales
        path: "onchain/*/ens_sales_partial.parquet"
---

# ENS Appraiser — Multi-source Training Data

A versioned, multi-source dataset assembling the inputs needed to train an ML
appraiser for ENS (`.eth`) domain names. The core prediction problem is
**given a name, predict its market value**, which requires composing several
signal types that no single existing dataset provides.

## Sources

| Source | What it provides | Status |
|---|---|---|
| **Discourse forums** | Governance and research signal — what protocol-level changes are being debated *before* they ship | ✅ Live |
| **CoinGecko hourly OHLC** | Per-hour ETH/ENS/WETH/USDC/BTC USD prices for label denomination and market regime features | ✅ Live |
| **Market regime** | Daily macro-crypto signals: Fear & Greed Index, Ethereum DeFi TVL, stablecoin supply | ✅ Live (partial — accumulating siblings as we add more) |
| **Trademarks (USPTO)** | US trademark registry — mark text, Nice classes, goods/services descriptions, prosecution events. Used to flag ENS names that conflict with active trademarks | ✅ Live (USPTO complete; EUIPO planned) |
| **Clubs (Grails)** | Hand-curated `.eth` name club lists from the [grailsmarket/ens-categories](https://github.com/grailsmarket/ens-categories) repo. Used for clustering, filtering, and result-time tag UX. | ✅ Live |
| **Wordlists** | Multilingual Wiktionary dumps (15 languages), Wikipedia titles, GeoNames cities, US first/last names, ISO 3166, stock tickers, SEC EDGAR companies. Used to test "is this name a real word / city / first name / brand / ticker?" — the feature density of wordlist matches correlates with ENS market value. | ✅ Live |
| **On-chain registrations, renewals, transfers, sales** | Training labels (sale prices) and conviction features (registration history, lifecycle events). Sourced from The Graph's ENS subgraph + Alchemy NFT API. | ✅ Live |
| **Reddit cultural momentum** | Slang/meme/cultural term tracking from a curated subreddit list | 🔜 Planned |
| **Grails platform attention** | Buyer attention (views, watchlist, votes) and Google Ads CPC per name | 🔜 Planned |

## Versioning

Every scrape produces a date-stamped subfolder. The configs in this card use
glob patterns (`discourse/*/`, `coingecko/*/`, `market_regime/*/`, `trademarks/*/`,
`clubs/*/`, `wordlists/*/`, `onchain/*/`) so the viewer always shows the union
of all snapshots.

For reproducible training, **pin to a specific commit SHA** rather than relying
on `main`:

```python
import duckdb
con = duckdb.connect()
con.execute("INSTALL httpfs; LOAD httpfs;")
con.execute("CREATE SECRET hf (TYPE HUGGINGFACE, TOKEN '$HF_TOKEN');")
con.sql("""
  SELECT *
  FROM 'hf://datasets/quantumly/ens-appraiser-data@<commit-sha>/discourse/2026-04-25/all_topics.parquet'
""")
```

## Schemas

### `discourse_topics`

| Column | Type | Notes |
|---|---|---|
| `forum` | string | Forum slug (`ens`, `ethresearch`, ...) |
| `topic_id` | int64 | Discourse topic ID, unique within a forum |
| `slug` | string | URL slug |
| `title` | string | Topic title |
| `created_at` | timestamp[UTC] | When the topic was first posted |
| `last_posted_at` | timestamp[UTC] | Most recent post in the thread |
| `bumped_at` | timestamp[UTC] | Last activity (post, edit, etc.) |
| `posts_count` | int32 | Total posts in the thread |
| `views` | int64 | View count |
| `like_count` | int32 | Aggregate likes |
| `category_id` | int32 | Joins to `discourse_categories` |
| `tags` | list&lt;string&gt; | Discourse tags (sparse on most forums) |
| `pinned`, `closed`, `archived`, `visible` | bool | Topic state flags |
| `has_accepted_answer` | bool | Some forums use Discourse's Q&A plugin |

### `discourse_posts`

| Column | Type | Notes |
|---|---|---|
| `forum` | string | Forum slug |
| `topic_id` | int64 | Joins to `discourse_topics` |
| `post_id` | int64 | Discourse post ID |
| `post_number` | int32 | 1 = original post, 2+ = replies |
| `username`, `user_id` | string, int64 | Author |
| `created_at`, `updated_at` | timestamp[UTC] | |
| `cooked` | string | HTML-rendered body (always present) |
| `raw` | string | Markdown source (forum-dependent — not always exposed) |
| `reply_to_post_number` | int32 | For thread reconstruction |
| `score`, `reads`, `readers_count` | float/int | Engagement metrics |
| `incoming_link_count`, `quote_count` | int32 | Cross-thread reference counts |
| `trust_level` | int32 | Discourse user trust level (0-4) |

### `coingecko_ohlc_hourly`

| Column | Type | Notes |
|---|---|---|
| `coin_slug` | string | `eth`, `ens`, `weth`, `usdc`, `btc` |
| `ts_ms` | int64 | Candle close time in epoch milliseconds |
| `ts` | timestamp[UTC] | Same time as a parsed datetime |
| `open`, `high`, `low`, `close` | float64 | OHLC in USD |

Note: WETH and USDC have a small number of zero-close rows in early thinly-traded
periods (2018-2019). These are CoinGecko data-quality glitches representing
"no observed trades" rather than real prices. Use `COALESCE(weth.close, eth.close)`
for label denomination.

### `market_regime`

A growing collection of daily macro-crypto signals, each shipped as a separate
`_partial.parquet` file under a single `market_regime/<run_date>/` folder so
they can be added incrementally without schema migrations. The four splits all
key on a daily UTC `date` column and join cleanly to sales data via
`DATE_TRUNC('day', sales.sold_at)`.

**Split: `fear_greed`** — sourced from alternative.me. Daily values from 2018-02-01.

| Column | Type | Notes |
|---|---|---|
| `date` | timestamp[UTC, day-truncated] | Join key |
| `value` | int32 | Sentiment score 0–100 (0 = extreme fear, 100 = extreme greed) |
| `classification` | string | `Extreme Fear`, `Fear`, `Neutral`, `Greed`, `Extreme Greed` |
| `ts_unix` | int64 | Original epoch seconds (kept for reproducibility) |

**Split: `eth_tvl`** — sourced from DefiLlama (`api.llama.fi/v2/historicalChainTvl/Ethereum`). Daily Ethereum DeFi TVL.

| Column | Type | Notes |
|---|---|---|
| `date` | timestamp[UTC, day-truncated] | Join key |
| `tvl_usd` | float64 | Total value locked across DeFi protocols on Ethereum, in USD |
| `ts_unix` | int64 | Original epoch seconds |

**Split: `stables_eth`** — sourced from DefiLlama (`stablecoins.llama.fi/stablecoincharts/Ethereum`). Daily total stablecoin supply on Ethereum.

| Column | Type | Notes |
|---|---|---|
| `date` | timestamp[UTC, day-truncated] | Join key |
| `circulating_usd` | float64 | Total USD-pegged stablecoin supply on Ethereum |
| `ts_unix` | int64 | Original epoch seconds |

**Split: `stables_all`** — sourced from DefiLlama (`stablecoins.llama.fi/stablecoincharts/all`). Daily total stablecoin market cap across all chains.

| Column | Type | Notes |
|---|---|---|
| `date` | timestamp[UTC, day-truncated] | Join key |
| `circulating_usd` | float64 | Total USD-pegged stablecoin supply across all tracked chains |
| `ts_unix` | int64 | Original epoch seconds |

DefiLlama excludes liquid staking and double-counted TVL by default; chain-staking
(e.g. ETH PoS) is also not included. See https://docs.llama.fi for methodology.

### `trademarks`

Sourced from the **USPTO Trademark Case Files Dataset** — a pre-aggregated
research dataset published annually by the USPTO Office of Chief Economist
covering ~12.7 million trademark applications and registrations from October
1870 → March 2024. All four splits join on `serial_no` (USPTO's primary key
per trademark record).

The data is saved raw (no acquisition-time filtering by mark type, status, or
ENS-pattern match). Filter at training time per use case. Mark text is also
exposed via the `mark_text_norm` column (lowercase, stripped) for direct
joins to ENS labels.

EUIPO equivalent (EU trademark registry) is planned but blocked on EUIPO's
sandbox account requirement; will land as additional `euipo_*` splits in this
config.

**Split: `uspto_case_files`** — one row per trademark.

| Column | Type | Notes |
|---|---|---|
| `serial_no` | string | USPTO serial number — primary key, joins to other splits |
| `mark_id_char` | string | Original mark text as filed |
| `mark_text_norm` | string | Lowercase, whitespace-stripped — useful join key vs. ENS labels |
| `mark_draw_cd` | string | 4-digit code; leading digit indicates type (1xxx=word, 3xxx=word+design, 4xxx=standard chars, 5xxx=stylized) |
| `filing_dt`, `registration_dt`, `abandon_dt`, `reg_cancel_dt` | string | Date strings (YYYYMMDD format) |
| `cfh_status_cd`, `cfh_status_dt` | string | Current status code and date |
| `registration_no` | string | Registration number (null if not registered) |
| `publication_dt`, `renewal_dt` | string | Publication for opposition / most recent renewal |
| `trade_mark_in`, `serv_mark_in`, `std_char_claim_in` | int64 | Boolean flags (0/1) |

**Split: `uspto_intl_classes`** — Nice classification (one row per (mark, class) pair).

| Column | Type | Notes |
|---|---|---|
| `serial_no` | string | Joins to uspto_case_files |
| `class_id` | int64 | Internal class record ID |
| `intl_class_cd` | string | Nice classification code 001–045 (zero-padded) |

**Split: `uspto_statements`** — goods/services descriptions and other free-text statements.

| Column | Type | Notes |
|---|---|---|
| `serial_no` | string | Joins to uspto_case_files |
| `statement_type_cd` | string | Statement type (GS = goods/services, DM = description of mark, etc.) |
| `statement_text` | string | Free-text content. For trademark conflict analysis, the `GS*` types are most useful — they describe what each mark *actually covers* in plain language ("blockchain-based digital wallets" vs. "stuffed toys") |

**Split: `uspto_events`** — full prosecution timeline (one row per event per trademark).

| Column | Type | Notes |
|---|---|---|
| `serial_no` | string | Joins to uspto_case_files |
| `event_cd` | string | 4-character prosecution event code |
| `event_dt` | string | Date of event (YYYYMMDD format) |
| `event_seq` | int64 | Sequence number within event type |
| `event_type_cd` | string | Event category (A = application, P = post-publication, R = registration, etc.) |

Total events is ~209M rows. This is the largest split in the dataset by row
count; use DuckDB or polars streaming for queries — don't `pl.read_parquet`
into memory.

The Nice classification crosswalk for trademark conflict analysis: classes
**9 (computer software), 35 (advertising), 36 (financial services),
38 (telecommunications), 41 (entertainment), 42 (computer services),
45 (legal/identity)** are the highest-relevance classes for crypto / web3 /
digital identity.

### `clubs`

Hand-curated `.eth` name club lists. "Clubs" terminology matches the grails
marketplace API (their `/api/v1/clubs` endpoint) — each club is a curated set
of `.eth` names that share some property (semantic, structural, or historical).

Examples of clubs in the source data: `un_cities`, `bip_39` (the Bitcoin
BIP39 wordlist), `english_adjectives`, `gamertags`, `ethmoji_keycaps`,
`periodic_table_natural`, `prepunks-100-1k-10k` (names registered before
CryptoPunks launched), `wikidata_top_fantasy_char`, `pokemon_gen1` through
`pokemon_gen4`, `firstnames_usa`, `top500_cities_global`, `crypto_terms`,
`paranormal`, `mythical_creatures`, etc.

Each scrape captures the exact source repo commit SHA in a sibling
`grails_clubs_metadata.json` file for reproducibility.

**Split: `grails`** — long format, one row per (name, club, source_path) tuple.

| Column | Type | Notes |
|---|---|---|
| `name` | string | ENS label, normalized (lowercase, no `.eth` suffix) |
| `club` | string | Cleaned thematic club name (e.g., `top_crypto_tickers`, `paranormal`). Acquisition-date prefixes from the source repo (`jan5`, `12feb`, etc.) have been stripped — see `scrape_date` for the date and `source_path` for the original location. |
| `source_path` | string | Original full path in the grails source repo. Provenance + audit trail. |
| `scrape_date` | string | ISO date (YYYY-MM-DD) parsed from the source folder name when applicable (e.g., `jan5/foo.csv` → `2025-01-05`). Null for clubs that aren't in date-prefixed folders. |
| `extra_fields` | string | JSON-encoded extra columns from CSV-formatted source files (null if line-per-name). For `prepunk_full_rankings` this typically contains rank/position metadata; for the `_root` rows it contains hash columns (labelhash + namehash) for direct on-chain joins. |

A single name appears multiple times if it's in multiple clubs. This is
intentional — multi-club names tend to be the most desirable ENS names
(a name that's both an English word AND a common first name AND a brand
name has overlapping appeal). In the current scrape, names like `silver`,
`gold`, `blue`, `green` appear in 15+ clubs each.

To pivot to wide-format (one boolean column per club):

```sql
PIVOT 'hf://datasets/quantumly/ens-appraiser-data/clubs/*/grails_clubs_partial.parquet'
ON club USING bool_or(true) GROUP BY name
```

To extract structured fields from `extra_fields`:

```sql
-- prepunk rankings are in extra_fields
SELECT
  name,
  json_extract_string(extra_fields, '$.rank') AS rank,
  json_extract_string(extra_fields, '$.labelhash') AS labelhash,
  json_extract_string(extra_fields, '$.namehash') AS namehash
FROM 'hf://datasets/quantumly/ens-appraiser-data/clubs/*/grails_clubs_partial.parquet'
WHERE extra_fields IS NOT NULL
```

### `wordlists`

A collection of word/name lookup tables from public sources. Each split is
a *lookup table*: one row per word, plus columns describing what we know
about that word (population, gender, exchange, etc.).

At training time the appraiser asks "is this ENS label in `wiktionary_en`?
in `geonames_cities`? in `us_firstnames`?" Each answer becomes a boolean
feature. Names that match many wordlists tend to be more valuable than
names that match none. A name like `tokyo` matches both Wiktionary EN AND
GeoNames; `nike` matches Wiktionary EN AND SEC EDGAR; `vitalik` matches
nothing in this corpus (its value derives from celebrity rather than
generic wordlist coverage).

Coverage: ~17M Wiktionary entries across 15 languages, ~18M Wikipedia EN
titles, ~146k GeoNames cities, ~7k US first names with gender, ~13k stock
tickers, ~11k SEC EDGAR companies, ~417 ISO 3166 countries.

All splits share a `word` primary column — lowercase, whitespace-stripped,
multi-word phrases excluded so it can be used as a direct join key against
ENS labels.

**Splits: `wiktionary_<lang>`** (15 languages: `en`, `zh`, `es`, `ar`, `hi`,
`bn`, `pt`, `ru`, `ja`, `de`, `fr`, `ko`, `tr`, `vi`, `it`)

| Column | Type | Notes |
|---|---|---|
| `word` | string | Wiktionary page title, normalized |
| `lang` | string | ISO 639 code matching the split |

Wiktionary redirects are skipped (they're spelling variants pointing to
canonical forms — adds noise without much value). Multi-word phrases are
also skipped because ENS labels can't contain whitespace.

**Split: `wikipedia_titles`**

| Column | Type | Notes |
|---|---|---|
| `word` | string | Wikipedia EN article title (main namespace), normalized |

~18M entries. The largest single parquet (~213 MB). Includes places, people,
events, brands, art, technology, etc. Title-only — full article content is
not included.

**Split: `geonames_cities`** — sourced from [GeoNames](https://www.geonames.org/) `cities500.zip` (populated places with population > 500).

| Column | Type | Notes |
|---|---|---|
| `word` | string | City ASCII name, normalized |
| `country` | string | ISO 3166-1 alpha-2 country code |
| `population` | int64 | Population at last census update |

**Split: `us_firstnames`** — sourced from a [GitHub mirror](https://github.com/hadley/data-baby-names) of the SSA baby names dataset (1880-2008). Direct SSA download is blocked at the Akamai edge for non-browser clients; this mirror is the same underlying SSA data.

| Column | Type | Notes |
|---|---|---|
| `word` | string | First name, normalized |
| `score_male` | float64 | Cumulative percent across all years registered as male |
| `score_female` | float64 | Cumulative percent across all years registered as female |
| `score_total` | float64 | Sum of male + female scores (overall popularity proxy) |
| `primary_gender` | string | `M`, `F`, or `U` (unisex — equal counts) |

**Split: `us_surnames`** — when present, sourced from a community mirror of the 2010 Census surnames data. Best-effort: this split is conditionally populated. Check for file presence before joining.

| Column | Type | Notes |
|---|---|---|
| `word` | string | Surname, normalized |
| `rank` | int64 | National frequency rank (1 = most common) |
| `count` | int64 | Number of occurrences in the 2010 Census |

**Split: `iso3166_countries`** — sourced from the [datasets/country-list](https://github.com/datasets/country-list) repository.

| Column | Type | Notes |
|---|---|---|
| `word` | string | Country name OR ISO code (both forms ingested) |
| `iso_code` | string | ISO 3166-1 alpha-2 code |
| `kind` | string | `name` if the row is a country name, `code` if it's the ISO code |

**Split: `stock_tickers`** — sourced from NASDAQ Trader's daily ticker dumps (`nasdaqlisted.txt` and `otherlisted.txt`).

| Column | Type | Notes |
|---|---|---|
| `word` | string | Ticker symbol, normalized |
| `exchange` | string | `NASDAQ` or `NYSE/AMEX` |
| `company_name` | string | Issuer name as listed |

**Split: `sec_edgar_companies`** — sourced from `https://www.sec.gov/files/company_tickers.json`.

| Column | Type | Notes |
|---|---|---|
| `word` | string | Company name (first comma-segment) OR ticker, normalized |
| `ticker` | string | Stock ticker symbol |
| `cik` | string | SEC CIK number — primary key in EDGAR |
| `kind` | string | `company_name` or `ticker` |

To compute "wordlist hit count" for an ENS label across all wordlists:

```sql
-- DuckDB UNION-based hit count per name
WITH all_words AS (
  SELECT word, 'wiktionary_en' AS source FROM 'hf://.../wordlists/*/wiktionary_en_partial.parquet'
  UNION ALL SELECT word, 'wiktionary_de' FROM 'hf://.../wordlists/*/wiktionary_de_partial.parquet'
  UNION ALL SELECT word, 'geonames' FROM 'hf://.../wordlists/*/geonames_cities_partial.parquet'
  UNION ALL SELECT word, 'us_firstnames' FROM 'hf://.../wordlists/*/us_census_firstnames_partial.parquet'
  -- ... add other splits as needed
)
SELECT word, COUNT(DISTINCT source) AS n_hits
FROM all_words
WHERE word IN ('apple', 'tokyo', 'vitalik')
GROUP BY word
```

### `onchain`

ENS on-chain data: registrations, renewals, transfers, and secondary sales.
Split sourcing:

- **Registrations, renewals, transfers**: The Graph's [ENS subgraph](https://thegraph.com/explorer/subgraphs/5XqPmWe6gjyrJtFn9cLy237i4cWw2j9HcUJEXsP5qGtH)
  on the decentralized network. The subgraph is maintained by ENS Labs and
  indexes both the BaseRegistrar (ERC-721) and NameWrapper (ERC-1155)
  contracts. Free tier on The Graph allows 100k queries/month, which is more
  than enough for a full backfill (~5,000 paginated queries).
- **Sales**: Alchemy's [`getNFTSales`](https://docs.alchemy.com/reference/getnftsales)
  endpoint. Aggregates marketplace fills across OpenSea (Seaport + legacy
  Wyvern), Blur, X2Y2, LooksRare, and CryptoPunks. Filtered to the two ENS
  contract addresses (BaseRegistrar `0x57f1887a8...` and NameWrapper
  `0xd4416b13d...`). Free tier 300 CU/sec, 100M CU/month.

Why not Dune: Dune's free tier charges 20 credits/MB on API exports, and
their UI CSV download is paywalled at the $399/mo Plus tier. Even with paid
plans the API export pricing makes large result sets prohibitive (we
exceeded the free tier in a single sales export attempt). The Graph + Alchemy
combo is fully free for our query volumes.

**Split: `registrations`** — every ENS first-time registration event.

| Column | Type | Notes |
|---|---|---|
| `registration_id` | string | Subgraph entity ID, primary key. Format: `<labelhash>` |
| `label` | string | ENS label (e.g., `vitalik`), no `.eth` suffix. Direct join key vs other configs. |
| `labelhash` | string | bytes32 hash of the label (`0x...`). Direct join key vs `transfers.token_id` (which is `tokenId = uint256(labelhash)` for BaseRegistrar) |
| `registrant` | string | Initial registrant address (`0x...`) |
| `registered_unix` | int64 | Registration timestamp, epoch seconds |
| `expires_unix` | int64 | Expiry timestamp, epoch seconds |
| `cost` | string | Wei paid at registration (string to avoid uint256 overflow). Includes the base annual fee, not the premium. |

Every name registered through any ETHRegistrarController version (v1–v5) ends
up here — the subgraph normalizes across controller versions. Names registered
directly via the BaseRegistrar (without going through a controller) won't
appear; this is rare and only relevant for very early ENS history.

**Split: `renewals`** — every renewal event (when an existing owner extends
their registration).

| Column | Type | Notes |
|---|---|---|
| `renewal_id` | string | Subgraph entity ID, primary key |
| `label` | string | ENS label, lowercase, no `.eth` suffix |
| `labelhash` | string | bytes32 hash of the label |
| `cost` | string | Wei paid for the renewal (string to avoid overflow) |
| `new_expires_unix` | int64 | New expiry timestamp after the renewal, epoch seconds |
| `blockNumber` | int64 | Ethereum block number |
| `transactionID` | string | Transaction hash |

Renewals are useful as a *conviction signal* — a name that's been renewed
multiple times is more likely valuable to its owner than one held to expiry.
This is one of the strongest behavioral features for predicting future sale price.

**Split: `transfers`** — every NameWrapper ownership transfer.

| Column | Type | Notes |
|---|---|---|
| `transfer_id` | string | Subgraph entity ID, primary key |
| `label` | string | ENS label, lowercase, no `.eth` suffix |
| `labelhash` | string | bytes32 hash of the label |
| `new_owner` | string | Receiving address (`0x...`) |
| `blockNumber` | int64 | Ethereum block number |
| `transactionID` | string | Transaction hash |

Note: this is **NameWrapper-only** transfers via the subgraph's `wrappedTransfers`
collection. Pre-NameWrapper-era BaseRegistrar transfers are not in this split
— for those, join `sales` by `contract_type='base_registrar'`. Free transfers
(non-sale) on the BaseRegistrar before NameWrapper adoption (March 2023) are
not currently captured in this dataset; if needed, they can be sourced
separately from `erc721_ethereum.evt_Transfer` style data.

**Split: `sales`** — secondary-market sale events with prices.

| Column | Type | Notes |
|---|---|---|
| `tx_hash` | string | Ethereum transaction hash |
| `log_index` | int64 | Log index within the transaction |
| `bundle_index` | int64 | Index within a bundled sale (0 = single-item, > 0 = multi-item bundle) |
| `block_number` | int64 | Ethereum block number |
| `marketplace` | string | One of `seaport`, `wyvern`, `looksrare`, `x2y2`, `blur`, `cryptopunks` |
| `contract_type` | string | `base_registrar` (ERC-721, pre-wrap) or `name_wrapper` (ERC-1155, post-wrap) |
| `contract_address` | string | NFT contract address |
| `token_id` | string | Decimal uint256 string. For BaseRegistrar, this equals `uint256(labelhash)` and can be converted to `labelhash` via `'0x' || lpad(to_hex(token_id::HUGEINT), 64, '0')`. For NameWrapper, `token_id` is a *namehash*, not a labelhash. |
| `quantity` | string | Always `1` for ERC-721; potentially > 1 for ERC-1155 (rare for ENS) |
| `buyer_address`, `seller_address` | string | Counterparty addresses |
| `taker` | string | `BUYER` or `SELLER` — which side initiated the trade (i.e., accepted the order) |
| `seller_fee_wei` | string | Amount paid to the seller, in raw token units (string to avoid uint256 overflow) |
| `seller_fee_symbol` | string | `ETH`, `WETH`, `USDC`, etc. |
| `seller_fee_decimals` | int64 | Token decimals (18 for ETH/WETH, 6 for USDC) |
| `protocol_fee_wei`, `protocol_fee_symbol` | string | Marketplace fee |
| `royalty_fee_wei`, `royalty_fee_symbol` | string | Creator royalty (ENS doesn't enforce royalties, often null/0) |

Important schema notes:

- **No USD column.** Alchemy returns wei-denominated amounts only. To compute
  USD prices, join to `coingecko_ohlc_hourly` on the appropriate symbol +
  hour-truncated timestamp:

  ```sql
  SELECT
    s.tx_hash,
    s.label,
    s.seller_fee_wei,
    s.seller_fee_symbol,
    (s.seller_fee_wei::HUGEINT / POW(10, s.seller_fee_decimals)) * c.close AS amount_usd
  FROM onchain_sales s
  JOIN coingecko_ohlc_hourly c
    ON c.coin_slug = lower(s.seller_fee_symbol)  -- 'eth', 'weth', 'usdc'
    AND c.ts = date_trunc('hour', to_timestamp(s.block_timestamp))
  ```

- **Total sale price = `seller_fee + protocol_fee + royalty_fee`** (all in
  the same currency). The seller only receives `seller_fee`; the buyer paid
  the sum. For training labels (predicting "what would this name sell for?"),
  use the sum.

- **Bundled sales appear as multiple rows with the same `tx_hash`** but
  different `bundle_index`. To dedupe to per-name: each row is already a
  single (token_id, tx_hash) pair — the bundling is just metadata.

- **`token_id` ↔ `labelhash` join:** For `contract_type='base_registrar'`
  rows, `token_id` is the decimal representation of the label's keccak256
  hash, so it joins to `registrations.labelhash` after a hex conversion:

  ```sql
  -- BaseRegistrar sales joined to registrations
  SELECT s.*, r.label, r.registered_unix
  FROM onchain_sales s
  JOIN onchain_registrations r
    ON r.labelhash = '0x' || lpad(to_hex(s.token_id::HUGEINT), 64, '0')
  WHERE s.contract_type = 'base_registrar'
  ```

  For `contract_type='name_wrapper'` rows, `token_id` is a *namehash* (the
  recursive hash including parent domains), not a labelhash. NameWrapper
  joins require keeping a separate (label, namehash) lookup, which the
  subgraph's `domain` entity provides.

## Coverage

As of the latest scrape:

**Discourse** (12 forums): ~135k posts across ~43k topics. ENS gov has 2,513 topics
since 2021; OpenZeppelin has 10,571 topics going back to 2018.

**CoinGecko**: ~320k hourly OHLC rows, 5 coins. ETH/BTC/WETH cover Feb 2018 →
present (~71k rows each). ENS the token covers Nov 2021 → present (~39k rows).

**Market regime**: ~3k daily F&G rows since Feb 2018; ~1.8k daily ETH-TVL rows
since 2020; ~1.5k daily stablecoin rows since 2021. Together these form a
4-feature daily-resolution macro context table.

**Trademarks (USPTO)**: ~12.7M case files, ~15M (mark × class) pairs,
~26M statements, ~209M prosecution events. Coverage from October 1870 to
March 2024 (the USPTO 2023 annual release).

**Clubs (Grails)**: ~261k (name, club) pairs across 45 clubs, ~211k unique
names. See the per-scrape `grails_clubs_metadata.json` sidecar for the
exact club count, per-club row counts, and source repo commit SHA.

**Wordlists**: 15 Wiktionary languages totalling ~17M dictionary entries
(largest: en 8.2M, zh 2.5M, ru 1.4M, tr 1.1M, de 1.1M); ~18M Wikipedia EN
titles; ~146k GeoNames populated places (population > 500); ~6.7k US first
names with gender; ~12.5k NYSE/NASDAQ tickers; ~10.9k SEC EDGAR companies;
~417 ISO 3166 country names+codes. Total ~135 MB on disk.

**On-chain**: ~3.8M registrations since the BaseRegistrar deployment
(May 2019); ~1M renewals; ~5M NameWrapper transfers since the wrapper
launched (March 2023); ~500k secondary sales across OpenSea Seaport/Wyvern,
Blur, X2Y2, LooksRare. The exact counts per scrape are in the sidecar
`thegraph_metadata.json`.

## Data quality notes

- **Time-as-of-snapshot:** every dataset is keyed on a timestamp that represents
  when the event occurred, NOT when it was scraped. Training pipelines should
  filter to "data available *as of* the prediction time" to avoid leakage.
- **Discourse `cooked` is HTML.** Strip tags before NLP. `raw` (markdown) is more
  convenient but not always present.
- **CoinGecko hourly only goes back to Feb 9, 2018.** For sales before that, fall
  back to daily candles (a separate scrape, not yet included).
- **Market regime is `_partial`-suffixed** because it accumulates siblings over
  time. Each `_partial.parquet` is independently versioned; future additions
  (e.g. ETH staking ratio, derivatives open interest) will land in the same
  folder without schema migrations.
- **USPTO mark drawing codes are 4-digit, not single-digit.** Codes like `1000`,
  `4000`, `5000` are the standard buckets; values like `5W20` or `2X20` appear
  in the long tail and are likely USPTO data-keying artifacts. To filter "word
  marks only" use `mark_draw_cd LIKE '1%' OR mark_draw_cd LIKE '4%'`.
- **USPTO has ~1.4M case files with null `mark_id_char`.** These are mostly
  pre-digital-era records where mark text wasn't OCR'd. They're useless for
  string-match joins but kept in the dataset per the "save raw" principle.
- **USPTO `uspto_events` is large (~209M rows).** Use DuckDB/polars streaming
  or filter to specific `serial_no` values before loading. Don't try to
  `read_parquet` the full split into memory.
- **Clubs `data_dump` is the largest club** (~152k rows in the latest scrape,
  roughly 60% of all club rows) but is **not a thematic category** — it's
  grails' bulk name pool, names of interest that haven't been bucketed yet.
  For thematic features (e.g., "is this a paranormal-themed name?"), filter
  `club != 'data_dump'`. For "is this name on grails' radar at all,"
  `data_dump` membership is itself a signal.
- **Clubs `_root` and `_dated_root` rows** are catch-alls for files that didn't
  land in a category folder. `_root` is the repo root, `_dated_root` is files
  that were directly in a date folder (e.g., `jan5/some_file.csv` with no
  sub-folder). Usually metadata about other clubs rather than name lists
  themselves. Check `extra_fields` and `source_path` to interpret.
- **Clubs date prefixes have been stripped** from the `club` column; the
  underlying date is preserved in `scrape_date` and the original full path
  in `source_path`. So a file at `jan5/top_crypto_tickers/list.txt` becomes
  `club='top_crypto_tickers'`, `scrape_date='2025-01-05'`,
  `source_path='jan5/top_crypto_tickers/list.txt'`.
- **Wiktionary inflated counts.** Wiktionary EN includes inflections, conjugations,
  and translations of words from many languages; ~95% of "words" in the EN
  Wiktionary aren't English in any meaningful sense. Same for fr (heavy
  conjugation coverage) and ru (many redirects skipped reduce this somewhat —
  ru had ~1M redirects skipped vs ~1.4M kept). For "is this an English word
  used by English speakers?" use Wiktionary EN as a coarse signal and
  layer Wikipedia EN titles + frequency lists for refinement.
- **Wiktionary `is_redirect` skipped.** Redirects (spelling variants pointing
  to canonical forms) are filtered out at acquisition time. Trade-off:
  loses some legitimate alternate spellings but removes a lot of noise.
- **`us_firstnames` is from a 2008-era mirror.** Direct SSA download
  (`ssa.gov/oact/babynames/names.zip`) is blocked at the Akamai edge for
  non-browser HTTP clients. We use the
  [hadley/data-baby-names](https://github.com/hadley/data-baby-names) GitHub
  mirror which covers 1880-2008 (~6.7k unique names). Misses 2009-present
  trends like `Aydenn`, `Brielynn`, etc., but covers ~99% of names anyone
  would actually encounter as an ENS label.
- **`us_surnames` may not always be present.** The 2010 Census surnames file
  is on `www2.census.gov` which is also Akamai-fronted and intermittently
  blocks scrapers. The notebook attempts a community mirror but doesn't
  fail the run if surnames can't be fetched. Check for split presence
  before joining.
- **Wordlist `word` column is normalized for ENS matching** — lowercased,
  whitespace stripped, multi-word phrases removed, no `.eth` suffix. Direct
  string equality joins against ENS labels work without further
  preprocessing.
- **On-chain sales lack USD prices.** Alchemy's `getNFTSales` returns wei
  amounts and currency symbols only. Join to `coingecko_ohlc_hourly` at
  hour resolution to compute USD prices for training labels.
- **On-chain sales total = sum of three fees.** `seller_fee + protocol_fee +
  royalty_fee` equals what the buyer paid; `seller_fee` alone is what the
  seller received. Use the sum as the price label.
- **On-chain transfers are NameWrapper-only via the subgraph.** Pre-wrapper
  BaseRegistrar transfers are not in `onchain_transfers`. Sales (which include
  pre-wrapper sales) cover this gap for ownership-change-with-payment events;
  free transfers on BaseRegistrar before March 2023 are not in this dataset.
- **`token_id` overflow risk.** Both registrations' `cost` and sales'
  `token_id` are uint256 values stored as strings. Cast to `HUGEINT` (DuckDB)
  or use Python's native int when manipulating; do not cast to `BIGINT` or
  `INT64` (will overflow silently).

## Intended use

This dataset is the input layer for a value-prediction model on ENS names.
Specifically:

- Sale prices (from the `onchain` config's `sales` split) provide labels
- All other sources provide features
- Time-aligned features prevent label leakage

Out of scope: this is a research dataset, not a production price oracle. Do not
use predicted prices for live trading without independent validation.

## Licensing & attribution

The aggregated and processed data in this dataset is released under the **MIT
License**. Individual sources retain their original terms:

- **Discourse forums:** Each forum's posts remain under that forum's terms of use.
  Most are public-readable; check the source forum for redistribution rules.
- **CoinGecko data:** Per CoinGecko's API terms, displays must include
  "Data provided by CoinGecko" with a link to https://www.coingecko.com/en/api.
- **DefiLlama data:** Citing DefiLlama as the source is appreciated though not
  strictly required per their FAQ. Link: https://defillama.com.
- **Fear & Greed Index:** Provided by alternative.me; free for any use including
  commercial. A "Data from alternative.me" reference is appreciated.
- **USPTO Trademark Case Files:** US Government work, public domain. Cite as:
  Graham, Stuart J.H., Marco, Alan C., Miller, Richard (2018). The USPTO
  Trademark Case Files Dataset. *Journal of Economics & Management Strategy*
  22(4), pp. 669–705.
- **Grails clubs:** Source repo [grailsmarket/ens-categories](https://github.com/grailsmarket/ens-categories)
  is MIT-licensed. Each scrape pins an exact commit SHA in the sidecar metadata.
- **Wiktionary / Wikipedia titles:** Released under [CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
  and [GFDL](https://www.gnu.org/copyleft/fdl.html); attribution to "Wiktionary"
  / "Wikipedia" contributors. We redistribute only article titles, not article
  bodies.
- **GeoNames:** [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/);
  attribution required: "GeoNames" with a link to https://www.geonames.org.
- **US Census / SSA names:** US Government works, public domain.
- **ISO 3166 country list:** From the open
  [datasets/country-list](https://github.com/datasets/country-list) repo,
  Public Domain Dedication & License (PDDL).
- **NYSE/NASDAQ tickers:** Public listings from NASDAQ Trader's official feed.
- **SEC EDGAR:** US Government work, public domain. Per SEC's policy, our
  scraper declares a contact email in the User-Agent.
- **The Graph (ENS subgraph):** The subgraph itself is MIT-licensed
  ([ensdomains/ens-subgraph](https://github.com/ensdomains/ens-subgraph)).
  Underlying on-chain data is public; The Graph's terms apply to the indexer
  service.
- **Alchemy NFT API:** Per Alchemy's [terms of service](https://www.alchemy.com/policies/terms),
  data retrieved via the API may be used for analytics and product development.
  Sale event data ultimately originates from public on-chain marketplace
  contracts (Seaport, Blur, etc.).

## Contact

Questions, corrections, or pull requests: nejc@nejc.dev

## Citation

```bibtex
@misc{ens_appraiser_data_2026,
  author = {Drobnič, Nejc},
  title  = {ENS Appraiser — Multi-source Training Data},
  year   = {2026},
  publisher = {Hugging Face},
  url    = {https://huggingface.co/datasets/quantumly/ens-appraiser-data}
}
```