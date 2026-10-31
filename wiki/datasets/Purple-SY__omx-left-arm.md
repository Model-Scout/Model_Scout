---
type: "dataset"
id: "Purple-SY/omx-left-arm"
source: "huggingface"
url: "https://huggingface.co/datasets/Purple-SY/omx-left-arm"
downloads: 88
summary: "OMX 왼팔 로봇의 블록 집기-놓기 모방학습용 행동 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[영상 (입력 형식)|영상]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Purple-SY/omx-left-arm

> dataset · [Hugging Face](https://huggingface.co/datasets/Purple-SY/omx-left-arm)

OMX 왼팔 로봇의 블록 집기-놓기 모방학습용 행동 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `학습은 ACT / Diffusion Policy 같은 행동복제(imitation learning) 파이프라인을 권장합니다.` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme = `기록: 30 fps, 카메라 2대 (top, wrist) 640x480` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding = `태스크 문장: `Pick up the block and put it in the tray`` · 신뢰도 medium
- **입력 형식**: [[영상 (입력 형식)|영상]] — metadata · modality = `video` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `관절 키: `observation.state` / `action` = 6 관절 + `gripper.pos` (LeRobot 표준 순서)` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `OpenMANIPULATOR-X(OMX) 왼팔(leader/follower) 텔레옵으로 수집한 LeRobot v3 데이터셋입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `학습은 ACT / Diffusion Policy 같은 행동복제(imitation learning) 파이프라인을 권장합니다.` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
