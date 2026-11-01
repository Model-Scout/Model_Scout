---
license: other
language:
- en
- ko
- sw
tags:
- code-switched-rlvr
- val_generations
- reasoning
- evaluation
size_categories:
- 100K<n<1M
---

# Code-Switched RLVR — Validation Generations

Validation-set generation dumps for the 4 RLVR model groups in our
Code-Switched RLVR analysis. Distributed as raw jsonl, **path-compatible with
the original on-disk layout** used by our analysis code.

**This dataset is private.** Reviewers should request access from the maintainer
and then export a read-scoped `HUGGINGFACE_HUB_TOKEN` before downloading.

External users running the analysis suite can:

```bash
# (0) Auth (token with read scope on this repo):
huggingface-cli login         # or: export HUGGINGFACE_HUB_TOKEN=hf_...

# (1) Download to a local dir
huggingface-cli download navvh/cs-rlvr-val-generations --repo-type dataset \
    --local-dir $HOME/cs_rlvr_val_gen

# (2) Point the analysis suite at it (in analysis_paper/.env)
GG_KO_VG_ROOT=$HOME/cs_rlvr_val_gen/hf_valgen
GG_SW_VG_ROOT=$HOME/cs_rlvr_val_gen/sw-cyber-smollm
GG_MED_VG_ROOT=$HOME/cs_rlvr_val_gen/qw25-med
GG_LCMED_VG_ROOT=$HOME/cs_rlvr_val_gen/lc-med
GG_SW_CYBER_ROOT=$HOME/cs_rlvr_val_gen/sw-cyber-smollm
GG_QW25_MED_ROOT=$HOME/cs_rlvr_val_gen/qw25-med
GG_LC_MED_ROOT=$HOME/cs_rlvr_val_gen/lc-med
```

## Contents

| Family | Path | Files | Group |
|---|---|--:|---|
| KO smollm3 cyber (5 RLVR variants + Base) | `hf_valgen/` | 6 | representation, gemba_mtq |
| SW smollm3 cyber (5 RLVR variants) | `sw-cyber-smollm/` | 10 | surface_alignment, gemba_mtq |
| Qwen2.5 medical KO (5 RLVR variants) | `qw25-med/` | 5 | surface_alignment, gemba_mtq |
| Llama-3.2 medical KO (4 RLVR variants) | `lc-med/` | 4 | surface_alignment, gemba_mtq |

Best steps (per group) match the analysis suite's `STEP_FILES` /
`SW_VG_PATHS` / `MED_VG_PATHS` / `LCMED_VG_PATHS`.

## Schema

Each jsonl row is one validation example. Common keys:

- `input` — fully-rendered chat prompt (system + user + assistant scaffold)
- `output` — model generation (may include `<think>...</think>` block)
- `gts` — ground-truth answer letter (`A`/`B`/`C`/`D`) for MCQ benches
- `acc` — boolean correctness (parsed by the training pipeline)
- bench metadata depends on the source training run

The SW family ships two files per variant: ``val_generations_step<N>.jsonl``
(English side) and ``val_generations_step<N>_sw.jsonl`` (Swahili side).

## Related

- Code: <https://oss.navercorp.com/HyperscaleAI/cs-golden-goose> (private)
- Analysis: see [`analysis_paper/`](https://oss.navercorp.com/HyperscaleAI/cs-golden-goose/tree/main/analysis_paper)
- Companion ckpts (KO group only): `navvh/{mono_en,mono_ko,bi_mono_mix,crosslingual_full_mix,6way_cs,cs_only}_smollm3-3b`
