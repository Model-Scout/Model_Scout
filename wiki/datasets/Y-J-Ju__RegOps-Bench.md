---
type: "dataset"
id: "Y-J-Ju/RegOps-Bench"
source: "huggingface"
url: "https://huggingface.co/datasets/Y-J-Ju/RegOps-Bench"
downloads: 66
summary: "한국 국가 연구개발 규제 준수 QA를 위한 RegOps-Bench 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
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
  - "[[법률]]"
dataset_role:
  - "[[평가용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Y-J-Ju/RegOps-Bench

> dataset · [Hugging Face](https://huggingface.co/datasets/Y-J-Ju/RegOps-Bench)

한국 국가 연구개발 규제 준수 QA를 위한 RegOps-Bench 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — metadata · task_categories, task_ids = `question-answering` · 신뢰도 low
- **작업**: [[문서 검색]] — metadata · readme, task_categories, task_ids = `text-retrieval` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:question_answering, task:retrieval = `Each question targets a specific procedural decision a researcher or administrator would face when conducting government-funded research in Korea` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `evaluation QA pairs with ground-truth references back into the corpus` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · readme, tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
