---
license: cc-by-nc-4.0
language: [ko]
task_categories: [text-generation]
tags: [recommendation, korean-tv, persona, rolling, top5, channel]
---

# LGUplus TV 추천 (rolling-persona 기반, self-contained · 채널급 포함)

`(persona, date, block)` 마다 후보 프로그램 A∪B(≤20) 중 교사 LLM(**Qwen3-235B-A22B-Instruct-2507-FP8**)이
그 시청자가 그 시간대에 '실제로 볼' **top5** 를 고른 결과.

**persona 컨텍스트**: [`jungsanghyun/lgu-rolling-persona`](https://huggingface.co/datasets/jungsanghyun/lgu-rolling-persona)
의 **전일까지 갱신된 롤링 페르소나**(장기 성향 + 최근 성향 + 고정 시청 프로그램 표). 추천대상 날짜의 직전 스냅샷을 쓰며, 그날 시청이 없으면 더 과거 스냅샷으로 백워크한다.

**업데이트**: 이제 각 행이 **입력을 포함(self-contained)** 하며, program-level `picks` 에 더해 **채널급**(`cand_channels`/`label_channels`) 도 제공한다.

## 필드
| 필드 | 설명 |
|---|---|
| `persona_id` | 시청자 ID |
| `split` | test / train |
| `target_week` | 대상 주차 |
| `date` / `block` | 추천 대상 날짜 / 2시간 블록(0,2,...,22) |
| `n_cand` | 후보 개수 |
| `persona_date` | 사용된 롤링 페르소나 스냅샷 날짜 (as-of 전일) |
| `picks` | 선택된 program_id 5개 (program-level) |
| `persona_text` | **(신규)** 사용된 롤링 페르소나 스냅샷 본문 (없으면 "") |
| `recent` | **(신규)** 직전 2시간 15분+ 시청 `[{channel,title,summary}]` |
| `cand_channels` | **(신규)** 후보 채널 **20개** — 후보 프로그램 채널 dedup + 주차 채널 유니버스 distractor로 20개 증강(셔플) |
| `label_channels` | **(신규)** `picks` 프로그램들의 채널 dedup — 채널급 정답 (⊆ `cand_channels`) |

`picks` 상세는 `HBKenerzai/LGUplus_recommendation_candidates` 의 `programs_{target_week}.jsonl` 로 조인.

## 출처
- 후보/프로그램표: `HBKenerzai/LGUplus_recommendation_candidates`
- 롤링 페르소나: `jungsanghyun/lgu-rolling-persona`
- 시청이력/요약: `HBKenerzai/LGUplus_viewing_history`, `HBKenerzai/LGUplus_epg_summary`
