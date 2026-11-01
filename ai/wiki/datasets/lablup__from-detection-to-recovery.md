---
type: "dataset"
id: "lablup/from-detection-to-recovery"
source: "huggingface"
url: "https://huggingface.co/datasets/lablup/from-detection-to-recovery"
downloads: 24
summary: "504 GPU 클러스터에서 대규모 LLM 사전학습의 이상 탐지와 자동 복구 운영 분석 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[시계열 예측]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
  - "[[시계열 (출력 형식)|시계열]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[학술·논문]]"
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# lablup/from-detection-to-recovery

> dataset · [Hugging Face](https://huggingface.co/datasets/lablup/from-detection-to-recovery)

504 GPU 클러스터에서 대규모 LLM 사전학습의 이상 탐지와 자동 복구 운영 분석 데이터입니다.

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `55일간의 Prometheus 시계열 데이터` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `대규모 LLM 사전학습의 장애 탐지부터 자동 복구까지를 실증 분석합니다` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:language_modeling = `73일간의 운영 로그` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — ner · readme, task:forecasting = `55일간의 Prometheus 시계열 데이터` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:language_modeling = `text` · 신뢰도 medium
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — ner · readme, task:forecasting = `55일간의 Prometheus 시계열 데이터` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[학술·논문]] — tag_match · tags = `arxiv` · 신뢰도 medium
- **도메인**: [[일반]] — ner · readme = `대규모 LLM 사전학습의 장애 탐지부터 자동 복구까지를 실증 분석합니다` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `224회 다중 노드 학습 작업을 포괄하는 73일간의 운영 로그` · 신뢰도 medium
