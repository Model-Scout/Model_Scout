---
type: "dataset"
id: "KICJ/legal_qa_ko"
source: "huggingface"
url: "https://huggingface.co/datasets/KICJ/legal_qa_ko"
downloads: 53
summary: "한국형사정책연구원(KICJ)의 10년간 연구보고서 30편과 GPT4o 기반 Q/A 세트 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[법률]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# KICJ/legal_qa_ko

> dataset · [Hugging Face](https://huggingface.co/datasets/KICJ/legal_qa_ko)

한국형사정책연구원(KICJ)의 10년간 연구보고서 30편과 GPT4o 기반 Q/A 세트 데이터입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `augmented with a Q/A set using GPT4o based on each research report page` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `augmented with a Q/A set using GPT4o based on each research report page` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `2242` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · readme, tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This is a dataset of 30 research reports published by the Korea Institute of Criminal Justice and Public Policy (KICJ) over the past 10 years, augmented with a ` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `Chunk Context` 열 p90 3363자 ≈ 2242 토큰 (viewer statistics, A Study on Reasoning in Investigation as a Legal Reasoning/train)
