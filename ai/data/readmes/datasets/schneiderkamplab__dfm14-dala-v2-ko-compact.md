---
language:
- ko
license: other
license_name: source-specific
license_link: LICENSE.md
task_categories:
- text-classification
- text-generation
configs:
- config_name: acceptability
  data_files:
  - split: train
    path: data/acceptability/train_representative-*.jsonl.gz
  - split: validation_representative
    path: data/acceptability/validation_representative-*.jsonl.gz
  - split: validation_challenge
    path: data/acceptability/validation_challenge-*.jsonl.gz
  - split: test_representative
    path: data/acceptability/test_representative-*.jsonl.gz
  - split: test_challenge
    path: data/acceptability/test_challenge-*.jsonl.gz
- config_name: correction
  data_files:
  - split: train
    path: data/correction/train_representative-*.jsonl.gz
  - split: validation_representative
    path: data/correction/validation_representative-*.jsonl.gz
  - split: validation_challenge
    path: data/correction/validation_challenge-*.jsonl.gz
  - split: test_representative
    path: data/correction/test_representative-*.jsonl.gz
  - split: test_challenge
    path: data/correction/test_challenge-*.jsonl.gz
---
# DaLA v2 — Korean — DFM14 compact audit subset

One language dataset combining all selected base and additive runs. Two task views share the same accepted source records; they are not independent observations. Each independently audited clean control contributes one correct input per task; each passing pair contributes one corrupted input per task. No extra clean controls are synthesized.

| Split/view | Acceptability rows | Correction rows |
| --- | ---: | ---: |
| train_representative | 833,536 | 833,536 |
| validation_representative | 52,323 | 52,323 |
| validation_challenge | 52,207 | 52,207 |
| test_representative | 52,335 | 52,335 |
| test_challenge | 52,366 | 52,366 |

Only completed, correctly formed automated audit passes with a nonempty rationale are included. Flagged, uncertain, failed and otherwise invalid decisions are excluded. Automated Gemma judgments are fallible, not native-speaker validation, and not the producer's isolated-edit certification. Audit filtering changes family counts and class balance; this is not a claim of balanced producer release or gold evaluation data.

Only `messages` are model input, with `target_message_index=1`. Other fields expose labels, full original source text, edits, provenance and audit evidence. Preserve the original validation/test representative/challenge views; only train is integrated into DFM14. Language-specific prompts are preserved.

Source text, titles, URLs, revisions, licenses and transformation spans remain in each row's lossless `provenance_json` (parse with `json.loads`); audit decisions are in `audit_json`. These JSON strings give every shard the same portable Hugging Face schema. Publisher endorsement is not implied. No blanket relicensing: retain applicable attribution/share-alike and source-specific terms in LICENSE.md and row metadata. See metadata/release.json for measured composition, exact-overlap screening and its limits. Both task views reproduce the same source excerpts.
