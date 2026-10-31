---
type: "dataset"
id: "Shitao/MLDR"
source: "huggingface"
url: "https://huggingface.co/datasets/Shitao/MLDR"
downloads: 2041
summary: "MLDR은 13개 언어의 위키피디아, Wudao, mC4 기반 다국어 장문 문서 검색 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# Shitao/MLDR

> dataset · [Hugging Face](https://huggingface.co/datasets/Shitao/MLDR)

MLDR은 13개 언어의 위키피디아, Wudao, mC4 기반 다국어 장문 문서 검색 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — metadata · readme, task_categories = `text-retrieval` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:retrieval = `The generated question and the sampled article constitute a new text pair to the dataset.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Then we use GPT-3.5 to generate questions based on these paragraphs.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `13 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `MLDR is a Multilingual Long-Document Retrieval dataset built on Wikipeida, Wudao and mC4, covering 13 typologically diverse languages.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `For each language, there are three splits: `train`, `dev`, and `test`. The `corpus` is also avaliable here.` · 신뢰도 medium

## 같은 데이터의 사본·중복 등록

- `whooray/MLDR`
