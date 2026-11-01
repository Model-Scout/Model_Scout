---
license: cc-by-4.0
language:
- ko
tags:
- real-estate
- korea
- seoul
- apartment
- rent
- jeonse
- wolse
- public-data
size_categories:
- 1M<n<10M
task_categories:
- tabular-regression
- tabular-classification
---

# Seoul Apartment Rent (Jeonse/Wolse) Real Transaction Data

Real transaction data for apartment rent (jeonse and wolse) in Seoul, South Korea.
Covers all 25 districts with monthly granularity.

- **전세 (Jeonse)**: Large lump-sum deposit, no monthly rent (monthly_rent = 0)
- **월세 (Wolse)**: Smaller deposit + monthly rent payments

Data sourced from Korea's Ministry of Land, Infrastructure and Transport (국토교통부)
via the official data.go.kr API.


## Dataset Summary

- **Records**: 1,220,346
- **Features**: 19
- **Source**: [data.go.kr](https://www.data.go.kr/data/15126471/openapi.do)
- **HuggingFace Repo**: [kpubdata/seoul-apartment-rent](https://huggingface.co/datasets/kpubdata/seoul-apartment-rent)

## Statistics

| Feature | Mean | Std | Min | Max |
| :--- | ---: | ---: | ---: | ---: |
| `build_year` | 2,004.20 | 12.39 | 1961 | 2025 |
| `deal_year` | 2,022.14 | 1.37 | 2020 | 2024 |
| `deal_month` | 6.49 | 3.50 | 1 | 12 |
| `deal_day` | 15.97 | 8.52 | 1 | 31 |
| `deposit` | 40,214.04 | 35,177.90 | 0 | 1100000 |
| `monthly_rent` | 39.57 | 85.54 | 0 | 4500 |
| `exclusive_area` | 69.41 | 29.38 | 10.3215 | 317.36 |
| `floor` | 9.46 | 6.36 | -4 | 69 |
| `previous_deposit` | 45,387.50 | 33,458.48 | 0 | 630000 |
| `previous_monthly_rent` | 98.44 | 95.22 | 0 | 4100 |

## Features

| Feature | Description |
| :--- | :--- |
| `apartment_name` | Name of the apartment complex (아파트명) |
| `build_year` | Year the building was constructed (건축년도) |
| `deal_year` | Transaction year (거래년도) |
| `deal_month` | Transaction month (거래월) |
| `deal_day` | Transaction day (거래일) |
| `deal_date` | Transaction date in YYYY-MM-DD format (derived) |
| `deposit` | Deposit amount in 만원 (10,000 KRW units) — 보증금 |
| `monthly_rent` | Monthly rent in 만원 (10,000 KRW units) — 월세 (0 = jeonse) |
| `exclusive_area` | Exclusive area in ㎡ (전용면적) |
| `floor` | Floor number (층) |
| `jibun` | Land lot number (지번) |
| `district` | District name within gu (법정동) |
| `region_code` | Administrative district code (시군구코드) |
| `contract_type` | Contract type — 신규/갱신 (new/renewal) |
| `contract_term` | Contract term in months (계약기간) |
| `previous_deposit` | Previous deposit amount for renewal contracts (종전 보증금) |
| `previous_monthly_rent` | Previous monthly rent for renewal contracts (종전 월세) |
| `use_request_right` | Whether tenant used renewal request right (갱신요구권 사용 여부) |
| `road_name` | Road name address (도로명) |

## Sample Data

| apartment_name | build_year | deal_year | deal_month | deal_day | deposit | monthly_rent | exclusive_area | floor | jibun | district | region_code | contract_type | contract_term | previous_deposit | previous_monthly_rent | use_request_right | road_name | deal_date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 현대 | 2000 | 2020 | 1 | 30 | 38000 | 0 | 60.0 | 13 | 82 | 무악동 | 11110 | None | None | None | None | None | 통일로 246-20 | 2020-01-30 |
| 창신쌍용1 | 1992 | 2020 | 1 | 13 | 32000 | 0 | 79.87 | 3 | 702 | 창신동 | 11110 | None | None | None | None | None | 동망산길 19 | 2020-01-13 |
| 효성쥬얼리시티 | 2006 | 2020 | 1 | 17 | 45000 | 0 | 98.39 | 7 | 48-2 | 인의동 | 11110 | None | None | None | None | None | 종로 183 | 2020-01-17 |
| 경희궁자이(3단지) | 2017 | 2020 | 1 | 4 | 89900 | 0 | 84.944 | 10 | 233 | 평동 | 11110 | None | None | None | None | None | 경교장길 35 | 2020-01-04 |
| 경희궁자이(1단지) | 2017 | 2020 | 1 | 23 | 11168 | 37 | 39.0561 | 5 | 211 | 행촌동 | 11110 | None | None | None | None | None | 송월길 130 | 2020-01-23 |

## Usage

```python
from datasets import load_dataset

ds = load_dataset("kpubdata/seoul-apartment-rent")
df = ds["train"].to_pandas()
print(df.head())
```

## Source

This dataset was generated using [kpubdata](https://github.com/yeongseon/kpubdata)
from public data APIs on data.go.kr.

데이터 출처: 국토교통부 아파트 전월세 실거래가 자료
(Ministry of Land, Infrastructure and Transport — Apartment Rent Transaction Data)

