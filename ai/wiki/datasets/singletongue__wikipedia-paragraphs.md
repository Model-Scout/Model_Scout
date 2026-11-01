---
type: "dataset"
id: "singletongue/wikipedia-paragraphs"
source: "huggingface"
url: "https://huggingface.co/datasets/singletongue/wikipedia-paragraphs"
downloads: 38289
summary: "Wikipedia 문단과 위키링크 정보를 포함한 NLP 연구용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# singletongue/wikipedia-paragraphs

> dataset · [Hugging Face](https://huggingface.co/datasets/singletongue/wikipedia-paragraphs)

Wikipedia 문단과 위키링크 정보를 포함한 NLP 연구용 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Each entry contains cleaned paragraph text and Wikilink information extracted from a Wikipedia page, along with useful metadata such as categories, templates, a` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `wikipedia-paragraphs is a dataset generated from Wikipedia, designed for natural language processing (NLP) research.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:retrieval = `Each entry contains cleaned paragraph text and Wikilink information extracted from a Wikipedia page` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Each entry contains cleaned paragraph text and Wikilink information extracted from a Wikipedia page` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `11 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `gfdl` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `wikipedia-paragraphs is a dataset generated from Wikipedia, designed for natural language processing (NLP) research.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `999999999.0` · 신뢰도 high
