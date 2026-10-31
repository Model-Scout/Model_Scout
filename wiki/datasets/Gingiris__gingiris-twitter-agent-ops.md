---
type: "dataset"
id: "Gingiris/gingiris-twitter-agent-ops"
source: "huggingface"
url: "https://huggingface.co/datasets/Gingiris/gingiris-twitter-agent-ops"
downloads: 79
summary: "AI 에이전트가 트위터/X 계정을 자동 운영하며 팔로워를 증가시키는 완전한 SOP 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
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
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Gingiris/gingiris-twitter-agent-ops

> dataset · [Hugging Face](https://huggingface.co/datasets/Gingiris/gingiris-twitter-agent-ops)

AI 에이전트가 트위터/X 계정을 자동 운영하며 팔로워를 증가시키는 완전한 SOP 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[문서 검색]] — ner · readme = `将账号主人的所有一手内容转化为可检索的文本` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:retrieval = `日均发布 1 条，全程自动化运营` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `让 agent 写出"像这个人"的内容` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `4 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Twitter/X Agent Operations — AI 自动运营完整 SOP` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `本 skill 适用于任何支持 system prompt 的 AI agent（Claude Code, Cursor, Trae, GPT）` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
