---
license: cdla-permissive-2.0
language:
- en
- fr
- de
- it
- es
- ja
- zh
- ko
task_categories:
- automatic-speech-recognition
- voice-activity-detection
size_categories:
- 1K<n<10K
tags:
- notsofar
- chime-8
- meeting
- far-field
- multi-microphone
---

# NOTSOFAR-1 — eval splits (mirror)

Mirror byte-exact des 3 splits du dossier `benchmark-datasets/eval_set/` du
repo upstream **`microsoft/NOTSOFAR`** (Vinnikov et al. 2024,
CHiME-8 NOTSOFAR-1 Challenge).

| Split | Files | Size | GT |
|-------|-------|------|-----|
| `240629.1_eval_small`         | 1 360 | 15.4 GB | — (no GT) |
| `240629.1_eval_small_with_GT` | 1 899 | 20.0 GB | ✓ |
| `240825.1_eval_full_with_GT`  | 4 509 | 49.2 GB | ✓ |

**Total : 7 768 files, ~84.5 GB.**

## Structure (préservée à l'identique)

```
benchmark-datasets/eval_set/<split>/MTG/MTG_<id>/
    devices.json
    close_talk/CT_<n>.wav
    <device_array>/...wav
    transcript.json     (si has_gt)
```

## Tâche

NOTSOFAR-1 est un benchmark **DIA + STT joints** sur réunions naturelles
multi-locuteurs en bureau (far-field + close-talk). Métriques de référence :
DER, tcpWER (time-constrained permutation-invariant), SA-WER.

## Source upstream

- Repo : https://huggingface.co/datasets/microsoft/NOTSOFAR
- Paper : Vinnikov et al. *NOTSOFAR-1 Challenge: New Datasets, Baselines and
  Tasks for Distant Meeting Transcription*, ICASSP 2024.
- License : CDLA-Permissive-2.0
