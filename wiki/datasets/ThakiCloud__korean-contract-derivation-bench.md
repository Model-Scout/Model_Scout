---
type: "dataset"
id: "ThakiCloud/korean-contract-derivation-bench"
source: "huggingface"
url: "https://huggingface.co/datasets/ThakiCloud/korean-contract-derivation-bench"
downloads: 97
summary: "한국어 계약서 요약에서 계약금액 도출 정확도를 평가하는 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[법률]]"
dataset_role:
  - "[[평가용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# ThakiCloud/korean-contract-derivation-bench

> dataset · [Hugging Face](https://huggingface.co/datasets/ThakiCloud/korean-contract-derivation-bench)

한국어 계약서 요약에서 계약금액 도출 정확도를 평가하는 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · tags, task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **작업**: [[문서 검색]] — tag_match · tags = `rag` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering, task:retrieval = `240 synthetic Korean procurement summaries.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `answer_krw` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[법률]] — ner · readme = `Korean Contract Derivation Benchmark` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `This benchmark isolates that.` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
