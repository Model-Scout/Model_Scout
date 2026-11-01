---
type: "dataset"
id: "Bingsu/zeroth-korean"
source: "huggingface"
url: "https://huggingface.co/datasets/Bingsu/zeroth-korean"
downloads: 867
summary: "한국어 음성 인식 학습용으로 51.6시간 음성 및 전사 데이터 제공"
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
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Bingsu/zeroth-korean

> dataset · [Hugging Face](https://huggingface.co/datasets/Bingsu/zeroth-korean)

한국어 음성 인식 학습용으로 51.6시간 음성 및 전사 데이터 제공

## 분류

- **작업**: [[음성 인식]] — metadata · readme, task_categories = `automatic-speech-recognition` · 신뢰도 medium
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:speech_recognition = `The data set contains transcriebed audio data for Korean.` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme = `text: `string`` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `text: `string`` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `57` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Zeroth project introduces free Korean speech corpus and aims to make Korean speech recognition more broadly accessible to everyone.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `1.2 hours transcribed Korean audio for testing data (457 utterances, 10 people)` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `51.6 hours transcribed Korean audio for training data (22,263 utterances, 105 people, 3000 sentences)` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 85자 ≈ 57 토큰 (viewer statistics, default/test)

## 이 데이터로 학습한 모델

- [[ghost613__faster-whisper-large-v3-turbo-korean|ghost613/faster-whisper-large-v3-turbo-korean]]
- [[ghost613__whisper-large-v3-turbo-korean|ghost613/whisper-large-v3-turbo-korean]]
- [[junnei__Phi-4-multimodal-instruct-ko-asr|junnei/Phi-4-multimodal-instruct-ko-asr]]
