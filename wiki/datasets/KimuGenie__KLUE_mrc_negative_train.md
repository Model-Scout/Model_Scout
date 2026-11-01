---
type: "dataset"
id: "KimuGenie/KLUE_mrc_negative_train"
source: "huggingface"
url: "https://huggingface.co/datasets/KimuGenie/KLUE_mrc_negative_train"
downloads: 26
summary: "KLUE mrc 학습 데이터에 BM25로 찾은 hard negative 텍스트 20개를 추가한 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
  - "[[문서 검색]]"
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
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# KimuGenie/KLUE_mrc_negative_train

> dataset · [Hugging Face](https://huggingface.co/datasets/KimuGenie/KLUE_mrc_negative_train)

KLUE mrc 학습 데이터에 BM25로 찾은 hard negative 텍스트 20개를 추가한 데이터입니다.

## 분류

- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `KLUE mrc train dataset에 BM25을 이용해서 question에 대한 hard negative text 20개를 추가한 데이터입니다.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering, task:retrieval = `KLUE mrc train dataset에 BM25을 이용해서 question에 대한 hard negative text 20개를 추가한 데이터입니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `KLUE mrc train dataset에 BM25을 이용해서 question에 대한 hard negative text 20개를 추가한 데이터입니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `982` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `KLUE mrc train dataset에 BM25을 이용해서 question에 대한 hard negative text 20개를 추가한 데이터입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `KLUE mrc train dataset에 BM25을 이용해서 question에 대한 hard negative text 20개를 추가한 데이터입니다.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `context` 열 p90 1473자 ≈ 982 토큰 (viewer statistics, default/validation)
