---
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

# smoltalk2-sigi-screened

**Purpose**: row-ID + verdict lists for the `HuggingFaceTB/smoltalk2`
strata screened for Sigi -- rewrite (C13/C14 volume), multilingual (fr/es
/it/pt/de language floors), and the strata found unsuitable
(everyday_conversations, smol_summarize, systemchats_30k, smol_magpie_ultra
provisional). **No raw row text is included** -- SmolTalk2 is huge
(millions of rows across dozens of streaming splits) and its
top-level/multilingual-stratum licensing is not fully confirmed (see
`../../licenses.md` #3); reconstruction from the pin is a single streaming
pass, so this package ships IDs + our own judgments + `reconstruct.py`
only.

**Upstream**: [`HuggingFaceTB/smoltalk2`](https://huggingface.co/datasets/HuggingFaceTB/smoltalk2)
@ `fc6cc2103c066455aade5d7fbb346039ae36ca5e`, config `SFT`.

**License**: see `../../licenses.md` #3 in full. Short version: no
top-level license tag on smoltalk2 itself; its own README says "new"
strata are Apache-2.0 and "existing public dataset" repackagings inherit
the original license. smol_rewrite traces cleanly to SmolTalk's own
Apache-2.0 "Smol-rewrite" dataset. multilingual_8languages' Apache-2.0
status is ambiguous (naming mismatch between the `no_think` split we use
and the license section's enumeration) -- flagged, not resolved.

**Citation**: HuggingFaceTB, SmolTalk2 (SmolLM3 post-training data mix).

## Verification method (honest, one paragraph)

Every stratum first passed a mechanical screen (missions 007/010, 100
rows/split: refusal-phrase regex, `<think>`-leak check). Six strata then
got a 6-row semantic sample (mission 014, Sonnet). smol_rewrite and
multilingual_8languages cleared their 6-row band and got a follow-up
30-row confirm each (missions 016, 017): smol_rewrite 30/30 GOOD;
multilingual_8languages 26/30 GOOD (per-language breakdown in
`strata/multilingual_8languages/judgments_017_confirm30.jsonl` -- es is the
weakest language, it/de are clean). smol_rewrite's converted population
was later extended (mission 026) with a second batch of 4000
more rows, gated on its own 200-row 5% spot check (mission 028, two
workers): 185/200 = 92.5% GOOD, clearing the
80% un-quarantine threshold. What was **not** checked: everyday_
conversations, smol_magpie_ultra, and smol_summarize never got a 30-row
confirm (6-row samples only, all below or at the seeds-only band);
systemchats_30k never got any semantic review at all (dropped outright on
its 21/100 mechanical refusal rate, which itself violates Sigi's
no-volitional-refusal constraint).

## Strata in this package

| Stratum | Population shipped | Judgment files | Verdict |
|---|---|---:|---|
| smol_rewrite | 5000 ids (batch1 1000 + batch2 4000) | 014 (6) + 016 (30) + 028 (200) | **BULK-ACCEPT, confirmed** (batch1 30/30 + batch2 92.5%) |
| multilingual_8languages | 750 ids (fr/es/pt/it/de, 150 each) | 014 (6) + 017 (30) | **BULK-ACCEPT, confirmed** (26/30, es weakest) |
| smol_magpie_ultra | none converted | 014 (6) | provisional/seeds -- needs its own 30-row confirm before bulk use |
| everyday_conversations | none converted | 014 (6) | seeds only -- fabricates real-time facts unhedged (anti-C10) |
| smol_summarize | none converted | 014 (6) | **DROP** -- systemic self-violation of its own summarize template |
| systemchats_30k | none | mechanical summary only | **DROP** -- 21/100 refusal-shaped, no-volitional-refusal violation |

## Sigi project provenance

Missions 007/010 (mechanical) -> 014 (6-row semantic) -> 016/017 (30-row
confirms) -> 026 (batch2 extension) -> 028 (batch2 spot check) -> this
package. Verdict on file at
`data/foundation_v1/source_verdicts/smoltalk2.md`.

## Known limitations

- No raw content in this package at all -- every downstream user must
  rehydrate via `reconstruct.py` and the pin before doing anything with
  these rows.
- multilingual_8languages' Spanish rows are the weakest in the confirmed
  sample (4/6 GOOD in mission 017); one BAD there was a verified
  code-shadowing bug, not noise.
- smol_rewrite's batch2 spot check (200/4000 = 5%) found 15
  FIXABLE rows, all the same failure mode (a "friendlier tone" rewrite
  that also dropped or inverted a concrete stake/deadline/accusation
  instead of only softening delivery) -- worth a mechanical filter pass
  before training on the full batch2 population, not just accepting all
  4000 rows uncritically.
