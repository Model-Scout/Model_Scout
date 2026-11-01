---
type: "dataset"
id: "chanwook/actioncam-vio"
source: "huggingface"
url: "https://huggingface.co/datasets/chanwook/actioncam-vio"
downloads: 96
summary: "액션캠 영상과 IMU 데이터를 활용한 SLAM 재현용 actioncam-vio 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[영상 (입력 형식)|영상]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# chanwook/actioncam-vio

> dataset · [Hugging Face](https://huggingface.co/datasets/chanwook/actioncam-vio)

액션캠 영상과 IMU 데이터를 활용한 SLAM 재현용 actioncam-vio 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `액션캠 하나로 촬영한 MP4에서 RGB + IMU(내장 텔레메트리)를 추출해 캘리브레이션·ORB-SLAM3 mono-inertial까지 재현할 수 있습니다.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:retrieval = `text` · 신뢰도 medium
- **입력 형식**: [[영상 (입력 형식)|영상]] — ner · modality, readme = `액션캠 하나로 촬영한 MP4에서 RGB + IMU(내장 텔레메트리)를 추출해 캘리브레이션·ORB-SLAM3 mono-inertial까지 재현할 수 있습니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `액션캠 하나로 촬영한 MP4에서 RGB + IMU(내장 텔레메트리)를 추출해 캘리브레이션·ORB-SLAM3 mono-inertial까지 재현할 수 있습니다.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `actioncam-vio 파이프라인(UMI 스타일 액션캠 VIO)의 원본 영상 + SLAM 산출물입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `actioncam-vio 파이프라인(UMI 스타일 액션캠 VIO)의 원본 영상 + SLAM 산출물입니다.` · 신뢰도 low
