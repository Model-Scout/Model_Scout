---
type: "dataset"
id: "google-research-datasets/paws"
source: "huggingface"
url: "https://huggingface.co/datasets/google-research-datasets/paws"
downloads: 115113
summary: "PAWS 데이터셋은 단어 순서와 문맥 정보를 활용한 패러프레이즈 식별용 문장 쌍 데이터입니다."
readme_status: "template"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# google-research-datasets/paws

> dataset · [Hugging Face](https://huggingface.co/datasets/google-research-datasets/paws)

PAWS 데이터셋은 단어 순서와 문맥 정보를 활용한 패러프레이즈 식별용 문장 쌍 데이터입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories, task_ids = `text-classification` · 신뢰도 medium
- **작업**: [[임베딩]] — metadata · task_ids = `semantic-similarity-scoring` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding = `pairs that feature the importance of modeling structure, context, and word order information` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `pairs that feature the importance of modeling structure, context, and word order information` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `39` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `based on Wikipedia and the other one based on the Quora Question Pairs (QQP) dataset` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `108,463 human-labeled and 656k noisily labeled pairs` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `sentence1` 열 p90 157자 ≈ 39 토큰 (viewer statistics, labeled_final/validation)
