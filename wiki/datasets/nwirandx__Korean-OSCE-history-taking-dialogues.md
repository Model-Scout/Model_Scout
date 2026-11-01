---
type: "dataset"
id: "nwirandx/Korean-OSCE-history-taking-dialogues"
source: "huggingface"
url: "https://huggingface.co/datasets/nwirandx/Korean-OSCE-history-taking-dialogues"
downloads: 135
summary: "GPT-4o 가상 표준 환자와의 한국어 OSCE 병력 청취 대화 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
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
  - "[[의료·보건]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# nwirandx/Korean-OSCE-history-taking-dialogues

> dataset · [Hugging Face](https://huggingface.co/datasets/nwirandx/Korean-OSCE-history-taking-dialogues)

GPT-4o 가상 표준 환자와의 한국어 OSCE 병력 청취 대화 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `49 text-based history-taking dialogue sessions` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `GPT-4o VSP response (Korean original)` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `67` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[의료·보건]] — tag_match · tags = `medical` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `Released as the empirical evaluation dataset accompanying A Stratified Multi-Rater Evaluation of LLM-Based Virtual Standardized Patients` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `translated_answer` 열 p90 100자 ≈ 67 토큰 (viewer statistics, default/sessions)
