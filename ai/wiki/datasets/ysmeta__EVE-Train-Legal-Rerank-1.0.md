---
type: "dataset"
id: "ysmeta/EVE-Train-Legal-Rerank-1.0"
source: "huggingface"
url: "https://huggingface.co/datasets/ysmeta/EVE-Train-Legal-Rerank-1.0"
downloads: 25
summary: "한국 법률 문서 리랭킹 학습용 데이터셋으로, 쿼리-문서 관련성 평가를 포함함."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[리랭킹]]"
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
dataset_size:
  - "[[중규모 데이터]]"
---
# ysmeta/EVE-Train-Legal-Rerank-1.0

> dataset · [Hugging Face](https://huggingface.co/datasets/ysmeta/EVE-Train-Legal-Rerank-1.0)

한국 법률 문서 리랭킹 학습용 데이터셋으로, 쿼리-문서 관련성 평가를 포함함.

## 분류

- **작업**: [[리랭킹]] — metadata · tags, task_categories = `text-ranking` · 신뢰도 low
- **작업**: [[문서 검색]] — tag_match · tags = `retrieval` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:reranking, task:retrieval = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `all judged for relevance` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `openrail` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · readme, tags = `legal` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
