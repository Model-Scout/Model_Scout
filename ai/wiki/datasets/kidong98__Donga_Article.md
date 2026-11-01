---
type: "dataset"
id: "kidong98/Donga_Article"
source: "huggingface"
url: "https://huggingface.co/datasets/kidong98/Donga_Article"
downloads: 111
summary: "동아일보 2023~2024년 기사 제목, 본문, NER 포함 데이터셋으로 관련기사 검색·추천에 활용됨"
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[정보 추출]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[뉴스·미디어]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# kidong98/Donga_Article

> dataset · [Hugging Face](https://huggingface.co/datasets/kidong98/Donga_Article)

동아일보 2023~2024년 기사 제목, 본문, NER 포함 데이터셋으로 관련기사 검색·추천에 활용됨

## 분류

- **작업**: [[임베딩]] — metadata · task_categories = `feature-extraction` · 신뢰도 low
- **작업**: [[정보 추출]] — metadata · tags, task_categories = `token-classification` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `'관련기사 검색 및 추천' 시스템 구축을 위해 수집 및 구축되었으며` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:information_extraction, task:retrieval = `기사 제목, 기사 본문, 기사의 고유 ID, 기사 링크를 추출하여 생성한 데이터셋입니다.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `기사 제목, 기사 본문, 기사의 고유 ID, 기사 링크를 추출하여 생성한 데이터셋입니다.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[뉴스·미디어]] — tag_match · readme, tags = `News` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `해당 데이터셋은 '관련기사 검색 및 추천' 시스템 구축을 위해 수집 및 구축되었으며` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
