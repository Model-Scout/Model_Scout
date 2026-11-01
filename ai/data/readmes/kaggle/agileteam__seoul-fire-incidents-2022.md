# Seoul Fire Incidents 2022

Every fire in Seoul in 2022: cause, place, casualties, response time, weather

**Every fire incident reported in Seoul, South Korea in 2022: 5,396 rows, one per fire, with time, place, cause, casualties, damage, response time, resources mobilised and weather. Fully in English.**

The source file is published by the National Fire Agency of Korea on the Korean public data portal, in Korean. This dataset translates it into English, adds a `datetime` column and fixes swapped headers.

### Files
| file | rows × cols | what it is |
|---|---|---|
| `seoul_fire_incidents_2022.csv` | 5,396 × 26 | One row per fire. English headers and values |
| `data_dictionary.csv` | 26 | Every column with notes |

### Quick facts (checked against the file)
- 5,396 fires, 37 deaths, 325 injuries
- Ignition cause: carelessness 54.1%, electrical 27.0%, unknown 9.7%
- Most fires: Gangnam-gu (437), Songpa-gu (350), Gwanak-gu (305)
- Median response time 229 s; 97.2% of fires reached within 7 minutes (420 s)

### How it was translated
- Categories (fire type, ignition cause, place, day of week, wind) are translated by hand from a fixed list.
- District and neighbourhood (dong) names are romanized with the Revised Romanization of Korean, the official system (e.g. Sillim-dong, Jongno 1-ga).

### Cleaning notes
- **Wind columns were swapped in the source.** The column named wind speed holds directions (N, NW…) and the one named wind direction holds speed bands. Corrected here.
- `fire_floor` is blank for 1,188 rows (non-building fires or not recorded). Negative = basement.
- `humidity_pct` is 0 for 440 rows and `temperature_c` is 0 for 47 rows. These are most likely missing values; left as published.
- `property_damage_krw1000`: the source does not state the unit. Korean fire statistics report property damage in thousand KRW.
- `suppression_time_sec` is 0 for 569 rows.

### Ideas
- Which neighbourhoods have the most fires per resident? Join with Seoul population by dong.
- Does response time differ by district or hour?
- Predict casualties or damage from cause, place and time.
- Pair with **Seoul Fire Hydrants & Water Facilities 2026** (same author) for hydrant coverage.

### Source and licence
- National Fire Agency of Korea (Fire Investigation Division), "Fire occurrence by eup/myeon/dong in Seoul", Public Data Portal dataset 15124423: https://www.data.go.kr/data/15124423/fileData.do (registered 2023-10-12, updated 2025-09-11).
- The portal lists the licence as **no restrictions on use**. Please cite the source above.
- Translation and cleaning by the uploader. Translations are the uploader's own; the source file has the original Korean values.

출처: Kaggle (agileteam/seoul-fire-incidents-2022)
태그: cities and urban areas, beginner, data cleaning, tabular
라이선스: Other (specified in description)
수정일: 2026-10-24T04:47:30.323Z
