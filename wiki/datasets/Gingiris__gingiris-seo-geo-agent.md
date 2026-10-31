---
type: "dataset"
id: "Gingiris/gingiris-seo-geo-agent"
source: "huggingface"
url: "https://huggingface.co/datasets/Gingiris/gingiris-seo-geo-agent"
downloads: 90
summary: "자율 AI 에이전트가 일일 SEO 및 GEO 작업을 자동화하여 월 3만2천 건 구글 노출을 달성하는 SOP 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
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
domain:
  - "[[상거래·상품]]"
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Gingiris/gingiris-seo-geo-agent

> dataset · [Hugging Face](https://huggingface.co/datasets/Gingiris/gingiris-seo-geo-agent)

자율 AI 에이전트가 일일 SEO 및 GEO 작업을 자동화하여 월 3만2천 건 구글 노출을 달성하는 SOP 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[임베딩]] — ner · readme = `AI search citation on ChatGPT/Perplexity/Claude` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[정보 추출]] — ner · readme = `Schema markup, IndexNow, internal linking architecture` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Run today's SEO/GEO patrol on gingiris.tools` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:embedding, task:generation, task:information_extraction, task:retrieval = `Run today's SEO/GEO patrol on gingiris.tools` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Generate daily report: which keywords are on Google page 1?` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `4 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `Run autonomous SEO at $50-100/month — the day-by-day agent SOP behind ~32K Google impressions/month + AI search citation` · 신뢰도 low
- **도메인**: [[일반]] — ner · readme = `AI agents can run 90% of SEO work autonomously — but only if the SOP tells them *exactly* what to do every day.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This is a **complete operational SOP (Standard Operating Procedure)** for running an autonomous AI agent that handles daily SEO and GEO (Generative Engine Optim` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
