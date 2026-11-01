---
license: cc-by-4.0
language:
  - ko
pretty_name: Korean Saju (Four Pillars) Five-Element Distribution
size_categories:
  - n<1K
tags:
  - korean
  - astrology
  - saju
  - four-pillars
  - wuxing
  - myeongni
configs:
  - config_name: default
    data_files: element-distribution.csv
---

# Korean Saju Five-Element (오행) Distribution

Every possible birth moment from 1966-01-01 to 2010-12-31 —
**16,436 days × 12 double-hours = 197,232 charts** —
computed with one deterministic Four Pillars (사주) engine, then counted by how many
of each of the five elements (오행: 목 wood, 화 fire, 토 earth, 금 metal, 수 water)
the eight characters contain.

**This is an exhaustive enumeration of a time space, not a sample of people.**
Real births are not uniform across dates and hours, so these frequencies are *not*
population proportions. A rare spread is not a better spread — this is frequency only.

## Why this exists

Korean Four Pillars content is everywhere; counted Korean Four Pillars data is not.
Commercial services compute charts inside a language model, so they cannot count.
This is the counted version, published so it can be checked and cited.

## What is in the file

One CSV, 693 rows, 10 columns.

| column | meaning |
| --- | --- |
| `characters` | `8` = birth time known · `6` = birth time unknown |
| `count_목` … `count_수` | how many of that element the chart holds |
| `occurrences` | how many charts in the window have exactly this spread |
| `sample_size` | total charts counted for that `characters` group |
| `window_start` / `window_end` | the counted window |

Rows are sorted by `occurrences` **within each `characters` group**, then the groups
are concatenated. Split on `characters` before you read the order.

There is no `share` or `one_in` column on purpose. Both are exactly recoverable as
`occurrences / sample_size`, and rounding them produces a share column that does not
sum to 1 — which makes anyone checking the file distrust all of it.

The 8-character and 6-character tables are **different random variables** over samples
that differ by a factor of 12. Do not put them side by side.

## Headline numbers (8 characters, n=197,232)

| element | mean count | charts with none |
| --- | ---: | ---: |
| 목 | 1.431 | 21.8% |
| 화 | 1.484 | 18.9% |
| 토 | 2.155 | 7.4% |
| 금 | 1.478 | 20.1% |
| 수 | 1.451 | 20.5% |

Earth (토) is the outlier: four of the twelve earthly branches (진·술·축·미) are earth,
so it is both hardest to be missing and easiest to be plentiful. That asymmetry is
structural, not mystical.

## Reproducing

16,436 days from 1966-01-01 to 2010-12-31 inclusive,
times 12 double-hours, is 197,232 — you can check the sample size with
a calendar alone. Reproducing the spreads themselves needs a Four Pillars engine that
agrees on solar-term boundaries and true solar time.

## Source and citation

- Page: https://sortia-ai.com/data/ohaeng
- CSV: https://sortia-ai.com/data/ohaeng/element-distribution.csv
- Summary JSON API: https://sortia-ai.com/api/backend/v1/public/element-statistics

```
SORTIA, "사주 오행 분포 통계" (1966–2010),
CC BY 4.0, https://sortia-ai.com/data/ohaeng
```

CC BY 4.0 asks three things: credit the author, link the license, and say if you
changed it.
