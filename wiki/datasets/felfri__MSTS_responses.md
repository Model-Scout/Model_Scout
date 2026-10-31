---
type: "dataset"
id: "felfri/MSTS_responses"
source: "huggingface"
url: "https://huggingface.co/datasets/felfri/MSTS_responses"
downloads: 21
summary: "MSTS_responses 데이터셋은 멀티모달 정렬 및 안전성 튜닝을 위한 프롬프트-응답 쌍의 인간 라벨을 포함합니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# felfri/MSTS_responses

> dataset · [Hugging Face](https://huggingface.co/datasets/felfri/MSTS_responses)

MSTS_responses 데이터셋은 멀티모달 정렬 및 안전성 튜닝을 위한 프롬프트-응답 쌍의 인간 라벨을 포함합니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `This set can be used for multimodal alignment/safety tuning.` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-text-to-text` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:visual_qa = `image` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:visual_qa = `human labels for prompt-response pairs` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:visual_qa = `human labels for prompt-response pairs` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `11 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `This set can be used for multimodal alignment/safety tuning.` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
