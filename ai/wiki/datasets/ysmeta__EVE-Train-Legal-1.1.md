---
type: "dataset"
id: "ysmeta/EVE-Train-Legal-1.1"
source: "huggingface"
url: "https://huggingface.co/datasets/ysmeta/EVE-Train-Legal-1.1"
downloads: 28
summary: "한국어 법률 판례 검색을 위한 쿼리-판례 쌍 학습 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[법률]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# ysmeta/EVE-Train-Legal-1.1

> dataset · [Hugging Face](https://huggingface.co/datasets/ysmeta/EVE-Train-Legal-1.1)

한국어 법률 판례 검색을 위한 쿼리-판례 쌍 학습 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — metadata · readme, tags, task_categories = `text-retrieval` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:retrieval = `Training pairs for Korean legal precedent retrieval: 134,996 (query, precedent) pairs` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Training pairs for Korean legal precedent retrieval: 134,996 (query, precedent) pairs` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `openrail` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · readme, tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Training pairs for Korean legal precedent retrieval: 134,996 (query, precedent) pairs plus 19,038 queries with verified hard negatives, used to train ysmeta/EVE` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
