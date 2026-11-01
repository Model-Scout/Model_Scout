---
type: "dataset"
id: "kaggle/fliarbi/open-company-database"
source: "kaggle"
url: "https://www.kaggle.com/datasets/fliarbi/open-company-database"
downloads: 35
summary: "웹사이트, 국가, 도시, 산업, 설립연도, 상태, 규모 정보를 포함한 500만 기업 데이터베이스입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[상거래·상품]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/fliarbi/open-company-database

> dataset · [Kaggle](https://www.kaggle.com/datasets/fliarbi/open-company-database)

웹사이트, 국가, 도시, 산업, 설립연도, 상태, 규모 정보를 포함한 500만 기업 데이터베이스입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Each record is classified into a sector, industry and business model by Radar's own models` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Companies with website, country, city, sector, founding year, status and size` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:retrieval = `Companies with website, country, city, sector, founding year, status and size` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Companies with website, country, city, sector, founding year, status and size` · 신뢰도 low
- **상업 이용**: [[비상업 전용]] — metadata · license = `CC BY-NC-SA 4.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `Companies with website, country, city, sector, founding year, status and size` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This file is a 2% sample: 100,000 of 4,863,273 companies.` · 신뢰도 low
