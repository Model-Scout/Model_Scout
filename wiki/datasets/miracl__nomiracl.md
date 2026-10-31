---
type: "dataset"
id: "miracl/nomiracl"
source: "huggingface"
url: "https://huggingface.co/datasets/miracl/nomiracl"
downloads: 1578
summary: "NoMIRACL은 18개 언어의 LLM 검색 결과 관련성 평가를 위한 인간 주석 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[리랭킹]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# miracl/nomiracl

> dataset · [Hugging Face](https://huggingface.co/datasets/miracl/nomiracl)

NoMIRACL은 18개 언어의 LLM 검색 결과 관련성 평가를 위한 인간 주석 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 high
- **작업**: [[리랭킹]] — ner · readme = `evaluating query-passage relevance across diverse language families` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `evaluating query-passage relevance across diverse language families` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:reranking, task:retrieval = `topics, qrels, and top-k (a maximum of 10) annotated passages` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `LLM relevance as a binary classification objective` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `16 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `evaluating query-passage relevance across diverse language families` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `a completely human-annotated dataset designed for evaluating multilingual LLM relevance` · 신뢰도 low
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
