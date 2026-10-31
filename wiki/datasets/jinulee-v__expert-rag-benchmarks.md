---
type: "dataset"
id: "jinulee-v/expert-rag-benchmarks"
source: "huggingface"
url: "https://huggingface.co/datasets/jinulee-v/expert-rag-benchmarks"
downloads: 149
summary: "법률 분야 전문가 수준의 RAG 벤치마크 데이터셋으로, 법률 문서 검색 및 질의응답 연구용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[법률]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# jinulee-v/expert-rag-benchmarks

> dataset · [Hugging Face](https://huggingface.co/datasets/jinulee-v/expert-rag-benchmarks)

법률 분야 전문가 수준의 RAG 벤치마크 데이터셋으로, 법률 문서 검색 및 질의응답 연구용입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `The collection is intended for research on retrieval and retrieval-augmented generation in expert legal domains.` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 medium
- **작업**: [[문서 검색]] — metadata · readme, tags, task_categories = `text-retrieval` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering, task:retrieval = `questions, documents, and qrels.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `questions, documents, and qrels.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `155` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · readme, tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `The KCL split is named kcl_essay because Hugging Face split identifiers do not permit hyphens; its source name remains kcl-essay.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The KCL split is named kcl_essay because Hugging Face split identifiers do not permit hyphens; its source name remains kcl-essay.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `meta_json` 열 p90 232자 ≈ 155 토큰 (viewer statistics, questions/housing)
