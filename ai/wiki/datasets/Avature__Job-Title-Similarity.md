---
type: "dataset"
id: "Avature/Job-Title-Similarity"
source: "huggingface"
url: "https://huggingface.co/datasets/Avature/Job-Title-Similarity"
downloads: 475
summary: "11개 언어로 된 직무명 유사도 벤치마크 데이터셋으로 직무명 의미 유사도 평가에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
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
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[상거래·상품]]"
dataset_role:
  - "[[평가용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Avature/Job-Title-Similarity

> dataset · [Hugging Face](https://huggingface.co/datasets/Avature/Job-Title-Similarity)

11개 언어로 된 직무명 유사도 벤치마크 데이터셋으로 직무명 의미 유사도 평가에 사용됨.

## 분류

- **작업**: [[임베딩]] — metadata · task_categories = `sentence-similarity` · 신뢰도 low
- **작업**: [[리랭킹]] — ner · readme = `The task involves ranking a set of job titles, given another job title as query, such that the resulting ranking reflects the semantic similarity of each job ti` · 신뢰도 low
- **작업**: [[문서 검색]] — metadata · task_categories = `text-retrieval` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:reranking, task:retrieval = `job titles (short text phrases with the name of an occupation)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Indices of relevant corpus job titles` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `11 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `2` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `job title similarity datasets` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `including the English evaluation dataset used in the text ranking experiments` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 10자 ≈ 2 토큰 (viewer statistics, ko/queries)
