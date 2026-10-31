---
type: "dataset"
id: "GEM/surface_realisation_st_2020"
source: "huggingface"
url: "https://huggingface.co/datasets/GEM/surface_realisation_st_2020"
downloads: 967
summary: "11개 언어의 보편 의존구조를 자연어 문장으로 재구성하는 다국어 표면 실현 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
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
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# GEM/surface_realisation_st_2020

> dataset · [Hugging Face](https://huggingface.co/datasets/GEM/surface_realisation_st_2020)

11개 언어의 보편 의존구조를 자연어 문장으로 재구성하는 다국어 표면 실현 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `a model gets full or partial universal dependency structures and has to reconstruct the natural language` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `this field contains an input tree in CoNLL-U format` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `this field contains the target sentence to generate` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `11 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `490` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-2.5` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The datasets cover a large variety of domains (news, blogs, forums, wikipedia pages, etc.).` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The dataset is intended to be used for training models to solve several NLG subtasks` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `input` 열 p90 1961자 ≈ 490 토큰 (viewer statistics, default/validation)
