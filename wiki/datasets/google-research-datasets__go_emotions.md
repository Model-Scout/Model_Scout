---
type: "dataset"
id: "google-research-datasets/go_emotions"
source: "huggingface"
url: "https://huggingface.co/datasets/google-research-datasets/go_emotions"
downloads: 29084
summary: "GoEmotions는 27가지 감정 범주로 라벨링된 58k 개의 Reddit 댓글 데이터셋으로 감정 분류에 사용됩니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# google-research-datasets/go_emotions

> dataset · [Hugging Face](https://huggingface.co/datasets/google-research-datasets/go_emotions)

GoEmotions는 27가지 감정 범주로 라벨링된 58k 개의 Reddit 댓글 데이터셋으로 감정 분류에 사용됩니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories, task_ids = `text-classification` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Each instance is a reddit comment with a corresponding ID and one or more emotion annotations (or neutral).` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `This dataset is intended for multi-class, multi-label emotion classification.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `31` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The data is in English.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `The raw data is included as well as the smaller, simplified version of the dataset with predefined train/val/test splits.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 122자 ≈ 31 토큰 (viewer statistics, simplified/validation)

## 이 데이터로 학습한 모델

- [[Zeolit__lettuce-thymos-26m-v1|Zeolit/lettuce-thymos-26m-v1]]
