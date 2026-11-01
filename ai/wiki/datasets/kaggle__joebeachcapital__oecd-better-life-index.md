---
type: "dataset"
id: "kaggle/joebeachcapital/oecd-better-life-index"
source: "kaggle"
url: "https://www.kaggle.com/datasets/joebeachcapital/oecd-better-life-index"
downloads: 563
summary: "OECD의 11가지 주제로 국가별 삶의 질과 물질적 생활 조건을 비교하는 지표 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[행정·민원]]"
dataset_role:
  - "[[서비스 데이터]]"
---
# kaggle/joebeachcapital/oecd-better-life-index

> dataset · [Kaggle](https://www.kaggle.com/datasets/joebeachcapital/oecd-better-life-index)

OECD의 11가지 주제로 국가별 삶의 질과 물질적 생활 조건을 비교하는 지표 데이터입니다.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `This Index allows you to compare well-being across countries, based on 11 topics the OECD has identified as essential` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `Percentage of the population The value is an average of data available between 2015-20` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:retrieval = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `Percentage of the population The value is an average of data available between 2015-20` · 신뢰도 low
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `Database: Open Database, Contents: Database Contents` · 신뢰도 high
- **도메인**: [[행정·민원]] — tag_match · readme, tags = `government` · 신뢰도 medium
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `Latest Better Life Index from OECD` · 신뢰도 low
