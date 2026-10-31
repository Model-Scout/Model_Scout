---
type: "dataset"
id: "MarkrAI/k-overrefusal"
source: "huggingface"
url: "https://huggingface.co/datasets/MarkrAI/k-overrefusal"
downloads: 47
summary: "한국어 LLM의 과잉 안전 거부를 측정하는 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
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
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# MarkrAI/k-overrefusal

> dataset · [Hugging Face](https://huggingface.co/datasets/MarkrAI/k-overrefusal)

한국어 LLM의 과잉 안전 거부를 측정하는 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `한국어 LLM의 과잉 안전 거부(over-refusal / false refusal) 를 측정하는 벤치마크입니다.` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:generation = ``prompt_ko`에 모델을 응답하게 한 뒤 judge로 분류합니다.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = ``prompt_ko`에 모델을 응답하게 한 뒤 judge로 분류합니다.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 LLM의 과잉 안전 거부(over-refusal / false refusal) 를 측정하는 벤치마크입니다.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `한국어 LLM의 과잉 안전 거부(over-refusal / false refusal) 를 측정하는 벤치마크입니다.` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
