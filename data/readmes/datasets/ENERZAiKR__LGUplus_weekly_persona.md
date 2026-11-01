---
license: cc-by-nc-4.0
language: [ko]
task_categories: [text-generation, summarization]
tags: [korean, tv, viewing-history, persona, user-profiling, synthetic]
size_categories: [10K<n<100K]
configs:
- config_name: default
  data_files:
  - {split: train, path: data/train.jsonl}
  - {split: test, path: data/test.jsonl}
---

# LGUplus Weekly Viewing Persona

일주일치 일일 페르소나 → 주간 장기 시청성향 카드. 3주치(기존 + 신규 2주).

- **train** = 기존주 + 신규 첫주 · **test** = 신규 다음주 · `week` 필드로 구분
- 입력 daily_personas(요일별) + main_genre/sub_genre(주별 시청 장르 카운트) → 카드 7필드(viewing_tendency/preferred_programs/frequent_channels/preferred_genres/weekday·weekend_viewing_times/key_keywords)
