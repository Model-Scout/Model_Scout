---
type: "dataset"
id: "splo2t/haerae-query-context-stress-v3"
source: "huggingface"
url: "https://huggingface.co/datasets/splo2t/haerae-query-context-stress-v3"
downloads: 18
summary: "HAE-RAE 벤치마크 기반 한국어 쿼리/컨텍스트 토큰 경계 스트레스 데이터셋 v3입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[질의응답]]"
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
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# splo2t/haerae-query-context-stress-v3

> dataset · [Hugging Face](https://huggingface.co/datasets/splo2t/haerae-query-context-stress-v3)

HAE-RAE 벤치마크 기반 한국어 쿼리/컨텍스트 토큰 경계 스트레스 데이터셋 v3입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `This repository packages a v3 paired Korean boundary-stress dataset` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · task_categories = `multiple-choice` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:question_answering = `modifies only the query/context side` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `the original answer options the original gold answer` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `2059` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `a v3 paired Korean boundary-stress dataset` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `original_query` 열 p90 3088자 ≈ 2059 토큰 (viewer statistics, default/train)
