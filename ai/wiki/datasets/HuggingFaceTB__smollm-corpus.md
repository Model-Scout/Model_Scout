---
type: "dataset"
id: "HuggingFaceTB/smollm-corpus"
source: "huggingface"
url: "https://huggingface.co/datasets/HuggingFaceTB/smollm-corpus"
downloads: 60828
summary: "SmolLM-Corpus는 소형 언어 모델 학습용 고품질 교육 및 합성 데이터 모음입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[언어 모델링]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# HuggingFaceTB/smollm-corpus

> dataset · [Hugging Face](https://huggingface.co/datasets/HuggingFaceTB/smollm-corpus)

SmolLM-Corpus는 소형 언어 모델 학습용 고품질 교육 및 합성 데이터 모음입니다.

## 분류

- **작업**: [[언어 모델링]] — ner · readme = `designed for training small language models` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:language_modeling = `text content` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling = `generated text content` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1503` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `odc-by` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `high-quality educational and synthetic data` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `designed for training small language models` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `999999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 6011자 ≈ 1503 토큰 (viewer statistics, cosmopedia-v2/train)

## 이 데이터로 학습한 모델

- [[FINAL-Bench__Aether-7B-5Attn|FINAL-Bench/Aether-7B-5Attn]]
- [[FINAL-Bench__Aether-7B-5Attn-it|FINAL-Bench/Aether-7B-5Attn-it]]
