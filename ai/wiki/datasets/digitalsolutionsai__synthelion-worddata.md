---
type: "dataset"
id: "digitalsolutionsai/synthelion-worddata"
source: "huggingface"
url: "https://huggingface.co/datasets/digitalsolutionsai/synthelion-worddata"
downloads: 274
summary: "Synthelion의 규칙 기반 프롬프트 압축에 쓰이는 56개 이상 언어별 언어학 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[서비스 데이터]]"
---
# digitalsolutionsai/synthelion-worddata

> dataset · [Hugging Face](https://huggingface.co/datasets/digitalsolutionsai/synthelion-worddata)

Synthelion의 규칙 기반 프롬프트 압축에 쓰이는 56개 이상 언어별 언어학 데이터입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Per-language linguistic data used by Synthelion's rule-based prompt compressor: function words (stopwords), lemma maps, proper-noun lists, part-of-speech tags, ` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding = `Brotli-compressed (`.br`) YAML/JSON per language (ISO 639-3 code)` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Brotli-compressed (`.br`) YAML/JSON per language (ISO 639-3 code)` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `47 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Per-language linguistic data used by Synthelion's rule-based prompt compressor` · 신뢰도 low
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `This data is loaded at runtime by every compress() call — it is not an ML model, just precomputed per-language tables.` · 신뢰도 low
