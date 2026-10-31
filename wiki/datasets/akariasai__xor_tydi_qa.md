---
type: "dataset"
id: "akariasai/xor_tydi_qa"
source: "huggingface"
url: "https://huggingface.co/datasets/akariasai/xor_tydi_qa"
downloads: 245
summary: "XOR-TyDi QA는 7개 언어의 정보 탐색 질문과 다국어 교차 언어 답변 검색을 위한 QA 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[질의응답]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[ar]]"
  - "[[bn]]"
  - "[[fi]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[ru]]"
  - "[[te]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# akariasai/xor_tydi_qa

> dataset · [Hugging Face](https://huggingface.co/datasets/akariasai/xor_tydi_qa)

XOR-TyDi QA는 7개 언어의 정보 탐색 질문과 다국어 교차 언어 답변 검색을 위한 QA 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories, task_ids = `question-answering` · 신뢰도 medium
- **작업**: [[문서 검색]] — ner · readme = `XOR-Retrieve is a cross-lingual retrieval task where a question is written in a target language (e.g., Japanese) and a system is required to retrieve English pa` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:question_answering, task:retrieval = `A typical data point comprises a `question`, it's `answer` the `language` of the question text and the split to which it belongs.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `XOR-English Span is a cross-lingual retrieval task where a question is written in a target language (e.g., Japanese) and a system is required to output a short ` · 신뢰도 medium
- **언어**: [[ar]] — metadata · languages = `ar` · 신뢰도 high
- **언어**: [[bn]] — metadata · languages = `bn` · 신뢰도 high
- **언어**: [[fi]] — metadata · languages = `fi` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `7 languages` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[te]] — metadata · languages = `te` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `XOR-TyDi QA brings together for the first time information-seeking questions, open-retrieval QA, and multilingual QA to create a multilingual open-retrieval QA ` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The data is split into a training, validation and test set for each of the two configurations.` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
