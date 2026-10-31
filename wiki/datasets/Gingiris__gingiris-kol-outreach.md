---
type: "dataset"
id: "Gingiris/gingiris-kol-outreach"
source: "huggingface"
url: "https://huggingface.co/datasets/Gingiris/gingiris-kol-outreach"
downloads: 74
summary: "200회 이상의 AFFiNE 캠페인 기반 KOL 아웃리치 및 인플루언서 마케팅 전략과 실행 매뉴얼 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
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
# Gingiris/gingiris-kol-outreach

> dataset · [Hugging Face](https://huggingface.co/datasets/Gingiris/gingiris-kol-outreach)

200회 이상의 AFFiNE 캠페인 기반 KOL 아웃리치 및 인플루언서 마케팅 전략과 실행 매뉴얼 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Separate outreach replies, test interest, invitations, actual use, completed tests and feedback. Compare channel performance from recorded evidence.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:generation, task:retrieval = `Includes pricing benchmarks across Twitter/X, YouTube, TikTok, LinkedIn; email templates; content package templates; platform algorithm guides for 7 platforms; ` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Includes pricing benchmarks across Twitter/X, YouTube, TikTok, LinkedIn; email templates; content package templates; platform algorithm guides for 7 platforms; ` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `4 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `Battle-tested with 200+ KOL campaigns at AFFiNE` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
