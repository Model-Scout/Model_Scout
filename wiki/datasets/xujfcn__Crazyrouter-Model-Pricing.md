---
type: "dataset"
id: "xujfcn/Crazyrouter-Model-Pricing"
source: "huggingface"
url: "https://huggingface.co/datasets/xujfcn/Crazyrouter-Model-Pricing"
downloads: 351
summary: "40개 챗봇 모델의 1백만 토큰당 API 가격 비교 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[pt]]"
  - "[[ru]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[상거래·상품]]"
dataset_role:
  - "[[서비스 데이터]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# xujfcn/Crazyrouter-Model-Pricing

> dataset · [Hugging Face](https://huggingface.co/datasets/xujfcn/Crazyrouter-Model-Pricing)

40개 챗봇 모델의 1백만 토큰당 API 가격 비교 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — tag_match · tags = `llm` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `One row per model, flat columns (see schema below)` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Per-1M-token API prices for 40 chat models` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:information_extraction, task:retrieval = `pricing.csv One row per model, flat columns` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Per-1M-token API prices for 40 chat models` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `5 languages` · 신뢰도 high
- **언어**: [[pt]] — metadata · languages = `pt` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `4` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `Per-1M-token API prices for 40 chat models` · 신뢰도 low
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `the price on Crazyrouter (one API key, OpenAI/Anthropic/Gemini-compatible endpoints)` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `model` 열 p90 17자 ≈ 4 토큰 (viewer statistics, default/train)
