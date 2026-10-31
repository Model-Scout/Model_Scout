---
type: "dataset"
id: "miracl/miracl-corpus"
source: "huggingface"
url: "https://huggingface.co/datasets/miracl/miracl-corpus"
downloads: 16778
summary: "MIRACL는 18개 언어 위키피디아 문서 기반 다국어 검색 데이터셋입니다."
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
# miracl/miracl-corpus

> dataset · [Hugging Face](https://huggingface.co/datasets/miracl/miracl-corpus)

MIRACL는 18개 언어 위키피디아 문서 기반 다국어 검색 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — metadata · task_categories, task_ids = `text-retrieval` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:retrieval = `we keep only the plain text and discard images, tables, etc.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Each retrieval unit contains three fields: `docid`, `title`, and `text`` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `16 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `568` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The corpus for each language is prepared from a Wikipedia dump` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset contains the collection data of the 16 "known languages"` · 신뢰도 low
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 2274자 ≈ 568 토큰 (viewer statistics, ko/train)
