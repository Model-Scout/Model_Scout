---
type: "dataset"
id: "Spatial1ntelligence/synthetic-bedroom-layouts"
source: "huggingface"
url: "https://huggingface.co/datasets/Spatial1ntelligence/synthetic-bedroom-layouts"
downloads: 455
summary: "Amazon Berkeley Objects 기반 4,000개 침실 레이아웃과 가구 배치 데이터셋으로 실내 장면 합성에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Spatial1ntelligence/synthetic-bedroom-layouts

> dataset · [Hugging Face](https://huggingface.co/datasets/Spatial1ntelligence/synthetic-bedroom-layouts)

Amazon Berkeley Objects 기반 4,000개 침실 레이아웃과 가구 배치 데이터셋으로 실내 장면 합성에 활용됨.

## 분류

- **작업**: [[임베딩]] — ner · readme = `in the box format used by indoor scene-synthesis models (ATISS-style boxes.npz)` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `4,000 procedurally composed bedroom layouts with 27,025 furniture placements` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:generation = `in the box format used by indoor scene-synthesis models (ATISS-style boxes.npz)` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `4,000 procedurally composed bedroom layouts with 27,025 furniture placements` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Furniture is drawn from Amazon Berkeley Objects (CC BY 4.0), so the whole dataset is redistributable and usable commercially.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The generator, the prior builder, and every check.` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
