---
annotations_creators:
- expert-generated
language:
- ko
multilinguality: monolingual
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- multi-class-classification
pretty_name: Credit Rating Prediction Dataset
---

# Credit Rating Prediction Dataset

## Features

- Columns:
  - `credit_rating`
  - `revenue`
  - `operating_profit`
  - `net_income`
  - `total_assets`
  - `total_liabilities`
  - `total_equity`
  - `capital`
  - `operating_cash_flow`
  - `interest_bearing_debt`
  - `debt_ratio`
  - `ROA`
  - `ROE`
  - `asset_turnover_ratio`
  - `interest_to_assets_ratio`
  - `interest_to_revenue_ratio`
  - `cash_flow_to_interest`
  - `interest_to_cash_flow`
  - `log_total_assets`
  - `log_total_liabilities`

- Task: Predict `credit_rating` based on financial indicators

## Splits

| Split      | Size   |
|------------|--------|
| Train      | 44,900 |
| Validation | 100    |
| Test       | 5,000  |

## License

MIT (or your choice)
