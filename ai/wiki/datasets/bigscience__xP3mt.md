---
type: "dataset"
id: "bigscience/xP3mt"
source: "huggingface"
url: "https://huggingface.co/datasets/bigscience/xP3mt"
downloads: 9025
summary: "46개 언어와 16개 NLP 작업에 걸친 다국어 프롬프트 및 데이터셋 모음으로 BLOOMZ, mT0 학습용 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
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
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# bigscience/xP3mt

> dataset · [Hugging Face](https://huggingface.co/datasets/bigscience/xP3mt)

46개 언어와 16개 NLP 작업에 걸친 다국어 프롬프트 및 데이터셋 모음으로 BLOOMZ, mT0 학습용 데이터입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `16 NLP tasks` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `multilingual language models capable of following human instructions in dozens of languages zero-shot` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `Closed-book QA` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:question_answering = `the natural language input fed to the model` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `the natural language target that the model has to generate` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `46 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `64` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `multilingual language models capable of following human instructions in dozens of languages zero-shot` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `It is used for the training of BLOOMZ and mT0` · 신뢰도 medium
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

샘플 길이: `inputs` 열 p90 255자 ≈ 64 토큰 (viewer statistics, ak/train)

## 이 데이터로 학습한 모델

- [[bigscience__mt0-xxl-mt|bigscience/mt0-xxl-mt]]
