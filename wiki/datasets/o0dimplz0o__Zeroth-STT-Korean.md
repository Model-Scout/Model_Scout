---
type: "dataset"
id: "o0dimplz0o/Zeroth-STT-Korean"
source: "huggingface"
url: "https://huggingface.co/datasets/o0dimplz0o/Zeroth-STT-Korean"
downloads: 60
summary: "Zeroth-STT-Korean은 한국어 음성 인식 학습용 데이터셋입니다."
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
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# o0dimplz0o/Zeroth-STT-Korean

> dataset · [Hugging Face](https://huggingface.co/datasets/o0dimplz0o/Zeroth-STT-Korean)

Zeroth-STT-Korean은 한국어 음성 인식 학습용 데이터셋입니다.

## 분류

- **작업**: [[음성 인식]] — metadata · readme, task_categories = `automatic-speech-recognition` · 신뢰도 high
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:speech_recognition = `Zeroth-STT-Korean Dataset` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `Zeroth-STT-Korean Dataset` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `52` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `Zeroth-STT-Korean Dataset` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 78자 ≈ 52 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[o0dimplz0o__Whisper-Large-v3-turbo-STT-Zeroth-KO-v2|o0dimplz0o/Whisper-Large-v3-turbo-STT-Zeroth-KO-v2]]
