---
type: "dataset"
id: "kaggle/yeeeengyu/cloud-classification-dataset"
source: "kaggle"
url: "https://www.kaggle.com/datasets/yeeeengyu/cloud-classification-dataset"
downloads: 186
summary: "YOLO11v로 학습하는 구름 양에 따른 맑음, 흐림, 비 분류 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/yeeeengyu/cloud-classification-dataset

> dataset · [Kaggle](https://www.kaggle.com/datasets/yeeeengyu/cloud-classification-dataset)

YOLO11v로 학습하는 구름 양에 따른 맑음, 흐림, 비 분류 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — tag_match · readme, tags = `classification` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme = `image` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `맑음, 흐림, 비오는 날씨 3개의 클래스로 구분합니다` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `Other (specified in description)` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `train, validation, test 각각 8:1:1의 비율로 배치됩니다` · 신뢰도 medium
