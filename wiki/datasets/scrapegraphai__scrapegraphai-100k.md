---
type: "dataset"
id: "scrapegraphai/scrapegraphai-100k"
source: "huggingface"
url: "https://huggingface.co/datasets/scrapegraphai/scrapegraphai-100k"
downloads: 166
summary: "ScrapeGraphAI-100k는 웹 콘텐츠에서 JSON 스키마 기반 구조화 데이터 추출을 위한 LLM 추출 이벤트 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# scrapegraphai/scrapegraphai-100k

> dataset · [Hugging Face](https://huggingface.co/datasets/scrapegraphai/scrapegraphai-100k)

ScrapeGraphAI-100k는 웹 콘텐츠에서 JSON 스키마 기반 구조화 데이터 추출을 위한 LLM 추출 이벤트 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[임베딩]] — metadata · task_categories = `feature-extraction` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:generation = `the prompt, the Markdown-converted page content, the target schema, the model's response, and rich metadata` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `LLM's extracted output (JSON string)` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `11 languages` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `22615` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `real web content under a user-defined JSON schema` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `content` 열 p90 90462자 ≈ 22615 토큰 (viewer statistics, default/train)
