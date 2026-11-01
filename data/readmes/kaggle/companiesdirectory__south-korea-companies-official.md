# 120k South Korean Companies from Official Registry

120k South Korean companies from the official register

# 120k South Korean Companies from Official Registry

**119,569 South Korea companies**, one file.

> Part of the **companies.directory** database of **300M+ companies worldwide**.
> This snapshot is refreshed **weekly** (matching how often the
> underlying register changes); the companies.directory app & API are refreshed
> **monthly** — usually fresher than this file.

| | |
| --- | --- |
| **Records** | 119,569 |
| **Country** | South Korea (KR) |
| **Format** | CSV, UTF-8, gzip-compressed |
| **Columns** | 12 (basic fields) |
| **Snapshot** | 2026-10-18 |
| **Next snapshot** | 2027-01-01 (weekly) |

## Links

- **Browse on companies.directory** — https://companies.directory/south-korea
- **API documentation** — https://companies.directory/docs

## Files

- `kr-companies-official.csv.gz` — 119,569 rows, 8.6 MB

## Columns

| Column | Description |
| --- | --- |
| `company_id` | Stable SHA-1 identifier for the company (per source). |
| `source_id` | Catalog id of the originating official register (e.g. `de`, `us-ny`). |
| `reg_number_raw` | Registration / registry number exactly as published. |
| `legal_name_norm` | Upper-cased, whitespace-normalized legal name for matching. |
| `legal_form` | Legal form exactly as published (e.g. `GmbH`, `Osaühing`, `S.A.`). |
| `status` | Registration status as published by the register. |
| `incorporation_date` | Incorporation / registration date (ISO 8601). |
| `addr_street` | Street address. |
| `addr_city` | City / town. |
| `addr_zip` | Postal code. |
| `addr_region` | Region / state / province. |
| `addr_country` | ISO 3166-1 alpha-2 country of the address. |

## More fields on companies.directory

This file carries the **basic registry fields**. The full record on
[companies.directory](https://companies.directory) additionally has, where the register publishes
them — with standardized, human-friendly values:

| Example field | In the full record |
| --- | --- |
| Industry | `isic_rev5_code` = `4312` → human-readable label **"Site preparation activities"** |
| Legal form | `legal_form` = `GmbH` / `Osaühing` → standardized English **"Private limited liability company"** |
| Registration number | `reg_number_raw` = `Hamburg HRB 150148` → normalized `reg_number_norm` = **`HRB150148`** |
| Status | register-specific status text → standardized active / inactive / dissolved |

Plus raw + trade names, officers & directors, revenue, employee counts,
coordinates, website, email and phone. Browse [https://companies.directory](https://companies.directory) or use the API ([docs](https://companies.directory/docs)).

## Provenance / sources

| Source | Records | Last update | Cadence | Next update | Access | License | Official source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DART 기업개황 — Korea company register | 119,569 | 2026-10-20 | Daily | 2026-10-21 | public | Public disclosure (DART/FSS Korea); attribution requested | [link](https://dart.fss.or.kr/dsae001/main.do) |

## What you can build

Company search and lookups · KYC / KYB & onboarding · sales and lead
enrichment · market and industry research · risk and credit signals ·
entity-resolution and deduplication · academic and economic research.

## Go beyond a single country

This file is one slice of the **companies.directory** global company database.

- **300M+ companies in one place.** Every country we cover, normalized to one
  schema — not 50 incompatible register exports.
- **API access.** Query, filter and enrich programmatically over the full
  database (name, registration number, country, city, industry, status and
  more). Start at [https://companies.directory/docs](https://companies.directory/docs).
- **Additional fields not in this file.** Where a source publishes them:
  normalized registration numbers, trade names, standardized legal form and
  status, industry codes (ISIC Rev. 5), officers & directors, revenue,
  employee counts, geocoding, websites, emails and phones — see
  [companies.directory](https://companies.directory).
- **Bulk download.** The complete multi-country dataset is available as a
  single bulk download.
- **Dedicated infrastructure.** A hosted, indexed PostgreSQL deployment with
  sub-second search across hundreds of millions of rows.

Commercial use, volume licensing and custom extracts: **luka@companies.directory**.


## Update schedule

- **This platform snapshot** — refreshed **weekly**, matching
  how often the underlying register changes. Generated 2026-10-20; next
  snapshot **2027-01-01**.
- **companies.directory (app & API)** — refreshed **monthly**, usually
  fresher than this file: https://companies.directory/south-korea

## Citation

```bibtex
@misc{companies_directory_kr_20261018,
  title  = {120k South Korean Companies from Official Registry},
  author = {companies.directory},
  year   = {2026},
  note   = {Snapshot of the companies.directory database},
  url    = {https://companies.directory/south-korea}
}
```

## License & attribution

The processed, standardized compilation is published by
[companies.directory](https://companies.directory) under **CC BY 4.0**; the upstream sources keep their own licenses.

These attributions and licenses **must be preserved unchanged in any further use or redistribution** of this data:

**Data attribution:**

- **Trade registry data** — derived from the official company trade registries of South Korea. Per-register attribution, license and access terms: [companies.directory/sources](https://companies.directory/sources).

*Questions or commercial licensing: luka@companies.directory*

출처: Kaggle (companiesdirectory/south-korea-companies-official)
태그: business
라이선스: Attribution 4.0 International (CC BY 4.0)
수정일: 2026-10-20T20:04:52.837Z
