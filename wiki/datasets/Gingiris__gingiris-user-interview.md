---
type: "dataset"
id: "Gingiris/gingiris-user-interview"
source: "huggingface"
url: "https://huggingface.co/datasets/Gingiris/gingiris-user-interview"
downloads: 113
summary: "HeyGen의 937회 창업자 주도 사용자 인터뷰 프레임워크로 PMF 검증과 사용자 등급화를 지원하는 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Gingiris/gingiris-user-interview

> dataset · [Hugging Face](https://huggingface.co/datasets/Gingiris/gingiris-user-interview)

HeyGen의 937회 창업자 주도 사용자 인터뷰 프레임워크로 PMF 검증과 사용자 등급화를 지원하는 데이터입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `Help me design PMF validation interviews" · "Draft questions for our 10 power users" · "Build a churn diagnostic interview script` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:generation, task:question_answering = `Help me design PMF validation interviews" · "Draft questions for our 10 power users" · "Build a churn diagnostic interview script` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `Score users into S/A/B/C tiers based on these usage signals` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `4 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Find PMF through founder-led conversations — the exact framework behind HeyGen's 937 interviews, JTBD scripts, screen-share protocols, and S/A/B/C user tier gra` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
