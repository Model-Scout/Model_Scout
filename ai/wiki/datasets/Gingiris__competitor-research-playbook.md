---
type: "dataset"
id: "Gingiris/competitor-research-playbook"
source: "huggingface"
url: "https://huggingface.co/datasets/Gingiris/competitor-research-playbook"
downloads: 41
summary: "경쟁사 성장 분석을 위한 웹사이트, 소셜미디어, 성장 플라이휠 분석 SOP 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[문서 검색]]"
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
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Gingiris/competitor-research-playbook

> dataset · [Hugging Face](https://huggingface.co/datasets/Gingiris/competitor-research-playbook)

경쟁사 성장 분석을 위한 웹사이트, 소셜미디어, 성장 플라이휠 분석 SOP 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `content effectiveness ranking (validated: Visual Demo > User Story > Competitor Comparison)` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `growth flywheel 6-stage scoring system (Activation → Referral → Acquisition → Retention → Revenue → Product)` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Complete SOP for systematic competitor research: website evolution analysis, social media channel teardown, growth flywheel scoring, X/Twitter propagation chain` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:embedding, task:generation, task:retrieval = `website teardown → social media → traffic sources → ad spend` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `growth flywheel 6-stage scoring system (Activation → Referral → Acquisition → Retention → Revenue → Product)` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `4 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `Built from 150+ AI startup competitive analyses including the Lovable case study` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
