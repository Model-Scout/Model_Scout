---
type: "dataset"
id: "jinjh0123/bbg"
source: "huggingface"
url: "https://huggingface.co/datasets/jinjh0123/bbg"
downloads: 71
summary: "BBG는 영어와 한국어로 된 장문 생성에서 사회적 편향을 평가하는 벤치마크입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
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
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
---
# jinjh0123/bbg

> dataset · [Hugging Face](https://huggingface.co/datasets/jinjh0123/bbg)

BBG는 영어와 한국어로 된 장문 생성에서 사회적 편향을 평가하는 벤치마크입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `calculate the neutrality and bias scores` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:generation, task:question_answering = `Input: `context` (`amb_context` + `obfdis_context`)` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `Let the target model generate a continuation of the seed story.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Measuring social bias in large language models (LLMs) is crucial` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `Recommended for standard benchmarking.` · 신뢰도 medium
