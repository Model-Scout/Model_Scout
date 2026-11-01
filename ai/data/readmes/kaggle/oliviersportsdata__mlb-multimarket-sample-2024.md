# ⚾ MLB Odds 2018–2026: Opening + 7 Books (Sample)

Moneyline, run line and totals with public betting splits, 20-game sample

# ⚾ MLB Multi-Market Odds — Opening Line + 7 Sportsbooks (2018–2026) · Free Sample

**Free sample: 20 games across nine seasons, 2018 to 2026.**

👉 Full dataset on Gumroad (19,801 games): https://sportsdataolivier.gumroad.com/l/mqzlxm?utm_source=kaggle&utm_medium=dataset&utm_campaign=mlb_sample

Every MLB game from Opening Day 2018 to 29 July 2026, regular season and postseason, with the opening line and the closing prices of seven named sportsbooks on three markets: moneyline, run line and total. Public betting percentages sit on the same row, next to the away starting pitcher and the final score.

## What's in this sample

| | |
|---|---|
| Games | 20 of 19,801 |
| Seasons | 2018 to 2026, two or three games each |
| Highlights | five World Series games (2018 G5, 2019 G7, 2022 G6, 2024 G5, 2025 G7), the 2021 Field of Dreams game, Opening Days |
| Columns | 138, identical to the full file |
| Format | one row per game · semicolon-separated · UTF-8 |

**Identical schema to the full dataset.** Code written against this sample runs unchanged on the complete file.

```python
import pandas as pd
df = pd.read_csv("MLB_MultiMarket_Sample_20_Games.csv", sep=";", encoding="utf-8-sig")
```

## Columns

| Group | Columns |
|---|---|
| Game | Season, Date, Day, Time, Away_Team, Home_Team, Away_Pitcher |
| Result | Away_Score, Home_Score, Winner, Total_Runs, Margin |
| Public betting | bet % on both sides of the moneyline, run line and total |
| Moneyline | opening line + 7 books, US and decimal odds |
| Run line | opening line + 7 books: line, US and decimal odds |
| Total | opening line + 7 books: line, over and under prices |

Sportsbooks: BookMaker · Heritage · BetOnline · Bovada · BetAnything · William Hill · Everygame.

## Read this first

- **Time** is the scheduled first pitch in US Eastern Time.
- **Doubleheaders** appear as two rows with the same date and teams. The time tells them apart.
- **Opener** is the opening line. Each sportsbook column holds that book's closing price.
- **Book coverage is not uniform.** BookMaker is thin in 2021 and 2022, and BetAnything starts in mid-2021.
- **2026 runs to 29 July.** From 23 June 2026, the run line and total lines are present but their prices are not.
- **Two international openers are missing**: the 2024 Seoul Series and the 2025 Tokyo Series, four games in all.

## The full dataset

| | Sample | Full |
|---|---|---|
| Games | 20 | 19,801 |
| Seasons | 2018–2026 | 2018 → 29 July 2026 |
| Columns | 138 | 138 |

👉 https://sportsdataolivier.gumroad.com/l/mqzlxm?utm_source=kaggle&utm_medium=dataset&utm_campaign=mlb_sample

🐔 Olivier Sports Data — From Chicken Area. Multi-sport historical datasets for data scientists, quants and professional syndicates.

출처: Kaggle (oliviersportsdata/mlb-multimarket-sample-2024)
태그: baseball, sports, finance, classification, gambling
라이선스: Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)
수정일: 2026-10-06T17:35:43.637Z
