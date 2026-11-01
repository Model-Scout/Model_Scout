---
type: "dataset"
id: "ChuGyouk/argilla-distilabel-math-preference-dpo-korean"
source: "huggingface"
url: "https://huggingface.co/datasets/ChuGyouk/argilla-distilabel-math-preference-dpo-korean"
downloads: 41
summary: "argilla/distilabel-math-preference-dpo 데이터셋의 한국어 번역본으로, 질문과 선택/거부 응답을 포함함."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# ChuGyouk/argilla-distilabel-math-preference-dpo-korean

> dataset · [Hugging Face](https://huggingface.co/datasets/ChuGyouk/argilla-distilabel-math-preference-dpo-korean)

argilla/distilabel-math-preference-dpo 데이터셋의 한국어 번역본으로, 질문과 선택/거부 응답을 포함함.

## 분류

- **작업**: [[번역]] — ner · readme = `You are tasked with translating English text into Korean for Direct Preference Optimization training data.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `This data consists of a question, a chosen response, and a rejected response.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `Your goal is to accurately translate the content while preserving the meaning and structure of the original text.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1270` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `This is a gpt-4o-2024-08-06 Korean translated-version of argilla/distilabel-math-preference-dpo.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `chosen_response` 열 p90 1904자 ≈ 1270 토큰 (viewer statistics, default/train)
