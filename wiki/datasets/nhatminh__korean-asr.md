---
type: "dataset"
id: "nhatminh/korean-asr"
source: "huggingface"
url: "https://huggingface.co/datasets/nhatminh/korean-asr"
downloads: 124
summary: "YODAS2 한국어 음성 인식용 의사 라벨 데이터셋으로 ASR 모델 학습에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[표 (입력 형식)|표]]"
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
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# nhatminh/korean-asr

> dataset · [Hugging Face](https://huggingface.co/datasets/nhatminh/korean-asr)

YODAS2 한국어 음성 인식용 의사 라벨 데이터셋으로 ASR 모델 학습에 활용됨.

## 분류

- **작업**: [[임베딩]] — ner · readme = `pseudo-labels for distilling a small streaming ASR model` · 신뢰도 low
- **작업**: [[음성 인식]] — metadata · readme, tags, task_categories = `automatic-speech-recognition` · 신뢰도 high
- **입력 형식**: [[음성 (입력 형식)|음성]] — task_rule · task:speech_recognition = `audio` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding = `This repository contains transcripts and segment metadata only.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:speech_recognition = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `145` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-3.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `YouTube videos published under the Creative Commons Attribution licence` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 217자 ≈ 145 토큰 (viewer statistics, default/train)
