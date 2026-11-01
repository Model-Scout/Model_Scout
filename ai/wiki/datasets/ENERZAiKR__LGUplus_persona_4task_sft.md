---
type: "dataset"
id: "ENERZAiKR/LGUplus_persona_4task_sft"
source: "huggingface"
url: "https://huggingface.co/datasets/ENERZAiKR/LGUplus_persona_4task_sft"
downloads: 6
summary: "LG U+ 페르소나 350M 모델의 4태스크 SFT 학습 데이터로 개인화 추천에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[비상업 전용]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# ENERZAiKR/LGUplus_persona_4task_sft

> dataset · [Hugging Face](https://huggingface.co/datasets/ENERZAiKR/LGUplus_persona_4task_sft)

LG U+ 페르소나 350M 모델의 4태스크 SFT 학습 데이터로 개인화 추천에 활용됨.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `각 행 = {task, prompt, completion}` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `학습 시 loss는 completion(<|gen|> 뒤 JSON+<|im_end|>)에만.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `4태스크 SFT 학습 데이터 (실제 학습에 사용한 예시 그대로)` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
