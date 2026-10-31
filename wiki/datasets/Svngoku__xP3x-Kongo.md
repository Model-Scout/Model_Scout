---
type: "dataset"
id: "Svngoku/xP3x-Kongo"
source: "huggingface"
url: "https://huggingface.co/datasets/Svngoku/xP3x-Kongo"
downloads: 99
summary: "xP3x-Kongo는 277개 언어와 16개 NLP 작업을 포함한 다국어 프롬프트 및 데이터셋 모음으로, mT0와 BLOOMZ 모델 학습에 사용됩니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# Svngoku/xP3x-Kongo

> dataset · [Hugging Face](https://huggingface.co/datasets/Svngoku/xP3x-Kongo)

xP3x-Kongo는 277개 언어와 16개 NLP 작업을 포함한 다국어 프롬프트 및 데이터셋 모음으로, mT0와 BLOOMZ 모델 학습에 사용됩니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `xP3x (Crosslingual Public Pool of Prompts eXtended) is a collection of prompts & datasets across 277 languages & 16 NLP tasks.` · 신뢰도 low
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:translation = ``inputs`: the natural language input fed to the model` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:translation = ``targets`: the natural language target that the model has to generate` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `220 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `65` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `xP3x (Crosslingual Public Pool of Prompts eXtended) is a collection of prompts & datasets across 277 languages & 16 NLP tasks.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `It is used for training future contenders of mT0 & BLOOMZ at project Aya @C4AI` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `inputs` 열 p90 261자 ≈ 65 토큰 (viewer statistics, default/test)
