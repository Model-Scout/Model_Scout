---
license: cc-by-4.0
language:
- ko
- en
pretty_name: Korea Lotto 6/45 First Prize - After-tax and Inflation-adjusted Average by Year
tags:
- lottery
- korea
- inflation
- time-series
- economics
size_categories:
- n<1K
configs:
- config_name: default
  data_files: lotto-first-prize.csv
---

# 로또 6/45 1등 평균 실수령액 연도별 시계열 (대한민국)

Korea Lotto 6/45 first prize by year, 2002 to the latest draw: average prize per draw,
average per winner, after-tax average per winner, the same in 2025 won (CPI-adjusted),
and how many years of full-time minimum wage it equals.

**Source page (canonical):** https://cashlogy.kr/data/lotto-first-prize
This repository is a mirror of the CSV published there. The canonical page carries the
method, limits and the latest update.

## Columns

| column | meaning |
|---|---|
| `year` | draw year |
| `draws` | number of draws in the year |
| `draws_with_winner` | draws that had at least one first-prize winner (others rolled over) |
| `winners` | first-prize winners in the year |
| `avg_by_draw_krw` | average of per-draw prize per winner, rollover draws counted as 0 (the method Donghaeng Lottery and the press use) |
| `avg_by_winner_krw` | average per winner, weighted by winners per draw |
| `net_by_winner_krw` | same, after 22% (up to 300M won) / 33% (above) withholding tax |
| `net_real_krw_2025` | `net_by_winner_krw` in 2025 won, CPI-adjusted. Empty when the year's CPI is not published |
| `min_wage_years` | `net_by_winner_krw` / (hourly minimum wage x 209 h x 12) |
| `partial_year` | 1 when the year is still in progress |

## Limits

- The current tax rates are applied to every year.
- 209 hours/month is applied to every year. Under the 44-hour week of the early 2000s the
  real monthly hours were longer, so `min_wage_years` is overstated for those years.
- 2002 has only 4 draws; ticket price and rollover rules differed until August 2004.
  Compare from 2005.
- First prize only.

## Sources

- Draw results: Donghaeng Lottery (https://www.dhlottery.co.kr/)
- Minimum wage: Minimum Wage Commission (https://www.minimumwage.go.kr/)
- CPI: Statistics Korea via World Bank API (FP.CPI.TOTL)

## Citation

KGENOTS / Cashlogy, "로또 1등 평균 실수령액 연도별 시계열",
https://cashlogy.kr/data/lotto-first-prize (CC BY 4.0)
