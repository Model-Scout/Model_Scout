---
type: "dataset"
id: "facebook/voxpopuli"
source: "huggingface"
url: "https://huggingface.co/datasets/facebook/voxpopuli"
downloads: 29441
summary: "VoxPopuli는 유럽 의회 연설 녹음 기반 다국어 음성 말뭉치로 음성 표현 학습용입니다."
readme_status: "template"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# facebook/voxpopuli

> dataset · [Hugging Face](https://huggingface.co/datasets/facebook/voxpopuli)

VoxPopuli는 유럽 의회 연설 녹음 기반 다국어 음성 말뭉치로 음성 표현 학습용입니다.

## 분류

- **작업**: [[음성 인식]] — metadata · readme, task_categories = `automatic-speech-recognition` · 신뢰도 medium
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:speech_recognition = `VoxPopuli is a large-scale multilingual speech corpus for representation learning, semi-supervised learning and interpretation.` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `This implementation contains transcribed speech data for 18 languages.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `16 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `62` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc0-1.0` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `VoxPopuli is a large-scale multilingual speech corpus for representation learning, semi-supervised learning and interpretation.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `This implementation contains transcribed speech data for 18 languages.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `raw_text` 열 p90 246자 ≈ 62 토큰 (viewer statistics, cs/validation)

## 이 데이터로 학습한 모델

- [[Trendency__whisper-large-v3-hu|Trendency/whisper-large-v3-hu]]
