---
type: "dataset"
id: "Bingsu/zeroth-korean"
source: "huggingface"
url: "https://huggingface.co/datasets/Bingsu/zeroth-korean"
downloads: 867
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Bingsu/zeroth-korean

> dataset · [Hugging Face](https://huggingface.co/datasets/Bingsu/zeroth-korean)

## 분류

- **작업**: [[음성 인식]] — metadata · task_categories = `automatic-speech-recognition` · 신뢰도 high
- **입력 형식**: [[음성 (입력 형식)|음성]] — metadata · modality, task:speech_recognition = `audio` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:speech_recognition = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[ghost613__faster-whisper-large-v3-turbo-korean|ghost613/faster-whisper-large-v3-turbo-korean]]
- [[ghost613__whisper-large-v3-turbo-korean|ghost613/whisper-large-v3-turbo-korean]]
- [[junnei__Phi-4-multimodal-instruct-ko-asr|junnei/Phi-4-multimodal-instruct-ko-asr]]
