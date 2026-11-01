---
license: cc-by-nc-4.0
language: [ko]
task_categories: [text-generation]
tags: [persona, tv, lg-uplus, rolling]
pretty_name: LG U+ Rolling Persona (aug, table-corrected)
---

# LGUplus_rolling_persona_aug

[jungsanghyun/lgu-rolling-persona-aug](https://huggingface.co/datasets/jungsanghyun/lgu-rolling-persona-aug)
의 **[주요 시청 프로그램] 표를 실제 시청기록으로 양방향 재구성한 판**.

원본 문제: 표가 단방향 누적이라 (1) 안 본 프로그램도 계속 '상승'으로 잔류(DROP 안 됨),
(2) 새로 꾸준히 본 프로그램이 표에 안 들어감(3일+ 시청의 62%가 누락).

보정: 표 각 행에 **연속 미시청 일수**를 명시하고 실제 시청기록으로 재체이닝(상태기계).
- 오늘 시청 → 미시청 0, 미시청 → +1, **미시청 ≥ 10일 → 드랍**, 신규 시청 → 미시청 0 으로 추가(채널·요일·시간·장르 합성).
- `[장기 성향]`·`[최근 성향]` 서술과 user/system 메시지는 원본 그대로, 표만 교체.
- 표기: `제목 | 채널 | 요일 | 시간 | 장르 | 미시청 N일`.

스키마: `persona_id, date, dow, mode, messages([system,user,assistant])` — 원본과 동일.
