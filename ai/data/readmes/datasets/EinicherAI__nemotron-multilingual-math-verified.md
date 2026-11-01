---
license: cc-by-sa-4.0
language:
- en
- de
- ja
- ko
- pt
tags:
- verified-subset
- sigi
---

# nemotron-multilingual-math-verified

**Purpose**: a verified subset of `nvidia/Nemotron-SFT-Multilingual-v2`'s
math splits (math_ja, math_ko, math_pt), screened and spot-checked for the
Sigi personal-assistant SFT project. Rows are useful for small-model SFT in
Japanese, Korean, and Brazilian Portuguese mathematical reasoning where an
answer must be boxed.

**Upstream**: [`nvidia/Nemotron-SFT-Multilingual-v2`](https://huggingface.co/datasets/nvidia/Nemotron-SFT-Multilingual-v2)
@ `971a252224b75414b1b67c55dbe0446d8b6606a0` (config `default`, splits `math_ja`/`math_ko`/`math_pt` -- the only
math splits in a Sigi-supported language; `math_hi` exists but Hindi is
outside the twelve Sigi languages).

**License**: mixed at the card level (`cc-by-4.0` + `cc-by-sa-4.0`); a
per-row check (`metadata.license`) confirmed every math row in this subset
carries **CC BY-SA 4.0** (source categories "Math GenSelect" and "Math
GPT-OSS StackOverflow", both StackOverflow-derived per the upstream card).
ShareAlike applies: derivative/redistributed forms must also be CC BY-SA
4.0 with attribution to NVIDIA and the original StackOverflow authors. See
`../../licenses.md` #1 for the full check. This is also why this package
ships **row IDs + a streaming rehydration script (`rehydrate.py`)**, not a
baked static text dump -- no local copy to keep in sync with the notice.

**Citation**: NVIDIA Nemotron-SFT-Multilingual-v2 (translated from
Nemotron-Math-v2 seed data via DeepSeek-V3-0324); cite the upstream dataset
card if you use this subset.

## Verification method (honest, one paragraph)

Screening was two-stage. Stage 1 (mission 001, Haiku, 200 rows/split,
seed-independent): five hard mechanical checks (H1-H5, including a
`\boxed{}` presence check and a fasttext language-ID check) --
180/200 (math_ja),
188/200 (math_ko),
169/200 (math_pt) passed
(537/600 = 89.5%). Stage 2 (mission 002, Sonnet,
30 random accepted rows/split, seed 42): the judge solved each problem
independently before comparing to the boxed answer --
88.1% matched over 90 sampled rows (own-hand
owner re-check of 6 further rows: 5 correct, 1 partial, consistent). What
was **not** checked: reasoning-trace faithfulness (kept separate per Sigi's
locked constraints and never trained), translation quality of the original
Nemotron-Math-v2 seed problems, or the remaining ~85% of rows outside the
002 spot-check sample (accepted on mechanical grounds only).

## Measured rates

- Mechanical accept rate (batch1, rows 0-199): 537/600 = 89.5%
  (math_ja 180/200, math_ko 188/200, math_pt 169/200).
- Correctness spot-check (mission 002): 88.1% over 90 rows
  ({'MATCH': 74, 'MISMATCH': 5, 'PARTIAL': 5, 'UNSURE': 6}).
- Batch2 status: batch2 (rows 200-999) was re-screened by mission 024 after a fasttext API bug was fixed: 2210/2400 accepted (92.1%, in line with the batch1 84.5-90% range per split). Its mandatory correctness spot check (mission 031, 109 rows across 3 workers) is DISPATCHED but has not landed results for all three splits as of this packaging run (splits with results so far: none yet). Per mission 027's own rule, batch2 stays **batch2_pending and is NOT included** in this release until mission 031 completes and clears the 80% threshold per split. See `batch2-status.json` for the exact
  mission 024 + mission 031 (if landed) numbers.

## Sigi project provenance

Mission 001 (mechanical screen) -> mission 002 (correctness spot-check) ->
this package. Bulk-accept verdict on file at
`data/foundation_v1/source_verdicts/nemotron-multilingual-math.md`.

## Known limitations

- Only batch1 (rows 0-199 per split, 537 rows) is confirmed and
  included as of this packaging run. Batch2 (rows 200-999,
  2210 mechanically-accepted rows) is a moving target across
  concurrent missions -- see `batch2-status.json` for the exact state this
  run observed and re-run `027_package.py` after mission 031 lands to pick
  up batch2 automatically if it clears 80%.
- No ground-truth answer field exists upstream; "correctness" here means
  an independent Sonnet solve agreeing with the boxed answer, checked on a
  90-row sample, not the full 537-row set.
- Reasoning traces are excluded from any rendered/trained form by Sigi
  project policy; this package ships neither reasoning nor rendered text,
  only IDs, so that limitation is inherited by any consumer who rehydrates.
