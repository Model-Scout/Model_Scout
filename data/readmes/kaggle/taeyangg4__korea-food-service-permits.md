# South Korea Food-Service Permits - Snapshot

3,010,802 restaurant, cafe and bakery permit records nationwide

## What this dataset is

A nationwide **current snapshot** of South Korean local-government food-service permits from Ministry of the Interior and Safety / LOCALDATA sources. It contains **3,010,802 records x 26 columns** across three categories: general restaurants, rest cafes, and bakeries. **This is not a historical time series or a lossless lifecycle event log.**

## Coverage

- General restaurants: **2,295,369** records
- Rest cafes: **645,952** records
- Bakeries: **69,481** records
- Nationwide current snapshot: **3,010,802** records

## Main files

- `korea_food_service_permits.csv` - 1.40 GB UTF-8 CSV for broad compatibility
- `korea_food_service_permits.parquet` - 165 MB typed ZSTD Parquet for fast analytics
- Both files contain the **same 3,010,802 rows and the same 26 columns**
- `DATA_DICTIONARY.md`, `schema.json`, `SOURCES.md`, and `release-manifest.json` document every field and the release lineage

## Good starting points

Regional restaurant-market mapping, permit-status analysis, business-type profiling, address/geospatial preprocessing, public-sector data engineering, and data-quality research.

Public Quickstart / EDA notebook: https://www.kaggle.com/code/taeyangg4/korea-food-service-permits-3m-row-quickstart

## Important interpretation limits

- `management_number` is a bounded continuity candidate, **not an asserted official primary key**.
- `permit_date` is an administrative permit date, **not necessarily the physical opening date**.
- `closure_date` is contextual and **not treated as an irreversible terminal event**.
- Source status `03` is reversible in observed evidence; status `05` remains unresolved.
- `source_coordinate_x` / `source_coordinate_y` use **EPSG:5174** for this verified snapshot.
- The separately derived WGS84 sidecar and partial history are not included.

## Provenance

Official source identifiers and links are listed in `SOURCES.md`. The project repository is https://github.com/TaeyanG4/korea-business-lifecycle.

## License / reuse

Kaggle license metadata is set to `Other` so this project does not claim to relicense upstream public records. The three official Public Data Portal source pages currently display `이용허락범위 제한 없음` (no restriction on the permitted-use scope). Attribution and source links are preserved in `SOURCES.md`.

출처: Kaggle (taeyangg4/korea-food-service-permits)
태그: business, government, geospatial analysis, food, restaurants
라이선스: Other (specified in description)
수정일: 2026-09-07T17:53:16.360Z
