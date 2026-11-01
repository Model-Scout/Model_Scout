---
type: "dataset"
id: "youjunhyeok/glaiveai-reflection-v1-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/youjunhyeok/glaiveai-reflection-v1-ko"
downloads: 28
summary: "glaiveai/reflection-v1 데이터를 영어에서 한국어로 번역한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
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
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# youjunhyeok/glaiveai-reflection-v1-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/youjunhyeok/glaiveai-reflection-v1-ko)

glaiveai/reflection-v1 데이터를 영어에서 한국어로 번역한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `For this dataset, we only used data that is 5000 characters or less in length and has language of English.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Translated glaiveai/reflection-v1 using nayohan/llama3-instrucTrans-enko-8b.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1746` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `For this dataset, we only used data that is 5000 characters or less in length and has language of English.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `response` 열 p90 2619자 ≈ 1746 토큰 (viewer statistics, default/train)
