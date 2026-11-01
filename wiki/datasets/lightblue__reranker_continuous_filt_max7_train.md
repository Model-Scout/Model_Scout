---
type: "dataset"
id: "lightblue/reranker_continuous_filt_max7_train"
source: "huggingface"
url: "https://huggingface.co/datasets/lightblue/reranker_continuous_filt_max7_train"
downloads: 178
summary: "95개 언어 35개 데이터셋에서 쿼리-텍스트 쌍을 수집해 리랭커 학습용 점수 데이터를 생성한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[리랭킹]]"
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
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# lightblue/reranker_continuous_filt_max7_train

> dataset · [Hugging Face](https://huggingface.co/datasets/lightblue/reranker_continuous_filt_max7_train)

95개 언어 35개 데이터셋에서 쿼리-텍스트 쌍을 수집해 리랭커 학습용 점수 데이터를 생성한 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `we mined hard negatives using the BAAI/bge-m3 embedding model` · 신뢰도 medium
- **작업**: [[리랭킹]] — ner · readme = `Reranker training data` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:reranking = `queries and corresponding text data` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `rate the relatedness of each query-text pair using a token "1", "2"…` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `96 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `942` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `We gathered queries and corresponding text data from 35 high quality datasets covering more than 95 languages.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `Reranker training data` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `context` 열 p90 3768자 ≈ 942 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[QuantFactory__lb-reranker-0.5B-v1.0-GGUF|QuantFactory/lb-reranker-0.5B-v1.0-GGUF]]
