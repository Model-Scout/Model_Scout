---
type: "dataset"
id: "ETRI7203/ETRI_VR_Robotics_data_research"
source: "huggingface"
url: "https://huggingface.co/datasets/ETRI7203/ETRI_VR_Robotics_data_research"
downloads: 237
summary: "Apple Vision Pro 텔레오퍼레이션으로 로봇 행동 변화 연구를 위한 VR 로봇 시연 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
---
# ETRI7203/ETRI_VR_Robotics_data_research

> dataset · [Hugging Face](https://huggingface.co/datasets/ETRI7203/ETRI_VR_Robotics_data_research)

Apple Vision Pro 텔레오퍼레이션으로 로봇 행동 변화 연구를 위한 VR 로봇 시연 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `VLA(Vision-Language-Action) 모델 3종(π0.5 · GR00T N1.7 · RDT-1B)을 학습해` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `"언어가 로봇의 행동을 실제로 바꾸는가" 를 실기로 검증하는 연구` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `지시문 문자열은 수집·학습·평가에 이대로 쓰입니다` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme = `WebXR 손 트래킹` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme = `카메라 4채널 아틀라스 · 20Hz 레코더` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:generation, task:question_answering = `지시문 문자열은 수집·학습·평가에 이대로 쓰입니다` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `action 은 다음 프레임 목표 관절값(절대값)` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `ETRI VR Robotics Data Research — 데이터 · 가중치 저장소` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `실물 회차(10회 단위, 사람 육안 판정) · 결과는 `result` 브랜치` · 신뢰도 low
