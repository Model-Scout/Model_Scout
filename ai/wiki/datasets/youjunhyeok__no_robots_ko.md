---
type: "dataset"
id: "youjunhyeok/no_robots_ko"
source: "huggingface"
url: "https://huggingface.co/datasets/youjunhyeok/no_robots_ko"
downloads: 31
summary: "GPT o4-mini 모델로 HuggingFaceH4/no_robots 데이터셋을 한국어로 번역한 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[비상업 전용]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# youjunhyeok/no_robots_ko

> dataset · [Hugging Face](https://huggingface.co/datasets/youjunhyeok/no_robots_ko)

GPT o4-mini 모델로 HuggingFaceH4/no_robots 데이터셋을 한국어로 번역한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:translation = `GPT o4-mini 모델을 사용하여 HuggingFaceH4/no_robots 데이터셋을 번역하였습니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:translation = `GPT o4-mini 모델을 사용하여 HuggingFaceH4/no_robots 데이터셋을 번역하였습니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `655` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `GPT o4-mini 모델을 사용하여 HuggingFaceH4/no_robots 데이터셋을 번역하였습니다.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `prompt` 열 p90 982자 ≈ 655 토큰 (viewer statistics, default/train)
