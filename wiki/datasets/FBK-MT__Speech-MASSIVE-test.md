---
type: "dataset"
id: "FBK-MT/Speech-MASSIVE-test"
source: "huggingface"
url: "https://huggingface.co/datasets/FBK-MT/Speech-MASSIVE-test"
downloads: 159
summary: "12개 언어의 음성 기반 다국어 음성언어이해(SLU) 테스트 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[음성 분류]]"
  - "[[텍스트 분류]]"
  - "[[질의응답]]"
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# FBK-MT/Speech-MASSIVE-test

> dataset · [Hugging Face](https://huggingface.co/datasets/FBK-MT/Speech-MASSIVE-test)

12개 언어의 음성 기반 다국어 음성언어이해(SLU) 테스트 데이터셋입니다.

## 분류

- **작업**: [[음성 분류]] — metadata · task_categories = `audio-classification` · 신뢰도 low
- **작업**: [[텍스트 분류]] — metadata · readme, tags, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[질의응답]] — ner · readme = `annotations for the intent prediction and slot-filling tasks` · 신뢰도 low
- **작업**: [[음성 인식]] — metadata · readme, task_categories = `automatic-speech-recognition` · 신뢰도 medium
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:audio_classification, task:speech_recognition = ``audio.array`: Read audio file with the sampling rate of 16,000` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:question_answering = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering, task:speech_recognition = `annotations for the intent prediction and slot-filling tasks` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `12 languages` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Speech-MASSIVE is a multilingual Spoken Language Understanding (SLU) dataset comprising the speech counterpart for a portion of the MASSIVE textual corpus.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `This dataset repository is only for test split of Speech-MASSIVE.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
