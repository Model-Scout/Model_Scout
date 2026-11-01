---
license: cc-by-4.0
task_categories:
  - text-generation
language:
  - en
  - ko
tags:
  - reasoning
  - agent-traces
  - wcy
size_categories:
  - n<1K
---

# WCY reasoning traces

Line-oriented, phase-tagged agent reasoning traces in the WCY format.

## Splits

| config | file | traces | description |
|---|---|---|---|
| v1 | `wcy_traces_v1_clean.jsonl` | 528 | original WCY v1 corpus (pipeline-generated; the full 540-trace v1 set incl. 12 hand-crafted traces is at [10.5281/zenodo.19068769](https://doi.org/10.5281/zenodo.19068769) and [github.com/ycmath/wcy](https://github.com/ycmath/wcy)) |
| v2-semantized | `data_v2/wcy2_semantized_540.jsonl` | 317 | v1 traces re-encoded in WCY-2 semantics |
| v2-merge | `data_v2/wcy2_native_b1.jsonl` | 18 | merge-conflict resolution |
| v2-level | `data_v2/wcy2_native_b2.jsonl` | 9 | level refinement |
| v2-safe | `data_v2/wcy2_native_b3.jsonl` | 14 | safe-fragment query discipline |
| v2-schema | `data_v2/wcy2_native_b4.jsonl` | 21 | schema evolution |

## Quality gates

Every v2 trace passed nine mechanical gates — parse, merge laws, CON
discipline, void termination, resolve integrity, retraction form, rail sanity,
merge replay, provenance — and an LLM audit pass.

## Disclosure

**145 of 379 v2 traces (38%) carry
`corrected_from_v1: true`**: their domain content was altered relative to the
v1 source, not merely re-encoded, because the audit identified factual defects
(some inherited from the v1 source text, some introduced during re-encoding).
This corpus is **not** a faithful re-encoding of v1. Filter
on `corrected_from_v1` to exclude them. Per-row fields `source_id`,
`was_fixed`, `fix_tier`, and `audit_notes` give full provenance.

License: CC BY 4.0.
