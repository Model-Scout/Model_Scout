---
language:
- en
- ko
tags:
- robotics
- interpretability
- sparse-autoencoder
- openvla
- libero
pretty_name: Event-SAE Head full10 completed experiment
---

# Event-SAE Head: completed LIBERO-Spatial experiment

This public release preserves **3600 completed rollouts**, 18 conditions,
200 paired evaluation cases and 16 ablated features.
The model and SAE were frozen. These are post-pilot follow-up results, not a fully held-out confirmatory study.

## Read results immediately

- [Main report](reports/report.md)
- [Task 0–1 and task 2–9](reports/task_groups_v1.md)
- [Machine-readable summary and actual timings](reports/summary.json)
- [Every evaluated episode](reports/episodes.csv)
- [Paired effects](reports/paired_effects.csv)
- [Predictor comparison](reports/predictor_comparison.csv)

The reports contain the measured Head-KL/Event results and their scope. Positive drop means
success deteriorated after removing a feature; values multiplied by 100 are percentage points.
Top-3 mean drop averages three **separate single-feature interventions**, not one joint intervention.
The archived analysis records the paired bootstrap confidence interval for the method difference.

## What is preserved

`experiment.tar.gz` contains the complete original result directory (all conditions, per-episode
results, action sequences, logs, scores, readout cache, head bundle, parity certificates, plan and
analysis), the complete generated `head-inputs/full10` metadata/input directory, and the exact
local experiment YAML (checked against the frozen normalized configuration hash).
Original documents are unchanged, including their historical absolute paths.

The archive also contains the exact source at commit `8924a8d9b62edb16d261785cbc2124729017f2b1`,
public input repositories and pinned revisions, and an export-time package/GPU environment snapshot.
The summed recorded condition runtimes are **40.877 hours**. This is not an independently measured
Pod wall-clock duration or bill: preprocessing, downloads, analysis and idle time are separate.

Source public dense activations, full model weights, inherited TopK tensors and the SAE checkpoint
are referenced by pinned revisions/checksums, not duplicated in this release. The exact download
scripts are in the archived source. Videos are included only if they were actually saved;
the full10 preset disables new rollout video recording.

## Download, verify and restore anywhere (no GPU or model needed)

Install the Hugging Face CLI, then download the release. For citation/reproducibility use
`--revision <dataset-commit>` with the commit displayed in the Hugging Face Files history.

```bash
hf download jiyeony/event-sae-head-full10-results --repo-type dataset --local-dir ./head-full10
python ./head-full10/tools/headbundle.py verify --bundle ./head-full10
python ./head-full10/tools/headbundle.py restore --bundle ./head-full10 --destination ./head-full10-restored
python ./head-full10/tools/headbundle.py inspect --root ./head-full10-restored/results/full10-followup-v1
```

The tools require Python 3.10+ and its standard library only. Restoration requires a NEW destination.
Verification checks archive and per-file SHA-256, all frozen conditions and cases, original result
fingerprints, saved action hashes/identity, and recomputes observed success-rate drops from episodes.
It does not execute torch/pickle files, replay the simulator, or rerun GPU numerical parity.
The bootstrap intervals are preserved from the original analysis; checking their saved consistency
is distinct from recomputing all bootstrap draws.

`manifest.json` inventories archived files. `SHA256SUMS` inventories every published bundle file
except itself. Verification needs temporary free disk space for the uncompressed archive.
The preserved source archive is `source/experiment-code.tar.gz` after restoration.
To rerun the original analysis/rollouts, use that source, its documented dependencies and original
`/workspace` layout; the portable verifier intentionally does not rewrite provenance-bound paths.

## Research scope

The discovery/evaluation trial lists are separated. The SAE and Event clusters were inherited
from existing data; historical collection state bytes and generation flags are not independently
verified. Task 0–1 informed the earlier pilot. Rankings were computed across all ten tasks, so the
task 2–9 subgroup does not establish held-out-task generalization. Uncertainty is conditional on
the fixed tasks and evaluated feature panel. See the original reports for full limitations.

Only code, scientific artifacts and a curated environment inventory are packaged. Authentication
tokens, shell histories, Hugging Face caches and `.git` directories are not collected.
