---
type: "dataset"
id: "KETI-NLP/korean-heritage-qa"
source: "huggingface"
url: "https://huggingface.co/datasets/KETI-NLP/korean-heritage-qa"
downloads: 122
summary: "문화재 사진과 한국어 QA 문항으로 구성된 비상업적 한국어 문화재 QA 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[문화·관광]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# KETI-NLP/korean-heritage-qa

> dataset · [Hugging Face](https://huggingface.co/datasets/KETI-NLP/korean-heritage-qa)

문화재 사진과 한국어 QA 문항으로 구성된 비상업적 한국어 문화재 QA 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `문화재 사진 1장과 user/assistant 1쌍으로 이루어진 한국어 QA 데이터입니다.` · 신뢰도 medium
- **작업**: [[이미지 이해]] — metadata · task_categories = `visual-question-answering` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:visual_qa = `문화재 사진 1장과 user/assistant 1쌍으로 이루어진 한국어 QA 데이터입니다.` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering, task:visual_qa = `user 질문과 assistant 정답.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering, task:visual_qa = `user 질문과 assistant 정답.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `문화재 사진 1장과 user/assistant 1쌍으로 이루어진 한국어 QA 데이터입니다.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `QA 예제 전체의 상업적 이용은 이번 공개 라이선스에서 허용하지 않습니다.` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
