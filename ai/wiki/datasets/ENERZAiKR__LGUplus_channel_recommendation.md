---
type: "dataset"
id: "ENERZAiKR/LGUplus_channel_recommendation"
source: "huggingface"
url: "https://huggingface.co/datasets/ENERZAiKR/LGUplus_channel_recommendation"
downloads: 41
summary: "LG U+ 페르소나 기반 채널 추천 데이터셋으로, 2시간 블록별 채널 5개 추천 학습용입니다."
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
dataset_role:
  - "[[학습용]]"
---
# ENERZAiKR/LGUplus_channel_recommendation

> dataset · [Hugging Face](https://huggingface.co/datasets/ENERZAiKR/LGUplus_channel_recommendation)

LG U+ 페르소나 기반 채널 추천 데이터셋으로, 2시간 블록별 채널 5개 추천 학습용입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `페르소나 기반 채널 추천 데이터셋 (추천 top5에서 파생)` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:generation = `입력: 주간 페르소나(전주, key_keywords 제외: viewing_tendency/preferred_genres/preferred_programs/frequent_channels) + 직전일 일일페르소나 서술 + 직전 2시간 시청(총 15분+) + 후보 채널(≤20)` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `350m 페르소나 모델의 ` ` 태스크 학습용.` · 신뢰도 medium
