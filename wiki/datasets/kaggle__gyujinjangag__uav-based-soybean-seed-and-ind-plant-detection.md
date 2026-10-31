---
type: "dataset"
id: "kaggle/gyujinjangag/uav-based-soybean-seed-and-ind-plant-detection"
source: "kaggle"
url: "https://www.kaggle.com/datasets/gyujinjangag/uav-based-soybean-seed-and-ind-plant-detection"
summary: "UAV로 촬영한 콩 식물의 씨앗과 개체별 식물 경계 상자 주석 데이터로, 식물 표현형 분석과 수량 예측에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[정보 추출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[환경·기상]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/gyujinjangag/uav-based-soybean-seed-and-ind-plant-detection

> dataset · [Kaggle](https://www.kaggle.com/datasets/gyujinjangag/uav-based-soybean-seed-and-ind-plant-detection)

UAV로 촬영한 콩 식물의 씨앗과 개체별 식물 경계 상자 주석 데이터로, 식물 표현형 분석과 수량 예측에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `object detection/counting, multi-task deep learning (joint point + box detection)` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `supports research in UAV-based crop phenotyping` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `annotated at two levels: seed-level point annotations and individual plant-level bounding boxes` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:embedding, task:information_extraction = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `seed-level point annotations and individual plant-level bounding boxes` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC BY-SA 4.0` · 신뢰도 high
- **도메인**: [[환경·기상]] — ner · readme = `soybean (Glycine max L.) plants at the reproductive stage` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `651 images, manually annotated using Labelme` · 신뢰도 low
