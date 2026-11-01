---
type: "dataset"
id: "RobotisAI/evButtonPush-260429-01-hdf5"
source: "huggingface"
url: "https://huggingface.co/datasets/RobotisAI/evButtonPush-260429-01-hdf5"
downloads: 65
summary: "로보티스 OMY 6-DoF 매니퓰레이터의 엘리베이터 콜 버튼 누르기 시연 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
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
# RobotisAI/evButtonPush-260429-01-hdf5

> dataset · [Hugging Face](https://huggingface.co/datasets/RobotisAI/evButtonPush-260429-01-hdf5)

로보티스 OMY 6-DoF 매니퓰레이터의 엘리베이터 콜 버튼 누르기 시연 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Imitation learning demo dataset for elevator call button press task using ROBOTIS OMY 6-DoF arm.` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme = `30Hz Multi-Camera RGB Demo Set v01` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation = `State obs | qpos, qvel (10), eef_pos (3), eef_quat (4), call_button_pos (3), rel_dist (3), call_button_lit (1), action history` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Action space | 7-dim (6 arm joints + 1 binary gripper)` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Isaac Sim 5.1 + Isaac Lab 환경에서 scripted teacher (DLS-IK + force-feedback)로 자동 수집.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Imitation learning demo dataset for elevator call button press task` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
