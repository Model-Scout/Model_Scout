---
type: "dataset"
id: "lbourdois/fineweb-2-trimming"
source: "huggingface"
url: "https://huggingface.co/datasets/lbourdois/fineweb-2-trimming"
downloads: 1265
summary: "124개 언어별 최대 20만 텍스트로 경량화한 FineWeb2 데이터셋, 모델 트리밍용"
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# lbourdois/fineweb-2-trimming

> dataset · [Hugging Face](https://huggingface.co/datasets/lbourdois/fineweb-2-trimming)

124개 언어별 최대 20만 텍스트로 경량화한 FineWeb2 데이터셋, 모델 트리밍용

## 분류

- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme = `For each of them we kept the first 200,000 texts` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `For each of them we kept the first 200,000 texts` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `124 languages` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[alphaedge-ai__Qwen3-Embedding-kor-32768|alphaedge-ai/Qwen3-Embedding-kor-32768]]
- [[alphaedge-ai__bge-m3-kor-32768|alphaedge-ai/bge-m3-kor-32768]]
- [[alphaedge-ai__multilingual-e5-base-kor-32768|alphaedge-ai/multilingual-e5-base-kor-32768]]
- [[alphaedge-ai__multilingual-e5-small-kor-32768|alphaedge-ai/multilingual-e5-small-kor-32768]]
