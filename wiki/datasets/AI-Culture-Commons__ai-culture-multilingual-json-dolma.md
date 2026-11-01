---
type: "dataset"
id: "AI-Culture-Commons/ai-culture-multilingual-json-dolma"
source: "huggingface"
url: "https://huggingface.co/datasets/AI-Culture-Commons/ai-culture-multilingual-json-dolma"
downloads: 108
summary: "12개 언어로 정제된 철학·문화 콘텐츠 5천개 기사 병렬 데이터셋으로 AI 문화 연구용."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
  - "[[요약]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[문화·관광]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# AI-Culture-Commons/ai-culture-multilingual-json-dolma

> dataset · [Hugging Face](https://huggingface.co/datasets/AI-Culture-Commons/ai-culture-multilingual-json-dolma)

12개 언어로 정제된 철학·문화 콘텐츠 5천개 기사 병렬 데이터셋으로 AI 문화 연구용.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[임베딩]] — metadata · task_categories = `feature-extraction` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · tags, task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — metadata · readme, tags, task_categories = `fill-mask` · 신뢰도 medium
- **작업**: [[요약]] — metadata · task_categories = `summarization` · 신뢰도 low
- **작업**: [[번역]] — metadata · tags, task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:generation, task:language_modeling, task:summarization, task:translation = `The AI-Culture corpus contains 5K articles providing comprehensive philosophical and cultural content` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling, task:summarization, task:translation = `All content maintains identical parallel structure across translations with zero duplication and editor-curated quality.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `12 languages` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `14009` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[문화·관광]] — tag_match · readme, tags = `culture` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 56034자 ≈ 14009 토큰 (viewer statistics, dolma/train)
