---
type: "dataset"
id: "adithya7/xlel_wd_dictionary"
source: "huggingface"
url: "https://huggingface.co/datasets/adithya7/xlel_wd_dictionary"
downloads: 697
summary: "XLEL-WD는 위키데이터 이벤트 항목의 다국어 사전으로 이벤트 링크 작업에 활용됨."
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
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# adithya7/xlel_wd_dictionary

> dataset · [Hugging Face](https://huggingface.co/datasets/adithya7/xlel_wd_dictionary)

XLEL-WD는 위키데이터 이벤트 항목의 다국어 사전으로 이벤트 링크 작업에 활용됨.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `This dictionary can be used as a part of the event linking task.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:retrieval = `The descriptions for Wikidata event items are taken from the corresponding multilingual Wikipedia articles.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `The descriptions for Wikidata event items are taken from the corresponding multilingual Wikipedia articles.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `44 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `77` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `XLEL-WD is a multilingual event linking dataset.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dictionary has a single split, `dictionary`. It contains 10947 event items from Wikidata and a total of 114834 text descriptions collected from multilingua` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `label_desc` 열 p90 308자 ≈ 77 토큰 (viewer statistics, wikidata.ko/dictionary)
