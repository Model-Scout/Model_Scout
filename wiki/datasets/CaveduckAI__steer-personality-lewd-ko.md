---
type: "dataset"
id: "CaveduckAI/steer-personality-lewd-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/CaveduckAI/steer-personality-lewd-ko"
downloads: 23
summary: "CAA 기법으로 성격 특성 벡터 추출용 15000개 한국어 시나리오 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
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
# CaveduckAI/steer-personality-lewd-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/CaveduckAI/steer-personality-lewd-ko)

CAA 기법으로 성격 특성 벡터 추출용 15000개 한국어 시나리오 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `designed for extracting personality steering vectors using the Contrastive Activation Addition (CAA) method` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:generation = `Each sample presents a scenario with two response options` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `one exhibiting the target personality trait and one neutral` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This dataset contains 15000 samples designed for extracting personality steering vectors` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset contains 15000 samples designed for extracting personality steering vectors` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
