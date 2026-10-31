---
type: "dataset"
id: "niko0xdev/julia-1-router-data"
source: "huggingface"
url: "https://huggingface.co/datasets/niko0xdev/julia-1-router-data"
downloads: 112
summary: "julia-1-router 모델 학습 및 평가용 합성 다국어 프롬프트 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[vi]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# niko0xdev/julia-1-router-data

> dataset · [Hugging Face](https://huggingface.co/datasets/niko0xdev/julia-1-router-data)

julia-1-router 모델 학습 및 평가용 합성 다국어 프롬프트 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Prompts are in Vietnamese (with and without diacritics), Korean and English.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `a prompt router that picks one model tier: small, medium, large or reasoning` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `3 languages` · 신뢰도 high
- **언어**: [[vi]] — metadata · languages = `vi` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Prompts are in Vietnamese (with and without diacritics), Korean and English.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This is the synthetic training and evaluation data for niko0xdev/julia-1-router` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
