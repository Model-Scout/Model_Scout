---
type: "dataset"
id: "kaggle/visang2022/seoul-citizens-happiness-index-data-for-education"
source: "kaggle"
url: "https://www.kaggle.com/datasets/visang2022/seoul-citizens-happiness-index-data-for-education"
downloads: 50
summary: "서울시 시민 행복지수 데이터를 중학생 교육용으로 편집한 데이터셋입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[행정·민원]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/visang2022/seoul-citizens-happiness-index-data-for-education

> dataset · [Kaggle](https://www.kaggle.com/datasets/visang2022/seoul-citizens-happiness-index-data-for-education)

서울시 시민 행복지수 데이터를 중학생 교육용으로 편집한 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `서울시 행복지수 데이터 분석(교육용)` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `각 속성은 다음과 같은 의미입니다. 1. 분류: 지역 분류 기준 2. 구 이름: 조사 대상 서울시 자치구의 이름 3. 행복지수 종합: 행복 지수에 대한 서울시민 응답점수(단위: 점(10점 만점)) 4. 건강 상태: 건강 상태에 대한 서울시민 응답점수(단위: 점(10점 만점)) 5. 재정` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `각 속성은 다음과 같은 의미입니다. 1. 분류: 지역 분류 기준 2. 구 이름: 조사 대상 서울시 자치구의 이름 3. 행복지수 종합: 행복 지수에 대한 서울시민 응답점수(단위: 점(10점 만점)) 4. 건강 상태: 건강 상태에 대한 서울시민 응답점수(단위: 점(10점 만점)) 5. 재정` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[행정·민원]] — ner · readme = `서울시 행복지수 데이터 분석(교육용)` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `중학교 학생들을 위해 교육용으로 편집하여 업로드한 데이터셋입니다.` · 신뢰도 low
