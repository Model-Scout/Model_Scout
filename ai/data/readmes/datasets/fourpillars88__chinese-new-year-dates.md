---
license: cc-by-4.0
language:
- en
- zh
- ja
- ko
pretty_name: Chinese New Year and Lichun dates 1930-2026
size_categories:
- n<1K
tags:
- chinese-new-year
- lunar-new-year
- chinese-zodiac
- calendar
- solar-terms
- astrology
task_categories:
- table-question-answering
configs:
- config_name: default
  data_files: chinese-new-year-lichun-1930-2026.csv
---

# Chinese New Year and Lichun dates, 1930–2026

Every Chinese New Year date and Lichun (立春, start of spring) time from 1930 to 2026, with the year's zodiac animal, element, Heavenly Stem and Earthly Branch, and Na Yin. 97 rows, one per year.

Use it to classify birth dates by Chinese zodiac correctly. Because the Chinese year does not start on January 1, people born in January or early February often belong to the previous animal, and the two common conventions (Chinese New Year vs. Lichun, used in BaZi astrology) can disagree.

Source and online version: [Four Pillars](https://fourpillars88.com/chinese-new-year-dates) · Calculator: [What is my Chinese zodiac?](https://fourpillars88.com/what-is-my-chinese-zodiac) · GitHub: [liubinwork-ux/chinese-new-year-dates](https://github.com/liubinwork-ux/chinese-new-year-dates)

## Columns

| Column | Example | Meaning |
| --- | --- | --- |
| `year` | 1990 | Gregorian year in which this Chinese year starts |
| `animal`, `animal_zh` | Horse, 马 | Zodiac animal (Earthly Branch) |
| `element`, `yin_yang` | Metal, Yang | Element and polarity of the Heavenly Stem |
| `stem_branch`, `stem_branch_pinyin` | 庚午, Geng Wu | Sexagenary name |
| `nayin`, `nayin_zh` | Roadside Earth, 路旁土 | Na Yin “sound element” |
| `chinese_new_year` | 1990-01-27 | First day of the Chinese year |
| `new_year_weekday` | Saturday | Weekday of Chinese New Year |
| `year_ends` | 1991-02-14 | Last day before the next Chinese New Year |
| `lichun_beijing` | 1990-02-04 10:11 | Lichun moment, Beijing time (UTC+8) |
| `lichun_utc` | 1990-02-04 02:11 | Lichun moment, UTC |

## Methods and accuracy

Chinese New Year dates come from the open-source lunardate tables (based on Hong Kong Observatory data), spot-checked against published dates. Lichun is computed with Jean Meeus's low-precision solar longitude formula (sun at 315°), accurate to about ±15 minutes.

## License and citation

CC BY 4.0. Please credit: Four Pillars, https://fourpillars88.com/chinese-new-year-dates

DOI: [10.5281/zenodo.23189503](https://doi.org/10.5281/zenodo.23189503)
