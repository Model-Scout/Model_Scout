---
license: cc-by-sa-4.0
language:
- ko
size_categories:
- 10K<n<100K
task_categories:
- tabular-classification
tags:
- saju
- bazi
- four-pillars
- korean
- public-figures
- wikidata
- wikipedia
- astrology-research
pretty_name: Korean Public Figures with Saju (Four Pillars)
configs:
- config_name: default
  data_files:
  - split: train
    path: train.parquet
---

# Korean Public Figures with Saju (Four Pillars)

39,494 Korean public figures (politicians, actors, athletes, etc.) with verified day-precision birth dates, occupations, and computed **Saju (사주, four-pillars / bazi)** astrological columns — assembled from Wikidata + Korean Wikipedia, used to empirically test whether Saju can predict occupation.

## Dataset Summary

- **Rows**: 39,494 (Track A — birth date precision = day)
- **Sources**: Wikidata (CC0) seed + Korean Wikipedia (CC BY-SA 3.0) infobox enrichment
- **Saju engine**: [sajupy 0.2](https://github.com/0ssw1/sajupy) (Korean Manseryeok / 만세력)
- **Date range**: 0995-12-19 ~ 2017-10-28 (most concentrated 1950–1999)
- **Track**: A only (year-month-day, no hour pillar — birth-time is missing in <5% of wiki infoboxes, so it was excluded by design)

## Use Cases

- Empirical validation of Saju / Bazi astrology claims (occupation prediction, day-master analysis)
- Korean public-figure demographics
- Korean name parsing benchmarks
- Multi-label occupation classification baseline

## Columns

### Identity
| field | type | note |
|---|---|---|
| `wikidata_qid` | str | `Q12345` — Wikidata entity ID |
| `name_ko` | str | Korean label |
| `name_aliases` | str | `|`-separated (English names etc.) |

### Birth & Bio
| field | type | note |
|---|---|---|
| `birth_date` | str (ISO date) | `1976-10-11`, day-precision |
| `birth_calendar_src` | str | `solar` / `lunar` / `unknown` (lunar already solar-converted) |
| `gender` | str | `남성` / `여성` / etc. |
| `birth_place` | str | seed-or-kowiki, normalized first 3 tokens |
| `occupations_raw` | str | `|`-separated multi-label (e.g. `정치인 \| 변호사`) |
| `in_track_a` | bool | always True (filtered) |

### Saju 6 characters (六字, year-month-day stems & branches)
Hour pillar **omitted** — birth-time is missing for ~95% of public-figure infoboxes, making the fourth pillar unreliable.

| field | example | description |
|---|---|---|
| `year_stem`, `year_branch` | 丙, 辰 | year pillar (年柱) |
| `month_stem`, `month_branch` | 戊, 戌 | month pillar (月柱), 24-solar-term aware |
| `day_stem`, `day_branch` | 丙, 申 | **day pillar (日柱) — `day_stem` = 일간/日干 = native** |

### Derived (5-elements 오행, yin-yang 음양, 12-zodiac)
| pattern | values |
|---|---|
| `{year,month,day}_stem_element` | 목/화/토/금/수 (wood/fire/earth/metal/water) |
| `{year,month,day}_branch_element` | 목/화/토/금/수 |
| `{year,month,day}_stem_polarity` | 양/음 (yang/yin) |
| `{year,month,day}_branch_polarity` | 양/음 |
| `{year,month,day}_branch_animal` | 쥐/소/범/.../돼지 (12 zodiac) |

### Provenance
| field | note |
|---|---|
| `kowiki_title` | matched ko.wikipedia.org page title (None if no match) |
| `infobox_template` | which infobox template was parsed |
| `source_wikidata` | `https://www.wikidata.org/wiki/Q...` |
| `source_wikipedia` | `https://ko.wikipedia.org/wiki/...` |
| `fetched_at` | UTC timestamp |

## How the Saju 6-character was computed

For each person, the date triple `(year, month, day)` is passed to `sajupy.calculate_saju(y, m, d, 12, 0)`. The fixed `hour=12, minute=0` choice means the **hour pillar from sajupy must be ignored**; only the **year / month / day** pillars are reliable. That is why hour-pillar columns were dropped from the export.

The Manseryeok inside sajupy covers 1900–2100. Persons with birth-year outside that range (mostly pre-1900 historical figures: ~384 rows) get NaN in saju columns.

## License

**CC BY-SA 4.0** — Creative Commons Attribution-ShareAlike 4.0 International.

This is the strictest license among the source materials used (Wikidata CC0 + Korean Wikipedia CC BY-SA 3.0). If you build on this dataset, you must attribute and share-alike.

**Namuwiki data is intentionally excluded** from this release, because Namuwiki's CC BY-NC-SA 2.0 KR license would force a non-commercial restriction on the whole dataset.

## Attribution

Please cite Wikidata and Korean Wikipedia as the original data sources:

```bibtex
@misc{korean_public_figures_saju_2026,
  title  = {Korean Public Figures with Saju (Four Pillars)},
  year   = {2026},
  note   = {Built from Wikidata (CC0) and Korean Wikipedia dump kowiki-20260501. Saju computation via sajupy.},
  url    = {https://huggingface.co/datasets/brandonrhie/korean-public-figures-saju}
}
```

## Empirical findings (from this dataset)

Using 930 chi-square tests × FDR-corrected (Benjamini-Hochberg α=0.05) across 31 occupations × 15 Saju dimensions, **no robust evidence was found that Saju predicts occupation**:

- Day-master (`day_stem_element`) distribution across the population is nearly uniform (20.3/20.3/19.9/19.9/19.6%), and remains uniform within almost every occupation.
- The strongest "signals" (Cramér's V ≈ 0.04–0.07) all map onto:
  - **Relative Age Effect (RAE)** — football/baseball/basketball players cluster on certain `month_branch` due to school-year cutoff dates, not Saju metaphysics
  - **Birth-year cohort effects** — politicians cluster on certain `year_branch` because they are mostly born 1950–1960s
- All effect sizes are V<0.07 = "negligible" by Cohen's convention.

See the `analysis/` files for full reproduction.

## Limitations

1. **Selection bias**: only Korean Wikipedia-notable figures (politicians, athletes, entertainers, etc.). Not generalizable to general population.
2. **Hour pillar missing**: Saju traditionalists hold that birth-hour is the most important variable. This dataset cannot test that claim because birth-hour is virtually never recorded in public biography sources.
3. **Multi-label occupation noise**: `occupations_raw` is preserved as free-form tags (e.g. both "축구 선수" and "대한민국의 축구선수" may appear for the same person). Clustering / normalization required before downstream use.
4. **Historical figures**: persons born before 1900 are present but their Saju is computed by Manseryeok extrapolation and may have edge cases.

## Files

- `train.parquet` — main data (Parquet, snappy compression)
- `persons.xlsx` — same data in Excel format with column ordering

