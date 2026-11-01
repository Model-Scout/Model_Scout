---
type: "dataset"
id: "kaggle/romainfonta2/kpop-song-rankings"
source: "kaggle"
url: "https://www.kaggle.com/datasets/romainfonta2/kpop-song-rankings"
downloads: 2225
summary: "2010년부터 2023년까지 Kpop 노래 주간 순위 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[문서 검색]]"
  - "[[표 데이터 예측]]"
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
  - "[[문화·관광]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/romainfonta2/kpop-song-rankings

> dataset · [Kaggle](https://www.kaggle.com/datasets/romainfonta2/kpop-song-rankings)

2010년부터 2023년까지 Kpop 노래 주간 순위 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `Ranking of kpop songs since 2010` · 신뢰도 low
- **작업**: [[표 데이터 예측]] — ner · readme = `The data is present in one csv file with the following columns : - year : Year of the ranking (2010 to 2023) - time : Week of the year of the ranking (1 to 53) ` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme, task:tabular_prediction = `The data is present in one csv file with the following columns` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:retrieval = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `The data is present in one csv file with the following columns` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `Database: Open Database, Contents: Database Contents` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `Ranking of kpop songs since 2010` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The data is present in one csv file with the following columns` · 신뢰도 low
