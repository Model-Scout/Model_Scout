# SeoulMMOD Benchmark Dataset

Large-scale public benchmark for citywide multimodal mobility in Seoul.

# SeoulMMOD Dataset

SeoulMMOD contains hourly multimodal origin-destination flows within Seoul
from 2023 to 2025. It covers six urban transport modes at district and
subdistrict scales, with aligned administrative metadata and contextual data.


## Files

| File | Description |
|---|---|
| `raw/od_flow_2023.parquet` | Hourly multimodal OD flow records for 2023. |
| `raw/od_flow_2024.parquet` | Hourly multimodal OD flow records for 2024. |
| `raw/od_flow_2025.parquet` | Hourly multimodal OD flow records for 2025. |
| `district_metadata.csv` | District code, name, and representative coordinates. |
| `subdistrict_metadata.csv` | Subdistrict code, name, parent district code, and representative coordinates. |
| `district_boundaries.geojson` | District administrative boundary geometries. |
| `subdistrict_boundaries.geojson` | Subdistrict administrative boundary geometries. |
| `calendar.csv` | Weekend and holiday indicators. |
| `district_poi.csv` | District-level POI category counts based on 2025 data. |
| `subdistrict_poi.csv` | Subdistrict-level POI category counts based on 2025 data. |
| `rainfall/seoul_rain_hourly_2023.csv` | Hourly district rainfall for 2023. |
| `rainfall/seoul_rain_hourly_2024.csv` | Hourly district rainfall for 2024. |
| `rainfall/seoul_rain_hourly_2025.csv` | Hourly district rainfall for 2025. |

## OD Flow Schema

| Attribute | Description | Values |
|---|---|---|
| `date` | Calendar date. | `YYYY-MM-DD` |
| `st_hour` | Hour of day. | 0-23 |
| `origin` | Origin subdistrict code. | District-scale datasets use the first five digits |
| `dest` | Destination subdistrict code. | District-scale datasets use the first five digits |
| `mode` | Transport mode code. | 4 metro bus, 5 local bus, 6 subway, 7 walk, 8 car, 9 other |
| `flow` | Estimated OD flow volume. | Nonnegative real number |
| `avg_dist_m` | Average travel distance in meters. | Nonnegative real number |
| `avg_time_min` | Average travel time in minutes. | Nonnegative real number |

## Metadata

| File | Main Attributes |
|---|---|
| `district_metadata.csv` | `district_cd`, `district_name`, `lon`, `lat` |
| `subdistrict_metadata.csv` | `subdistrict_cd`, `subdistrict_name`, `district_cd`, `district_name`, `lon`, `lat` |
| `district_poi.csv` | `district_cd`, `district_name`, POI category counts |
| `subdistrict_poi.csv` | `subdistrict_cd`, `subdistrict_name`, `district_cd`, `district_name`, POI category counts |
| `calendar.csv` | `date`, `day_of_week`, `is_weekend`, `is_holiday`, `is_workday`, `holiday_name` |
| `rainfall/seoul_rain_hourly_*.csv` | `timestamp`, `district_cd`, `rain_mm` |

## License

The original Seoul Open Data Plaza records remain under the Korea Open
Government License (KOGL) Type 1. The processed SeoulMMOD benchmark
release is distributed under CC BY-NC 4.0, with attribution to the
original public data source.

출처: Kaggle (muutyy/seoulmmod)
태그: 
라이선스: Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)
수정일: 2026-05-07T01:46:04.863Z
