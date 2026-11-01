---
type: "dataset"
id: "kaggle/metformin/bigdata-test-example-data"
source: "kaggle"
url: "https://www.kaggle.com/datasets/metformin/bigdata-test-example-data"
downloads: 469
summary: "한국 빅데이터 분석가 시험용 예제 데이터로 성별 예측 모델 구축에 활용됨."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[표 데이터 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/metformin/bigdata-test-example-data

> dataset · [Kaggle](https://www.kaggle.com/datasets/metformin/bigdata-test-example-data)

한국 빅데이터 분석가 시험용 예제 데이터로 성별 예측 모델 구축에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `성별예측 모형을 만든 후, 이를 평가용 데이터(X_test.csv)에 적용하여 얻은 2,482명 고객의 성별 예측값` · 신뢰도 low
- **작업**: [[표 데이터 예측]] — ner · readme = `고객의 상품구매 속성 (학습용 및 평가용), CSV 형식의 파일` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme, task:tabular_prediction = `CSV 형식의 파일` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `다음과 같은 형식의 CSV 파일로 생성하시오` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `Other (specified in description)` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Example Dataset of Korean Bigdata Analyst Test` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `고객 3,500명에 대한 학습용 데이터(y_train.csv, X_train.csv)를 이용하여 성별예측 모형을 만든 후` · 신뢰도 medium
