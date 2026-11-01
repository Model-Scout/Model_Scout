---
license: cc-by-nc-4.0
language: [ko]
task_categories: [text-generation]
tags: [keyword, reranking, korean-tv, persona, rolling]
---

# LGUplus 키워드 top1 리랭킹 (rolling-persona 기반, self-contained)

`(persona, date, block)` 마다 그 시청자가 그 블록에 15분+ 시청한 프로그램들의 **키워드 후보** 중,
그 사람의 관심사를 가장 잘 대표하는 **키워드 1개**를 교사 LLM(**Qwen3-235B-A22B-Instruct-2507-FP8**)이 선택.

**persona 컨텍스트**: [`jungsanghyun/lgu-rolling-persona`](https://huggingface.co/datasets/jungsanghyun/lgu-rolling-persona)
의 전일까지 갱신된 롤링 페르소나(장기+최근 성향+시청표), 추천대상 날짜의 직전 스냅샷(없으면 백워크).
후보 키워드는 그 블록 시청 프로그램의 키워드(페르소나 무관, 최근 시청은 미고려). 후보가 1개면 LLM 없이 그대로, 2개+ 만 LLM 선택.

**업데이트**: 이제 각 행이 **입력을 포함(self-contained)** — 페르소나 본문(`persona_text`)과 후보 키워드(`cand_keywords`) 를 함께 제공.

## 필드
| 필드 | 설명 |
|---|---|
| `persona_id` / `split` / `target_week` / `date` / `block` | 대상 식별 |
| `n_cand` | 후보 키워드 개수 |
| `keyword` | 선택된 키워드 (top1) |
| `persona_date` | 사용된 롤링 페르소나 스냅샷 날짜 (as-of 전일) |
| `persona_text` | **(신규)** 사용된 롤링 페르소나 스냅샷 본문 (없으면 "") |
| `cand_keywords` | **(신규)** 후보 키워드 목록 — `keyword` 는 이 중 top1 (⊇ `keyword`) |

## 출처
- 후보 키워드/프로그램: `HBKenerzai/LGUplus_keyword_reranking`, `HBKenerzai/LGUplus_epg_summary`
- 롤링 페르소나: `jungsanghyun/lgu-rolling-persona`
