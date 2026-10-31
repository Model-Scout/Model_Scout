---
license: cc-by-nc-4.0
language: [ko]
task_categories: [text-generation]
tags: [sft, persona, tv, lg-uplus, multi-task, rolling-persona]
pretty_name: LG U+ Persona 350M 4-Task SFT v2 (rolling)
---

# LGUplus_persona_4task_sft_v2

LG U+ 페르소나 350M(ternary QAT) 모델의 **rolling 기반 SFT 학습 데이터** (v1의 rolling 버전).
각 행 = `{task, prompt, completion}`. 학습 시 loss는 completion(`<|gen|>` 뒤 + `<|im_end|>`)에만.

v1(`LGUplus_persona_4task_sft`)과의 차이:
- **일일(`day`)+주간(`week`) 페르소나 태스크를 rolling 페르소나 갱신 태스크 하나(`persona`)로 통합** → 4태스크 → **3태스크**.
- 추천(`chan`)·키워드(`kw`)의 페르소나 컨텍스트를 주간+직전일 대신 **전일까지 갱신된 rolling 페르소나 텍스트**로 대체.

## 3태스크
| task | 토큰 | 입력(prompt) | 출력(completion) |
|---|---|---|---|
| `persona` | `<\|persona\|>` | `[이전 페르소나]` + `[오늘 시청 기록]` | 갱신된 페르소나 텍스트(`[장기 성향]`+`[최근 성향]`+`[시청 프로그램]` 표) |
| `chan` | `<\|chan\|>` | rolling 페르소나 + 최근2h 시청 + 후보채널(**20개**, 유니버스 distractor로 증강·셔플) | `{"channels":[≤5]}` |
| `kw` | `<\|kw\|>` | rolling 페르소나 + 후보키워드(≥2) [최근시청 미포함] | `{"keyword":"top1"}` |

## 구성 (서브샘플: persona 전량, chan/kw 각 100,000)
- `data/train.jsonl` (399,238) : persona 199,238 + chan 100,000 + kw 100,000
- `data/val.jsonl` (5,997) : persona 1,997 + chan 2,000 + kw 2,000

chan은 후보채널≥2, kw는 후보키워드≥2(실제 리랭크)만 포함. 라벨은 항상 후보의 부분집합(검증됨).

## 스키마
```json
{"task": "chan",
 "prompt": "<|startoftext|><|chan|>[페르소나]\n[장기 성향]...\n[최근 성향]...\n[시청 프로그램]...\n최근:...\n후보채널:KBS2,...<|gen|>",
 "completion": "{\"channels\":[\"KBS2\",...]}<|im_end|>"}
```

## 원천 데이터셋 (rolling)
- [jungsanghyun/lgu-rolling-persona-aug](https://huggingface.co/datasets/jungsanghyun/lgu-rolling-persona-aug) — `persona` 태스크 (시기 다양성 증강본). **[주요 시청 프로그램] 표는 최근 7일 미시청 프로그램을 드랍 보정**(원본은 안 본 프로그램도 계속 '상승'으로 유지되는 문제가 있어 후처리; persona_table_fix.py). 입력 [이전 페르소나]는 원본 유지 → "입력에 stale 있어도 출력에서 드랍" 학습.
- [HBKenerzai/LGUplus_recommendation_top5_rolling](https://huggingface.co/datasets/HBKenerzai/LGUplus_recommendation_top5_rolling) — 프로그램 top5 → 채널 dedup 변환(`chan`)
- [HBKenerzai/LGUplus_keyword_rerank_top1_rolling](https://huggingface.co/datasets/HBKenerzai/LGUplus_keyword_rerank_top1_rolling) — 키워드 top1(`kw`)

주차: wk0=5/31~6/6, wk1=6/7~13, wk2=6/14~20 (연속 3주). chan/kw의 페르소나 컨텍스트는 각 행 `persona_date`(전일까지 갱신) 스냅샷.
