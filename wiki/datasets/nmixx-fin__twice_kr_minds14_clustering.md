---
type: "dataset"
id: "nmixx-fin/twice_kr_minds14_clustering"
source: "huggingface"
url: "https://huggingface.co/datasets/nmixx-fin/twice_kr_minds14_clustering"
downloads: 16
summary: "AIHub 금융/보험 분야 민원 Q&A에서 사용자 의도 클러스터링용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# nmixx-fin/twice_kr_minds14_clustering

> dataset · [Hugging Face](https://huggingface.co/datasets/nmixx-fin/twice_kr_minds14_clustering)

AIHub 금융/보험 분야 민원 Q&A에서 사용자 의도 클러스터링용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Constructed a dataset for clustering user intents based on their queries.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Utilized user questions and intents from the 'Finance/Insurance' category` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Constructed a dataset for clustering user intents based on their queries.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Constructed a dataset for clustering user intents based on their queries.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
