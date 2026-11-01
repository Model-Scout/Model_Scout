---
type: "dataset"
id: "sosoai/dataset_ko_Ultrafeedback_binarized_test"
source: "huggingface"
url: "https://huggingface.co/datasets/sosoai/dataset_ko_Ultrafeedback_binarized_test"
downloads: 11
summary: "Ultrafeedback_binarized 데이터셋의 번역 및 정제된 테스트용 데이터로 모델 학습에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# sosoai/dataset_ko_Ultrafeedback_binarized_test

> dataset · [Hugging Face](https://huggingface.co/datasets/sosoai/dataset_ko_Ultrafeedback_binarized_test)

Ultrafeedback_binarized 데이터셋의 번역 및 정제된 테스트용 데이터로 모델 학습에 사용됨.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `This is the only test dataset and will use for train our own model.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `The provided data is a dataset that has been translated and refined using the Synatra-7B-Translation model` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `The provided data is a dataset that has been translated and refined using the Synatra-7B-Translation model` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `2999` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[평가용]] — ner · readme = `This is the only test dataset and will use for train our own model.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `chosen` 열 p90 4499자 ≈ 2999 토큰 (viewer statistics, default/train)
