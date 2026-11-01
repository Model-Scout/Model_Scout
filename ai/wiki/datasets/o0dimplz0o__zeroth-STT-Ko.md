---
type: "dataset"
id: "o0dimplz0o/zeroth-STT-Ko"
source: "huggingface"
url: "https://huggingface.co/datasets/o0dimplz0o/zeroth-STT-Ko"
downloads: 24
summary: "한국어 음성 인식 학습용 문장 데이터셋으로 10만 건 이상의 문장 포함"
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
# o0dimplz0o/zeroth-STT-Ko

> dataset · [Hugging Face](https://huggingface.co/datasets/o0dimplz0o/zeroth-STT-Ko)

한국어 음성 인식 학습용 문장 데이터셋으로 10만 건 이상의 문장 포함

## 분류

- **작업**: [[음성 인식]] — metadata · readme, task_categories = `automatic-speech-recognition` · 신뢰도 high
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:speech_recognition = `Zeroth-STT-Ko Dataset` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme = `This provides over 102K rows of data (sentences)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `This provides over 102K rows of data (sentences)` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `50` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset combines the following publicly available Korean language datasets` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 75자 ≈ 50 토큰 (viewer statistics, default/train)
