---
type: "dataset"
id: "KokunoYumeto/emmy-noether"
source: "huggingface"
url: "https://huggingface.co/datasets/KokunoYumeto/emmy-noether"
downloads: 98
summary: "에미 뇌터의 수학 논문을 여러 언어 AI 번역과 LaTeX 소스로 제공하는 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[문서 검색]]"
  - "[[번역]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[문서 파일 (출력 형식)|문서 파일]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[학술·논문]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# KokunoYumeto/emmy-noether

> dataset · [Hugging Face](https://huggingface.co/datasets/KokunoYumeto/emmy-noether)

에미 뇌터의 수학 논문을 여러 언어 AI 번역과 LaTeX 소스로 제공하는 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `eleven complete AI-translated editions in nine languages` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `All translations are AI-translated.` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `PDF readers and editable LaTeX sources of Emmy Noether's collected mathematical works` · 신뢰도 low
- **작업**: [[번역]] — tag_match · tags = `translation` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — ner · modality, readme = `PDF readers and editable LaTeX sources` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:generation, task:retrieval, task:translation = `German source text, eleven complete AI-translated editions` · 신뢰도 medium
- **출력 형식**: [[문서 파일 (출력 형식)|문서 파일]] — ner · readme = `PDF readers and editable LaTeX sources` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:translation = `AI-translated editions in nine languages` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `15 languages` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `Emmy Noether: mathematical works in translation` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `All translations are AI-translated.` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
