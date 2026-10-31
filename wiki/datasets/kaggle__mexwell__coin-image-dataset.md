---
type: "dataset"
id: "kaggle/mexwell/coin-image-dataset"
source: "kaggle"
url: "https://www.kaggle.com/datasets/mexwell/coin-image-dataset"
downloads: 623
summary: "로마 공화국 시대 동전 60종의 뒷면 이미지로 구성된 동전 이미지 데이터셋입니다."
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
# kaggle/mexwell/coin-image-dataset

> dataset · [Kaggle](https://www.kaggle.com/datasets/mexwell/coin-image-dataset)

로마 공화국 시대 동전 60종의 뒷면 이미지로 구성된 동전 이미지 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `image classification` · 신뢰도 medium
- **작업**: [[이미지 인식]] — tag_match · tags = `image classification` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:vision = `coin images of the reverse side` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `maps the class-IDs to the reference numbers` · 신뢰도 low
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `Attribution 4.0 International (CC BY 4.0)` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `people, people and society` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `image classification, image augmentation, image segmentation` · 신뢰도 low
