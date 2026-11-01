---
type: "dataset"
id: "Qrzysztof/ecommerce-chat-tool-calling"
source: "huggingface"
url: "https://huggingface.co/datasets/Qrzysztof/ecommerce-chat-tool-calling"
downloads: 56
summary: "자연어 쇼핑 요청을 다양한 도구 스키마 호출로 매핑하는 전자상거래 챗봇 도구 호출 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[도구 호출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
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
  - "[[소규모 데이터]]"
---
# Qrzysztof/ecommerce-chat-tool-calling

> dataset · [Hugging Face](https://huggingface.co/datasets/Qrzysztof/ecommerce-chat-tool-calling)

자연어 쇼핑 요청을 다양한 도구 스키마 호출로 매핑하는 전자상거래 챗봇 도구 호출 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[도구 호출]] — tag_match · readme, tags = `function-calling` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `A visitor chats with the store's corner chatbot: "I need an inexpensive top-loading washing machine, preferably from a German manufacturer"` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `the model must emit the declared tool call with the right query and filters` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `25 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `218` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — tag_match · readme, tags = `e-commerce` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Synthetic training data that teaches a small model (e.g. google/functiongemma-270m-it) to map natural-language shopping requests onto whatever tool schema is de` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `tools_json` 열 p90 872자 ≈ 218 토큰 (viewer statistics, default/train)
