---
type: "dataset"
id: "nthngdy/oscar-small"
source: "huggingface"
url: "https://huggingface.co/datasets/nthngdy/oscar-small"
downloads: 4394
summary: "OSCAR는 Common Crawl 데이터를 언어별로 분류·필터링한 대규모 다국어 말뭉치로, 언어 모델 사전학습용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
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
dataset_size:
  - "[[대규모 데이터]]"
---
# nthngdy/oscar-small

> dataset · [Hugging Face](https://huggingface.co/datasets/nthngdy/oscar-small)

OSCAR는 Common Crawl 데이터를 언어별로 분류·필터링한 대규모 다국어 말뭉치로, 언어 모델 사전학습용입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — metadata · readme, task_ids = `language-modeling` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling = `These contain the extracted plain texts from the websites mostly converted to UTF-8` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `OSCAR is mainly inteded to pretrain language models and word represantations.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `106 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `2016` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc0-1.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The Open Super-large Crawled ALMAnaCH coRpus is a huge multilingual corpus obtained by language classification and filtering of the Common Crawl corpus` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `OSCAR is mainly inteded to pretrain language models and word represantations.` · 신뢰도 low
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 8064자 ≈ 2016 토큰 (viewer statistics, unshuffled_deduplicated_ko/train)
