---
type: "dataset"
id: "KTH/hungarian-single-speaker-tts"
source: "huggingface"
url: "https://huggingface.co/datasets/KTH/hungarian-single-speaker-tts"
downloads: 181
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[음성 합성]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[음성 (출력 형식)|음성]]"
language:
  - "[[hu]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# KTH/hungarian-single-speaker-tts

> dataset · [Hugging Face](https://huggingface.co/datasets/KTH/hungarian-single-speaker-tts)

## 분류

- **작업**: [[음성 합성]] — metadata · task_categories = `text-to-speech` · 신뢰도 high
- **입력 형식**: [[음성 (입력 형식)|음성]] — metadata · modality = `audio` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:text_to_speech = `text` · 신뢰도 high
- **출력 형식**: [[음성 (출력 형식)|음성]] — task_rule · task:text_to_speech = `audio` · 신뢰도 medium
- **언어**: [[hu]] — metadata · languages = `hu` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc0-1.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[Trendency__whisper-large-v3-hu|Trendency/whisper-large-v3-hu]]
