---
license: other
license_name: kogl-type-1
license_link: https://www.kogl.or.kr/info/licenseType1.do
language:
- ko
tags:
- weather
- forecast
- korea
- time-series
- public-data
size_categories:
- n<1K
task_categories:
- tabular-regression
---

# Korea Short-Term Weather Forecast (단기예보)

Short-term weather forecast data from the Korea Meteorological
Administration (기상청). Grid-based forecasts with multiple
weather categories (temperature, precipitation, humidity, etc.).

Data sourced via the official data.go.kr API.


## Dataset Summary

- **Records**: 907
- **Features**: 8
- **Source**: [data.go.kr](https://www.data.go.kr/data/15084084/openapi.do)
- **HuggingFace Repo**: [kpubdata/weather-village-forecast](https://huggingface.co/datasets/kpubdata/weather-village-forecast)

## Statistics

| Feature | Mean | Std | Min | Max |
| :--- | ---: | ---: | ---: | ---: |
| `grid_x` | 55.00 | 0.00 | 55 | 55 |
| `grid_y` | 127.00 | 0.00 | 127 | 127 |

## Features

| Feature | Description |
| :--- | :--- |
| `base_date` | Base date of forecast (발표일자, YYYYMMDD) |
| `base_time` | Base time of forecast (발표시각, HHMM) |
| `category` | Weather category code (TMP=기온, POP=강수확률, etc.) |
| `forecast_date` | Forecast target date (예보일자) |
| `forecast_time` | Forecast target time (예보시각) |
| `forecast_value` | Forecast value (예보값) |
| `grid_x` | Grid X coordinate (격자 X) |
| `grid_y` | Grid Y coordinate (격자 Y) |

## Sample Data

| base_date | base_time | category | forecast_date | forecast_time | forecast_value | grid_x | grid_y |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20260101 | 0500 | TMP | 20260101 | 0600 | -11 | 55 | 127 |
| 20260101 | 0500 | UUU | 20260101 | 0600 | 1.7 | 55 | 127 |
| 20260101 | 0500 | VVV | 20260101 | 0600 | -2 | 55 | 127 |
| 20260101 | 0500 | VEC | 20260101 | 0600 | 319 | 55 | 127 |
| 20260101 | 0500 | WSD | 20260101 | 0600 | 2.7 | 55 | 127 |

## Usage

```python
from datasets import load_dataset

ds = load_dataset("kpubdata/weather-village-forecast")
df = ds["train"].to_pandas()
print(df.head())
```

## Source

This dataset was generated using [kpubdata](https://github.com/kpubdata-lab/kpubdata)
from public data APIs on data.go.kr.

데이터 출처: 기상청, 단기예보 조회서비스
(Korea Meteorological Administration — short-term forecast service)
원문: https://www.data.go.kr/data/15084084/openapi.do
이용허락범위: 공공누리 제1유형 (출처표시)

