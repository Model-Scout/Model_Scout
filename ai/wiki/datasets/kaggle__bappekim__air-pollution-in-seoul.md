---
type: "dataset"
id: "kaggle/bappekim/air-pollution-in-seoul"
source: "kaggle"
url: "https://www.kaggle.com/datasets/bappekim/air-pollution-in-seoul"
downloads: 36843
summary: "서울시 25개 구의 2017~2019년 대기오염 측정 정보를 제공하는 데이터셋입니다."
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
  - "[[환경·기상]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/bappekim/air-pollution-in-seoul

> dataset · [Kaggle](https://www.kaggle.com/datasets/bappekim/air-pollution-in-seoul)

서울시 25개 구의 2017~2019년 대기오염 측정 정보를 제공하는 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `This dataset deals with air pollution measurement information in Seoul, South Korea.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `This dataset is divided into four files.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:retrieval = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `This dataset is divided into four files.` · 신뢰도 low
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC BY-SA 4.0` · 신뢰도 high
- **도메인**: [[환경·기상]] — tag_match · readme, tags = `environment` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `I made a structured dataset by collecting and adjusting various air pollution related datasets provided by the Seoul Metropolitan Government` · 신뢰도 low
