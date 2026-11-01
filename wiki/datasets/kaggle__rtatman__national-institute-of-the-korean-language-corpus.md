---
type: "dataset"
id: "kaggle/rtatman/national-institute-of-the-korean-language-corpus"
source: "kaggle"
url: "https://www.kaggle.com/datasets/rtatman/national-institute-of-the-korean-language-corpus"
downloads: 983
summary: "한국어 단어 빈도 정보를 담은 데이터셋으로 NLP에 활용됨"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[교육]]"
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/rtatman/national-institute-of-the-korean-language-corpus

> dataset · [Kaggle](https://www.kaggle.com/datasets/rtatman/national-institute-of-the-korean-language-corpus)

한국어 단어 빈도 정보를 담은 데이터셋으로 NLP에 활용됨

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `In natural language processing, very frequent words tend to be less informative than less frequent one and are often removed during preprocessing` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `How frequently a word occurs in a language is an important piece of information for natural language processing` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:embedding = `The text in this dataset is UTF-8` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `For each item, both the frequency (number of times it occurs in the corpus) and its relative rank to other lemmas is provided` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `Other (specified in description)` · 신뢰도 high
- **도메인**: [[교육]] — tag_match · readme, tags = `education` · 신뢰도 medium
- **도메인**: [[일반]] — ner · readme = `This dataset contains frequency information on Korean, which is spoken by 80 million people` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset contains six sub-files with frequency information` · 신뢰도 low
