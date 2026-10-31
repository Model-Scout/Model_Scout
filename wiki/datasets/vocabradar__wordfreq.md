---
type: "dataset"
id: "vocabradar/wordfreq"
source: "huggingface"
url: "https://huggingface.co/datasets/vocabradar/wordfreq"
downloads: 660
summary: "43개 언어의 정제된 단어 빈도 리스트로 오프라인 빈도 사전 및 단어 번역에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[번역]]"
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
dataset_size:
  - "[[대규모 데이터]]"
---
# vocabradar/wordfreq

> dataset · [Hugging Face](https://huggingface.co/datasets/vocabradar/wordfreq)

43개 언어의 정제된 단어 빈도 리스트로 오프라인 빈도 사전 및 단어 번역에 활용됨.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Small word-frequency lists for 43 languages, derived from wordfreq 3.0.2 and cleaned for use as offline frequency dictionaries` · 신뢰도 low
- **작업**: [[번역]] — ner · readme = `These lists are also the direct vocabulary source of vocabradar/WordTranslation, which translates them word by word.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:translation = `Small word-frequency lists for 43 languages` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `Small word-frequency lists for 43 languages` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `43 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Small word-frequency lists for 43 languages` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Small word-frequency lists for 43 languages, derived from wordfreq 3.0.2 and cleaned for use as offline frequency dictionaries` · 신뢰도 low
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
