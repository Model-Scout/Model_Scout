---
type: "dataset"
id: "mariem123kfg/fine-tuning-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/mariem123kfg/fine-tuning-dataset"
downloads: 24
summary: "JSON 추출 및 수정 작업을 위한 내부 파인튜닝 데이터셋으로 CAREBench 모델 학습용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# mariem123kfg/fine-tuning-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/mariem123kfg/fine-tuning-dataset)

JSON 추출 및 수정 작업을 위한 내부 파인튜닝 데이터셋으로 CAREBench 모델 학습용입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Internal fine-tuning corpus for JSON extraction and JSON repair tasks` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `context, question, json_schema` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `A valid JSON object matching the schema (`validated_output`)` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `59409` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Internal fine-tuning corpus for JSON extraction and JSON repair tasks` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `context` 열 p90 89113자 ≈ 59409 토큰 (viewer statistics, default/train)
