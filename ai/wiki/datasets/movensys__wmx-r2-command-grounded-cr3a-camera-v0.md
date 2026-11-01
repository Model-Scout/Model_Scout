---
type: "dataset"
id: "movensys/wmx-r2-command-grounded-cr3a-camera-v0"
source: "huggingface"
url: "https://huggingface.co/datasets/movensys/wmx-r2-command-grounded-cr3a-camera-v0"
downloads: 82
summary: "Dobot CR3A 로봇의 30fps 카메라 영상과 축 상태 데이터를 포함한 시각 기반 학습용 로봇 동작 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[영상 (입력 형식)|영상]]"
output_modality:
  - "[[이미지 (출력 형식)|이미지]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# movensys/wmx-r2-command-grounded-cr3a-camera-v0

> dataset · [Hugging Face](https://huggingface.co/datasets/movensys/wmx-r2-command-grounded-cr3a-camera-v0)

Dobot CR3A 로봇의 30fps 카메라 영상과 축 상태 데이터를 포함한 시각 기반 학습용 로봇 동작 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `30 fps. Robot: Dobot CR3A, six axes; wrist RealSense D455; AG-160-95 gripper.` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme = `Wrist RGB decoded by LeRobot` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `numeric Parquet shards.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:embedding = `text` · 신뢰도 high
- **입력 형식**: [[영상 (입력 형식)|영상]] — metadata · modality = `video` · 신뢰도 high
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — ner · readme = `Wrist RGB decoded by LeRobot` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Public dataset. Downloading does not require authentication.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
