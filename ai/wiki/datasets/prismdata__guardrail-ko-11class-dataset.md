---
type: "dataset"
id: "prismdata/guardrail-ko-11class-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/prismdata/guardrail-ko-11class-dataset"
downloads: 46
summary: "한국어 혐오발언과 프롬프트 인젝션 탐지용 11개 클래스 텍스트 분류 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# prismdata/guardrail-ko-11class-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/prismdata/guardrail-ko-11class-dataset)

한국어 혐오발언과 프롬프트 인젝션 탐지용 11개 클래스 텍스트 분류 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `11-class 텍스트 분류 데이터셋입니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `11-class 텍스트 분류 데이터셋입니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `152` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `gpl-3.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 혐오발언과 프롬프트 인젝션을 탐지하기 위한 11-class 텍스트 분류 데이터셋입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `LLM 가드레일 모델 학습에 사용되며, 안전한 AI 시스템 구축을 목표로 합니다.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 228자 ≈ 152 토큰 (viewer statistics, default/validation)
