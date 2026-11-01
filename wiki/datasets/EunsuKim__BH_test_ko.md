---
type: "dataset"
id: "EunsuKim/BH_test_ko"
source: "huggingface"
url: "https://huggingface.co/datasets/EunsuKim/BH_test_ko"
downloads: 17
summary: "BenchHub의 한국어 테스트 데이터로, LLM 평가를 위한 통합 벤치마크 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
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
  - "[[평가용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# EunsuKim/BH_test_ko

> dataset · [Hugging Face](https://huggingface.co/datasets/EunsuKim/BH_test_ko)

BenchHub의 한국어 테스트 데이터로, LLM 평가를 위한 통합 벤치마크 데이터입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `BenchHub: A Unified Benchmark Suite for Holistic and Customizable LLM Evaluation` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `BenchHub: A Unified Benchmark Suite for Holistic and Customizable LLM Evaluation` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1361` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **데이터 용도**: [[평가용]] — ner · readme = `This repository contains the data for BenchHub: A Unified Benchmark Suite for Holistic and Customizable LLM Evaluation.` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `context` 열 p90 2041자 ≈ 1361 토큰 (viewer statistics, default/train)
