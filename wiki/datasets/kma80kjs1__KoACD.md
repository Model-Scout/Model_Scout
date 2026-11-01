---
type: "dataset"
id: "kma80kjs1/KoACD"
source: "huggingface"
url: "https://huggingface.co/datasets/kma80kjs1/KoACD"
downloads: 29
summary: "KoACD는 한국 청소년의 인지 왜곡 분석을 위한 대규모 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# kma80kjs1/KoACD

> dataset · [Hugging Face](https://huggingface.co/datasets/kma80kjs1/KoACD)

KoACD는 한국 청소년의 인지 왜곡 분석을 위한 대규모 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories, task_ids = `text-classification` · 신뢰도 medium
- **작업**: [[텍스트 생성]] — tag_match · tags = `llm` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `Data was collected from NAVER Knowledge iN (Q&A platform)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `containing 108,717 instances across 10 distortion types` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `99` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[의료·보건]] — ner · readme = `KoACD is the first large-scale dataset of cognitive distortions in Korean adolescents` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Data was collected from NAVER Knowledge iN (Q&A platform) and labeled using a role-switching multi-LLM negotiation framework` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `Generated Story` 열 p90 149자 ≈ 99 토큰 (viewer statistics, default/train)
