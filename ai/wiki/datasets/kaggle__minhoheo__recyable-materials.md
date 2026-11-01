---
type: "dataset"
id: "kaggle/minhoheo/recyable-materials"
source: "kaggle"
url: "https://www.kaggle.com/datasets/minhoheo/recyable-materials"
downloads: 10092
summary: "한국에서 촬영한 재활용품 이미지 데이터로 분류 모델 학습에 활용 가능"
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[환경·기상]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/minhoheo/recyable-materials

> dataset · [Kaggle](https://www.kaggle.com/datasets/minhoheo/recyable-materials)

한국에서 촬영한 재활용품 이미지 데이터로 분류 모델 학습에 활용 가능

## 분류

- **작업**: [[텍스트 분류]] — tag_match · readme, tags = `classification` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme = `All image files have jpeg format and resolution of 3024 × 3024x3, 3024 × 4032x3, and 4032 × 3024x3.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `classification, image, multiclass classification` · 신뢰도 low
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[환경·기상]] — tag_match · readme, tags = `environment` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `I hope it is useful to someone :)` · 신뢰도 low
