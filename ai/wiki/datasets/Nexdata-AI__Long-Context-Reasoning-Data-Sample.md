---
type: "dataset"
id: "Nexdata-AI/Long-Context-Reasoning-Data-Sample"
source: "huggingface"
url: "https://huggingface.co/datasets/Nexdata-AI/Long-Context-Reasoning-Data-Sample"
downloads: 12
summary: "긴 문서와 복잡한 추론을 다루는 다국어(중국어, 영어, 한국어) 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[질의응답]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Nexdata-AI/Long-Context-Reasoning-Data-Sample

> dataset · [Hugging Face](https://huggingface.co/datasets/Nexdata-AI/Long-Context-Reasoning-Data-Sample)

긴 문서와 복잡한 추론을 다루는 다국어(중국어, 영어, 한국어) 학습용 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `includes questions that require synthesizing information across paragraphs and documents, while following multi-step logical chains` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — metadata · modality = `document` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:question_answering = `Each instance is built around a long-text passage` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `includes questions that require synthesizing information across paragraphs and documents` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `long documents and performing complex reasoning` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `It consists of 7,500 high-quality training examples` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
