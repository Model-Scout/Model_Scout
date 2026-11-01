---
license: cc-by-nc-4.0
language: [ko]
task_categories: [text-generation]
tags: [recommendation, tv, persona, channel, lg-uplus]
pretty_name: LG U+ Persona Channel Recommendation
---

# LGUplus_channel_recommendation

페르소나 기반 **채널 추천** 데이터셋 (추천 top5에서 파생). 350m 페르소나 모델의 `<|chan|>` 태스크 학습용.

`(persona, date, 2h block)` 마다: 컨텍스트를 보고 후보 채널(≤20) 중 그 시간대에 볼 **채널 5개**를 고른다.

## 태스크 I/O
- **입력**: 주간 페르소나(전주, key_keywords 제외: viewing_tendency/preferred_genres/preferred_programs/frequent_channels) + 직전일 일일페르소나 서술 + 직전 2시간 시청(총 15분+) + 후보 채널(≤20)
- **출력**: 채널 5개 (`label_channels`)
- 후보 채널 = 추천 20개 프로그램 후보(A∪B)의 채널 dedup(≤20). 정답 = 교사가 뽑은 top5 프로그램의 채널 dedup(≤5).

## 구성
- `data/train.jsonl` (1,620,000) : wk0(5/31~6/6)←wk1, wk1(6/7~13)←wk2
- `data/test.jsonl` (840,000) : wk2(6/14~20)←wk1

## 스키마
```json
{"persona_id": 96, "split": "test", "target_week": "wk2", "date": "2026-06-14", "block": 20,
 "viewing_tendency": "...", "preferred_genres": [...], "preferred_programs": [...], "frequent_channels": [...],
 "daily_desc": "직전일 서술",
 "recent": [{"channel": "KBS1", "title": "뉴스9", "summary": "..."}],
 "cand_channels": ["EBS1", ...],   // ≤20
 "label_channels": ["EBS1", ...]}  // ≤5
```
`recent`는 직전 2시간에 총 15분 이상 시청한 프로그램만. 심야 등 직전 시청 없으면 `[]`.

관련: [LGUplus_recommendation_candidates](https://huggingface.co/datasets/HBKenerzai/LGUplus_recommendation_candidates) (프로그램 top5 원본) · [LGUplus_keyword_reranking](https://huggingface.co/datasets/HBKenerzai/LGUplus_keyword_reranking)
