---
type: "dataset"
id: "nvidia/Aegis-AI-Content-Safety-Dataset-1.0"
source: "huggingface"
url: "https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-1.0"
downloads: 1749
summary: "Nemotron Content Safety Dataset V1은 LLM과 인간 간 상호작용을 수집한 콘텐츠 안전성 데이터셋입니다."
readme_status: "ok"
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
# nvidia/Aegis-AI-Content-Safety-Dataset-1.0

> dataset · [Hugging Face](https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-1.0)

Nemotron Content Safety Dataset V1은 LLM과 인간 간 상호작용을 수집한 콘텐츠 안전성 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `approximately `11,000` manually annotated interactions between humans and LLMs` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `The samples are annotated with respect to the following taxonomy.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `361` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `split into `10,798` training samples and `1,199` test samples.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 1445자 ≈ 361 토큰 (viewer statistics, default/test)

## 이 데이터로 학습한 모델

- [[blackmallangcow__nari-decision-4b|blackmallangcow/nari-decision-4b]]
