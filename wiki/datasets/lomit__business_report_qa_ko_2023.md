---
type: "dataset"
id: "lomit/business_report_qa_ko_2023"
source: "huggingface"
url: "https://huggingface.co/datasets/lomit/business_report_qa_ko_2023"
downloads: 7
summary: "한국어 기업 사업보고서 기반 질의응답 데이터셋으로 금융 분야에 활용됨."
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
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# lomit/business_report_qa_ko_2023

> dataset · [Hugging Face](https://huggingface.co/datasets/lomit/business_report_qa_ko_2023)

한국어 기업 사업보고서 기반 질의응답 데이터셋으로 금융 분야에 활용됨.

## 분류

- **작업**: [[질의응답]] — ner · readme = `lomit/business_report_qa_ko_2023` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `features:
- name: question
dtype: string
- name: answer
dtype: string
- name: input
dtype: string
- name: company
dtype: string` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `features:
- name: question
dtype: string
- name: answer
dtype: string
- name: input
dtype: string
- name: company
dtype: string` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `splits:
- name: train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
