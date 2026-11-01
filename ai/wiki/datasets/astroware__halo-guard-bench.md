---
type: "dataset"
id: "astroware/halo-guard-bench"
source: "huggingface"
url: "https://huggingface.co/datasets/astroware/halo-guard-bench"
downloads: 73
summary: "LLM 입력 안전성 분류를 위한 헌법적 다국어 벤치마크 및 학습 코퍼스입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
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
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# astroware/halo-guard-bench

> dataset · [Hugging Face](https://huggingface.co/datasets/astroware/halo-guard-bench)

LLM 입력 안전성 분류를 위한 헌법적 다국어 벤치마크 및 학습 코퍼스입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `user message to classify` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Target classifier output (`Safety: \nCategory: `)` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `46 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `455` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A constitutional, multilingual benchmark and training corpus for LLM input safety classification.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `Training and evaluating LLM input safety classifiers.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Training and evaluating LLM input safety classifiers.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `user_content` 열 p90 1819자 ≈ 455 토큰 (viewer statistics, default/test)
