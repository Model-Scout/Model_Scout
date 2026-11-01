---
type: "dataset"
id: "NickyNicky/oasst2_clusters"
source: "huggingface"
url: "https://huggingface.co/datasets/NickyNicky/oasst2_clusters"
downloads: 27
summary: "텍스트 클러스터링 데이터셋으로, 클러스터별 텍스트와 감성 정보를 포함함."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# NickyNicky/oasst2_clusters

> dataset · [Hugging Face](https://huggingface.co/datasets/NickyNicky/oasst2_clusters)

텍스트 클러스터링 데이터셋으로, 클러스터별 텍스트와 감성 정보를 포함함.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `features: ['Text', 'Cluster', 'Polarity', 'count_word']` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `features: ['Text', 'Cluster', 'Polarity', 'count_word']` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `features: ['Text', 'Cluster', 'Polarity', 'count_word']` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `26 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `920` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `DatasetDict({ Cluster_1: Dataset({ features: ['Text', 'Cluster', 'Polarity', 'count_word'], num_rows: 4797 }) Cluster_2: Dataset({ features: ['Text', 'Cluster',` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `Text` 열 p90 3681자 ≈ 920 토큰 (viewer statistics, default/Cluster_1)
