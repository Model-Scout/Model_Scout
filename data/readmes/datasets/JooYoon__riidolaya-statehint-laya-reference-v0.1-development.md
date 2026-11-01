---
license: apache-2.0
language:
  - ko
  - en
task_categories:
  - text-classification
tags:
  - research
  - development
  - aggregate-only
  - frozen-reference
  - laya
  - mps
---

# Riidolaya Statehint frozen Laya reference — development report v0.1

[한국어 보고서](README.ko.md)

**Report-only research release; source CI passed.** No weights, new model,
raw data, features or per-row predictions are included. Formal eligibility was
**not assessed**, and no deployment-qualified teacher was established. These
already-exposed development results did not select or promote an arm.

The practical target is optional progress/completion-report/question hints in
bounded Korean/English development comments. A completion report is a claim
in prose, not verified successful work or authority to change a task. This
package records a frozen pretrained reference rather than training a new hint
model. It performs no annotation, reaction or state mutation.

## What was measured

One FP32 MPS worker used the original frozen **English** Laya checkpoint for
240 input rows /120 paired families /43 declared groups from the previously
exposed V4 validation set. It made one shared backbone forward per row (240
encoder calls). The serialized base and published V1 delta scores were CPU last-linear
computations over those same MPS-captured option features. The full-base native
MPS logits served as parity references. The native-forward timer covers that
full base forward, not an isolated encoder-only benchmark.
Automatic multilingual routing or another language checkpoint was not tested.

The eight output columns match the existing intent IDs: question, blocker,
reference, progress, completion_report, cancel_request, planned and unclear.
However, the inherited V1 instruction/definitions differ from V4's visible-unit
and primary-act rubric. The instruction text, its fingerprint, current input
pins and evaluation sentences are omitted from this package.

There were **zero new training updates**, zero calibration calls, zero final-test
calls, zero selection weight and no promotion. The Go report adapter itself
made zero model calls; the preceding native worker's 240 forwards are recorded
separately. Training-step provenance of the pretrained origins is unknown:
`training_steps_known:false` and `training_steps:null` do not imply an untrained
or freshly zero-initialized head.

## Actual aggregate results

| Frozen origin |Raw eight-intent correct |KO correct /120 |EN correct /120 |Eight-intent NLL |Correct gated /proposed |
| --- | ---: | ---: | ---: | ---: | ---: |
| Original base |89/240 (37.08%) |16 (13.33%) |73 (60.83%) |1.738268 |12/12 |
| Published V1 delta |88/240 (36.67%) |16 (13.33%) |72 (60.00%) |1.616183 |11/11 |

| Frozen origin |KO gated P/C/Q |EN gated P/C/Q |EN correct completion family support |Formal eligibility |
| --- | --- | --- | ---: | --- |
| Original base |0/0/0 |8/4/0 |4/15 |Unassessed |
| Published V1 delta |0/0/0 |7/4/0 |4/15 |Unassessed |

All gated proposals in this observation were correct, but there were no Korean
proposals and no question proposals in either locale. English completion
support is only four of fifteen families. This sparse support does not establish
reliable completion hints or a qualified teacher. Zero-proposal precision is
**undefined**, not0% or100%; the JSON numeric0 sentinel must be read with its
false `precision_defined_pcq` flag. Four correct completion proposals do not
establish100% product completion precision.

Counts use confidence.9 and margin.05, with P/C/Q display candidates and the
other intents yielding no such candidate. Ties follow the frozen intent order
but a zero-margin tie cannot gate. `RESULTS.reference.aggregate.json` preserves
all aggregate confusion, locale/support/coverage/precision fields and NLL.
The `eligible:false` values are accompanied by `eligibility_assessed:false`;
they are not a completed formal eligibility decision. No qualified deployment
or useful teacher has been demonstrated.

The original base temperature is1.0000158548355103, and the inherited V1 delta
temperature is.65. They were not fitted to V4 here. Head origin, temperature and
instruction/rubric compatibility are not isolated. The lower delta NLL therefore
does not establish improved head classification, V4 calibration or task utility;
its raw correct count is one lower.

## Resource observations and their scope

| Observation |Actual value |Scope |
| --- | ---: | --- |
| Whole command wall time |24.24s |Parent-recorded whole pipeline |
| Worker elapsed |23.442346s |Includes setup, runtime/model loading and extraction |
| Native forward total |13.228715s |240 shared backbone forwards |
| Mean native forward |55.119646ms |This run's per-row mean, not serving latency |
| Process peak RSS |2,887,172,096bytes |About2.689GiB /2.887GB decimal |
| Minimum reported available system memory |51% |483 resource observations |
| Sampled MPS allocated maximum |1,688,613,632bytes |Sample maximum, not transient peak |
| Sampled MPS driver maximum |2,166,046,720bytes |Sample maximum, not transient peak |

The worker used MPS/FP32, CPU fallback disabled, one worker and allocator
fraction.25. `RESOURCES.aggregate.json` contains reduced sample counts and
min/max/mean/median values, not the raw resource timeline. MPS allocation and
driver samples overlap process RSS in unified memory: **do not add them**.
Sample statistics are not transient GPU peaks or independent replicates.
The worker and whole-command times have different scopes; native forward time
excludes model loading. Runtime versions and reported token ranges are retained
as reproducibility context.

These are one-workstation observations. They are not a matched latency/memory
comparison with the separate Go training studies, a portable benchmark, or
proof of a low-cost deployment. No new model run was made during staging.

## Exact reference origins and licenses

- [Original Laya base](https://huggingface.co/convaiinnovations/laya/tree/55cf4c4ebb4ebe31b2550e8bdf3bd21b99753851), revision `55cf4c4ebb4ebe31b2550e8bdf3bd21b99753851`; public model SHA256 `891102d372688fc2a094dac56a384bc537b87c63f21f9f3dac0be2b7cbc8d86c`.
- [Published V1 development delta](https://huggingface.co/JooYoon/riidolaya-statehint-laya-scorer-v0.1/tree/e6a8603cd53f1340a97373675dde2fbc31e85fc0), immutable revision `e6a8603cd53f1340a97373675dde2fbc31e85fc0`, tag `statehint-v0.1`; `scorer.safetensors` SHA256 `e7037a4c92460dd0c77facb643a26a2f3ce99240e6a59bd78c15ad91df314fcc`.

These are provenance links; no base/delta weights were downloaded or copied
for staging. The earlier delta is a final-linear modification requiring its
pinned original base, not a standalone model. Its prior notice is preserved in
`DELTA-SOURCE-NOTICE.txt` and describes that separate package.

The exact upstream `BASE-MODEL-CARD.md` is preserved for provenance. Its broad
family, calibration, routing and performance claims are attributed to the
upstream card and do not qualify this English-checkpoint V4 reference.
The base and ModernBERT-large cards declare Apache-2.0; `LICENSE` contains the
full terms, with source attribution in `NOTICE`. Original aggregate data and
report text are Apache-2.0. This records declared source provenance, not an
independent audit of all pretraining data rights. No affiliation is claimed.

## Report files and publication boundary

This is a dataset repository of **aggregate reports**, not training/evaluation
records. Inspect `RESULTS.reference.aggregate.json`, `RESOURCES.aggregate.json`
and `PROVENANCE.json`. No raw corpus, scores, features, model bodies, source
instruction, current input paths/pins, runtime logs or private task text is
included. No inference loader or endpoint is supplied.

After the publisher verifies source CI and the immutable dataset revision,
replace `PUBLISHED_DATASET_COMMIT` with that exact Hub commit:

```sh
hf download JooYoon/riidolaya-statehint-laya-reference-v0.1-development \
  --type dataset --revision PUBLISHED_DATASET_COMMIT --local-dir reference-report
(cd reference-report && shasum -a 256 -c SHA256SUMS)
```

Source [CI](https://github.com/teamswyg/laya-tools/actions/runs/37553334520) passed on Linux and macOS; [PR172](https://github.com/teamswyg/laya-tools/pull/172) automatically merged with the identical tested source tree. Checksums and full immutable dataset readback bind this research report.

Previously exposed synthetic data, AI labels, author/reviewer/topic bias and
prior project history limit conclusions. This is not new human gold, independent
product evaluation, verified task completion or qualification. Current defaults,
original model bytes and older published packages remain unchanged.
