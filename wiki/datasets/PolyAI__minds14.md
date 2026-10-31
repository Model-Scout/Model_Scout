---
type: "dataset"
id: "PolyAI/minds14"
source: "huggingface"
url: "https://huggingface.co/datasets/PolyAI/minds14"
downloads: 11371
summary: "MInDS-14은 전자은행 도메인의 14개 의도 인식용 음성 데이터셋입니다."
readme_status: "template"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[음성 분류]]"
  - "[[텍스트 분류]]"
  - "[[음성 인식]]"
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
  - "[[상거래·상품]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# PolyAI/minds14

> dataset · [Hugging Face](https://huggingface.co/datasets/PolyAI/minds14)

MInDS-14은 전자은행 도메인의 14개 의도 인식용 음성 데이터셋입니다.

## 분류

- **작업**: [[음성 분류]] — metadata · task_ids = `keyword-spotting` · 신뢰도 low
- **작업**: [[텍스트 분류]] — ner · readme = `MINDS-14 is training and evaluation resource for intent detection task with spoken data.` · 신뢰도 low
- **작업**: [[음성 인식]] — metadata · tags, task_categories = `automatic-speech-recognition` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:audio_classification, task:speech_recognition = `intent detection task with spoken data` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `intent detection task` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `12 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `27` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `extracted from a commercial system in the e-banking domain` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `MINDS-14 is training and evaluation resource for intent detection task` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `english_transcription` 열 p90 109자 ≈ 27 토큰 (viewer statistics, ko-KR/train)
