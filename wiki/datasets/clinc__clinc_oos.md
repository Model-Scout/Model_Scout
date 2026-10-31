---
type: "dataset"
id: "clinc/clinc_oos"
source: "huggingface"
url: "https://huggingface.co/datasets/clinc/clinc_oos"
downloads: 25614
summary: "CLINC150은 대화 시스템의 지원 의도 범위 밖 쿼리를 포함한 텍스트 분류 데이터셋입니다."
readme_status: "template"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# clinc/clinc_oos

> dataset · [Hugging Face](https://huggingface.co/datasets/clinc/clinc_oos)

CLINC150은 대화 시스템의 지원 의도 범위 밖 쿼리를 포함한 텍스트 분류 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories, task_ids = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `current text classification corpora only define label sets that cover every example` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `current text classification corpora only define label sets that cover every example` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `15` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-3.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 61자 ≈ 15 토큰 (viewer statistics, imbalanced/validation)

## 이 데이터로 학습한 모델

- [[blackmallangcow__nari-decision-4b|blackmallangcow/nari-decision-4b]]
