---
type: "dataset"
id: "ysmeta/EVE-Bench-Legal-2.0"
source: "huggingface"
url: "https://huggingface.co/datasets/ysmeta/EVE-Bench-Legal-2.0"
downloads: 41
summary: "한국 법률 판례 검색 벤치마크로, 5,999개 실무자 스타일 질의와 59,786개 판례를 포함함."
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
  - "[[평가용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# ysmeta/EVE-Bench-Legal-2.0

> dataset · [Hugging Face](https://huggingface.co/datasets/ysmeta/EVE-Bench-Legal-2.0)

한국 법률 판례 검색 벤치마크로, 5,999개 실무자 스타일 질의와 59,786개 판례를 포함함.

## 분류

- **작업**: [[문서 검색]] — metadata · readme, tags, task_categories = `text-retrieval` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:retrieval = `5,999 practitioner-style queries over 59,786 court precedents` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `graded multi-gold relevance labels (43,179 query-document judgements, 7.20 relevant precedents per query)` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `openrail` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · readme, tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `Korean legal precedent retrieval benchmark: 5,999 practitioner-style queries over 59,786 court precedents, with graded multi-gold relevance labels` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
