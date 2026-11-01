---
type: "dataset"
id: "ManhHoDinh/titlegen-conversations"
source: "huggingface"
url: "https://huggingface.co/datasets/ManhHoDinh/titlegen-conversations"
downloads: 39
summary: "다국어 대화 제목 생성용 데이터셋으로, 9개 언어의 LLM 생성 및 레거시 데이터를 포함함."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[de]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[fr]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[th]]"
  - "[[vi]]"
  - "[[중국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# ManhHoDinh/titlegen-conversations

> dataset · [Hugging Face](https://huggingface.co/datasets/ManhHoDinh/titlegen-conversations)

다국어 대화 제목 생성용 데이터셋으로, 9개 언어의 LLM 생성 및 레거시 데이터를 포함함.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `Legacy rows contain only `messages`; nine-language rows retain their richer IDs, language, coverage, cluster, quality, and model-provenance fields.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Use this dataset to train or evaluate concise same-language conversation-title generation.` · 신뢰도 medium
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `9 languages` · 신뢰도 high
- **언어**: [[th]] — metadata · languages = `th` · 신뢰도 high
- **언어**: [[vi]] — metadata · languages = `vi` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Use this dataset to train or evaluate concise same-language conversation-title generation.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The 23,784 examples are split as train 20,584, validation 1,550, legacy test 200, legacy Vietnamese test 100, and label-free synthetic holdout 1,350.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
