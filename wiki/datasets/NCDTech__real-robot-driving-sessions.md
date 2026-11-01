---
type: "dataset"
id: "NCDTech/real-robot-driving-sessions"
source: "huggingface"
url: "https://huggingface.co/datasets/NCDTech/real-robot-driving-sessions"
downloads: 212
summary: "궤도 시험 로봇의 20Hz 실주행 세션 3개(총 18분) 데이터로 로봇 주행 모델 학습용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[시계열 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
  - "[[시계열 (출력 형식)|시계열]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# NCDTech/real-robot-driving-sessions

> dataset · [Hugging Face](https://huggingface.co/datasets/NCDTech/real-robot-driving-sessions)

궤도 시험 로봇의 20Hz 실주행 세션 3개(총 18분) 데이터로 로봇 주행 모델 학습용입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `multimodal robot telemetry is rare at this size` · 신뢰도 low
- **작업**: [[시계열 예측]] — ner · readme = `this is the same recording discipline we now focus on the predictive maintenance (PdM) of aging mechanical equipment` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding = ``.csv` is the accessible form: 71 columns, one row per 50 ms sample` · 신뢰도 high
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — ner · readme, task:forecasting = `Three real driving sessions of our tracked test robot, recorded at 20 Hz on the test floor` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `the 18 minutes that trained our 101-parameter driver` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `multimodal robot telemetry is rare at this size` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `These are the exact sessions that trained NCDTech/real-robot-driving-mlp-numpy` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
