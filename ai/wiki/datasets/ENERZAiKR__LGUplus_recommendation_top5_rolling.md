---
type: "dataset"
id: "ENERZAiKR/LGUplus_recommendation_top5_rolling"
source: "huggingface"
url: "https://huggingface.co/datasets/ENERZAiKR/LGUplus_recommendation_top5_rolling"
downloads: 8
summary: "LGUplus TV 시청자 롤링 페르소나 기반 top5 프로그램 추천 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[리랭킹]]"
  - "[[문서 검색]]"
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
---
# ENERZAiKR/LGUplus_recommendation_top5_rolling

> dataset · [Hugging Face](https://huggingface.co/datasets/ENERZAiKR/LGUplus_recommendation_top5_rolling)

LGUplus TV 시청자 롤링 페르소나 기반 top5 프로그램 추천 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[리랭킹]] — ner · readme = `교사 LLM(Qwen3-235B-A22B-Instruct-2507-FP8)이 그 시청자가 그 시간대에 '실제로 볼' top5 를 고른 결과` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `LGUplus TV 추천 (rolling-persona 기반, self-contained · 채널급 포함)` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation, task:reranking, task:retrieval = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `그 시청자가 그 시간대에 '실제로 볼' top5 를 고른 결과.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `LGUplus TV 추천 (rolling-persona 기반, self-contained · 채널급 포함)` · 신뢰도 low
