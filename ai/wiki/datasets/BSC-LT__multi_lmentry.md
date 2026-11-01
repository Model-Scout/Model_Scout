---
type: "dataset"
id: "BSC-LT/multi_lmentry"
source: "huggingface"
url: "https://huggingface.co/datasets/BSC-LT/multi_lmentry"
downloads: 742
summary: "Multi-LMentry는 9개 언어의 초등 수준 기본 과제를 평가하는 다국어 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[질의응답]]"
  - "[[리랭킹]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[ca]]"
  - "[[de]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[eu]]"
  - "[[gl]]"
  - "[[it]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[pt]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# BSC-LT/multi_lmentry

> dataset · [Hugging Face](https://huggingface.co/datasets/BSC-LT/multi_lmentry)

Multi-LMentry는 9개 언어의 초등 수준 기본 과제를 평가하는 다국어 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `elementary reasoning and understanding tasks` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 medium
- **작업**: [[리랭킹]] — ner · readme = `systematic assessments of model outputs` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:question_answering, task:reranking = `Each JSON contains input prompts and expected outputs for that task.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `Each JSON contains input prompts and expected outputs for that task.` · 신뢰도 medium
- **언어**: [[ca]] — metadata · languages = `ca` · 신뢰도 high
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[eu]] — metadata · languages = `eu` · 신뢰도 high
- **언어**: [[gl]] — metadata · languages = `gl` · 신뢰도 high
- **언어**: [[it]] — metadata · languages = `it` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `9 languages` · 신뢰도 high
- **언어**: [[pt]] — metadata · languages = `pt` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `20` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `multilingual benchmark designed for evaluating large language models (LLMs) on fundamental, elementary-level tasks across nine languages` · 신뢰도 low
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `input` 열 p90 79자 ≈ 20 토큰 (viewer statistics, ko/train)
