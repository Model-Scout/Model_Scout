---
type: "dataset"
id: "castorini/mr-tydi"
source: "huggingface"
url: "https://huggingface.co/datasets/castorini/mr-tydi"
downloads: 5683
summary: "Mr. TyDi는 11개 언어의 단일언어 검색 평가용 다국어 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[문서 검색]]"
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
dataset_size:
  - "[[중규모 데이터]]"
---
# castorini/mr-tydi

> dataset · [Hugging Face](https://huggingface.co/datasets/castorini/mr-tydi)

Mr. TyDi는 11개 언어의 단일언어 검색 평가용 다국어 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — metadata · readme, task_categories = `text-retrieval` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:retrieval = `This dataset stores the queries, judgements, and example training data of Mr. TyDi.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `It is designed for monolingual retrieval, specifically to evaluate ranking with learned dense representations.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `11 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `9` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Mr. TyDi is a multi-lingual benchmark dataset built on TyDi, covering eleven typologically diverse languages.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The only configuration here is the `language`, For each language, there are three splits: `train`, `dev`, and `test`.` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `query` 열 p90 35자 ≈ 9 토큰 (viewer statistics, korean/test)
