---
type: "dataset"
id: "kaggle/parkseungjoon/national-assembly-of-korea-minutes-database"
source: "kaggle"
url: "https://www.kaggle.com/datasets/parkseungjoon/national-assembly-of-korea-minutes-database"
downloads: 47
summary: "국회 상임위 회의록 데이터를 정리하여 의원별 발언 분석에 활용하는 데이터셋입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
  - "[[정보 추출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
domain:
  - "[[행정·민원]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/parkseungjoon/national-assembly-of-korea-minutes-database

> dataset · [Kaggle](https://www.kaggle.com/datasets/parkseungjoon/national-assembly-of-korea-minutes-database)

국회 상임위 회의록 데이터를 정리하여 의원별 발언 분석에 활용하는 데이터셋입니다.

## 분류

- **작업**: [[정보 추출]] — ner · readme = `누가(국회의원), 어디서(회의), 무슨 발언을 하였는지 정리하였습니다.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:information_extraction = `국회 상임위 회의록 데이터` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `누가(국회의원), 어디서(회의), 무슨 발언을 하였는지 정리하였습니다.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **도메인**: [[행정·민원]] — tag_match · readme, tags = `government` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `2021년 1학기 Machine Learning and Deep Learning for Data Science 수업 프로젝트 과정에서 정리한 데이터입니다.` · 신뢰도 low
