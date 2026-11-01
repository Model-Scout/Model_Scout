---
type: "dataset"
id: "jaeyong2/FineFineWeb-Ko"
source: "huggingface"
url: "https://huggingface.co/datasets/jaeyong2/FineFineWeb-Ko"
downloads: 11
summary: "m-a-p/FineFineWeb-test 데이터셋을 Qwen2-72B-Instruct 모델로 번역한 한국어 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# jaeyong2/FineFineWeb-Ko

> dataset · [Hugging Face](https://huggingface.co/datasets/jaeyong2/FineFineWeb-Ko)

m-a-p/FineFineWeb-test 데이터셋을 Qwen2-72B-Instruct 모델로 번역한 한국어 데이터셋입니다.

## 분류

- **작업**: [[번역]] — ner · readme = `We used Qwen/Qwen2-72B-Instruct model to translate.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `source dataset from m-a-p/FineFineWeb-test` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `We used Qwen/Qwen2-72B-Instruct model to translate.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `4752` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `source dataset from m-a-p/FineFineWeb-test` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `en` 열 p90 7128자 ≈ 4752 토큰 (viewer statistics, default/train)
