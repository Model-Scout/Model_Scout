---
type: "dataset"
id: "won75/text_to_sql_ko"
source: "huggingface"
url: "https://huggingface.co/datasets/won75/text_to_sql_ko"
downloads: 26
summary: "한국어 자연어 질문을 MySQL 쿼리로 변환하는 모델 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# won75/text_to_sql_ko

> dataset · [Hugging Face](https://huggingface.co/datasets/won75/text_to_sql_ko)

한국어 자연어 질문을 MySQL 쿼리로 변환하는 모델 학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `This dataset is designed to train models that convert natural language questions in Korean into MySQL queries.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `589` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Korean Text to MySQL is a dataset comprising approximately 3,300 samples generated using OpenAI's gpt-4o model.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is designed to train models that convert natural language questions in Korean into MySQL queries.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `Schema` 열 p90 884자 ≈ 589 토큰 (viewer statistics, default/train)
