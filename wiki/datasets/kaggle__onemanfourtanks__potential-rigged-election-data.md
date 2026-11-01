---
type: "dataset"
id: "kaggle/onemanfourtanks/potential-rigged-election-data"
source: "kaggle"
url: "https://www.kaggle.com/datasets/onemanfourtanks/potential-rigged-election-data"
downloads: 16
summary: "2022년 인천 지역 한국 총선 조기 투표 의심 데이터로 선거 조작 가능성 분석용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[행정·민원]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/onemanfourtanks/potential-rigged-election-data

> dataset · [Kaggle](https://www.kaggle.com/datasets/onemanfourtanks/potential-rigged-election-data)

2022년 인천 지역 한국 총선 조기 투표 의심 데이터로 선거 조작 가능성 분석용 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `From data, can anyone prove whether this is a legitimate vote or not?` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `Early votes and poll-station votes show discrepancy in behavior.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:retrieval = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `Early votes and poll-station votes show discrepancy in behavior.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `Unknown` · 신뢰도 high
- **도메인**: [[행정·민원]] — ner · readme = `Election for Korean Congress April, 2022.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Possibly Rigged Election Data - Early Votes are suspicious` · 신뢰도 low
