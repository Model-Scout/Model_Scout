---
type: "dataset"
id: "kaggle/jericbustos/2016-2025-kdramas-dataset"
source: "kaggle"
url: "https://www.kaggle.com/datasets/jericbustos/2016-2025-kdramas-dataset"
downloads: 170
summary: "2016년부터 2025년까지 한국 드라마 285편의 방송 정보와 평점을 담은 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[문화·관광]]"
---
# kaggle/jericbustos/2016-2025-kdramas-dataset

> dataset · [Kaggle](https://www.kaggle.com/datasets/jericbustos/2016-2025-kdramas-dataset)

2016년부터 2025년까지 한국 드라마 285편의 방송 정보와 평점을 담은 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Average user rating (on a scale of 1-10)` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `Studying the relationship between episode length and ratings` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Analyzing rating trends across different years` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:embedding, task:retrieval = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Average user rating (on a scale of 1-10)` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `Korean Drama Dataset (2016-2025)` · 신뢰도 low
