---
type: "dataset"
id: "Aikyam-Lab/CUREMED-BENCH"
source: "huggingface"
url: "https://huggingface.co/datasets/Aikyam-Lab/CUREMED-BENCH"
downloads: 198
summary: "다국어 의료 추론 벤치마크 데이터셋으로, 다양한 언어의 의료 과제 평가 및 미세조정용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Aikyam-Lab/CUREMED-BENCH

> dataset · [Hugging Face](https://huggingface.co/datasets/Aikyam-Lab/CUREMED-BENCH)

다국어 의료 추론 벤치마크 데이터셋으로, 다양한 언어의 의료 과제 평가 및 미세조정용입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `designed for evaluating and fine-tuning models on medical tasks` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `medical reasoning benchmark dataset` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:question_answering = `Training data CSVs` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `medical reasoning benchmark dataset` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `13 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `718` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[의료·보건]] — tag_match · readme, tags = `medical` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `designed for evaluating and fine-tuning models` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `Includes train, test, and validation splits` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `CoT` 열 p90 2871자 ≈ 718 토큰 (viewer statistics, default/validation)

## 이 데이터로 학습한 모델

- [[Aikyam-Lab__CURE-MED-1.5B|Aikyam-Lab/CURE-MED-1.5B]]
- [[Aikyam-Lab__CURE-MED-7B|Aikyam-Lab/CURE-MED-7B]]
- [[mradermacher__CURE-MED-1.5B-GGUF|mradermacher/CURE-MED-1.5B-GGUF]]
- [[mradermacher__CURE-MED-1.5B-i1-GGUF|mradermacher/CURE-MED-1.5B-i1-GGUF]]
- [[mradermacher__CURE-MED-14B-GGUF|mradermacher/CURE-MED-14B-GGUF]]
- [[mradermacher__CURE-MED-14B-i1-GGUF|mradermacher/CURE-MED-14B-i1-GGUF]]
- [[mradermacher__CURE-MED-3B-GGUF|mradermacher/CURE-MED-3B-GGUF]]
- [[mradermacher__CURE-MED-3B-i1-GGUF|mradermacher/CURE-MED-3B-i1-GGUF]]
- [[mradermacher__CURE-MED-7B-GGUF|mradermacher/CURE-MED-7B-GGUF]]
- [[mradermacher__CURE-MED-7B-i1-GGUF|mradermacher/CURE-MED-7B-i1-GGUF]]
