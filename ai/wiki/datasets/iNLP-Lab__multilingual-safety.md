---
type: "dataset"
id: "iNLP-Lab/multilingual-safety"
source: "huggingface"
url: "https://huggingface.co/datasets/iNLP-Lab/multilingual-safety"
downloads: 127
summary: "다국어 안전 지침 데이터셋으로, 유해한 명령어에 대한 거부 응답 학습 및 평가용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
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
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# iNLP-Lab/multilingual-safety

> dataset · [Hugging Face](https://huggingface.co/datasets/iNLP-Lab/multilingual-safety)

다국어 안전 지침 데이터셋으로, 유해한 명령어에 대한 거부 응답 학습 및 평가용입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `probing refusal behaviour in language models, building multilingual safety calibration corpora` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:generation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Safe refusal / corrective response (translated; `en` is the original)` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `12 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `72` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 288자 ≈ 72 토큰 (viewer statistics, ko/train)
