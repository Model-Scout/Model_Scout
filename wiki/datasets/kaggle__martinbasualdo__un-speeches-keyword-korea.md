---
type: "dataset"
id: "kaggle/martinbasualdo/un-speeches-keyword-korea"
source: "kaggle"
url: "https://www.kaggle.com/datasets/martinbasualdo/un-speeches-keyword-korea"
downloads: 11
summary: "UN 디지털 도서관에서 'Korea' 키워드로 수집한 연설문 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[행정·민원]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/martinbasualdo/un-speeches-keyword-korea

> dataset · [Kaggle](https://www.kaggle.com/datasets/martinbasualdo/un-speeches-keyword-korea)

UN 디지털 도서관에서 'Korea' 키워드로 수집한 연설문 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Each downloaded record contains speeches from various countries, so the text of each PDF was partitioned into the individual speeches it includes.` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `This dataset is a result of a WebScrap of the [UN Digital Library]` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:retrieval = `Each downloaded record contains speeches` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Each downloaded record contains speeches` · 신뢰도 low
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `MIT` · 신뢰도 high
- **도메인**: [[행정·민원]] — ner · readme = `UN speeches. Keyword: "Korea"` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is a result of a WebScrap of the [UN Digital Library]` · 신뢰도 low
