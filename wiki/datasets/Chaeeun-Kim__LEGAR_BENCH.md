---
type: "dataset"
id: "Chaeeun-Kim/LEGAR_BENCH"
source: "huggingface"
url: "https://huggingface.co/datasets/Chaeeun-Kim/LEGAR_BENCH"
downloads: 40
summary: "한국어 법률 판례 검색을 위한 대규모 LEGAR BENCH 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "ko"
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
  - "[[상업 이용 가능]]"
domain:
  - "[[법률]]"
dataset_role:
  - "[[평가용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Chaeeun-Kim/LEGAR_BENCH

> dataset · [Hugging Face](https://huggingface.co/datasets/Chaeeun-Kim/LEGAR_BENCH)

한국어 법률 판례 검색을 위한 대규모 LEGAR BENCH 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — metadata · readme, task_categories = `text-retrieval` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:retrieval = `queries cover 411 distinct crime types` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `retrieval pool of 1.2M cases` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[법률]] — ner · readme = `Korean legal case retrieval benchmark` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `designed for a comprehensive evaluation across a broad spectrum of criminal offenses` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
