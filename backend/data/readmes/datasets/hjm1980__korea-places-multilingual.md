---
license: cc-by-4.0
language:
  - ko
  - en
  - ja
  - zh
  - ru
  - th
tags:
  - korea
  - toponym
  - romanization
  - multilingual
  - geospatial
pretty_name: Korean Place Names, Multilingual
size_categories:
  - 10K<n<100K
configs:
  - config_name: default
    data_files: korea-places-multilingual.csv
dataset_info:
  config_name: default
  features:
    - name: id
      dtype: string
    - name: name_ko
      dtype: string
    - name: name_en
      dtype: string
    - name: name_ja
      dtype: string
    - name: name_zh_hant
      dtype: string
    - name: name_zh_hans
      dtype: string
    - name: name_ru
      dtype: string
    - name: name_th
      dtype: string
    - name: lat
      dtype: float64
    - name: lng
      dtype: float64
    - name: region
      dtype: string
    - name: category
      dtype: string
    - name: address_en
      dtype: string
    - name: subway_lines
      dtype: string
    - name: homepage
      dtype: string
    - name: source
      dtype: string
    - name: ours
      dtype: string
  splits:
    - name: train
      num_examples: 16126
---

# Korean Place Names, Multilingual

Built and maintained by **[Korea Basics](https://basics.aljal.kr)**, a sourced guide to Korean
entry rules and getting around, published in seven languages.

16,126 places in South Korea with their **Korean (Hangul) name next to the
romanized English name**, plus Japanese and Chinese names where the source has
them, coordinates, road-name address, and subway lines for stations.

## Why this exists

A visitor who reads "Gyeongbokgung Palace" in a guide cannot type that into
KakaoMap or Naver Map, which is what actually works for navigation and taxis in
Korea. They need `경복궁`. Going the other way, a Korean name in a news article
or a signboard photo is hard to match against an English itinerary.

That mapping is not published anywhere as a plain table. This is that table.

## See it in use

The map at **https://basics.aljal.kr/map/** runs on this data. Search an English name, get the
Hangul back, and hand it straight to KakaoMap, Naver Map or a taxi driver. The
same site publishes Korean entry rules with a source link and a checked-on date
against every value, which is where this table comes from in the first place.

## Coverage

| Column | Non-empty rows |
|---|---:|
| `name_ko` | 16,126 |
| `name_en` | 16,126 |
| `name_ja` | 14,223 |
| `name_zh_hant` | 13,514 |
| `name_zh_hans` | 13,711 |
| `name_ru` | 32 |
| `name_th` | 32 |
| `region` | 16,126 |
| `category` | 16,126 |
| `address_en` | 15,047 |
| `subway_lines` | 941 |
| `homepage` | 1,040 |
| `source` | 16,126 |
| `ours` | 62 |

Regions: busan, chungbuk, chungnam, daegu, daejeon, gangwon, gwangju, gyeongbuk, gyeonggi, gyeongnam, incheon, jeju, jeonbuk, jeonnam, sejong, seoul, ulsan (our own slugs, e.g. `seoul`, `gyeonggi`, `busan`).
Categories: `attraction`, `course`, `culture`, `event`, `food`, `hub`, `nightview`, `shopping`, `station`, `stay`.

## Columns

- `id` - stable identifier. For TourAPI rows this is the Korea Tourism
  Organization `contentId`.
- `name_ko` - Korean name. **This is the column the dataset exists for.**
- `name_en` / `name_ja` / `name_zh_hant` / `name_zh_hans` - names as published
  by the source in that language.
- `name_ru` / `name_th` - Russian and Thai names. The upstream API has no
  service in these languages, so these are ours (see `ours`).
- `lat` / `lng` - WGS84.
- `region`, `category` - our classification.
- `address_en` - romanized road-name address, where the source provides one.
- `subway_lines` - semicolon separated, stations only.
- `homepage` - official page, where the source provides one.
- `source` - where the row came from (see below).
- `ours` - which name columns we authored rather than received, semicolon
  separated. Empty for most rows.

## Sources and licensing

Rows carry different upstream terms. The `source` column tells you which.

| `source` | Upstream | Terms |
|---|---|---|
| `tourapi` | Korea Tourism Organization TourAPI (Eng/Jpn/Cht/Chs services, data.go.kr 15101753 / 15101760 / 15101769 / 15101764) | No usage restriction stated by the provider |
| `rail-standard` | Korea National Railway, national urban-rail station standard dataset (data.go.kr 15013205) | Korea Open Government License |
| `seoul-nightview` | Seoul Open Data Plaza, night view spots | KOGL Type 1 (attribution required) |
| `curated` | Airports, bus terminals and KTX-only stations added by [Korea Basics](https://basics.aljal.kr) | Ours |
| compiled table | Merged, matched, normalized and released by [Korea Basics](https://basics.aljal.kr) | CC BY 4.0 |

Every name marked in `ours` is our own translation work, as is the compiled
table itself. Keep the upstream attributions above intact alongside ours.

## How to cite

CC BY 4.0 asks for attribution. Copy one of these.

```
Korean Place Names, Multilingual. Korea Basics, 2026.
https://basics.aljal.kr - CC BY 4.0.
Derived from Korea Tourism Organization, Korea National Railway
and Seoul Metropolitan Government open data.
```

```bibtex
@misc{koreabasics_places_2026,
  title        = {Korean Place Names, Multilingual},
  author       = {Korea Basics},
  year         = {2026},
  howpublished = {https://huggingface.co/datasets/hjm1980/korea-places-multilingual},
  url          = {https://basics.aljal.kr},
  note         = {CC BY 4.0. Derived from Korea Tourism Organization TourAPI,
                  Korea National Railway and Seoul Metropolitan Government open data}
}
```

## What this is not

- **Not a rules or regulations dataset.** Entry requirements, customs
  allowances and visa rules live on the site with per-value sources and a
  checked-on date, and are deliberately not published as bulk data: a copy
  stripped of its date is worse than no copy.
- **Not exhaustive.** It is what the upstream ledgers contain as of the sync
  date, not every place in Korea.
- **Not verified place-by-place by us.** Names come from the upstream sources.
  We did not walk them.

Ledgers synced 2026-08-12. Questions, corrections and wrong names:
**contact@aljal.kr**, or the Community tab here. Corrections get folded back into the
site as well, since the same table draws the map.
