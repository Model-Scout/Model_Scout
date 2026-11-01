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

# nemotron-agentic-judgments

**Purpose**: full-prefix semantic judgments (not a bulk training corpus --
this source is SEEDS ONLY) over `nvidia/Nemotron-SFT-Agentic-v2`'s
`interactive_agent` and `tool_calling` splits, plus the row IDs of the
judged-GOOD rows, which are the only direct-render candidates from this
source. Useful as an evaluation/audit set for agentic tool-use failure
modes, and as a pointer set for the 26 rows worth carrying
forward.

**Upstream**: [`nvidia/Nemotron-SFT-Agentic-v2`](https://huggingface.co/datasets/nvidia/Nemotron-SFT-Agentic-v2)
@ `49e79a3be5ab8cf7511a12958b95cfd6408cd8db`, splits `interactive_agent` + `tool_calling` (`search` is a
separate release, `nemotron-search-triage`).

**License**: CC BY 4.0 (card-level; no per-row override found in this
dataset's schema). See `../../licenses.md` #4/6. Attribution to NVIDIA
required on redistribution.

**Citation**: NVIDIA Nemotron-SFT-Agentic-v2.

## Verification method (honest, one paragraph)

Mission 003 (Haiku) ran a 400-row (200/split) mechanical screen first and
found the release structurally perfect (400/400 pass) -- mechanical
cleanliness carried **no quality signal** for this source. Mission 004
(Sonnet) then did a full-prefix semantic review of 25 random accepted rows
per split (seed 42): the reviewer read the complete system policy, every
simulated-user turn, every tool call/result, and the final answer together
(full-prefix review, not just the last turn) and assigned GOOD/FIXABLE/BAD.
interactive_agent: 10/25 GOOD (40%, drop band, <50%).
tool_calling: 16/25 GOOD (64%, seeds-only band, 50-80%).
An owner-side hand recheck of 3 rows (2 BAD, 1 GOOD) confirmed all three
verdicts. What was **not** checked: rows outside the 25/split sample
(975 unreviewed rows/split remain unjudged), and reasoning-trace content
(kept separate, never trained, per Sigi policy) -- a judged-GOOD row's
reasoning was not itself audited.

## Measured rates

- Mechanical (mission 003): 400/400 rows passed across both splits (200/split).
- Semantic (mission 004, n=25/split): interactive_agent 10/25 GOOD,
  7/25 FIXABLE, 8/25 BAD.
  tool_calling 16/25 GOOD, 3/25 FIXABLE,
  6/25 BAD.
- Total judged: 50 rows. Total judged-GOOD (the only direct
  candidates): 26 (10 interactive_agent +
  16 tool_calling).

**Note on the mission brief's "100 full-prefix judgments":** the actual
mission 004 evidence is **50** judgments (25 rows x 2 splits),
not 100. This package ships the real 50, matching
`missions/004-out/*.judgments.jsonl` exactly, rather than the mission
text's figure -- flagged here rather than silently reconciled.

## Sigi project provenance

Mission 003 (mechanical) -> mission 004 (semantic, full-prefix) -> this
package. Verdict on file at
`data/foundation_v1/source_verdicts/nemotron-agentic-v2.md`.

## Known limitations

- SEEDS ONLY verdict: do not bulk-convert this source. Only the
  26 GOOD-judged rows in `good_row_ids.json` are direct-render
  candidates (source content itself is not shipped here, only the IDs and
  our judgments -- rehydrate via `datasets.load_dataset(streaming=True)`
  at the pin above; the HF `/rows` viewer 500s on this dataset, a known
  server-side CastError unrelated to the data).
  FIXABLE rows (10 across both splits) are bounded-repairable but were
  not repaired here.
- The dominant defects (confident fabrication, premature action, policy-
  violating escalation) are exactly Sigi's C10 anti-behaviors -- this
  source actively teaches them if bulk-converted, which is why it is
  capped at seeds/GOOD-only use.
