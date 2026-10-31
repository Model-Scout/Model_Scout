---
type: "dataset"
id: "openfoodfacts/product-database"
source: "huggingface"
url: "https://huggingface.co/datasets/openfoodfacts/product-database"
downloads: 50378
summary: "Open Food Facts는 전 세계 식품 제품의 성분, 알레르기 정보, 영양 성분 등을 담은 공개 식품 데이터베이스입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
  - "[[조건부 이용]]"
domain:
  - "[[상거래·상품]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# openfoodfacts/product-database

> dataset · [Hugging Face](https://huggingface.co/datasets/openfoodfacts/product-database)

Open Food Facts는 전 세계 식품 제품의 성분, 알레르기 정보, 영양 성분 등을 담은 공개 식품 데이터베이스입니다.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `Open Food Facts is a database of food products with ingredients, allergens, nutrition facts and all the tidbits of information we can find on product labels.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:retrieval = `Open Food Facts is a database of food products with ingredients, allergens, nutrition facts and all the tidbits of information we can find on product labels.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Open Food Facts is a database of food products with ingredients, allergens, nutrition facts and all the tidbits of information we can find on product labels.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `57 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `odbl` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `agpl-3.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `Open Food Facts is a database of food products with ingredients, allergens, nutrition facts and all the tidbits of information we can find on product labels.` · 신뢰도 low
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
