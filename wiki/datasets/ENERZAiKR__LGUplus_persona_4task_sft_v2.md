---
type: "dataset"
id: "ENERZAiKR/LGUplus_persona_4task_sft_v2"
source: "huggingface"
url: "https://huggingface.co/datasets/ENERZAiKR/LGUplus_persona_4task_sft_v2"
downloads: 8
summary: "LG U+ 페르소나 350M 모델의 rolling 기반 SFT 학습 데이터로, 페르소나 갱신 및 추천 태스크에 사용됨."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# ENERZAiKR/LGUplus_persona_4task_sft_v2

> dataset · [Hugging Face](https://huggingface.co/datasets/ENERZAiKR/LGUplus_persona_4task_sft_v2)

LG U+ 페르소나 350M 모델의 rolling 기반 SFT 학습 데이터로, 페르소나 갱신 및 추천 태스크에 사용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `chan은 후보채널≥2, kw는 후보키워드≥2(실제 리랭크)만 포함. 라벨은 항상 후보의 부분집합(검증됨)` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `각 행 = `{task, prompt, completion}`` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `각 행 = `{task, prompt, completion}`` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `LG U+ 페르소나 350M(ternary QAT) 모델의 rolling 기반 SFT 학습 데이터` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
