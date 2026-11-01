---
type: "dataset"
id: "CohereLabs/m-ArenaHard"
source: "huggingface"
url: "https://huggingface.co/datasets/CohereLabs/m-ArenaHard"
downloads: 1003
summary: "m-ArenaHard는 23개 언어로 번역된 다국어 LLM 평가용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[질의응답]]"
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
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# CohereLabs/m-ArenaHard

> dataset · [Hugging Face](https://huggingface.co/datasets/CohereLabs/m-ArenaHard)

m-ArenaHard는 23개 언어로 번역된 다국어 LLM 평가용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `used to perform automatic LLM judge evaluations` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `500 challenging user queries sourced from Chatbot Arena` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:question_answering = `prompts from the originally English-only LMarena` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `used to perform automatic LLM judge evaluations` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `23 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `184` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `multilingual LLM evaluation set` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `arena-hard-auto-v0.1 test dataset` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `prompt` 열 p90 735자 ≈ 184 토큰 (viewer statistics, ko/test)
