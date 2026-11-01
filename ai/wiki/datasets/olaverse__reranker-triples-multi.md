---
type: "dataset"
id: "olaverse/reranker-triples-multi"
source: "huggingface"
url: "https://huggingface.co/datasets/olaverse/reranker-triples-multi"
downloads: 39
summary: "25개 언어의 쿼리-정답-유사오답 삼중항으로 크로스 인코더 리랭커 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[리랭킹]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# olaverse/reranker-triples-multi

> dataset · [Hugging Face](https://huggingface.co/datasets/olaverse/reranker-triples-multi)

25개 언어의 쿼리-정답-유사오답 삼중항으로 크로스 인코더 리랭커 학습용 데이터셋입니다.

## 분류

- **작업**: [[리랭킹]] — metadata · readme, tags, task_categories = `text-ranking` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:reranking = `(query, positive, negatives[5])` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `(query, positive, negatives[5])` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `25 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `460` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `Intended Use Pairwise or listwise ranking loss for cross-encoder reranker fine-tuning` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `positive` 열 p90 1841자 ≈ 460 토큰 (viewer statistics, default/train)
