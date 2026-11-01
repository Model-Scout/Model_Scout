---
type: "dataset"
id: "Jaeuk-Han/korean-traditional-liquor-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/Jaeuk-Han/korean-traditional-liquor-dataset"
downloads: 17
summary: "132개의 역사 문헌에서 수집한 한국 전통주와 양조 문화 말뭉치로, IR/RAG 및 문화·역사 분석에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[질의응답]]"
  - "[[문서 검색]]"
  - "[[요약]]"
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
  - "[[학술·논문]]"
  - "[[문화·관광]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Jaeuk-Han/korean-traditional-liquor-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/Jaeuk-Han/korean-traditional-liquor-dataset)

132개의 역사 문헌에서 수집한 한국 전통주와 양조 문화 말뭉치로, IR/RAG 및 문화·역사 분석에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **작업**: [[문서 검색]] — metadata · readme, task_categories = `text-retrieval` · 신뢰도 high
- **작업**: [[요약]] — metadata · task_categories = `summarization` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:question_answering, task:retrieval, task:summarization = `paragraph-level chunks for IR/RAG and document-/process-level metadata` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering, task:summarization = `paragraph-level chunks for IR/RAG and document-/process-level metadata` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `32` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-2.0` · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `historical texts written between 886 and 1947` · 신뢰도 low
- **도메인**: [[문화·관광]] — ner · readme = `A corpus of Korean traditional liquors and brewing culture` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Structured texts into JSONL/CSV/Parquet, normalized historical units (Mal/Doi → L), added English category labels, and derived per-docume` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `description` 열 p90 48자 ≈ 32 토큰 (viewer statistics, default/train)
