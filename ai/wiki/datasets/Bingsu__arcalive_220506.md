---
type: "dataset"
id: "Bingsu/arcalive_220506"
source: "huggingface"
url: "https://huggingface.co/datasets/Bingsu/arcalive_220506"
downloads: 46
summary: "아카라이브 베스트 라이브 채널의 2021년 8월 16일부터 2022년 5월 6일까지 댓글 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Bingsu/arcalive_220506

> dataset · [Hugging Face](https://huggingface.co/datasets/Bingsu/arcalive_220506)

아카라이브 베스트 라이브 채널의 2021년 8월 16일부터 2022년 5월 6일까지 댓글 데이터입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `댓글만 골라낸 데이터입니다.` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — metadata · task_categories, task_ids = `fill-mask` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `댓글만 골라낸 데이터입니다.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:language_modeling, task:retrieval = `댓글만 골라낸 데이터입니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `댓글만 골라낸 데이터입니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `481` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc0-1.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `커뮤니티 특성상, 민감한 데이터들도 많으므로 사용에 주의가 필요합니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `데이터를 수집하여, 댓글만 골라낸 데이터입니다.` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 721자 ≈ 481 토큰 (viewer statistics, arcalive comments/train)
