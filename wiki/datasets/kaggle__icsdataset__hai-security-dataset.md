---
type: "dataset"
id: "kaggle/icsdataset/hai-security-dataset"
source: "kaggle"
url: "https://www.kaggle.com/datasets/icsdataset/hai-security-dataset"
downloads: 9611
summary: "HAI 보안 데이터셋은 산업제어시스템(ICS) 테스트베드에서 수집된 공격 탐지용 시계열 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[정보 추출]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/icsdataset/hai-security-dataset

> dataset · [Kaggle](https://www.kaggle.com/datasets/icsdataset/hai-security-dataset)

HAI 보안 데이터셋은 산업제어시스템(ICS) 테스트베드에서 수집된 공격 탐지용 시계열 데이터입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `The last four columns provide data labels for whether an attack occurred or not` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `The time-series data in each CSV file satisfies time continuity. The first column represents the observed time as “yyyy-MM-dd hh:mm:ss,” while the rest columns ` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `Each dataset consists of several CSV files, and each file satisfies time continuity.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:information_extraction = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `The last four columns provide data labels for whether an attack occurred or not` · 신뢰도 low
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC BY-SA 4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The HAI dataset was collected from a realistic industrial control system (ICS) testbed augmented with a Hardware-In-the-Loop (HIL) simulator` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `HAI 23.05 |86 |hai-train1.csv (78 hours, 154.9 MB) hai-train2.csv (81 hours, 161.3 MB) hai-train3.csv (35 hours, 69.4 MB) hai-train4.csv (55 hours, 109.2 MB)` · 신뢰도 medium
