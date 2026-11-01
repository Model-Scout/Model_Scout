---
type: "dataset"
id: "JOHNISKING/ai-coding-prompt-language"
source: "huggingface"
url: "https://huggingface.co/datasets/JOHNISKING/ai-coding-prompt-language"
downloads: 64
summary: "다국어 코딩 프롬프트에 따른 Claude Code와 Codex 비용 및 성능 비교 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
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
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# JOHNISKING/ai-coding-prompt-language

> dataset · [Hugging Face](https://huggingface.co/datasets/JOHNISKING/ai-coding-prompt-language)

다국어 코딩 프롬프트에 따른 Claude Code와 Codex 비용 및 성능 비교 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Coding in your own language: does the prompt language change what Claude Code and Codex cost?` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `the prompt language barely moves the bill for agentic coding. Median input tokens` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Output did not grow either: median 7,870 tokens in English vs 7,116 to 8,841 for Claude Code` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `5 languages` · 신뢰도 high
- **언어**: [[uk]] — metadata · languages = `uk` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The same brick-breaker task given to Claude Code and Codex in English, Korean, Japanese, Spanish and Ukrainian` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `five runs each (50 runs): input and output tokens, time, cost, whether the game ran, and the language of the game text and code comments.` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
