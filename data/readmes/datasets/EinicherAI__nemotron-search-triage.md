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

# nemotron-search-triage

**Purpose**: the 10-row ground-truth-vs-actual-answer contradiction table
from the July 26 semantic triage of `nvidia/Nemotron-SFT-Agentic-v2`'s
`search` split -- documentation of why this split is **stopped for direct
trajectory use**, not a training corpus.

**Upstream**: [`nvidia/Nemotron-SFT-Agentic-v2`](https://huggingface.co/datasets/nvidia/Nemotron-SFT-Agentic-v2)
@ `49e79a3be5ab8cf7511a12958b95cfd6408cd8db`, split `search` (6,977 web-search trajectories total).

**License**: CC BY 4.0 (same dataset/pin as `nemotron-agentic-judgments`;
see `../../licenses.md` #4/6). Attribution to NVIDIA required.

**Citation**: NVIDIA Nemotron-SFT-Agentic-v2.

## Verification method (honest, one paragraph)

The July 26 first-10 pilot sampled the literal first ten `search` rows
(not random) and found every one satisfies
`metadata.ground_truth == metadata.final_answer_entity`. That equality is
**not outcome validation**: `final_answer_entity` is a copy of the
reference label baked into the metadata regardless of what the model
actually said. Comparing the reference label to *itself* trivially always
matches. The triage instead read each row's actual generated final
assistant text and compared it by hand to `ground_truth`:
2/10 exact matches, 1/10
plausible/partial, **7/10 clear contradictions**.
What was **not** checked: any row beyond this non-random first-10 sample
(6,967 further search trajectories remain unreviewed), and whether the
underlying *questions* (as opposed to the generated answers) are usable as
task seeds with an independently produced solution.

## Measured rates

- 10/10 rows sampled (first-10, non-random -- percentages here must not be
  projected onto the full 6,977-trajectory split).
- 2 exact match, 1 plausible/partial,
  7 contradiction -- i.e. **70% of the sample's
  generated final answers contradict their own reference label**, despite
  the metadata equality claiming 10/10 "correct."

## Sigi project provenance

July 26 semantic triage
(`docs/research/public-source-semantic-triage-20260726.md`) -> this
package. No further mission has re-sampled this split; disposition is
unchanged: stop direct trajectory use, treat questions + independently
verified ground truth as task seeds only.

## Known limitations

- n=10, first-10 (not random) -- this is a documented existence proof
  that the metadata-equality shortcut is unreliable, not a measured
  contradiction *rate* for the split. Do not quote "70%" as the split's
  overall error rate.
- No packaged row content beyond the 10-row table above (question text,
  full trajectories) -- this package is evidence-of-a-finding, not a
  dataset slice; there is nothing here to bulk-convert.
