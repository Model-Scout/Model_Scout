---
type: "dataset"
id: "kaggle/aniss7/gtav-legacy-dataset-for-visual-place-recognition"
source: "kaggle"
url: "https://www.kaggle.com/datasets/aniss7/gtav-legacy-dataset-for-visual-place-recognition"
downloads: 52
summary: "GTA V 레거시 버전에서 촬영한 이미지로 시각적 장소 인식 연구용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[문서 검색]]"
  - "[[이미지 인식]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/aniss7/gtav-legacy-dataset-for-visual-place-recognition

> dataset · [Kaggle](https://www.kaggle.com/datasets/aniss7/gtav-legacy-dataset-for-visual-place-recognition)

GTA V 레거시 버전에서 촬영한 이미지로 시각적 장소 인식 연구용 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `Images from Grand Theft Auto V Legacy for visual place recognition (GTAV-VPR)` · 신뢰도 low
- **작업**: [[이미지 인식]] — tag_match · tags = `image classification` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:vision = `Images from Grand Theft Auto V Legacy for visual place recognition (GTAV-VPR)` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:retrieval = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `6dpose_list.txt contains the 6DOF camera poses for each image in the corresponding folder.` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Images from Grand Theft Auto V Legacy for visual place recognition (GTAV-VPR)` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset contains the following: 1. Legacy Dataset: The original dataset made on the legacy version of GTA V.` · 신뢰도 low
