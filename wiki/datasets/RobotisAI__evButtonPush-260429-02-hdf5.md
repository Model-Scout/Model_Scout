---
type: "dataset"
id: "RobotisAI/evButtonPush-260429-02-hdf5"
source: "huggingface"
url: "https://huggingface.co/datasets/RobotisAI/evButtonPush-260429-02-hdf5"
downloads: 867
summary: "엘리베이터 콜 버튼 누르기 task용 ROBOTIS OMY 6-DoF 매니퓰레이터 시연 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[문서 검색]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
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
dataset_size:
  - "[[중규모 데이터]]"
---
# RobotisAI/evButtonPush-260429-02-hdf5

> dataset · [Hugging Face](https://huggingface.co/datasets/RobotisAI/evButtonPush-260429-02-hdf5)

엘리베이터 콜 버튼 누르기 task용 ROBOTIS OMY 6-DoF 매니퓰레이터 시연 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `엘리베이터 콜 버튼 누르기 task 의 ROBOTIS OMY 6-DoF 매니퓰레이터 시연 데이터셋.` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme = `30Hz 멀티카메라 RGB 데모셋` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:retrieval = `State 관측 | qpos (10), qvel (10), eef_pos (3), eef_quat (4), call_button_pos (3), rel_dist (3), call_button_lit (1), button_pixel_uv_{wrist,top,belly} (각 3: u, v` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Action 차원 | 7 (6 arm joint + 1 binary gripper)` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Isaac Sim 5.1 + Isaac Lab 환경에서 scripted teacher (DLS-IK + force-feedback) 로 자동 수집됨.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `각 데모는 별도 teacher launch 로 수집 (`--num-demos 1 --usd-index $ID`).` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
