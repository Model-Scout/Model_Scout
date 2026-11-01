---
license: cc-by-nc-4.0
language: [ko]
task_categories: [text-generation]
tags: [sft, persona, tv, lg-uplus, multi-task]
pretty_name: LG U+ Persona 350M 4-Task SFT
---

# LGUplus_persona_4task_sft

LG U+ 페르소나 350M(ternary QAT) 모델의 **4태스크 SFT 학습 데이터** (실제 학습에 사용한 예시 그대로).
각 행 = `{task, prompt, completion}`. 학습 시 loss는 completion(`<|gen|>` 뒤 JSON+`<|im_end|>`)에만.

## 4태스크
| task | 토큰 | 입력(prompt) | 출력(completion) |
|---|---|---|---|
| `day` | `<\|day\|>` | 그날 시청기록+자막요약 | `{interest_genres, time_pattern, description}` |
| `week` | `<\|week\|>` | 일일페르소나 7일 + 직전주간페르소나(wk0=없음) | `{viewing_tendency, preferred_programs, frequent_channels, preferred_genres, weekday_viewing_times, weekend_viewing_times}` |
| `chan` | `<\|chan\|>` | 주간·직전일 페르소나 + 최근2h 시청 + 후보채널(≤20) | `{"channels":[≤5]}` |
| `kw` | `<\|kw\|>` | 주간·직전일 페르소나 + 후보키워드(≤8) | `{"keyword":"top1"}` |

## 구성 (태스크 균형 서브샘플: chan/kw 각 60,000 ≈ chan+kw 60%)
- `data/train.jsonl` (200,339) : day 60,339 + week 20,000 + chan 60,000 + kw 60,000
- `data/val.jsonl` (20,673) : day 6,673 + week 10,000 + chan 2,000 + kw 2,000

## 스키마
```json
{"task": "chan",
 "prompt": "<|startoftext|><|chan|>성향:...\n선호장르:... 채널:...\n직전일:...\n최근:...\n후보채널:...<|gen|>",
 "completion": "{\"channels\":[\"KBS2\",...]}<|im_end|>"}
```
- week/chan/kw 입력에서 key_keywords 제외. week은 v2 3주(wk0/wk1/wk2), 직전주간 연결.
- 원천 데이터셋: [recommendation_candidates](https://huggingface.co/datasets/HBKenerzai/LGUplus_recommendation_candidates)·[channel_recommendation](https://huggingface.co/datasets/HBKenerzai/LGUplus_channel_recommendation)·[keyword_reranking](https://huggingface.co/datasets/HBKenerzai/LGUplus_keyword_reranking)·[daily/weekly_persona](https://huggingface.co/datasets/HBKenerzai/LGUplus_weekly_persona) 에서 조합·토크나이즈.
