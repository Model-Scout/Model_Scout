---
type: "dataset"
id: "kaggle/imeintanis/collision-detection-ai-using-vibration-data"
source: "kaggle"
url: "https://www.kaggle.com/datasets/imeintanis/collision-detection-ai-using-vibration-data"
downloads: 596
summary: "원자력 발전소 냉각 시스템 내 충돌체 감지를 위한 진동 데이터 기반 AI 경진대회 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[환경·기상]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/imeintanis/collision-detection-ai-using-vibration-data

> dataset · [Kaggle](https://www.kaggle.com/datasets/imeintanis/collision-detection-ai-using-vibration-data)

원자력 발전소 냉각 시스템 내 충돌체 감지를 위한 진동 데이터 기반 AI 경진대회 데이터입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Vibration data to predict the x-coordinate, y-coordinate, mass, and velocity of the collider` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — ner · readme = `Vibration data to predict the x-coordinate, y-coordinate, mass, and velocity of the collider` · 신뢰도 low
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Vibration data to predict the x-coordinate, y-coordinate, mass, and velocity of the collider` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `Data files © Original Authors` · 신뢰도 high
- **도메인**: [[환경·기상]] — ner · readme = `Colliders that exist inside the coolant system of a nuclear power plant can cause damage to equipment.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The purpose of this competition is to activate artificial intelligence technology research that can diagnose abnormal signs of devices early.` · 신뢰도 low
