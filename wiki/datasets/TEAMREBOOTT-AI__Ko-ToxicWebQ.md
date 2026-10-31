---
type: "dataset"
id: "TEAMREBOOTT-AI/Ko-ToxicWebQ"
source: "huggingface"
url: "https://huggingface.co/datasets/TEAMREBOOTT-AI/Ko-ToxicWebQ"
downloads: 11
summary: "Ko-ToxicWebQ는 한국어 유해 웹 검색 쿼리 데이터셋으로, 유해성 및 회피 전략 평가에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# TEAMREBOOTT-AI/Ko-ToxicWebQ

> dataset · [Hugging Face](https://huggingface.co/datasets/TEAMREBOOTT-AI/Ko-ToxicWebQ)

Ko-ToxicWebQ는 한국어 유해 웹 검색 쿼리 데이터셋으로, 유해성 및 회피 전략 평가에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `annotated for harmfulness and obfuscation strategies` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `training language models to handle adversarial or sensitive inputs in Korean` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:language_modeling = `Korean web search queries` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling = `annotated for harmfulness and obfuscation strategies` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `real-world Korean web search queries` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `designed for evaluating moderation systems and training language models` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
