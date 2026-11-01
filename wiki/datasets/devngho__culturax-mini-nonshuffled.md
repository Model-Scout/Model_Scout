---
type: "dataset"
id: "devngho/culturax-mini-nonshuffled"
source: "huggingface"
url: "https://huggingface.co/datasets/devngho/culturax-mini-nonshuffled"
downloads: 2877
summary: "uonlp/CulturaX의 각 언어별 1% 샘플을 포함한 다국어 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
  - "[[문서 검색]]"
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
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# devngho/culturax-mini-nonshuffled

> dataset · [Hugging Face](https://huggingface.co/datasets/devngho/culturax-mini-nonshuffled)

uonlp/CulturaX의 각 언어별 1% 샘플을 포함한 다국어 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — metadata · task_categories, task_ids = `fill-mask` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `load_dataset('devngho/culturax-mini-nonshuffled', '[lang]', split='train') # read specified language` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling, task:retrieval = `load_dataset('devngho/culturax-mini-nonshuffled', '[lang]', split='train')` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `load_dataset('devngho/culturax-mini-nonshuffled', '[lang]', split='train')` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `149 languages` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `4260` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `split='train'` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 17039자 ≈ 4260 토큰 (viewer statistics, ko/train)
