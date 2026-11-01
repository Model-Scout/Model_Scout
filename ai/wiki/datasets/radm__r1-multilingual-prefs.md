---
type: "dataset"
id: "radm/r1-multilingual-prefs"
source: "huggingface"
url: "https://huggingface.co/datasets/radm/r1-multilingual-prefs"
downloads: 36
summary: "다국어 추론 및 사고 관련 데이터셋으로, 모델 학습에 사용됨"
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# radm/r1-multilingual-prefs

> dataset · [Hugging Face](https://huggingface.co/datasets/radm/r1-multilingual-prefs)

다국어 추론 및 사고 관련 데이터셋으로, 모델 학습에 사용됨

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `Dataset basen on: lightblue/reasoning-multilingual-R1-Llama-70B-train` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Dataset basen on: lightblue/reasoning-multilingual-R1-Llama-70B-train` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `38 languages` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `6172` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `Dataset basen on: lightblue/reasoning-multilingual-R1-Llama-70B-train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `chosen` 열 p90 24686자 ≈ 6172 토큰 (viewer statistics, default/train)
