---
type: "dataset"
id: "Squezilia/Route4Secure"
source: "huggingface"
url: "https://huggingface.co/datasets/Squezilia/Route4Secure"
downloads: 111
summary: "Route4Secure는 다국어 LLM 프롬프트 복잡도, 의도, 안전성 라우팅을 위한 대규모 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
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
# Squezilia/Route4Secure

> dataset · [Hugging Face](https://huggingface.co/datasets/Squezilia/Route4Secure)

Route4Secure는 다국어 LLM 프롬프트 복잡도, 의도, 안전성 라우팅을 위한 대규모 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Raw user prompt text to be classified/routed` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Primary task intent category` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `12 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `149` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `multilingual dataset designed for training unified LLM prompt routers and safety guardrails` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Main training dataset` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `reason` 열 p90 597자 ≈ 149 토큰 (viewer statistics, default/train)
