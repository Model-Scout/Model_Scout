---
type: "dataset"
id: "Bingsu/calibration"
source: "huggingface"
url: "https://huggingface.co/datasets/Bingsu/calibration"
downloads: 90
summary: "Bingsu/calibration은 skt/kobest_v1 데이터셋의 boolq 훈련 데이터를 포함한 평가용 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[텍스트 파일]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Bingsu/calibration

> dataset · [Hugging Face](https://huggingface.co/datasets/Bingsu/calibration)

Bingsu/calibration은 skt/kobest_v1 데이터셋의 boolq 훈련 데이터를 포함한 평가용 데이터입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `boolq train` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `boolq train` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `boolq train` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `789` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **데이터 용도**: [[평가용]] — ner · readme = `boolq train` · 신뢰도 low
- **데이터 형식**: [[텍스트 파일]] — metadata · format = `text` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 1184자 ≈ 789 토큰 (viewer statistics, default/train)
