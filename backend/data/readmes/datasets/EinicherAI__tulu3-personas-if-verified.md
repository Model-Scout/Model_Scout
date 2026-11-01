---
license: odc-by
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

# tulu3-personas-if-verified

**Purpose**: a deterministically constraint-verified subset of
`allenai/tulu-3-sft-personas-instruction-following`, for small-model SFT on
precise instruction-following (English, C13/C14 in the Sigi capability
matrix).

**Upstream**: [`allenai/tulu-3-sft-personas-instruction-following`](https://huggingface.co/datasets/allenai/tulu-3-sft-personas-instruction-following)
@ `fe0c7d350c9b4542b8d829a6f1daa1c259f0ba0e`, split `train` (29980 rows).

**License**: ODC-BY 1.0 (Open Data Commons Attribution). Attribution
notice: this package redistributes rows derived from the Allen Institute
for AI's tulu-3-sft-personas-instruction-following dataset, licensed under
ODC-BY 1.0 (https://opendatacommons.org/licenses/by/1-0/). No
redistribution restriction found; see `../../licenses.md` #2.

**Citation**: Allen Institute for AI, Tulu 3 SFT Personas Instruction
Following dataset.

## Verification method (honest, one paragraph)

Verification is fully deterministic, not LLM-judged: mission 013 built a
type-keyed checker registry (`checkers.json`, 23 of the
25 observed constraint types have an implemented checker; 2 types --
`use quotation` and `length constraints:first word of the nth paragraph`
-- have none and are always UNCHECKED) that maps each row's declared
`constraints` (IFEval-style) to a parameter extractor over the prompt text
and a pass/fail checker over the assistant response, with an assert that
makes a type/checker mismatch structurally impossible (mission 011's
original 42% figure was invalid because of exactly that mismatch bug; 013
replaced it). Mission 018 ran this over the full 29980-row
stream: 8456 rows had every declared
constraint checkable and passing (**VERIFIED_PASS**),
12364 had all *checkable* constraints pass but
at least one constraint that could not be checked (missing checker or
failed parameter extraction) (**PARTIAL**), 4403
had a checked constraint fail (excluded), 4757
had nothing checkable at all (excluded). What was **not** checked: the
`use quotation` and nth-paragraph-first-word constraint types (no checker
exists, documented rather than guessed), and roughly a third of instances
where parameter extraction from free-text prompts failed (see
`checkers.json` / `018-full-filter-summary.json` `unchecked_reasons` for
the exact breakdown) -- these degrade a row from VERIFIED_PASS to PARTIAL,
never silently pass it.

## Splits in this package

- `verified_pass.jsonl` -- 8456 rows, status
  `VERIFIED_PASS`, source schema (`id`, `row_index`, `prompt`, `messages`,
  `constraints`) plus `checked_constraints` (list of
  `{type, checker, passed}`) and an empty `unchecked_types`.
- `partial.jsonl` -- 12364 rows, status `PARTIAL`, same schema,
  with a non-empty `unchecked_types` naming exactly which of the row's
  declared constraints could not be checked (the checked ones all passed).

## Measured rates

- Full-run classification (29980 rows, mission 018):
  VERIFIED_PASS 8456, PARTIAL
  12364, FAIL 4403,
  UNCHECKED 4757.
- Instance-level: 36994/59803
  constraint instances checkable (61.9%);
  of those, 72.8% passed.
- This package's rehydration matched 20820 of
  20820 rows named in `missions/018-out/accepted.jsonl`.

## Sigi project provenance

Mission 011 (invalid, checker-mismatch bug) -> mission 013 (redo, 300-row
validation of the registry) -> mission 018 (full 29,980-row run) -> this
package (rehydrates full rows from the pin + attaches the per-row
checked/unchecked detail that 018's output alone didn't carry). Verdict on
file at `data/foundation_v1/source_verdicts/tulu3-personas-if.md`.

## Known limitations

- A 5% human/LLM spot-check sample of the batch-2 conversion slice was
  drawn (`missions/026-out-tulu-spotcheck.jsonl`, 347 ids) but **has not
  been reviewed yet** -- acceptance here rests entirely on the
  deterministic checkers, not on any semantic read of response quality
  beyond what the checkers measure (e.g. a response can satisfy every
  constraint and still be a poor answer to the underlying prompt; that
  axis is not scored anywhere in this pipeline).
- PARTIAL rows are not verified on their unchecked constraint(s) at all --
  they are exactly as reliable as VERIFIED_PASS on the *checked* subset of
  their constraints, and unknown on the rest. Treat status as a filter
  floor, not a quality ceiling.
- English-only; does not contribute to Sigi's non-English language floors.
