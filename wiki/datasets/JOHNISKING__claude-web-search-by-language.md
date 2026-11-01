---
type: "dataset"
id: "JOHNISKING/claude-web-search-by-language"
source: "huggingface"
url: "https://huggingface.co/datasets/JOHNISKING/claude-web-search-by-language"
downloads: 136
summary: "Claude Code와 Codex가 5개 언어로 웹 검색하며 질문에 답하는 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[질의응답]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[es]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[uk]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# JOHNISKING/claude-web-search-by-language

> dataset · [Hugging Face](https://huggingface.co/datasets/JOHNISKING/claude-web-search-by-language)

Claude Code와 Codex가 5개 언어로 웹 검색하며 질문에 답하는 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `Claude Code and Codex answering the same questions in English, Korean, Japanese, Spanish and Ukrainian with web search on` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Claude Code and Codex answering the same questions in English, Korean, Japanese, Spanish and Ukrainian with web search on` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering, task:retrieval = `the language of every search query, every cited link and its language, the answer language, tokens, searches and time` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `Every answer came back in the language of the question.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `5 languages` · 신뢰도 high
- **언어**: [[uk]] — metadata · languages = `uk` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `103` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `AI web search by language: what Claude Code and Codex search for, and cite, in 5 languages` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Version 3 (320 runs): the local-topic questions now have five runs each for both Claude Code and Codex.` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `search_queries` 열 p90 412자 ≈ 103 토큰 (viewer statistics, default/train)
