---
type: "dataset"
id: "haritzpuerto/PEEP-contextual-integrity"
source: "huggingface"
url: "https://huggingface.co/datasets/haritzpuerto/PEEP-contextual-integrity"
downloads: 45
summary: "PEEP는 실제 사용자-챗봇 대화에서 개인정보 노출 여부를 평가하는 프라이버시 평가 벤치마크입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# haritzpuerto/PEEP-contextual-integrity

> dataset · [Hugging Face](https://huggingface.co/datasets/haritzpuerto/PEEP-contextual-integrity)

PEEP는 실제 사용자-챗봇 대화에서 개인정보 노출 여부를 평가하는 프라이버시 평가 벤치마크입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `PEEP is a privacy evaluation benchmark derived from WildChat, a corpus of real user–chatbot conversations.` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `PEEP is used in this repository to evaluate whether controllable reasoning models can act as “private thinkers” while still remaining useful.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `Conversations are annotated with potential pieces of confidential information (e.g., names, locations, contact details).` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `38 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `894` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `odc-by` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `PEEP is a privacy evaluation benchmark derived from WildChat, a corpus of real user–chatbot conversations.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `PEEP is used in this repository to evaluate whether controllable reasoning models can act as “private thinkers” while still remaining useful.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `user_prompt` 열 p90 3577자 ≈ 894 토큰 (viewer statistics, default/test)
