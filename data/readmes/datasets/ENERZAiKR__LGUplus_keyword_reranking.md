---
license: cc-by-nc-4.0
language: [ko]
task_categories: [text-generation]
tags: [reranking, tv, persona, keyword, lg-uplus]
pretty_name: LG U+ Persona Keyword Reranking
---

# LGUplus_keyword_reranking

페르소나 기반 **키워드 top1 선택** 데이터셋. 350m 페르소나 모델의 `<|kw|>` 태스크 학습용.

`(persona, date, 2h block)` 마다: 그 블록에서 **총 15분 이상 시청한 프로그램들의 키워드**(1~8, dedup) 중,
그 사람의 성향을 가장 잘 대표하는 **키워드 1개(top1)**를 고른다.

## 태스크 I/O
- **입력**: 주간 페르소나(전주, key_keywords 제외: viewing_tendency/preferred_genres/preferred_programs/frequent_channels) + 직전일 일일페르소나 서술 + 후보 키워드(1~8). **최근 시청이력은 입력에 넣지 않음**(후보를 만들 때만 사용).
- **출력**: 키워드 1개 (`label_keyword`)
- 후보 키워드 = 그 블록 15분+ 시청 프로그램들의 키워드(프로그램별 1개, dedup). 정답 = 교사 LLM 리랭킹 top1.

## 구성
- `data/train.jsonl` (323,239) : wk0(5/31~6/6)←wk1, wk1(6/7~13)←wk2
- `data/test.jsonl` (165,626) : wk2(6/14~20)←wk1
- 후보가 1개인 블록(대부분)은 그 키워드가 곧 정답.

## 스키마
```json
{"persona_id": 96, "split": "test", "target_week": "wk2", "date": "2026-06-14", "block": 20,
 "viewing_tendency": "...", "preferred_genres": [...], "preferred_programs": [...], "frequent_channels": [...],
 "daily_desc": "직전일 서술",
 "cand_keywords": ["가족의 의미", "주요 사건 보도", ...],   // 1~8
 "label_keyword": "가족의 의미"}
```

관련: [LGUplus_channel_recommendation](https://huggingface.co/datasets/HBKenerzai/LGUplus_channel_recommendation) · 프로그램별 키워드는 별도 생성(235B, epg_summary/gen_keyword).
