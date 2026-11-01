---
type: "dataset"
id: "pasinit/xlwic"
source: "huggingface"
url: "https://huggingface.co/datasets/pasinit/xlwic"
downloads: 511
summary: "XL-WiC는 여러 언어에서 단어의 의미 일치 여부를 판별하는 이진 분류 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# pasinit/xlwic

> dataset · [Hugging Face](https://huggingface.co/datasets/pasinit/xlwic)

XL-WiC는 여러 언어에서 단어의 의미 일치 여부를 판별하는 이진 분류 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories, task_ids = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Each instance in XL-WiC has a target word w, either a verb or a noun, for which two contexts are provided.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `The task is to identify if the occurrences of w in the two contexts correspond to the same meaning or not.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `13 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `5` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A system's task on any of the XL-WiC datasets is to identify the intended meaning of a word in a context of a given language.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `training sets in the following 3 languages: German (DE) French (FR) Italian (IT)` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `context_2` 열 p90 19자 ≈ 5 토큰 (viewer statistics, xlwic_en_ko/validation)
