---
type: "dataset"
id: "rulehold/lineage-blindspot-v0"
source: "huggingface"
url: "https://huggingface.co/datasets/rulehold/lineage-blindspot-v0"
downloads: 12
summary: "Hugging Face 텍스트 생성 모델의 기반 모델 계열 식별 불가 비율을 집계한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
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
# rulehold/lineage-blindspot-v0

> dataset · [Hugging Face](https://huggingface.co/datasets/rulehold/lineage-blindspot-v0)

Hugging Face 텍스트 생성 모델의 기반 모델 계열 식별 불가 비율을 집계한 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Aggregate measurements of model-lineage blind spots on Hugging Face: how often a text-generation model's base-model family cannot be seen from its repository na` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding = `text-generation model's base-model family cannot be seen from its repository name or self-declared base_model` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `summary.json — aggregates per sample (counts, rates, 95% Wilson intervals, inferred-family counts); breakdown.json — S and M3 by inferred family and by GGUF vs ` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **데이터 용도**: [[평가용]] — ner · readme = `Aggregate measurements of model-lineage blind spots on Hugging Face` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
