---
license: cc-by-4.0
language:
- ko
- en
tags:
- transportation
- bicycle
- seoul
- public-data
- korea
- tabular
task_categories:
- tabular-regression
size_categories:
- 100K-1M
---

# Seoul Bike Ttareungi Monthly Usage (서울 따릉이 월별 이용정보)

Monthly usage statistics for Seoul's public bike-sharing system "Ttareungi" (따릉이),
aggregated by station, subscription type, and age group.

**Important**: Text values (`rent_type`, `station_name`, `age_group`) are in Korean.
Column names are in English for global accessibility.

## Dataset Summary

| | |
|---|---|
| Records | ~119,000 |
| Features | 11 |
| Period | Multiple months (YYYYMM format) |
| Source | [Seoul Open Data Plaza](https://data.seoul.go.kr/) |

## Features

| Feature | Description |
|---|---|
| `rent_month` | Rental year-month in YYYYMM format (대여 년월) |
| `rent_type` | Subscription type: 정기권 (monthly pass), 일일권 (daily pass), etc. |
| `station_no` | Station number (대여소 번호) |
| `station_name` | Station name in Korean (대여소 이름) |
| `gender_code` | Gender code (성별 코드). May be null. |
| `age_group` | Age group: ~10대, 20대, 30대, etc. (연령대) |
| `use_count` | Number of rentals (이용 건수) |
| `exercise_kcal` | Total exercise amount in kcal (운동량) |
| `carbon_reduction_kg` | Total carbon reduction in kg (탄소 절감량) |
| `distance_m` | Total distance traveled in meters (이동 거리) |
| `duration_min` | Total duration in minutes (이동 시간) |

## Usage

```python
from datasets import load_dataset

ds = load_dataset("kpubdata/seoul-bike-rent-month")
df = ds["train"].to_pandas()
print(df.head())
```

Or collect fresh data with [kpubdata](https://github.com/yeongseon/kpubdata):

```python
from kpubdata import Client

client = Client.from_env()
ds = client.dataset("seoul.bike_rent_month")
result = ds.list(RENT_NM="202604", page_size=1000)
```

## Source

This dataset was generated using [kpubdata](https://github.com/yeongseon/kpubdata)
from public data APIs on [data.seoul.go.kr](https://data.seoul.go.kr/).

## Legal & Attribution

This dataset uses "서울시 공공자전거 이용정보(월별)" published by
the Seoul Metropolitan Government (서울특별시) under
Korea Open Government License Type 1 (공공누리 제1유형).

**Korean attribution (한국어 출처표시)**:

> 본 저작물은 '서울특별시'에서 작성하여 공공누리 제1유형으로 개방한
> '서울시 공공자전거 이용정보(월별)'를 이용하였으며, 해당 저작물은
> 'data.seoul.go.kr'에서 무료로 다운받으실 수 있습니다.

License: CC-BY-4.0
