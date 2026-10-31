---
type: "dataset"
id: "gretelai/synthetic_text_to_sql"
source: "huggingface"
url: "https://huggingface.co/datasets/gretelai/synthetic_text_to_sql"
downloads: 4262
summary: "Gretel Navigator로 생성한 고품질 합성 Text-to-SQL 데이터셋으로 SQL 생성 모델 학습용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[표 질의응답]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# gretelai/synthetic_text_to_sql

> dataset · [Hugging Face](https://huggingface.co/datasets/gretelai/synthetic_text_to_sql)

Gretel Navigator로 생성한 고품질 합성 Text-to-SQL 데이터셋으로 SQL 생성 모델 학습용입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 medium
- **작업**: [[표 질의응답]] — metadata · task_categories = `table-question-answering` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — task_rule · task:table_qa = `table` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering, task:table_qa = `synthetic Text-to-SQL samples` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering, task:table_qa = `Natural language explanations of what the SQL query is doing` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `118` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Coverage across 100 distinct domains/verticals` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `105,851 records partitioned into 100,000 train and 5,851 test records` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `sql_context` 열 p90 472자 ≈ 118 토큰 (viewer statistics, default/test)

## 이 데이터로 학습한 모델

- [[Ellbendls__Qwen-2.5-3b-Text_to_SQL|Ellbendls/Qwen-2.5-3b-Text_to_SQL]]
- [[Ellbendls__Qwen-3-4b-Text_to_SQL|Ellbendls/Qwen-3-4b-Text_to_SQL]]
