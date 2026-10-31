---
type: "dataset"
id: "adithya7/xlel_wd"
source: "huggingface"
url: "https://huggingface.co/datasets/adithya7/xlel_wd"
downloads: 490
summary: "XLEL-WD는 다국어 위키피디아/위키뉴스 기사에서 위키데이터 이벤트 항목으로 연결하는 다국어 이벤트 링크 데이터셋입니다."
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
  - "[[평가용]]"
  - "[[학습용]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# adithya7/xlel_wd

> dataset · [Hugging Face](https://huggingface.co/datasets/adithya7/xlel_wd)

XLEL-WD는 다국어 위키피디아/위키뉴스 기사에서 위키데이터 이벤트 항목으로 연결하는 다국어 이벤트 링크 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `This dataset can be used for the task of event linking.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:retrieval = `This dataset contains text from 44 languages.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `This dataset contains mention references from multilingual Wikipedia/Wikinews articles to event items in Wikidata.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `44 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This dataset contains mention references in multilingual Wikipedia/Wikinews articles to event items from Wikidata.` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `The Wikinews-based evaluation set has two variants, one for cross-domain evaluation and another for zero-shot evaluation.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The Wikipedia-based corpus has three splits.` · 신뢰도 low
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
