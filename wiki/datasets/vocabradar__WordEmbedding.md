---
type: "dataset"
id: "vocabradar/WordEmbedding"
source: "huggingface"
url: "https://huggingface.co/datasets/vocabradar/WordEmbedding"
downloads: 74
summary: "42개 언어 167만 단어에 대한 384차원 워드 임베딩 벡터 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
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
  - "[[서비스 데이터]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# vocabradar/WordEmbedding

> dataset · [Hugging Face](https://huggingface.co/datasets/vocabradar/WordEmbedding)

42개 언어 167만 단어에 대한 384차원 워드 임베딩 벡터 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — tag_match · readme, tags = `embeddings` · 신뢰도 medium
- **작업**: [[문서 검색]] — ner · readme = `the vocabulary radar can place a word in semantic space as soon as it meets it` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:retrieval = `One 384-dimensional vector for every word in vocabradar/wordfreq` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `One 384-dimensional vector for every word` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `42 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `42 languages, 1,672,738 words` · 신뢰도 low
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `The [VocabRadar browser extension](https://vocabradar.com) marks up the words you do not know yet while you watch videos or browse the web` · 신뢰도 low
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
