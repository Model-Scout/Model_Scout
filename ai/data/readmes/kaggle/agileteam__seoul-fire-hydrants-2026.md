# Seoul Fire Hydrants & Water Facilities 2026

62,771 geocoded fire hydrants and water facilities in Seoul, Korea

**All 62,771 fire hydrants and fire-fighting water facilities in Seoul, South Korea, with coordinates, type, installation year, outlet pressure and the fire station responsible. Reference date 2026-09-10. Fully in English and ready for maps.**

The source is the Seoul Metropolitan Fire & Disaster Headquarters' standard registration file (Korean, Excel, two-line headers). This dataset translates it into English and fixes coordinates.

### Files
| file | rows × cols | what it is |
|---|---|---|
| `seoul_fire_water_facilities_2026.csv` | 62,771 × 18 | One row per facility. English headers and values, numeric lat/lon (WGS84), `coord_status` flag |
| `data_dictionary.csv` | 18 | Every column with notes |

### Quick facts (checked against the file)
- Underground hydrants 42,860, above-ground hydrants 16,983, cisterns 271, underground rising hydrants 49, water towers 29
- Type code 06 (2,579 rows) is not in the source legend. 1,761 of them carry the emergency fire-fighting device marker in their ID, so they are labelled "likely emergency fire-fighting device".
- Median installation year 1996
- 25 districts and 25 fire stations; Gangnam-gu has the most facilities (3,716)

### How it was translated
- Districts, neighbourhoods, roads, fire stations and safety centres are romanized with the Revised Romanization of Korean, the official system. Examples: Gangnam Fire Station, Yeoksam 119 Safety Center, Sejong-daero 23-gil.
- Addresses are rewritten in English order: `67, Ujeongguk-ro, Jongno-gu, Seoul`. Building names go in brackets.
- `location_detail` is free text written by firefighters (e.g. "in front of the villa"). It was **machine-translated by rules**: common words are translated (front of, near, house, apartment, convenience store…), well-known brands use their English names, and other proper names (shops, buildings) are romanized. Expect some awkward phrases.

### Cleaning notes (`coord_status`)
- `ok` 61,527 rows
- `fixed_swapped` 442 rows: latitude and longitude were swapped in the source and are corrected here
- `invalid_blanked` 34 rows: coordinates outside Seoul, set blank
- `missing` 768 rows: no coordinates in the source
- `install_year` is blank for 5,879 rows. 3,368 are blank in the source. The other 2,511 are set blank because they are placeholders or typos: year 1900 is used for 2,507 rows (2,440 of them in Nowon-gu), plus 1905, 201 and 2905.
- `outlet_pressure_kgf_cm2` is 0 for 16,788 rows (often not measured).
- `facility_id` has 272 duplicates in the source. They are kept.
- Privacy: some source notes named private residents (e.g. "Mr. X's house"). These names are replaced with `private house` / `private property` / `private building`. Names on public business signs (clinics, shops, buildings) are kept.
- Stray Korean letters typed by mistake (e.g. a Korean vowel typed instead of a hyphen in `13-23`) are cleaned, and 13 malformed fire-station phone numbers are corrected to `02-6981-7372`.

### Ideas
- Map hydrant density per district or 500 m grid.
- Find areas far from the nearest hydrant (nearest-neighbour distance).
- Look at infrastructure age by district using `install_year`.
- Combine with **Seoul Fire Incidents 2022** (same author).

### Source and licence
- Seoul Metropolitan Fire & Disaster Headquarters, "Seoul fire-fighting water facilities", Seoul Open Data Plaza OA-21306: https://data.seoul.go.kr/dataList/OA-21306/S/1/datasetView.do (standard registration file, 2026 edition).
- Licence: **Korea Open Government License (KOGL) Type 1**: free to use, including commercially and with changes, **with attribution**. Please cite the source above.
- Translation and cleaning by the uploader. Translations are the uploader's own; the source file has the original Korean values.

출처: Kaggle (agileteam/seoul-fire-hydrants-2026)
태그: cities and urban areas, data cleaning, geospatial analysis, tabular
라이선스: Other (specified in description)
수정일: 2026-10-25T07:42:55.653Z
