---
type: "dataset"
id: "nlpai-lab/miracl-multilingual-triplets"
source: "huggingface"
url: "https://huggingface.co/datasets/nlpai-lab/miracl-multilingual-triplets"
downloads: 592
summary: "51개 언어로 된 MIRACL 삼중항 데이터셋으로 다국어 검색 및 리랭킹 모델 학습용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[리랭킹]]"
  - "[[문서 검색]]"
  - "[[번역]]"
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
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# nlpai-lab/miracl-multilingual-triplets

> dataset · [Hugging Face](https://huggingface.co/datasets/nlpai-lab/miracl-multilingual-triplets)

51개 언어로 된 MIRACL 삼중항 데이터셋으로 다국어 검색 및 리랭킹 모델 학습용입니다.

## 분류

- **작업**: [[임베딩]] — tag_match · readme, tags = `triplet` · 신뢰도 medium
- **작업**: [[리랭킹]] — metadata · readme, tags, task_categories = `text-ranking` · 신뢰도 high
- **작업**: [[문서 검색]] — metadata · readme, tags, task_categories = `text-retrieval` · 신뢰도 high
- **작업**: [[번역]] — metadata · tags, task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:embedding, task:reranking, task:retrieval, task:translation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:translation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `51 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `158` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `MIRACL Triplets in 51 Languages is a multilingual retrieval and reranking dataset` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Split: `train`` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `positive` 열 p90 631자 ≈ 158 토큰 (viewer statistics, ko/train)
