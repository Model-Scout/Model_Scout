---
type: "dataset"
id: "Saxo/alpaca_function_calling_dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/Saxo/alpaca_function_calling_dataset"
downloads: 206
summary: "llm RAG의 function calling 학습을 위한 Alpaca 포맷 변환 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[도구 호출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Saxo/alpaca_function_calling_dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/Saxo/alpaca_function_calling_dataset)

llm RAG의 function calling 학습을 위한 Alpaca 포맷 변환 데이터셋입니다.

## 분류

- **작업**: [[도구 호출]] — tag_match · readme, tags = `function calling` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme = `llam3 instruct format인 mzbac/function-calling-llama-3-format-v1.1 을 Alpaca Format으로 변경` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `llam3 instruct format인 mzbac/function-calling-llama-3-format-v1.1 을 Alpaca Format으로 변경` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `783` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `AI 와 빅데이터 분석 전문 기업인 Linkbricks(www.linkbricks.com)의 데이터사이언티스트인 지윤성(Saxo) 박사가 만든` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `llm RAG를 위한 function calling 학습용 데이터셋` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `system` 열 p90 1175자 ≈ 783 토큰 (viewer statistics, default/train)
