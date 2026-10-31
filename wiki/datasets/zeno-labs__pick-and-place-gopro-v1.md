---
type: "dataset"
id: "zeno-labs/pick-and-place-gopro-v1"
source: "huggingface"
url: "https://huggingface.co/datasets/zeno-labs/pick-and-place-gopro-v1"
downloads: 119
summary: "GoPro 헤드 마운트 카메라로 촬영한 Pick and place 도메인 로봇 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
  - "[[영상 (입력 형식)|영상]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# zeno-labs/pick-and-place-gopro-v1

> dataset · [Hugging Face](https://huggingface.co/datasets/zeno-labs/pick-and-place-gopro-v1)

GoPro 헤드 마운트 카메라로 촬영한 Pick and place 도메인 로봇 학습용 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Head-mounted GoPro / smartphone footage is processed into LeRobot v2.1 datasets with multiple modalities aligned frame-by-frame` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `ZenO Labs builds an egocentric data pipeline for training Physical AI and robot learning policies.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · modality, readme = `LeRobot v2.1 — parquet (per-episode) + meta JSON + mp4 videos` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:generation = `Hand pose — 21 keypoints × 2 hands, with temporal post-processing` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — metadata · modality = `timeseries` · 신뢰도 high
- **입력 형식**: [[영상 (입력 형식)|영상]] — ner · modality, readme = `Head-mounted GoPro / smartphone footage is processed into LeRobot v2.1 datasets with multiple modalities aligned frame-by-frame` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Egocentric head-mounted camera dataset from the Pick and place domain.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `ZenO Labs builds an egocentric data pipeline for training Physical AI and robot learning policies.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
