---
type: "dataset"
id: "KorQuAD/squad_kor_v2"
source: "huggingface"
url: "https://huggingface.co/datasets/KorQuAD/squad_kor_v2"
downloads: 158
summary: "KorQuAD 2.0은 한국어 위키피디아 문서 기반 질의응답 데이터셋으로 다양한 길이와 형식의 답변을 포함합니다."
readme_status: "template"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[정보 추출]]"
  - "[[질의응답]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# KorQuAD/squad_kor_v2

> dataset · [Hugging Face](https://huggingface.co/datasets/KorQuAD/squad_kor_v2)

KorQuAD 2.0은 한국어 위키피디아 문서 기반 질의응답 데이터셋으로 다양한 길이와 형식의 답변을 포함합니다.

## 분류

- **작업**: [[정보 추출]] — ner · readme = `the answer can be a long text covering not only word or phrase units, but paragraphs, tables, and lists` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · readme, task_categories, task_ids = `question-answering` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `the document also contains tables and lists` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:information_extraction, task:question_answering = `a given document is a whole Wikipedia page` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `the answer can be a long text covering not only word or phrase units, but paragraphs, tables, and lists` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `cc-by-nd-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `a given document is a whole Wikipedia page` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `As a baseline model, BERT Multilingual is used, released by Google as an open source` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
