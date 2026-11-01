---
type: "dataset"
id: "splo2t/haerae-query-context-stress-v2-extreme"
source: "huggingface"
url: "https://huggingface.co/datasets/splo2t/haerae-query-context-stress-v2-extreme"
downloads: 22
summary: "HAE-RAE 벤치마크 기반 한국어 쿼리/컨텍스트 토큰 경계 스트레스 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[질의응답]]"
  - "[[문서 검색]]"
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
# splo2t/haerae-query-context-stress-v2-extreme

> dataset · [Hugging Face](https://huggingface.co/datasets/splo2t/haerae-query-context-stress-v2-extreme)

HAE-RAE 벤치마크 기반 한국어 쿼리/컨텍스트 토큰 경계 스트레스 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · task_categories = `multiple-choice` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `query/context side to make the surface form more tokenization-fragile` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:question_answering, task:retrieval = `query/context side to make the surface form more tokenization-fragile` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `the original answer options the original gold answer` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1212` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `paired Korean boundary-stress dataset` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `original_query` 열 p90 1817자 ≈ 1212 토큰 (viewer statistics, default/train)
