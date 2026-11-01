---
type: "dataset"
id: "Gingiris/gr-readme"
source: "huggingface"
url: "https://huggingface.co/datasets/Gingiris/gr-readme"
downloads: 56
summary: "GitHub README 작성법을 안내하는 3초 내 방문자 전환 가이드 스킬입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[요약]]"
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
  - "[[서비스 데이터]]"
---
# Gingiris/gr-readme

> dataset · [Hugging Face](https://huggingface.co/datasets/Gingiris/gr-readme)

GitHub README 작성법을 안내하는 3초 내 방문자 전환 가이드 스킬입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[요약]] — metadata · task_categories = `summarization` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:summarization = `This skill guides you through writing a README that converts visitors into stars within the first 3 seconds of landing.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:summarization = `This skill guides you through writing a README that converts visitors into stars within the first 3 seconds of landing.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `4 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `GitHub README Writing System — 3-Second Conversion Framework` · 신뢰도 low
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `Works with Claude Code, Cursor, Windsurf, and any AI agent that supports the skills protocol.` · 신뢰도 low
