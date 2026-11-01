---
type: "dataset"
id: "sonsdf/k-ifrs-qa-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/sonsdf/k-ifrs-qa-dataset"
downloads: 16
summary: "한국채택국제회계기준(K-IFRS) 기반 QA 데이터셋으로 회계 도메인 LLM 파인튜닝 등에 활용 가능"
readme_status: "ok"
readme_language: "mixed"
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
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# sonsdf/k-ifrs-qa-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/sonsdf/k-ifrs-qa-dataset)

한국채택국제회계기준(K-IFRS) 기반 QA 데이터셋으로 회계 도메인 LLM 파인튜닝 등에 활용 가능

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 high
- **작업**: [[문서 검색]] — tag_match · tags = `RAG` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering, task:retrieval = `Instruction-Input-Output (Alpaca 형식)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `Instruction-Input-Output (Alpaca 형식)` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `64` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `Validation 분할 약 3,442개 (10%)` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Train 분할 약 30,976개 (90%)` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 96자 ≈ 64 토큰 (viewer statistics, default/train)
