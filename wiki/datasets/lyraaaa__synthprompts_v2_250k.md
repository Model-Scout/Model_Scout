---
type: "dataset"
id: "lyraaaa/synthprompts_v2_250k"
source: "huggingface"
url: "https://huggingface.co/datasets/lyraaaa/synthprompts_v2_250k"
downloads: 90
summary: "217개 주제, 64개 문체, 16개 언어로 구성된 25만 개의 합성 사용자 프롬프트 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# lyraaaa/synthprompts_v2_250k

> dataset · [Hugging Face](https://huggingface.co/datasets/lyraaaa/synthprompts_v2_250k)

217개 주제, 64개 문체, 16개 언어로 구성된 25만 개의 합성 사용자 프롬프트 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `64 values including 4 intellectual peer registers` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `produce an artifact — write, translate, summarize, code, rewrite` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `Every prompt is answerable and self-contained` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:question_answering = `Every prompt is answerable and self-contained` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `Every prompt is answerable and self-contained` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `16 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `687` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `250,000 synthetic first-turn user prompts` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `prompt` 열 p90 2747자 ≈ 687 토큰 (viewer statistics, default/train)
