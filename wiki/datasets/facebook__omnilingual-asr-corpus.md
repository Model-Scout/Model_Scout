---
type: "dataset"
id: "facebook/omnilingual-asr-corpus"
source: "huggingface"
url: "https://huggingface.co/datasets/facebook/omnilingual-asr-corpus"
downloads: 5502
summary: "348개 소수 언어의 자발적 음성 녹음과 전사 데이터로 음성 인식 모델 학습용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[음성 분류]]"
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
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
# facebook/omnilingual-asr-corpus

> dataset · [Hugging Face](https://huggingface.co/datasets/facebook/omnilingual-asr-corpus)

348개 소수 언어의 자발적 음성 녹음과 전사 데이터로 음성 인식 모델 학습용입니다.

## 분류

- **작업**: [[음성 분류]] — metadata · task_categories = `audio-classification` · 신뢰도 low
- **작업**: [[음성 인식]] — metadata · readme, task_categories = `automatic-speech-recognition` · 신뢰도 high
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:audio_classification, task:speech_recognition = `The Omnilingual ASR Corpus is a collection of spontaneous speech recordings and their transcriptions` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `The Omnilingual ASR Corpus is a collection of spontaneous speech recordings and their transcriptions` · 신뢰도 medium
- **언어**: [[다국어]] — metadata · languages = `348 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `253` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The Omnilingual ASR Corpus is a collection of spontaneous speech recordings and their transcriptions for 348 under-served languages.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `raw_text` 열 p90 1013자 ≈ 253 토큰 (viewer statistics, default/test)
