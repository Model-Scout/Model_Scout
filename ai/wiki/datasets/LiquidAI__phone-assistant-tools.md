---
type: "dataset"
id: "LiquidAI/phone-assistant-tools"
source: "huggingface"
url: "https://huggingface.co/datasets/LiquidAI/phone-assistant-tools"
downloads: 84
summary: "108개 도구 카탈로그를 활용한 16개 언어의 전화 비서 요청 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[도구 호출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[코드 (출력 형식)|코드]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# LiquidAI/phone-assistant-tools

> dataset · [Hugging Face](https://huggingface.co/datasets/LiquidAI/phone-assistant-tools)

108개 도구 카탈로그를 활용한 16개 언어의 전화 비서 요청 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[도구 호출]] — tag_match · readme, tags = `function-calling` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `Requests to a phone assistant with the gold tool calls` · 신뢰도 high
- **출력 형식**: [[코드 (출력 형식)|코드]] — ner · readme = `tool catalog, as function schemas` · 신뢰도 low
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `16 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `37` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Requests to a phone assistant with the gold tool calls, for a fixed catalog of 108 tools.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = ``test` | 499 | requests for the same 98 tools` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = ``train` | 2,500 | requests for 98 of the tools` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `calls` 열 p90 149자 ≈ 37 토큰 (viewer statistics, default/test)
