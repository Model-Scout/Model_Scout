---
type: "dataset"
id: "kaggle/pranavjha24/car-hacking-dataset"
source: "kaggle"
url: "https://www.kaggle.com/datasets/pranavjha24/car-hacking-dataset"
downloads: 3255
summary: "실제 차량 CAN 버스 트래픽과 사이버 공격 데이터를 포함한 자동차 침입 탐지용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교통·모빌리티]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/pranavjha24/car-hacking-dataset

> dataset · [Kaggle](https://www.kaggle.com/datasets/pranavjha24/car-hacking-dataset)

실제 차량 CAN 버스 트래픽과 사이버 공격 데이터를 포함한 자동차 침입 탐지용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `It is widely used to develop machine learning models for detecting intrusions in automotive communication systems.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification = `Features: Timestamp, CAN ID, Data Length Code (DLC), Data (hexadecimal payload).` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Label (0 for normal, 1 for attack).` · 신뢰도 low
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `MIT` · 신뢰도 high
- **도메인**: [[교통·모빌리티]] — ner · readme = `This dataset captures Controller Area Network (CAN) bus traffic from a real vehicle` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Train ML/DL models (e.g., Random Forest, LSTM) for real-time CAN intrusion detection.` · 신뢰도 medium
