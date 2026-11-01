---
type: "dataset"
id: "Nagase-Kotono/LLaVA-CoT-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/Nagase-Kotono/LLaVA-CoT-ko"
downloads: 38
summary: "LLaVA-CoT 논문 기반 한국어 시각-언어 멀티모달 추론 데이터셋으로 복합 시각 질의응답에 활용됨."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[문서 검색]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
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
  - "[[중규모 데이터]]"
---
# Nagase-Kotono/LLaVA-CoT-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/Nagase-Kotono/LLaVA-CoT-ko)

LLaVA-CoT 논문 기반 한국어 시각-언어 멀티모달 추론 데이터셋으로 복합 시각 질의응답에 활용됨.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `structured approach enables LLaVA-CoT to achieve marked improvements on reasoning-intensive tasks` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `complex visual question-answering tasks` · 신뢰도 medium
- **작업**: [[문서 검색]] — ner · readme = `test-time stage-wise retracing search method (SWIRES), which enables effective and efficient test-time scaling` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-text-to-text` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:visual_qa = `visual question answering sources` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering, task:retrieval, task:visual_qa = `Korean version of the LLaVA-CoT-100k dataset` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering, task:visual_qa = `structured reasoning annotations` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Vision-Language Models (VLMs)` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `with only 100k training samples` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
