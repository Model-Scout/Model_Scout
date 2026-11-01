---
type: "dataset"
id: "Reubencf/Adaption-multilingual-sentences"
source: "huggingface"
url: "https://huggingface.co/datasets/Reubencf/Adaption-multilingual-sentences"
downloads: 44
summary: "123개 언어의 9,999개 문장으로 구성된 다국어 문장 데이터셋으로, 다국어 LLM 튜닝과 번역 연구에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
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
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Reubencf/Adaption-multilingual-sentences

> dataset · [Hugging Face](https://huggingface.co/datasets/Reubencf/Adaption-multilingual-sentences)

123개 언어의 9,999개 문장으로 구성된 다국어 문장 데이터셋으로, 다국어 LLM 튜닝과 번역 연구에 활용됨.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[질의응답]] — ner · readme = `Benchmarking low-resource and constructed-language capability in multilingual LLMs.` · 신뢰도 low
- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering, task:translation = `9,999 sentences across 123 languages.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering, task:translation = `Adaption-sharpened enhanced_prompt / enhanced_completion / reasoning_trace columns.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `124 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `561` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A broad multilingual subset of PolyglotText — originally derived from the Tatoeba project` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Multilingual instruction tuning across a long tail of languages.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `reasoning_trace` 열 p90 2245자 ≈ 561 토큰 (viewer statistics, default/train)
