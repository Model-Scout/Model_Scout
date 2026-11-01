# XI-V Bench 1.0

System One decision benchmark: en/ko/zh/ja x 3 tiers

XI-V Bench 1.0 — a multilingual decision benchmark for System One models. 3 tiers (easy/standard/hard) x 4 languages (en/ko/zh/ja) x 32 items = 384 items, with 96 cross-language groups.

- Includes the item schema, validator, runner and scorer (schema.json, validate_items.py, datasets/manifest.json)
- Question contract: for the noul type, labels are ["no","yes"] (adapter probability keys) while question.criteria keys must be exactly true/false (the option texts the model reads)
- Items require a correct label plus confidence, so evaluation covers accuracy, ECE, Brier and language-consistency (LCS)
- License: MIT (the 96 English base items are excerpted and adapted from JevBench v1.3 public, MIT; ko/zh/ja items are localized)
- Baseline: XERON-1.0 overall 0.5495 (easy 0.8203 / standard 0.5234 / hard 0.3047), ECE 0.0848, see results/xeron-1.0.summary.json
- GitHub: https://github.com/PIXELZX0/XI-V-Bench

출처: Kaggle (pistonx/xi-v-bench-1-0)
태그: chinese, japanese, korean, multilingual, benchmark
라이선스: Other (specified in description)
수정일: 2026-09-26T10:22:35.483Z
