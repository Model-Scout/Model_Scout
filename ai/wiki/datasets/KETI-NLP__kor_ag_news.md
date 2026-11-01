---
type: "dataset"
id: "KETI-NLP/kor_ag_news"
source: "huggingface"
url: "https://huggingface.co/datasets/KETI-NLP/kor_ag_news"
downloads: 34
summary: "1백만 개 이상의 뉴스 기사로 구성된 AG 뉴스 데이터셋으로 텍스트 분류 및 정보 검색 연구에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[뉴스·미디어]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# KETI-NLP/kor_ag_news

> dataset · [Hugging Face](https://huggingface.co/datasets/KETI-NLP/kor_ag_news)

1백만 개 이상의 뉴스 기사로 구성된 AG 뉴스 데이터셋으로 텍스트 분류 및 정보 검색 연구에 사용됨.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories, task_ids = `text-classification` · 신뢰도 high
- **작업**: [[문서 검색]] — ner · readme = `information retrieval (ranking, search, etc)` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:retrieval = `The AG's news topic classification dataset is constructed by Xiang Zhang` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `The AG's news topic classification dataset is constructed by Xiang Zhang` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `133` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `unknown` · 신뢰도 high
- **도메인**: [[뉴스·미디어]] — ner · readme = `AG is a collection of more than 1 million news articles.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The dataset is provided by the academic comunity for research purposes in data mining (clustering, classification, etc), information retrieval` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 199자 ≈ 133 토큰 (viewer statistics, default/test)
