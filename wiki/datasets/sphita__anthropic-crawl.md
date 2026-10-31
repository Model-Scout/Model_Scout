---
type: "dataset"
id: "sphita/anthropic-crawl"
source: "huggingface"
url: "https://huggingface.co/datasets/sphita/anthropic-crawl"
downloads: 236
summary: "Anthropic의 공개 웹사이트에서 수집한 고품질 웹 크롤링 데이터로 AI 안전 연구 등에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
  - "[[질의응답]]"
  - "[[문서 검색]]"
  - "[[요약]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[ar]]"
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[ru]]"
  - "[[중국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[학술·논문]]"
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# sphita/anthropic-crawl

> dataset · [Hugging Face](https://huggingface.co/datasets/sphita/anthropic-crawl)

Anthropic의 공개 웹사이트에서 수집한 고품질 웹 크롤링 데이터로 AI 안전 연구 등에 활용됨.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — metadata · readme, task_ids = `language-modeling` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Users can query the latest state or pin reproducible training pipelines to a historical snapshot.` · 신뢰도 low
- **작업**: [[요약]] — metadata · task_categories = `summarization` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling, task:question_answering, task:retrieval, task:summarization = `preserves both the raw Server-Side Rendered (SSR) HTML DOM trees and structured, clean Markdown texts` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling, task:question_answering, task:summarization = `preserves both the raw Server-Side Rendered (SSR) HTML DOM trees and structured, clean Markdown texts` · 신뢰도 medium
- **언어**: [[ar]] — metadata · languages = `ar` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `6 languages` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `12990` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `gpl-3.0` · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `this dataset is designed for frontier AI safety research` · 신뢰도 low
- **도메인**: [[일반]] — ner · readme = `Anthropic's public-facing digital footprint (`www.anthropic.com` and `claude.com`)` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `Users can query the latest state or pin reproducible training pipelines to a historical snapshot.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `this dataset is designed for frontier AI safety research, web-agent grounding, language model pre-training` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `markdown` 열 p90 51962자 ≈ 12990 토큰 (viewer statistics, default/train)
