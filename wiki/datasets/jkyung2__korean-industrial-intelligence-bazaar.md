---
type: "dataset"
id: "jkyung2/korean-industrial-intelligence-bazaar"
source: "huggingface"
url: "https://huggingface.co/datasets/jkyung2/korean-industrial-intelligence-bazaar"
downloads: 48
summary: "한국의 10,000개 산업 공급망 및 기술 정보 데이터셋으로 산업 분석에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[질의응답]]"
  - "[[문서 검색]]"
  - "[[표 질의응답]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[상거래·상품]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# jkyung2/korean-industrial-intelligence-bazaar

> dataset · [Hugging Face](https://huggingface.co/datasets/jkyung2/korean-industrial-intelligence-bazaar)

한국의 10,000개 산업 공급망 및 기술 정보 데이터셋으로 산업 분석에 활용됨.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Free for open sampling and AI agent research benchmarking.` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **작업**: [[문서 검색]] — metadata · readme, task_categories = `text-retrieval` · 신뢰도 medium
- **작업**: [[표 질의응답]] — metadata · task_categories = `table-question-answering` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — task_rule · task:table_qa = `table` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:embedding, task:question_answering, task:retrieval, task:table_qa = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:question_answering, task:table_qa = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `127` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `South Korea's high-value industrial supply-chain, market-share, and technological intelligence.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Free for open sampling and AI agent research benchmarking.` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `sample_metrics` 열 p90 191자 ≈ 127 토큰 (viewer statistics, default/train)
