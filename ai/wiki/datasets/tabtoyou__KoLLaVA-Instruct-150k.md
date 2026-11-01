---
type: "dataset"
id: "tabtoyou/KoLLaVA-Instruct-150k"
source: "huggingface"
url: "https://huggingface.co/datasets/tabtoyou/KoLLaVA-Instruct-150k"
downloads: 27
summary: "LLaVA의 Instruction-following 데이터를 한국어로 번역한 시각적 질의응답 및 설명 데이터셋입니다."
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
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# tabtoyou/KoLLaVA-Instruct-150k

> dataset · [Hugging Face](https://huggingface.co/datasets/tabtoyou/KoLLaVA-Instruct-150k)

LLaVA의 Instruction-following 데이터를 한국어로 번역한 시각적 질의응답 및 설명 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `이미지에 대한 풍부하고 포괄적인 설명을 내포하게 디자인 했습니다.` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 medium
- **작업**: [[이미지 이해]] — metadata · task_categories = `visual-question-answering` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:visual_qa = `이미지에 대해 질문하는 사람과 이에 답하는 Assistant 사이의 대화 형식으로 디자인합니다.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering, task:visual_qa = `이미지에 대해 질문하는 사람과 이에 답하는 Assistant 사이의 대화 형식으로 디자인합니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering, task:visual_qa = `대답은 Assistant가 이미지를 보고 질문에 대답하는 것과 같은 어조이며` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `LLaVA의 Instruction-following Dataset을 한국어로 번역한 데이터셋입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `LLaVA의 Instruction-following Dataset을 한국어로 번역한 데이터셋입니다.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
