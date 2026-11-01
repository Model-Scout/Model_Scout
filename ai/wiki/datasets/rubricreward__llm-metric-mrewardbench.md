---
type: "dataset"
id: "rubricreward/llm-metric-mrewardbench"
source: "huggingface"
url: "https://huggingface.co/datasets/rubricreward/llm-metric-mrewardbench"
downloads: 98
summary: "다국어 LLM 평가용 M-RewardBench 데이터셋으로 모델 간 응답 품질 비교에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[리랭킹]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
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
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# rubricreward/llm-metric-mrewardbench

> dataset · [Hugging Face](https://huggingface.co/datasets/rubricreward/llm-metric-mrewardbench)

다국어 LLM 평가용 M-RewardBench 데이터셋으로 모델 간 응답 품질 비교에 사용됨.

## 분류

- **작업**: [[리랭킹]] — ner · readme = `Multilingual RewardBench (M-RewardBench)` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:reranking = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `- name: chosen
dtype: string
- name: rejected
dtype: string` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `22 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `629` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `odc-by` · 신뢰도 high
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `- split: test` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `prompt` 열 p90 2516자 ≈ 629 토큰 (viewer statistics, kor_Hang/test)

## 같은 데이터의 사본·중복 등록

- `rifqifarhansyah/llm-metric-mrewardbench`
