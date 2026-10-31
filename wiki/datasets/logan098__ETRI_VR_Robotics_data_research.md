---
type: "dataset"
id: "logan098/ETRI_VR_Robotics_data_research"
source: "huggingface"
url: "https://huggingface.co/datasets/logan098/ETRI_VR_Robotics_data_research"
downloads: 157
summary: "Apple Vision Pro로 수집한 ROBOTIS AI Worker FFW-BG2 로봇의 시연 데이터와 VLA 모델 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
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
# logan098/ETRI_VR_Robotics_data_research

> dataset · [Hugging Face](https://huggingface.co/datasets/logan098/ETRI_VR_Robotics_data_research)

Apple Vision Pro로 수집한 ROBOTIS AI Worker FFW-BG2 로봇의 시연 데이터와 VLA 모델 학습용 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `VLA(Vision-Language-Action) 모델 3종(π0.5 · GR00T N1.7 · RDT-1B)을 학습해` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `"언어가 로봇의 행동을 실제로 바꾸는가" 를 실기로 검증하는 연구` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme = `WebXR 손 트래킹` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme = `카메라 4채널 아틀라스 · 20Hz 레코더` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:generation = `지시문 문자열은 수집·학습·평가에 이대로 쓰입니다` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Apple Vision Pro 텔레오퍼레이션으로 ROBOTIS AI Worker FFW-BG2 실물 시연 데이터를 모으고` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `실물 회차(10회 단위, 사람 육안 판정) · 결과는 `result` 브랜치` · 신뢰도 low
