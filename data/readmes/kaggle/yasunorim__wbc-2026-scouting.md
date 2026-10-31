# WBC 2026 Scouting - Statcast Data

Statcast pitch-by-pitch data for WBC 2026 roster players, 20 countries

# WBC 2026 Scouting - Statcast Data

Pitch-by-pitch MLB Statcast data for players selected to the **WBC 2026 (World Baseball Classic)** rosters, covering **18 national teams** (batting data) and **14 national teams** (pitching data). Only players with MLB records are included.

## Files

### statcast_batters.csv (37 MB)
- **338,811 pitches** faced by WBC batters (MLB regular season data)
- **18 countries**: AUS, CAN, COL, CUB, DOM, GBR, ISR, ITA, JPN, KOR, MEX, NCA, NED, PUR, TPE, USA, VEN + more
- `country` and `country_name` columns added for easy filtering
- Full Statcast columns: pitch type, speed, movement, launch angle, exit velocity, expected stats, bat tracking (2024+), and more

### statcast_pitchers.csv (30 MB)
- **220,385 pitches** thrown by WBC pitchers (MLB regular season data)
- **14 countries**: CAN, COL, DOM, GBR, ISR, ITA, JPN, KOR, MEX, NED, PAN, PUR, USA, VEN
- `country` and `country_name` columns added for easy filtering

### batter_summary.csv
- Per-player batting summary: **109 batters** across 19 countries
- Columns: PA, AB, H, 1B, 2B, 3B, HR, BB, HBP, K, TB, AVG, OBP, SLG, OPS, K_pct, BB_pct, xwOBA, avg_exit_velo, avg_launch_angle

### pitcher_summary.csv
- Per-player pitching summary: **90 pitchers** across 14 countries
- Columns: total_pitches, PA_faced, K, BB, HR_allowed, H_allowed, opp_AVG, opp_SLG, K_pct, BB_pct, xwOBA_against, avg_velo, avg_spin_rate, pitch_type_count, primary_pitch

### rosters.csv
- Clean roster for all **308 MLB-affiliated WBC 2026 players** across 20 countries
- Columns: name, country, pool, position, team, on_40_man, role
- Includes players with and without Statcast data (e.g., minor league players)
- **Updated Mar 2, 2026**: USA roster: Carroll (broken hamate) → Anthony; Joe Ryan (back tightness) → Yarbrough

### stadiums.csv
- MLB stadium coordinates used for spray chart rendering
- 1,002 rows covering all 30 MLB parks

## Country Codes

| Code | Country | Pool |
|---|---|---|
| USA | USA | B (Houston) |
| JPN | Japan | C (Tokyo) |
| DOM | Dominican Republic | D (Miami) |
| VEN | Venezuela | D (Miami) |
| PUR | Puerto Rico | A (San Juan) |
| MEX | Mexico | B (Houston) |
| KOR | Korea | C (Tokyo) |
| NED | Netherlands | D (Miami) |
| CAN | Canada | A (San Juan) |
| ITA | Italy | B (Houston) |
| ISR | Israel | D (Miami) |
| GBR | Great Britain | B (Houston) |
| PAN | Panama | A (San Juan) |
| COL | Colombia | A (San Juan) |
| CUB | Cuba | A (San Juan) |
| TPE | Chinese Taipei | C (Tokyo) |
| NCA | Nicaragua | D (Miami) |
| AUS | Australia | C (Tokyo) |
| BRA | Brazil | B (Houston) |
| CZE | Czechia | C (Tokyo) |

> Brazil and Czechia have no MLB-affiliated players; their Statcast data is not included.

## Notes on Coverage

- **Batting Statcast**: Available for 18 countries (all except Brazil and Czechia)
- **Pitching Statcast**: Available for 14 countries (Cuba, Nicaragua, Chinese Taipei, and Australia do not have pitcher Statcast data)
- All data reflects MLB regular season performance; WBC game data is not included
- Stats may be influenced by sample size differences between players and countries

## Analysis Ideas

- Compare batting profiles (exit velocity, launch angle, xwOBA) across countries
- Analyze pitching arsenals and velocity distributions by country
- Identify players with strong MLB track records heading into the tournament
- Build country-level offensive and defensive strength indexes
- Explore pitch type usage patterns across different national pitching staffs
- Study the relationship between MLB regular season stats and potential WBC performance

## Interactive Dashboard

**Landing page (all teams):** [https://wbc-2026-scouting-dashboard-zvg.caffeine.xyz/](https://wbc-2026-scouting-dashboard-zvg.caffeine.xyz/)

A bilingual (EN/JA) landing page hosted on ICP via Caffeine, listing all team dashboard links organized by pool.

Exploratory dashboards for all WBC teams are available as Streamlit apps:
- Batter dashboards: spray charts, zone heatmaps, count-based performance
- Pitcher dashboards: pitch movement charts, usage heatmaps, L/R split stats

> **Note**: Streamlit apps go to sleep after inactivity. If you see "Zzzz" or "Your app is in the oven," wait a moment and reload.

| Country | Batters | Pitchers |
|---|---|---|
| USA | [wbc-usa-batters](https://wbc-usa-batters.streamlit.app/) | [wbc-usa-pitchers](https://wbc-usa-pitchers.streamlit.app/) |
| Japan | [wbc-japan-batters](https://wbc-japan-batters.streamlit.app/) | [wbc-japan-pitchers](https://wbc-japan-pitchers.streamlit.app/) |
| Dominican Republic | [wbc-dr-batters](https://wbc-dr-batters.streamlit.app/) | [wbc-dr-pitchers](https://wbc-dr-pitchers.streamlit.app/) |
| Mexico | [wbc-mex-batters](https://wbc-mex-batters.streamlit.app/) | [wbc-mex-pitchers](https://wbc-mex-pitchers.streamlit.app/) |
| Puerto Rico | [wbc-pr-batters](https://wbc-pr-batters.streamlit.app/) | [wbc-pr-pitchers](https://wbc-pr-pitchers.streamlit.app/) |
| Korea | [wbc-kor-batters](https://wbc-kor-batters.streamlit.app/) | [wbc-kor-pitchers](https://wbc-kor-pitchers.streamlit.app/) |
| Netherlands | [wbc-ned-batters](https://wbc-ned-batters.streamlit.app/) | [wbc-ned-pitchers](https://wbc-ned-pitchers.streamlit.app/) |
| Canada | [wbc-can-batters](https://wbc-can-batters.streamlit.app/) | [wbc-can-pitchers](https://wbc-can-pitchers.streamlit.app/) |
| Italy | [wbc-ita-batters](https://wbc-ita-batters.streamlit.app/) | [wbc-ita-pitchers](https://wbc-ita-pitchers.streamlit.app/) |
| Israel | [wbc-isr-batters](https://wbc-isr-batters.streamlit.app/) | [wbc-isr-pitchers](https://wbc-isr-pitchers.streamlit.app/) |
| Great Britain | [wbc-gb-batters](https://wbc-gb-batters.streamlit.app/) | [wbc-gb-pitchers](https://wbc-gb-pitchers.streamlit.app/) |
| Panama | [wbc-pan-batters](https://wbc-pan-batters.streamlit.app/) | [wbc-pan-pitchers](https://wbc-pan-pitchers.streamlit.app/) |
| Colombia | [wbc-col-batters](https://wbc-col-batters.streamlit.app/) | [wbc-col-pitchers](https://wbc-col-pitchers.streamlit.app/) |
| Cuba | [wbc-cuba-batters](https://wbc-cuba-batters.streamlit.app/) | — |
| Chinese Taipei | [wbc-twn-batters](https://wbc-twn-batters.streamlit.app/) | — |
| Nicaragua | [wbc-nic-batters](https://wbc-nic-batters.streamlit.app/) | — |
| Australia | [wbc-aus-batters](https://wbc-aus-batters.streamlit.app/) | — |

[Source code (GitHub)](https://github.com/yasumorishima/wbc-scouting)

## Data Source

Data retrieved from [Baseball Savant](https://baseballsavant.mlb.com/) via the [pybaseball](https://github.com/jldbc/pybaseball) Python library. Roster data based on the official WBC 2026 roster announcement (February 2026, Baseball America).

> **Data accuracy note:** This dataset is based on publicly available roster announcements (Baseball America, February 2026) and MLB Statcast records. Some players may be missing, misclassified, or have since been added/removed from rosters. If you notice any errors, please leave a comment.

출처: Kaggle (yasunorim/wbc-2026-scouting)
태그: baseball, sports, data visualization, data analytics, news
라이선스: CC0: Public Domain
수정일: 2026-03-08T07:39:03.043Z
