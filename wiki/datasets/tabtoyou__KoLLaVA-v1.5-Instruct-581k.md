---
type: "dataset"
id: "tabtoyou/KoLLaVA-v1.5-Instruct-581k"
source: "huggingface"
url: "https://huggingface.co/datasets/tabtoyou/KoLLaVA-v1.5-Instruct-581k"
downloads: 71
summary: "LLaVA-v1.5의 Instruction-following 데이터를 필터링하고 한국어로 번역한 시각 지시 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[비상업 전용]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# tabtoyou/KoLLaVA-v1.5-Instruct-581k

> dataset · [Hugging Face](https://huggingface.co/datasets/tabtoyou/KoLLaVA-v1.5-Instruct-581k)

LLaVA-v1.5의 Instruction-following 데이터를 필터링하고 한국어로 번역한 시각 지시 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Instruction-following Data에서 필요한 데이터를 필터링하고, 한국어로 번역한 데이터셋입니다.` · 신뢰도 medium
- **작업**: [[이미지 이해]] — metadata · task_categories = `visual-question-answering` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:visual_qa = `이미지 다운로드 및 사용 방법은 KoLLaVA repo를 참고해주세요.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:visual_qa = `Instruction-following Data에서 필요한 데이터를 필터링하고, 한국어로 번역한 데이터셋입니다.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:visual_qa = `Instruction-following Data에서 필요한 데이터를 필터링하고, 한국어로 번역한 데이터셋입니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `Instruction-following Data에서 필요한 데이터를 필터링하고, 한국어로 번역한 데이터셋입니다.` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
