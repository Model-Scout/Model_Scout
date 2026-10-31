---
pretty_name: LG Long-tail Data Selection Experiment Archive (2026-08-29)
license: other
task_categories:
  - text-generation
language:
  - en
  - ko
tags:
  - data-selection
  - convfinqa
  - lora
  - exaone
  - reproducibility
---

# LG Long-tail data-selection experiment archive

This public repository is the canonical, self-contained archive for the ConvFinQA
data-selection budget-scaling experiments started on 2026-08-29 and the preceding
diversity reproduction run started on 2026-08-26. It replaces the earlier split
model/subset repositories.

The archive preserves the local directory trees in full: selected subsets,
selection manifests, LoRA adapters, DeepSpeed optimizer states, trainer states,
logs, raw Core16 evaluation artifacts, aggregate reports, and reproducibility
metadata. The large optimizer-state directories are intentionally included so a
checkpoint can be resumed rather than used only for inference.

## Experiment question

The main question is whether accuracy-, diversity-, anti-diversity-, and random
selection retain similar behavior as the selected-data budget changes. The
budget-scaling runs use 5%, 10%, and 50% subsets where available. Training is
controlled at three epochs so smaller subsets are not exposed to a fixed number
of optimizer steps many more times than larger subsets.

## Archive layout

```text
README.md
analysis.md
integrated_experiment_results_grouped_highlighted.xlsx
checkpoint_results.csv
checkpoint_results.json
data_selection_budget_scaling_20260829/
  archive_tools/build_archive_index.py
  datasets/                     # selected JSONL subsets and selections
  training/                     # adapters plus resumable DeepSpeed checkpoints
  evaluation/core16/            # raw outputs, logs, report.json, report.md
  hub_export_subsets/            # historical export staging for non-random subsets
data_selection_repro_20260826/   # preceding diversity reproduction run
archive_manifest.json
```

At archive creation time the two source trees contained approximately 100.2 GB
across 1,399 files. The machine-readable manifest records the final uploaded
paths, sizes, and SHA-256 hashes for small/critical files.

## Training contract

| Item | Setting |
|---|---|
| Base model | `LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct` |
| Training | LoRA SFT |
| Learning rate | `2e-5` |
| GPU count | 1 |
| Per-device batch | 4 |
| Gradient accumulation | 4 |
| Effective batch | 16 |
| Train seed | 42 |
| Budget-scaling duration | 3 epochs |
| Checkpoint cadence | 1, 2, and 3 epochs |
| Evaluation | Core16 grouped into Target, SDST, DDST, SDDT, Essential |

The exact subset checksum, step schedule, model path, and recorded Git SHA are in
each run's `run_preflight.txt`. Two preflight files have an empty `git_sha`; the
archive reports this as unknown rather than inventing provenance. Most other runs
record `bf85d17a6139462ebe97c967a91943ce59f0f963`.

## Final three-epoch Core16 results

Values below are unweighted group macro averages. Higher is better.

| Method | Budget | Step | Target | SDST | DDST | SDDT | Essential |
|---|---:|---:|---:|---:|---:|---:|---:|
| Accuracy-medium | 5% | 102 | **0.6029** | **0.1857** | **0.5559** | 0.3506 | 0.7905 |
| Diversity-v2 | 5% | 102 | 0.5884 | 0.1815 | 0.5487 | 0.3501 | **0.7953** |
| Anti-diversity | 5% | 102 | 0.5003 | 0.1691 | 0.5246 | 0.3475 | 0.7890 |
| Random (seed 42) | 5% | 102 | 0.5485 | 0.1631 | 0.5475 | **0.3596** | 0.7926 |
| Accuracy-medium | 10% | 204 | **0.6414** | 0.1849 | 0.5466 | **0.3528** | **0.7951** |
| Diversity-v2 | 10% | 204 | 0.6222 | 0.1837 | 0.5446 | 0.3465 | 0.7690 |
| Anti-diversity | 10% | 204 | 0.5630 | 0.1626 | 0.5250 | 0.3511 | 0.7797 |
| Random (seed 42) | 10% | 204 | 0.6332 | **0.1997** | **0.5578** | 0.3503 | 0.7843 |
| Diversity-v2 | 50% | 1020 | 0.6937 | **0.2073** | 0.5207 | 0.3471 | 0.7352 |
| Anti-diversity | 50% | 1020 | 0.6648 | 0.1983 | 0.5236 | **0.3635** | **0.7906** |
| Random (seed 42) | 50% | 1020 | **0.6951** | 0.2067 | **0.5488** | 0.3383 | 0.7674 |

Accuracy-medium 50% was not run. Random intermediate checkpoints were retained
but only the final three-epoch checkpoint was evaluated.

## Important evaluation correction

The original Diversity-v2 10% step-204 report contains invalid zero DDST scores
caused by an evaluation/cache failure. The canonical DDST macro is **0.5446** from
`evaluation/core16/diversity_v2_cr0.01_ratio0.10/step204_ddst_retry1/report.md`.
The workbook and machine-readable indexes apply this correction while preserving
both original artifacts.

## Result interpretation

- Target performance rises with budget for diversity, anti-diversity, and random.
- Accuracy-medium is strongest on Target at 5% and 10%.
- At 50%, random and diversity-v2 are effectively tied on Target (difference 0.0014).
- Anti-diversity is consistently weaker on Target at matched budgets.
- DDST changes relatively little with budget, while some SDDT/Essential results
  suggest a specialization trade-off at larger budgets.
- Accuracy-medium versus diversity overlap is close to an independent random
  expectation. The methods can therefore achieve similar performance while
  selecting mostly different examples.
- These are primarily one-seed comparisons. They show tendencies, not stable
  estimates of method superiority.

See `analysis.md` and the Excel workbook for checkpoint-level values, overlap
counts, caveats, and provenance.

## Download and use

Download the complete dataset repository:

```python
from huggingface_hub import snapshot_download

root = snapshot_download(
    repo_id="Jongbin-kr/lg-longtail-data-selection-experiment-archive-20260829",
    repo_type="dataset",
)
```

For inference, point PEFT/vLLM to a checkpoint directory containing
`adapter_config.json` and `adapter_model.safetensors`. For exact training resume,
also retain the corresponding `global_step*/` DeepSpeed state and
`trainer_state.json`.

## Provenance and limitations

- Repository at archive time: `/data6/jongbinwon/lg_longtail`
- Archive-preparation branch/HEAD: `jb/add-essential-nq-kmmlu` /
  `d763bd8fa8cf7d32ef8edd96c9b19a5684b44828`
- The worktree was dirty during archive preparation. The experiment artifacts
  retain their own preflight metadata; the archive-preparation HEAD must not be
  mistaken for the training commit.
- Hub repository visibility is public.
- Evaluation reports are authoritative for metric values; the Excel file is an
  index and analysis convenience layer.
