---
type: "dataset"
id: "kaggle/jpjp0902/car-classification"
source: "kaggle"
url: "https://www.kaggle.com/datasets/jpjp0902/car-classification"
downloads: 256
summary: "한국에서 판매 중인 33개 자동차 모델 이미지로 차량 분류를 위한 데이터셋입니다."
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
  - "[[이용 조건 미확인]]"
domain:
  - "[[교통·모빌리티]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/jpjp0902/car-classification

> dataset · [Kaggle](https://www.kaggle.com/datasets/jpjp0902/car-classification)

한국에서 판매 중인 33개 자동차 모델 이미지로 차량 분류를 위한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — tag_match · readme, tags = `classification` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme = `33 Car Models Image Dataset` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `You can classify images by Convolutional Neural Networks.` · 신뢰도 low
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `Unknown` · 신뢰도 high
- **도메인**: [[교통·모빌리티]] — ner · readme = `33 different car models currently merchandising in South Korea.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is composed of 33 different car models` · 신뢰도 low
