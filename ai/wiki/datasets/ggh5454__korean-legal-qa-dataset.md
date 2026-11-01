---
type: "dataset"
id: "ggh5454/korean-legal-qa-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/ggh5454/korean-legal-qa-dataset"
downloads: 80
summary: "법령 조문과 판례를 연결한 한국어 법률 질의응답 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[법률]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# ggh5454/korean-legal-qa-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/ggh5454/korean-legal-qa-dataset)

법령 조문과 판례를 연결한 한국어 법률 질의응답 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, tags, task_categories = `question-answering` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:question_answering = `각 항목은 질문(question), 정답(answer), 검색문서(retrieved_documents) 3가지 필드로 구성됩니다` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `각 항목은 질문(question), 정답(answer), 검색문서(retrieved_documents) 3가지 필드로 구성됩니다` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · readme, tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `베제처 국가법령정보센터의 공개 법령·판례 데이터를 바탕으로 구축되었습니다.` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
