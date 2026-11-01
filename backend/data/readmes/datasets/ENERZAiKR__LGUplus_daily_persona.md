---
license: cc-by-nc-4.0
language: [ko]
task_categories: [text-generation, summarization]
tags: [korean, tv, viewing-history, persona, synthetic]
size_categories: [100K<n<1M]
configs:
- config_name: default
  data_files:
  - {split: train, path: data/train.jsonl}
  - {split: test, path: data/test.jsonl}
---

# LGUplus Daily Viewing Persona

하루치 시청기록 → 일일 시청성향 페르소나. 3주치(기존 6/3~9 + 신규 6/7~13, 6/14~20).

- **train** = 기존주(6/3~9) + 신규 첫주(6/7~13) · **test** = 신규 다음주(6/14~20)
- `week` 필드로 주 구분 (2026-06-03 / -06-07 / -06-14). 동일 1만 페르소나가 주마다 등장
- 입력 `viewing`(15분 초과 시청, content_summary 포함) → 출력 interest_genres/time_pattern/keywords/description (교사 LLM Qwen3-235B)
