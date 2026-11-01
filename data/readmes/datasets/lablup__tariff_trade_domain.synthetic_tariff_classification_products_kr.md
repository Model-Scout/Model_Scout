---
language:
  - ko
  - en
license: cc-by-4.0
pretty_name: Synthetic Tariff Classification Products (Korean)
tags:
  - tariff
  - hs-code
  - product-classification
  - synthetic
  - korean
  - customs
  - trade
annotations_creators:
  - machine-generated
language_creators:
  - machine-generated
multilinguality:
  - multilingual
size_categories:
  - 10K<n<100K
task_categories:
  - text-classification
task_ids:
  - multi-class-classification
source_datasets:
  - original
configs:
  - config_name: default
    data_files:
      - split: train
        path: data/train-00000.parquet
dataset_info:
  features:
    - name: case_id
      dtype: string
    - name: source
      dtype: string
    - name: generation_model
      dtype: string
    - name: product_name
      dtype: string
    - name: hs_code_clean
      dtype: string
    - name: hs_code_declared
      dtype: string
    - name: product_description
      dtype: string
    - name: decision_reason
      dtype: string
    - name: decision_date
      dtype: string
    - name: created_at
      dtype: string
    - name: document_id
      dtype: string
  config_name: default
  splits:
    - name: train
      num_bytes: 15139272
      num_examples: 27562
  download_size: 15139272
  dataset_size: 15139272
---

# Synthetic Tariff Classification Products (Korean)

A synthetic dataset of Korean product descriptions paired with their HS (Harmonized System) tariff codes and classification rationales, generated to support training and evaluation of customs classification models. All entries are LLM-generated; no real personal or confidential customs records are included.

## Dataset Description

Korean customs classification requires assigning a 10-digit HS code to an imported or exported product. This dataset provides:
- A **product name** and **detailed product description** (mostly Korean, some English)
- The **10-digit HS code** (`hs_code_clean`) as the classification target
- A **decision rationale** (`decision_reason`) referencing the Korean tariff schedule (관세율표) and HS explanatory notes (해설서)

The data covers **94 HS chapters** and **10,592 unique 10-digit HS codes** across all major trade categories.

## Data Fields

| Field | Type | Nullable | Description |
|-------|------|----------|-------------|
| `case_id` | string | no | Unique identifier for the classification case |
| `source` | string | no | Pipeline tag: `synthetic_gemma` or `synthetic_gemma3` |
| `generation_model` | string | no | LLM used to generate the entry: `gemma3` or `gpt-5-mini` |
| `product_name` | string | no | Short product name (Korean / English) |
| `hs_code_clean` | string | no | 10-digit target HS code (e.g. `0201100000`) |
| `hs_code_declared` | string | yes | Declared HS code at import — present only in gpt-5-mini batch (16.7% of rows) |
| `product_description` | string | no | Detailed product description used as model input |
| `decision_reason` | string | no | HS code rationale citing tariff schedule provisions (관세율표 해석) |
| `decision_date` | string | yes | Date of classification decision — present only in gpt-5-mini batch (16.7% of rows) |
| `created_at` | string | no | Generation timestamp (`YYYY-MM-DD HH:MM:SS`) |
| `document_id` | string | no | Source document reference if any; empty string when not applicable |

## Examples

| `product_name` | `hs_code_clean` | `product_description` (truncated) | `decision_reason` (truncated) |
|----------------|-----------------|-----------------------------------|-------------------------------|
| 냉동 돼지 간 | 0303911000 | 도축된 돼지의 간을 세척, 절단하여 -18℃ 이하에서 냉동. 무게 약 500g, 진공 포장 유통… | 돼지 간을 냉동한 것으로 관세율표제0303호의 냉동 어류가 아닌, 제0206호 식용 설육에 해당… |
| 냉동 명란젓 (명태알젓) | 0303912010 | 명태의 알을 소금에 절인 후 -18℃ 이하 냉동 보관. 직경 2~3mm, 염도 7~9%, 500g 진공 포장… | 명태 알을 냉동한 것으로 관세율표제0303호 냉동 어류에 해당하며, 소금 절임 처리로 인해 부호 0303.91… |
| 미국산 냉장 소 도체 | 0201100000 | 미국산 홀스타인 소 도체로, 도축 후 냉장 보관 출하. 무게 약 220kg, 뼈 미제거 상태, 붉은 육색, 균일한 지방층 분포. 진공 포장되지 않은 신선 상태로 유통… | 뼈가 제거되지 않은 소 도체로 냉장 보관된 육류 제품. 관세율표 제02류는 식용설육 및 육류를 분류하며, 제0201호는 소고기 신선·냉장을 규정. 도체는 뼈 포함 전체 상태이므로 제0201.10호(carcasses and half-carcasses)에 분류… |

## Generation Details

| `generation_model` | `source` tag | Row count | Generated |
|--------------------|--------------|-----------|-----------|
| `gemma3` | `synthetic_gemma` | 22,436 | ~2025-11-03 |
| `gemma3` | `synthetic_gemma3` | 4,616 | ~2025-11-17 |
| `gpt-5-mini` | `synthetic_gemma3` | 510 | ~2025-10-30 |
| **Total** | | **27,562** | |

The `source` field preserves the original pipeline batch tag. Use `generation_model` to filter by the LLM backend. The `gpt-5-mini` batch (510 rows) additionally has `hs_code_declared` and `decision_date` populated.

## HS Code Coverage

- **94 HS chapters** covered (out of 97 total)
- **10,592 unique 10-digit HS codes**
- Chapters with highest representation: Ch. 03 (fish & seafood, 1,208 rows), Ch. 90 (optical/precision instruments, 835 rows), Ch. 12 (oil seeds, 456 rows)
- Full chapter range: 01–97

## Usage

```python
from datasets import load_dataset

ds = load_dataset("lablup/synthetic_tariff_classification_products_kr")
print(ds["train"][0])
# {
#   'case_id': '88880299207101e992',
#   'source': 'synthetic_gemma',
#   'generation_model': 'gemma3',
#   'product_name': '미국산 냉장 소 도체',
#   'hs_code_clean': '0201100000',
#   'product_description': '미국에서 생산된 홀스타인 품종의 소 도체로...',
#   'decision_reason': '본 물품은 뼈가 제거되지 않은 상태의 소 도체로서...',
#   ...
# }
```

Filter by generation model:
```python
gemma_only     = ds["train"].filter(lambda x: x["generation_model"] == "gemma3")
gpt_mini_only  = ds["train"].filter(lambda x: x["generation_model"] == "gpt-5-mini")
```

Use only rows that have HS code declared (for declared-vs-actual studies):
```python
with_declared = ds["train"].filter(lambda x: x["hs_code_declared"] is not None)
```

## Data Splits

| Split | Rows |
|-------|------|
| train | 27,562 |

## Limitations

- All product descriptions and rationales are LLM-generated and may contain factual errors or hallucinated provisions
- HS code assignments have not been verified by licensed customs brokers
- Coverage is skewed toward categories present in the Korean customs reference database used as a seed

## License

[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)
