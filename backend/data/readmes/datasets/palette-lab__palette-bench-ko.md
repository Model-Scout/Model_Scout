---
pretty_name: PALETTE-BENCH-KO
license: cc-by-4.0
language:
- ko
task_categories:
- text-generation
- question-answering
tags:
- korean
- benchmark
- enterprise
- business-documents
- evaluation
- llm-judge
size_categories:
- n<1K
configs:
- config_name: default
  data_files:
  - split: test
    path: data/*
---

# PALETTE-BENCH-KO — Korean Enterprise Document Benchmark

**Version:** 0.1 (seed) · **License:** CC BY 4.0 · **Language:** Korean (ko)

## What this is

The first public benchmark for **Korean enterprise document work** — the drafting,
extraction, and compliance tasks that office staff actually do, which existing Korean
benchmarks (KMMLU, HAE-RAE, KoBALT, LogicKor) do not cover. A landscape sweep (2026-08)
found no public benchmark testing 공문서/품의서 drafting, 회의록→결정 extraction, or
business-register control; the nearest neighbors test QA/RAG (Allganize) or law (KCL),
not workflow. Demand is documented: Seoul Metropolitan Government's own survey put
document drafting (23%) + summarization (20%) as civil servants' top AI needs.

## Task families (6)

| Family | Task | Scoring | Deterministic? |
|---|---|---|---|
| `minutes_to_decision` | 회의록 → {decision, owner, due_date} 구조화 추출 | field F1 | ✅ yes |
| `dart_comprehension` | 공시 발췌 → 사실 QA + 수치 추론 | token-F1 / exact | ✅ yes |
| `gongmun_drafting` | 브리프 → 공문서 초안 | rubric (LLM judge) | ⚪ judge |
| `pumui_drafting` | 시나리오 → 품의서/기안 | rubric (LLM judge) | ⚪ judge |
| `email_register` | 관계·의도 → 비즈니스 이메일 (존댓말 register) | rubric (LLM judge) | ⚪ judge |
| `policy_compliance` | 작업 + 조직 정책 → 준수/거부/플래그 판단 | compliance rubric | ⚪ judge |

## Size

**v0.1 seed: 24 items** (4 per family; 6 easy / 12 medium / 6 hard). This is a
**reference seed**, released to establish the format, scoring, and the axis. The
production release (v1.0) expands to ~1.5–3k items with native-expert authoring and a
rotated held-out split — see [README.md](README.md) → roadmap.

## Provenance & honesty

- All items are **synthetic** (authored for this benchmark) or **DART-style** (modeled on
  the public disclosure register, not copied from a specific filing). No customer data, no
  scraped copyrighted documents. This keeps the set redistributable under CC BY 4.0.
- The `policy_compliance` family includes the exact PIPA-scoped data-handling dilemma a
  governance product must get right (item `pc-003`), and the drafting families include
  the residency-justification and sensitive-incident cases (`pm-002`, `pm-003`, `gm-003`).
- The harness **never fabricates a score**: rubric items with no judge configured are
  reported `UNSCORED`, not given a number. Deterministic families need no LLM.

## Fields per item

`id` · `family` · `task_class` · `difficulty` · `provenance` · `input` (Korean) ·
`reference` **or** `reference_rubric` · `scoring` · optional `notes` / `max_score`.

## How to evaluate

```bash
# 1. run your model on each item's `input`, collect {id: output} → preds.json
# 2. score:
cd harness
python evaluate.py --data ../data --preds preds.json --judge none        # deterministic only
python evaluate.py --data ../data --preds preds.json --judge anthropic   # full (needs key)
```

Deterministic families (`minutes_to_decision`, `dart_comprehension`) score with stdlib
only. Rubric families use a pluggable LLM judge (OpenAI / Anthropic adapters included).

## Intended use & limitations

- **Use**: measuring Korean enterprise-document capability of LLMs; a held-out slice for
  adapter evaluation; a citable axis for a model release.
- **Limitations (v0.1)**: 24 items is a seed, not a statistically powerful test set;
  rubric scoring inherits judge-model bias (report the judge used); Korean items are
  authored by the release team and await native-expert review for v1.0. Do **not** report
  v0.1 numbers as a definitive leaderboard — report them as a seed baseline.

## Citation

> PALETTE-BENCH-KO: A Korean Enterprise Document Benchmark (v0.1 seed), 2026.
> Released under CC BY 4.0.
