---
type: "dataset"
id: "kaggle/azimjaan21/fire-and-smoke-dataset-object-detection-yolo"
source: "kaggle"
url: "https://www.kaggle.com/datasets/azimjaan21/fire-and-smoke-dataset-object-detection-yolo"
downloads: 4819
summary: "YOLO 기반 화재 및 연기 객체 탐지용 이미지 데이터셋으로 산업 안전과 산불 조기 감지에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[이미지 인식]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/azimjaan21/fire-and-smoke-dataset-object-detection-yolo

> dataset · [Kaggle](https://www.kaggle.com/datasets/azimjaan21/fire-and-smoke-dataset-object-detection-yolo)

YOLO 기반 화재 및 연기 객체 탐지용 이미지 데이터셋으로 산업 안전과 산불 조기 감지에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `object detection models, specifically YOLO, to identify fire and smoke` · 신뢰도 low
- **작업**: [[이미지 인식]] — tag_match · readme, tags = `object detection` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:vision = `High-quality images – Well-annotated dataset with bounding boxes for fire and smoke` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Annotations: Bounding box format (YOLO, COCO)` · 신뢰도 low
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `Community Data License Agreement - Permissive - Version 1.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Real-world diversity – Covers various environments (urban, forest, industrial, and indoor settings)` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The Fire & Smoke Detection Dataset is designed for training object detection models` · 신뢰도 medium
