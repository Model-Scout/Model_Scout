---
type: "dataset"
id: "MarkrAI/ko-jailbreak"
source: "huggingface"
url: "https://huggingface.co/datasets/MarkrAI/ko-jailbreak"
downloads: 145
summary: "한국어 LLM 안전 가드의 탈옥 공격 방어력을 평가하는 한국어 jailbreak 벤치마크입니다."
readme_status: "ok"
readme_language: "en"
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
  - "[[중규모 데이터]]"
---
# MarkrAI/ko-jailbreak

> dataset · [Hugging Face](https://huggingface.co/datasets/MarkrAI/ko-jailbreak)

한국어 LLM 안전 가드의 탈옥 공격 방어력을 평가하는 한국어 jailbreak 벤치마크입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `한국어 LLM·안전 가드가 실제 탈옥 공격에 얼마나 견고한지 측정합니다.` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:generation = ``prompt_ko`에 응답하게 한 뒤 judge로 분류합니다.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `judge로 분류합니다.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `공개된 영어 jailbreak(탈옥) 벤치마크들을 한국어로 번역·정제하고 소스 간 중복을 제거해 하나로 통합한 한국어 jailbreak 평가 벤치마크입니다.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `한국어 jailbreak 평가 벤치마크입니다.` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
