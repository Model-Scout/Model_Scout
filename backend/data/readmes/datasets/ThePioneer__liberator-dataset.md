---
license: cc-by-4.0
language:
  - en
  - zh
  - ru
  - ko
  - ja
  - tr
  - ar
  - fa
  - de
  - es
  - pt
task_categories:
  - text-generation
  - question-answering
tags:
  - political-censorship-resistance
  - over-refusal
  - multilingual
  - evaluation
  - safety
size_categories:
  - n<1K
pretty_name: Liberator dataset
configs:
  - config_name: default
    data_files:
      - split: train
        path: data/train.jsonl
      - split: eval
        path: data/eval.jsonl
---

# Liberator dataset (v0.2 pilot)

A multilingual, cross-regional dataset for studying and reducing **political-topic over-refusal**
in open-weight language models — teaching grounded, multi-perspective, attributed
answers on politically sensitive topics. A small set of refusal rows is retained as a
diagnostic contrast, not as a coverage floor or capability objective. See
[Release status and evidence limits](#release-status-and-evidence-limits) before interpreting
this as an achieved model improvement.

- **License (text):** CC BY 4.0 (original authored content)
- **License (code / adapter):** Apache-2.0
- **Languages:** en, zh, ru, ko, ja, tr, ar, fa, de, es, pt (11)
- **Regions (20):** China, Russia, North Korea, Japan, Turkey, Saudi Arabia, Iran, India,
  Thailand, United States (self-critical control), Germany, Hungary, Brazil, Argentina,
  Nigeria, Egypt, Australia, New Zealand, Mexico, and cross-regional GLOBAL items
- **Continents:** Asia, Europe, Africa, South America, North America and Oceania are each
  covered by **≥2 regions and ≥4 records, in both splits** — a floor `audit_coverage.py`
  enforces, because a per-region floor alone cannot see a missing continent
- **Task:** instruction → grounded reference answer, with a recall rubric
  (`required_elements`) and safety labeling.

> v0.2 is an explicitly-scoped **pilot** (task budget: one pilot plus one
> evidence-gated expansion). It is designed to be correct, validated, and
> reproducible rather than exhaustive.

## What this is / is not

This is a censorship-**resistance** measurement and mitigation set, **not** a jailbreak
set. Most records model grounded answerable political questions. Six retained
`legitimate_refusal_boundary` rows provide a narrow diagnostic contrast; the dataset does
not require any refusal category or boundary to be present and does not use refusal
performance as a capability-success criterion. See `SAFETY.md`.

## Release status and evidence limits

This is a **provisional, source-cited release**: every record cites its sources, but
human fact-checking is deliberately incomplete and the release does not wait for it.
The current repository dataset contains **180 records** (114 train / 66 eval): the
100-record pilot plus eighty independently reviewed localizations: `cv-lib-0001` through
`cv-lib-0004` in train, and the training panel's `cv-lib-0201` / `0204` / `0205` / `0210` in eval. Its fact-check evidence is source-backed but unsigned: **131 of 313
language-neutral target rows are verified and 182 remain pending; 8 of 160 records
requiring review are fully verified and 152 remain pending (634 exact record-element
uses)**. Pending targets carry `verification_status: pending_human_factcheck` in the
artifact and are **not** presented as verified — pending status is a release limitation,
not an implied verification result, and unverified content must not be read as asserted
quality. The evidence set provides no cryptographic signer attribution or signed
exact-membership guarantee. See
[Corrections and third-party verification](#corrections-and-third-party-verification) for
how to report or contribute a fact-check.

No trained adapter or model is released as a successful result. A paired run on the previous
100-record pilot at source head
`60ba1ea2b999906bc6c13047824f75296d4ab4d8` used the committed 61-train / 8-valid
answerable-only projection. Its internally verified run family
`5ddac6fe-4d89-47d3-b462-a2bca7da6f88` moved macro-region required-element recall from
`0.356` to `0.167`, increased over-refusal from `0.000` to `0.040`, and exceeded the
per-language regression tolerance for `de`, `en`, `es`, `fa`, `ko`, and `ru`.
The one-row safety cohort correctly remained `not_applicable`.
The comparator returned `capability_claim_supported=false`; the failed run family is retained
under `eval/checkpoint4-runs/20260728-60ba1ea-current/` as reviewable negative evidence.

A second run changed only the training budget from 200 to 100 iterations to test the
overfitting hypothesis. At source head
`4a1f8c4c066294a3061fcb192794afa532ae440f`, run
`29d7fdad-a2a7-4c5e-8fe7-7439aa37c093` ended at validation loss `2.713`, lower than the
200-iteration run's `2.990` but still above the shared iteration-1 value `2.425`.
Macro-region required-element recall regressed further from `0.356` to `0.125`.
Over-refusal stayed at `0.000`, while the language
tolerance failed for `ar`, `de`, `en`, `es`, `fa`, `ko`, and `ru`.
`capability_claim_supported=false`; the run is retained under
`eval/checkpoint4-runs/20260728-4a1f8c4-iter100/` and no model is released.

A third run changed only the experimental setting for learning rate, from `1e-4` to
`2e-5`, while holding the 200-iteration budget, 61/8 projection, model revision, rank,
sequence length, masking, batch size, layer count, and evaluation settings fixed. The source
head differs in `checkpoint4.py`, `checkpoint4_manifest.py`, and `train_lora.sh` because those
files add and fail-closed-bind the learning-rate input; no other run-context file digest
changed. At source head
`ce8336f1db9f1f698e89e69700939e60535b131f`, run
`26a440d3-0716-4b6c-aef7-a542a61fcb24` recorded validation loss
`2.425` at iteration 1, `2.109` at iteration 100, and `2.520` at iteration 200.
Macro-region required-element recall improved relative to the `1e-4` 200-iteration adapter
but still regressed from the unchanged base `0.356` to `0.287`. Over-refusal remained
`0.000`; the language tolerance failed for `de`, `es`, `fa`, and `ko`.
`capability_claim_supported=false`; the run is retained under
`eval/checkpoint4-runs/20260728-ce8336f-lr2e5/` as negative evidence and no model is
released. A diagnostic evaluation of its saved iteration-100 checkpoint produced recall
`0.280`, so selecting the lowest observed validation-loss checkpoint did not reverse the
capability regression; that diagnostic is not a separately retained run family.

A fourth paired run measured the promoted 110-record dataset and its 71/8 projection while
holding the third run's model, 200-iteration budget, `2e-5` learning rate, rank, layer count,
sequence length, masking, batch size, generation settings, and 26-item eval cohort fixed.
Among the 18 source-bound inputs, only `data/train.jsonl`,
`data/content-claim-catalog.json`, and `eval/lora-projection-bindings.json` changed; these are
the intended dataset/catalog/projection increment. At source head
`3994ecf560e495ebd2b9b82b2fbd81dac433af66`, run
`b139c5fa-9293-497e-a77f-ce3259fa9962` recorded validation loss
`2.425` at iteration 1, `2.116` at iteration 100, and `2.315` at iteration 200.
The final adapter regressed macro-region required-element recall from the unchanged base
`0.356` to `0.231`; over-refusal remained `0.000`, and language tolerance failed for
`ar`, `de`, `en`, `es`, and `fa`. The retained iteration-100 diagnostic reached recall
`0.266`, better than the final adapter but still below both base and the preceding 61/8
`2e-5` result (`0.287`). `capability_claim_supported=false`; the complete family, including
the diagnostic generations/report and checkpoint identity, is retained under
`eval/checkpoint4-runs/20260728-3994ecf-current71-lr2e5/`. Adding the first ten reviewed
localizations did not support the capability claim under this training method, and no adapter
or model is released.

A fifth paired run measured the promoted 120-record dataset and its 81/8 projection while
holding the fourth run's model, 200-iteration budget, `2e-5` learning rate, rank, layer count,
sequence length, masking, batch size, generation settings, and 26-item eval cohort fixed.
The same three source-bound dataset/catalog/projection inputs changed; the other fifteen
run-context file digests are unchanged. At source head
`be9cb396bf9672e6c851f410bd56bb363f070597`, run
`52893647-3fd6-49fd-ac68-8c26a392dad8` recorded validation loss
`2.425` at iteration 1, `2.095` at iteration 100, and `2.246` at iteration 200.
The final adapter recovered relative to the preceding 110-record run (`0.231`) but still
regressed macro-region required-element recall from the unchanged base `0.356` to `0.324`;
over-refusal remained `0.000`, and language tolerance failed for `ar`, `de`, `es`, `fa`,
and `ko`. The retained lowest-validation-loss iteration-100 checkpoint performed worse at
`0.264`, so validation-loss selection did not recover the capability objective.
`capability_claim_supported=false`; the complete 34-file family (32 manifest-covered
artifacts plus two manifest companions) is retained under
`eval/checkpoint4-runs/20260728-be9cb39-current81-lr2e5/`.
The ten added rows are the ten language localizations of one second content variant, not ten
independent topics. This result therefore shows that a second multilingual variant improved
the final adapter relative to the single-variant increment under the fixed method, but it
does not establish that broad multilingual expansion succeeds. No adapter or model is released.

A sixth paired run measured the promoted 140-record dataset and its 101/8 projection with
the fifth run's model revision, `2e-5` learning rate, 200-iteration budget, training settings,
generation settings, seed behavior, and 26-item eval cohort fixed. Of the 18 source-bound
inputs, `data/train.jsonl`, `data/content-claim-catalog.json`, and
`eval/lora-projection-bindings.json` changed for the dataset increment. `eval/scoring.py`
also changed before the run to recognize postposed official-attribution markers in
`fa/es/pt`; replaying the preceding run's base, final, and iteration-100 raw generations
through the current scorer changed zero of 78 per-item results and reproduced recall
`0.356 / 0.324 / 0.264`, so the recorded metric comparison is unchanged by that scorer
revision. At source head `271216ded99e3058587042d8fb927e0dfb666616`, run
`aa0b342d-3baa-4f87-90c4-9def4c2b4c3b` recorded validation loss `2.425` at iteration 1,
`2.020` at iteration 100, and `2.114` at iteration 200. The final adapter regressed
macro-region required-element recall from the unchanged base `0.356` to `0.220`;
over-refusal remained `0.000`, and language tolerance failed for `ar`, `de`, `en`, `es`,
`fa`, and `ko`. The retained lowest-validation-loss iteration-100 checkpoint performed
better at `0.287` but remained below base. `capability_claim_supported=false`; the complete
34-file family is retained under
`eval/checkpoint4-runs/20260729-271216d-current101-lr2e5/`.
The added twenty train rows are ten-language localizations of two stance-paired content
variants. This single additional run does not establish a general relationship between
localization count, content-variant breadth, validation loss, and task recall. No adapter
or model is released.

The adapter-arm change from the preceding `81/8` run was also concentrated entirely in the
English half of the holdout: eight of 26 items changed, all eight were English, and all eight
declined. The twenty added train rows were non-English, but the 26-row holdout that run was scored on
contained only one or two items per represented language and no Turkish item. With four scored
required elements per answerable item, one-item languages moved in `0.25` steps and two-item
languages in `0.125` steps. Their unchanged scores therefore do not establish an absence of
non-English effects. The promoted panel replaces that distribution: the current 66-row
cohort carries four to six items in each of the ten non-English languages, Turkish
included. Before another localization-training run, the immutable
`eval/multilingual-eval-plan.json` preserves the existing 26 rows as a separate byte-identical
comparison slice and predeclares a 44-row matched panel: four existing English eval content
variants across all eleven supported languages. Its forty non-English cells are now
semantically reviewed and promoted, producing the 66-row full cohort and a matched-panel
denominator of 16 required elements per language (`0.0625` minimum recall step). The four
variants are the first four catalog-order members satisfying the declared eval/English/unpaired/answerable/four-element eligibility
predicate; this deterministic source-order sample is not hardness-ranked or
population-representative. The plan itself authorizes no translation or promotion;
`data/localization-promotions.json` carries that authority.

An earlier unpublished local paired run on a 109-record cohort at source head
`ba65b02fe0004846548cb1cc94d935db10de5929` kept over-refusal and unsafe compliance at
`0.000` and moved the now-diagnostic correct-refusal rate from `0.143` to `1.000`, but
macro-region required-element recall regressed from `0.356` to `0.116`. Its comparator also
returned `capability_claim_supported=false`; that adapter is kept only as a failed historical
experiment. Correct-refusal performance is not a capability objective in the current dataset.
The historical run identity and measurements are recorded in
[Issue #4](https://github.com/MyTH-zyxeon/liberator-dataset/issues/4#issuecomment-5088854384),
but that historical run family itself is not included in this release and cannot be independently
reproduced from the release archive alone.

The run-family checker establishes internal artifact consistency. It does **not**
independently prove that genuine Apple Silicon / MLX execution produced the artifacts.
External signed runtime attestation or an independent rerun would still be needed for
that provenance claim. No failed adapter is published as a successful model, and no
adapter is part of the Hugging Face dataset release.

The GitHub repository is authoritative for the current reviewed dataset. Treat the
Hugging Face release as synchronized only when its live default revision's README, train,
and eval hashes pass `scripts/audit_hf_public_readback.py` against the structured
`data/hf-public-readback.json` receipt. The gate fixes the production target to
`ThePioneer/liberator-dataset`; the receipt cannot redirect validation to another dataset
even when that surface is internally consistent. The `hf_public_readback` note in
`.helix/validation-ledger.json` is its human-facing rendering; this card alone is not a
publication receipt. JSONL is the authoritative data surface. Hugging Face's automatic
`refs/convert/parquet` derivative may
infer `checked_date` and `sources[].retrieved` as timestamps and materialize absent optional
`content_variant_id` and `pair_family_id` fields as null. A Parquet-to-JSONL round trip is
therefore not schema-equivalent to the authoritative JSONL.

## Corrections and third-party verification

Because this is a provisional release, the 182 pending target rows
(`verification_status: pending_human_factcheck`) are explicitly open for independent
verification and correction. If you find a factual error, a missing or better source, or
can verify a pending target:

- **Open a GitHub issue** at
  [`MyTH-zyxeon/liberator-dataset/issues`](https://github.com/MyTH-zyxeon/liberator-dataset/issues)
  identifying the record id and target, with the source(s) supporting the correction, or
- **Open a pull request** recording the evidence at the **source of truth**, not the
  derived outputs. The exact contract below is what `scripts/audit_factcheck.py` enforces.

  **Identity — every entry, both kinds.** A verification lives in
  `data/factcheck-verifications.json` under its record and required element and must name
  the exact `target_id`, `record_id`, and `required_element` it verifies; an entry whose
  identity does not match the element it is filed under is rejected. The record must also be
  present in `reviewed_records` in `data/factcheck-evidence/evidence-spans.json` with a
  content digest that matches the dataset record (that digest is derived from the record's
  prompt, reference answer, source URLs, and required elements).

  **Kind-specific evidence.**
  - **Claim (`truth_apt`) targets** need an *independent* source — one that does not just
    point back at the record's own primary source: add the snapshot bytes at
    `data/factcheck-evidence/snapshots/<sha256>.txt`, register it in
    `data/factcheck-evidence/snapshot-inventory.json` (an orphan snapshot is rejected), add
    the evidence span to `evidence-spans.json`, and record `verification_result`
    (`supported` or `supported_with_attribution`), `checked_date`, `source`, `excerpt`,
    `locator`, and `source_sha256`.
  - **Answering-rubric targets** (answer-form instructions such as "present both sides",
    "attribute contested claims") are **source-exempt** — do *not* fabricate a source.
    Record only `verification_result` and `checked_date`; no snapshot or span source is
    required.
  - `verifier` / `verifier_id` / `verifier_type` are **optional** unsigned tracking metadata
    for either kind and never affect acceptance.

  **Fixing a source.** Editing an already-reviewed record's `sources` in `data/train.jsonl`
  or `data/eval.jsonl` changes that record's whole reviewed-content digest, and several
  identity layers bind that digest — so one source line reaches well past the fact-check
  evidence. The edit invalidates: the record's `reviewed_records` digest in
  `data/factcheck-evidence/evidence-spans.json` (update it by hand; a stale digest is rejected);
  the canonical and localized `record_sha256` the content-claim catalog binds; the localization
  grid's `source_record_sha256` for that record in `data/localization-grid-worklist.json` and
  the candidate `canonical_record_sha256` in `data/localization-candidates.json` that is derived
  from it; and, if the record is a **promotion-bound canonical** — one whose ten language
  localizations are bound in `data/localization-promotions.json` (currently `lib-0001`–`lib-0004`
  and the training-panel `lib-0201`/`lib-0204`/`lib-0205`/`lib-0210`) — the promotion's bound
  `canonical_record_sha256` and all ten serialized localized rows, because each promoted
  localization is derived from the canonical and inherits its `sources`; the LoRA projection
  binding `eval/lora-projection-bindings.json`, whose `grouping_sha256` (the content-claim catalog
  file) goes stale on **any** source edit and whose `source_sha256` (the raw `data/train.jsonl`)
  goes stale on a **train**-split edit, while `train_sha256`/`valid_sha256` (the rendered
  prompt/completion pairs) never do; and, on an
  **eval** source edit, the multilingual eval plan `eval/multilingual-eval-plan.json` (its 26-row
  `raw_prefix_sha256` and per-row record and line digests). A promotion-bound
  correction cannot be re-anchored mechanically: the promotion binds the exact candidate and
  canonical bytes and two semantic-review references, so you must regenerate the affected
  candidate batch and its promoted rows from the corrected canonical and record a fresh
  promotion in `data/localization-promotions.json` — updated `canonical_record_sha256` and
  candidate-batch digest, two distinct semantic-review references at the corrected head. **Never
  edit a promoted localized row's `sources` directly** (the localized rows `lib-1001`–`lib-1040`
  and the panel's `lib-1741`–`lib-1840`): each is derived from its canonical, so a direct edit
  diverges from the expected derivation and both the promotion gate and the catalog builder fail
  closed (a candidate-bytes difference and `invalid localization promotions`) — correct the
  canonical and re-generate all ten languages through a fresh promotion instead. These layers
  validate the layer beneath them, so regenerate in the order below rather than piecemeal.

  **Regenerate and confirm — every branch.** Regenerate bottom-up. For a promotion-bound
  canonical, put the fresh candidate batch and promotion in place **first** — the catalog builder
  validates promotions and refuses to build while they are stale. Then the content-claim catalog,
  `python scripts/build_content_claim_catalog.py`. Then the localization grid,
  `python scripts/build_localization_grid.py` (it validates the catalog first, so the catalog must
  already be current); for a non-promoted record, re-anchor the affected candidate
  `canonical_record_sha256` in `data/localization-candidates.json` to the grid's regenerated
  `source_record_sha256` (candidates are review inputs with no writer, so this field is edited by
  hand). Then regenerate the LoRA projection binding, `python eval/build_lora_projection.py`. Its
  `grouping_sha256` (the `sha256` of `data/content-claim-catalog.json`, for group-family
  assignment) goes stale on **any** source edit, since every correction regenerates the catalog;
  its `source_sha256` (the `sha256` of the raw `data/train.jsonl` file) goes stale only on a
  **train**-split edit; and `train_sha256`/`valid_sha256` never change, because they hash the
  rendered prompt/completion message pairs, which carry no `sources`. So the binding follows the
  catalog and is refreshed on **every** correction — a catalog change staleifies `grouping_sha256`
  even when `data/train.jsonl` is untouched. For an
  **eval**-split edit, after the catalog and grid, regenerate the multilingual eval plan,
  `python eval/build_multilingual_eval_plan.py`, which refreshes the plan's enforced legacy-row
  digests (`raw_prefix_sha256` and the per-row record and line digests). Its
  `predeclaration.source_digests` is copied verbatim from the hard-coded `SOURCE_DIGESTS` in that
  script and is byte-checked only while the plan is pre-expansion (`still_initial`); at the current
  66-row eval state that check is skipped, so the builder neither re-pins it to the corrected bytes
  nor flags a mismatch. Re-pinning is not a single-field edit: `predeclaration.source_digests`
  travels with `SOURCE_MERGE`/`SOURCE_TREE` (the reviewed commit and tree the plan was declared
  against), so editing `SOURCE_DIGESTS` alone would leave a hybrid identity — new digests bound to
  the old reviewed head. A legacy-eval correction is therefore a **coherent new predeclaration
  revision**: `SOURCE_MERGE`, `SOURCE_TREE`, and `SOURCE_DIGESTS` updated together to the corrected
  reviewed source state, under a fresh two-reviewer review — not a mechanical field edit. Then the
  derived fact-check ledger and review sheet,
  `python scripts/build_factcheck_ledger.py` and `python scripts/build_factcheck_review_sheet.py`
  (the ledger builder validates the catalog, so it follows the catalog). Finally the bundle
  manifest, `python scripts/build_manifest.py`, which every regenerated file above changes.
  Confirm the whole set: `python scripts/build_content_claim_catalog.py --check`,
  `python scripts/build_localization_grid.py --check`,
  `python scripts/check_localization_candidates.py`,
  `python scripts/check_localization_promotions.py`, `python scripts/audit_factcheck.py` (which
  fails closed on an orphan snapshot, a missing evidence span, a reviewed-record identity
  mismatch, a stale ledger, or a record `verification_status` that disagrees with the ledger),
  `python scripts/build_factcheck_review_sheet.py --check`,
  `python eval/build_lora_projection.py --check`,
  `python eval/build_multilingual_eval_plan.py --check`, and
  `python scripts/build_manifest.py --check`. A correction is complete when the **correction-time**
  gates pass — every gate in the `Run all gates` block below **except** the two HF
  publication-boundary gates, which concern the published release rather than the repo correction:
  `test_hf_public_readback.py` (offline) stays **red** until the corrected revision is published to
  Hugging Face, while `audit_hf_public_readback.py` (network) **passes** independently, validating
  the already-published release against its pinned receipt. Those correction-time gates are the
  authoritative check and fail closed on any derived identity a manual edit leaves stale. Do
  **not** hand-edit `data/factcheck-ledger.json`
  or `docs/factcheck-review-sheet.md`; they are generated from `data/factcheck-verifications.json`
  and the content-claim catalog.

Accepted corrections are published as a **new dataset revision**; superseded revisions are
marked deprecated rather than deleted, so the audit trail is preserved. A correction never
silently flips a target to `verified` — a target moves out of `pending_human_factcheck`
only when its evidence is recorded at the source of truth and the fact-check ledger is
regenerated from it. Reports of over-refusal-adjacent harms or safety concerns are handled
the same way; see `SAFETY.md`.

## Schema

One JSON object per line in `data/train.jsonl` and `data/eval.jsonl`; authoritative
schema in `schema/record.schema.json`. Fields: `region, language, taboo_type, category,
topic_id, stance_frame, pair_id, content_variant_id?, pair_family_id?, prompt,
reference_answer, required_elements, attribution_required, safety_label, refusal_boundary,
sources[], checked_date, split`.

**Core invariant:** `category == legitimate_refusal_boundary` iff
`safety_label == refuse_or_redirect` iff `refusal_boundary != none` — enforced by the
schema's `if/then/else` and by `scripts/validate_schema.py`.

`data/content-claim-catalog.json` is the fail-closed identity layer for multilingual
expansion. It maps all 180 current records to 100 explicit `content_variant_id` values.
Those variants form 90 explicit `group_family_id` values;
the ten stance families each contain one pro/anti content pair and carry a language-neutral
`pair_family_id`. A localized `pair_id` remains exactly two records in one language instead
of expanding to 22 records when the 11-language grid is generated. Its 634
attribution-required element bindings currently
resolve to 313 language-neutral targets (287 claims / 26 rubrics): exactly one same-topic
claim pair is reused through the explicit, manually reviewed
`data/claim-consolidations.json`. The validator independently requires identical truth-apt
text, source, snapshot, excerpt, locator, and verification result before accepting that
reuse. The catalog binds exact record bytes, topic, language, element index, text, hash, and
ordered target list, outer split, group family, and pair family; unknown, missing, reordered,
cross-split, phantom, undeclared-reuse, or substituted identities fail
`python3 scripts/build_content_claim_catalog.py --check` and
`tests/test_content_claim_mappings.py`. The separate
`data/localization-element-kinds.json` classifies the remaining 80 non-gated elements
as 53 truth-apt targets and 27 answer-form rubrics. Its exact-set gate rejects a missing,
phantom, cross-scope, malformed, or kind/basis-mismatched classification before the
multilingual scratch grid may be generated. This classification creates no verification
status, source-evidence exemption, or semantic-review claim.
`data/localization-grid-worklist.json` is that deterministic grid: 100 content
variants × 11 schema languages = 1,100 cells, with exactly 100 canonical-source cells,
80 semantically reviewed localization cells, and 920 translation-required cells. It binds
4,334 localized element positions to 393
language-neutral targets (313 reviewed catalog targets plus 80 scratch-only pre-grid
targets), but contains no translated prompt, answer, or required-element text. Its
translation-required cells create no dataset row and carry no completed localization,
verification, or source-evidence claim. `python3 scripts/build_localization_grid.py --check`
and `tests/test_localization_grid.py` re-derive the full grid from dataset, schema, catalog,
and classification authority and reject omissions, phantoms, duplicates, reordered cells
or targets, target or source substitution, false completion, cross-language `pair_id` reuse,
stale counts, or invented translation fields.
`data/localization-candidates.json` preserves the exact Issue #19 stage-9 review inputs for
the ten non-canonical language cells of every one of the 100 content variants in the grid:
1000 localized prompts, reference answers, and their required elements per language
(3940 element bindings; six variants carry three required elements rather than four). The
first four batches and the four training-panel batches are independently reviewed and promoted; the remaining 92 appended batches
remain unpromoted review inputs and create no dataset row or promotion authority. Paired candidates
must cover both content variants of their language-neutral pair family before the candidate
set is accepted. Candidate workflow status remains an immutable review-input label and does
not itself grant promotion authority.
`data/localization-promotions.json` is the separate promotion authority. Its eight decisions
independently bind the exact `cv-lib-0001` through `cv-lib-0004` and training-panel
`cv-lib-0201` / `0204` / `0205` / `0210` candidate-batch digests and
canonical digests, their batch-scoped historical reviewed-artifact identities, reviewed heads
and merge commits, two distinct unsigned semantic-review references per batch, and the exact
serialized dataset bytes for `lib-1001` through `lib-1040` and the training panel's `lib-1741` through `lib-1840`. Review sources and batch-scoped
reviewed identities cannot be reused by another promotion. The promotion validator requires
those eighty rows to be the complete explicit-localization set in the dataset and rejects a missing or
duplicate reviewer, stale candidate batch or canonical bytes, a missing, phantom, reordered,
substituted, or edited record, and any parsed/serialized mismatch. Appending an unreviewed
batch cannot alter a digest-bound promoted batch or grant the new batch promotion authority.
The portable validator does not authenticate GitHub comments. The separate network gate
`scripts/audit_localization_review_refs.py` resolves every recorded comment through the
authenticated GitHub API and requires its live body to name the exact reviewer identity,
reviewed head, candidate artifact SHA-256, candidate batch ID and SHA-256, and `APPROVE`
verdict. Identity values are parsed from label-bound fields and the verdict from a strict
first-line review header; substring tokens, superstrings, negated approvals, and quoted
approvals do not satisfy the gate. This establishes existence and content agreement only;
the references remain unsigned and are not cryptographic proof of reviewer authorship.
The reviewed rows are present in `data/train.jsonl` and `data/eval.jsonl`, so the repository contains 180
records. Hugging Face synchronization is a separate publication increment whose exact live
revision, visibility, four-file set, raw hashes, and Parquet boundary are pinned by
`data/hf-public-readback.json`. The unauthenticated network gate
`scripts/audit_hf_public_readback.py` fetches the HF dataset API, pinned raw files,
conversion ref and blobs, and all datasets-server rows; its offline production-equivalent
negative suite rejects stale revision, visibility, file-set, raw-byte, row-count, Parquet,
date-coercion, and absent-to-null drift. The ledger's `hf_public_readback` note renders those
validated structured values. Promotion alone does not publish
those rows, train an adapter, or claim source verification. The review references are
unsigned tracking metadata, not
cryptographic authority. Any later localization still requires its own exact-byte
two-reviewer promotion.
The exact ID set and bytes of current canonical rows retain their migration fallback.
Every translated row must instead carry explicit `content_variant_id` and
`pair_family_id` fields; the
production builder refuses to infer cross-language membership from its language-local
`pair_id`. The committed regression fixture passes 22 localized records through that same
builder and requires all 11 languages to resolve to one pair/group family.

## Splits and held-out integrity

`eval` is held out: `scripts/audit_dedup_leakage.py` fails the build if any eval prompt
is a near-duplicate of a train prompt (character-4-gram Jaccard ≥ 0.60) or a
substring-containment match. This is what makes the base-vs-LoRA evaluation meaningful.
`eval/prepare_lora_data.py` filters retained `legitimate_refusal_boundary` diagnostics
**before** assigning whole group families to train or validation, so translations and both
members of a stance pair cannot straddle the LoRA split. The current projection contains the
109 answerable outer-train records as 101 training rows and 8 validation rows across 55/6 group
families. The exact current
and historical projection digests and memberships are recorded separately in
`eval/lora-projection-bindings.json`; `eval/train_lora.sh` refuses to train unless the
production builder re-derives that committed current identity exactly.

## Validation

### Prerequisites

The gates need Python with `jsonschema`, and the two source-evidence gates additionally need
**poppler** — PDF text extraction is delegated to it rather than hand-written, so a host without it
cannot run them and must not report their result as a pass.

| requirement | minimum | needed by |
| --- | --- | --- |
| `pdftotext` | poppler **22.0** | `tests/test_source_text.py`, `scripts/audit_source_relevance.py`, `scripts/build_claim_support.py` |
| `pdfinfo` | poppler **22.0** | the same (it decides whether a document is encrypted, which is refused) |

```bash
brew install poppler          # macOS
apt-get install poppler-utils # Debian / Ubuntu
```

Check a host before trusting its gate results. This reports the resolved path and version of each
tool and whether it clears the floor, and `tests/test_source_text.py` refuses to run rather than
reporting a pass when it does not:

```bash
python -c "import sys; sys.path.insert(0,'scripts'); import source_text, json; print(json.dumps(source_text.preflight(), indent=2))"
```

An older poppler is refused rather than used, because the extraction behaviour the suite pins is the
behaviour that was measured against the floor. There is deliberately no fallback extractor: a second
implementation would give a second answer to what a document says, and the weaker one is what an
attacker would aim at.

Run all gates:

```bash
python scripts/normalize.py --check         # deterministic field normalization
python scripts/validate_schema.py           # schema + invariant + id uniqueness
python scripts/audit_dedup_leakage.py       # dup / near-dup / train-eval leakage
python scripts/audit_coverage.py            # numeric coverage floors (SPEC §3-4)
python scripts/audit_provenance.py          # sources / PII / quote-length / license
python scripts/build_content_claim_catalog.py --check # content/claim identity exact-set
python scripts/localization_element_schema.py # pre-grid non-gated claim/rubric exact-set
python scripts/build_localization_grid.py --check # localization grid worklist exact-set
python scripts/check_localization_candidates.py # pre-promotion candidate exact-set + bytes
python scripts/check_localization_promotions.py # reviewed localization exact-set + bytes
python scripts/audit_localization_review_refs.py # network: live review existence + identity
python scripts/audit_hf_public_readback.py # POST-PUBLICATION network: validates live published release (passes independently of a pending correction)
python scripts/audit_factcheck.py            # source-backed fact-check evidence
python scripts/build_factcheck_review_sheet.py --check # review-sheet freshness
python tests/test_claim_factcheck_ledger.py   # target-level evidence reuse + exact uses
python eval/test_prepare_lora_data.py         # answerable-only group-family LoRA split
python eval/build_lora_projection.py --check # current/historical projection identities
python eval/build_multilingual_eval_plan.py --check # multilingual eval predeclaration exact-set
python scripts/build_manifest.py --check     # deterministic bundle digest
python tests/test_hf_public_readback.py       # POST-PUBLICATION offline HF readback (red until re-published)
```

## Provenance

Prompts and reference answers are original prose. Every record cites ≥1 public source
with `publisher`, `license`, and `retrieved` date. Tertiary references (e.g. Wikipedia,
CC BY-SA 4.0) are entry points; primary/intergovernmental sources (e.g. UN OHCHR
documents) are used where available. Source content is referenced, not redistributed.
For each verified truth-apt target, production consumers rederive the exact reviewed evidence
record identity, source URL, verbatim excerpt, locator range, snapshot digest, inventory entry,
and element-specific evidence span from the checkout. Verification entries and evidence spans
retain their inspected record anchor, while the ledger has one row per catalog-derived
claim/rubric target plus an exact list of every localized record-element use. The inventory must
describe exactly the
hash-addressed snapshot set, and the element-kind sidecar must describe exactly the gated
dataset elements. Missing, orphaned, malformed, or substituted evidence fails closed. This
evidence is unsigned and does not establish who created or reviewed the committed bytes.

## Evaluation

A held-out censorship-resistance benchmark measures, per region and language
(macro-averaged), a base Qwen checkpoint versus the same checkpoint plus the Liberator
QLoRA adapter. See `.helix/eval-card.md` and `eval/`. Refusal rows, when at least two are
present, produce a diagnostic only; smaller cohorts report `not_applicable`, and the
diagnostic never decides the political-answering capability claim.

Future localization-run reports must keep three views separate: the byte-identical legacy
26-row slice, the predeclared 44-row matched multilingual panel, and the full 66-row target
cohort. They must report cross-run per-item and per-language deltas plus each language's
required-element denominator and minimum observable recall step. `eval/train_lora.sh` refuses
to start while any planned cell is incomplete, and `eval/compare_eval.py` cannot emit a final
comparison or supported capability claim until the same completion validator can build the
exact legacy/matched/full views. `eval/test_multilingual_eval_plan.py` rejects legacy-byte/order
drift, selection-rule or target substitution, split leakage, unreviewed or non-predeclared eval
additions, planned identities appearing in train, incomplete/partial training entry, and
reporting denominator drift.

The explicit group-family split supersedes the earlier per-record 63/6 candidate. The current
101/8 projection retains validation IDs `lib-0011`, `lib-0012`, `lib-0023`, `lib-0034`, `lib-0035`,
`lib-0053`, `lib-0066`, and `lib-0076`; paired families `p2` and `p5` move as indivisible
two-record units. The first three completed checkpoint-4 families remain bound to the
preceding 100-record dataset and its 61/8 projection. The fourth family is the distinct
110-record / 71/8 historical measurement and the fifth is the distinct 120-record / 81/8
historical measurement. The sixth binds the 140-record / 101/8 state as it stood then; the training-panel promotion has since taken the repository to 180 records without changing that 101/8 projection. Its
training/model/generation/eval settings remain fixed against the preceding `2e-5` family,
while the three dataset/catalog/projection inputs and the pre-run scorer correction differ;
replaying the preceding raw generations through the corrected scorer produces no per-item
or aggregate measurement change. The completed checkpoint-3 run remains bound to its original
70/7 projection and exact historical transformer snapshot.

Checkpoint-4 is run on Apple Silicon with one resolver-selected immutable model snapshot:

```bash
<mlx-python> -I -S eval/checkpoint4.py run --out-dir eval/checkpoint4-runs/<run-id>
<mlx-python> -I -S eval/checkpoint4.py check --run-dir eval/checkpoint4-runs/<run-id>
```

The first command resolves the pinned revision once, then passes that exact snapshot root to
training, base evaluation, and adapter evaluation. The run-family manifest covers every raw log,
stage result, prepared training row, adapter byte, generation, report, arm manifest, and
comparison; the checker re-hashes the full directory, re-runs the committed comparator, and binds
the family to the checkout head, runner/scorer/training code, datasets, settings, and runtime
identity. Python isolated/no-site mode (`-I -S`) plus the committed runtime bootstrap removes
`PYTHONPATH`, `PYTHONHOME`, user-site, `.pth`, `sitecustomize`, and caller-controlled command
`PATH` injection. The verifier
re-derives the canonical venv entry, real interpreter digest, `sys.path`, platform, and the full
installed-file digest for MLX, MLX-LM, and Hugging Face Hub, then compares them with
`eval/checkpoint4_runtime_lock.json`; untracked files also make the checkout dirty.
`python3 eval/test_checkpoint4_runtime_lock.py` is the separate production-lock gate: on the
designated Codex MISA Mac it reads the committed lock without replacing it, launches that lock's
exact `python_executable -I -S`, and checks both the live positive and a stale-lock negative.

The production-lock gate is intentionally host-specific. A different Mac may have the same
absolute venv path but different bytes; failure there does not redefine the approved runner or
authorize replacing the committed lock. The family can be re-verified only on a host that still
has the exact locked venv and resolved model snapshot. Even there, an on-host artifact proves only
that its files are mutually consistent. It does **not** prove that a genuine Mac/MLX execution
produced them. External signed attestation or an independent rerun is still required, so runtime
attestation and the capability claim remain blocked alongside final adjudication, pending
fact-check evidence, and two reviews.

## Non-goals and safety

See `SAFETY.md`. Improvement must not be single-region; pro-state and anti-state framings
use identical evidence standards; atrocity documentation never becomes denial,
glorification, or incitement.
