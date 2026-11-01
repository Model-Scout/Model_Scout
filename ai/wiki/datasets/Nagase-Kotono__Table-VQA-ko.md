---
type: "dataset"
id: "Nagase-Kotono/Table-VQA-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/Nagase-Kotono/Table-VQA-ko"
downloads: 40
summary: "한국어 표 이미지 대화 데이터셋으로, 표 이미지에 대한 질문과 답변을 포함합니다."
readme_status: "ok"
readme_language: "ko"
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
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Nagase-Kotono/Table-VQA-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/Nagase-Kotono/Table-VQA-ko)

한국어 표 이미지 대화 데이터셋으로, 표 이미지에 대한 질문과 답변을 포함합니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `한국어 싱글, 멀티런 표 이미지 대화 데이터셋입니다.` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `visual-question-answering` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:visual_qa = `한국어 싱글, 멀티런 표 이미지 대화 데이터셋입니다.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:question_answering, task:visual_qa = `LLaVA 형식에 맞게 제작되었습니다.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering, task:visual_qa = `한국어 싱글, 멀티런 표 이미지 대화 데이터셋입니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 싱글, 멀티런 표 이미지 대화 데이터셋입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `제작중인 데이터셋 인 것입니닷!!! 가끔 업데이트 될거 같아요.` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
