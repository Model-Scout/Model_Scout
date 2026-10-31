---
type: "dataset"
id: "ysmeta/EVE-Bench-Legal-1.0"
source: "huggingface"
url: "https://huggingface.co/datasets/ysmeta/EVE-Bench-Legal-1.0"
downloads: 18
summary: "한국 법률 판례 검색 벤치마크로, 실제 실무자 질문 형태로 검색 성능 평가용 데이터셋입니다."
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
dataset_size:
  - "[[중규모 데이터]]"
---
# ysmeta/EVE-Bench-Legal-1.0

> dataset · [Hugging Face](https://huggingface.co/datasets/ysmeta/EVE-Bench-Legal-1.0)

한국 법률 판례 검색 벤치마크로, 실제 실무자 질문 형태로 검색 성능 평가용 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — metadata · readme, tags, task_categories = `text-retrieval` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:retrieval = `6,000 practitioner-style queries over 59,786 Korean court precedents.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `6,000 practitioner-style queries over 59,786 Korean court precedents.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `openrail` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · readme, tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `6,000 practitioner-style queries over 59,786 Korean court precedents.` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
