---
type: "dataset"
id: "kaggle/seventyfivebyte/seoul-daily-hourly-traffic-accident-status"
source: "kaggle"
url: "https://www.kaggle.com/datasets/seventyfivebyte/seoul-daily-hourly-traffic-accident-status"
downloads: 108
summary: "서울시 행정구역별 2017-2019년 일별 시간대별 교통사고 현황 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[뉴스·미디어]]"
  - "[[교통·모빌리티]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/seventyfivebyte/seoul-daily-hourly-traffic-accident-status

> dataset · [Kaggle](https://www.kaggle.com/datasets/seventyfivebyte/seoul-daily-hourly-traffic-accident-status)

서울시 행정구역별 2017-2019년 일별 시간대별 교통사고 현황 데이터입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Number of Accidents, Number of Fatalities, Number of Severe Injuries, Number of Minor Injuries, Number of Reported Injuries` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Seoul City Daily Hourly Traffic Accident Status by Administrative District (2017-2019)` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `Seoul City Daily Hourly Traffic Accident Status by Administrative District (2017-2019)` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:retrieval = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `Number of Accidents, Number of Fatalities, Number of Severe Injuries, Number of Minor Injuries, Number of Reported Injuries` · 신뢰도 low
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `Unknown` · 신뢰도 high
- **도메인**: [[뉴스·미디어]] — tag_match · tags = `news` · 신뢰도 medium
- **도메인**: [[교통·모빌리티]] — ner · readme = `Seoul City Daily Hourly Traffic Accident Status by Administrative District (2017-2019)` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Seoul City Daily Hourly Traffic Accident Status by Administrative District (2017-2019)` · 신뢰도 low
