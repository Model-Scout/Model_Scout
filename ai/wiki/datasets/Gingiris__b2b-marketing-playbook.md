---
type: "dataset"
id: "Gingiris/b2b-marketing-playbook"
source: "huggingface"
url: "https://huggingface.co/datasets/Gingiris/b2b-marketing-playbook"
downloads: 38
summary: "B2B SaaS 스타트업을 위한 LinkedIn, 이메일, 웨비나 기반 마케팅 파이프라인 데이터입니다."
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
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[상거래·상품]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Gingiris/b2b-marketing-playbook

> dataset · [Hugging Face](https://huggingface.co/datasets/Gingiris/b2b-marketing-playbook)

B2B SaaS 스타트업을 위한 LinkedIn, 이메일, 웨비나 기반 마케팅 파이프라인 데이터입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:generation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Plan a 90-day marketing strategy for our B2B SaaS` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `4 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `Complete B2B marketing pipeline combining LinkedIn content, cold email sequences, and webinar funnels.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Installs the full B2B Marketing Playbook — Enterprise GTM & ABM Framework playbook` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
