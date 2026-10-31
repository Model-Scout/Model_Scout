---
license: other
license_name: trading-agent-free-licence
license_link: https://www.tradingagentapp.com/licences/free
language:
  - en
  - fr
  - nl
  - da
  - ja
  - ko
  - zh
tags:
  - finance
  - fundamentals
  - financial-statements
  - annual-accounts
  - company-registers
  - private-companies
  - xbrl
pretty_name: Company accounts by filing date (public sample)
size_categories:
  - 1K<n<10K
configs:
  - config_name: default
    data_files: trial_all_markets.csv
---

<!--
Upload with this card: trial_all_markets.csv, which must be the file served at
https://www.tradingagentapp.com/api/v1/fundamentals/sample, downloaded and
renamed, nothing else changed (1,447 rows, 84 entities, 8 markets, filings to
2026-10-07; 1,230,771 bytes, SHA-256 616D7F16...1B84F4). The Free Licence 1.2(c) covers the public sample CSV file only.
Re-check this copy against the Deletions Feed every 30 days and replace it
when rows are withdrawn.
-->

# Company accounts by filing date: public sample

Financial statement figures from eight official registers, for 84 entities
(73 companies and 11 New Zealand registered charities). Every row carries its
filing date, the register it came from, a link to the register's own page and
the source notice that must travel with it.

This is the public sample of [Trading Agent Data](https://www.tradingagentapp.com/fundamentals),
the same file as on <https://www.tradingagentapp.com/fundamentals/sample>. In
each market one entity runs across every fiscal year held; the others show
every metric for their latest year. The full dataset (about 2.75 million
entities, most of them private European companies) is served by the same API.

## The file

`trial_all_markets.csv`: 1,447 rows, 19 columns, UTF-8 with a header row (and
a byte-order mark, so Excel opens accented names correctly). One row per
entity, metric, fiscal year, period and basis.

| market | register | entities | rows | fiscal years | `filed` dates |
|---|---|---|---|---|---|
| FR | INPI, Registre national des entreprises | 14 | 219 | 2014–2025 | 2017-03-20 to 2026-09-30 |
| BE | National Bank of Belgium, Central Balance Sheet Office | 13 | 192 | 2021–2025 | 2022-05-12 to 2026-09-16 |
| DK | Danish Business Authority (Erhvervsstyrelsen), CVR | 12 | 198 | 2012–2026 | 2013-05-02 to 2026-09-24 |
| US | SEC EDGAR | 8 | 161 | 2014–2026 | 2014-10-27 to 2026-10-07 |
| JP | Financial Services Agency, EDINET | 8 | 213 | 2019–2026 | 2019-06-24 to 2026-06-26 |
| KR | Financial Supervisory Service, OpenDART | 11 | 178 | 2016–2025 | 2017-03-31 to 2026-03-18 |
| TW | Taiwan Stock Exchange (OpenAPI and MOPS) | 7 | 136 | 2013–2025 | 2014-03-31 to 2026-03-31 |
| NZC | Charities Services, Charities Register | 11 | 150 | 2014–2026 | 2015-01-25 to 2026-08-28 |
| **total** | | **84** | **1,447** | | |

## Columns

| column | meaning |
|---|---|
| `market` | FR, BE, DK, US, JP, KR, TW or NZC (New Zealand registered charities) |
| `ticker` | the ID to send to the API: `AAPL`, `E01766.JP` (EDINET code), `005930.KS` (KRX code), `2330.TW`, `387949530.FR` (SIREN), `0403091220.BE` (KBO), `14227547.DK` (CVR), `CC21860.NZC` (charity number) |
| `name` | the entity's name as the register holds it; Japanese, Korean and Taiwanese entities are named in their own script |
| `issuer_id` | the register's own identifier: CIK, EDINET code, DART corporation code, TWSE code, SIREN, KBO, CVR, or the charity's NZBN |
| `activity_code` | activity code (APE/NAF) where the register states one; France only, empty elsewhere |
| `address` | postcode and commune where the register states them; France only, empty elsewhere |
| `metric` | revenue, net_income, assets, equity, liabilities, operating_income, cash and other statement lines; ratios such as `roe` or `net_margin` are calculated from the filed figures and carry a `derived` form |
| `fy`, `fp`, `period_end` | fiscal year, period (`FY`, or `Q1`–`Q4` for Taiwan quarters) and the last day of the period |
| `filed` | the filing date: the date each register records for the filing (meaning per market below) |
| `form` | the filing type: `10-K`, `annual`, `annual/ifrs`, `annual/solo`, `quarterly`, `annual-return`; France: reporting model and confidentiality flag (`K/Public`, `C/Public`, `S/Public` …); Belgium: the NBB model (`m02-f` …); `derived` for ratios |
| `basis` | which entity the figure describes: `consolidated` (the group), `solo` (the company's own accounts) or `reported` |
| `value`, `unit` | the figure as filed, in the filer's unit: EUR, USD, JPY, KRW, TWD, DKK, NZD, per-share units such as `USD/shares`, or `ratio` |
| `source_id` | the register's ID for the filing, where the source gives one (France; Japan; Korea: the DART receipt number; Denmark: the register's publication ID) |
| `register`, `register_url` | the register the filing came from, and its own page for the entity, to check a figure against the filing |
| `source_attribution` | the source notice that must stay with the row wherever it goes |

## What `filed` means, per market

`filed` is the date each register records for the filing. Filter on it to see
which figures had been filed by a given day, allowing for the known issues
below.

- **US**: the SEC filing date of the 10-K or 10-Q.
- **JP**: EDINET `submitDateTime`, the statutory filing timestamp.
- **KR**: the DART receipt date of the year's original annual report (사업보고서),
  the later of the receipt date and the date in its receipt number. A
  deadline-extension notice is never taken for the report, and a corrected
  report's figures are not used: each year carries its original report's figures.
- **TW**: the general statutory reporting deadline for the period, not the day
  the company filed. For most companies that is on or after the real release.
  Known issue, being corrected: some companies have later deadlines for some
  quarters, and a deadline on a weekend moves to the next business day, so for
  them this date can be earlier than their real deadline.
- **FR**: INPI `dateDepot`, the register's deposit date.
- **BE**: the NBB deposit date.
- **DK**: the Copenhagen calendar date on which the register published the
  report (before 11 April 2015 the register records a date only).
- **NZC**: the New Zealand date of the register's record for the annual
  return; it moves later if the return is amended. Known issue, being
  corrected: about a quarter of these dates are one day early.

Details: <https://www.tradingagentapp.com/fundamentals/methodology>.

## Read before using a figure

- `value` is the figure as filed. A later restatement does not replace it.
- Taiwan `Q1`–`Q4` income-statement figures are **single-quarter
  (three-month) amounts**. Taiwan files cumulative year-to-date totals and
  they are converted, so do not difference adjacent quarters again.
- Belgium is **statutory (solo)** accounts, never group consolidation.
- Korea is **consolidated** accounts of listed companies.
- France and Japan can carry **both** the group's accounts (`consolidated`)
  and the company's own (`solo`) for the same year; both rows are present.
- Denmark is the reporting entity's own accounts (`reported`): for a
  Danish-GAAP group parent usually its own, not the group's; IFRS filers'
  figures are the group's. Equity is checked against each filing's own
  balance sheet and left out where the filing shows the tagged figure is not
  total equity.
- Japan's `ordinary_income` (経常利益) is struck before extraordinary items and
  is not `pretax_income`.
- Turnover is lawfully absent from much private-company data (confidentiality
  declarations in France, gross-profit-only filers in Belgium and Denmark). It
  is never imputed. Measured fill rate per metric and market:
  <https://www.tradingagentapp.com/api/v1/fundamentals/quality> (no key).
- New Zealand rows are **registered charities**, not companies. Balance-sheet
  totals appear only where assets minus liabilities equals equity.

## Licence

The file is Free Data under the
[Free Licence](https://www.tradingagentapp.com/licences/free); using it means
you accept that licence.

- You may use it to evaluate the data and for internal use, including inside a
  company; publish aggregated results made from it; and quote small extracts
  (for example a company's figures in an article or paper) with the source
  notice for each market used.
- You may not republish or resell the file or a substantial part of it, or use
  it to build a competing dataset.
- Keep the `source_attribution` column in every copy. If you remove it, keep
  beside that copy an `ATTRIBUTION.txt` from
  <https://www.tradingagentapp.com/api/v1/fundamentals/attribution>.
- New Zealand charities data is also CC BY 3.0 NZ, and everything that
  licence permits still applies.

## Source notices

The binding notice for each row is its `source_attribution` column. In short:

- **US**: U.S. Securities and Exchange Commission, EDGAR (public information),
  last updated 2026-10-16. Processed by WU Capital Limited (Trading Agent
  Data); not reviewed or endorsed by the SEC.
- **JP**: 出典：EDINET閲覧（提出）サイト（https://disclosure2.edinet-fsa.go.jp/）、PDL1.0（https://www.digital.go.jp/resources/open_data/public_data_license_v1.0）.
  Financial Services Agency (Japan), EDINET, under Public Data License 1.0,
  last updated 2026-10-26. EDINET閲覧（提出）サイトのデータをもとにWU Capital
  Limitedが加工して作成. Not the Financial Services Agency's own publication
  and not endorsed by it.
- **KR**: Financial Supervisory Service (Korea), OpenDART
  (https://opendart.fss.or.kr), last updated 2026-10-26. Processed by WU
  Capital Limited (Trading Agent Data); not endorsed by the Financial
  Supervisory Service.
- **TW**: two routes, and both notices stay with every Taiwan row.
  - Current quarters: Taiwan Stock Exchange OpenAPI (t187ap06_L, t187ap07_L,
    v1), last updated 2026-10-26. 此開放資料依政府資料開放授權條款 (Open
    Government Data License) 進行公眾釋出，使用者於遵守本條款各項規定之前提下，得利用之。政府資料開放授權條款：https://data.gov.tw/license
  - History: Taiwan Stock Exchange, Market Observation Post System (MOPS),
    XBRL financial reports (https://mops.twse.com.tw), last updated
    2026-10-26. This archive is not released under the Open Government Data
    License.
  - Processed by WU Capital Limited (Trading Agent Data): fields mapped and
    reformatted, and cumulative year-to-date income converted to single
    quarters. Not the Taiwan Stock Exchange's original data and not endorsed
    by it.
- **FR**: Source : INPI, Registre national des entreprises (comptes annuels),
  Licence de réutilisation des informations du RNE, homologuée
  (https://www.inpi.fr/sites/default/files/Licence%20donn%C3%A9es%20RNE_2024_0.pdf),
  last updated
  2026-10-26. Données retraitées par WU Capital Limited (Trading Agent Data) ;
  cette réutilisation n'a aucun caractère officiel et n'est ni reconnue ni
  cautionnée par l'INPI.
- **BE**: National Bank of Belgium, Central Balance Sheet Office
  (Balanscentrale), last updated 2026-10-27. Processed by WU Capital Limited
  (Trading Agent Data); not endorsed by the National Bank of Belgium.
- **DK**: Erhvervsstyrelsen (Danish Business Authority), published annual
  reports (distribution.virk.dk), last updated 2026-10-28, used under the
  terms for Danish public data. All entities are treated as
  advertising-protected (Danish CVR Act, section 19): not for direct
  marketing. Not endorsed by Erhvervsstyrelsen.
- **NZC**: Charities Services, Department of Internal Affairs (New Zealand),
  Charities Register, CC BY 3.0 NZ
  (https://creativecommons.org/licenses/by/3.0/nz/), last updated 2026-09-20.
  Adapted by WU Capital Limited (Trading Agent Data); not endorsed by the
  Department of Internal Affairs. Original data:
  <https://catalogue.data.govt.nz/dataset/charities-register-open-data>.

## Deletions

Records are sometimes removed from the data, for example when a register
withdraws a filing. The Deletions Feed lists each one:
<https://www.tradingagentapp.com/api/v1/fundamentals/deletions>.

If you keep a copy of this file:

1. Check the feed at least once every 30 days, or turn on the daily email of
   new entries at <https://www.tradingagentapp.com/account/api-keys>.
2. Within 30 days after a record is listed, delete it from your copy and stop
   showing it.
3. Entries marked `delete` are served only to a free key, never to the `demo`
   key. A free key is at <https://www.tradingagentapp.com/account/api-keys>.

We re-check this copy against the feed every 30 days and replace it when rows
are withdrawn. The current file is always at
<https://www.tradingagentapp.com/fundamentals/sample>.

## Getting the live data

The `demo` key needs no signup and reads every company in the dataset at its
latest fiscal year:

```bash
curl -H "Authorization: Bearer demo" \
  "https://www.tradingagentapp.com/api/v1/fundamentals?ticker=387949530.FR"
```

Full history, and the `as_of` query (only figures filed on or before a chosen
day), come with a paid licence or a 30-day evaluation key for a work email:
<https://www.tradingagentapp.com/fundamentals/evaluate>. Python package and MCP
server: <https://www.tradingagentapp.com/developers>.

Questions, by email only: contact@tradingagentapp.com. Send up to 1,000
tickers or register IDs (SIREN, KBO, CVR, EDINET code) and we reply with the
match rate.

---

Factual, historical data from official filings; nothing here is a
recommendation to buy or sell any security. The records are about legal
entities: no directors or shareholders are added and sole traders are
excluded. If you find a record that relates to a person,
email contact@tradingagentapp.com with its market and identifier.

Published by WU Capital Limited (Trading Agent Data), New Zealand company
number 9434075.
