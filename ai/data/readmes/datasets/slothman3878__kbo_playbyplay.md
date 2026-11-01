---
license: cc-by-4.0
language:
- en
- ko
pretty_name: KBO Play-by-Play (v0)
task_categories: [tabular-regression]
tags: [baseball, kbo, sports, play-by-play, statcast]
configs:
  - config_name: default
    data_files:
      - split: train
        path: "v0/kbo_pbp_*.parquet"
---

# KBO Play-by-Play, 2023-2026 (v0)

One row per pitch, 805,960 rows over 2,630 regular-season games, derived from NAVER Sports 문자중계. A Statcast/Retrosheet-style representation of KBO games: pitches, plate-appearance outcomes, base-out state and the transitions between them. Column names follow MLB Statcast wherever the meaning matches, so the same analysis code runs on both.

Built with [**kbo_pbp**](https://github.com/slothman3878/kbo_pbp_naver_sports) — the extraction code, the column schema and the validation harness that produced the accuracy figures below. Use it to rebuild this dataset, extend it to other seasons, or check the parsing yourself. [**demo.ipynb**](https://github.com/slothman3878/kbo_pbp_naver_sports/blob/main/demo.ipynb) works through loading this file, aggregating batting lines, plotting the strike zone, and building a 24-state run-expectancy table.

| season | games | pitches | plate appearances | batters |
|---|---|---|---|---|
| 2023 | 720 | 219,934 | 56,401 | 293 |
| 2024 | 720 | 223,277 | 57,401 | 298 |
| 2025 | 720 | 217,970 | 56,139 | 299 |
| 2026 | 470 | 144,779 | 37,192 | 272 |

The current season is in progress — this build covers games through **2026-07-26**.

## Columns

`v0/schema.yaml` is the authority: all 48 columns, with types, nullability and units. Four things to know before doing arithmetic:

- **Units are mixed.** Speed is km/h; the pitch-tracking block (locations, velocities, accelerations) is in feet, inherited from PITCHf/x.
- **`plate_z` is derived**, not supplied — solved from the trajectory. NAVER's `crossPlateY` is a constant reference plane, not the pitch's height.
- **Outcomes are coded**, into a closed set of 15 values: `single`, `strikeout`, `sac_fly`, `fielders_choice` and so on.
- **Pitch types are localised.** `pitch_type` and `pitch_name` are Statcast's codes and English names (`FF` / `4-Seam Fastball`); the Korean label they were mapped from is kept in `_naver_pitch_name`. Beyond that and player names, no Korean text is included — see the usage notice below.

## Accuracy

Every batter's season line was aggregated from these rows and diffed against the official NAVER season stats. Home runs, hit-by-pitch and walks match exactly; at-bats and hits land within a handful of events per season out of ~50,000, and some of that residual is NAVER's own bookkeeping rather than the parser's.

Known source-side defects, all handled or documented: replayed relay chunks in three 2024 games, a `crossPlateY` that reads wrong in some games, and official season lines that cover only part of a traded player's year.

## Caveats

- Regular season only. Preseason, the All-Star game and the postseason are excluded, matching the official totals this was validated against.
- The latest season is partial and will be rebuilt as it goes. Pin a specific revision if you need a stable cut.
- 2022 and earlier carry no pitch tracking at all.
- Baserunners resolve through the batting order, so they are only meaningful at plate-appearance boundaries.
- Sacrifices are the official scorer's judgement, taken from the source's wording — they are not derivable from the game state.
- There is no human-readable play description in v0. A generated English one, composed from the structured fields rather than copied from the source, is planned.

# Source

The dataset was generated from publicly available KBO play-by-play information provided through NAVER Sports 문자중계, using [kbo_pbp](https://github.com/slothman3878/kbo_pbp_naver_sports). Unofficial, and not affiliated with or endorsed by the KBO or NAVER.

# Data Usage Notice

This dataset does not contain the original NAVER Sports commentary text. Only structured baseball event records derived from the source information are included.

The original source material may be subject to separate terms and rights. Users are responsible for complying with applicable terms of service and regulations when using this dataset.

# License

This dataset is released under the Creative Commons Attribution 4.0 International (CC BY 4.0) License.
