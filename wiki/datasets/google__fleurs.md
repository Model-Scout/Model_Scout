---
type: "dataset"
id: "google/fleurs"
source: "huggingface"
url: "https://huggingface.co/datasets/google/fleurs"
downloads: 176323
summary: "102개 언어의 음성 인식, 번역, 분류, 검색 평가용 다국어 음성 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[문서 검색]]"
  - "[[음성 인식]]"
  - "[[번역]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
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
  - "[[중규모 데이터]]"
---
# google/fleurs

> dataset · [Hugging Face](https://huggingface.co/datasets/google/fleurs)

102개 언어의 음성 인식, 번역, 분류, 검색 평가용 다국어 음성 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Fine-tune your own Language Identification models on FLEURS` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Retrieval provides n-way parallel speech and text data.` · 신뢰도 medium
- **작업**: [[음성 인식]] — metadata · readme, tags, task_categories = `automatic-speech-recognition` · 신뢰도 high
- **작업**: [[번역]] — ner · readme = `Fleurs is the speech version of the FLoRes machine translation benchmark.` · 신뢰도 medium
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:speech_recognition = `Path to the audio file` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:retrieval, task:translation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition, task:translation = `transcription of the audio file` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `102 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `23` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `It covers 102 languages from 10+ language families, 3 different domains and 4 task families` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `Training sets have around 10 hours of supervision.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `raw_transcription` 열 p90 92자 ≈ 23 토큰 (viewer statistics, ko_kr/validation)

## 이 데이터로 학습한 모델

- [[BuzzASR__korean|BuzzASR/korean]]
- [[facebook__mms-1b-all|facebook/mms-1b-all]]
- [[facebook__mms-1b-fl102|facebook/mms-1b-fl102]]
- [[facebook__mms-1b-l1107|facebook/mms-1b-l1107]]
- [[junnei__Phi-4-multimodal-instruct-ko-asr|junnei/Phi-4-multimodal-instruct-ko-asr]]
- [[leuconoe__whisper-acft-ko|leuconoe/whisper-acft-ko]]
