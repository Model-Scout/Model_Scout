---
type: "dataset"
id: "HERIUN/kor-ner-spacy-data"
source: "huggingface"
url: "https://huggingface.co/datasets/HERIUN/kor-ner-spacy-data"
downloads: 32
summary: "여러 공개 데이터셋을 수집·변환한 한국어 개체명 인식(NER) 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[정보 추출]]"
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
---
# HERIUN/kor-ner-spacy-data

> dataset · [Hugging Face](https://huggingface.co/datasets/HERIUN/kor-ner-spacy-data)

여러 공개 데이터셋을 수집·변환한 한국어 개체명 인식(NER) 학습용 데이터셋입니다.

## 분류

- **작업**: [[정보 추출]] — metadata · readme, tags, task_categories, task_ids = `token-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:information_extraction = `각 줄은 하나의 문장이며 JSONL 형식입니다.
{"text": "홍길동이 서울에 산다.", "entities": [[0, 3, "PER"], [5, 7, "LOC"]]}` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `entities : [start, end, label] 리스트` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 NER(Named Entity Recognition) 학습을 위해 여러 공개 데이터셋을 수집·변환한 데이터셋입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `한국어 NER(Named Entity Recognition) 학습을 위해 여러 공개 데이터셋을 수집·변환한 데이터셋입니다.` · 신뢰도 medium
