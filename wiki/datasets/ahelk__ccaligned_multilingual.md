---
type: "dataset"
id: "ahelk/ccaligned_multilingual"
source: "huggingface"
url: "https://huggingface.co/datasets/ahelk/ccaligned_multilingual"
downloads: 198
summary: "CCAligned는 영어와 137개 언어의 웹 문서 쌍을 정렬한 다국어 병렬 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# ahelk/ccaligned_multilingual

> dataset · [Hugging Face](https://huggingface.co/datasets/ahelk/ccaligned_multilingual)

CCAligned는 영어와 137개 언어의 웹 문서 쌍을 정렬한 다국어 병렬 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `This pattern matching approach yielded more than 100 million aligned documents paired with English` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `parallel or comparable web-document pairs in 137 languages aligned with English` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:retrieval = `The text in the dataset is in (137) multiple languages aligned with english.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `126 languages` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `unknown` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `parallel or comparable web-document pairs in 137 languages aligned with English` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Split sizes of some small configurations` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
