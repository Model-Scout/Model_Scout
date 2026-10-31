---
type: "dataset"
id: "FBK-MT/Speech-MASSIVE"
source: "huggingface"
url: "https://huggingface.co/datasets/FBK-MT/Speech-MASSIVE"
downloads: 2143
summary: "12개 언어의 음성 기반 다국어 음성 언어 이해(SLU) 데이터셋으로 의도 예측과 슬롯 채우기 작업에 활용됨."
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
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
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
# FBK-MT/Speech-MASSIVE

> dataset · [Hugging Face](https://huggingface.co/datasets/FBK-MT/Speech-MASSIVE)

12개 언어의 음성 기반 다국어 음성 언어 이해(SLU) 데이터셋으로 의도 예측과 슬롯 채우기 작업에 활용됨.

## 분류

- **작업**: [[음성 분류]] — metadata · task_categories = `audio-classification` · 신뢰도 low
- **작업**: [[텍스트 분류]] — metadata · readme, tags, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[질의응답]] — ner · readme = `annotations for the intent prediction and slot-filling tasks` · 신뢰도 low
- **작업**: [[음성 인식]] — metadata · readme, task_categories = `automatic-speech-recognition` · 신뢰도 medium
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:audio_classification, task:speech_recognition = `Speech-MASSIVE is a multilingual Spoken Language Understanding (SLU) dataset comprising the speech counterpart` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:question_answering = `annotations for the intent prediction and slot-filling tasks` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering, task:speech_recognition = `annotations for the intent prediction and slot-filling tasks` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `12 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `14` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Speech-MASSIVE is a multilingual Spoken Language Understanding (SLU) dataset comprising the speech counterpart for a portion of the MASSIVE textual corpus.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `validation split available for all the 12 languages` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `Full train split is provided for French and German, and for all the 12 languages (including French and German), we provide few-shot train, validation, test spli` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `annot_utt` 열 p90 55자 ≈ 14 토큰 (viewer statistics, ko-KR/validation)

## 이 데이터로 학습한 모델

- [[Trendency__whisper-large-v3-hu|Trendency/whisper-large-v3-hu]]
