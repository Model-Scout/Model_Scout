---
type: "dataset"
id: "kaggle/crxxom/manhwa-dataset"
source: "kaggle"
url: "https://www.kaggle.com/datasets/crxxom/manhwa-dataset"
downloads: 677
summary: "한국 만화인 만화(Manhwa) 2천여 편의 상세 정보와 설명을 포함한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[정보 추출]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[문화·관광]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/crxxom/manhwa-dataset

> dataset · [Kaggle](https://www.kaggle.com/datasets/crxxom/manhwa-dataset)

한국 만화인 만화(Manhwa) 2천여 편의 상세 정보와 설명을 포함한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `genres` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `detailed descriptions and information regarding the manhwa` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `help you discover underrated manhwa!` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:information_extraction, task:retrieval = `title of the manhwa` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `detailed descriptions and information regarding the manhwa` · 신뢰도 low
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `Unknown` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `arts and entertainment, comics and animation, anime and manga, korea, korean` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset contains all manhwa from MAL, including detailed descriptions and information` · 신뢰도 low
