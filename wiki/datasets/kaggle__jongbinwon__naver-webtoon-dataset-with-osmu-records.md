---
type: "dataset"
id: "kaggle/jongbinwon/naver-webtoon-dataset-with-osmu-records"
source: "kaggle"
url: "https://www.kaggle.com/datasets/jongbinwon/naver-webtoon-dataset-with-osmu-records"
downloads: 134
summary: "네이버 웹툰과 OSMU 기록을 포함한 메타데이터를 수집한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[문화·관광]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/jongbinwon/naver-webtoon-dataset-with-osmu-records

> dataset · [Kaggle](https://www.kaggle.com/datasets/jongbinwon/naver-webtoon-dataset-with-osmu-records)

네이버 웹툰과 OSMU 기록을 포함한 메타데이터를 수집한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `It labels each webtoon to indicate whether it has been utilized as an OSMU (One-Source Multi-Use).` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `The dataset compiles metadata from Naver webtoons` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `It labels each webtoon to indicate whether it has been utilized as an OSMU (One-Source Multi-Use).` · 신뢰도 low
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `Apache 2.0` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `dataset crawled from NAVER Webtoon(Korea) with its OSMU records` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset was created as part of the final project for the 23-2 Machine Learning course (@Korea University).` · 신뢰도 low
