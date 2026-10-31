---
type: "dataset"
id: "agentlans/personal-information-prompts"
source: "huggingface"
url: "https://huggingface.co/datasets/agentlans/personal-information-prompts"
downloads: 180
summary: "다국어 인공 개인 식별 정보가 포함된 프롬프트 데이터셋으로 분류 학습에 활용됨"
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
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# agentlans/personal-information-prompts

> dataset · [Hugging Face](https://huggingface.co/datasets/agentlans/personal-information-prompts)

다국어 인공 개인 식별 정보가 포함된 프롬프트 데이터셋으로 분류 학습에 활용됨

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = ``contains_pii`: whether PII was used in constructing the prompt` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `59 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `287` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This dataset contains multilingual prompts derived from the all_sample subset of the agentlans/allenai-WildChat-4.8M dataset.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `prompt` 열 p90 1150자 ≈ 287 토큰 (viewer statistics, classification/test)
