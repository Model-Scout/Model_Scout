---
type: "dataset"
id: "mansiksohn/opendict-korean-proverb"
source: "huggingface"
url: "https://huggingface.co/datasets/mansiksohn/opendict-korean-proverb"
downloads: 46
summary: "국립국어원 우리말샘 속담을 정제한 한국어 속담 데이터셋입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# mansiksohn/opendict-korean-proverb

> dataset · [Hugging Face](https://huggingface.co/datasets/mansiksohn/opendict-korean-proverb)

국립국어원 우리말샘 속담을 정제한 한국어 속담 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — metadata · task_ids = `language-modeling` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `국립국어원 누리집 사전에 실려 있는 속담을 '자세히 찾기' 기능을 활용하여 보실 수 있습니다.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling, task:retrieval = `국립국어원 우리말샘의 속담을 정제해 만든 데이터입니다.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `국립국어원 우리말샘의 속담을 정제해 만든 데이터입니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `국립국어원 우리말샘의 속담을 정제해 만든 데이터입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `국립국어원 우리말샘의 속담을 정제해 만든 데이터입니다.` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
