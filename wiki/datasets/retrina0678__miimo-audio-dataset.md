---
type: "dataset"
id: "retrina0678/miimo-audio-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/retrina0678/miimo-audio-dataset"
downloads: 767
summary: "음향 이벤트 분류 학습용 오디오 데이터셋으로 다양한 환경음과 증강 데이터를 포함함."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[음성 분류]]"
  - "[[텍스트 분류]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# retrina0678/miimo-audio-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/retrina0678/miimo-audio-dataset)

음향 이벤트 분류 학습용 오디오 데이터셋으로 다양한 환경음과 증강 데이터를 포함함.

## 분류

- **작업**: [[음성 분류]] — metadata · tags, task_categories = `audio-classification` · 신뢰도 low
- **작업**: [[텍스트 분류]] — ner · readme = `음향 이벤트 분류 학습용 데이터셋.` · 신뢰도 medium
- **입력 형식**: [[음성 (입력 형식)|음성]] — metadata · modality, task:audio_classification = `audio` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification = `text` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `31` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Edge Audio Dataset` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `음향 이벤트 분류 학습용 데이터셋.` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `filename` 열 p90 47자 ≈ 31 토큰 (viewer statistics, default/test)
