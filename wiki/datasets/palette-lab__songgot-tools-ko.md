---
type: "dataset"
id: "palette-lab/songgot-tools-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/palette-lab/songgot-tools-ko"
downloads: 102
summary: "한국어 도구 호출 데이터로, Songgot 모델 후학습에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[도구 호출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# palette-lab/songgot-tools-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/palette-lab/songgot-tools-ko)

한국어 도구 호출 데이터로, Songgot 모델 후학습에 사용됨.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[도구 호출]] — tag_match · readme, tags = `tool-calling` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `call JSON` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Synthetic Korean tool-calling data used to post-train Songgot` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `Synthetic Korean tool-calling data used to post-train Songgot` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[palette-lab__songgot-x-0.8b|palette-lab/songgot-x-0.8b]]
