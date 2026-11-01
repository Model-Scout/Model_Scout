---
type: "dataset"
id: "thaki-AI/SkillRetBench"
source: "huggingface"
url: "https://huggingface.co/datasets/thaki-AI/SkillRetBench"
downloads: 74
summary: "SkillRetBench는 자연어 질의에 맞는 절차적 스킬 문서를 검색하는 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[평가용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# thaki-AI/SkillRetBench

> dataset · [Hugging Face](https://huggingface.co/datasets/thaki-AI/SkillRetBench)

SkillRetBench는 자연어 질의에 맞는 절차적 스킬 문서를 검색하는 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — tag_match · readme, tags = `retrieval` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:retrieval = `given a natural-language user request` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `systems must rank or select the correct procedural skill document(s) from a fixed library` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `The benchmark includes 1,250 queries with gold skill identifiers and optional distractors, spanning five evaluation settings` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
