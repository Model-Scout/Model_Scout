---
type: "dataset"
id: "ko-vlm/KVQA-ChatML"
source: "huggingface"
url: "https://huggingface.co/datasets/ko-vlm/KVQA-ChatML"
downloads: 1024
summary: "SKT의 KVQA 데이터셋을 ChatML 형식으로 변환한 한국어 시각질의응답 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
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
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# ko-vlm/KVQA-ChatML

> dataset · [Hugging Face](https://huggingface.co/datasets/ko-vlm/KVQA-ChatML)

SKT의 KVQA 데이터셋을 ChatML 형식으로 변환한 한국어 시각질의응답 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `포맷: ChatML (user/assistant 대화 형식)` · 신뢰도 medium
- **작업**: [[질의응답]] — ner · readme = `KVQA (Korean Visual Question Answering)` · 신뢰도 medium
- **작업**: [[이미지 이해]] — metadata · tags, task_categories, task_ids = `visual-question-answering` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:visual_qa = `"image": PIL.Image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering, task:visual_qa = `"role": "user", "content": "질문"` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering, task:visual_qa = `"role": "assistant", "content": "답변"` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `KVQA (Korean Visual Question Answering)` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `이 데이터셋은 SKT의 KVQA 데이터셋을 ChatML 형식으로 변환한 것입니다.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
