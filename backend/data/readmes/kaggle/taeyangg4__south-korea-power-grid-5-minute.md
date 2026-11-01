# South Korea Power Grid 5-Minute Data 2015-2026

1B+ KPX rows in Parquet + July 2026 CSV sample

## Analysis-ready South Korea power-grid operations data

The current release provides **1,008,249,180 normalized Korea Power Exchange (KPX) five-minute rows from 2015-08 through 2026-07** in one compact ZSTD Parquet file. A separate UTF-8 CSV contains the complete **2026-07 month** across all three sources (10,060,444 rows) for CSV-only tools and quick interoperability tests. Both files use the columns `timestamp`, `source`, `generator_id`, and `value_mw`.

Use `south_korea_power_grid_5min.parquet` for the full history. The July 2026 CSV is intentionally a bounded compatibility slice rather than a duplicate 50+ GB copy of the entire table. For exploratory analysis, notebooks, DuckDB, Polars, Spark, or PyArrow, use Parquet and filter by source/time before materializing rows.

### Source semantics

`source=demand` stores the five-minute system demand forecast and has no generator ID. `source=dispatch` stores generator economic-dispatch BASEPOINT targets. `source=state_estimation` stores state-estimated generator output. All values are MW. Generator codes remain source-native and are not joined by a guessed crosswalk.

### Data-quality policy

Missing timestamps remain missing, eight unavailable official source-month attachments are documented explicitly, exact duplicates are removed only under the documented candidate-key rule, and one ambiguous 2016-06 state-estimation timestamp with two conflicting full-generator snapshots is excluded rather than arbitrarily selecting a version. Timestamps are timezone-naive because verified timezone metadata is not present in the source files.

### Provenance

The original provider is **Korea Power Exchange (KPX), Republic of Korea**. This is a cleaned derivative dataset, not an official KPX distribution channel. Official KPX/data.go.kr source links are recorded in the provenance field; Kaggle license metadata remains `other`.

출처: Kaggle (taeyangg4/south-korea-power-grid-5-minute)
태그: asia, government, energy, time series analysis, tabular, electricity
라이선스: Other (specified in description)
수정일: 2026-09-11T04:18:27.137Z
