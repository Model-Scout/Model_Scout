---
type: "dataset"
id: "brainer/health_checkup"
source: "huggingface"
url: "https://huggingface.co/datasets/brainer/health_checkup"
downloads: 9
summary: "한국 건강검진 데이터를 포함하며 건강 상태 분석에 활용되는 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[표 데이터 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# brainer/health_checkup

> dataset · [Hugging Face](https://huggingface.co/datasets/brainer/health_checkup)

한국 건강검진 데이터를 포함하며 건강 상태 분석에 활용되는 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — metadata · task_categories = `feature-extraction` · 신뢰도 low
- **작업**: [[표 데이터 예측]] — metadata · task_categories = `tabular-classification` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality, task:tabular_prediction = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding = `features: ['기준년도', '가입자 일련번호', '시도코드', '성별코드', '연령대코드(5세 단위)', '신장(5cm 단위)', '체중(5kg 단위)', '허리둘레', '시력(좌)', '시력(우)', '청력(좌)', '청력(우)', '수축기 혈압', '이완기 혈압', '식전혈당` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `features: ['기준년도', '가입자 일련번호', '시도코드', '성별코드', '연령대코드(5세 단위)', '신장(5cm 단위)', '체중(5kg 단위)', '허리둘레', '시력(좌)', '시력(우)', '청력(좌)', '청력(우)', '수축기 혈압', '이완기 혈압', '식전혈당` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[의료·보건]] — tag_match · tags = `health` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `print(health_checkup_ds, hp_t20_ds, hp_t60_ds)` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high
