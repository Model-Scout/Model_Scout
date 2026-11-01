---
type: "dataset"
id: "kaggle/visang2022/seoul-tropical-night-days-data-for-education"
source: "kaggle"
url: "https://www.kaggle.com/datasets/visang2022/seoul-tropical-night-days-data-for-education"
downloads: 8
summary: "서울 열대야 일수 데이터를 중학생 교육용으로 한글 편집한 기상 데이터셋입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
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
  - "[[환경·기상]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/visang2022/seoul-tropical-night-days-data-for-education

> dataset · [Kaggle](https://www.kaggle.com/datasets/visang2022/seoul-tropical-night-days-data-for-education)

서울 열대야 일수 데이터를 중학생 교육용으로 한글 편집한 기상 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `서울 열대야 일수 데이터 분석(교육용)` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `1. 연도: 조사한 연도
2. 1~12월: 조사한 월
3. 연합계: 해당 연도 열대야 일수 합계
4. 순위: 연합계 열대야 일수가 많은 순위` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `1. 연도: 조사한 연도
2. 1~12월: 조사한 월
3. 연합계: 해당 연도 열대야 일수 합계
4. 순위: 연합계 열대야 일수가 많은 순위` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[환경·기상]] — ner · readme = `기상청의 '기상자료개방포털(https://data.kma.go.kr/)'에 업로드된 [기후통계분석] - [열대야일수] 데이터` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `교육용으로 한글로 편집하여 업로드한 데이터셋입니다.` · 신뢰도 low
