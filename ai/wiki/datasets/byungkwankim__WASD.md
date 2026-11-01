---
type: "dataset"
id: "byungkwankim/WASD"
source: "huggingface"
url: "https://huggingface.co/datasets/byungkwankim/WASD"
downloads: 13
summary: "WASD는 도시 환경 무선 신호 이상 탐지용 LTE 및 5G 대역 실제 및 시뮬레이션 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# byungkwankim/WASD

> dataset · [Hugging Face](https://huggingface.co/datasets/byungkwankim/WASD)

WASD는 도시 환경 무선 신호 이상 탐지용 LTE 및 5G 대역 실제 및 시뮬레이션 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `This dataset is suitable for training various object detection networks and developing robust deep learning models for accurate and efficient anomaly detection ` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — ner · readme = `Includes real-world signal data collected from 19 LTE and 5G bands.` · 신뢰도 low
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Label data (`.csv` files) containing bounding box coordinates and Interference-to-Signal Ratio (ISR) information of anomaly signals.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-nd-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `WASD (Wireless Anomaly Signal Dataset) is designed for anomaly signal detection in wireless signals within fixed urban scenarios.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is suitable for training various object detection networks and developing robust deep learning models` · 신뢰도 medium
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `999999999999.0` · 신뢰도 high
