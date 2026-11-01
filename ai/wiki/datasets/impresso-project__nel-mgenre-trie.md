---
type: "dataset"
id: "impresso-project/nel-mgenre-trie"
source: "huggingface"
url: "https://huggingface.co/datasets/impresso-project/nel-mgenre-trie"
downloads: 119
summary: "mGENRE 기반 다국어 개체명 연결을 위한 위키데이터 QID 조회 및 속성 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
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
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[서비스 데이터]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# impresso-project/nel-mgenre-trie

> dataset · [Hugging Face](https://huggingface.co/datasets/impresso-project/nel-mgenre-trie)

mGENRE 기반 다국어 개체명 연결을 위한 위키데이터 QID 조회 및 속성 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — tag_match · tags = `text2text-generation` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `support multilingual entity linking with mGENRE` · 신뢰도 low
- **작업**: [[문서 검색]] — metadata · task_categories = `text-retrieval` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:information_extraction, task:retrieval = `a title prefix tree that constrains beam search to valid Wikipedia titles` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `106 languages` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `multilingual entity linking with mGENRE` · 신뢰도 low
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `They are the runtime assets for the impresso-project/nel-mgenre-multilingual model as run by the impresso-inference harness` · 신뢰도 low
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high
