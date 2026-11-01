---
type: "dataset"
id: "go2abroad-sop/go2abroad-sop-catalog"
source: "huggingface"
url: "https://huggingface.co/datasets/go2abroad-sop/go2abroad-sop-catalog"
downloads: 289
summary: "GO2ABROAD SOP는 180개국 419개 산업 분류의 표준 운영 절차를 다국어로 제공하는 산업 규정 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[정보 추출]]"
  - "[[문서 검색]]"
  - "[[표 데이터 예측]]"
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
domain:
  - "[[일반]]"
dataset_role:
  - "[[서비스 데이터]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# go2abroad-sop/go2abroad-sop-catalog

> dataset · [Hugging Face](https://huggingface.co/datasets/go2abroad-sop/go2abroad-sop-catalog)

GO2ABROAD SOP는 180개국 419개 산업 분류의 표준 운영 절차를 다국어로 제공하는 산업 규정 데이터입니다.

## 분류

- **작업**: [[정보 추출]] — ner · readme = `provides compact global metadata indexes, verified engineering tolerances, international compliance codes (ISO, DIN, OSHA, ASME, IEC)` · 신뢰도 low
- **작업**: [[문서 검색]] — metadata · readme, task_categories = `text-retrieval` · 신뢰도 medium
- **작업**: [[표 데이터 예측]] — metadata · task_categories = `tabular-classification` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — task_rule · task:tabular_prediction = `table` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:information_extraction, task:retrieval = `Standard Operating Procedures across 180+ jurisdictions and 419 UN ISIC Rev.4 industrial classifications` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `compact global metadata indexes, verified engineering tolerances, international compliance codes` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `11 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Global Industrial Operating Procedures Core` · 신뢰도 low
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `This open dataset repository provides high-level index metadata, quantitative tolerances, and regulatory codes.` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
