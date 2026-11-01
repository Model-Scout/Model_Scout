---
type: "dataset"
id: "kaggle/shaido978/novel-dataset"
source: "kaggle"
url: "https://www.kaggle.com/datasets/shaido978/novel-dataset"
downloads: 94
summary: "www.novelupdates.com의 번역 소설 통계와 연관 정보를 담은 데이터셋입니다."
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
# kaggle/shaido978/novel-dataset

> dataset · [Kaggle](https://www.kaggle.com/datasets/shaido978/novel-dataset)

www.novelupdates.com의 번역 소설 통계와 연관 정보를 담은 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `Both individual novel statistics such as the number of chapters and ranking as well as relations to other novels are available.` · 신뢰도 low
- **작업**: [[표 데이터 예측]] — ner · readme = `Statistics and associations between translated novels from www.novelsupdates.com` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme, task:tabular_prediction = `Dataset columns:

- General Information
- Novel ID
- Name
- Associated Names
- Original Langauge
- Author / Authors
- Genres
- Tags
- Publishing Information
- S` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:retrieval = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `Dataset columns:

- General Information
- Novel ID
- Name
- Associated Names
- Original Langauge
- Author / Authors
- Genres
- Tags
- Publishing Information
- S` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `MIT` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `Dataset of translated novels from novelupdates (https://www.novelupdates.com) containing information about translated novels.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Dataset of translated novels from novelupdates (https://www.novelupdates.com) containing information about translated novels.` · 신뢰도 low
