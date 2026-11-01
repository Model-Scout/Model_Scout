---
type: "dataset"
id: "Kasher13/prospire-synth-global-personas"
source: "huggingface"
url: "https://huggingface.co/datasets/Kasher13/prospire-synth-global-personas"
downloads: 274
summary: "Prospire Synth Global Personas는 AI 시뮬레이션, 시장 조사, 문화 분석용 합성 인물 데이터베이스입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[상거래·상품]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# Kasher13/prospire-synth-global-personas

> dataset · [Hugging Face](https://huggingface.co/datasets/Kasher13/prospire-synth-global-personas)

Prospire Synth Global Personas는 AI 시뮬레이션, 시장 조사, 문화 분석용 합성 인물 데이터베이스입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `a unified, query-ready database of synthetic human personas built for AI agent simulations, market research, and cultural analysis` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `512M+ records · 82 columns · 77+ countries · 39 languages · DuckDB-native` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation, task:question_answering, task:retrieval = `text` · 신뢰도 high
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `512M+ records · 82 columns · 77+ countries · 39 languages · DuckDB-native` · 신뢰도 low
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:question_answering = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `12 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `83` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `If we launch a durian milk tea product, which customer segments across Southeast Asia would prefer it — and why?` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Prospire Synth Global Personas is a unified, query-ready database of synthetic human personas built for AI agent simulations, market research, and cultural anal` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `999999999.0` · 신뢰도 high

샘플 길이: `persona_text` 열 p90 332자 ≈ 83 토큰 (viewer statistics, default/train)
