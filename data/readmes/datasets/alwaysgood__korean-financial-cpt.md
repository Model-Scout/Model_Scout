---
license: other
language:
- ko
tags:
- finance
- korean
- cpt
- jsonl
size_categories:
- 100K<n<1M
task_categories:
- text-generation
pretty_name: Korean Financial CPT (Raw JSONL)
---

# Korean Financial CPT (Raw JSONL)

## Dataset Summary

- Last updated: 2026-04-09 01:03 UTC
- Data type: raw JSONL files (no instruction formatting)
- Length metric below: **character length** of `content` (fallback `contents`)
- Cleaning applied: rows with `char_len < 10` removed from raw files

## File Sizes

| File | Size | Rows | Valid Text Rows | Missing Text Rows |
|---|---:|---:|---:|---:|
| bok.jsonl | 846.20 KB | 652 | 652 | 0 |
| hk.jsonl | 92.34 MB | 30,254 | 30,254 | 0 |
| mk.jsonl | 19.39 MB | 6,856 | 6,856 | 0 |
| naver_dict.jsonl | 15.88 MB | 11,663 | 11,663 | 0 |
| naver_financial.jsonl | 149.69 MB | 79,462 | 79,462 | 0 |

## Character Length Distribution by Source

| Source File | min | mean | p50 | p95 | p99 | max |
|---|---:|---:|---:|---:|---:|---:|
| bok.jsonl | 26 | 506.39 | 498.0 | 844.9 | 1103.9 | 1,332 |
| hk.jsonl | 42 | 1197.34 | 985.0 | 2662.3 | 4710.4 | 16,101 |
| mk.jsonl | 301 | 1091.48 | 998.0 | 2122.0 | 2949.0 | 7,282 |
| naver_dict.jsonl | 15 | 487.53 | 405.0 | 1148.9 | 1483.0 | 2,799 |
| naver_financial.jsonl | 300 | 708.50 | 655.0 | 1277.0 | 1697.4 | 8,534 |

## Notes

- This repository currently stores raw source files only.
- Processed/packed training datasets are intentionally not included in this card.
