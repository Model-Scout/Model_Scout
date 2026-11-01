---
type: "dataset"
id: "KETI-NLP/kor_race"
source: "huggingface"
url: "https://huggingface.co/datasets/KETI-NLP/kor_race"
downloads: 159
summary: "RACE 데이터셋은 비상업적 연구용으로 인터넷에서 수집한 지문과 문제로 구성된 영어 독해 평가 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# KETI-NLP/kor_race

> dataset · [Hugging Face](https://huggingface.co/datasets/KETI-NLP/kor_race)

RACE 데이터셋은 비상업적 연구용으로 인터넷에서 수집한 지문과 문제로 구성된 영어 독해 평가 데이터입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories, task_ids = `multiple-choice` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `All passages are obtained from the Internet which is not property of Carnegie Mellon University.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `All passages are obtained from the Internet which is not property of Carnegie Mellon University.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `730` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `RACE dataset is available for non-commercial research purpose only.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `RACE dataset is available for non-commercial research purpose only.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `article` 열 p90 1095자 ≈ 730 토큰 (viewer statistics, default/validation)
