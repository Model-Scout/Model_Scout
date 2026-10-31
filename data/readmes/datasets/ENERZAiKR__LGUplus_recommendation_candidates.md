---
license: cc-by-nc-4.0
language:
- ko
task_categories:
- text-generation
tags:
- recommendation
- tv
- persona
- lg-uplus
pretty_name: LG U+ Persona TV Recommendation Candidates
---

# LGUplus_recommendation_candidates

LG U+ 페르소나 기반 TV 추천 파이프라인의 **1차 후보 목록**(A∪B, combo당 최대 20개)과
후보 id를 프로그램 상세로 조인하기 위한 **프로그램 테이블**입니다.
최종 top5 선정(교사 LLM)은 이 후보에서 5개를 고르는 다음 단계이며, 여기엔 후보까지만 포함합니다.

## 구성

하루를 12개 2시간 블록으로 나눔. `(persona_id, date, block)` 마다 후보 2종:
- **cand_stat (후보A · 시청통계)**: 기반주에 그 페르소나가 가장 많이 본 채널 top10, 각 채널에서 그 블록에 가장 먼저 시작하는 프로그램 1개 (≤10).
- **cand_persona (후보B · 주간페르소나)**: 그 블록 프로그램을 주간페르소나 프로필과 ko-sroberta 임베딩 유사도 + 시청장르 비례배분으로 뽑은 10개.
- 두 후보는 겹칠 수 있으며 dedup 후 **A∪B ≤ 20** (평균 ~17).

주차: wk0(6/3~9), wk1(6/7~13), wk2(6/14~20). 대상주←기반주 구성:
- **train** (`data/rec_train.jsonl`, 1,620,000행): wk0←wk1, wk1←wk2
- **test** (`data/rec_test.jsonl`, 840,000행): wk2←wk1

## 파일

| 파일 | 행 | 내용 |
|---|---|---|
| `data/rec_train.jsonl` | 1,620,000 | train 후보 (persona×date×block) |
| `data/rec_test.jsonl` | 840,000 | test 후보 |
| `data/programs_wk0.jsonl` | 49,680 | wk0 프로그램 상세 (id→제목/채널/장르/시작시각) |
| `data/programs_wk1.jsonl` | 45,761 | wk1 프로그램 상세 |
| `data/programs_wk2.jsonl` | 49,927 | wk2 프로그램 상세 |

## 스키마

**rec_{train,test}.jsonl**
```json
{"persona_id": 96, "split": "test", "target_week": "wk2", "basis_week": "wk1",
 "date": "2026-06-14", "block": 0,
 "cand_stat": [45250, ...], "cand_persona": [45254, ...]}
```
`target_week` = 추천 대상 EPG 주차, `basis_week` = 통계·페르소나 기반 주차. `block` = 0,2,…,22시.

**programs_{wk}.jsonl**
```json
{"program_id": 1009, "channel_name": "AsiaUHD", "title": "히스토리야 시즌3 (1회)<재>",
 "genre": "시사/교양", "start_time": "2026-06-14 00:00:00"}
```
후보 id는 `target_week` 에 대응하는 `programs_{wk}` 로 조인합니다.

## 관련 데이터셋
페르소나/시청이력/요약은 별도 업로드:
[LGUplus_weekly_persona](https://huggingface.co/datasets/HBKenerzai/LGUplus_weekly_persona) ·
[LGUplus_daily_persona](https://huggingface.co/datasets/HBKenerzai/LGUplus_daily_persona) ·
[LGUplus_viewing_history](https://huggingface.co/datasets/HBKenerzai/LGUplus_viewing_history) ·
[LGUplus_epg_summary](https://huggingface.co/datasets/HBKenerzai/LGUplus_epg_summary)
