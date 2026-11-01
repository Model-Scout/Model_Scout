---
type: "dataset"
id: "Roshang09112007/adaption-air-bench-healthcare-zh"
source: "huggingface"
url: "https://huggingface.co/datasets/Roshang09112007/adaption-air-bench-healthcare-zh"
downloads: 14
summary: "중국어 의료 질의응답 데이터로 의료 분야 검색-생성 시스템 평가용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
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
  - "[[이용 조건 미확인]]"
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Roshang09112007/adaption-air-bench-healthcare-zh

> dataset · [Hugging Face](https://huggingface.co/datasets/Roshang09112007/adaption-air-bench-healthcare-zh)

중국어 의료 질의응답 데이터로 의료 분야 검색-생성 시스템 평가용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `The data is formatted as prompt-completion pairs where prompts represent medical queries and completions reference specific document IDs.` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `It is designed for evaluating retrieval-augmented generation systems in the medical domain.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:retrieval = `The data is formatted as prompt-completion pairs where prompts represent medical queries` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `multilingual` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[의료·보건]] — ner · readme = `This dataset contains Chinese healthcare question-answer pairs from the AIR-Bench 24.05 benchmark` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `specifically focusing on the default development and test splits.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
