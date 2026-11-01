---
type: "dataset"
id: "kaggle/nafisanaimahoquec/nafisa-naima-hoques-project"
source: "kaggle"
url: "https://www.kaggle.com/datasets/nafisanaimahoquec/nafisa-naima-hoques-project"
downloads: 4
summary: "중국, 한국, 일본 남성과 방글라데시 여성의 다인종 인물 이미지 1500장 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[이미지 인식]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/nafisanaimahoquec/nafisa-naima-hoques-project

> dataset · [Kaggle](https://www.kaggle.com/datasets/nafisanaimahoquec/nafisa-naima-hoques-project)

중국, 한국, 일본 남성과 방글라데시 여성의 다인종 인물 이미지 1500장 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `image classification` · 신뢰도 medium
- **작업**: [[이미지 인식]] — tag_match · tags = `image classification` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:vision = `Multiracial people with 100 images` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `image classification` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `Unknown` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `This is beginner friendly and low cpu,gpu consuming dataset.` · 신뢰도 low
