---
type: "dataset"
id: "datalama/RAG-Evaluation-Dataset-KO"
source: "huggingface"
url: "https://huggingface.co/datasets/datalama/RAG-Evaluation-Dataset-KO"
downloads: 212
summary: "allganize/RAG-Evaluation-Dataset-KO 기반 PDF 포함 한국어 RAG 평가 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[문서 검색]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# datalama/RAG-Evaluation-Dataset-KO

> dataset · [Hugging Face](https://huggingface.co/datasets/datalama/RAG-Evaluation-Dataset-KO)

allganize/RAG-Evaluation-Dataset-KO 기반 PDF 포함 한국어 RAG 평가 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `RAG Evaluation: 본 데이터는 한국어 RAG 파이프라인에 대한 E2E Evaluation이 가능합니다.` · 신뢰도 medium
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — ner · readme = `PDF 파일을 페이지 단위로 분리하였습니다.` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:retrieval = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `RAG Evaluation: 본 데이터는 한국어 RAG 파이프라인에 대한 E2E Evaluation이 가능합니다.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The dataset is in Korean (ko).` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `본 데이터셋은 allganize/RAG-Evaluation-Dataset-KO를 기반으로 PDF 파일을 포함하도록 재구성한 한국어 평가 데이터셋입니다.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
