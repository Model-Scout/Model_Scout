---
license: cc-by-4.0
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

# nemotron-terminal-replay-evidence

**Purpose**: Docker replay verdicts (with independently-derived evidence,
not the source's own self-reported `task_complete` flag) over
`nvidia/Nemotron-Terminal-Corpus`'s skill_based configs, for small-model
SFT on CLI/terminal-agent behavior. Only VERIFIED trajectories are usable
as direct SFT material; the rest are documented failure/gap evidence.

**Upstream**: [`nvidia/Nemotron-Terminal-Corpus`](https://huggingface.co/datasets/nvidia/Nemotron-Terminal-Corpus)
@ `a1667c4ffdadea02a89bffe4f1bb7ca2ff19f8d9`, configs `skill_based_easy`, `skill_based_medium`,
`skill_based_mixed` (`dataset_adapters` and raw direct use were already
stopped per the July 26 triage).

**License**: CC BY 4.0 (card-level; no per-row override found). See
`../../licenses.md` #5. Attribution to NVIDIA required on redistribution.

**Citation**: NVIDIA Nemotron-Terminal-Corpus ("On Data Engineering for
Scaling LLM Terminal Capabilities").

## Verification method (honest, one paragraph)

Mission 005 (Haiku) streamed 100 rows/config and sampled 10 unique tasks/
config (seed 42) into replay bundles; only 40% of trajectories even
self-declare `task_complete: true`, already a weak signal. Mission 006
(Sonnet) replayed each of the 30 sampled tasks in a fresh
`--network none` `python:3.12-slim` Docker container per task: a
trajectory is **VERIFIED** only if its input files were fully revealed in
the terminal output (a complete `cat`, not a `head`/`tail` excerpt) *and*
an independently-written verification script (not the trajectory's own
checker code) recomputed the expected output from the reconstructed input
and matched exactly. Verdicts: **12/30 VERIFIED**,
5/30 FAILED (real, reproduced bugs -- e.g.
naive/aware datetime comparison crashes), 13/30
NOT_RECOVERABLE (the input was never fully shown, not a quality failure).
What was **not** checked: any task outside the 30-task sample (the corpus
has ~140k skill-based tasks total), and the `dataset_adapters` config
(~226k samples, out of scope for this mission).

## Recoverability rule

A trajectory can only be replayed and verified if **every** input file it
depends on was fully dumped somewhere in its own terminal output (full
`cat`/`cat -n`, not `head -N`/`tail -N`/a handful of sample lines) --
because the corpus ships **no separate initial-environment snapshot**.
Partial reveals (even a 43-line gap in an otherwise-shown file) make the
row NOT_RECOVERABLE by rule, regardless of how sensible the trajectory's
commands look. This is a corpus/logging gap, not a trajectory-quality
signal, and should not be read as evidence against the underlying model
behavior in those rows.

## The `task_complete` finding

`task_complete: true` is **not evidence of correctness**. Per the
July 26 pilot, only 19/40 first-10 rows self-declared complete and that
did not correlate with actual test-passing; mission 006 confirms this
directly -- e.g. `skill_based_mixed` task 0292's own trailing turns
notice a missing tool call and run out of turns before finishing, and
several NOT_RECOVERABLE/FAILED bundles look like session truncation by the
collection harness rather than the model giving up. Never train on
`task_complete` as a label.

## Measured rates (per config)

| Config | VERIFIED | FAILED | NOT_RECOVERABLE |
|---|---:|---:|---:|
| skill_based_easy | 8 | 0 | 2 |
| skill_based_medium | 1 | 0 | 9 |
| skill_based_mixed | 3 | 5 | 2 |
| **Total (30)** | **12** | **5** | **13** |

## Sigi project provenance

Mission 005 (prep/bundling) -> mission 006 (Docker replay + independent
verification) -> this package. Verdict on file at
`data/foundation_v1/source_verdicts/nemotron-terminal-corpus.md`.

## Known limitations

- Only 12 of 30 sampled tasks are usable direct SFT
  material; `skill_based_medium` in particular is almost entirely
  NOT_RECOVERABLE (9/10) --
  do not read that as "medium tasks are worse," it means inputs were less
  often fully revealed for that config.
- `skill_based_mixed`'s 5 FAILED rows carry real, reproduced bugs (crashed
  scripts, wrong aggregate values) -- these are negative examples, not
  neutral seed stock, if ever used for training signal.
- Evidence lines quote terminal output and reconstructed file contents in
  `judgments/*.judgments.jsonl` (`evidence` field) -- this is our own
  replay record, not a raw dump of the source's proprietary harness JSON.
