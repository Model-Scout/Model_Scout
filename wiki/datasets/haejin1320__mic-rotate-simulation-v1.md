---
type: "dataset"
id: "haejin1320/mic-rotate-simulation-v1"
source: "huggingface"
url: "https://huggingface.co/datasets/haejin1320/mic-rotate-simulation-v1"
downloads: 63
summary: "Android 스마트폰 마이크 회전에 따른 스테레오 오디오 변환 AI 모델 학습용 시뮬레이션 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[음성 (출력 형식)|음성]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# haejin1320/mic-rotate-simulation-v1

> dataset · [Hugging Face](https://huggingface.co/datasets/haejin1320/mic-rotate-simulation-v1)

Android 스마트폰 마이크 회전에 따른 스테레오 오디오 변환 AI 모델 학습용 시뮬레이션 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `스테레오 오디오 변환 AI 모델 학습용 시뮬레이션 데이터셋.` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme = `audio_0deg_ch0 Audio Portrait 0° MIC_TOP (48kHz)` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:embedding = `text` · 신뢰도 high
- **출력 형식**: [[음성 (출력 형식)|음성]] — ner · readme = `audio_90deg_ch0 Audio Landscape 90° MIC_TOP (48kHz)` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `MicRotate Simulation Dataset` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `스테레오 오디오 변환 AI 모델 학습용 시뮬레이션 데이터셋.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
